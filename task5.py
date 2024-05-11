def is_harshot(a):
    b=0
    k=a
    while a>0:
        b=a%10
        k=k//10
    if k%b==0:
        return True
    else:
        return False
a=int(input())
print(is_harshot(a))