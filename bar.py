from argparse import ArgumentTypeError
from enum import Enum
from operator import truediv
from re import T
from termios import CR0
from tokenize import Number

class TypeTaille(Enum) :
    Small = 0
    Medium = 1
    Large = 2

class Boisson():
    type = TypeTaille.Small

    def __init__(self, type):
        self._type = type

    @property
    def type(self):
        return self._type

class ListBoisson():
    _Nom = ""
    _Ingredients = ""
    _Prix = 4

    def __init__(self, nom, ingredients, prix):
        self._nom = nom
        self._Ingredients = ingredients
        self._Prix = prix
    
    @property
    def Nom(self):
        return self._nom
    
    @property
    def Ingredients(self):
        return self._Ingredients
    
    @property
    def Prix(self):
        return self._Prix
    
class Barmaid():
    _ListBoisson = list()
    _BoissonSelection = list()
    _Commande = list()
    _Stock = {"mango": 10, "orange": 10, "guajana" : 10, "apple" : 10, "ginger" : 10, "lemon" : 10, "guava" : 10, "pineapple" : 10, "banana" : 10, "carrot" : 10, "celery stick" : 10, "beetroot" : 10}
    _NbBoisson = 0
    _DejaPaye = 0
    _Continue = True
    _estValide = False
    _estPaye = False
    _estDonne = False

    @property
    def Continue(self):
        return self._Continue

    @property
    def facture(self):
        total = 0.
        for i in self._Commande:
            if isinstance(i,float):
                total += i
        return(total)
    
    @property
    def estAnnule(self):
        return self._BoissonSelection == None and self._NbBoisson == 0

    @property
    def estValide(self):
        return self._BoissonSelection != None

    def __init__(self, ListeBoisson):
        if isinstance(ListeBoisson, list):
            if not all(isinstance(elem, ListBoisson) for elem in ListeBoisson):
                raise ArgumentTypeError("Must be a list of Boisson")
        else :
            raise ArgumentTypeError("Must be a list")

        self._ListBoisson = ListeBoisson

    def Suite(self,suite):
        if suite == True:
            self._Continue = True
        else:
            self._Continue = False

    def ConsulterBoisson(self):
        return self._ListBoisson
    
    def selectionnerBoisson(self, boisson, taille):
        if not isinstance(boisson, ListBoisson):
            raise ArgumentTypeError("Jus must be a boisson")
        if not isinstance(taille, TypeTaille):
            raise ArgumentTypeError("Must be a TypeTaille")
        if taille == TypeTaille.Small:
            addtaille = "Small"
        elif taille == TypeTaille.Medium:
            addtaille = "Medium"
        elif taille == TypeTaille.Large:
            addtaille = "Large"
        self._BoissonSelection.append(boisson)
        self._Commande.append(boisson.Nom)
        self._Commande.append(addtaille)
        self._Commande.append(boisson.Prix+(taille.value*0.5))
        return True

    def VoirCommande(self):
        return self._Commande

    def valider(self):
        if self.estValide:
            self._estValide = True
        else :
            self._estValide = False
        return self._estValide
    
    def Annulation(self):
        self._estValide  = False
        self._TailleSelecition = list()
        self._BoissonSelection = list()
        self._NbBoisson = 0
    
    def payer(self, somme) :
        if not self.estValide :
            raise BaseException("Command must be confirmed !")

        reste = self.facture - float(somme) - float(self._DejaPaye)
        if reste <= 0:
            self._estPaye = True
        else:
            self._estPaye = False
        self._DejaPaye += float(somme)
        return(self._estPaye, reste)

    def Donner(self):
        if not self.estValide or not self._estPaye:
            raise BaseException("Command must be confirmed and payed")

        return True

    def VerifStock(self):
        c0=0
        c1=0
        c2=2
        c3=3

        for i in self._Commande:
            if i == "The Boost":
                c0+=1
            if i == "The Fresh":
                c1+=1
            if i == "The Fusion":
                c2+=1
            if i == "The Detox":
                c3+=1
        if c0 != 0:
            if (self._Stock["mango"]- c0*0.5) < 0:
                print("Stock Mango non suffisant !")
            if (self._Stock["orange"]- c0*2) < 0:
                print("Stock orange non suffisant !")
            if (self._Stock["guajana"]- c0*1) < 0:
                print("Stock guajana non suffisant !")
        if c1 != 0:
            if (self._Stock["apple"]- c1*3) < 0:
                print("Stock apple non suffisant !")
            if (self._Stock["ginger"]- c1*1) < 0:
                print("Stock ginger non suffisant !")
            if (self._Stock["lemon"]- c1*1) < 0:
                print("Stock lemon non suffisant !")
        if c2 != 0:
            if (self._Stock["guava"]- c0*1) < 0:
                print("Stock guava non suffisant !")
            if (self._Stock["pineapple"]- c0*0.25) < 0:
                print("Stock pineapple non suffisant !")
            if (self._Stock["banana"]- c0*0.5) < 0:
                print("Stock banana non suffisant !")
        if c3 != 0:
            if (self._Stock["carrot"]- c1*3) < 0:
                print("Stock carrot non suffisant !")
            if (self._Stock["celery stick"]- c1*1) < 0:
                print("Stock celery stick non suffisant !")
            if (self._Stock["beetroot"]- c1*1) < 0:
                print("Stock beetroot non suffisant !")
        print(self._Stock)
            

    

    
