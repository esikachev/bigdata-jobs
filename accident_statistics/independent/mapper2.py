#!/usr/bin/env python

import os
import sys

from BeautifulSoup import BeautifulSoup
import urllib2


for line in sys.stdin:
    line = line.strip()
    year, year_link = line.split()

    html_page = urllib2.urlopen(year_link)
    parsed_html = BeautifulSoup(html_page)

    for link in parsed_html.findAll('a'):
        if year in link.get("href"):
            print year, "{}/{}".format(os.path.dirname(year_link),
                                       link.get("href"))
