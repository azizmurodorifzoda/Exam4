def har_appears(str1, a):
    my_list=[]
    for i in str1:
        cnt=0
        for j in range(len(i)):
            if j==a:
                cnt+=1
            
        my_list.append(cnt)
    return my_list
a=input()
b=input()
print(har_appears(a,b))