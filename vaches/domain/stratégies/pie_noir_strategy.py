from vaches.domain.stratégies.protocols import Rumination_strategy
from vaches.pie_noire import PieNoire

class PieNoireMilkStrategy():
    def calculer_lait(self, vache: "Vache", panse_avant: float) -> float:
        lait = RENDEMENT_LAIT * somme(quantite * coefficent_lait(type))
        return lait

    def stocker_lait(self, vache: "Vache", lait: float) -> None:
        return

    def post_rumination(self, vache: "Vaches", panse_avant: float, lait: float) -> None:
        return


strategy: Rumination_strategy = PieNoireMilkStrategy()