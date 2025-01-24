import os

print('1. 현재 작업 폴더 : ', os.getcwd())
print('-' * 50)
# files 폴더로 변경하기
os.chdir('files')
print('2. os.chdir() 작업 후 폴더 : ', os.getcwd())
print('-' * 50)
# 다시 상위 폴더로 변경하기
os.chdir('..')
print('3. 상위 폴더로 변경 : ',os.getcwd())
print('-' * 50)
# 작업 중인 폴더에서 특정 유형의 파일을 출력하기
for filename in os.listdir():
    if filename.endswith('.py'):
        print(filename)
print('-' * 50)

# 작업 중인 폴더에서 종류가 파일인 것만 출력하기
for filename in os.listdir():
    if os.path.isfile(filename):
        print(filename)
print('-' * 50)

# 파일에서 특정 단어가 포함 된 파일을 출력하기
os.chdir('Day7')
print(os.getcwd())
for filename in os.listdir():
    if os.path.isfile(filename):
        print(filename)
        infile = open(filename, 'r', encoding='utf8')
        for line in infile:
            e = line.strip()
            if 'python' in e:
                print('   ------- python 단어가 포함된 파일 : ', filename, ':', e)
        infile.close()
print('-' * 50)
