import requests
import lxml
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
webpage_text = response.text

soup = BeautifulSoup(webpage_text, 'lxml')

all_titles = [t.getText() for t in soup.find_all(name='h3', class_='title')]
# print(all_titles)

while len(all_titles) > 0:
    movie = (all_titles.pop().encode('latin1')).decode('utf-8')

    with open('movies', mode='a', encoding='utf-8') as file:
        file.write(f'{movie}\n')
