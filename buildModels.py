from dotenv import load_dotenv
from utils.db import Database
from models import (
    UserModel,
    ChannelModel,
    StreamModel,
    OneTimePasswordModel
)

if __name__ == "__main__":
    load_dotenv()

    connectionStatus, exception = Database.connect()
    if (connectionStatus == False):
        raise exception

    Database.Base.metadata.create_all(bind = Database.getEngine())
    