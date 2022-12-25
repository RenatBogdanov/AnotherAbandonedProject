import requests
from bs4 import BeautifulSoup

def _request(url):


	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'lxml')

	quotes = soup.find_all('div', class_='content-title content-title--short l-island-a')
	images = soup.find_all('img', class_= "andropov_image")

	n = 1
	for quote in quotes:

		print(str(n)+".", quote.text.replace("Статьи редакции", '').strip(' \n\t'))

		n += 1

	n = 1

	for image in images:
		if image.has_attr('data-image-src'):
			print(str(n) + '. ' + image['data-image-src'])
		n += 1

_request('https://dtf.ru/')
input()

#data-image-src