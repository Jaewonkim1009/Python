# class의 속성 = 변수 (Field)
# class의 기능 = 함수 (method)
# class안에서 구현 된 함수는 함수가 아닌 메서드라고 한다
# 첫 글자는 대문자로 구성한다.

# 클래스 선언
class Car:
    # 속성(필드) 구성
    color = ""
    speed = 0

    # 기능(메소드) 구성
    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value
    
    def printMessage(self):
        print(f'이 차의 색상은 {self.color}색이고 현재 속도는 {self.speed} Km 입니다.')

#인스턴스 생성
myCar1 = Car()
myCar2 = Car()
myCar3 = Car()
myCar1.printMessage()

#print(type(myCar1)) # 타입 확인

myCar1.color = '빨강'
myCar1.upSpeed(100)
myCar1.printMessage()

myCar2.color = '파랑'
myCar2.downSpeed(50)
myCar2.printMessage()

myCar3.color = '노랑'
myCar3.upSpeed(80)
myCar3.printMessage()

print(f"자동차3의 색상은 {myCar3.color}이고, 현재 속도는 {myCar3.speed}입니다.")
