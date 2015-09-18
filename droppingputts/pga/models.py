from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published', null=True)

    def __str__(self):
        return self.name


class Score(models.Model):
    player = models.ForeignKey(Player)
    tournament = models.ForeignKey(Tournament)
    round_one = models.CharField(max_length=10, null=True)
    round_two = models.CharField(max_length=10, null=True)
    round_three = models.CharField(max_length=10, null=True)
    round_four = models.CharField(max_length=10, null=True)
    overall = models.CharField(max_length=10, null=True)
    total_strokes = models.IntegerField(null=True)
    position = models.CharField(max_length=10)

    def __str__(self):
        return self.player.name + self.overall

    def made_cut(self):
        if self.position == 'CUT':
            return False
        else:
            return True


class Odd(models.Model):
    player = models.ForeignKey(Player)
    tournament = models.ForeignKey(Tournament)
    odds_to_win = models.CharField(max_length=10)

    def __str__(self):
        return self.player.name


class Pick(models.Model):
    user = models.ForeignKey(User)
    tournament = models.ForeignKey(Tournament)
    pick_one = models.ForeignKey(Player, related_name='pick_one')
    pick_two = models.ForeignKey(Player, related_name='pick_two')
    pick_three = models.ForeignKey(Player, related_name='pick_three')
    pick_four = models.ForeignKey(Player, related_name='pick_four')

    def __str__(self):
        return self.user.name, self.pick_one.name, self.pick_two.name,
        self.pick_three.name, self.pick_four.name
