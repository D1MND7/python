# Добавлено для доп. задания: новый враг
from .abstract_enemy import AbstractEnemy

class Vampire(AbstractEnemy):
    def __init__(self) -> None:
        super().__init__("vampire", "Вампир", 180, 14, 26, 200, 150)