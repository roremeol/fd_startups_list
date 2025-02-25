import re
import os
import json

# read all tables/.md files
readmefiles = []
path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"tables")
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".md"):
             readmefiles.append(os.path.join(root, file))

# load README.md
path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"README")
with open(path, 'r') as file:
  readme_data = file.read()

# match pattern (<variable-*.?-tag>)(`*.?`)
# example: (<variable-VERSION-tag>)(`1.1`)
for filename in readmefiles:
    basename = os.path.basename(filename)

    with open(filename,"r") as f:
      content = f.read()
    
    # update readme variables
    # Replace the target string
    readme_data = readme_data.replace('![[' + basename + ']]', content)

# white README.md
path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"README.md")
with open(path, "w") as f:
    f.write(readme_data)
    