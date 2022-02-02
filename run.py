#coding: UTF-8

import requests
from bs4 import BeautifulSoup
from slack import Slack

url = 'https://koto-kosodate-portal.jp/smf/mizube/general/refresh_cal.php?center_cd=10' #東陽
url2 = 'https://koto-kosodate-portal.jp/smf/mizube/general/refresh_cal.php?center_cd=20' #大島
# url = 'https://koto-kosodate-portal.jp/smf/mizube/general/refresh_cal.php?center_cd=40' #南砂
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
result = soup.find_all('a', attrs={ 'class': lambda val: val in ['bgG', 'bgB'] }) 

if result:
   print('result:',result)
   Slack(10).post()
else:
   print('result is empty:',result)
   Slack(10).post()

# ---------------------------

res2 = requests.get(url2)
soup2 = BeautifulSoup(res2.text, 'html.parser')

result2 = soup2.find_all('a', attrs={ 'class': lambda val: val in ['bgG', 'bgB'] })

if result2:
   print('result２:',result2)
   Slack(20).post()
else:
   print('result2 is empty:',result2)
   # Slack(20).post()