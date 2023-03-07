"""
Describe the Train object.
Class must contain fields and a method for adding wagons (it is necessary to add objects, instances of the wagon class).
Describe the class Wagon together with the train.The Wagon must contain a list of passengers and allow adding passengers
In the Wagon can be 10 passengers for example. When using the len function on a Wagon,
I want to see the number of passengers. When using len on a train, I want to see a list of Wagons without a locomotive.
Each wagon must have a number. When printing a wagon to the console,
I want to see the following "[n]" where n is the number of the wagon.
"""


class Train:
    __train_wagons = list()

    def __init__(self):
        self.locomotive = ['locomotive of the train']
        self.__train_wagons.append(self.locomotive)

    @property
    def train_wagons(self):
        return self.__train_wagons

    def __add__(self, obj):
        self.__train_wagons.append(obj.passengers_wagon)
        obj.wagon_number = self.__train_wagons.index(obj.passengers_wagon)

    def __len__(self):
        return f'Train consist of locomotive and {len(self.__train_wagons) - 1} wagon(s)'
