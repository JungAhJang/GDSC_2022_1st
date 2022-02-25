def change_number(a, b) :
    if a > b :
        a = a + 25
        b = b * 2
    else :
        b = b + 25
        a = a * 2
        
    return a, b

a, b = tuple(map(int,input().split()))
 #a,b는 int이기 때문에 immutable.따라서 함수에서 a, b 값이 바뀌어도 밖에 있는 a,b는 바뀌지 않으니, 
 # a,b에 함수 값을 넣어주는 과정이 필요하다.
a, b = change_number(a,b)
print(a, b)
