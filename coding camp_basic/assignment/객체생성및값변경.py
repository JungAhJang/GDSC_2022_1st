# "아이디", "레벨"을 같이 저장할 수 있는 형태(c언어의 경우 구조체를, 다른 언어의 경우 class)를 정의하고, 2개의 객체를 선언한 후, 하나의 객체는 아이디에 "codetree", 레벨에 "10"으로 각각 초기화하고 다른 객체는 새롭게 입력받은 값을 넣어 입출력 예제와 같이 출력하는 프로그램을 작성해보세요.



class User :
    def __init__(self, user_id="None",user_lv="0" ) :
        self.user_id = user_id
        self.user_lv = user_lv
    
u1 = User("codetree","10")

u2 = User() #u2사용자에 값을 받을 빈 껍데기를 만듦
u2.user_id, u2.user_lv = tuple(input().split()) #u2사용자에 받을 값을 입력
u2 = User(u2.user_id,u2.user_lv) #받은 값을 u2에 집어넣음

# u2 = User(tuple(input().split())) 이렇게 한번에 쓰면 언팩킹이 안되기 때문에 안됨. 
#즉, 클래스에 들어가는 인자는 각 각 하나인 형태여야한다는것, (1,2)가 들어가는게 아니라 1,2가 들어가야함


print(f"user {u1.user_id} lv {u1.user_lv}")
print(f"user {u2.user_id} lv {u2.user_lv}")