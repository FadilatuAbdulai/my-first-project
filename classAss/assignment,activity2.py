# Activity2: Polymorphism with Animals

class Animal:
    def move(self):
        pass   # base method (to be overridden)


class Dog(Animal):
    def move(self):
        return "The dog runs 🐕💨"


class Bird(Animal):
    def move(self):
        return "The bird flies 🕊✈"


class Fish(Animal):
    def move(self):
        return "The fish swims 🐟🌊"


# Create objects
animals = [Dog(), Bird(), Fish()]

for a in animals:
    print(a.move())