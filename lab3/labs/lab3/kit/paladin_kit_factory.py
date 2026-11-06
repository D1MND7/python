# Добавлено для доп. задания: фабрика нового класса
from ..item.armor import Armor
from ..item.default_catalog import CRUSADER_ARMOR, HAMMER_OF_LIGHT
from ..item.item_catalog import ItemCatalog
from ..item.weapon import Weapon
from .starter_kit_factory import StarterKitFactory

class PaladinKitFactory(StarterKitFactory):

    def __init__(self, catalog: ItemCatalog) -> None:
        self._catalog = catalog

    def create_weapon(self) -> Weapon:
        return self._catalog.create_weapon(HAMMER_OF_LIGHT)

    def create_armor(self) -> Armor:
        return self._catalog.create_armor(CRUSADER_ARMOR)