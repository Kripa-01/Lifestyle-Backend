from sqlalchemy.orm import Session
from database import SessionLocal
from models import Listing

data = [
    {
        "title": "Pizza Hut",
        "description": "Famous pizza restaurant",
        "category": "restaurant",
        "city": "Calicut",
        "rating": 4.2
    },
    {
        "title": "Burger King",
        "description": "Popular fast food chain",
        "category": "restaurant",
        "city": "Calicut",
        "rating": 4.0
    }
]

# DB session
db = SessionLocal()

for item in data:
    listing = Listing(
        title=item["title"],
        description=item["description"],
        category=item["category"],
        city=item["city"],
        rating=item["rating"]
    )
    
    db.add(listing)

db.commit()
db.close()

print("Data saved to DB")