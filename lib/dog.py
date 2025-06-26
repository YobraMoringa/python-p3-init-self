#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed = "Mutt"):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def adopt(self, owner_name):
        self.owner = owner_name

    def showing_self(self):
        return self

fido = Dog("Fido")
print(fido.name)
print(fido.showing_self())
print(fido is fido.showing_self())
fido.owner = "Sophie"
print(fido.owner)
fido.adopt("Sopie")
print(fido.owner)

snoopy = Dog("snoopy")
print(snoopy.name)