from fastapi import FastAPI
from pydantic import BaseModel
from typing import *
import pandas as pd

class User(BaseModel):
    Name: List[str]
    Age: List[int]
    Boat: List[str]


class Summary(BaseModel):
    mean_age: float
    median_age: float


def summary_statistics(user_dict):
    df = pd.DataFrame(user_dict)
    response = {"mean_age":df['Age'].mean(),
                "median_age":df['Age'].median()}
    return response


app = FastAPI()


@app.post("/user/", response_model=Summary)
async def create_item(user: User):
    user_dict = user.dict()
    response = summary_statistics(user_dict)
    return response