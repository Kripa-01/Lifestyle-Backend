import requests
from bs4 import BeautifulSoup

from database import SessionLocal
from models import Listing

def get_rating(tag):
    classes = tag.get("class", [])
    ratings = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    for c in classes:
        if c in ratings:
            return ratings[c]
    return 0

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

db = SessionLocal()

for book in books:
    title = book.h3.a["title"]

    rating_tag = book.find("p", class_="star-rating")
    rating = get_rating(rating_tag)

    description = f"{title} is a popular book"

    listing = Listing(
        title=title,
        description=description,
        category="Books",
        city="Calicut",
        rating=rating
    )

    db.add(listing)

db.commit()
db.close()

print("Scraped data with rating saved to DB")