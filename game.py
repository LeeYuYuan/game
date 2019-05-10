import random
start = input('請輸入數字範圍開始值:')
end = input('請輸入數字範圍結束值:')
start = int(start)
end = int(end)
rn = random.randint(start, end)
count = 0
while True:
	count = count + 1
	print('這是您猜得第', count, '次')
	number = input('猜個號碼吧:')
	number = int(number)
	if number == rn:
		print('恭喜你猜對了')
		break
	elif number > rn and number < end:
		print('太大了')
	elif number < rn and number > start:
		print('太小了')
	elif number < start:
		print('只能猜範圍內的數字')
	elif number > end:
		print('只能猜範圍內的數字')