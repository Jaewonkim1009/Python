# 문자열 변환

#['apple', 'banana', 'cherry'] 가 들어 있는 리스트를 모두 대문자로 바꾸어 
# capitalized 리스트로 작성하는 코드를 작성하자

words = ["apple", 'banana', 'cherry']
capitalized = []

for word in words:
    capitalized.append(word.upper())
print(capitalized)


# 리스트 내포

capitalized = [word.upper() for word in words]
print(capitalized)