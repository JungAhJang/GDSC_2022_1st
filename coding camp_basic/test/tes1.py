a, b, c, d = 0, 0, 0, 0

a, b = tuple(map(int,input().split()))
c, d = tuple(map(int,input().split()))

min_x = 0
max_x = 0

if a < c :
    min_x = a 
elif c < a :
    min_x = c

if b < d :
    max_x = d
elif d < b :
    max_x = b


print(max_x-min_x)