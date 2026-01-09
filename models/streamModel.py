from sqlalchemy import (
    Column,
    Integer, 
    String, 
    Boolean, 
    Date, 
    ForeignKey,
    func
)
from sqlalchemy.orm import relationship

from utils.db import Database


class StreamModel(Database.Base):
    __tablename__ = "streams"

    Id = Column (
        Integer,
        primary_key = True
    )

    Channel_Id = Column (
        Integer,
        ForeignKey("channels.Id")
    )
    
    Title = Column (
        String,
        nullable = False
    )

    Description = Column (
        String,
        nullable = False
    )

    Is_Live = Column (
        Boolean,
        nullable = False,
        default = True
    )

    Started_At = Column (
        Date,
        nullable = False,
        server_default = func.current_date()
    )

    Likes = Column (
        Integer,
        nullable = False,
        default = 0
    )

    channel = relationship (
        "ChannelModel", 
        back_populates = "streams"
    )