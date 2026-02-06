

class NoMilkStrategy:

    def calculer_lait(self, vache: "Vache", panse_avant: float)-> float:
        return 0.0
    def stocker_lait(self, vache : "Vache", lait : float) -> None:
        return
    def post_rumination(self, vache : "Vache", panse_avant: float, lait : float) -> None:
        return