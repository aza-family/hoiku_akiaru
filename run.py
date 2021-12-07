#coding: UTF-8

import requests
from bs4 import BeautifulSoup
from slack import Slack

#url = 'https://koto-kosodate-portal.jp/smf/mizube/general/refresh_cal.php?center_cd=20' #大島
url = 'https://koto-kosodate-portal.jp/smf/mizube/general/refresh_cal.php?center_cd=10' #東陽
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

result = soup.find_all('p', attrs={'style':'color:#000000;background-color:#00bfff;border:solid 1px;'})

if result:
    print('result:',result)
    Slack.post()
else:
   print('result is empty:',result)
   #Slack.post()

# --- Slack Post ---

