# 숫자 제곱 리스트
# 1 ~ 10 까지의 숫자들의 제곱값 리스트 생성하기

list = []

for i in range(1, 11):
    list.append(i * i)
print(list)


list = [i ** 2 for i in range(1, 11)] 
print(list)

