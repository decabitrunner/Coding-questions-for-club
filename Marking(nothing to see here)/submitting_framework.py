#Getting the inputs
import requests
response = requests.get('https://programmingqmarker.onrender.com/Sequances/q3')
print(response.json())
model, actual= list(response.json()['model']),list(response.json()['actual'])
print(f"your inputs are: \n model = {model}\n real_life = {actual}\n")

#Marking
answer = 'ENTER YOUR ANSWER HERE'
r = requests.post('https://programmingqmarker.onrender.com/submit',json={'id':int(response.json()['id']),'answer':answer})
print(f"\nyour answer is {'correct'if r.json()['correct']else'wrong'}! "+(''if  r.json()['correct'] else  f"{r.json()['solution']} should be the answer."))