year = int(input('당신의 태어난 연도를 입력하세요: '))

age = 2020 - year +1


if 20<=age<=29:
    print('나이는 {}이고 대학생입니다.' .format(age))
elif 17<=age<=19:
    print('나이는 {}이고 고등학생입니다.' .format(age))
elif 14<=age<=16:
    print('나이는 {}이고 중학생입니다.' .format(age))
elif 8<=age<=13:
    print('나이는 {}이고 초등학생입니다.' .format(age))
else:
    print('나이는 {}이고 학생이 아닙니다.' .format(age))
