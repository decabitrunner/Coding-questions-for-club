# Programatorske otázky pre krúžok
#teaching
## 1. Fibonacci
Given two positive integers $a$ and $b$. Generate a sequence which is made by the following, simple rule: if you want the next number in the sequence you get it by adding the previous two numbers. This is called a Fibonacci sequence. You’ve been given terms 1 and 2 so your task is to generate the next $n$ terms.

An example of the program input and output
```
a: 1
b: 1
n: 4
2 3 5 8
```
If you are interested, the (recursive) definition for a Fibonacci sequence of a the nth term $u_n$ is
$$
u_n=u_{n-1}+u_{n-2}
$$
## 2. Arithmetic

There’s also another type of sequence, this one is made by adding the same number every time you go forward. For example:
$$
2,4,6,8,10,12...
$$
Here you add 2 each time. But you could also add 2 like this:
$$
-1,1,3,5,7,9
$$
But in this case, you start at -1. 
