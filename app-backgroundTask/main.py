from fastapi import FastAPI, BackgroundTasks
from time import sleep

app = FastAPI()

def send_mail(message):
    sleep(10)
    print(f"Mail has been sent with message {message}")

@app.get("/")
async def get_message(bg_task: BackgroundTasks):
    bg_task.add_task(send_mail, "ImSudipta")
    #send_mail("HI")
    return {"message":"Get API"}