# 상속이 클래스 간의 'is-a(자식클래스is a부모클래스)' 관계를 생성하는데 사용
# 푸들은 강아지다
# 자동차는 차량이다
# 꽃은 식물이다
# 사각형은 모양이다
# ex) 부모클래스 : Animal 자식클래스 : Lion , Cat, Dog..

# class 자식클래스(부모클래스 or 슈퍼클래스)

class Car:
    def __init__(self, make, model, color, price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price

    def setMake(self, make):
        self.make = make
    
    def getMake(self):
        return self.make
    
    def getDesc(self):
        return '차량 = ('+str(self.make)+ ','+\
            str(self.model)+','+\
            str(self.color)+','+\
            str(self.price)+')'
class ElectricCar(Car):
    def __init__(self, make, model, color, price, batterySize):
        super().__init__(make, model, color, price) # 부모 클래스 상속
        self.batterySize = batterySize

    def setBatterySize(self, batterySize):
        self.batterySize = batterySize

    def getBatterySize(self):
        return self.batterySize

Car1 =ElectricCar('포르쉐', '타이칸', '흰색', '16000', '5000')
print(Car1.getDesc())
print(Car1.getMake())
print(Car1.getBatterySize())

car2 = Car('현대자동차', '아이오닉6', '흰색', '6000')
print(car2.getDesc())
# print(car2.getBatterySize()) 자식 클래스의 것은 가지고 올수없다.

print(type(Car1))
print(type(car2))

# isinstance() 함수
print(isinstance(Car1,Car)) # (자식클래스,부모클래스) 상속여부를 알 수 있음. True or False
print(isinstance(car2,Car))

class Parent(object):
    def __init__(self):
        self.__money = 100

class Child(Parent):
    def __init__(self):  # 부모클래스가 private이므로 자식클래스에서 사용 할 수 없다. 
        super().__init__(self)

# obj = Child()
# print(obj)

