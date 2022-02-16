#n명의 이름, 키, 몸무게가 주어지면 키를 기준으로 오름차순으로 정렬하여 출력하는 프로그램을 작성해보세요. 단, 키가 동일한 경우에는 몸무게가 더 큰 사람이 먼저 나오도록 정렬해야 합니다. 키, 몸무게가 둘 다 동일한 경우는 없다고 가정해도 좋습니다.
n = int(input())

class User :
    def __init__(self,name,height,weight) :
        self.name = name
        self.height = height
        self.weight = weight

users = []
for _ in range(n) :
    name, height, weight = tuple(input().split())
    users.append(User(name,int(height),int(weight)))

users.sort(key=lambda x: (x.height,-x.weight))

for user in users :
    print(user.name, user.height, user.weight)