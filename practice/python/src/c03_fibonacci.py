
# Print fibbonaci series up to n using recursion and return the output in List


def fibonacci(n,c=0,a=0,b=1,l=None):
    if l is None:
        l=[]
    
    if c==n:
        return l
    l.append(a)
    return fibonacci(n,c+1,b,a+b,l)
    
print(fibonacci(10))