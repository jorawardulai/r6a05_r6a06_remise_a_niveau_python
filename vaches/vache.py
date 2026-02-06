from vaches.domain.errors.exceptions import InvalidVacheException



class Vache:
    AGE_MAX = 25
    POIDS_MAX = 1000.0
    PANSE_MAX = 50.0
    POIDS_MIN = 2.0
    AGE_MIN = 0
    PANSE_MIN = 0
    _NEXT_ID = 1
    RENDEMENT_RUMINATION = 0.25


    def __init__(self, petitNom: str, poids: float, age: int):
        if not petitNom or petitNom.strip() == "":
            raise InvalidVacheException("Le petitNom ne peut pas être vide.")
        if age < self.AGE_MIN or age > self.AGE_MAX:
            raise InvalidVacheException("L'age ne peut pas être inférieur à 0 ni plus grand que AGE_MAX")
        if poids < self.POIDS_MIN:
            raise InvalidVacheException("Le poids ne peut pas être négatif")

        self.petitNom = petitNom
        self.poids = poids
        self.age = age
        self.panse = 0.0


    def get_poids(self):
        return self.poids
    def get_petitNom(self):
        return self.petitNom

    def get_age(self):
        return self.age


    def brouter(self, broute: float, nourriture=None):
        if nourriture!=None:
            raise InvalidVacheException("La vache mange pas de type de nourriture")
        if broute <= 0:
            raise InvalidVacheException("le broute doit être supérieur à 0")
        if self.panse + broute > self.PANSE_MAX:
            raise InvalidVacheException("le broute est plus haut que le panse Max")
        self.panse += broute

    def ruminer(self):
        if self.panse <= 0:
            raise InvalidVacheException("Erreur")

        gain = Vache.RENDEMENT_RUMINATION * self.panse
        self.poids += gain
        self.panse = 0.0

    def vieillir(self) :
        if self.age>=Vache.AGE_MAX:
            raise InvalidVacheException("Vous ne pouvez pas dépasser l'age maximal")

        self.age+=1

    def _calculer_lait(self, pense_avant: float) -> float:
        return 0

    def _stocker_lait(self, lait: float) -> None:
        pass

    def _post_rumination(self, pense_avant: float, lait: float) -> None:
        pass


