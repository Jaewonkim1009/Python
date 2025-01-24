my_list = [10, 20, 30]

def modify_list():
    print(my_list[1])
    my_list.append(40)
    print("함수 내부 my_list : ", my_list)

modify_list() 
print("함수 외부 my_list : ", my_list)




