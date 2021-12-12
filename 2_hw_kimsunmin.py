#2_hw_kimsunmin

number = int(input('정수를 입력하세요: '))

sum = 0

q = number//1000
w = (number//100) %10 
e = (number//10) %10 
r = number%10

sum = q+w+e+r

print(q)
print(w)
print(e)
print(r)

print('자리수 합은 {}이다.'.format(sum))
