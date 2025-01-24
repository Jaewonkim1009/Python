# 정보 은닉
# 인스턴스 변수를 private 정의 하려면 변수 이름 앞에 __ 을 붙인다
# private 가 붙은 인스턴스 변수는 클래스 내부에서만 접근 할 수 있다.

# 인스턴스 변수값을 반환하는 접근자 = gettets
# 인스턴스 변수값을 설정하는 설정자 = setters

class Student:
    def __init__(self, name = None, age = 0):
        self.__name = name
        self.__age = age
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def setName(self, name):
        self.__name = name
    def setAge(self, age):
        self.__age = age
obj = Student()
# print(obj.__age) 외부에서 변경 금지
print(obj.getAge())
print(obj.getName())

obj2 = Student('홍길동', 50)
print(obj2.getAge())
print(obj2.getName())

obj2.setAge(30)
obj2.setName('길동')
print(obj2.getAge())
print(obj2.getName())


#은행 계좌는 현재 잔액(balance)만을 인스턴스 변수로 가진다.
#생성자와 인출 메소드 withdraw()와 저축 메소드 deposit()만을 가정하자.
#은행 계좌의 잔액은 외부에서 직접 접근하지 못하도록 해라.
#통장에서 000가 출금되었음
#통장에서 000가 입금되었음
#현재 잔액은 000

class Bank:
    def __init__(self ,balance = 0):
        self.__balance = balance
    
    def Withdraw(self, withdraw):
        if withdraw > self.__balance:
            print('잔액이 부족합니다.')
        else:
            self.withdraw = withdraw
            self.__balance -= withdraw
            print(f'{withdraw}원이 출금 되었음. 현재 잔액 {self.__balance}원 입니다.')

    def Deposit(self, deposit):
        self.deposit = deposit
        self.__balance += deposit
        print(f'{deposit}원이 입금 되었음. 현재 잔액 {self.__balance}원 입니다.')
        
    def getBalance(self):
        return self.__balance
    
account = Bank(5000)
account.Withdraw(5000)
account.Deposit(500000)
account.Deposit(10000)
account.Withdraw(1000000)
account.Deposit(6000000)
print(f'현재 잔액은 {account.getBalance()}원 입니다.')

account2 = Bank()
money = input('작업을 선택 해주세요 입금/출금 : ')
if money == '입금':
    deposit = int(input('입금하실 금액을 입력해주세요 : '))
    account2.Deposit(deposit)
elif money == '출금':
    withdraw = int(input('출금하실 금액을 입력해주세요 : '))
    account2.Withdraw(withdraw)
else:
    print('올바른 방식을 선택해주세요.')
