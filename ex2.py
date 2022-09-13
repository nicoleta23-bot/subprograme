n=int(input('n='))
def subp(x):
    s=1
    for i in range(x,x+1):
     s+=s*i
    return s
print(subp(n))