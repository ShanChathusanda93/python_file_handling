import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

# print(page.status_code)
# print(page.headers)
page_content = page.content

soup = BeautifulSoup(page_content, 'html.parser')

# Print with indentations
# print(soup.prettify())

top_level = list(soup.children)
print("\n-------------------- 001 -----------------")
print(top_level)

# What the type of each element in the list
tag_type_list = [type(item) for item in list(soup.children)]
print("\n-------------------- 002 -----------------")
print(tag_type_list)

# Select the html tag and its children by taking the third item in the list
html = top_level[2]
print("\n-------------------- 003 -----------------")
print(html)

# Find the children inside the html tag
next_level = list(html.children)
print("\n-------------------- 004 -----------------")
print(next_level)

# Go into body part and extract p tag
body = next_level[3]

# Get the p tag by finding the children of the body tag
bottom_level = list(body.children)
print("\n-------------------- 005 -----------------")
print(bottom_level)

# Isolate the p tag
p = bottom_level[1]
print("\n-------------------- 006 -----------------")
print(p)

# Extract all of the text inside the tag
text = p.get_text()
print("-------------------- 007 -----------------")
print('\n' + text)


# All instances
p = soup.find_all('p')
print("-------------------- 008 -----------------")
print(p[0].get_text())

# First instance only
p = soup.find('p')
print("-------------------- 009 -----------------")
print(p.get_text())
