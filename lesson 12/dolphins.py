from cetaceans import Cetaceans


class Dolphins(Cetaceans):
    def __init__(self, family: str, sub_class: str, living_area: str, hunting_area: str, food_type: str,
                 qty_of_population: int, dolphin_name: str, color: str, weight: float, age: int, sex: str):
        super().__init__(family, sub_class, living_area, hunting_area, food_type,
                         qty_of_population)

        self.__dolphin_name = dolphin_name
        self.__color = color
        self.__weight = weight
        self.__age = age
        self.__sex = sex

    @property
    def dolphin_name(self):
        return self.__dolphin_name

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
    dolphin = Dolphins(family='Mammals',
                       sub_class='cetacean',
                       living_area='black sea',
                       hunting_area='water',
                       food_type='fish',
                       qty_of_population=1000,
                       dolphin_name='John',
                       color='grey',
                       weight=50.5,
                       age=3,
                       sex='male')

    print(dolphin.dolphin_name)
    print(dolphin.family)
    print(dolphin.sub_class)
    print(dolphin.color)
    print(dolphin.weight)
    print(dolphin.age)
    print(dolphin.sex)
    print(dolphin.get_food())
