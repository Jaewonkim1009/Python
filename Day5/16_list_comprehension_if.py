# 0 ~ 9 까지의 일련 번호로 이루어진 리스트를 생성해보자.(단, 짝수만 포함)

# 기본 방식
numbers = []
for i in range(10):
    if i % 2 == 0:
        numbers.append(i)
print(numbers)


# 리스트 내포
numbers=[i for i in range(10) if i % 2 == 0]
print(numbers)

even_numbers = [i for i in range(500) if i % 10 == 0]
print(even_numbers)

