import scrapy
import json
from bs4 import BeautifulSoup
from retsinfo_scraper.items import RetsinfoItem


class RetsinfoSpider(scrapy.Spider):
    name = "retsinfo"
    start_urls = ["https://www.retsinformation.dk/api/document/eli/lta/2000/"]

    def start_requests(self):
        for i in range(1, 6):
            yield scrapy.Request(url=self.start_urls[0] + str(i), callback=self.parse)

    def parse(self, response):
        item = RetsinfoItem()
        document_data = json.loads(response.body)[0]
        item = self.map_json_to_item(item, document_data)
        yield item

    # TODO: Convert this part into Item Load class see https://docs.scrapy.org/en/latest/topics/loaders.html
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

    # TODO: Implementer redis til at holde styr på resultatet af iterationer over API-et
    # https://docs.scrapy.org/en/latest/topics/request-response.html#topics-request-response-ref-errbacks
    def errback_control_iter(self, failure):
        pass