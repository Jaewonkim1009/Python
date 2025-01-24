# 랜덤하게 1000명의 키와 몸무게를 파일에 작성 해보자
# 랜덤하게 숫자를 만들기 위해 random 을 가져오자

import random

# 간단한 한글 리스트를 만든다.
hanguls = list("가나다라마바사아자차카타파하")

# 파일을 쓰기 모드로 열기

with open("info.txt", 'w',encoding="UTF-8") as file:
    for i in range(1000):
        # 랜덤한 값으로 변수를 생성합니다.
        name = random.choice(hanguls) + random.choice(hanguls) + random.choice(hanguls)
        weight = random.randint(40,100)
        height = random.randrange(140,200)
        # 텍스트를 작성
        file.write("{}, {}, {}\n".format(name, weight, height))