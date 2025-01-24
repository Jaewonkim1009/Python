# [(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)] 로 구성 된 리스트를 생성해보자.

list = []

for i in range(5):
    for j in range(5):
        if i % 2 == 0 and j % 2 == 1:
            list.append((i, j))
print(list)


list = [(i, j) for i in range(5) for j in range(5) if i % 2 == 0 and j % 2 == 1]
print(list)

