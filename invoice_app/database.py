from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE URL for PostgreSQL or *.db filepath for SQLite
DATABASE_URL = "sqlite:///./invoice_app.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

# Create the SQLAlchemy engine
if "sqlite" in DATABASE_URL:
    engine = create_engine(
            DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(DATABASE_URL)

# Instances will be database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Used to create ORM models
Base = declarative_base()

