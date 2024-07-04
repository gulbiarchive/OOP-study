# class MyError(Exception):
# 	pass
	
# def say_nick(nick):
# 	if nick == '악마':
# 		raise MyError()
# 	print(nick)
	
# say_nick('천사')
# say_nick('악마')

# class MyError(Exception):
# 	pass
	
# def say_nick(nick):
# 	if nick == '악마':
# 		raise MyError()
# 	print(nick)
	
# try:
#     say_nick('천사')
#     say_nick('악마')
# except MyError:
#     print('허용되지 않는 별명')

class MyError(Exception):
	def __str__(self):
		return '허용되지 않는 별명'
	
def say_nick(nick):
	if nick == '악마':
		raise MyError()
	print(nick)
	
try:
    say_nick('천사')
    say_nick('악마')
except MyError as e:
    print(e)