from django.db import models

class Scout(models.Model):
    name = models.CharField(max_length=100)
    
