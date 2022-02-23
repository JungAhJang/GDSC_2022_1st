#좌표평면 위 (0, 0)에서 북쪽을 향한 상태에서 움직이는 것을 시작하려 합니다. N개의 명령에 따라 총 N번 움직이며, 명령 L이 주어지면 왼쪽으로 90도 방향 전환을, 명령 R이 주어지면 오른쪽으로 90도 방향전환을 하고, 명령 F가 주어지면 바라보고 있는 방향으로 한칸 이동하려고 합니다. 이동 이후 최종 위치를 출력하는 프로그램을 작성해보세요.

dir_num = 3
x, y = 0, 0
# 동0 남1 서2 북3
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
L_count = 0
R_count = 0

arr = list(input())

for elem in arr :
    if elem == "L" :
        L_count += 1
    elif elem == "R" :
        R_count += 1
    elif elem == "F" :
        if L_count > R_count :
            dir_m = L_count - R_count
            for _ in range(dir_m) :
                dir_num = (dir_num - 1 + 4) % 4
        elif L_count < R_count :
            dir_m = R_count - L_count
            for _ in range(dir_m) :
                dir_num = dir_num = (dir_num + 1) % 4
        x, y = x + dx[dir_num] , y + dy[dir_num]
        L_count = 0
        R_count = 0

print(x, y)

#해답
# x, y = 0, 0
# commands = input()

# dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
# dir_num = 3

# for command in commands:
#     if command == "L":
#         dir_num = (dir_num - 1 + 4) % 4
#     elif command == "R":
#         dir_num = (dir_num + 1) % 4
#     else:
#         x, y = x + dx[dir_num], y + dy[dir_num]

# print(x, y)




# # rotate direction
# dir_num = (dir_num + 1) % 4
# dir_num = (dir_num - 1 + 4) % 4

# #move
# x, y = x + dx[dir_num] + y + dy[dir_num] 