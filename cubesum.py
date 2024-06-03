def cube_sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i*i*i
    return sum
n=int(input("Enter"))
print("The cubesum is",cube_sum(n))
