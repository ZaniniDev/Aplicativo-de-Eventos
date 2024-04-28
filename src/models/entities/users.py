from src.models.settings.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey

class Users(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    company_name = Column(String)

    def __repr__(self):
        return f"User [name={self.name}, email={self.email}, company={self.company_name}]"
