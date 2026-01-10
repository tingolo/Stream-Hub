from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from utils.tokens import Tokens

class AuthenticationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        PUBLIC_PATHS = (
            "/auth/login",
            "/auth/register",
            "/auth/logout",
            "/favicon",
            "/static",
            "/docs",
            "/redoc",
            "/"
        )

        if request.url.path.startswith(PUBLIC_PATHS):
            return await call_next(request)
        
        accessToken = request.cookies.get("access_token")
        if not accessToken:
            return JSONResponse(
                status_code=401,
                content={
                    "status": "failed",
                    "message": "No access token was provided"
                }
            )
        
        
        try:
            tokens = Tokens()
            payload = tokens.verifyToken(accessToken)

        except ValueError as err:
            return JSONResponse(
                status_code=401,
                content={
                    "status": "failed",
                    "message": str(err)
                }
            )
        
        request.state.user = payload
        return await call_next(request)
        
        