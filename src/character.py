# Object-oriented game simulator
# Turid Torheim, NMBU, 2026
from item import Weapon


class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def take_damage(self, damage_points: int):
        """Subtract damage_points from the character's HP, without going below 0."""
        self._hp = max(0, self._hp - damage_points)

    def heal(self, heal_points: int):
        """Add heal_points to the character's HP, without going above hp_max."""
        self._hp = min(self.hp_max, self._hp + heal_points)

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        if self.weapon is not None:
            target.weapon.roll_damage()
        else:
            target.take_damage(self.damage)

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Public read-only property to check if HP > 0"""
        return self._hp > 0


class Warrior(Character):
    """Represent a character with warrior specialization."""

    def __init__(
            self,
            name: str,
            hp_max: int,
            damage: int,
            armor: int = 5,
    ) -> None:
        """Initialize a warrior with an armor level."""
        super().__init__(name, hp_max, damage)
        self.armor = armor

    def take_damage(self, damage_points: int) -> None:
        """Subtract damage_points reduced by armor."""
        super().take_damage(max(0, damage_points - self.armor))


class Mage(Character):
    """Represent a character with mage specialization."""

    SPELL_COST = 10
    SPELL_MULTIPLIER = 2
    MANA_REGEN = 5

    def __init__(
            self,
            name: str,
            hp_max: int,
            damage: int,
            mana: int = 30,
            mana_max: int = 30
    ) -> None:
        """Initialize a mage with a mana level."""
        super().__init__(name, hp_max, damage)
        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target) -> None:
        """Attack with magic if mana allows, else attack and regain mana."""
        if self.mana >= self.SPELL_COST:
            target.take_damage(self.damage * self.SPELL_MULTIPLIER)
            self.mana -= self.SPELL_COST
        else:
            super().attack(target)
            self.mana = min(self.mana_max, self.mana + self.MANA_REGEN)
