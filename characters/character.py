"""Represent a character"""
from abc import ABC

from weapon_behavior.weapon_behavior import WeaponBehavior


class Character(ABC):
    """Character abstract base class"""

    def __init__(self) -> None:
        self.weapon: WeaponBehavior

    def set_weapon(self, weapon: WeaponBehavior) -> None:
        """Set a weapon

        Args:
            weapon (WeaponBehavior): weapon
        """
        self.weapon = weapon

    def fight(self) -> None:
        """Fight"""
        self.weapon.use_weapon()
