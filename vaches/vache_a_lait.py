from vaches.domain.errors.exceptions import InvalidVacheException
from vaches.vache import Vache

class VacheALait(Vache):
    # Constantes spécifiques à la classe VacheALait
    RENDEMENT_LAIT = 1.1  # Le rendement de la production de lait par rumination
    PRODUCTION_LAIT_MAX = 40.0  # Production de lait maximale par vache (en litres)

    def __init__(self, petitNom: str, poids: float, age: int):
        # Initialisation de la classe par héritage de la classe Vache
        super().__init__(petitNom, poids, age)
        self.lait_disponible = 0.0  # Initialisation de la quantité de lait disponible
        self.lait_total_produit = 0.0  # Initialisation du total de lait produit
        self.lait_total_traite = 0.0  # Initialisation du total de lait trait
        self.lait_total_roti = 0.0  # Initialisation du lait roti (si applicable dans votre contexte)

    def ruminer(self):
        """
        La vache rumine et produit du lait.
        La production dépend du rendement de la rumination et de la panse.
        """
        if self.panse <= 0:
            raise InvalidVacheException("La panse est vide, impossible de ruminer.")

        # Calcul de la quantité de lait produite lors de la rumination
        gain = VacheALait.RENDEMENT_LAIT * self.panse

        # Vérifier si la production de lait dépasse la capacité maximale
        if self.lait_disponible + gain > VacheALait.PRODUCTION_LAIT_MAX:
            raise InvalidVacheException("La production de lait a dépassé la capacité maximale de la vache.")

        # Ajouter le lait à la quantité disponible
        self.lait_disponible += gain
        self.lait_total_produit += gain

        # Vider la panse après la rumination
        self.panse = 0.0

    def traire(self, litres: float):
        """
        Traire la vache et diminuer la quantité de lait disponible.
        Le lait total traître est augmenté en fonction de la quantité traitée.
        """
        if litres <= 0:
            raise InvalidVacheException("La quantité traitée doit être positive.")

        if litres > self.lait_disponible:
            raise InvalidVacheException("Pas assez de lait disponible pour traire cette quantité.")

        # Diminuer le lait disponible
        self.lait_disponible -= litres
        self.lait_total_traite += litres

        return litres

    def vieillir(self):
        """
        La vache vieillit d'un an et son âge est mis à jour.
        """
        super().vieillir()

    def _calculer_lait(self, panse_avant: float) -> float:
        """
        Calculer la quantité de lait produite en fonction de la quantité de panse avant la rumination.
        """
        return VacheALait.RENDEMENT_LAIT * panse_avant

    def _stocker_lait(self, lait: float) -> None:
        """
        Stocker le lait produit, par exemple dans un réservoir de lait.
        """
        self.lait_disponible += lait

    def _post_rumination(self, panse_avant: float, lait: float) -> None:
        """
        Effectuer des actions après la rumination.
        Par exemple, il pourrait s'agir de sauvegarder des informations liées à la production de lait.
        """
        pass

    def ajouter_panse(self, quantite: float) -> None:
        """
        Ajouter une quantité de nourriture à la panse de la vache.
        La quantité ne doit pas dépasser la capacité maximale de la panse.
        """
        if quantite <= 0:
            raise InvalidVacheException("La quantité ajoutée à la panse doit être positive.")

        if self.panse + quantite > Vache.PANSE_MAX:
            raise InvalidVacheException("La panse a dépassé sa capacité maximale.")

        self.panse += quantite

    def valider_rumination_possible(self) -> None:
        """
        Vérifie si la rumination est possible en fonction de la panse.
        """
        if self.panse <= 0:
            raise InvalidVacheException("La panse est vide, impossible de ruminer.")

    def valider_etat(self) -> None:
        """
        Vérifie l'état de la vache avant de procéder à des actions (comme ruminer, traire, etc.)
        """
        if self.age < Vache.AGE_MIN or self.age > Vache.AGE_MAX:
            raise InvalidVacheException("L'âge de la vache n'est pas valide.")
        if self.poids < Vache.POIDS_MIN:
            raise InvalidVacheException("Le poids de la vache n'est pas valide.")
        if self.panse < Vache.PANSE_MIN:
            raise InvalidVacheException("La panse de la vache est vide.")
