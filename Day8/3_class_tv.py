# TV 클래스를 작성해보자.
class TV:

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
    
t1 = TV(3,5,True)
t1.show()
t1.setChannel(7)
print('현재 채널은' , t1.getCannnel(), '번 입니다.')
t1.setVolume(30)
t1.show()
print('현재 볼륨은', t1.getVolume(), '입니다.')
t1.power()

t2 = TV(53, 30, False)
t2.show()
t2.setChannel(25)
print(f'현재 채널은 {t1.getCannnel()} 번 입니다.')
t2.setVolume(50)
print(f'현재 볼륨은 {t2.getVolume()} 입니다.')
t2.show()
t2.power()