from vaches.NoMilkStrategy import NoMilkStrategy
from vaches.RuminationStrategy import RuminationStrategy
from vaches.exceptions import InvalidVacheException



class Vache:
    AGE_MAX = 25
    POIDS_MAX = 1000.0
    PANSE_MAX = 50.0
    POIDS_MIN = 2.0


    def __init__(self, petitNom: str, poids: float, age: int):
        if not petitNom or petitNom.strip() == "":
            raise InvalidVacheException("Le petitNom ne peut pas être vide.")
        if age < 0 or age > self.AGE_MAX:
            raise InvalidVacheException("L'age ne peut pas être inférieur à 0 ni plus grand que AGE_MAX")
        if poids < self.POIDS_MIN:
            raise InvalidVacheException("Le poids ne peut pas être négatif")

        self.petitNom = petitNom
        self.poids = poids
        self.age = age
        self.panse = 0.0



    def brouter(self, broute: float, nourriture=None):
        if nourriture!=None:
            raise InvalidVacheException("La vache mange pas de type de nourriture")
        if broute <= 0:
            raise InvalidVacheException("le broute doit être supérieur à 0")
        if self.panse + broute > self.PANSE_MAX:
            raise InvalidVacheException("le broute est plus haut que le panse Max")
        self.panse += broute


