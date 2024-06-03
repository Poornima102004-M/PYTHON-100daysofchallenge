def fact(n):
    if(n==1 or n==0):
       return 1
    else:
        factorial=n*fact(n-1)
        return factorial
n=int(input("Enter the number"))
print("factorial of ",n,"is",fact(n))
