from argparse import ArgumentError, ArgumentTypeError
from enum import Enum
from xml.sax.handler import property_declaration_handler

class Classification(Enum):
    POISSON = 0
    INSECTE = 1
    OISEAU = 2
    MAMIFERE = 3
    AMPHIBIEN = 4
    REPTILE = 5
    INVERTEBRE = 6

class Animal:
    _nom            = ""
    _classification = None
    _isCute         = True
    _age            = 0 
    
    def __init__(self, nom = "Noooopy", classification = Classification.AMPHIBIEN, age = 0) :
        if not isinstance(nom, str):
            raise ArgumentTypeError("Must be a string !")
        if not isinstance(classification, Classification):
            raise ArgumentTypeError("Must be a classification")
        if not isinstance(age, int):
            raise ArgumentTypeError("Must be a int")
        self._nom = nom
        self._classification = classification
        self._age = age

    @property
    def classification(self):
        return self._classification
        
    @property
    def nom(self):
        return self._nom

    @property
    def isCute(self):
        return self._isCute

    @property
    def age(self):
        return self._age


class Chat(Animal) :
    def __init__(self, nom, age = 0):
        super().__init__(nom, Classification.MAMIFERE, age)
        print("chat : " + self._nom + " " +str(self._classification) + " agé de : " + str(self._age))

Chat("Noopy, c'est un garrène", 18)
