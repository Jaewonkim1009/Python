import math

class Circle:
    
    def __init__(self, value = 1):
        self.value = value

    def getArea(self): # 넓이
        return math.pi * self.value ** 2 # pi * value의 제곱
    
    def getPrimeter(self): # 둘레
        return  math.pi * 2 * self.value # 2pi * value 
    
a = Circle(30)
print(f'원의 넓이는 {a.getArea()}')
print(f'원의 둘레는 {a.getPrimeter()}')
