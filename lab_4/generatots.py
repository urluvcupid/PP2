#1. Create a generator that generates the squares of numbers up to some number N.
def SquareGen(n):
    for i in range(n+1):
        yield i*i
mynum = list(SquareGen(7))
print(*mynum) 

#2. Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def EvenGen():
    n = int(input("Write a number: "))
    for i in range(n+1):
        if i%2==0:
            yield i
mynum = list(EvenGen())
print(*mynum, sep=", ")

#3. Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def Divfor34():
    n = int(input("Write a number: "))
    for i in range(n+1):
        if i%4==0 or i%3==0:
            yield i
mynum = list(Divfor34())
print(*mynum, sep=", ")

#4. Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for i in range(a, b+1):
        yield i*i 
mynum = list(squares(1, 5))
print(*mynum, sep=", ")

#5. Implement a generator that returns all numbers from (n) down to 0.
def returner(n):
    for i in range(n, -1, -1):
        yield i
mynum = list(returner(5))
print(*mynum, sep=", ")












