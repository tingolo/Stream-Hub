from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


class Database:
    '''Class for intrecating with the database.'''

    _engine = None
    _SessionLocal = None
    Base = declarative_base()


    @classmethod
    def connect(cls):
        '''Connect to the database.'''

        try:
            cls._engine = create_engine(cls.__getDbConnectionUrl (
                host = getenv("DB_HOST"),
                port = int(getenv("DB_PORT")),
                db = getenv("DB_NAME"),
                username = getenv("DB_USERNAME"),
                password = getenv("DB_PASSWORD")
            ))

            cls.__SessionLocal = sessionmaker(bind = cls._engine)
            return (True, None)

        except Exception as exception:
            return (False, exception)
        

    @classmethod
    def getSession(cls):
        '''Creates and gives the session for the connection to db server. 
            For getting a session, first make sure to connect to db with connect() function.
        '''
        
        if (cls.__SessionLocal is None):
            raise ConnectionError("Database not connected.")

        session = cls.__SessionLocal()
        try:
            yield session
            session.commit()

        except Exception as exception:
            raise

        finally:
            session.close()

    
    @classmethod
    def getEngine(cls):
        return cls._engine
        
    
    @staticmethod
    def __getDbConnectionUrl(host: str, port: int, db: str, username: str, password: str) -> str:
        dbConnectionUrl = None

        if (username is None) and (password is None):
            dbConnectionUrl = f"postgresql+psycopg2://{host}:{port}/{db}"
        
        elif(username is not None) and (password is None):
            dbConnectionUrl = f"postgresql+psycopg2://{username}@{host}:{port}/{db}"

        elif (username is not None) and (password is not None):
            dbConnectionUrl = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db}"

        else:
            raise ValueError("Invalid argunments were given.")
        
        return dbConnectionUrl

