from sqlalchemy import Column, Integer, String, Float
from database import Base

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    category = Column(String)
    city = Column(String)
    rating = Column(Float)