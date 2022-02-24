string = input()
find_string = input()

#범위 판단
def in_range(i,j,n) :
    return i+j < n

def find_idx(string,find_string) :
    n, m = len(string) , len(find_string)
    for i in range(n) : #입력받은 문자열만큼 반복, 시작점부터문자열길이까지 문자열이 일치하는지
        cnt = 0
        for j in range(m) :
            if in_range(i,j,n) and string[i+j] == find_string[j] :
                cnt += 1 
        if cnt == m :
            idx = i #시작 문자열의 위치 반환
            return idx
    return -1

print(find_idx(string,find_string))
