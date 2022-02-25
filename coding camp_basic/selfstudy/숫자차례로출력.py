#정수 N이 주어지면 재귀함수를 2개 작성하여 첫 번째 재귀함수를 이용하여 1부터 N까지 숫자를 차례대로 출력하고, 두 번째 재귀함수를 이용하여 N부터 1까지 차례로 출력하는 프로그램을 작성해보세요. 단, 두 재귀함수 모두 인자로 N을 넘기는 함수여야만 합니다.

n = int(input())

def ordered_print(n) :
    if n == 0 :
        return 
    ordered_print(n-1)
    print(n, end=" ")

def reversed_print(n) :
    if n == 0 :
        return
    print(n, end=" ")
    reversed_print(n-1)

ordered_print(n)
print()
reversed_print(n)