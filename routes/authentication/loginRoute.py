import os
from fastapi import APIRouter, Depends, Response
from fastapi.responses import FileResponse

from sqlalchemy.orm import Session

from utils.db import Database
from utils.validatePassword import verifyPassword
from utils.tokens import Tokens

from models import UserModel
from schema import LoginSchema


loginRouter = APIRouter (
    prefix = "/auth",
    tags = ["Authentication"]
)


@loginRouter.get("/login")
def getLoginPage():
    loginPage = f"{os.getenv('PROJECT_ROOT')}/{os.getenv('TEMPLATE_FILES_DIR')}/login.html"
    return FileResponse(loginPage)


@loginRouter.post("/login")
def loginUser(user: LoginSchema, response: Response, dbSession: Session = Depends(Database.getSession)):
    db_account = dbSession.query(UserModel).filter (
        UserModel.Email == user.email
    ).first()

    if db_account is None:
        return {
            "status": "failed",
            "message": f"No account with email {user.email} was found!"
        }
    
    passwordVerificationStatus = verifyPassword(password = user.password, hashedPassword = db_account.Password)
    if passwordVerificationStatus is False:
        return {
            "status": "failed",
            "message": f"Invalid password!"
        }
    

    # WORK: generating the tokens.
    token = Tokens()
    payload = {
        "user_id": db_account.Id,
        "email": db_account.Email
    }

    accessToken = token.generateAccessToken(payload)
    refreshToken = token.generateRefreshToken(payload)

    response.set_cookie(
        key="access_token",
        value=accessToken,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=(int(os.getenv("ACCESS_COOKIE_EXPIRE_MINUTES")) * 60)
    )

    response.set_cookie(
        key="refresh_token",
        value=refreshToken,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=(int(os.getenv("REFRESH_COOKIE_EXPIRE_DAYS")) * 24 * 60 * 60)
    )

    return {
        "status": "success",
        "message": "Logged in successfully"
    }
