#숫자 29를 2진법으로 표현하자

n = 29
digits = []

while True :
    if n//2 ==1 :
        break 
    digits.append(n%2)
    n //= 2

for digit in digits[::-1]:
    print(digit, end="")