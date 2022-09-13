n=int(input('n='))
def subp(x):
    s=0
    for i in range(x):
     s+=1+(0.5**2)+(0.5**4)+(0.5**6)+(0.5**8)
    return s
print(subp(n))
