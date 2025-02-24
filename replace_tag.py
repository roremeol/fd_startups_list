import re
import os
import json

# read all tables/.md files
readmefiles = []
for root, dirs, files in os.walk(os.path.dirname(os.path.realpath(__file__)) + "/tables/"):
    for file in files:
        if file.endswith(".md"):
             readmefiles.append(os.path.join(root, file))

# load README.md
with open(os.path.dirname(os.path.realpath(__file__)) + '/README.md', 'r') as file:
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
with open(os.path.dirname(os.path.realpath(__file__)) + '/README.md', "w") as f:
    f.write(readme_data)
    