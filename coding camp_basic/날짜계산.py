#2011년 m1월 d1일로부터 2011년 m2월 d2일까지는 총 몇 일이 있는지를 계산하는 프로그램을 작성해보세요. 2011년은 윤년이 아닌 해이기 때문에 2월은 28일까지 있습니다.

m1, d1, m2, d2 = tuple(map(int,input().split()))

#1 m2에서 m1을 빼는 방법
num_of_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
elapsed_day = 0
month = m1
day = d1

while True :
    if month == m2 and day == d2 :
        break 
    day += 1
    elapsed_day += 1

    if day > num_of_days[month] :
        month += 1
        day = 1
elapsed_day += 1
print(elapsed_day)

