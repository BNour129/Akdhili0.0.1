from django.db import models

# Create your models here.

class Kadhia(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField(blank=True, null=True, max_length=100)
    Price = models.DecimalField(decimal_places=2, max_digits=1000)
    StartingPlace = models.TextField(max_length=100)
    Destination = models.TextField(max_length=100)
    Recommended = models.BooleanField(null=True, default=True)

    def __str__(self):
        return self.Title

    def snippet(self):
        return self.body[:50] + '...'
