# 매개 변수가 있는 생성자

class Car:
    # color = ""
    # speed = 0

    def __init__(self, value1, value2):
        self.color = value1
        self.speed = value2

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

    def printMessage(self):
        print(f'{self.color}색 자동차, 속도는 {self.speed} Km 입니다.')

myCar1 = Car('빨강', 120)
myCar1.printMessage()

myCar2 = Car('파랑', 100)
myCar2.printMessage()

myCar3 = Car('노랑', 0)
myCar3.printMessage()

# 인스턴스 할당 id 확인
print(id(myCar1))
print(id(myCar2))
print(id(myCar3))