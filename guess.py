import random

r = random.randint(1, 100)
count = 0
while True:
	count += 1 #count = count + 1
	x = input('請輸入數字：')
	x = int(x)
	if x == r:
		print('恭喜答對！')
		print('這是你猜的第', count, '次')
		break
	elif x > r: 
		print('比答案大')
	elif x < r:
		print('比答案小')
	print('這是你猜的第', count, '次')