if __name__ == '__main__':
    initBoisson = [
         ListBoisson("The Boost", "0.5:mango, 2:oranges, 1:guajana", 5),
         ListBoisson("The Fresh", "3:apples, 1:ginger, 1:lemon", 4),
         ListBoisson("The Fusion", "1:guava, 0.25:pineapple, 0.5:banana", 5),
         ListBoisson("The Detox", "3:carrots, 1:celery stick, 1:beetroot", 3.5)
     ]   

    # Init barmaid
    barmaid = Barmaid(initBoisson)
    print("barmaid initalisee !")

    # Consultation
    

    # Selecition Boisson / Taille

    while(barmaid.Continue == True):
        jus = barmaid.ConsulterBoisson()
        print("Consultation jus : ")
        flag = 0
        for juss in jus:
            print("%d- %s / %s / %.2f $" %(flag,juss.Nom, juss.Ingredients, juss.Prix))
            flag += 1

        print()
        juss = initBoisson[int(input("Select boisson : "))]
        print("Tailles dispos : Small, Medium (+ 0.5 $), Large (+ 1 $)")
        Taille = input("Saisir taille voulue : ").upper()
        if Taille == "SMALL":
            JusTaille = TypeTaille.Small
        elif Taille == "MEDIUM":
            JusTaille = TypeTaille.Medium
        elif Taille == "LARGE":
            JusTaille = TypeTaille.Large
        else :
            raise ArgumentTypeError("Bien ecrire svp")
        jusSelect = barmaid.selectionnerBoisson(juss, JusTaille)
        print("jus selectionne ? %s" %jusSelect)
        print()

        print("Commande : ", barmaid.VoirCommande())
        print()

        test = input("Poursuivre la commande ? Oui/Non   ").upper()
        if test == "NON" :
            barmaid.Suite(False)
        
    barmaid.VerifStock()
    # validation
    estValidee = barmaid.valider() 
    print("commande validee ? %s" %estValidee)
    print()

    # Voir Commande
    commande = barmaid.VoirCommande()
    print("Commande : ",commande)
    print("Total : %.2f $" %barmaid.facture)
    #payer
    reste = 1
    while(reste > 0):
        (estPayee, reste) = barmaid.payer(float(input("Montant paye $ : ")))
        if estPayee == False :
            print("Reste a payer : ", reste, " $")
        else :
            if reste < 0 :
                print("Montant à rendre : ", - reste, " $")
            print("Merci pour votre commande ! Boujoux")
    
    print("Commande finie ? %s" % barmaid.Donner())