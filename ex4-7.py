number = int(input('정수를 입력하세요: '))

total=0
i=1

while i<=number:
    total +=i
    i += 1
print('1부터 {}까지의 합은 {}이다.' .format(number,total))
