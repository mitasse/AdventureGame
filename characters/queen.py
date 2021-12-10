"""Represent a Queen"""
from dataclasses import dataclass

from weapon_behavior.bow_and_arrow_behavior import BowAndArrowBehavior

from characters.character import Character


@dataclass
class Queen(Character):
    """Queen character concrete class"""

    weapon = BowAndArrowBehavior()
