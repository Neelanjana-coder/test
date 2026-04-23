from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass
class defender(Car):
    def mileage(self):
        print('the mileage is 7kmpl')
class diago(Car):
    def mileage(self):
        print('the mileage is 13kmpl')
class pajero(Car):
    def mileage(self):
        print('the mileage is 13kmpl')
d=defender()
d.mileage()

i=diago()
i.mileage()

j=pajero()
j.mileage()
