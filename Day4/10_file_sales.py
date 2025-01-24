infile = input('입력 파일 이름: ')
outfile = input('출력 파일 이름: ')

inf = open(infile, 'r')
outf = open(outfile, 'w', encoding='utf8')

sum = 0
count = 0

# 입력 파일에서 한 줄씩 읽어서 합계를 계산
line = inf.readline() #readline() 한 줄씩 읽기
while line != "":
    sale = int(line) 
    sum += sale
    count += 1
    line = inf.readline()

# 총 매출액과 일 평균 매출액을 출력파일에 기록
outf.write('총매출 = ' + str(sum) + '\n')  
outf.write('일 평균매출 = ' + str(sum / count))

inf.close()
outf.close()





