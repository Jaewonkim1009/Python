#은행 계좌는 현재 잔액(balance)만을 인스턴스 변수로 가진다.
#생성자와 인출 메소드 withdraw()와 저축 메소드 deposit()만을 가정하자.
#은행 계좌의 잔액은 외부에서 직접 접근하지 못하도록 해라.
#통장에서 000가 출금되었음
#통장에서 000가 입금되었음

class Bank:
    def __init__(self ,balance = 0):
        self.__balance = balance
    
    def Withdraw(self, withdraw):
        if withdraw > self.__balance:
            print('잔액이 부족합니다.')
        else:
            self.__balance -= withdraw
            print(f'{withdraw}원이 출금 되었음. 현재 잔액 {self.__balance}원 입니다.')

    def Deposit(self, deposit):
        self.__balance += deposit
        print(f'{deposit}원이 입금 되었음. 현재 잔액 {self.__balance}원 입니다.')
        
    def getBalance(self):
        print(f'현재 잔액은 {self.__balance}원 입니다.')
        return self.__balance
    
account = Bank(5000)
account.Withdraw(5000)
account.Deposit(500000)
account.Deposit(10000)
account.Withdraw(1000000)
account.Deposit(6000000)
#print(f'현재 잔액은 {account.getBalance()}원 입니다.')
account.getBalance()

# 참조 공유
# a = account
# money = input('작업을 선택 해주세요 입금/출금 : ')
# if money == '입금':
#     deposit = int(input('입금하실 금액을 입력해주세요 : '))
#     a.Deposit(deposit)
# elif money == '출금':
#     withdraw = int(input('출금하실 금액을 입력해주세요 : '))
#     a.Withdraw(withdraw)
# else:
#     print('올바른 방식을 선택해주세요.')

