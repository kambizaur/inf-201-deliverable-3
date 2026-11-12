from dice import Dice


class Weapon:

    """Represents a weapon in the RPG."""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialise the Weapon

        Args:
            name (str): The name of the weapon
            damage_dice (Dice): Damage dealt when character attacks with weapon
        """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        return self.damage_dice.roll()

    def __repr__(self) -> str:
        """Representation of weapon object"""
        return f"Weapon name={self.name} damage={self.damage_dice}"