# 특정 문자로 시작하는 단어만 추출

words = ['apple', 'banana', 'cherry', 'apricot', 'blueberry']

filtered = []

for word in words:
    if word.startswith('a'):
        filtered.append(word)
print(filtered)


filtered = [word for word in words if word.startswith('a')]
print(filtered)