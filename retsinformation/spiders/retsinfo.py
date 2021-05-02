import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from shutil import which
import json
from bs4 import BeautifulSoup

# et lille eksempel :)
class RetsinfoSpider(scrapy.Spider):
    name = "retsinfo"
    start_urls = ["https://www.retsinformation.dk/api/document/eli/lta/2015/2"]

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        json_data = json.loads(response.body)
        soup = BeautifulSoup(json_data[0].get('documentHtml'), 'html.parser')
        print(soup.get_text())
