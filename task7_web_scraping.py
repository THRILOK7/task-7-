# task7_web_scraping.py

import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Scrape the site
url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all("span", class_="titleline")

# Step 2: Prepare data
top_articles = []
for i, title in enumerate(titles[:10], start=1):
    link = title.find("a")
    article = {
        "Rank": i,
        "Title": link.text,
        "URL": link.get("href")
    }
    top_articles.append(article)
    print(f"{i}. {link.text}")

# Step 3: Save to CSV
with open("scraped_data.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Rank", "Title", "URL"])
    writer.writeheader()
    writer.writerows(top_articles)

print("\n✅ Saved top articles to 'scraped_data.csv'")
