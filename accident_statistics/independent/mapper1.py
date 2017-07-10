#!/usr/bin/env python

import os

from BeautifulSoup import BeautifulSoup
import urllib2

URL_OF_DATASET = "http://www.planecrashinfo.com/database.htm"
FORK_OF_YEARS = xrange(1920, 2018)

html_page = urllib2.urlopen(URL_OF_DATASET)
parsed_html = BeautifulSoup(html_page)

for link in parsed_html.findAll('a'):
    current_link = link.get('href')

    if current_link[0] == "/":
        year = current_link[1:5]
    else:
        year = current_link[0:4]

    try:
        if int(year) in FORK_OF_YEARS:
            print year, "{}/{}".format(os.path.dirname(URL_OF_DATASET),
                                       current_link)
    except ValueError:
        continue
