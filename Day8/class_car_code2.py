import random
class Car:
  class_var = 0
  def __init__(self, model, color, speed=0):
    self.model = model
    self.color = color
    self.speed = speed
    print('자율 주행 자동차 객체를 생성하였습니다.')

  def get_speed(self):
    return self.speed
  def set_speed(self, speed):
    self.speed = speed
    print(f'자동차의 속도가 {self.speed} 으로 변경되었습니다')

  def get_color(self):
    return self.color

  def get_model(self):
    return self.model

  def drive(self):
    print('자동차를 주행중 입니다')

  def turn(self):
    print(f'{random.choice(['우회전', '좌회전', '유턴'])} 하셨습니다')

  def park(self):
    print(f'자동차를 주차하셨습니다')


c = Car('E-class', 'blue')
print(f'자동차의 모델은 {c.get_model()} 입니다')
print(f'자동차의 색상은 {c.get_color()} 입니다')

c.drive()
print(f'자동차의 속도는 {c.get_speed()} 입니다.')
c.set_speed(60)

c.turn()
c.turn()
c.turn()
c.turn()
c.turn()
c.turn()

c.park()