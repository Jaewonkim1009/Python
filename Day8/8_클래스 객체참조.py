# is , is not
# if s is t:
#     print('2개의 변수는 동일한 객체를 참조 하고 있습니다.')
# if s is not t:
#     print('2개의 변수는 다른 객체를 참조하고 있습니다.')

# None 참조값
# 변수가 아무것도 참조하고 있지않다면 설정
# myTV = None

# 상수 = 변하지 않는 값
# 상수는 흔히 클래스 변수로 정의되고 대문자로 작성한다.



# 객체 참조 공유
class Television:

    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
    
    def show(self):
        print(self.channel, self.volume, self.on)

    def setChannel(self, channel):
        self.channel = channel

    def getCannnel(self):
        return self.channel
    
    def setVolume(self, volume):
        self.volume = volume

    def getVolume(self):
        return self.volume
    
    def power(self):
        if self.on == True:
            print('현재 TV 전원이 켜져 있습니다.')
        else:
            print('현재 TV 전원이 꺼져 있습니다.')

t1 = Television(23,12,True)

# 참조 공유
s = t1
s.show()
# 동일한 주소값을 가지고 있다.
print(id(t1))
print(id(s))

if s is t1:
    print('2개의 변수는 동일한 객체를 참조 하고 있습니다.')

t2 = Television(23,12,True)
print(id(t2))
if s is not t2:
    print('2개의 변수는 다른 객체를 참조 하고 있습니다.')

# 객체를 함수로 전달하는 방법
def setSlientMode(t): # t는 인스턴스 변수
    t.volume = 2

# setSlientMode()를 호출하여 객체의 인스턴스 변수를 변경해보자
setSlientMode(t2) # t = t2
t2.show()