

class Wagon:
    wagon_number = 0

    def __init__(self, **kwargs):
        self.wagon_type = kwargs['wagon_type']
        self.__passengers_wagon = list()

    @property
    def passengers_wagon(self):
        return self.__passengers_wagon

    def add_passenger(self, passengers_qty: int):
        if passengers_qty > 10 or passengers_qty < 0:
            raise SyntaxError('10 passengers is max size of wagon and 0 is minimum')
        elif not isinstance(passengers_qty, int):
            raise TypeError('Only int type can be set')
        else:
            array_with_customers = []
            for passenger in range(1, passengers_qty + 1):
                array_with_customers.append(f'passenger_{passenger}')
            self.__passengers_wagon.extend(array_with_customers)

    def __len__(self):
        return f'Number of passengers is - {len(self.__passengers_wagon)}'

    def __str__(self):
        return f'Wagon number is {self.wagon_number}'
