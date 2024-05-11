def now(a,n):
    if n==1:
        return a**n
    else:
        return pow(a, n-1)
a=input()
b=input()
print(now(a, b))