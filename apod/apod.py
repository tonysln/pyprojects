# IMPORTS
from urllib.request import urlopen
import urllib.request as req
import os
from bs4 import BeautifulSoup as bs
from datetime import date

# GET DATE
today = str(date.today())

# LOAD PAGE, PARSE HTML, FIND IMG, GET URL
nasapage = urlopen('https://apod.nasa.gov/apod/astropix.html')
soup = bs(nasapage, 'html.parser')
imganchor = soup.img.parent['href']
imgurl = f"https://apod.nasa.gov/apod/{imganchor}"

# CREATE DIRECTORY, GET PHOTO, NAME PHOTO
dir = 'NASA Astronomy Picture of the Day'
if not os.path.exists(dir):
		os.makedirs(dir)

imgname = today
req.urlretrieve(imgurl, f"{dir}/{imgname}.jpg")

print(f"Image downloaded for {today}")
