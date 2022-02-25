n = int(input())

given_input = [
    tuple(input().split())
    for _ in range(n)
]

studendts = [
    (name,int(kor),int(eng),int(math))
    for (name,kor,eng,math) in given_input
]

studendts.sort(key=lambda x: x[1]+x[2]+x[3])

for name,kor,eng,math in studendts :
    print(name,kor,eng,math)