import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
import json
from bs4 import BeautifulSoup
from retsinfo_scraper.items import RetsinfoItem
from .mixins import RedisMixin
from datetime import datetime

class RetsinfoSpider(scrapy.Spider, RedisMixin):
    name = "retsinfo"
    start_urls = ["https://www.retsinformation.dk/api/document/eli/lta/"]
    year_range = range(1986, datetime.now().year + 1)
    current_year = 1986
    redis_key = f"{current_year}:failures"

    def __init__(self, max_pages=10, *args, **kwargs):
        self.max_pages = int(max_pages)
        super().__init__(**kwargs)

    def start_requests(self):
        for year in self.year_range:
            self.current_year = year
            for i in range(1, self.max_pages):
                if self.no_more_pages(self.redis_key):
                    break
                else:
                    yield scrapy.Request(url=self.start_urls[0] + f"{year}/{i}", 
                                         callback=self.parse,
                                         errback=self.errback_set_failure_count)

    def parse(self, response):
        item = RetsinfoItem()
        document_data = json.loads(response.body)[0]
        item = self.map_json_to_item(item, document_data)
        yield item

    def map_json_to_item(self, item, document_data):
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
        return item

    def get_text_from_document(self, document_data):
        soup = BeautifulSoup(document_data.get('documentHtml'), 'html.parser')
        return soup.get_text()

    def errback_set_failure_count(self, failure):
        if failure.check(HttpError):
            self.no_page_incrementer(self.redis_key)
