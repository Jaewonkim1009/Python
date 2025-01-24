# 함수 ord = 문자열에 해당하는 유니코드를 코드 포인트(정수)로 변환해줌
# ex) 'A' = 65 , 'a' = 97 , '가' = 44032 , '1' = 49

# 작업 폴더의 경로 알아보기
import os
print('현재 작업 디렉토리는', os.getcwd(), '입니다.')

print('새 파일.txt 파일을 생성하고 쓰기')

f = open('files/새 파일.txt', 'w', encoding='utf-8')
print('생성된 파일은 ----')
print(f)

for i in range(1, 6):
    data = '%d번째 줄입니다. \n' %i
    f.write(data)

f.close()

# 전체읽기
f = open('files/새 파일.txt', 'r', encoding='utf8') 
print('#### readline()은 파일의 내용을 한 줄, 한 줄 씩 읽어옵니다.')
while True:
    line = f.readline()
    if line:
        print(line)
    else:
        break
f.close()
print('-' * 20)    

# 전체 읽기를 readlines()로 구현하기, \n를 제거하자
f = open('files/새 파일.txt', 'r', encoding='utf8')
print('#### readlines()는 파일 전체를 읽습니다.')
lines = f.readlines()
for line in lines:
    print(line.rstrip())
f.close() 
print('-' * 20)    

# read()를 사용해도 전체 읽기를 할 수 있다
print('### read()는 파일의 내용 전체를 문자열로 반환한다.')
f = open('files/새 파일.txt', 'r', encoding='utf8')
data = f.read()
print(data)
f.close()
print('-' * 20)  

# read(1)로 단어를 하나씩 읽기
print('### read(1)은 하나의 문자를 읽어 온다.')
f = open('files/새 파일.txt', 'r', encoding='utf8')
ch = f.read(1)
while ch:
    print(ch)
    ch = f.read(1)
f.close()
print('-' * 20) 

# 자원을 자동으로 반환하는 with()문
print("")
print('### with()는 자원을 자동으로 반환해준다.')
with open('files/too.txt', 'w') as f:
    f.write('Life is short, you need python')

with open('files/too.txt', 'r') as f:
    print(f.read())
print('-' * 20) 

# 파일에 새로운 내용 추가하기
print('### 파일에 새로운 내용을 추가할 때에는 a모드를 사용한다.')
with open('files/too.txt', 'a') as f:
    f.write('\nPython is very fun')
with open('files/too.txt', 'r') as f:
    print(f.read())
print('-' * 20)