arrA = input()
arrB = input()

a, b = len(arrA) , len(arrB) #문자열의 개수
result = 0

def in_range(i,j,n) :
    return i+j < n

def in_range2(i,n) :
    return i<n

for i in range(a) :
    if in_range2(i,b)and arrA[i] == arrB[i] : #첫 글자가 같다면 검사 시작
        cnt = 0
        for j in range(b) : #배열B의 길이동안 반복
            if in_range(i,j,a) and arrA[i+j] == arrB[j] :
                cnt += 1
        if cnt == b : #부분 문자열 이라면
            result += 1


print(result)