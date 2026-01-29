class Car():
    def __init__(self, window, doors, enginetype):
        self.__window = window
        self.__doors = doors
        self.__enginetype = enginetype

audi = Car(4, 4, "Diesel")
audi._Car__doors = 5
print(audi._Car__doors)