import requests
from bs4 import BeautifulSoup

def _request(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'lxml')

	quotes = soup.find_all('div', class_='feed__item l-island-round')

	_reqOut = str()

	for quote in quotes:

		if quote:
			
			title = quote.find('div', class_='content-title content-title--short l-island-a')
			
			#Заголовок
			if title:
				title = title.get_text().replace("Статьи редакции", '').strip(' \n\t')
			

			#data-content-id
			post_id = quote.find('div', attrs={'data-content-id' : True})
			if post_id:
				post_id = post_id.get_text()
			print(post_id)

			

		_reqOut += (title + '\n')

	print(_reqOut)
	
	return _reqOut


_request('https://dtf.ru/gameindustry/entries/new')