offset = 100
MAX_R = 200

arr = [
    [0] * (MAX_R+1)
    for _ in range(MAX_R+1)
]

n = int(input())

for _ in range(n) :
    x1, y1 = tuple(map(int,input().split()))
    x2 , y2 = x1 + 8 + offset, y1 + 8 + offset
    x1, y1  = x1 + offset, y1 + offset
    for i in range(x1,x2) :
        for j in range(y1,y2) :
            arr[i][j] += 1

cnt = 0

for i in range(MAX_R+1) :
    for j in range(MAX_R) :
        if arr[i][j] > 0 :
            cnt += 1

print(cnt)