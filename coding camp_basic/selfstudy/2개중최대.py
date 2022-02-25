#삼항연산자
#정수 2개를 입력받아 두 값중 최댓값을 출력하는 프로그램을 작성해보세요.

a, b = tuple(map(int,input().split()))
max_num = a if a >b else b
print(max_num)