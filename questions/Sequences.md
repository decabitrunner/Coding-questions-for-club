# Sequences

## 1. Fibonacci
Given two positive integers $a$ and $b$. Generate a sequence which is made by the following, simple rule: if you want the next number in the sequence you get it by adding the previous two numbers. This is called a Fibonacci sequence. You’ve been given terms 1 and 2 so your task is to generate the next $n$ terms.

An example of the program input and output
```
a: 1
b: 1
n: 4
2 3 5 8
```
If you are interested, the (recursive) definition for a Fibonacci sequence of the nth term $u_n$ is

$$u_n=u_{n-1}+u_{n-2}$$

## 2. Arithmetic

There’s also another type of sequence, this one is made by adding the same number every time you go forward. For example:

$$2,4,6,8,10,12...$$
Here you add 2 each time and the nth term can be given by

$$
u_n = 2n
$$

But you could also add 2 like this:

$$-1,1,3,5,7,9$$
But in this case, you start at -1 and the nth term can be given by

$$
u_n = 2n-3
$$

In general, if you are adding a constant $d$ each time, and start at the number $u_1$ the formula for the nth term of an arithmetic series can be given as:

$$
u_n = u_1 + (n-1)d
$$

Sebastian likes to think of numbers, and then check if they could be in different arithmetic sequances. Lately, he has a lot of school work to do and needs your help to write a program that will do it for him.

This program shoud take as input: the first number in the arithmetic sequence $a$, and the difference $d$. Then it should read $x$, this is the number that Sebastian wants to check. $a,d,x$ are all integers.

Your program should output `YES` if the number is somwhere in the sequance and  `NO` if it isn't. These are some examples:

```
a: 2
d: 2
x: 24
YES
```

```
a: 3
d: 7
x: 25
NO
```

```
a: 1
d: 5
x: 44611
YES
```

## 3.Modeling

Sequances can also be used to create models for things. A model, is a math equation which predicts what will happen in the real world. Geometric sequences are often used to create models. Geometric sequences are made, when you move to the next number by multiplying. For example in the sequance below, you start at 1 and then multiply by 2 each time.

$$
1,2,4,8,16,32,64,128...
$$

If you want to get the 3rd term in this sequacne you have to multiply the first term in the sequency by 2 two times, like this:

$$
1 \times 2 \times 2 = 4
$$

Because $2\times2=2^2$, you can write this as

$$
1\times2^2 = 4
$$

If you want to get the 6th term in this sequance you have to multiply the first term in the sequency by 2 five times, like this:

$$
1 \times 2 \times 2 \times 2 \times 2 \times 2 = 32
$$

$$
1 \times 2^5 = 32
$$

So, if you want to get the nth term of this sequance, you have to do this:

$$
u_n = 1 \times 2^{n-1}
$$

This can be used to model the population of bacteria for example. We know that bacteria can split into two to reproduce. Let's say we have a population of bacteria which reproduce 1 time per day. On day 1 ($n=1$), we have just one bacterium, but then the next day ($n=2$) its 2 and then on the next one ($n=3$) its 4 and so on. Now we have a model and if we want to know how many bacteria there will be at day $20$, we can just substitute it into the equation, as shown:

$$
 1 \times 2^{n-1} = \text{amount of bacteria}
$$

$$
 1 \times 2^{20-1} = 524288
$$

