import random


class Dice:
    """Represent an n-sided dice."""
    
    def __init__(self, sides=6):
        """Initialize a dice with the specified number of sides.

        Args:
            sides: Number of sides. Defaults to 6.

        Raises:
            ValueError: If the number of sides is less than 2.
        """
        if sides < 2:
            raise ValueError("Dice must have at least 2 sides.")
        
        self.sides = sides

    def roll(self) -> int:
        """Roll the dice and return a random number between 1 and the number of sides."""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Return a string representation of the dice."""
        return f'Dice(sides={self.sides})'

    def __call__(self) -> int:
        """Allow the dice object to be called like a regular function to perform a roll."""
        return self.roll()



