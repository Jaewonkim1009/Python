# 리스트 내포

# 기본 문법 : [표현식 for 변수 in 반복 가능한 객체 if 조건]
# 표현식 : 리스트의 각 요소를 어떻게 변환할지 결정
# for 변수 in 반복 가능한 객체 : 반복문을 통해 요소 순회
# if 조건 


# 0 부터 5개의 일련번호로 구성 된 리스트를 생성하여 출력해보자.
# 기본 반복문
numbers = []
for i in range(5):
    numbers.append(i)
print(numbers)

# 리스트 내포
numbers = [i for i in range(5)] 
print(numbers)

list = [i for i in range(5)]
print(list)

