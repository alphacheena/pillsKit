from accounts.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Kit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kits')
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.location}_{self.user}"


class Medicine(models.Model):
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE, related_name='medicines')
    name = models.CharField(max_length=255)
    expire_date = models.DateField()
    count = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name
