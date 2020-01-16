import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('http://services.runescape.com/m=itemdb_oldschool/Leaping+trout/viewitem?obj=11328').read()

soup = bs.BeautifulSoup(sauce,'lxml')

print(soup.title.string)

#print(soup.find_all('h3'))

for h3 in soup.find_all('h3'):
    print(h3.text)
