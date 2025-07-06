from fastapi import FastAPI
import router1

app = FastAPI()

app.include_router(router1.router)