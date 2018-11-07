import re

with open("C:\\xampp\\htdocs\\research\\frontend\\front.php", "r") as file:
    orig = file.read()
    text = orig.replace('\n', '')
    stringLength = len(text)

# develop a for loop for this section for the try block
try:
    found = re.search('<?php(.+?)?>', text).group(1)
    counter = text.index("?>")
    print(str(counter) + "\n")
    print(found + "\n")
except AttributeError:
    found = 'Not found in the original string'
    print(found)

file.close()
