#숫자 0과 1로만 이루어진 n * n 크기의 격자 상태가 주어집니다. 각 칸 중 상하좌우로 인접한 칸 중 숫자 1이 적혀 있는 칸의 수가 3개 이상인 곳의 개수를 세는 프로그램을 작성해보세요. 단, 인접한 곳이 격자를 벗어나는 경우에는 숫자 1이 적혀있지 않은 것으로 생각합니다.

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
cnt = 0
result_cnt = 0
nx, ny = 0, 0 #0행 0열

#행이 dx , 열이 dy
#동 남 서 북
dxs , dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y) :
    return x >= 0 and x < n and y >=0 and y < n

for x in range(n) :
    for y in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys) :
            nx, ny = x + dx, y + dy
            if in_range(nx,ny) and arr[nx][ny] == 1 :
                cnt += 1
                # print(cnt)
        if cnt >= 3 :
            result_cnt += 1

       

print(result_cnt)
