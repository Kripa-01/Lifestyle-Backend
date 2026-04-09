from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Listing

# ✅ Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Server running 🚀"}

# Create Listing
@app.post("/listings")
def create_listing(title: str, description: str, category: str, city: str, rating: float, db: Session = Depends(get_db)):
    listing = Listing(
        title=title,
        description=description,
        category=category,
        city=city,
        rating=rating
    )
    db.add(listing)
    db.commit()
    db.refresh(listing)
    return listing

# Get Listings
@app.get("/listings")
def get_listings(db: Session = Depends(get_db)):
    return db.query(Listing).all()