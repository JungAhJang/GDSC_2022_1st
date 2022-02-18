#좌표평면위에 직사각형 A, B를 먼저 붙이고 그 위에 직사각형 M을 붙였습니다. 아직 남아있는 (M으로 덮이지 못한) 직사각형 A, B의 넓이의 합을 구하는 프로그램을 작성해보세요. 단, 직사각형 A, B는 겹치지 않게 주어진다고 가정해도 좋습니다.

offset = 1000
max_r = 2000

arr = [
    [0] * (max_r+1)
    for _ in range(max_r+1)
]

for idx in range(1,4) :
    x1,y1,x2,y2 = tuple(map(int,input().split()))
    x1, y1, = x1 + offset, y1 + offset
    x2 , y2 = x2 + offset, y2 + offset
    for i in range(x1,x2) :
        for j in range(y1,y2) :
            arr[i][j] = idx

cnt = 0
for x in range(0, max_r+1) :
    for y in range(0,max_r+1) :
        if arr[x][y] == 1 or arr[x][y] == 2:
            cnt += 1

print(cnt)