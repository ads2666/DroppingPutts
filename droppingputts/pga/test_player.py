import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DP.droppingputts.settings")


from models import Player

player = Player(
    name='test123'
)
player.save()
