
a = 1234 * 4
b = 13456 / 2

if a > b : 
    print('a' , a)
else : 
    print('b' , b)

c = 15 *5
d = 15 ** 5

if a < b : 
    print ('b')
elif a < c :
    print ('c')
elif a < d :
    print ('d')

if c == 15 * 5 :
    print ('c 는 15 * 5와 값이 동일합니다.')

while True : 
    num = int (input('입력해'))    
    if num > 10 :
        print ('10보다 크니 중지')
        break
    else :
        print('10 보다 작네')