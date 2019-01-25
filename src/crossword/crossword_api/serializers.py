from rest_framework import serializers

from . import models


class CrosswordSerializer(serializers.ModelSerializer):
    """A serializer for a crossword."""

    class Meta:
        model = models.Crossword
        fields = ('id', 'crossword_date')


class SquareSerializer(serializers.ModelSerializer):
    """A serializer for a square in a crossword."""

    class Meta:
        model = models.Square
        fields = ('id', 'crossword_id', 'value', 'cleared')
