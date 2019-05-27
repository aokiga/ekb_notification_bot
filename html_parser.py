'''
TODO
'''
from bs4 import BeautifulSoup
import requests

#Getting the html

page = requests.get('https://xn--90agdcm3aczs9j.xn--80acgfbsl1azdqr.xn--p1ai/#tab2')
soup = BeautifulSoup(page.text, 'html.parser')

#Getting discussions links

discussions = set()

for table in soup.find_all(attrs={'class' : 'ed-content js-tab2'}):
	discuss_links = table.find_all('a')
	for link in discuss_links:
		discussions.add(link.attrs['href'])

#Checking if there are any new discussions

new_discussions = set()

with open('saved/discussions.txt', 'r') as inFile:
	new_discussions = discussions.difference(set(map(str.rstrip, inFile)))

#Saving in out file

with open('saved/discussions.txt', 'w') as outFile:	
	print('\n'.join(discussions), file=outFile)
