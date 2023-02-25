# Create a class describing any company. For example, Toshiba or Apple
import re
import requests


class Company:

    @staticmethod
    def validate_date_of_foundation(date: str) -> bool:
        """Date should be in format dd.mm.yyyy"""

        day, month, _ = date.split('.')
        if re.match(r"\d{2}.\d{2}.\d{4}$", date) is not None:
            if int(day) > 31:
                raise SyntaxError(f"Day cannot be more than 31. You have set {day}")
            elif int(month) > 12:
                raise SyntaxError(f"Month cannot be more than 12. You have set {month}")
            else:
                return True
        else:
            raise SyntaxError(f"Date should be in dd.mm.yyyy format. You have set {date}")

    @staticmethod
    def validate_website(site: str) -> bool:
        """Check that site is exist"""

        try:
            requests.get(f'https://{site}')
            return True
        except:
            raise ConnectionError(f'Looks like site address is wrong. You have set{site}')

    @staticmethod
    def validate_phone_number(phone_number: str) -> str:
        """Phone number validation"""

        number = ''
        for digit in phone_number:
            number += digit if digit.isdigit() else ''

        return number

    _qty_of_employers: int = None
    _date_of_foundation: str = None
    _headquarters: str = None
    _website: str = None
    _telephone: str = None

    def __init__(self, ceo: str, company_name: str):
        self._ceo = str(ceo)
        self._company_name = str(company_name)

    @property
    def ceo(self) -> str:
        return self._ceo

    @ceo.setter
    def ceo(self, new_ceo: str):
        if isinstance(new_ceo, str) and len(new_ceo) < 30:
            self._ceo = new_ceo
        else:
            raise ValueError('Only string type shorter than 30 symbols')

    @property
    def company_name(self) -> str:
        return self._company_name

    @company_name.setter
    def company_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) < 50:
            self._company_name = new_name
        else:
            raise ValueError('Only string type shorter than 50 symbols')

    @property
    def qty_of_employers(self) -> int:
        return self._qty_of_employers

    @qty_of_employers.setter
    def qty_of_employers(self, qty: int):
        if isinstance(qty, int) and qty > 0:
            self._qty_of_employers = qty
        else:
            raise ValueError('Only integer can be set and positive digits')

    @property
    def date_of_foundation(self):
        return self._date_of_foundation

    @date_of_foundation.setter
    def date_of_foundation(self, date: str):
        if isinstance(date, str):
            if self.validate_date_of_foundation(date):
                self._date_of_foundation = date
        else:
            raise ValueError('Only string can be set')

    @property
    def headquarters(self) -> str:
        return self._headquarters

    @headquarters.setter
    def headquarters(self, address):
        if isinstance(address, str):
            self._headquarters = address
        else:
            raise ValueError('Only string can be set')

    @property
    def website(self):
        return self._website

    @website.setter
    def website(self, website: str):
        if isinstance(website, str):
            if self.validate_website(website):
                self._website = website
        else:
            raise ValueError('Only string can be set')

    @property
    def telephone(self) -> str:
        return self._telephone

    @telephone.setter
    def telephone(self, phone_number: str):
        if isinstance(phone_number, str):
            self._telephone = self.validate_phone_number(phone_number)
        else:
            raise ValueError('Only string can be set')


if __name__ == '__main__':
    google = Company('Mister Founder', 'Google')

    print(google.ceo)
    print(google.company_name)

    google.qty_of_employers = 50000
    print(google.qty_of_employers)

    google.date_of_foundation = '15.11.1998'
    print(google.date_of_foundation)

    google.website = 'www.google.com'
    print(google.website)

    google.headquarters = 'USA, California'
    print(google.headquarters)

    google.telephone = '(050)589-53-65'
    print(google.telephone)
