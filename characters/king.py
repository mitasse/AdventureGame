"""Represent a King"""
from dataclasses import dataclass

from weapon_behavior.knife_behavior import KnifeBehavior

from characters.character import Character


@dataclass
class King(Character):
    """King character concrete class"""

    weapon = KnifeBehavior()
