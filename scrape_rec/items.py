import scrapy
from scrapy_jsonschema.item import JsonSchemaItem


class RealEstateRentedApartmentItem(JsonSchemaItem):
    jsonschema = {
        '$schema': 'http://json-schema.org/draft-04/schema#',
        'title': 'Realestate apartment item',
        'description': 'An apartment for rent in Cluj',
        'type': 'object',
        'properties': {
            'fingerprint': {
                'description': 'The unique identifier for a product',
                'type': 'string'
            },
            'title': {
                'description': 'Apartment listing title',
                'type': 'string'
            },
            'price': {
                'type': 'number',
                'minimum': 0,
                'exclusiveMinimum': True
            },
            'currency': {
                'description': 'The creation date of the listing or if not found the scrape date',
                'type': 'string'
            },
            'posted_date': {
                'description': 'The creation date of the listing or if not found the scrape date',
                'type': 'string'
            },
            'description': {
                'description': 'Apartment description',
                'type': 'string'
            },
            'partitioning': {
                'description': 'Apartment sections',
                'type': 'string'
            },
            'surface': {
                'description': 'Surface in mp^2',
                'type': 'string'
            },
            'building_year': {
                'description': 'The building construition date',
                'type': 'string'
            },
            'floor': {
                'description': 'Obvious',
                'type': 'integer',
                'minimum': 0
            },
            'number_of_rooms': {
                'description': 'Obvious',
                'type': 'integer',
                'minimum': 0
            },
            'terrace': {
                'description': 'Has or not terrace',
                'type': 'boolean'
            },
            'parking': {
                'description': 'Has or not parking',
                'type': 'boolean'
            },
            'cellar': {
                'description': 'Has or not cellar',
                'type': 'boolean'
            },
            'source_website': {
                'description': 'The website of origin',
                'type': 'string'
            },
            'source_offer': {
                'description': 'Is or not sold by an agency',
                'type': 'boolean'
            },
            'neighborhood': {
                'description': 'The area',
                'type': 'string'
            },
        },
        'required': ['fingerprint', 'title', 'price', 'posted_date']
    }
