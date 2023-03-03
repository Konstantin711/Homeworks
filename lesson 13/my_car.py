from car import Car
# Encapsulation ^


# inheritance
class MyCar(Car):
    # hiding
    __car_mileage = 0
    __gas_level = 100

    def __init__(self, car_brand: str, fuel_type: str, color: str, weight: int, car_type: str):
        # hiding
        self.__car_brand = car_brand
        self.__fuel_type = fuel_type
        self.__color = color
        self.__weight = weight
        self.__car_type = car_type

    def start_engine(self):
        print('Engine is started')
        self.__car_mileage += 5
        self.__gas_level -= 5

    def stop_engine(self):
        print('Engine is stopped')

    def turn_left(self):
        print('Terning left')
        self.__car_mileage += 5
        self.__gas_level -= 5

    def turn_right(self):
        print('Turning right')
        self.__car_mileage += 5
        self.__gas_level -= 5

    def drive_ahead(self):
        print('driving ahead')
        self.__car_mileage += 5
        self.__gas_level -= 5

    def get_gas_level(self):
        return f'{self.__gas_level} percent left'

    def get_car_mileage(self):
        return f'{self.__car_mileage} KM'

    def find_fuel_station(self):
        # Polymorphism
        if self.__fuel_type == 'gasoline':
            print('We are driving to the fuel station')
        else:
            print('We are driving to the electric charger')


if __name__ == '__main__':
    my_car = MyCar(car_brand='Jeep', fuel_type='gasoline', color='black', weight=3, car_type='Outlander')

    my_car.start_engine()
    my_car.drive_ahead()
    my_car.turn_right()
    my_car.turn_right()

    print(my_car.get_gas_level())
    print(my_car.get_car_mileage())

    my_car.find_fuel_station()
