import sys
class CodeName :
    def __init__(self,name=0,score=0) :
        self.name = name
        self.score = score

#5명 입력 받기
CodeNames = []
for _ in range(5) :
    name,score = tuple(input().split())
    CodeNames.append(CodeName(name,int(score)))

# CodeNames= [CodeName(A,50),(),...]
min_socre = sys.maxsize
min_name = ""

for i in range(5) : 
    if min_socre > CodeNames[i].score :
        min_socre = CodeNames[i].score
        min_name = CodeNames[i].name

print(min_name,min_socre)


# 선생님 답: 최소 점수를 갖는 유저 찾기
min_idx = 0
for i in range(1, 5):
    if users[min_idx].score > users[i].score:
        min_idx = i

# 출력
print(users[min_idx].code_name, users[min_idx].score)