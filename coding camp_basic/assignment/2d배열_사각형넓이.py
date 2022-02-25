#2차 평면 위에 N개의 직사각형이 주어집니다. 이 직사각형들이 만들어내는 총 넓이를 구하는 프로그램을 작성해보세요.

offset = 100

n = int(input())
arr = []
#2차원 배열
arr = [[0]*201 for _ in range(201)]

for _ in range(n) :
    x1,y1,x2,y2 = tuple(map(int,input().split()))
    x1, y1 = x1 + offset , y1 + offset
    x2, y2 = x2 + offset , y2 + offset
    for i in range(x1,x2) :
        for j in range(y1,y2) :
            arr[i][j] = 1

#1을 찾는 코드
cnt = 0
for x in range(0,201) :
    for y in range(0,201) :
        if arr[x][y] :
            cnt += 1

print(cnt)

 #if checked[x][y]: <==> checked[x][y] 가 0이 아니면 이라는 뜻


