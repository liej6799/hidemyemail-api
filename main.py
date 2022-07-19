from fastapi import FastAPI
from pyicloud import PyiCloudService


app = FastAPI()

@app.get("/generate")
async def generate(username: str, label: str, note: str):
    api = PyiCloudService(username, '')
    email = api.hidemyemail.generate()
    api.hidemyemail.reserve(email, label, note)

    return {"email": email}