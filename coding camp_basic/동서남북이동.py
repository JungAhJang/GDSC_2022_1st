#(0, 0)에서 시작하여 총 N번 움직여보려고 합니다. N번에 걸쳐 움직이려는 방향과 움직일 거리가 주어졌을 때, 최종 위치를 출력하는 프로그램을 작성해보세요.

n = int(input())

x , y = 0 , 0

#0이면 동쪽 -> | 1이면 남쪽(아래) | 2이면 서쪽 (<-) | 3이면 북쪽(위) 
#     동 서 남 북
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


arr = [
    tuple(input().split())
    for _ in range(n)
]

for elem in arr :
    if elem[0] == "E" :
        for _ in range(int(elem[1])) : 
            x, y = x+dx[0] , y+dy[0]
    elif elem[0] == "S" :
        for _ in range(int(elem[1])) : 
            x, y = x+dx[1] , y+dy[1]
    elif elem[0] == "W" :
        for _ in range(int(elem[1])) : 
            x, y = x+dx[2] , y+dy[2]
    elif elem[0] == "N" :
        for _ in range(int(elem[1])) : 
            x, y = x+dx[3] , y+dy[3]

print(x, y)