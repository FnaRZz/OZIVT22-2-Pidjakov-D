# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

# основной код
class Tomato:
    states = {'unripe': 0, 'ripe': 1, 'overripe': 2}

    def __init__(self, index):
        self._index = index
        self._state = self.states['unripe']

    def grow(self):
        if self._state == self.states['ripe']:
            return "Can't grow overripe tomato"
        else:
            next_state = self._state if self._state == 'overripe' else self._state + 1
            self._state = next_state
            return f"Grown tomato #{self._index} from '{self._state}' to '{next_state}'"

    def is_ripe(self):
        return self._state == self.states['ripe']


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(1, num_tomatoes + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def are_all_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name: str, plant: TomatoBush): #name (передается параметром, является публичным) и _plant (принимает объект класса TomatoBush
        self.__name = name
        self.__plant = plant

    @property
    def name(self) -> str:
        return self.__name

    @property
    def plant(self) -> TomatoBush:
        return self.__plant

    def work(self) -> None:
        self.__plant.grow_all()

    def harvest(self) -> bool:
        if not self.plant.are_all_ripe():
            print('Warning: not all fruits are ripe!')
            return False
        else:
            print(f'Harvesting from plant {self.plant}')
            return True

    @staticmethod
    def knowledge_base() -> None:
        print('The static method knowledge_base prints information about gardening.')


gardener = Gardener("John", TomatoBush(10))
gardener.work()
print(gardener.harvest())

