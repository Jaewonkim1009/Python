 # 범위를 1부터 6까지 지정
values = range(1,7)

# values 의 숫자 중 짝수를 x에 대입해서 x의 제곱을 구하는 딕셔너리 생성
dic = {x: x**2 for x in values if x % 2 ==0} 
print(dic) # {2: 4, 4: 16, 6: 36}

# values 의 숫자를 정수 key와 문자열 value로 가져오는 딕셔너리 생성
dic = {i:str(i) for i in values}
print(dic) # {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6'}

# fruits 안에 있는 각 원소와 해당 원소들의 글자 수를 표시 하는 딕셔너리 생성
fruits = ['apple', 'banana', 'orange']
dic = {x:len(x) for x in fruits} 
print(dic) # {'apple': 5, 'banana': 6, 'orange': 6}


text_data = 'Create the highest, grandest vision possible for your life, because you become what you believe'
dic= {}
words = text_data.split()
for word in words:
    # if word in dic:
    #     dic[word] += 1
    # else:
    #     dic[word] = 1
    dic[word] = word.count(word)
print(dic)
for word, count in sorted(dic.items()):
    print(f'{word}의 등장 횟수 : {count}')

print('-'*30)

# set 활용
set_txt = sorted(set(words))
for word in set_txt:
    print(word,'의 등장 횟수: ', words.count(word))