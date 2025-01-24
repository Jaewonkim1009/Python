# 가장 추웠던 날의 기온은?

import csv

file = open('weather.csv', encoding='utf8')
data = csv.reader(file)
header = next(data)
min_temp = 100

for row in data:
    temp = float(row[3])
    if temp < min_temp:
        min_temp = temp
print(f'가장 추운 날의 기온은 : {min_temp} 도 입니다.') 

# min_temp = []

# for row in data:
#     min_temp.append(float(row[3]))
    
# print(f'가장 추운 날의 기온은 : {min(min_temp)} 도 입니다.') 
file.close()