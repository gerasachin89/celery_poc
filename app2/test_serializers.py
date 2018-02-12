from django.test import TestCase
from app2.serializers import *
from decimal import *

class PuppyTest(TestCase):
    def setUp(self):
        self.bike_attributes = {
            'color': 'yellow',
            'size': Decimal('52.12')
        }

        self.serializer_data = {
            'color': 'black',
            'size': 51.23
        }

        self.bike = Bike.objects.create(**self.bike_attributes)
        self.serializer = BikeSerializer(instance=self.bike)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['color', 'size']))

    def test_color_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['color'], self.bike_attributes['color'])

    def test_size_lower_bound(self):
        self.serializer_data['size'] = 29.5

        serializer = BikeSerializer(data=self.serializer_data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), set(['size']))

    def test_float_data_correctly_saves_as_decimal(self):
        self.serializer_data['size'] = 31.7893

        serializer = BikeSerializer(data=self.serializer_data)
        serializer.is_valid()

        new_bike = serializer.save()
        new_bike.refresh_from_db()

        self.assertEqual(new_bike.size, Decimal('31.79'))

    def test_color_must_be_in_choices(self):
        self.bike_attributes['color'] = 'red'

        serializer = BikeSerializer(instance=self.bike, data=self.bike_attributes)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), set(['color']))
