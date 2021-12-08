#coding: UTF-8

import requests
from bs4 import BeautifulSoup
from slack import Slack

# url = 'https://koto-kosodate-portal.jp/smf/mizube/general/refresh_cal.php?center_cd=20' #大島
url = 'https://koto-kosodate-portal.jp/smf/mizube/general/refresh_cal.php?center_cd=10' #東陽
# url = 'https://koto-kosodate-portal.jp/smf/mizube/general/refresh_cal.php?center_cd=40' #南砂
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
# print('soup:',soup)

#color:#000000;background-color:#87ceeb;border:solid 1px;
result = soup.find_all('p', attrs={'style':'color:#000000;background-color:#87ceeb;border:solid 1px;'})
#result = soup.find_all('p', attrs={'style':'margin: 0 5px 5px 0;'})
result2 = soup.find_all('p', attrs={'style':'color:#000000;background-color:#00bfff;border:solid 1px;'})

if result:
    print('result:',result)
    Slack.post()
else:
   print('result is empty:',result)
   #Slack.post()

if result2:
    print('result:',result2)
    Slack.post()
else:
   print('result is empty:',result2)
   #Slack.post()
# --- Slack Post ---

