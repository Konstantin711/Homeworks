from train import Train
from wagon import Wagon


if __name__ == '__main__':
    train = Train()

    wagon1 = Wagon(wagon_type='lux')
    wagon1.add_passenger(10)
    train + wagon1

    print(wagon1.passengers_wagon)
    print(wagon1.__len__())
    print(train.__len__())
    print(wagon1.__str__())

    wagon2 = Wagon(wagon_type='casual')
    wagon2.add_passenger(5)
    train + wagon2

    print(wagon2.passengers_wagon)
    print(wagon2.__len__())
    print(train.__len__())
    print(wagon2.__str__())

    wagon3 = Wagon(wagon_type='lux')
    wagon3.add_passenger(8)
    train + wagon3

    print(wagon3.passengers_wagon)
    print(wagon3.__len__())
    print(train.__len__())
    print(wagon3.__str__())

    print(train.train_wagons)



