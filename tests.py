import unittest
from check_vat import get_country_code_and_number_from_vat_number


class SeparatingCountryPrefixTest(unittest.TestCase):
    def test_should_get_country_code_and_number(self):
        vat_number = 'CZ28987373'

        country_code, number = get_country_code_and_number_from_vat_number(vat_number)

        self.assertEqual(country_code, 'CZ')
        self.assertEqual(number, '28987373')

    def test_should_separate_more_complicated_country_code_and_number(self):
        vat_number = 'NL802465602B01'

        country_code, number = get_country_code_and_number_from_vat_number(vat_number)

        self.assertEqual(country_code, 'NL')
        self.assertEqual(number, '802465602B01')


if __name__ == '__main__':
    unittest.main()
