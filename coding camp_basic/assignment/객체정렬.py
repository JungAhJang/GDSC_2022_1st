class User :
    def __init__(self,name=0,height=0,weight=0) :
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
arr = []
for _ in range(n) :
    name,height,weight = tuple(input().split())
    arr.append(User(name,int(height),int(weight)))

#객체 정렬
arr.sort(key=lambda x:x.height)

for i in range(n) :
    print(f"{arr[i].name} {arr[i].height} {arr[i].weight}")

# 이것도 가능!!
# for elem in arr :
#     print(elem.name, elem.height, elem.weight)