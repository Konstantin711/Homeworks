from mammals import Mammals


class Cetaceans(Mammals):
    def __init__(self, family: str, sub_class: str, living_area: str, hunting_area: str, food_type: str,
                 qty_of_population: int):
        super().__init__(family, sub_class, living_area, hunting_area, food_type,
                         qty_of_population)

    def get_food(self):
        print('Find food for cetaceans')

    def make_some_noize(self):
        print('Make some noize as cetaceans')

    def take_rest(self):
        print('Take rest for cetaceans')

    def sleep(self):
        print('Sleep for cetaceans')

    def run(self):
        print('Run for cetaceans')

    def eat(self):
        print('Eat for cetaceans')
