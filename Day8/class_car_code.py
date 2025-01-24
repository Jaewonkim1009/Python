class Car :
    def __init__(self):
        self.speed=0
        self.direction=0
        self.color=''
        self.model=""
        
    def setSpeed(self, set_number):
        print('setSpeed =', set_number)
        self.speed =set_number

    def speed_up(self) :
        self.speed +=1

    def speed_down(self):
        self.speed -= 1

    def turn_right(self):
        self.direction +=1

    def turn_left(self):
        self.direction -=1

    def setting_car(self,my_color,my_model):
        self.color=my_color
        self.model=my_model

    def show_status(self):
        print('1. Object my_car was made')
        print('*'*35, '  STATUS OF MY CAR','*'*35)
        print('2. speed : ',self.speed, end = "")
        print('         3. Model of my_car is :', self.model,end ='')
        print('         4 Color of my_car is', self.color)
        if self.direction==0 :
            dir_lamp = '^'
        elif self.direction >=0:
            dir_lamp = '->'
        elif self.direction <=0:
            dir_lamp = '<-'
        print(' Direction Lamp :  '+dir_lamp*abs(self.direction),'  amount=', abs(self.direction))

        print('*'*90)
        print('')

my_car = Car()
my_car.setting_car('Red','Pony')
my_car.show_status()

my_car.setSpeed(40)
my_car.show_status()

my_car.speed_up()
my_car.show_status()
my_car.turn_right()
my_car.show_status()

my_car.turn_left()
my_car.turn_left()
my_car.turn_left()
my_car.turn_left()
my_car.show_status()

for i in range(10):
    my_car.turn_right()
my_car.show_status()