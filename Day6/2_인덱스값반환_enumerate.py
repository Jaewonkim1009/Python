fruits = ['apple', 'mango', 'grape']
for fruit in fruits:
    print(fruits)

#enumerate() 사용하기 
for index, value in enumerate(fruits):
    print(index, value) # 인덱스와 밸류가 출력 된다.

for index, value in enumerate(fruits):
    if index % 2 == 0: # 인덱스 짝수만 출력
        print(index, value)

