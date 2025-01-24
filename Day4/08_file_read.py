with open('info.txt', 'r',encoding='UTF-8') as file:
    for line in file:
        # 변수를 선언하기
        (name, weight, height) = line.strip().split(', ') # strip으로 공백제거, ' , '을 기준으로 잘라내기
        # 데이터가 사용가능 한 지 검증
        if (not name) or (not weight) or (not height):
            continue
        # 결과 계산
        bmi = int(weight) / (int(height) * int(height)) * 10000
        if bmi >= 25:
            result = '과체중'
        elif bmi >= 18.5:
            result = '정상체중'
        else:
            result = '저체중'
        print(f'이름: {name}, 몸무게: {weight}, 키: {height}, bmi: {result}\n')