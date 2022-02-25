#N개의 원소로 이루어진 배열을 인자로 받아 각각 절대값을 씌워주는 함수를 작성하고, 해당 함수를 호출 한 후 각 원소의 값을 출력하는 프로그램을 작성해보세요. 단, 값을 반환하지 않는 함수를 이용해 문제를 해결해야 합니다.

n = int(input())
arr = list(map(int,input().split()))

def absolute_value(arr) :
    for i in range(len(arr)) :
        if arr[i] < 0 :
            arr[i] = arr[i] * -1

absolute_value(arr)

for elem in arr :
    print(elem, end=" ")