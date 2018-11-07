import requests
from bs4 import BeautifulSoup
# import codecs

payload = {"uname": "sc9214", "upwd": "abcd1234"}

page = requests.get("https://en.wikipedia.org/wiki/University_of_Ruhuna")

print("Status Code : " + str(page.status_code))
print("Page Headers : " + str(page.headers))

page_content = page.content
soup = BeautifulSoup(page_content, 'html.parser')

# Print with indentations
print(soup.prettify())

# f = codecs.open("F:\\Year_4_Sem_1\\CSC4046-Individual-Research\\2018\\my-work\\Extracted Source Codes\\"
#                 "UoR_wiki_from_python\\uor-wiki-python.html", "a", encoding='utf-8')
# f.write(str(soup.prettify()))

