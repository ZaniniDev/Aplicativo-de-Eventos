from src.models.settings.base import Base
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer

class Events(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    finish_date = Column(DateTime, nullable=False)    
    details = Column(String)
    address = Column(String)
    city = Column(String)
    district = Column(String)
    online = Column(Integer)
    location = Column(String)
    maximum_attendees = Column(Integer)
    user_id = Column(String, ForeignKey("users.id"))
    
    def __repr__(self):
        return f"Events [title={self.title}, maximum_attendees={self.maximum_attendees}]"
