from django.db import models
from player.models import School, Player

class Game(models.Model):
    home = models.ForeignKey(School, related_name='home')
    away = models.ForeignKey(School, related_name='away')
    kickoff = models.DateTimeField()

    def __str__(self):
        return self.home.name + ' vs ' + self.away.name

class Report(models.Model):
    player = models.ForeignKey(Player)
    game = models.ForeignKey(Game)
    athletic_ability = models.FloatField()
    athletic_ability_desc = models.TextField()
    football_intelligence = models.FloatField()
    football_intelligence_desc = models.TextField()
    toughness = models.FloatField()
    toughness_desc = models.TextField()
    play_speed = models.FloatField()
    play_speed_desc = models.TextField()
    pos_athletic_ability = models.FloatField()
    pos_athletic_ability_desc = models.TextField()
    pos_football_intelligence = models.FloatField()
    pos_football_intelligence_desc = models.TextField()
    pos_toughness = models.FloatField()
    pos_toughness_desc = models.TextField()
    pos_play_speed = models.FloatField()
    pos_play_speed_desc = models.TextField()
    strength = models.TextField()
    weakness = models.TextField()
    summary = models.TextField()

    def __str__(self):
        return self.player.name + ' ' + self.game.__str__()

    @property
    def trait_avg(self):
        return (self.athletic_ability + self.football_intelligence + self.toughness + self.play_speed + self.football_intelligence ) / 5

    def pos_avg(self):
        return (self.pos_athletic_ability + self.pos_football_intelligence + self.pos_toughness + self.pos_play_speed + self.pos_football_intelligence ) / 5
