from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Nom unique de la salle
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création
    host = models.ForeignKey(User, on_delete=models.CASCADE)  # L'hôte de la salle
    active = models.BooleanField(default=True)  # État de la salle (active ou non)

    def __str__(self):
        return self.name
