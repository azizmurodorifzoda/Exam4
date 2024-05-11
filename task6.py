def sum_of_vowels(a, str1):
    sdict={
        "A=":'4',
        "E":'3',
        "I":'1',
        "O":'0',
        "U":'0'
    }
    cnt=0
    for i in a:
        if i in str1:
            cnt+=1
        return cnt
a=input()
print(sum_of_vowels(a))