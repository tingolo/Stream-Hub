from sqlalchemy import (
    Column,
    Integer, 
    String, 
    Boolean, 
    Date, 
    func
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY

from utils.db import Database


class UserModel(Database.Base):
    __tablename__ = "users"

    Id = Column (
        Integer,
        primary_key = True
    )

    Email = Column (
        String,
        unique = True,
        nullable = False
    )

    Password = Column (
        String,
        nullable = False
    )

    Joinned_On = Column (
        Date,
        nullable = False,
        server_default = func.current_date()
    )

    Email_Verified = Column (
        Boolean,
        nullable = False,
        default = False
    )

    Liked_Streams = Column (
        ARRAY(Integer)
    )

    # MARK: Relationships
    channels = relationship (
        "ChannelModel",
        back_populates = "user",
        cascade = "all, delete-orphan"
    )

    otp = relationship(
        "OneTimePasswordModel",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
        passive_deletes=True
    )
