"""Describe mammals using principles from the lesson. You should implement different fields and methods.
For example:

Animals -> mammals -> flying mammals-> Bird -> Eagle
............................
Minimum 3 chains should be implemented

Classes should be in different modules. You should have at least 5 different classes."""

from abc import ABC, abstractmethod


class Animals(ABC):
    def __init__(self, family: str, sub_class: str, living_area: str, food_type: str, hunting_area: str,
                 qty_of_population: int):
        self.family = family
        self.sub_class = sub_class
        self.living_area = living_area
        self.hunting_area = hunting_area
        self.food_type = food_type
        self.qty_of_population = qty_of_population

    @abstractmethod
    def get_food(self): ...

    @abstractmethod
    def make_some_noize(self): ...

    @abstractmethod
    def take_rest(self): ...

    @abstractmethod
    def sleep(self): ...

    @abstractmethod
    def run(self): ...

    @abstractmethod
    def eat(self): ...