![bacteriamodel](https://github.com/decabitrunner/Coding-questions-for-club/blob/main/src/bacteriamodel.png)

A more general form of the nth term, which is written as $u_n$ of a geometric sequance is shown below. $a$ means the first term and $r$ is the number you multiply by.

$$
u_n = ar^{n-1}
$$

For example, many games have score boosters which increase your score by some percentage (scores are always rounded to the nearest whole number). Let's say in a game you start out with a score of $320$ ($a=320$)and then you can collect score boosters which increase your score by 20%. That is the same as multiplying every time by $1.2$ so $r=1.2$. You can model the score using a geometric sequance if you say that $n$ is the number of times you collect the score booster:

$$
\text{score} = 320 \times 1.2^{n-1}
$$

This would give the sequance:

$$
320, 384, 461, 553, 664...
$$

But when you play this game your actual score after collecting 5 score boosters is 678, that is because you can also collect score points allong the way. This means the model is not 100% accurate. Is it good enough?

It was supposed to be 664 but it was actually 678. That means the model was off by $678-664$ score points. If a model is off by more than 10% of what it predicted, it is a `BAD` model. becuase 10% of 664 is 66.4, and that is more than 14 the model can be concidered a `GOOD` model. 

In this question, you will recive two lists, one stored in the variable `model` which stores the five values (indexed from 0 to n-1) predicted by the geometric sequance model and then another stored in the variable `actual` which stores the values measured in real life. The program needs to determine whether the model is `GOOD` (within 10% of the actual values) or `BAD`.

Use this template for your code, do not forget to store your answer in the `answer` variable

```python
#Getting the inputs
import requests
response = requests.get('https://programmingqmarker.onrender.com/Sequances/q3')
model, real_life = list(response.json()['model']),list(response.json()['actual'])
print(f"your inputs are: \n model = {model}\n real_life = {real_life}\n")

#YOUR CODE SHOULD BE IN THIS GAP

#Marking
answer = 'ENTER YOUR ANSWER HERE'
r = requests.post('https://programmingqmarker.onrender.com/submit',json={'id':int(response.json()['id']),'answer':str(answer)})
print(f"\nyour answer is {'correct'if r.json()['correct']else'wrong'}! "+(''if  r.json()['correct'] else  f"{r.json()['solution']} should be the answer."))
```

You also need to print your answer, this is an example:

```
your inputs are: 
 model = [320, 384, 461, 553, 664]
 real_life = [320, 384, 461, 553, 678]

GOOD

your answer is correct!
```

## 4. Ötzi the ice man is not a good programmer

After somehow waking up from his very long slumber in the ice Ötzi picks up a big interest in sequences. He starts laying sticks. For example, he could lay 3 stick then 5 sticks then 7 sticks and so on to create an arithmetic sequance. He could lay down a fiboncci sequance and also a geometric sequence with the sticks. One day, he was so fascinated that he layed out a 6500 terms of a sequence with sticks. He was very tired from a hard days work so and it was dark already, so he decided to go to sleep and admire his sequance of sticks in the sun the next day. To his horror, when he woke up the wind was blowing hard. This ment that some sticks may have been blown away by the wind. He prepared for another hard day working, as he knew he now had to count the sticks and add the stiks that were blown away. He counted all the sticks (he was good at this as he did it so many times so it didnt take too much time) and wrote them on a pice of ancient paper. Then he started veryfing that the sequance is still a valid sequance, he did the first 10 which had no issue but then an idea struck him: he heard in town about the modern beasts called computers. He thought that maybe a computer could tell him where the sticks blew away to spare him so many hours of work. Because Ötzi was born around 3345 BC, he didnt have much experiance with programming and the light from a computer screen seemed unbarable to him so he needs your help.

You will be given a list stored in the variable `sticks` which contains the sequance of sticks, as Ötzi counted them. The array is indexed from 0 to n-1 but Ötzi is unfamiliar with the concept of 0 so he counts them as 1 to n. Ötzi still wants to have some fun, figuring out how much he needs to add to a pile of sticks to make the sequance valid so tell him only the indexes (in his way) of the piles that had some sticks blown away.Return the array of all the indexes, starting from the smallest up to the largest index so its easy for Ötzi to follow.

These are examples with 12 piles, not 6500 for understanding:

The list is `[2,3,5,8,13,21,34,55,89,144,225,377]`

```
[11]

your answer is correct!
```

Explanation: Fibonacci sequance, the 10th index was wrong by 8. Becuase Ötzi considers the first index to be 1, the index in his terms is $11$. All the other ones are correct.

The list is `[2,6,18,54,162,486,1458,4374,13122,39366,236196,708588]`

```
[]

your answer is correct!
```

Explanation: Geometric sequence $2\times 3^{n-1}$ every single term is correct so there is no wrong index.

When you are ready to help Ötzi, use this template make sure to store your array in the `answer` variable:

```python
#Getting the inputs
import requests
response = requests.get('https://programmingqmarker.onrender.com/Sequances/q4')
sticks= list(response.json()['sticks'])

#PUT YOUR CODE HERE

#Marking
answer = 'PUT YOUR ANSWER HERE'
r = requests.post('https://programmingqmarker.onrender.com/submit',json={'id':int(response.json()['id']),'answer':str(answer)})
print(f"\nyour answer is {'correct'if r.json()['correct']else'wrong'}! "+(''if  r.json()['correct'] else  f"{r.json()['solution']} should be the answer."))
```
