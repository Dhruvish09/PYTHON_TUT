from django.db import models

# Create your models here.

class Population(models.Model):
    country = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    human_count = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return f"{self.country} => {self.year} => {self.human_count}"
    