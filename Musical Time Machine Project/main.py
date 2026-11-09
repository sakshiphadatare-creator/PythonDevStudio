import requests
from bs4 import BeautifulSoup
date = input("which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/135.0.0.0 Safari/537.36"}
url = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(url=url, headers= header)
soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]


