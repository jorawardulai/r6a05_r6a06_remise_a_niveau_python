from __future__ import annotations

from typing import Protocol

class Rumination_strategy(Protocol):

    def calculer_lait(selfself, vache: "Vache",panse_avant: float) -> float:
        ...
    def stocker_lait(self, vache: "Vache", lait: float) -> None:
        ...
    def post_rumination(self, vache: "Vache", panse_avant: float, lait: float) -> None:
        ...
