import os
import re
import requests
import sys
import urllib.request
import webbrowser
from bs4 import BeautifulSoup

def fetch_media(url, filename, choice):
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html, 'html.parser')
	media = soup.find_all('meta', attrs={'content':''})

	with open('index.html', 'w') as write_file:
		write_file.write(str(media))

	with open('index.html', 'r') as read_file:
		media_link = ''
		for line in read_file:
			if (choice == 1 and 'jpg' in line):
				media_link = line; break
			elif (choice == 2 and ('https' in line and 'mp4' in line)):
				media_link = line; break

	match = re.search('(?<=")(.+)(?<=")(\s)', media_link)
	media_url = match.group()
	medial_url = media_url[:-3]
	if (sys.platform == 'linux'):
		os.system('wget --output-document={}.{} \"{}'.format(filename, 'jpg' if choice == 1 else 'mp4' if choice == 2 else '', media_url))
		print('Success' if os.path.isfile('{}.{}'.format(filename, 'jpg' if choice == 1 else 'mp4' if choice == 2 else '')) else 'Failed')
	elif (sys.platform == 'win32'):
		webbrowser.open_new(media_url)
		os.system('pause')

if __name__ == '__main__':
	choice = int(input("[1] Photo\n[2] Video\nChoice >> "))
	fetch_media(url=input("Enter URL: "), filename=input("Enter filename: "), choice=choice)
