def Nechet():
    n = int(input("Write a number: "))
    for i in range(n+1):
        if i%2==1:
            yield i
mynum = list(Nechet())
print(*mynum, sep=", ")