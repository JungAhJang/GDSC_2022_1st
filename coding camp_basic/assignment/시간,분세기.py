#2011년 11월 11일 a시 b분에서 시작하여 2011년 11월 11일 c시 d분까지 몇 분이 걸리는지를 계산하는 프로그램을 작성해보세요.

#1
#제일 간단한거는
#a시b분이 총 몇분인지 계산
#C시d분이 총 몇분인지 계산

a, b, c, d = tuple(map(int,input().split()))

start = (a * 60) + b
end = (c * 60) +d

result = end - start

print(result)

#2 흐른 시간 계산
a, b, c, d = tuple(map(int,input().split()))

hours, mins = a , b
elapsed_time = 0

while True :
    if hours == c and mins == d :
        break
    mins += 1
    elapsed_time += 1

    if mins == 60 :
        mins = 0
        hours += 1

print(elapsed_time)
