from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
links = soup.find_all("span", class_="titleline")
articles = []
for span in links:
    if span.find("a"):
        articles.append({
            "title": span.find("a").getText(),
            "href": span.find("a").get("href")
                         })

print(articles)