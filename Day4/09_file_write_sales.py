import random

with open('sales.txt', 'w') as file:
    money = [1000000,10000000,100000000,500000,5000000]
    for i in range(10):
        file.write(str(random.choice(money)) + '\n')
