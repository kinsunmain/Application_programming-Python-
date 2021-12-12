def func_sum(score):
    total=0
    for i in range(len(score)):
        total += score[i]

    return total

score = [73, 95, 80, 57, 99]

sum = func_sum(score)
avg = sum / 5

print('합계 점수 : {}' .format(sum))
print('평균 점수 : {}' .format(avg))
