from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

titles = soup.find_all("h3", class_="title")
article_titles = [title.getText() for title in titles]

with open("movies.txt", "w",encoding="utf-8") as file:
    for item in article_titles[: : -1]:
        file.write(f"{item}\n")