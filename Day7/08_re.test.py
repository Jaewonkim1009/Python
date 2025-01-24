import re
# 이메일 형식에 맞는 것을 찾아오기

# 영문자로 시작, 대소문자 구분 없음
# _ . + @ + 영문자, 숫자, - . 사용하기 마지막은 영문자로 끝나야 한다.

emails = ['ab_cdsg..e&abc.com', 'abc.hr+ti@abc.com', 'SDF_jeyjn234@abc.com', '4643qwe#abc.com', 'zxc&asd.com', '43523@asc.com']

# /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.\[a-zA-Z]{2,}$/

for email in emails:
    # ^시작 A-Z, a-z , 0-9 , . , _ @ A-Z, a-z , 0-9 , . , .A-Z , a-z $까지
    if re.search('^[A-Za-z0-9._]+@[A-Za-z0-9.-]+.[A-Za-z]$',email):
        print(email)

print('-'* 50)

for email in emails:
    if re.search('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email):
        print(email)

# abc@abc.com
# abc+lalala@abc.com  
# 위와 동일한 이메일 주소를 가지고 있음, lalala를 별칭으로 기능할 수 있다.

