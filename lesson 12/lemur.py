from primates import Primates


class Lemur(Primates):
    def __init__(self, family: str, sub_class: str, living_area: str, hunting_area: str, food_type: str,
                 qty_of_population: str, lemur_name: str, color: str, weight: str, age: str, sex: str):
        super().__init__(family, sub_class, living_area, hunting_area, food_type,
                         qty_of_population)

        self.__lemur_name = lemur_name
        self.__color = color
        self.__weight = weight
        self.__age = age
        self.__sex = sex

    @property
    def lemur_name(self):
        return self.__lemur_name

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
    lemur = Lemur(family='Mammals',
                  sub_class='predators',
                  living_area='black wood',
                  hunting_area='wood',
                  food_type='meat',
                  qty_of_population='1000',
                  lemur_name='Silvester',
                  color='grey',
                  weight='20',
                  age='2',
                  sex='male')

    print(lemur.lemur_name)
    print(lemur.family)
    print(lemur.sub_class)
    print(lemur.color)
    print(lemur.weight)
    print(lemur.age)
    print(lemur.sex)
    print(lemur.get_food())
