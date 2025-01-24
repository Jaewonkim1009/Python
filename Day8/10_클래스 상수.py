class Monster:
    # 상수 선언
    # 해당 값만 변경하면 프로그램에 적용 된 사항들이 한번에 바뀐다
    WEAK = 0
    NORMAL = 10
    STRONG = 20
    VERY_STRONG = 30

    def __init__(self):
        self.__health = Monster.NORMAL
    
    def eat(self):
        self.__health = Monster.STRONG
    
    def attack(self):
        self.__health = Monster.WEAK

# 특수 메소드
# + - * / 과 관련된 특수메소드 가 있다.
# 이 메소드는 객체에 대하여 + - * / 와 같은 연산을 적용하면 자동으로 호출된다.
# __eq__ 같다는 의미