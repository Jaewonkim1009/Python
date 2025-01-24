# Vector : (0,1) + (1,0) = (1,1) 인덱스 번째끼리 더하기
#          (1,0) - (0,1) = (0,0) 인덱스 번째끼리 빼기

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y) 

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y 
    
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
    
u = Vector2D(0,1)
v = Vector2D(1,0)
w = Vector2D(1,1)
a = u + v
b = v - w
print(a) # (1,1)
print(b) # (0,-1)
print(a==w)
print(u==v)