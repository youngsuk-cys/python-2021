

str1 = "python is very easy."

strArr1 = str1.split(' ')

type(strArr1)


str2 = "Life is too short \n you need python"

print(str2)


head = 'Python '
tail = ' is fun!'

head + tail

tail * 2

for  x in range (0 , 11) :
    print('*' * x )

len(head + tail)

content = head + tail 

content[0]

content[ len(content) - 1]

content[-1]


content[0:6]

content[6:]

content[3:6]

# %d : 숫자 %s : 문자
"i eat %d apples." % 3

"i eat %s %s EEEe" % ('44444444444' , '55555555')

'i have %s apples .' % 2

'i have %s apples' % '2'

"Error is %d%%." % 98

'%20s' % 'hi'

'%-20s cys' % 'DD'

'%3.4f' % 2.123456

'{0} {1} ㅇㅇㅇㅇㅇ'.format('this' , 'is')

'{a} {b} 000'.format(a=10 , b='2222')

# 왼쪽 정렬
'{0:<20}'.format('a')

# 오른쪽 정렬
'{0:>20} aaaaa'.format('b')

# < : 완쪽 정렬 , > : 오른쪽 정렬 , ^ : 가운데
'{0:=>10}'.format('hi')

'{0:!<10}'.format('hi')

'{0:-^31}'.format('|')

'{0:0.4f}'.format(1.123456)

# 뭔가 채운다는 의미가 있는듯....
'{0: ... }' 

'{0:10.4f}'.format(1.33334)

'{{ aa|bb }}'.format()




# f 가 변수가 아니라 . format 예약어 인가 부다
name = '채영석'
f'{name} 입니다.'
'{name} 입니다.'.format(name = 'cys')


d = {'a' : 123 , 'b' : 'this is b'}

f'{d["a"]} 는 {d["b"]} 일가요 ?' 

