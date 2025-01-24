# 파일의 이름을 입력 받아 copy 해보기

infileName = input("입력 파일 이름 : ")
outfileName = input("출력 파일 이름 : ")

print(infileName)
print(outfileName)

# 입력과 출력을 위한 파일을 연다.
infile = open('files/'+ infileName, 'r', encoding='utf8')
outfile = open('files/'+ outfileName, 'w', encoding='utf8')

line = infile.readline()
while line:
    outfile.write(line)
    line = infile.readline()

infile.close()
outfile.close()
