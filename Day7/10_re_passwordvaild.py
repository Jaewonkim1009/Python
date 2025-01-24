import re

password = input('패스워드를 입력해주세요 : ')
flag = 0
while True:
    if len(password) < 8:
        flag = -1
        break
    # 해당 조건이 아닐시 break
    elif not re.search('[a-z]', password):
        flag = -1
        break
    elif not re.search('[A-Z]', password):
        flag = -1
        break
    elif not re.search('[0-9]', password):
        flag = -1
        break
    elif not re.search('[_@$]', password):
        flag = -1
        break
    else:
        print('유효한 패스워드')
        break
if flag == -1:
    print('잘못 된 패스워드 입니다.')

if not re.search('^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%?&])[A-Za-z\d@$!%?&]{8,24}$', password):
    print('유효하지 않은 패스워드 입니다.')
else:
    print('유효한 패스워드 입니다.')