# 이미지 파일을 읽어서 복사해보기

infile = open('files/123.png', 'rb') # 바이너리, 2진수로 읽기
outfile = open('files/copy_123.png', 'wb') # 바이너리, 2진수로 쓰기

# 이미지 파일은 크기가 크므로, 버퍼를 이용하여 읽는다.
while True:
    copy_buffer = infile.read(1024)
    if copy_buffer:
        outfile.write(copy_buffer)
    else:
        break
infile.close()
outfile.close()
print('이미지가 복사 되었습니다.')