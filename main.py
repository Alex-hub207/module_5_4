class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.houses_history.append(name)

    def __del__(self,*args):
        print(str(self.name) + ' снесён, но он останется в истории')

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return 'Название: ' + str(self.name) + ', кол-во этажей ' + str(self.number_of_floors)

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        if isinstance(other, House):
            if self.number_of_floors <= other.number_of_floors:
                return True
            else:
                return False

    def __gt__(self, other):
        if isinstance(other, House):
            if self.number_of_floors > other.number_of_floors:
                return True
            else:
                return False

    def __ge__(self, other):
        if isinstance(other, House):
            if self.number_of_floors >= other.number_of_floors:
                return True
            else:
                return False

    def __ne__(self, other):
        if isinstance(other, House):
            if self.number_of_floors != other.number_of_floors:
                return True
            else:
                return False

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        elif isinstance(value, House):
            return self

    def __radd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)

print(House.houses_history)

h2 = House('ЖК Акация', 30)

print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)

del h2

del  h3

print(House.houses_history)