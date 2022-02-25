#소문자 알파벳으로 이루어진 5행 3열의 배열이 주어지면 대문자로 바꾸어서 출력하는 프로그램을 작성해보세요.

arr = [
    input().split()
    for _ in range(5)
]

for i in range(5) :
    for j in range(3) :
        arr[i][j] = arr[i][j].upper()
        print(arr[i][j], end=" ")
    print()

