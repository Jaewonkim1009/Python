# 구구단 만들기

for i in range(2,10):
    print(f"---- {i} 단 ----")
    for j in range(1,10):
        print(f" {i} X {j} = {i * j:2}", end=" |")
    print()