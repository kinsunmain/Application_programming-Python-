num1 = int(input('첫번째 정수를 입력하세요: '))
num2 = int(input('두번째 정수를 입력하세요: '))
num3 = int(input('세번째 정수를 입력하세요: '))

max = 0

if (num1>num2 and num1> num3):
    max = num1
elif (num2>num1 and num2>num3):
    max = num2
else:
    max = num3

print('가장 큰 수는 {}입니다.' .format(max))
