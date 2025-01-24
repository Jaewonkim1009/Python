# 변수의 유효 범위 (Scope)
# 전역 변수 : 함수 외부에서 선언 된 변수로서 프로그램 전체에서 접근 가능
# 지역 변수 : 함수 내부에서 선언 된 변수로서 해당 함수에서만 접근 가능

x = 10

#지역변수
def my_function():
    x = 5
    print("지역 변수: ", x)
my_function()

#전역변수
print("전역 변수: ", x)

# 함수에서 전역변수 사용