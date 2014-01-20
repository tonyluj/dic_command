#! /bin/env python2
import urllib2,sys
from BeautifulSoup import BeautifulSoup
# get the word from commond
word = sys.argv[1]

# get the content of the bing
req = urllib2.Request("http://cn.bing.com/dict/search?q=" + word  + "&go=&qs=bs&form=CM")
content = urllib2.urlopen(req).read()

# convert string to soup
soup = BeautifulSoup(content)
try:
    print word
    attrCount = len(soup.find("div",{"class":"qdef"}).findAll("span",{"class":"def"}))
    for i in range(0, attrCount - 1):
        print soup.find("div",{"class":"qdef"}).findAll("span",{"class":"pos"})[i].findAll(text=True)[0] + soup.find("div",{"class":"qdef"}).findAll("span",{"class":"def"})[i].findAll(text=True)[0] 
except Exception,ex:
    print "Not Found"
