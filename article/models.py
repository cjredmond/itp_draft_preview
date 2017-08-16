from django.db import models

class SummerNote(models.Model):
    title = models.CharField(max_length=40)
    paid_neccessary = models.BooleanField(default=True)

class HeadToHead(models.Model):
    title = models.CharField(max_length=50)
    paid_neccessary = models.BooleanField(default=True)

class FollowUp(models.Model):
    title = models.CharField(max_length=50)
    paid_neccessary = models.BooleanField(default=True)

class SlackChat(models.Model):
    title = models.CharField(max_length=50)
    paid_neccessary = models.BooleanField(default=True)
