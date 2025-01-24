# 객체

class Counter:
    def __init__(self): # 생성자 지정함으로 인스턴스 생성시 0을 기본값으로 지정
        self.count = 0
    def increment(self): # increment() 함수를 호출 할 때마다 1씩 증가
        self.count += 1

a = Counter() # 클래스 Counter()의 생성자 호출, 인스턴스 a 생성
a.increment() #1
print('카운터의 값은',a.count)
a.increment() #2
print('카운터의 값은',a.count)
a.increment() #3
print('카운터의 값은',a.count)
a.increment() #4
print('카운터의 값은',a.count)
a.increment() #5
print('카운터의 값은',a.count)

b = Counter()
b.increment() #1
print('b 카운터의 값은',b.count)
b.increment() #2
print('b 카운터의 값은',b.count)