from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name


class Score(models.Model):
    player = models.ForeignKey(Player)
    tournament = models.ForeignKey(Tournament)
    round_one = models.CharField(max_length=10)
    round_two = models.CharField(max_length=10)
    round_three = models.CharField(max_length=10)
    round_four = models.CharField(max_length=10)
    overall = models.CharField(max_length=10)

    def __str__(self):
        return self.player + self.overall
