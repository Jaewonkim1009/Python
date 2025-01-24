# 주소록 만들기
address_book = {}

# 메인 메뉴
def display_menu():
    print('-' * 20)
    print('1. 연락처 추가')
    print('2. 연락처 삭제')
    print('3. 연락처 검색')
    print('4. 연락처 목록')
    print('5. 연락처 수정')
    print('6. 종료')
    
    print('-' * 20)
    menu = input('메뉴 항목을 선택 하세요 : ')
    return int(menu)


# 연락처 추가 함수
def get_contact():
    name = input('이름 : ')
    tel = input('전화번호 : ')
    return name, tel

# 연락처 삭제 함수
def get_name():
    name = input('이름 : ')
    return name

# 연락처 수정 함수
def get_modify(address_book):
    name = input('수정 할 사람의 이름을 입력해주세요 : ')
    if name in address_book:
        tel = input(f'{name}님의 새로운 전화번호를 입력 해주세요 : ')
        return name, tel
    else:
        return name, None


def main():
    address_book = {}
    try:
        while True:
            menu = display_menu()
            if menu == 1:
                print('추가하기')
                # name = get_contact() : 변수를 하나만 입력 시 튜플(name,tel)로 리턴 됨
                name, tel = get_contact()  # 이름과 전화번호 입력 받기
                address_book[name] = tel # 입력 받은 값 딕셔너리에 저장
                print(f'{name}님이 추가 되었습니다.')

            elif menu == 2:
                print('삭제하기')
                name = get_name()
                if name in address_book: # 딕셔너리 안에 저장 된 이름이 있을 경우
                    del address_book[name] # 딕셔너리 안의 해당 값 삭제
                    # address_book.pop(name)
                    print(f'{name}님이 삭제 되었습니다.')
                else:
                    print(f'{name}님은 등록 되어 있지 않습니다.')

            elif menu == 3:
                print('검색하기')
                name = get_name() # 검색 할 이름 입력 받기
                if name in address_book: # 딕셔너리 안에 저장 된 이름이 있을 경우
                    print(f'{name}님의 연락처는 {address_book[name]} 입니다.') # 딕셔너리 안의 검색 한 이름과 딕셔너리 밸류값 출력
                else:
                    print(f'{name}님은 등록 되어 있지 않습니다.')

            elif menu == 4:
                print('목록 조회하기')
                if address_book:
                    for name, tel in address_book.items(): # 딕셔너리 모든값을 name, tel로 조회
                        print(f'{name}님의 연락처는 {tel} 입니다.') # name , tel 출력
                else:
                    print('저장 된 연락처가 없습니다.')

            elif menu == 5:
                print('연락처 수정하기')
                name, tel = get_modify(address_book) # address_book에서 name, tel 받아오기
                if name and tel:   # address_book 안에 name과 tel 확인
                    address_book[name] = tel 
                    print(f'{name}님의 연락처가 수정 되었습니다.')
                else:
                    print(f'{name}님은 등록 되어 있지 않습니다.')

            elif menu == 6:
                print('종료 합니다.')
                break  # while 종료
            else:
                raise ValueError # 메시지 출력 후 메인메뉴로 돌아감                            
    except ValueError as err:
        print('잘못 입력 하였습니다. 다시 선택해 주세요.')
        print(err)
        main()


main()