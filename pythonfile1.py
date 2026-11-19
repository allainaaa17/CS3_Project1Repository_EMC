class Animal:
  def __init__(self, name):
    self.__name = name
  @property
  def name(self):
    return self.__name
  def eat(self):
    print(f"{self.__name} eats food.")
  def make_sound(self):
    print(f"{self.__name} makes sound!")

class Lion(Animal):
  def __init__(self, name):
    super().__init__(name)
  def make_sound(self):
    return (f"{self.name} roars loudly!")
  def eat(self):
    return (f"{self.name} eats fresh meat.")

class Elephant(Animal):
  def __init__(self, name):
    super().__init__(name)
  def make_sound(self):
    return (f"{self.name} trumpets!")
  def eat(self):
    return (f"{self.name} eats grass and fruits.")

class Monkey(Animal):
  def __init__(self, name):
    super().__init__(name)
  def make_sound(self):
    return (f"{self.name} chatters!")
  def eat(self):
    return (f"{self.name} eats bananas.")

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound())
print(lion.eat())
print("-----")

print(elephant.make_sound())
print(elephant.eat())
print("-----")

print("Hi")
print("Test path")

print(monkey.make_sound())
print(monkey.eat())
print("-----")
