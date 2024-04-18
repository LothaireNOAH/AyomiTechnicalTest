from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from npi_calcul import do_NPI_calcul
from typing import List
import sqlite3
import pandas as pd
import csv


class Item(BaseModel):
    expression: str

    class Config:
        orm_mode = True

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Bienvenue sur votre API FastAPI !"}

@app.post("/calculate")
async def calculate_numbers(item: Item):
    try : 
        result = do_NPI_calcul(item.expression)
        return {"result": result}
    except (ValueError, ZeroDivisionError) as e:
        raise HTTPException(status_code=400, detail=str(e))    

@app.get("/export_csv")
async def export_csv(response: Response):
    try:
        conn = sqlite3.connect('expressions.db')
        df = pd.read_sql_query("SELECT * FROM expressions", conn)
        output = df.to_csv(index=False)
        return StreamingResponse(
            iter([output]),
            media_type='text/csv',
            headers={"Content-Disposition":
                "attachment;filename=result.csv"})
    except Exception as e:
        return {"error": str(e)}
    finally:
        conn.close()