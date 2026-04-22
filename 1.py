# wrappiing up of data and function into a single entity
# restricts access to methods and variables from outside
# prevents data acidental opr unauthorised modificaton
# provides security by hiding data from outside world
class Person:
    def __init__(self, name, age):
        self.name = name
        # Private property
        self.__age= age  
p1=Person("Emil",25)
print(p1.name)
print(p1._Person__age)