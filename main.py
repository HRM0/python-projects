from bs4 import BeautifulSoup
import requests

#dateToLookUp = input("What year would you like to travel to? (YYYY-MM-DD) ")
dateToLookUp = "2005-07-01"
response = requests.get(f"https://www.billboard.com/charts/hot-100/{dateToLookUp}/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
betterSoup = soup.select("li ul li h3", id="title-of-a-story")
titles = []
for title in betterSoup:
    titles.append(title.get_text().strip())

print(titles)
