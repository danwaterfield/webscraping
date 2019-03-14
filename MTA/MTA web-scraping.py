# Followed the instructions from https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460



# Imports libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Sets URL
url = 'http://web.mta.info/developers/turnstile.html'


response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

for i in range(36,len(soup.findAll('a'))+1): #'a' tags are for links
    one_a_tag = soup.findAll('a')[i]
    link = one_a_tag['href']
    download_url = 'http://web.mta.info/developers/'+ link
    urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 
 #pause the code for a sec
    time.sleep(1) 