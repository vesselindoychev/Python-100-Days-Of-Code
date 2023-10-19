import requests
import lxml
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com')
webpage_text = response.text

soup = BeautifulSoup(webpage_text, 'lxml')

all_spans = soup.find_all(name='span', class_='titleline')
score_spans = soup.find_all(name='span', class_='score')

counter = 0
article_texts = []
article_links = []
article_upvotes = [int(ss.getText().split(' ')[0]) for ss in score_spans]
for span in all_spans:
    a_tag = span.find(name='a')
    article_texts.append(a_tag.getText())
    article_links.append(a_tag.get('href'))

print(article_upvotes)
largest_upvote = max(article_upvotes)
largest_index = article_upvotes.index(largest_upvote)
current_article_text = article_texts[largest_index]
current_article_link = article_links[largest_index]