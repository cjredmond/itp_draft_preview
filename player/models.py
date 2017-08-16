from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=2)
    school = models.ForeignKey(School)
    school_class = models.CharField(max_length=20)
    age = models.IntegerField()
    weight = models.IntegerField()
    height = models.CharField(max_length=100)
    hometown = models.CharField(max_length=100)
    highschool = models.CharField(max_length=100)
    fourty = models.FloatField(null=True,blank=True)
    ten_yard = models.FloatField(null=True,blank=True)
    bench = models.FloatField(null=True,blank=True)
    cone = models.FloatField(null=True,blank=True)
    short_shut = models.FloatField(null=True,blank=True)
    sixty = models.FloatField(null=True,blank=True)
    vertical = models.FloatField(null=True,blank=True)
    broad = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.name
