from abc import ABC, abstractmethod
# Encapsulation ^


# inheritance
class Car(ABC):

    # abstraction
    @abstractmethod
    def start_engine(self): ...

    def drive(self): ...

    @abstractmethod
    def stop_engine(self): ...

    @abstractmethod
    def turn_left(self): ...

    @abstractmethod
    def turn_right(self): ...

    @abstractmethod
    def drive_ahead(self): ...

    @abstractmethod
    def get_gas_level(self): ...

    @abstractmethod
    def get_car_mileage(self): ...

    @abstractmethod
    def find_fuel_station(self): ...
