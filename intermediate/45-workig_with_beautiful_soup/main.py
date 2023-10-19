from bs4 import BeautifulSoup
import lxml

with open('website.html') as html_file:
    contents = html_file.read()
    # print(contents)

soup = BeautifulSoup(contents, 'html.parser')

# print(soup.h1)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.p)
# print(soup.prettify())
all_tags = soup.find_all(name='a')

for tag in all_tags:
    # print(tag.getText())
    print(tag.get('href'))

specific_url = soup.select_one(selector='p a')
print(specific_url)

headings = soup.select(selector='.heading')
print(headings)