import os
from fastapi import FastAPI, Response
from pydantic import BaseModel
import pandas as pd
from sqlalchemy import create_engine

app = FastAPI(title="DAMG7245 - Data as Service")

BASE_URL = os.getenv("DB_URL", "postgresql://root:root@localhost:5432/noaa")

engine = create_engine(BASE_URL)
engine.connect()


@app.get("/get_station")
async def get_station() -> dict:
    res = pd.read_sql_table("noaa_tbl", con=engine)
    return Response(res.to_json(orient="records"), media_type="application/json")


@app.get("/load_data_into_db")
async def load_data_into_db() -> dict:
    cols = [
        (20, 51),    # Name
        (72, 75),    # ST
        (106, 116),  # Lat
        (116, 127)   # Lon
    ]
    df = pd.read_fwf(
        r"https://www.ncei.noaa.gov/access/homr/file/nexrad-stations.txt", colspecs=cols, skiprows=[1])
    df.to_sql(name='noaa_tbl', con=engine, index=False, if_exists='replace')
    return {"message": "Completed"}

# Testing
# uvicorn main:app --reload --port 8000

# Production
# gunicorn -k uvicorn.workers.UvicornWorker main:app
