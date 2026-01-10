from fastapi import FastAPI
from pydantic import BaseModel
import random
import math
import sys

sys.set_int_max_str_digits(0)

app = FastAPI()

trials = []

class submitModel(BaseModel):
    id: int
    answer: str

@app.get('/')
async def root():
    return 404

@app.get('/Sequances/q3')
async def sequences_q3():
    response = {}
    a = random.randint(1,1000)
    r = random.uniform(2,100)
    model = []
    actual = []
    q=1
    options = [lambda: random.uniform(0,0.1)]*7+[lambda: random.uniform(0,0.2), lambda: random.uniform(0,0.5)]
    for i in range(5):
        x = round(a*r**i)
        y = round(x+random.choice([1,-1])*random.choice(options)()*x)
        q= q & (1 if abs(x-y)<=0.1*x else 0)
        model.append(x)
        actual.append(y)
    id = len(trials)
    trials.append((id,'GOOD' if q else 'BAD'))
    response["id"]=id
    response["model"]=model
    response["actual"]=actual
    return response

@app.get('/Sequances/q4')
async def sequences_q4():
    response = {}
    answer = sorted(set([random.randint(11, 6500) for i in range(random.randint(0, 1000))]))
    sequence_functions = [lambda a, b, n: a * n + b, lambda a, b, n: a * b ** (n - 1), lambda a, b, n: round(
        ((b - a * ((1 - math.sqrt(5)) / 2)) / math.sqrt(5)) * ((1 + math.sqrt(5)) / 2) ** (n - 1) + (
                    (a * ((1 + math.sqrt(5)) / 2) - b) / math.sqrt(5)) * ((1 - math.sqrt(5)) / 2) ** (n - 1))]
    sequence = []
    sequence_type = random.choice(sequence_functions)
    a, b = random.randint(1, 50), random.randint(1, 50)
    for i in range(1, 6501):
        term = sequence_type(a, b, i)
        if i in answer:
            sequence.append(term - random.randint(1, (term - 1)))
        else:
            sequence.append(term)
    id = len(trials)
    trials.append((id, str(answer)))
    response["id"] = id
    response["sticks"] = sequence
    return response


print(sequences_q4())

@app.post('/submit')
async def submit(payload:submitModel):
    response = {}
    trial = trials.pop(payload.id)
    response["correct"] = True if trial[1]==payload.answer else False
    response["solution"] = trial[1]
    return response
