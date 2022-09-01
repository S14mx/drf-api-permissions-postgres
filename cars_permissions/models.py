from django.db import models

from django.contrib.auth import get_user_model


class Car(models.Model):
    make = models.TextField()
    model = models.TextField()
    year = models.CharField(max_length=4)
    mpg = models.CharField(max_length=3)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
