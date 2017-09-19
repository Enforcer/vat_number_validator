import argparse
import re

import zeep
from zeep.exceptions import Fault


WSDL = 'http://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl'


def get_vat_number_from_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('vat_number', metavar='vat_number', type=str, help='VAT number to check')
    args = parser.parse_args()
    return args.vat_number


def get_country_code_and_number_from_vat_number(vat_number):
    match_result = re.match(r'^([A-Z]+)(.+)$', vat_number)
    if not match_result:
        raise ValueError('Invalid format')
    return match_result.group(1), match_result.group(2)


def check_vat_number_with_eu_vat_service(vat_number):
    client = zeep.Client(wsdl=WSDL, strict=False)
    country_code, number = get_country_code_and_number_from_vat_number(vat_number)
    result = client.service.checkVat(country_code, number)
    return result['valid']


if __name__ == '__main__':
    vat_number = get_vat_number_from_args()
    try:
        is_valid = check_vat_number_with_eu_vat_service(vat_number)
    except Fault:
        print('error')  # SOAP error
    except Exception:
        print('exception')  # unknown exception
    else:
        message = 'Valid' if is_valid else 'Invalid'
        print(message)
