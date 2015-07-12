from bs4 import BeautifulSoup
import requests
import re
from pga.models import Player
import django
import datetime


def strip_nonalphanum_re(word):
    return re.sub(r"^\W+|\W+$", "", word)


def get_name(s):
    splitter = s.split(',')
    first_name = strip_nonalphanum_re(splitter[1])
    last_name = strip_nonalphanum_re(splitter[0])
    full_name = first_name + ' ' + last_name
    return str(full_name)

BASE_URL = "http://www.golfchannel.com/tours/pga-tour/"
r = requests.get(BASE_URL)
r = r.text

# filename = 'golf_channel.html'
# r = ''
# f = open(filename, 'rU')
# for line in f:
#   r += line

soup = BeautifulSoup(r)

ldrbrd = soup.find('table', 'gc_leaderboard tablesorter')


for row in ldrbrd.find_all('tr', class_=re.compile(r'playerRow')):
    now = datetime.datetime.now()
    playerInfo = []
    col = row.find_all('td')
    if len(col) < 11:
        break
    player, created = Player.objects.get_or_create(
        name=get_name(col[3].find('a', class_='pName').string)
    )
