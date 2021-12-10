"""Main function"""
from characters.queen import Queen
from weapon_behavior.knife_behavior import KnifeBehavior


def main() -> None:
    "Main function"
    queen = Queen()
    queen.fight()
    queen.set_weapon(KnifeBehavior())
    queen.fight()


if __name__ == "__main__":
    main()
