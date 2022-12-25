import requests
import random
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import os


def getPostImg(image_url, name, path):
	img_data = requests.get(image_url).content
	imgPath = str(path + name)
	with open(imgPath, 'wb') as handler:
		handler.write(img_data)
	print(name, 'is on device')

def genNameImg():
	name = str('img_' + curDate() + '_' + str(random.randint(1000000, 9999999)) + '.jpg')
	return name

def curDate():
	curDay = str(datetime.now().day)
	curMonth = str(datetime.now().month)
	curYear = str(datetime.now().year)
	curSecond= str(datetime.now().second)
	curMinute = str(datetime.now().minute)
	curHour = str(datetime.now().hour)

	fullDate = curDay + curMonth + curYear + curHour + curMinute + curSecond

	return fullDate

def _request(url):


	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'lxml')

	quotes = soup.find_all('div', class_='content-title content-title--short l-island-a')
	images = soup.find_all('div', class_= "andropov_image")
	avatars = soup.find_all('img', class_= "andropov_image")

	n = 1
	for quote in quotes:

		print(str(n)+".", quote.text.replace("Статьи редакции", '').strip(' \n\t'))

		n += 1

	n = 1

	for image in images:
		if image.has_attr('data-image-src'):
			print(str(n) + '. ' + image['data-image-src'])
			nameImg = image['data-image-src']
			getPostImg(nameImg, genNameImg(), 'images/postImages/')
		n += 1
	for avatar in avatars:
		if avatar.has_attr('data-image-src'):
			print(str(n) + '. ' + image['data-image-src'])
			nameImg = avatar['data-image-src']
			getPostImg(nameImg, genNameImg(), 'images/userProfileAvatars/')
		n += 1

def clearDir(dir): 
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

_request('https://dtf.ru/')

def closePr():
	clearDir('images/postImages')
	clearDir('images/userProfileAvatars/')

input()
closePr()