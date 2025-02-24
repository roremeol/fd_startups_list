from scrapy import Selector
import re
import sys
import os 

arg_separator=sys.argv[1:]

f = open(os.path.dirname(os.path.realpath(__file__)) + '/sites/unicamp.html')
sel = Selector(text=f.read())

cards = sel.css("a.meta")

startups = []
for card in cards:
    startup_name = card.xpath('@href').get()
    startup_info = card.xpath('@href').get()

    if startup_name is None:
        continue

    startups.append([startup_name.rsplit('/', 2)[1],startup_info])

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