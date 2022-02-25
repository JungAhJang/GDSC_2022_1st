#1번째 N번째 줄까지 별 출력을 다음 모양으로 재귀함수를 이용해 출력하는 프로그램을 작성해보세요.

n = int(input())

def star(n) :
    if n == 0 :
        return
    star(n-1)
    print("*" * n)

star(n)