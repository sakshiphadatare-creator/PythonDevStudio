import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# Uniform Resource Locator
# Write your code below this line 👇
response = requests.get(URL)
web_html = response.text
soup = BeautifulSoup(web_html, 'html.parser')
movie_title = soup.find_all(name="h3",class_='title')

list_of_movies = [item.getText() for item in movie_title]
movies = list_of_movies[::-1]

with open('movie.txt','w') as f:
    for movie in movies:
        f.write(f"{movie}\n")

# list_of_movies = [item.getText() for item in movie_title]
# for n in range(len(list_of_movies)-1,-1 ,-1):
#     print(list_of_movies[n])


