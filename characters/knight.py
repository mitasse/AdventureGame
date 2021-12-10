"""Represent a Knight"""
from dataclasses import dataclass

from weapon_behavior.sword_behavior import SwordBehavior

from characters.character import Character


@dataclass
class Knight(Character):
    """Knight character concrete class"""

    weapon = SwordBehavior()
