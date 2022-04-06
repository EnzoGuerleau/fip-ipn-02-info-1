from argparse import ArgumentError
from enum import Enum

class Classification(Enum):
    POISSON = 0
    INSECTE = 1
    OISEAU = 2
    MAMIFERE = 3
    AMPHIBIEN = 4
    REPTILE = 5
    INVERTEBRE = 6

class Animal:
    _nom = ""
    _classification = None

    def __init__(self, nom, classification) :
        self._nom = nom
        self._classification = classification

class chat(Animal) :
    def __init__(self, nom, classification):
        super().__init__(nom, classification)
        #print("chat : " + self._nom + " " +str(self._classification))

class chien(Animal):
    def __init__(self, nom, classification):
        super().__init__(nom, classification)
        print(self._nom + " est un chien")

chat("Noopy", Classification.MAMIFERE)
chien("Osama", Classification.MAMIFERE)