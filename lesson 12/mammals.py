from animals import Animals


class Mammals(Animals):

    def __init__(self, family: str, sub_class: str, living_area: str, hunting_area: str, food_type: str,
                 qty_of_population: int):
        super().__init__(family, sub_class, living_area, hunting_area, food_type,
                         qty_of_population)

    def get_food(self):
        print('Get food for animal')

    def make_some_noize(self):
        print('Make some noize for animal')

    def take_rest(self):
        print('Take rest for animal')

    def sleep(self):
        print('Sleep for animal')

    def run(self):
        print('Run for animal')

    def eat(self):
        print('Eat for animal')
