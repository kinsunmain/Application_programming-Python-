import random



while(1):
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    
    num3 = num1 + num2
    
    print(num1," + ",num2,"= ?")
    ans = input()

    if(ans == '종료'):
        break;

    elif( num3 == ans):
        print('정답입니다')
    
    elif(num3 != ans):
        print('오답입니다')
    
    

