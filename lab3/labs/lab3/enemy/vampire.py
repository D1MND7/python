from ..defense.armor_handler import ArmorHandler
from .abstract_enemy import AbstractEnemy

RESISTANCE = 0.2


class Vampire(AbstractEnemy):

    def __init__(self) -> None:
        super().__init__("vampire", "Вампир", 180, 14, 26, 200, 150, ArmorHandler(RESISTANCE))