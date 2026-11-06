# Добавлено для доп. задания: новая локация
from ..enemy.enemy import Enemy
from ..enemy.vampire import Vampire
from ..item.default_catalog import BLOOD_SWORD, VAMPIRE_CLOAK
from ..item.item_catalog import ItemCatalog
from .location import Location

class VampireCastle(Location):
    CODE = "vampire-castle"

    def __init__(self, catalog: ItemCatalog) -> None:
        super().__init__(VampireCastle.CODE, "Замок вампира", 4, catalog)

    def _create_enemy(self) -> Enemy:
        return Vampire()

    @property
    def _loot_table(self) -> tuple[str, ...]:
        return (BLOOD_SWORD, VAMPIRE_CLOAK)