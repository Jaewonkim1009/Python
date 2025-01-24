import pickle

# pickle.dump() = 파일 쓰기
# pickle.load() = 파일 읽기

gameOption = {
        "Sound" : 8,
        "VideoQuality" : 'HIGH',
        'Money' : 1000000,
        'Weaponlist' : ['gun', 'missile', 'knife']
}

# 딕셔너리에 저장된 데이터를 파일로 쓰기를 할때는 pickle.dump()를 사용한다.
file = open('files/save.pickle', 'wb')   # 2진 파일 쓰기 (객체이므로)
pickle.dump(gameOption, file)            # 딕셔너리를 피클 파일에 저장
file.close()                             # 파일 닫기

# 객체 파일이 저장된 경우 pickle 라이브러리를 이용하여 읽어 올 수 있다.
with open('files/save.pickle', 'rb') as f:
    object = pickle.load(f)
    print(type(object))
    print(object)
    for key, value in object.items():
        print(f'{key} : {value}')

