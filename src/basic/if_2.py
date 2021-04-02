num = 0
sum = 0

while num <= 10 :
    if num % 2 == 0:
        sum += num
        print ( num , sum )
    
    num += 1

print('sum' , sum)

sum = 0 
inputNum = 1

while True :
    inputNum = int(input('값 입력해'))

    if inputNum > 0 :             
        sum += inputNum   
    else :
        break

print('sum' , sum) 







