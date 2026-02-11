from vaches.domain.stratégies.protocols import Rumination_strategy
from vaches.vache import Vache


class StandardMilkStrategy():

    def calculer_lait(vache: "Vache", panse_avant: float) -> float:
        lait = Vache.RENDEMENT_LAIT * panse_avant
        return lait

    def stocker_lait(self, vache: "Vache", lait: float) -> None:
        self._lait_disponible += lait
        self._lait_total_produit += lait
        return

    def post_rumination(self, vache: "Vaches", panse_avant: float, lait: float) -> None:
        return


strategy: Rumination_strategy = StandardMilkStrategy()