from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Setup
DATABASE_URL = "mysql+pymysql://root:Amiandami%4022@localhost:3306/testdb"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

# Model
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# Create table
Base.metadata.create_all(engine)

# Session setup
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()  # ✅ Instantiate session

# Query (CORRECT)
students = session.query(Student).all()
for student in students:
    print(student.name, student.age)
