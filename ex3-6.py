number = int(input('정수를 입력하세요:'))

if number>0:
    print('{}는 양수이다.' .format(number))
elif number == 0:
    print('{}는 0이다.' .format(number))
else:
    print('{}는 음수이다.' .format(number))
