import requests
from bs4 import BeautifulSoup

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
				nameImg = image['data-image-src'].replace('https://leonardo.osnova.io/', '').replace('/', '')

			#Аватар
			avatar = quote.find('img', class_= "andropov_image")
			if avatar:
				nameAvatar = avatar['data-image-src'].replace('https://leonardo.osnova.io/', '').replace('/', '')

		#Добавление информации в массив массивов
		_reqOut += [[author_text, nameAvatar, title, subtitle_text, nameImg]]

	
	return _reqOut


print(_request('https://dtf.ru/'))

input()