from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class VentaEntity(Base):
    __tablename__ = "ventas"
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    amount = Column(Integer)
    products = Column(Integer)
    createdAt = Column(DateTime, default=datetime.now)

class UserEntity(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String, unique = True)
    dir = Column(String)
    createdAt = Column(DateTime, default=datetime.now)
    updatedAt = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    active = Column(Boolean, default=False)
    venta = relationship("VentaEntity", backref="users", cascade="delete,merge")
    # def model_dump(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "age": self.age,
    #         "email": self.email,
    #         "dir": self.dir,
    #         "createdAt": self.createdAt,
    #     }
