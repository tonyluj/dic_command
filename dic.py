#! /bin/env python2
import urllib2
import sys

from BeautifulSoup import BeautifulSoup


def get_translation(word):
    # get the content of the bing
    req = urllib2.Request("http://cn.bing.com/dict/search?q=" + word + "&go=&qs=bs&form=CM")
    content = urllib2.urlopen(req).read()

    # convert string to soup
    soup = BeautifulSoup(content)
    try:
        print word
        attrCount = len(soup.find("div", {"class": "qdef"}).findAll("span", {"class": "def"}))
        for i in range(attrCount - 1):
            print soup.find("div", {"class": "qdef"}).findAll("span", {"class": "pos"})[i].findAll(text=True)[0] + \
                  soup.find("div", {"class": "qdef"}).findAll("span", {"class": "def"})[i].findAll(text=True)[0]
    except Exception, ex:
        print "Not Found"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        get_translation()
    else:
        print "error: Please input some word"