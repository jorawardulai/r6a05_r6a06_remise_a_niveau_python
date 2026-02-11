from typing import Dict

from vaches.domain.errors.exceptions import InvalidVacheException
from vaches.domain.nourriture.TypeNourriture import TypeNourriture
from vaches.vache_a_lait import VacheALait


class PieNoire(VacheALait):

    COEFFICIENT_NUTRITIONNEL: Dict[TypeNourriture, float] = {
        TypeNourriture.MARGUERITE: 1.1,
        TypeNourriture.HERBE: 1.0,
        TypeNourriture.FOIN: 0.9,
        TypeNourriture.PAILLE: 0.4,
        TypeNourriture.CEREALES: 1.3,
    }

    def __init__(
            self,
            petit_nom: str,
            poids: float,
            age: int,
            nb_taches_blanches: int,
            nb_taches_noires: int,
    ):
        # Invariants métier
        if not isinstance(nb_taches_blanches, int) or nb_taches_blanches <= 0:
            raise InvalidVacheException("Nombre de taches blanches invalide.")

        if not isinstance(nb_taches_noires, int) or nb_taches_noires <= 0:
            raise InvalidVacheException("Nombre de taches noires invalide.")

        super().__init__(petit_nom, poids, age)

        self.nb_taches_blanches = nb_taches_blanches
        self.nb_taches_noires = nb_taches_noires
        self._ration: Dict[TypeNourriture, float] = {}

    # -------------------------
    # PROPERTY
    # -------------------------

    @property
    def ration(self) -> Dict[TypeNourriture, float]:
        return self._ration.copy()

    # -------------------------
    # BROUTER
    # -------------------------

    def brouter(
            self,
            quantite: float,
            type_nourriture: TypeNourriture = None,
    ) -> None:

        # Laisse la validation métier (quantité + panse max)
        # à la classe mère
        super().brouter(quantite)

        # Cas typé : on enrichit la ration
        if type_nourriture is not None:

            if not isinstance(type_nourriture, TypeNourriture):
                raise InvalidVacheException("Type de nourriture invalide.")

            self._ration[type_nourriture] = (
                    self._ration.get(type_nourriture, 0.0) + quantite
            )

    # -------------------------
    # CALCUL LAIT
    # -------------------------

    def _calculer_lait(self, panse_avant: float) -> float:

        # Si aucune ration typée → fallback mère
        if not self._ration:
            return super()._calculer_lait(panse_avant)

        # Calcul spécialisé
        facteur = 0.0
        for type_nourriture, quantite in self._ration.items():
            coefficient = self.COEFFICIENT_NUTRITIONNEL[type_nourriture]
            facteur += quantite * coefficient

        return VacheALait.RENDEMENT_LAIT * facteur

    # -------------------------
    # POST RUMINATION
    # -------------------------

    def _post_rumination(self, lait: float) -> None:
        super()._post_rumination(lait)
        self._ration.clear()