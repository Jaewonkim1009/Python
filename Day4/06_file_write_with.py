# with 구분으로 파일을 열면 수행 후 자동으로 close() 된다
with open("basic.txt",'r') as file:
    # 파일을 읽고 출력
    contents = file.read()
print(contents)

with open("test.txt", 'w') as file:
    file.write("Test")

with open('test.txt', 'r') as file:
    r = file.read()
print(r)