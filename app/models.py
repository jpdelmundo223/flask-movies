from . import db
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(30), unique=True, nullable=False)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)
    date_added = Column(DateTime, default=datetime.utcnow())