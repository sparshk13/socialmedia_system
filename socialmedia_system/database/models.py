from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from database.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# from passlib.context import CryptContext

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=True)
    username = Column(String, nullable=True)
    emp_id = Column(String, nullable=True, index=True)
    # password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    
    posts = relationship("posts", back_populates="users")
    follows = relationship("follows", back_populates="users")
    
    # def set_password(self, password):
    #     self.password_hash = pwd_context.hash(password)

    # def verify_password(self, password):
    #     return pwd_context.verify(password, self.password_hash)


class Subject(Base):
    __tablename__ = "subjects"
    
    id = Column(Integer, primary_key=True, index=True)
    sub_name = Column(String, nullable=True)


class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content_body = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), datetime.now())

    users = relationship("users", back_populates="posts")


class Follows(Base):
    __tablename__ = "follow"

    id = Column(Integer, primary_key=True, index=True)
    followers = Column(Integer, ForeignKey("users.id"))
    followed = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), datetime.now())

    followers = relationship("users", backref="followers")
    followed = relationship("users", backref="followed")


class Likes(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, index=True)
    users_id = Column(Integer, ForeignKey("users.id"))
    posts_id = Column(Integer, ForeignKey("posts.id"))
    creted_at = Column(DateTime(timezone=True), datetime.now())
    
    users = relationship("users", back_populates="likes")
    posts = relationship("psts", back_populates="likes")