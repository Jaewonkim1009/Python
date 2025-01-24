class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name, self.age)

class Student:
    def __init__(self, id):
        self.id = id
    def getId(self):
        return self.id

# Person 과 Student를 상속 받는다
class CollegeStudent(Person, Student):
    def __init__(self, name, age, id):
# 상속 받을 클래스가 다중이므로 super 대신 지정 해주어야 함
        Person.__init__(self, name, age)
        Student.__init__(self,id)

obj = CollegeStudent('Kim', 22, '100036') 
obj.show() 
print(obj.getId()) 

# 메소드 오버라이딩
# 자식 클래스의 메소드가 부모 클래스의 메소드를 재정의
import math
class Shape:
    def __init__ (self):
        pass
    def draw(self):
        print('draw()가 호출 됨')
    def get_area(self):
        print('get_area()가 호출됨')
# Shape 상속
class Circle(Shape):
    def __init__(self, radius=0):
        super().__init__() 
        self.radius = radius
# 메소드 오버라이딩(재정의)
    def draw(self):
        print('원을 그립니다.')
    def get_area(self):
        return math.pi * self.radius ** 2
    
c = Circle(10)
c.draw()
print('원의 면적 : ', c.get_area())
