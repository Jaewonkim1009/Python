# 리스트에서 짝수는 그대로, 홀수는 -1로 변환

list = []
for i in range(1, 11):
    if i % 2 == 1:
        list.append(-1)
    else:
        list.append(i)

print(list)


list = [i for i in range(1, 11) if i % 2 == 1]
print(list)

# if 구문에서 else가 있는 경우

list = [i if i % 2 == 0 else -1 for i in range(1, 11)]
print(list)