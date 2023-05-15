from django.db import models
from users.models import User


class RatingChoices(models.TextChoices):
    REATEDG = "G"
    REATEDPG = "PG"
    REATEDPG_13 = "PG-13"
    REATEDR = "R"
    REATEDNC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20,
        choices=RatingChoices.choices,
        default=RatingChoices.REATEDG,
    )
    synopsis = models.TextField(null=True, default=None)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
    )

    movies_users = models.ManyToManyField(
        "users.User",
        through="movies.MovieOrder",
        related_name="movies_orders",
    )


class MovieOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
