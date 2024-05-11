def reverse(str1):
    for i in range(len(str1)-1,-1,-1):
        if str1[i].isupper():
            print(str1[i].lower(),end="")
        elif str1[i].islower():
            print(str1[i].upper(),end="")
        else:
            print(str1[i],end="")
a=input()
reverse(a)
