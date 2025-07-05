from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

# -- App setup
app = FastAPI()

# -- Dummy user
fake_user = {
    "username": "john",
    "password": "$2b$12$lqeBRmWMP6Z5tPVEPatbF.F5HVN.T/jA/eC0A6YOnY/qzEzBaSZo2",  # hashed version of 'secret'
    "role": "user"
}

# -- Password hasher
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
print(pwd_context.hash("secret"))

# -- JWT settings
SECRET_KEY = "secret_key_here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# -- OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# -- Utility functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username != fake_user["username"]:
            raise HTTPException(status_code=401, detail="Invalid user")
        return fake_user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


# -- Login endpoint
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != fake_user["username"] or not verify_password(form_data.password, fake_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    access_token = create_access_token(data={"sub": fake_user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}


# -- Protected route
@app.get("/protected")
def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": f"Hello {current_user['username']}, you're authorized!"}
