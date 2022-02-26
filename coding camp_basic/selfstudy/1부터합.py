#정수 N이 주어지면 재귀함수를 이용하여 1부터 N까지의 합을 구하여 출력하는 프로그램을 작성해보세요.

n = int(input())

def hap(n) :
    if n == 1 :
        return 1
    return hap(n-1) + n

print(hap(n))