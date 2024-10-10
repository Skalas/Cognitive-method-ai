from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databases import Database
import os

# # "postgresql://username:password@host:port/database_name"
# DATABASE_URL = f"mysql://{os.environ['MYSQL_USER']}:{os.environ['MYSQL_PASSWORD']}@{os.environ['MYSQL_HOST']}:{os.environ['MYSQL_PORT']}/{os.environ['MYSQL_DATABASE']}"

# engine = create_engine(
#     DATABASE_URL
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# database = Database(DATABASE_URL)
