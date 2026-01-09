from sqlalchemy import (
    Column,
    Integer, 
    String, 
    Date, 
    ForeignKey,
    func
)
from sqlalchemy.orm import relationship

from utils.db import Database


class ChannelModel(Database.Base):
    __tablename__ = "channels"

    Id = Column (
        Integer,
        primary_key = True
    )

    User_Id = Column (
        Integer,
        ForeignKey("users.Id")
    )

    Name = Column (
        String,
        unique = True,
        nullable = False
    )
    
    Subscriber_Count = Column (
        Integer,
        nullable = False,
        default = 0
    )

    Created_At = Column (
        Date,
        nullable = False,
        server_default = func.current_date()
    )

    user = relationship (
        "UserModel",
        back_populates = "channels"
    )
    
    streams = relationship (
        "StreamModel", 
        back_populates = "channel", 
        cascade = "all, delete-orphan"
    )