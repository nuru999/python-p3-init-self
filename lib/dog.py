#!/usr/bin/env python3

class Dog:
     def __init__(self, name, breed = "Mutt"):
        self.name = name
        self.breed = breed

fav_dog = Dog("Rex")
print(fav_dog.name)

cool_dog = Dog("Bosco", "Simba")
print(cool_dog.breed)