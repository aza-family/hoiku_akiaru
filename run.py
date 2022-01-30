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
#result = soup.find_all('a', attrs={'class':'bgG'})
#result = soup.find_all('div', attrs={'class':'full'})
#result = soup.find_all('p', attrs={'style':'margin: 0 5px 5px 0;'})
#result2 = soup.find_all('p', attrs={'style':'color:#000000;background-color:#00bfff;border:solid 1px;'})

if result:
   print('result:',result)
   Slack.post(10)
else:
   print('result is empty:',result)
   #Slack.post()

# if result2:
#     print('result2:',result2)
#     Slack.post()
# else:
#    print('result2 is empty:',result2)
   #Slack.post()
# --- Slack Post ---

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