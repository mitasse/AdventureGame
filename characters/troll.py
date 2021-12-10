"""Represent a Troll"""
from dataclasses import dataclass

from weapon_behavior.axe_behavior import AxeBehavior

from characters.character import Character


@dataclass
class Troll(Character):
    """Troll character concrete class"""

    weapon = AxeBehavior()
