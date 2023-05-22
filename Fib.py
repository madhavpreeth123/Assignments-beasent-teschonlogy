#Fibonacci Series
def fibonacci(n):
    a=0
    b=1
    if n==1:
        print(a)
    if n>1:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            print(c)
            a=b
            b=c

n=int(input("Enter number: "))
fibonacci(n)


### output ###
Enter number: 5
0
1
1
2
3

Enter number: -5
nothing would printed for negetive values
