import scrapy
from ..items import RentScrapeItem


class RentSpider(scrapy.Spider):
    name = "makaan"
    # start_urls=[]
    # for city in ['chennai','mumbai','pune','hyderabad','bangalore','delhi','ahmedabad','hyderabad','kolkata','surat']:
    #     start_urls.append(f"https://www.makaan.com/{city}-residential-property/rent-property-in-{city}-city")
    start_urls = ["https://www.makaan.com/kolkata-residential-property/rent-property-in-kolkata-city"]

    def parse(self, response):
        items = RentScrapeItem()
        cards = response.css(".cardLayout")
        for card in cards:
            items['title'] = ' '.join([c.get() for c in card.css(".typelink span::text")])
            items['city'] = card.css(".cityName::text").get()
            items['locality'] = card.css(".loclink strong::text").get()
            items['price'] = card.css(".price .val::text").get()
            items['area'] = card.css(".size .val::text").get().strip()
            items['status'] = card.css(".w44 .val::text").get()
            items['deposit'] = card.css(".keypoint strong::text").get()
            items['num_bath'] = card.css(".keypoint:nth-child(2) span::text").get()

            yield items

        next_page = response.xpath("//*/a[contains(@aria-label,'nextPage')]/@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
