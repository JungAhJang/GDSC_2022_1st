#주어진 입력 문자열에 대하여 목적 문자열이 부분 문자열로 존재하는 경우, 부분 문자열의 시작 인덱스를 출력하는 코드를 작성해보세요. 단, 함수를 이용하여 문제를 해결해주세요. 인덱스는 0부터 시작한다고 가정합니다.

string = input()
find_string = input()
check = False
cnt = 0

def find() :
    global check, cnt
    for i in range(len(string)) : #입력받은 문자열만큼 반복
        if string[i] == find_string[0] :  #입력받은 문자열의 i번째 원소와 찾고자 하는 문자열의 i번째 원소가 같다면
            for j in range(len(find_string)) : #찾고자하는 문자열의 길이만큼 반복
                if string[i+j] == find_string[j] : #찾고자 하는 문자열길이만큼 반복해 부분문자열이 맞나 체크
                    cnt += 1 
            if cnt == len(find_string) : #찾고자 하는 부분 문자열 길이만큼 같다면
                check = True
                idx = i #처음 인덱스를 저장
            else :
                cnt = 0
                check = False
    if check :
        print(idx)
    elif not check :
        print(-1)

find()
