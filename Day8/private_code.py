class Account :
    def __init__(self, balance=1000):
        self.__balance=balance
        

    def withraw(self,money):
        self.__balance -= money
        print(f'통장에서 {money}원이 출금 되었음.')

    def deposit(self, money ):
       self.__balance +=money
       print(f'통장에서 {money}원이 입금 되었음.')

    def show_balnce(self):
        print(f'현재 잔고는 {self.__balance} 입니다')



print('*'*40)
my_account=Account()

my_account.show_balnce()
user_input = input("입출 금을 선택 하시오 (입금/출금): ")
if user_input == "입금":
    deposit=int(input('1.입금액을 입력하시오 >>>'))
    my_account.deposit(deposit)
else:
    withraw=int(input('1.출금액을 입력하시오 >>>'))
    my_account.withraw(withraw)

my_account.show_balnce()
print('*'*40)