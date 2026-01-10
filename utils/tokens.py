import jwt
import time
from os import getenv

class Tokens:
    
    def __init__(self):
        self.__key = getenv("SECRET_KEY")
        self.__algo = getenv("ALGORITHM")


    def generateAccessToken(self, payload: dict):
        currentTime = int(time.time())
        token_expiry_time = int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

        payload["type"] = "access"
        payload["iat"] = currentTime
        payload["exp"] = currentTime + token_expiry_time

        accesstoken = jwt.encode(payload, self.__key, self.__algo)
        return accesstoken
    
    
    def generateRefreshToken(self, payload: dict):
        currentTime = int(time.time())
        token_expiry_time = int(getenv("REFRESH_TOKEN_EXPIRE_DAYS"))

        payload["type"] = "refresh"
        payload["iat"] = currentTime
        payload["exp"] = currentTime + (token_expiry_time * 24 * 3600)

        refreshToken = jwt.encode(payload, self.__key, self.__algo)
        return refreshToken
    

    def verifyToken(self, token):
        try:
            payload = jwt.decode(token, self.__key, algorithms = self.__algo)

            if (payload.get("type") != "access") or (payload.get("type") != "refresh"):
                raise jwt.InvalidTokenError("Invalid token type")
            
            return {
                "status": "success",
                "message": "",
                "payload": payload
            }
        
        except jwt.ExpiredSignatureError:
            return {
                "status": "failed",
                "message": "Access token expired"
            }

        except jwt.InvalidTokenError:
            return {
                "status": "failed",
                "message": "Invalid token"
            }
            
    
