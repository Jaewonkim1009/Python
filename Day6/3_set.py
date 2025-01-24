# set() 사용하기
# 집합
# 고유한 값을 저장하는 자료구조
# 중복을 허용하지 않아 중복되는 값을 하나로 묶어서 저장
# 리스트와는 다르게 세트의 요소는 특정 순서로 저장되지 않으며 위치별로 액세스 할 수 없음

# 세트 생성하기
# 세트_이름 = {항목1, 항목2, 항목3...}
# numbers = {1, 2, 3}
# values = set()

# 리스트 <-> 세트
# numbers = set([1,2,3,1,2,3])
# print(numbers) = {1,2,3}
# letters = set("abc") # 요소를 하나씩 분리 해준다

numbers = set([1, 2, 3, 1, 2, 3])
print(numbers)

# set은 인덱스로 꺼낼 수 없다.
# numbers[0] <- 인덱스로 꺼낼 수 없다.
num1, num2, num3 = numbers
print(num1, num2, num3)

# 세트의 연산
# 사용 가능 all, any, enumerate, len, max, min, sorted, sum

# set에서 함수 사용하기
fruits = {'apple', 'banana', 'cherry'}
size = len(fruits)
print(f'집합 fruits에서는 {size} 개의 원소가 있습니다.') # 3 출력

if 'apple' in fruits:
    print(f'집합 안에 apple이 있습니다.')

for x in fruits: 
    print(x, end=' ') # 일렬로 출력, set이므로 순서는 랜덤으로 나온다
for x in fruits:
    print(x) # 하나씩 출력

for x in sorted(fruits): # 알파벳 순으로 정렬하기
    print(x, end=' ') 

# 세트의 요소 추가하기
fruits.add('kiwi') # kiwi 추가
print(fruits)

fruits.remove('kiwi') # kiwi 삭제
print(fruits)

result = {x for x in fruits if len(x) > 5} # 리스트 내포
print(result)

# 짝수만 가진 set 만들기
aList = [1, 2, 3, 4, 5, 1, 2, 3]
aset = set(aList)
result = {i for i in aset if i % 2 == 0}
print(result)

bList = [1, 2, 3, 4, 5, 1, 2, 3]
bset = set(bList)
results = set()
for i in bset:
    if i % 2 == 0:
        results.add(i)
print(results)


# 부분 집합 연산
# result 가 aset의 부분 집합인지 확인
print(aset) # {1, 2, 3, 4, 5}
print(result) # {2, 4}

if result < aset:
    print('result는 aset의 부분 집합 입니다.')
print(result.issubset(aset))

# 합집합
# result 와 aset의 합집합 확인
print(result | aset)
result.union(aset)

# 교집합
# result 와 aset의 교집합 확인
print(result & aset)
result.intersection(aset)

# 차집합
# result 와 aset의 차집합 확인
print(result - aset)
print(result.difference(aset))


hello = set('Hello World!')
how = set('How are you?')
print(how & hello)
print(hello.intersection(how) - {' '})

# s1 = input('첫 번째 문자를 입력 해주세요 : ')
# s2 = input('두 번째 문자를 입력 해주세요 : ')
# s1_set = set(s1)
# s2_set = set(s2)
# print(s1_set.intersection(s2_set) - {' '})

# list_a = {i for i in (set(s1) & set(s2)) if i != " "}
# print(list_a)
# for i in list_a:
#     print(i, end=" ")

# s3 = input('첫 번째 문자를 입력 해주세요 : ').replace(' ','')
# s4 = input('두 번째 문자를 입력 해주세요 : ').replace(' ','')
# s3_set = set(s3)
# s4_set = set(s4)
# print(s3_set.intersection(s4_set))

# s5 = input('첫 번째 문자를 입력 해주세요 : ')
# s6 = input('두 번째 문자를 입력 해주세요 : ')
# set_a = set(s5) & set(s6)
# set_a.remove(" ")
# print(set_a, end=" ")

text_a = 'I have a dream that one day every valley shall be exalted and every hill and mountain shall be made low'
print(len(set(text_a.split())))


text_a = ('I have a dream that one day every valley shall be exalted and every hill and mountain shall be made low')
text_b = ('I have a dream that one day every valley shall be exalted and every hill and mountain shall be made low')
set_a = set(text_a.split())
set_b = set(text_b.split())
set_c = set_a | set_b
print(f'중복되지 않는 단어의 갯수는 {len(set_c)} 개 입니다.')


# txt = input("텍스트를 입력해주세요 : ")
# words = txt.split(" ")
# aSet = set(words)
# print('사용 된 단어의 갯수는 : ', len(aSet))
# print(aSet)