from bs4 import BeautifulSoup
import requests
from pga.models import Player, Tournament, Odd
import django
django.setup()

BASE_URL = "https://sports.bovada.lv/golf/pga-tour/the-barclays"
r = requests.get(BASE_URL)
r = r.text

soup = BeautifulSoup(r)

ldrbrd = soup.find('ul', )
