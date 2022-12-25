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
	#print(name, 'is on device')

def genNameImg(name):
	name = str('img_' + curDate() + '_' + name + '.jpg')
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

	quotes = soup.find_all('div', class_='feed__item l-island-round')

	_reqOut = []

	for quote in quotes:

		if quote:
			
			title = quote.find('div', class_='content-title content-title--short l-island-a')
			
			#Заголовок
			if title:
				title = title.get_text().replace("Статьи редакции", '').strip(' \n\t')

			#Автор или подсайт
			author = quote.find('div', class_='l-island-a')
			
			if author:
				author_text = author.find('a')
				if author_text:
					author_text = author_text.get_text().strip(' \n\t')

			#Подзаголовок
			subtitle = quote.find('div', class_='content-container')

			if subtitle:
				subtitle_text = subtitle.find('p')

				if subtitle_text:
					#print(subtitle_text.get_text().replace("Статьи редакции", '').strip(' \n\t'))
					subtitle_text = subtitle_text.get_text().replace("Статьи редакции", '').strip(' \n\t')

			#Изображение
			image = quote.find('div', class_= "andropov_image")
			if image:
				urlImg = image['data-image-src']
				nameImg = image['data-image-src'].replace('https://leonardo.osnova.io/', '').replace('/', '')
				getPostImg(urlImg, genNameImg(nameImg), 'images/postImages/')

			#Аватар
			avatar = quote.find('img', class_= "andropov_image")
			if avatar:
				urlAvatar = avatar['data-image-src']
				nameAvatar = avatar['data-image-src'].replace('https://leonardo.osnova.io/', '').replace('/', '')
				getPostImg(urlAvatar, genNameImg(nameImg), 'images/userProfileAvatars/')

		#Добавление информации в массив массивов
		_reqOut += [[author_text, nameAvatar, title, subtitle_text, nameImg]]
	#print(_reqOut)
	
	return _reqOut

def clearDir(dir): 
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

_request('https://dtf.ru/')

def closePr():
	clearDir('images/postImages')
	clearDir('images/userProfileAvatars/')

input()
closePr()