from pydantic import BaseModel, EmailStr


# signup
class SignupData(BaseModel):
    username: str
    email: EmailStr
    password: str
    number: str


# login
class LoginData(BaseModel):
    login: str
    password: str


# signup response
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    number: str


# login response
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "Bearer"


# profile
class ProfileData(BaseModel):
    id: int
    username: str
    email: EmailStr
    number: str
