import os
from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from utils.db import Database
from utils.validatePassword import generateHashPassword

from models import UserModel
from schema import RegisterSchema


registerRouter = APIRouter (
    prefix = "/auth",
    tags = ["Authentication"]
)


@registerRouter.get("/register")
def getRegisterPage():
    registerPage = f"{os.getenv('PROJECT_ROOT')}/{os.getenv('TEMPLATE_FILES_DIR')}/register.html"
    return FileResponse(registerPage)


@registerRouter.post("/register")
def getRegisterPage(accountDetails: RegisterSchema, dbSession: Session = Depends(Database.getSession)):
    newAccount = UserModel (
        Email = accountDetails.email,
        Password = generateHashPassword(accountDetails.password)
    )

    try:
        dbSession.add(newAccount)
        dbSession.commit()
        
        return {
            "status": "success",
            "message": "New account was created successfully."
        }
    
    except IntegrityError as error:
        dbSession.rollback()

        return {
            "status": "failed",
            "message": "Account with email already exists!"
        }
    
    except Exception:
        dbSession.rollback()
        
        return {
            "status": "failed",
            "message": "Could not create a new account because of server issue."
        }