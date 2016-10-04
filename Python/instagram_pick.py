import os
import re
import requests
import urllib.request
from bs4 import BeautifulSoup

def fetch_image(url, filename):
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html, 'html.parser')
	images = soup.find_all('meta', attrs={'content':''})

	write_file = open('index.html', 'w')
	write_file.write(str(images))
	write_file.flush(); write_file.close()

	read_file = open('index.html', 'r')
	jpg = ''
	for line in read_file:
		if ('jpg' in line):
			jpg = line; break

	match = re.search('(?<=")(.+)(?<=")(\s)', jpg)
	jpg_url = match.group()
	urllib.request.urlretrieve(jpg_url, '{}.jpg'.format(filename))
	print('Success' if os.path.isfile('{}.jpg'.format(filename)) else 'Failed')

if __name__ == '__main__':
	fetch_image(input("Enter URL: "), input("Enter a filename for the photo: "))
