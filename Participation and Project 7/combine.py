# imports the dataclasses module and imports as dataclass
from dataclasses import dataclass


@dataclass  # call the dataclass function
class MadLib():
    """Sets the variables and creates the Mad Lib

    Returns:
        str: The newly created mad lib
    """
    noun1: str  # sets noun1 to a string
    noun2: str  # sets noun2 to a string
    verb1: str  # sets verb1 to a string
    verb2: str  # sets verb2 to a string

    def combineMadlib(self):
        """Combines the input nouns and verbs

        Returns:
            str: The newly created mad lib
        """
        madlib = ""  # sets madlib variable to blank
        # adds the following text and input variables together to the madlib variable
        madlib += "One day I woke up and went to grab my " + self.noun1 + ", only it wansn't there! Where had it gone? I quickly " + self.verb1 + " downstairs and started franticly searching. Since I couldn't find it in the house, I went outside into my " + \
            self.noun2 + " and " + self.verb2 + \
            " as fast as I could to my work office. Thank goodness that my" + \
            self.noun1 + " was right on my desk."
        return madlib  # send up the madlib variable
