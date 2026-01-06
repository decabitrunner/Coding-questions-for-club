from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

trials = []

class submitModel(BaseModel):
    id: int
    answer: str

@app.get('/')
async def root():
    return 404

@app.get('/q3')
async def q3():
    response = {}
    a = random.randint(1,1000)
    r = random.uniform(2,100)
    model = []
    actual = []
    q=1
    for i in range(5):
        x = round(a*r**i)
        y = round(x+random.choice([1,-1])*random.choice([lambda: random.uniform(0,0.1), lambda: random.uniform(0,0.2), lambda: random.uniform(0,0.5)])()*x)
        q= q & (1 if abs(x-y)<=0.1*x else 0)
        model.append(x)
        actual.append(y)
    id = len(trials)
    trials.append((id,'GOOD' if q else 'BAD'))
    response["id"]=id
    response["model"]=model
    response["actual"]=actual
    return response

@app.post('/submit')
async def submit(payload:submitModel):
    response = {}
    trial = trials.pop(payload.id)
    response["correct"] = True if trial[1]==payload.answer else False
    response["solution"] = trial[1]
    return response
#this works