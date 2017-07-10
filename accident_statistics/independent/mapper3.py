#!/usr/bin/env python

import sys

from BeautifulSoup import BeautifulSoup
import urllib2
import re

SELECT_FIELDS = ("AC Type", "Aboard", "Fatalities")

for line in sys.stdin:
    line = line.strip()
    year, year_link = line.split()
    
    html_page = urllib2.urlopen(year_link)
    parsed_html = BeautifulSoup(html_page)

    dict_table = dict()

    table = parsed_html.findAll('tr')
    for row in table:
        columns = row.findAll("td")
        dict_key = columns[0].getText().replace('\n       ', "")[:-1]
        if dict_key in SELECT_FIELDS:
            dict_table["".join(dict_key.split())] = (
                columns[1].getText())

    print ("{year} '{ac_type}' 1 {aboard} "
           "{fatalities}".format(year=year, ac_type=dict_table["ACType"],
                                 aboard=dict_table["Aboard"].split()[0],
                                 fatalities=dict_table["Fatalities"].split()[0]))
