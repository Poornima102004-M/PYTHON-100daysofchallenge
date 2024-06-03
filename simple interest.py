def simp_int(p,t,r):
    SI=(p*t*r)/100
    return SI
p=int(input('Principal'))
t=int(input('Time'))
r=int(input('Rate'))
print("The SI is",simp_int(p,t,r))
