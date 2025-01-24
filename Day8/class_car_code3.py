class Car:
    def __init__(self, model, color, speed = 0):
        self.model = model
        self.color = color
        self.speed = speed
        print("자동차 객체를 생성하였습니다.")
        # print(f"자동차 모델: {self.model}")
        # print(f"자동차 색상: {self.color}")
        # print(f"자동차 속도: {self.speed}km/h")
    
    def getModel(self):
        return self.model

    def getColor(self):
        return self.color
    
    def getSpeed(self):
        return self.speed

    def changeSpeed(self, speed):
        if speed >= 180:
            print("제한 속도를 초과할 수 없습니다.")
        else:
            if self.speed < speed:
                self.speed = speed
                print(f"자동차 속도를 {self.speed}km/h 으로 올립니다.")
            elif self.speed > speed:
                self.speed = speed
                print(f"자동차 속도를 {self.speed}km/h 으로 내립니다.")
            else:
                print("속도가 변경되지 않았습니다.")     

    def turn(self, direction):
        self.direction = direction
        print(f"자동차가 {direction}회전 합니다.")
    
    def park(self):
        print("자동차를 주차하였습니다.")

    def show_status(self):
        print("-" * 50)
        print(f"현재 {self.color} {self.model} 자동차의 속도는 {self.speed}km/h 입니다.")
        print("-" * 50)

# 인스턴스 생성
c1 = Car("E-Class", "Blue")
print(f"자동차 모델: {c1.getModel()}, 색상: {c1.getColor()}, 속도: {c1.getSpeed()}km/h")
c1.changeSpeed(50)
c1.changeSpeed(30)
c1.changeSpeed(181)
c1.turn("좌")
c1.park()
c1.show_status()

c2 = Car("G80", "Red")
print(f"자동차 모델: {c2.getModel()}, 색상: {c2.getColor()}, 속도: {c2.getSpeed()}km/h")
c2.changeSpeed(80)
c2.changeSpeed(60)
c2.turn("우")
c2.park()
c2.show_status()
