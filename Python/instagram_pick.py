import os
import re
import requests
from bs4 import BeautifulSoup

def fetch_image(url):
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
	os.system('firefox "{}'.format(match.group()))
#	os.system('wget "{}'.format(match.group()))	# for Linux only

if __name__ == '__main__':
	fetch_image(input("Enter URL: "))
