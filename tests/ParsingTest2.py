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
			author = quote.find('div', class_='l-island-a')
			subtitle = quote.find('div', class_='content-container')

			if author:
				author_text = author.find('a')

			if subtitle:
				subtitle_text = subtitle.find('p')



		if title:
			#print(title.get_text().replace("Статьи редакции", '').strip(' \n\t'))
			title = title.get_text().replace("Статьи редакции", '').strip(' \n\t')

		if subtitle_text:
			#print(subtitle_text.get_text().replace("Статьи редакции", '').strip(' \n\t'))
			subtitle_text = subtitle_text.get_text().replace("Статьи редакции", '').strip(' \n\t')

		if author_text:
			#print(author_text.get_text().strip(' \n\t'))
			author_text = author_text.get_text().strip(' \n\t')

		_reqOut += [[author_text, title, subtitle_text]]

	return _reqOut


print(_request('https://dtf.ru/'))

input()