from mammals import Mammals


class Primates(Mammals):
    def __init__(self, family: str, sub_class: str, living_area: str, hunting_area: str, food_type: str,
                 qty_of_population: str):
        super().__init__(family, sub_class, living_area, hunting_area, food_type,
                         qty_of_population)

    def get_food(self):
        print('Find food for primate')

    def make_some_noize(self):
        print('Make some noize as primate')

    def take_rest(self):
        print('Take rest for primates')

    def sleep(self):
        print('Sleep for primates')

    def run(self):
        print('Run for primates')

    def eat(self):
        print('Eat for primates')
