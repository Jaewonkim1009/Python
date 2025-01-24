
# 0으로 나누는 에러 
(x,y) = (2,0)

try:
    z = x/y
except ZeroDivisionError as e:
    print(e)


try:
    z = x/y
except Exception:
    print('0으로 나누는 예외 발생') 



# Value 에러
# while True:
#     try:
#         n = input('숫자를 입력하세요 : ')
#         n = int(n)
#         break
#     except ValueError:
#         print('정수가 아닙니다. 다시 입력하세요')
# print('정수 입력 성공')

# input / output 에러
# try:
#     fname = input('파일 이름을 입력하세요 : ')
#     infile= open(fname , 'r')
# except IOError as e:
#     print(e)

# try:
#     fname = input('파일 이름을 입력하세요 : ')
#     infile= open(fname , 'r')
# # except Exception: (Exception 모든 예외처리를 할 수 있다)
# except Exception:
#     print('파일' + fname + '를 찾을 수 없습니다.')



# 다중 예외 처리
# except는 여러번 사용 가능, else 문 사용 가능


# finally
# 에러 발생유무에 상관없이 사용 할 수 있다.

# 파이썬에서는 오류가 감지되면 raise 문을 사용하여 예외를 생성한다.
# raise NameError('Hello')
# -> NameError: Hello

# 사용자 에러를 발생시키는 방법
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("0 으로 나눌 수 없습니다.")
    return a / b
try:
    print(divide(10, '0'))
except (ZeroDivisionError, TypeError) as e:
    print(f'예외 발생 : {e}' )

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("0 으로 나눌 수 없습니다.")
    return a / b
try:
    print(divide(10,0))
except (ZeroDivisionError, ValueError) as e:
    print(f'예외 발생 : {e}' )


# 사용자 정의 예외 클래스
class NegativeNumberError(Exception):
    '''음수를 입력 할 때 발생시키는 사용자 정의 예외'''
    def __init__(self, message = '음수는 허용되지 않습니다.'):
        self.message = message
        super().__init__(self.message) #super() : 부모 클래스 (Exception)의 생성자 __init__을 호출 한다.
# 함수에서 사용자 정의 예외 발생
def check_positive(number):
    if number < 0:
        raise NegativeNumberError(f'입력 값 {number}은(는) 음수입니다.')
        #raise NegativeNumberError()
# 예외 처리
try:
    num = int(input("숫자를 입력하세요 : "))
    check_positive(num)
except NegativeNumberError as e:
    print(f'NegativeNumberError 발생 : {e}')
except ValueError:
    print('유효한 숫자를 입력해야 합니다.')
else:
    print(f'입력하신 {num}는 정상적으로 입력 되었습니다.')
finally:
    print('프로그램을 종료합니다.')
