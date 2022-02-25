#n개의 원소로 이루어진 수열 A가 주어지고, 숫자 m이 주어집니다. m이 1이 되기 전까지 m이 홀수면 1을 빼고, 짝수면 2로 나누는 걸 계속 반복하면서 A의 m번째 원소를 계속 더해 출력하는 프로그램을 작성해보세요. 단, 함수를 이용하여 문제를 해결해주세요

n, m = tuple(map(int,input().split()))

A = list(map(int,input().split()))

def calcul(A) :
    hap = 0
    global m
    while m :
        hap += A[m-1] 
        if m % 2 !=0 :
            m = m - 1
        elif m % 2 == 0 :
            m = m // 2
    return hap

print(calcul(A))