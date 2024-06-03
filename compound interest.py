def comp_int(p,t,r):
    Amount=p*((pow((1+r/100),t)))
    CI=Amount-p
    return CI
p=int(input('Principal'))
t=int(input('Time'))
r=int(input('Rate'))
print("The compound interest is ",comp_int(p,t,r))
