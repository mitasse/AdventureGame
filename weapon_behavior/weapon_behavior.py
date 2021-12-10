"""Weapon behavior"""
from typing import Protocol


class WeaponBehavior(Protocol):
    """Weapon behavior interface"""

    def use_weapon(self) -> None:
        """Use weapon"""
        ...
