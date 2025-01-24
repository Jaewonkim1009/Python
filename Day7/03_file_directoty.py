import os

# __file__ 은 현재 작성중인 파일을 의미함.
print('파일의 상대 경로 : ', os.path.realpath(__file__))
print('-' * 50)
print('파일의 절대 경로 : ', os.path.abspath(__file__))
print('-' * 50)
print('파일의 디렉토리 : ', os.path.dirname(__file__))
print('-' * 50)
# os.getcwd()는 현재 open 된 폴더를 의미함.
dir = os.getcwd()
print('현재 작업 디렉토리 : ', dir)
print('-' * 50)
# 현재 디렉토리의 하위 폴더와 파일을 모두 접근 할 때에는 os.walk()를 사용 한다.
# 하위 폴더, 파일 가져오기
for dirname, subDirList, fnames in os.walk(dir):
    print('디렉토리 : ', dirname)
    print('하위 폴더 : ', subDirList)
    for subdir in subDirList:
        print('###' , subdir)
    for fname in fnames:
        print(os.path.join(dirname, fname)) #join(dirname, fname) dirname 과 fname을 합쳐서 출력
print('-' * 50)

# os.chdir() : 작업 디렉토리 변경
subdir = 'files'
os.chdir(subdir)
print('변경 된 디렉토리 : ', os.getcwd())
print('-' * 50)

for filename in os.listdir():
    if filename.endswith('.txt'):
        print(filename)