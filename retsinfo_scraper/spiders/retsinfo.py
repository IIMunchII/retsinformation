import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from scrapy import signals
import json
from bs4 import BeautifulSoup
from retsinfo_scraper.items import RetsinfoItem
from .mixins import RedisMixin
from datetime import datetime

class RetsinfoSpider(scrapy.Spider, RedisMixin):
    name = "retsinfo"
    start_urls = ["https://www.retsinformation.dk/api/document/eli/lta/"]
    year_range = range(1986, datetime.now().year + 1)

    def __init__(self, max_pages=10, *args, **kwargs):
        self.max_pages = int(max_pages)
        super().__init__(**kwargs)

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(RetsinfoSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def start_requests(self):
        for year in self.year_range:
            for i in range(0, self.max_pages):
                if self.no_more_pages(self.get_redis_key(year)):
                    break
                else:
                    yield scrapy.Request(url=self.start_urls[0] + f"{year}/{i}", 
                                         callback=self.parse,
                                         errback=self.errback_set_failure_count,
                                         cb_kwargs={"year":year, "nr":i})

    def parse(self, response, **kwargs):
        item = RetsinfoItem()
        document_data = json.loads(response.body)[0]
        item = self.map_json_to_item(item, 
                                     document_data, 
                                     response.request.cb_kwargs)
        yield item

    def map_json_to_item(self, item, document_data, cb_kwargs):
        item['doc_id'] = document_data.get('id')
        item['title'] = document_data.get('title')
        item['short_name'] = document_data.get('shortName')
        item['document_text'] = self.get_text_from_document(document_data)
        item['document_html'] = document_data.get('documentHtml')
        item['is_historical'] = document_data.get('isHistorical')
        item['ressort'] = document_data.get('ressort')
        item['is_reprint'] = document_data.get('isReprint')
        item['geographic_id'] = document_data.get('geografiskDaekningId')
        item['retsinfo_klassifikation_id'] = document_data.get('retsinfoKlassifikationId')
        item['has_fob_tags'] = document_data.get('hasFobTags')
        item['editorial_notes'] = document_data.get('editorialNotes')
        item['alternative_media'] = document_data.get('alternativeMedia')
        item['metadata'] = document_data.get('metadata')
        item['document_year'] = cb_kwargs.get('year')
        item['document_nr'] = cb_kwargs.get('nr')
        return item

    def get_text_from_document(self, document_data):
        soup = BeautifulSoup(document_data.get('documentHtml'), 'html.parser')
        return soup.get_text()

    def errback_set_failure_count(self, failure):
        year = failure.request.cb_kwargs.get('year')
        if failure.check(HttpError):
            self.no_page_incrementer(self.get_redis_key(year))

    def spider_closed(self, spider):
        key_list = [self.get_redis_key(year) for year in self.year_range]
        self.clear_all_keys(key_list)