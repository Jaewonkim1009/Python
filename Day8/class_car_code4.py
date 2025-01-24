class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def getSpeed(self):
        return self.speed
    
    def setSpeed(self, speed):
        self.speed = speed

    def drive(self):
        self.setSpeed(60)
        print(f"{self.model}이(가) 달립니다.")

    def turn(self, direction):
        print(f"방향을 {direction}으로 바꿉니다.")

    def parking(self):
        print(f"{self.model}이(가) 주차를 합니다")
                

myCar = Car(0, "blue", "E-class")

print("자동차 객체를 생성하였습니다.")
print("자동차의 속도는", myCar.getSpeed())
print("자동차의 색상은", myCar.color)
print("자동차의 모델은", myCar.model)

myCar.drive()
print("자동차의 속도는", myCar.speed, "입니다.")
myCar.turn("왼쪽")
myCar.parking()