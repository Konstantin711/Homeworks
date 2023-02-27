# Create a class with a description of the worker. Any worker. employees.
import re
from datetime import datetime


class Worker:
    @staticmethod
    def validate_date_field(date: str) -> str:
        """Date should be in format dd.mm.yyyy"""

        day, month, _ = date.split('.')
        if re.match(r"\d{2}.\d{2}.\d{4}$", date) is not None:
            if int(day) > 31:
                raise SyntaxError(f"Day cannot be more than 31. You have set {day}")
            elif int(month) > 12:
                raise SyntaxError(f"Month cannot be more than 12. You have set {month}")
            else:
                return date
        else:
            raise SyntaxError(f"Date should be in dd.mm.yyyy format. You have set {date}")

    def __init__(self, name: str, date_of_birth: str, position: str, date_of_hiring: str,
                 marriage_status: str):
        self.__name = name
        self.__date_of_birth = self.validate_date_field(date_of_birth)
        self.__position = position
        self.__date_of_hiring = self.validate_date_field(date_of_hiring)
        self.__marriage_status = marriage_status

    def get_current_experience(self) -> str:
        current_time = datetime.now()

        day, month, year = self.date_of_hiring.split('.')
        date_of_hiring = datetime(int(year), int(month), int(day))

        delta = current_time - date_of_hiring
        years, days = divmod(delta.days, 365)

        return f'The Human is working for {years} years and {days} days'

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            raise TypeError("It should be str type")

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date):
        if self.validate_date_field(date):
            self.__date_of_birth = date
        else:
            raise TypeError("It should be str type")

    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        if isinstance(position, str):
            self.__position = position
        else:
            raise TypeError("It should be str type")

    @property
    def date_of_hiring(self) -> str:
        return self.__date_of_hiring

    @property
    def marriage_status(self) -> str:
        return self.__marriage_status

    @marriage_status.setter
    def marriage_status(self, new_status: str):
        """'Married', 'Pardoned' can be set"""
        if new_status in ['Married', 'Pardoned']:
            self.__marriage_status = new_status
        else:
            raise ValueError('Wrong status was set')


if __name__ == '__main__':
    worker = Worker('Konstantin', '28.12.1990', 'Manual QA Engineer', '19.12.2018', 'Married')

    worker.name = 'Konstantin Yarmack'
    print(worker.name)

    worker.position = 'Automation QA Engineer'
    print(worker.position)

    print(worker.get_current_experience())