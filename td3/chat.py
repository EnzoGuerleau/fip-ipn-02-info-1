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
    _nom = ""
    _classification = None
    _isCute = True
    
    def __init__(self, nom, classification) :
        if not isinstance(nom, str):
            raise ArgumentTypeError("Must be a string !")
        if not isinstance(classification, Classification):
            raise ArgumentTypeError("Must be a classification")
        self._nom = nom
        self._classification = classification

    @property
    def classification(self):
        return self._classification
        
    @property
    def nom(self):
        return self._nom

    @property
    def isCute(self):

        return self._isCute

class Chat(Animal) :
    def __init__(self, nom):
        
        super().__init__(nom, Classification.MAMIFERE)
        print("chat : " + self._nom + " " +str(self._classification))

Chat("Noopy, c'est un garrène")
