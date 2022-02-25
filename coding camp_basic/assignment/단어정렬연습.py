n = int(input())
# arr = []
# for _ in range(n) :
#     arr.append(input())
#리스트 컴프리헨션으로 어팬드하기
arr = [
    input()
    for _ in range(n)
]

#정렬하기
arr.sort()

for elem in arr :
    print(elem)