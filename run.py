#coding: UTF-8

import requests
from bs4 import BeautifulSoup
from slack import Slack

url = 'https://koto-kosodate-portal.jp/smf/mizube/general/refresh_cal.php?center_cd=20'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

result = soup.find_all('p', attrs={'style':'background-color:White;font-size:10pt;border-collapse:collapse;'})

if result:
    print('result:',result)
    Slack.post()
else:
   print('result is empty:',result)
   #Slack.post()

# --- Slack Post ---

