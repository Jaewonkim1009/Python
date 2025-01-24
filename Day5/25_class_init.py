# 생성자 : 인스턴스를 생성하면서 필드값을 초기화시키는 함수
# __init__()

class Car:
    # color = ""
    # speed = 0
    
    # 생성자 입력 (매개 변수가 없는 생성자)
    def __init__(self):
        self.color = '빨강'
        self.speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

    def printMessage(self):
        print(f'{self.color}색 자동차, 속도는 {self.speed} Km 입니다.')

myCar1 = Car()
myCar1.printMessage()

myCar2 = Car()
myCar2.printMessage()

myCar3 = Car()
myCar2.printMessage()
