string = list(input())
        #동0 남1 서2 북3
dx, dy = [1,0,-1,0],[0,-1,0,1]
x, y = 0, 0
dir_num = 3
cnt = 0
second = 0
check = False

for i in range(len(string)) :
    if string[i] == "L" :
        dir_num = (dir_num -1 + 4) % 4
    elif string[i] == "R" :
        dir_num = (dir_num + 1) % 4
    elif string[i] == "F":
        x, y = x + dx[dir_num] , y +dy[dir_num]
    cnt += 1
    if x == 0 and y == 0 :
        second = cnt
        check = True
        break


if check :
    print(second)
else : 
    print(-1)

    