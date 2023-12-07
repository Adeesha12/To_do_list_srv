from typing import Optional
from fastapi import Request, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from auth.jwt_handler import decode_jwt

class JWTBearer(HTTPBearer):
    def __init__(self, *, bearerFormat: str = None, scheme_name: str = None, description: str = None, auto_error: bool = True):
        super().__init__(bearerFormat=bearerFormat, scheme_name=scheme_name, description=description, auto_error=auto_error)
        
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials :
        credentials : HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials and credentials.scheme  == "Bearer":
            return credentials.credentials
        else:
            raise HTTPException(status_code=403 , detail='Invalid or Expired Token !') 
        
    def verify_jwt(self, jwttoken:str):
        is_token_valid: bool = False
        payload = decode_jwt(jwttoken)
        if payload:
            is_token_valid = True
        return is_token_valid