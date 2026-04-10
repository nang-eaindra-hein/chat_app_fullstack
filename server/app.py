from contextlib import asynccontextmanager
from litestar import Litestar, get, post, Request, put
from litestar.config.cors import CORSConfig
from litestar.di import Provide
from litestar.exceptions import HTTPException
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from database import Base, engine, SessionLocal
from models import User
from schemas import SignupData, LoginData, UserResponse, TokenResponse, ProfileData
from auth import (
    hash_password,
    verify_password,
    create_access_token,
    SECRET_KEY,
    ALGORITHM,
)
import jwt


# dependencies (session auto close after use database)
async def provide_db_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session


# lifespan (setup before server, tables auto-created)
@asynccontextmanager
async def lifespan(app: Litestar):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


# home (whengo to backend port ,signs -->ready)
@get("/")
async def home() -> dict:
    return {"message": "server is working"}


# get user
@get("/profile")
async def getUser(request: Request, db_session: AsyncSession) -> ProfileData:
    auth_header = request.headers.get("Authorization")  # backend checks request header

    if not auth_header:
        raise HTTPException(status_code=401, detail="No token")

    token = auth_header.split(" ")[1]  # token= "Barear token"
    payload = jwt.decode(
        token, SECRET_KEY, algorithms=[ALGORITHM]
    )  # backend read token using secret key
    user_id = int(payload["sub"])  # sub = userid ,userid = 1

    user = await db_session.get(User, user_id)  # in db find userid=1

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return ProfileData(
        id=user.id, username=user.username, email=user.email, number=user.number
    )


# get Users
@get("/getUsers")
async def getUsers(db_session: AsyncSession) -> list[ProfileData]:
    result = await db_session.execute(select(User))
    users = result.scalars().all()

    return [
        ProfileData(
            id=user.id,
            username=user.username,
            email=user.email,
            number=user.number,
        )
        for user in users
    ]


# post number
@put("/profile/number")
async def update_number(
    data: dict, request: Request, db_session: AsyncSession
) -> UserResponse:
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        raise HTTPException(status_code=401, detail="No token")

    token = auth_header.split(" ")[1]
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    user_id = int(payload["sub"])

    user = await db_session.get(User, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await db_session.commit()
    await db_session.refresh(user)

    return UserResponse(
        number=user.number,
    )


# post signup
# (data = user input,db = connect to db ,return userresponse)
@post("/signup")
async def signup(data: SignupData, db_session: AsyncSession) -> UserResponse:

    # exit email (search in db)
    existing_email = await db_session.scalar(
        select(User).where(User.email == data.email)
    )
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")
    # exit username(search in db)
    existing_username = await db_session.scalar(
        select(User).where(User.username == data.username)
    )
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already exists")
    # create new form
    new_user = User(
        username=data.username,
        email=data.email,
        password=hash_password(data.password),
        number=data.number,
    )

    db_session.add(new_user)  # told db to add form(prepare)
    await db_session.commit()  # save to db(save now)
    await db_session.refresh(new_user)  # refresh

    # return final to send back to frontend
    return UserResponse(
        id=new_user.id,
        username=new_user.username,
        email=new_user.email,
        number=new_user.number,
    )


# login
# data = user input , db = connect to db ,return tokenresponse
@post("/login")
async def login(data: LoginData, db_session: AsyncSession) -> TokenResponse:
    # exit username or email ?
    user = await db_session.scalar(
        select(User).where(or_(User.email == data.login, User.username == data.login))
    )
    # alert if user false or password false(compare typed pass and hased pass in db)
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(
            status_code=401, detail="Invalid username/email or password"
        )
    # if success will give token(vip pass) ,backend create and frontend store
    token = create_access_token(user.id, user.email)
    # frontend get that token ,different each login
    return TokenResponse(access_token=token)


# cors
cors_config = CORSConfig(  # setting rule for what can access my server
    allow_origins=[  # allow 2 worlds if not browser block
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["*"],  # allow all headers
    allow_credentials=True,  # allow cookie,auth
)

# app
app = Litestar(
    route_handlers=[home, signup, login, getUser, getUsers, update_number],
    dependencies={"db_session": Provide(provide_db_session)},
    lifespan=[lifespan],
    cors_config=cors_config,
)
