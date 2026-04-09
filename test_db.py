from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:Kripa%40pg21@localhost:5432/lifestyle_db"

try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("Database connected successfully!")
    connection.close()
except Exception as e:
    print("Connection failed:", e)