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
    discussions = []
    for table in get_html_tree().find_all(
            attrs={'class': 'ed-content js-tab2'}):
        for block in table.find_all(attrs={'class': 'title'}):
            discuss_name = block.find('a')
            discuss_date = block.find(attrs={'class': 'date'})
            discussions.append((
                discuss_name.text,
                discuss_name.attrs['href'],
                discuss_date.text))
    return discussions


# Checking if there are any new discussions
def get_new_discussions():
    new_discussions = set()
    with open('discussions.txt', 'r') as inFile:
        try:
            prev_discussions = eval(inFile.read())
        except SyntaxError:
            return get_discussions()
    new_discussions = [i for i in get_discussions()
                       if i not in prev_discussions]
    return new_discussions


# Saving in out file
def save_discussions():
    with open('discussions.txt', 'w') as outFile:
        print(repr(get_discussions()), file=outFile)
