y = 20
def update_global():
    global y
    y = 50
    print("함수 내부 y:",y)

update_global()
print("함수 외부 y :", y)