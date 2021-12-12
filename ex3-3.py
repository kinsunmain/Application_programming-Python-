number = int(input('정수를 입력하세요: '))
if number %2 ==0 and number %3 ==0 :
    print('{}는 2와 3으로 나누어 떨어집니다.' .format(number))

else:
    print('{}는 2와 3으로 나누어 떨어지지 않습니다.' .format(number))
