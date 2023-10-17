from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    rating = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name
