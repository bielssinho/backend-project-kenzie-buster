from rest_framework import serializers
from datetime import datetime

from movies.models import Movie, MovieOrder, RatingChoices


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, required=False)
    rating = serializers.ChoiceField(
        allow_null=True,
        required=False,
        choices=RatingChoices.choices,
        default=RatingChoices.REATEDG,
    )
    synopsis = serializers.CharField(allow_null=True, required=False)
    added_by = serializers.SerializerMethodField()

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)

    def get_added_by(self, movie: Movie):
        return movie.user.email


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField(read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)

    def get_buyed_by(self, obj: MovieOrder):
        return obj.user.email

    def get_title(self, obj: MovieOrder):
        return obj.movie.title

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
