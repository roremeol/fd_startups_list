from scrapy import Selector
import re
import sys
import os 
from urllib.parse import urlparse

arg_separator=sys.argv[1:]

f = open(os.path.dirname(os.path.realpath(__file__)) + '/sites/puc-rio.html')
sel = Selector(text=f.read())

cards = sel.css('.eael-filterable-gallery-item-wrap')

startups = []
for card in cards:
    startup_name = card.css('.eael-gallery-grid-item > a').xpath('@href').get()
    startup_info = card.css('.eael-gallery-grid-item > a').xpath('@href').get()

    if startup_name=="#":
        continue

    startups.append([urlparse(startup_name).netloc,startup_info])

heads=["Nome","Descrição","Link","CTO","Tech Leader","Área de atuação"]

# Possibilita input de separador via argv
if len(arg_separator)>0:
    separator=arg_separator[0]
else:
    separator=" | "

print(separator.join(heads))
if separator==" | ":
    print(separator.join([re.sub(r"[^`]", "-", h) for h in heads]))
for startup in startups:
    if len(startup) == len(heads):
         print(separator.join(startup))
    elif len(startup) < len(heads):
        print(separator.join(startup), separator ,separator.join([re.sub(r"[^`]", "", h) for h in heads[len(startup)-len(heads):]]))