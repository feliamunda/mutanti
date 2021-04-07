from django.db import models

# Create your models here.

class Human(models.Model):
    dna = models.JSONField()
    mutant = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)