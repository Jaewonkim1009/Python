# 튜플 <-> 리스트 변환하기

mylist = [1, 2, 3, 4] # list(range[1,5])
mytuple = tuple(mylist)
print(mytuple)

mylist2 = list(mytuple)

print(mylist2)

# 튜플에 추가하기
single_tuple = ('apple',)
print(single_tuple)

no_tuple = ('apple')
print(no_tuple)

fruits = ('apple', 'banana', 'kiwi')
fruits += ('cherry', 'grape')
print(fruits)

# 리스트에 추가하기
mylist += (40, 50)
print(mylist)

# 튜플의 패킹과 언패킹
t = ('apple', 'banana', 'grape')
(s1, s2, s3) = t  # (s1 : apple , s2 : banana , s3 : grape)
n1 = 10
n2 = 90
n1, n2 = (n2, n1) # (90, 10)

#enumerate() 사용하기 
fruits = ['apple', 'banana', 'grape']
for index, value in enumerate(fruits): # 인덱스를 사용 할 수 있게 해준다.
    print(index, value) # 인덱스 밸류가 출력 된다.


# 튜플
# 항목을 ()으로 감싼다.
# 변경 불가능한 객체
# 약 33개의 메소드 지원
# 딕셔너리에서 키 로 이용할 수 있다.

# 리스트
# 항목을 [] 으로 감싼다.
# 변경 가능한 객체
# 약 46개의 메소드 지원
# 딕셔너리에서 키로 이용할 수 없다.