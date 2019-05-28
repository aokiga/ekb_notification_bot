'''
TODO
'''
from bs4 import BeautifulSoup
import requests

URL = 'https://xn--90agdcm3aczs9j.xn--80acgfbsl1azdqr.xn--p1ai/#tab2'


# Getting the html
def get_html_tree():
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


# Getting discussions links
def get_discussions():
    discussions = set()
    for table in get_html_tree().find_all(
            attrs={'class': 'ed-content js-tab2'}):
        discuss_links = table.find_all('a')
        for link in discuss_links:
            discussions.add((link.text, link.attrs['href']))
    return discussions


# Checking if there are any new discussions
def get_new_discussions():
    new_discussions = set()
    with open('discussions.txt', 'r') as inFile:
        new_discussions = get_discussions().difference(
            set(map(str.rstrip, inFile)))
    return new_discussions


# Saving in out file
def save_discussions():
    with open('discussions.txt', 'w') as outFile:
        print('\n'.join(map(lambda a: ' '.join(a),
              get_discussions())), file=outFile)
