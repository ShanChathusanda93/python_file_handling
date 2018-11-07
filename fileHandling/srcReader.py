import re

# for windows
# with open("C:\\xampp\\htdocs\\research\\frontend\\front.php", "r") as file:
#     orig = file.read()
#     text = orig.replace('\n', '')
#     stringLength = len(text)

# for ubuntu
# did not work well like windows. Please reconsider
with open("/home/shan/php_codes/simple_php_project/frontend/front.php", "r") as file:
    orig = file.read()
    text = orig.replace('\n', '')
    stringLength = len(text)

try:
    found = re.search('<?php(.+?)?>', text).group(1)
    counter = text.index("?>")
    print(str(counter) + "\n")
    print(found + "\n")
except AttributeError:
    found = 'Not found in the original string'
    print(found)

file.close()
