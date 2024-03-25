class Person:
  def __init__(self, name, age, gender):
  self.name = name
  self.age = age
  self.gender = gender


def introduce(self):
  print(f"Hello, My name is {self.name}. I am {self.age} years old and I am {self.gender}.")

person1 = Person("Ernest", 29, "male")

person1.introduce()
