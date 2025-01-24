class Car:
    # 기본 값 지정
    def __init__(self, maker, model, color, speed, direction, status = True):
        self.maker = maker
        self.model = model
        self.color = color
        self.speed = speed
        self.direction = direction
        self.status = status
        print('자동차 객체를 생성하였습니다.')

    # set 값 지정    
    def setMaker(self, maker):
        self.maker = maker
        print(f'자동차의 브랜드는 {maker} 브랜드 입니다.')
    def setModel(self, model):
        self.model = model    
        print(f'자동차의 모델은 {model} 입니다.')    
    def setColor(self, color):
        self.color = color
        print(f'자동차의 색상은 {color}색 입니다.')
    def setSpeed(self, speed):
        self.speed = speed
        print(f'현재 속도는 {speed}Km 입니다.')
    def setDirection(self, direction):
        self.direction = direction
        print(f'현재 {direction} 중 입니다.')
    def setStatus(self, status = True):
        self.status = status
        if status == True:
            print('현재 주차 중입니다.') 
        else:
            pass  

    # set 값 받아오기
    def getMaker(self):
        return self.maker   
    def getModel(self):
        return self.model    
    def getColor(self):
        return self.color    
    def getDirection(self):
        return self.direction
    def getStatus(self):
        return self.status
    # 상태 확인용
    def showInfo(self):
        print(self.maker, self.model, self.color, self.speed, self.direction, self.status)
    
    # 출력
    def total(self):
        if self.status == True:
            print(f'{self.maker}의 모델 {self.model}의 색상은 {self.color}색이고\n'
               f'현재 {"주차 중" if self.status else ""} 입니다.')
        else:
            print(f'{self.maker}의 모델 {self.model}의 색상은 {self.color}색이고\n'
                f'현재 속도는 {self.speed}Km로 {self.direction} 중입니다.')



car1 = Car('BMW', '520i', '검정', 0, '우회전', True)
print('-' * 50)
car1.total()

car2 = Car('현대자동차', '그랜져', '흰', 80, '주행', False)
print('-' * 50)
car2.total()
print('-' * 50)

car3 = Car('','','','','',False)
car3.setMaker('벤츠')
car3.setModel('E-Class')
car3.setColor('흰')
car3.setSpeed(120)
car3.setDirection('주행')
car3.setStatus(False)
car3.total()
print('-' * 50)

car3.total()
print('-' * 50)
