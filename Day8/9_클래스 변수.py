class Television:
    SERIALNUMBER = 0 # 클래스 변수 지정, 모든 인스턴스들이 공유한다.

    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
        Television.SERIALNUMBER += 1 # 인스턴스 변수가 생성 될때마다 +1
        self.number = Television.SERIALNUMBER
        
    def show(self):
        print(self.channel, self.volume, self.on, self.number)

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

t1 = Television(20, 5, True)
t1.show()
t2 = Television(30, 5, True)
t2.show()
t3 = Television(40, 5, False)
t3.show()
t4 = Television(50, 5, True)
t4.show()