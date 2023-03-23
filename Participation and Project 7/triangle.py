# imports the dataclasses module and imports as dataclass
from dataclasses import dataclass
import math  # import the math modules


@dataclass  # call the dataclass function
class Pythagorean():
    """Hold the Pythagorean Theorem

    Returns:
        constant: The calculation output
    """
    A: float = 0.0  # sets A variable to a float
    B: float = 0.0  # sets B variable to a float

    def calculateC(self):
        """Calculate the Pythagorean Theorem

        Returns:
            constant: the calculation output
        """
        C = round(math.sqrt(self.A**2 + self.B**2),
                  3)  # C = the square root of input A squared added to B squared, all rounded to the 3rd decimal place
        return C  # send up the C variable
