from scrapy import Selector
import re
import sys
import os 
import json

# checa de dois arrays sao iguais
def checkEqual(a, b):
    n, m = len(a), len(b)
    if n != m:
        return False

    mp = {}
    for num in a:
        mp[num] = mp.get(num, 0) + 1

    for num in b:
        if num not in mp:
            return False
        if mp[num] == 0:
            return False
        mp[num] -= 1
    return True

json_parser_file=sys.argv[1:]
if len(json_parser_file)>=1:
    json_parser_file=json_parser_file[0]
else:
    json_parser_file=""

root_path = os.path.dirname(os.path.realpath(__file__))

# checa existencia do parse json
path = os.path.join(root_path, json_parser_file)
if os.path.isfile(path) != True:
    print("O arquivo descritor do parser não existe! ({})".format(path))
    sys.exit(-1) 

# carrega o parse json
with open(path, 'r') as json_data:
    json_parser = json.loads(json_data.read())
    json_data.close()

# checa integidade do parse json
if 'html_file' not in json_parser:
    print("A chave `html_file` não existe no parser")
    sys.exit(-2) 
if 'root_selector' not in json_parser:
    print("A chave `root_selector` não existe no parser")
    sys.exit(-2) 
if 'columns' not in json_parser:
    print("A chave `columns` não existe no parser")
    sys.exit(-2) 

# checa existencia do dump html
path = os.path.join(root_path, json_parser['html_file'])
if os.path.isfile(path) != True:
    print("O dumb do html é inexistente! ({})".format(path))
    sys.exit(-1) 

# carrega o dump do html 
f = open(path, 'r')
sel = Selector(text=f.read())
f.close()

root = sel.css(json_parser['root_selector'])

# loop no filhos do no  
startups = []
heads=[]
for child in root:
    startup = []

    # loop nas colunas da tabela
    for col in json_parser['columns']:
        if len(heads) < len(json_parser['columns']):
            heads.append( (col['name'] if 'name' in col else "") )

        node = ""
        if ('selector' in col) or ('xpath' in col) or ('eval' in col):
            node = child
            if 'selector' in col:
                node = node.css(col['selector'])
            if 'xpath' in col:
                node = node.xpath(col['xpath'])
            if node != child:
                node = node.get()
                if node is None:
                    node = ""
                node = node.replace('\r', '').replace('\n', '').strip()
                if 'eval' in col:
                    node = eval(col['eval'].replace("%var%", "node"))

        startup.append(node)

    if checkEqual(startup,["" for h in heads]) != True:
        startups.append(startup)

if 'separator' in json_parser:
    separator=json_parser['separator']
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