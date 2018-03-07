# -*- coding: utf-8 -*-
from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_splash import SplashRequest


class IeeeSpider(CrawlSpider):
    name = 'ieee'
    start_urls = ['https://www.ieee.org/conferences_events/conferences/search/index.html']
    rules = (
        Rule(
            LinkExtractor(allow='/conferences_events/conferences/search/index.html')
        ),
        Rule(
            LinkExtractor(
                allow='/conferences_events/conferences/search/index.html'
            ),
            callback='parse_conference',
            process_request='splash_request'
        )
    )

    def splash_request(self, request):
        return SplashRequest(
            url=request.url,
            callback=self.parse_conference(),
            args={
                'wait': 2,
            }
        )

    def parse_conference(self, response):
        title = response.xpath('//title/text()').extract_first()
        self.log(title)
