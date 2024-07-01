from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class OperationInput(BaseModel):
    number1: float
    number2: float

@app.post("/add")
async def add(input: OperationInput):
    result = input.number1 + input.number2
    return {"result": result}

@app.post("/multiply")
async def multiply(input: OperationInput):
    result = input.number1 * input.number2
    return {"result": result}
