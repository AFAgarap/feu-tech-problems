import os
import re
import requests
import urllib.request
from bs4 import BeautifulSoup

def fetch_media(url, filename, choice):
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html, 'html.parser')
	media = soup.find_all('meta', attrs={'content':''})

	write_file = open('index.html', 'w')
	write_file.write(str(media))
	write_file.flush(); write_file.close()

	read_file = open('index.html', 'r')
	media_link = ''
	for line in read_file:
		if (choice == 1 and 'jpg' in line):
			media_link = line; break
		elif (choice == 2 and 'https' in line and 'mp4' in line):
			media_link = line; break

	match = re.search('(?<=")(.+)(?<=")(\s)', media_link)
	media_url = match.group()
	media_url.rstrip()
	medial_url = media_url[:-2]
	urllib.request.urlretrieve(media_url, '{}.{}'.format(filename, 'jpg' if choice == 1 else 'mp4' if choice == 2 else '')) # video is still not working Error 400
	print('Success' if os.path.isfile('{}'.format(filename)) else 'Failed')
	# os.system('pause')

if __name__ == '__main__':
	choice = int(input("[1] Photo\n[2] Video\nChoice >> "))
	fetch_media(url=input("Enter URL: "), filename=input("Enter filename: "), choice=choice)
