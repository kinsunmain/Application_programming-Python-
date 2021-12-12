id = str(input('아이디를 입력하세요: '))

if id=='lovePython!':

    
    pw = str(input('비밀번호를 입력하세요: '))


    if id == 'lovePython!' and pw == 'p12345':
        print('lovePython!님 환영합니다~!!')

    elif id == 'lovePython!' and pw != 'p12345':
        print('비밀번호가 틀립니다.')


else :
    print('아이디를 찾을 수 없습니다.')
