from fastapi import FastAPI
from pydantic import BaseModel

app =FastAPI()

class UserInput(BaseModel):
    year:int
    month:int
    date:int
    station:str

@app.get("/say_hello")
async def say_hello() -> dict:
    return {"message":"Hello World"}


@app.post("/fetch_url")
async def fetch_url(userinput: UserInput) -> dict:
    # if userinput.date > 31:
    #     return 400 bad request . return incorrect date
    aws_nexrad_url = f"https://noaa-nexrad-level2.s3.amazonaws.com/index.html#{userinput.year:04}/{userinput.month:02}/{userinput.date:02}/{userinput.station}"
    return {'url': aws_nexrad_url }