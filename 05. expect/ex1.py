# f = open("없는 파일", 'r')

# print(4 / 0)

# a = [1, 2, 3]
# print(a[4])

# try:
#     4/0
# except ZeroDivisionError as e:
#     print(e)

a = [1, 2, 3]
try:
    a[4]
except IndexError as e:
    print(e)