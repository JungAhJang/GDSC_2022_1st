#문제: 5명의 이름, 키, 몸무게가 주어지면 이름순으로 정렬하여 출력하고, 키가 큰 순으로 정렬하여 출력하는 프로그램을 작성해보세요. 단, 동일한 이름과 키가 주어지지 않는다고 가정해도 좋습니다.

#문제: 5명의 이름, 키, 몸무게가 주어지면 이름순으로 정렬하여 출력하고, 키가 큰 순으로 정렬하여 출력하는 프로그램을 작성해보세요. 단, 동일한 이름과 키가 주어지지 않는다고 가정해도 좋습니다.

class User :
    def __init__(self,name,height,weight) :
        self.name = name
        self.height = height
        self.weight = weight

users = []
for _ in range(5) :
    name, height, weight = tuple(input().split())
    users.append(User(name,int(height),float(weight)))

print("name")
name_users = users
name_users.sort(key=lambda x: x.name)
for user in name_users :
    print(f"{user.name} {user.height} {user.weight:.1f}")

print()

print("height")
height_users = users
height_users.sort(key=lambda x: x.height , reverse=True)
for user in height_users :
    print(f"{user.name} {user.height} {user.weight: .1f}")
