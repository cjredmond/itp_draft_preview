from django.db import models

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    paid = models.BooleanField(default=False)
    
