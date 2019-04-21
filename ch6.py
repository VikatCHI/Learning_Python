# 6.1
class Thing:
    pass
print(Thing)
example = Thing()
print(example)

# 6.2
class Thing2:
    letters = 'abc'
print(Thing2.letters)

# 6.3
class Thing3:
    def _init_(self):
        self.letters = 'xyz'
something = Thing3()
print(something.letters)

# 6.4
class Element:
    def _init_(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(): # 6.6
        print('name = %s, symblo = %s, number = %s' % (self.name, self.symbol, self.number))
hydrogen = Element('Hydrogen', 'H', '1')

# 6.5
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number':1}
hydrogen = Element(**el_dict)
hydrogen.name
hydrogen.dump

# 6.7
print(hydrogen)
class Element:
    def _init_(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def _str_(self):
        return ('name = %s, symblo = %s, number = %s' % (self.name, self.symbol, self.number))
hydrogen = Element(**el_dict)
print(hydrogen)

# 6.8
class Element:
     def _init_(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    @property
    def name(self):
        return self._name
    @property
    def symbol(self):
        return self._symbol
    @property
    def number(self):
        return self._number
hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.name
hydrogen.symbol
hydrogen.number

# 6.9
class Bear:
    def eats(self):
        return 'berries'
b = Bear()
print(b.eats())

# 6.10
class Laser:
    def does(self):
        return 'disintegrate'
class Claw:
    def does(self):
        return 'crush'
class SmartPhone:
    def does(self):
        return 'ring'

class Robot:
    def _init_(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
    def does(self):
        return '''I have many attachments:
        My laser, to %s.
        My claw, to %s.
        My smartphone, to %s.''' % (self.laser.does(), self.claw.does(), self.smartphone.does())

robbie = Robot()
print(robbie.does())
