from weakref import WeakKeyDictionary

class Drinker:
    def __init__(self):
        self.req_age = 21
        self.age = WeakKeyDictionary()

    def __get__(self, instance_obj, objtype):
        return self.age.get(instance_obj, self.req_age)

    def __set__(self, instance, new_age):
        if new_age < 21:
            msg = '{name} is too young to legally imbibe'
            raise Exception(msg.format(name=instance.name))
        self.age[instance] = new_age
        print('{name} can legally drink in the USA'.format(
            name=instance.name))

    def __delete__(self, instance):
        del self.age[instance]


class Person:
    drinker_age = Drinker()

    def __init__(self, name, age):
        self.name = name
        self.drinker_age = age


p = Person('Miguel', 30)
p = Person('Niki', 13)