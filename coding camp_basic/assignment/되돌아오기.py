n = int(input())
x , y = 0 , 0
cnt,result = 0,0
check = True
#시작점 저장해놓고 움직이다가 시작점 만나면 그때까지의 움직인 거리(1칸=1초) 세면 될것같은데
    # 동 남 서 북
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

arr = [
    tuple(input().split())
    for _ in range(n)
]

for elem in arr :
    if elem[0] == "E" : #동
        for _ in range(int(elem[1])) : 
            x, y = x+dx[0] , y+dy[0]
            cnt += 1
            if x == 0 and y == 0 :
                check = False #시작점을 지났는지 검사
                result = cnt
                break
    elif elem[0] == "S" : #남
        for _ in range(int(elem[1])) : 
            x, y = x+dx[1] , y+dy[1]
            cnt += 1
            if x == 0 and y == 0 :
                check = False #시작점을 지났는지 검사
                result = cnt
                break
    elif elem[0] == "W" : #서
        for _ in range(int(elem[1])) : 
            x, y = x+dx[2] , y+dy[2]
            cnt += 1
            if x == 0 and y == 0 :
                check = False #시작점을 지났는지 검사
                result = cnt
                break
    elif elem[0] == "N" : #북
        for _ in range(int(elem[1])) : 
            x, y = x+dx[3] , y+dy[3]
            cnt += 1
            if x == 0 and y == 0 :
                check = False #시작점을 지났는지 검사
                result = cnt
                break
    if check == False : #이중반복문 빠져나가기
        break

if check: #시작점을 지나지 않았다면
    result = -1

print(result)

