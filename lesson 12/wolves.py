from predators import Predators


class Wolves(Predators):
    def __init__(self, family: str, sub_class: str, living_area: str, hunting_area: str, food_type: str,
                 qty_of_population: int, wolf_name: str, color: str, weight: float, age: int, sex: str):
        super().__init__(family, sub_class, living_area, hunting_area, food_type,
                         qty_of_population)

        self.__wolf_name = wolf_name
        self.__color = color
        self.__weight = weight
        self.__age = age
        self.__sex = sex

    @property
    def wolf_name(self):
        return self.__wolf_name

    @property
    def color(self):
        return self.__color

    @property
    def weight(self):
        return self.__weight

    @property
    def age(self):
        return self.__age

    @property
    def sex(self):
        return self.__sex


if __name__ == '__main__':
    wolf = Wolves(family='Mammals',
                  sub_class='predators',
                  living_area='black wood',
                  hunting_area='wood',
                  food_type='meat',
                  qty_of_population=1000,
                  wolf_name='Silvester',
                  color='grey',
                  weight=20.6,
                  age=2,
                  sex='male')

    print(wolf.wolf_name)
    print(wolf.family)
    print(wolf.sub_class)
    print(wolf.color)
    print(wolf.weight)
    print(wolf.age)
    print(wolf.sex)
    print(wolf.get_food())
