#Getting the inputs
import requests
response = requests.get('http://127.0.0.1:8000/Sequances/q4')
sticks= list(response.json()['sticks'])

#PUT YOUR CODE HERE

#Marking
answer = []
r = requests.post('http://127.0.0.1:8000/submit',json={'id':int(response.json()['id']),'answer':str(answer)})
print(r.json())
print(f"\nyour answer is {'correct'if r.json()['correct']else'wrong'}! "+(''if  r.json()['correct'] else  f"{r.json()['solution']} should be the answer."))