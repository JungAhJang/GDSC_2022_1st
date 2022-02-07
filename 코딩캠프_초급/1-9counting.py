# arr = [1, 5, 2, 2, 1, 6, 3, 1, 3, 4]

# for i in range(1, 7):
#     cnt = 0
#     for elem in arr:
#         if elem == i:
#             cnt += 1
    
#     print(f"숫자 {i} - {cnt}번")

count_arr = [0] * 7

# 개수 세기
arr = list(map(int, input().split()))
for elem in arr:
    count_arr[elem] += 1

# 개수 출력
for i in range(1, 7):
    cnt = count_arr[i]
    print(f"숫자 {i} - {cnt}번")