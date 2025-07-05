from fastapi import FastAPI, Request
import time
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000"
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],                # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],                # Allow all headers
)

@app.middleware("http")
async def add_process_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time= time.time() - start_time
    response.headers["X-Time"] = str(process_time)
    return response

@app.get("/ping")
async def ping():
    return{"message": "pong"}