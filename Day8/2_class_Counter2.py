# class Counter:
#     def __init__(self, initValue = 0): # 매개변수 initValue를 지정해서 값을 입력 받을 수 있다. 초기값 = 0
#         self.count = initValue # 매개변수에서 입력 값을 받아 카운트 한다.
#     def increment(self):
#         self.count += 1
    
# a = Counter(100)
# b = Counter()
# print('a의 카운터는', a.count)
# print('b의 카운터는', b.count)

# a.increment()
# b.increment()
# print('a의 카운터는', a.count)
# print('b의 카운터는', b.count)

# a.increment()
# b.increment()
# print('a의 카운터는', a.count)
# print('b의 카운터는', b.count)

class Counter:
    def __init__(self, initValue = 0): # 매개변수 initValue를 지정해서 값을 입력 받을 수 있다. 초기값 = 0
        self.count = initValue # 매개변수에서 입력 값을 받아 카운트 한다.
    def increment(self):
        self.count += 1
    def setCount(self, count): # setter : 이 메소드를 호출하면서 count값을 주면 인스턴스의 count변수에 값을 전달
        self.count = count
    def getCount(self): # getter : 인스턴스 변수 setCount의 값을 받아 리턴하는 역할
        return self.count
