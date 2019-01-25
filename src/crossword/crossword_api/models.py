from django.db import models


class Crossword(models.Model):
    """The crossword data."""

    crossword_date = models.DateTimeField()

    def __str__(self):
        """Return the crossword as a string."""

        return self.crossword_date


class Square(models.Model):
    """A crossword square inside of a crossword"""

    crossword_id = models.ForeignKey('Crossword', on_delete=models.CASCADE)
    value = models.CharField(max_length=1)
    cleared = models.BooleanField(default=False)

    def __str__(self):
        """Return the square as a string."""

        return self.value
