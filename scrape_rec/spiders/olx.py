import dateparser
from scrape_rec.spiders.base_realestate import BaseRealEstateSpider


class OlxSpider(BaseRealEstateSpider):
    name = "olx"
    start_urls = ['https://www.olx.ro/imobiliare/apartamente-garsoniere-de-inchiriat/cluj-napoca/',]
    item_links_xpath = '//a[contains(@class, "detailsLink") and not(contains(@class, "detailsLinkPromoted"))]/@href'
    next_link_xpath = '//a[@data-cy="page-link-next"]/@href'
    attributes_mapping = {
        'partitioning': 'Compartimentare',
        'surface': 'Suprafata utila',
        'building_year': 'An constructie',
        'floor': 'Etaj',
        'source_offer': 'Oferit de',
    }
    convert_to_int = ['surface', 'floor']
    title_xpath = '//h1/text()'
    description_xpath = '//div[@id="textContent"]/text()'
    date_xpath = '//em/text()'
    price_xpath = '//div[@class="price-label"]/strong/text()'
    base_floors_mapping = {
        'Parter': 0,
        'Demisol': -1,
    }
    currency_mapping = {
        '€': 'EUR',
        'lei': 'RON',
    }

    def get_attribute_values(self, response):
        attr_table = response.css('table.item')
        return {
            attr.css('th::text').extract_first(): (
                    attr.css('td strong a::text') or attr.css('td strong::text')
            ).extract_first().strip()
            for attr in attr_table
        }

    def process_ad_date(self, ad_date):
        processed_date = ' '.join(ad_date.split()).split(' ', 2)[-1]
        return dateparser.parse(processed_date)

    def process_price(self, price):
        full_price = price.split(' ')
        if not full_price:
            return 0, None
        return int(full_price[0]), self.currency_mapping.get(full_price[1])