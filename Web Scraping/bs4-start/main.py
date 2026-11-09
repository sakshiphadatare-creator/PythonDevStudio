from bs4 import BeautifulSoup
# Download the data from that website.
import requests
responses = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = responses.text

soup = BeautifulSoup(yc_web_page,"html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_tags = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_tags.append(link)

article_upvotes = [int(score.getText().split()[0])  for score in soup.find_all(name="span", class_="score") ]
largest_number= max(article_upvotes)
print(largest_number)

largest_index = article_upvotes.index(largest_number)
print(largest_index)
print(article_texts[largest_index])
print(article_tags[largest_index])

print("_________________________________________________________________")

print(article_texts)
print(article_tags)
print(article_upvotes)

# article_upvotes = []
# article_upvote = soup.find_all(name="span", class_="score")
# for upvote in article_upvote:
#     score = upvote.getText()
#     article_upvotes.append(score)
# print(article_upvotes)