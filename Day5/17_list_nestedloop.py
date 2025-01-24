# 중첩 반복문

pairs = []
for i in range(3):
    print(i, "---------")
    for j in range(3):
        print(i,j)
        pairs.append((i , j)) # (i, j)의 튜플
print("-" * 20)
print(pairs)
print('-' * 20)

# 리스트 내포

pairs = [(i,j) for i in range(3) for j in range(3)]
print(pairs)
