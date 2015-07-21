from bs4 import BeautifulSoup
import requests
from pga.models import Player, Tournament, Odd
import django
django.setup()

BASE_URL = "http://www.vegasinsider.com/golf/odds/futures/"
r = requests.get(BASE_URL)
r = r.text

soup = BeautifulSoup(r)

ldrbrd = soup.find('div', {"id": "oddsplayers"})

players = []

for row in ldrbrd.find_all('tr'):
    col = row.find_all('td')
    if len(col) > 1 and col[1].string != 'Golfer' and col[0].string != 'Golfer':
        player, created = Player.objects.get_or_create(
            name=col[0].string.strip()
        )
        tournament = Tournament.objects.get(name="British Open")
        odd, created = Odd.objects.get_or_create(
            player=player,
            tournament=tournament,
            odds_to_win=col[1].string
        )
