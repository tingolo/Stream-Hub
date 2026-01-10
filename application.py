import os
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from utils.db import Database
from routes import loginRouter, registerRouter
from middleware import AuthenticationMiddleware

class Application:
    '''Configures the data essential for running the fastapi application.'''

    def __init__(self):
        load_dotenv()

    
    def run(self, entryPoint: FastAPI):
        ''' Runs the fastapi application.'''
        
        self.__getDbConnection()

        entryPoint.mount("/static", StaticFiles(directory = os.getenv("STATIC_FILES_DIR")), name = "static")
        entryPoint.add_middleware(AuthenticationMiddleware)

        entryPoint.include_router(loginRouter)
        entryPoint.include_router(registerRouter)
        

    @staticmethod
    def __getDbConnection():
        '''Returns the connection status to database.'''
        dbConnectionStatus = False
        dbConnectionException = None

        for _ in range(3):
            print("\n")
            print("Trying to connect to database...")

            dbConnectionStatus, dbConnectionException = Database.connect()
            
            if (dbConnectionStatus == False):
                print("FAILED: Connection failed!")
                print("\n")
                continue

            else:
                print("SUCCESS: Connection succeeded.")
                print("\n")
                break

        if dbConnectionStatus == False:
            print("Could not connect to the database due to: ")
            raise dbConnectionException
            
        