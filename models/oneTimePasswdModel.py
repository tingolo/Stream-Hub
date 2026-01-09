from sqlalchemy import (
    Column,
    Integer, 
    String, 
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from utils.db import Database


class OneTimePasswordModel(Database.Base):
    __tablename__ = "otps"
    
    User_Id = Column (
        Integer,
        ForeignKey("users.Id"),
        primary_key = True,
        nullable = False
    )

    OTP = Column (
        String(6),
        unique = True,
        nullable = False
    )

    OTP_Expiry_Time = Column (
        DateTime(timezone = True),
        nullable = False
    )

    user = relationship("UserModel", back_populates = "otp")