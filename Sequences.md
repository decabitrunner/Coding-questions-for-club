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
daco
