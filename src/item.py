class Weapon:
    """Represents a weapon in the RPG."""
    import Dice
    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialise the Weapon

        Args:
            name (str): The name of the weapon
            damage_dice (Dice): Damage dealt when character attacks with weapon
        """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self, ):
        pass