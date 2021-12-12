name = []
score = []
while True:
    
    a = input("이름을 입력하시오: ")
    b = input("점수를 입력하시오: ")
    if a == b== '':
        break;
    else:
        name.append(a)
        score.append(b)
    
info = dict(zip(name, score))
print(info)
