score = int(input('학생의 점수를 입력하세요: '))
if score>= 90:
    grade = 'A'
else if score>= 80:
    grade = 'B'
else if score>= 70:
    grade = 'C'
else if score>= 60:
    grade = 'D'
else:
    grade = 'F'

print("학점은 {}이다." .format(grade));
