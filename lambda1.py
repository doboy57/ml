import os

clear = lambda: os.system("cls")
clear()

remainder = lambda num: num % 2
print(remainder(5))
product = lambda x,y: x * y
print(product(2,3))

def testfunc(num):
    print(num)
    return lambda x: x * num
result10 = testfunc(10)
result10 = lambda x: x * 10
result100 = testfunc(100)
result100 = lambda x: x * 100
print(result10(9))
print(result100(9))

def myfunc(n):
    return lambda x: x * n
mydoubler = myfunc(2)
mytrippler = myfunc(3)
print(mydoubler(3))
print(mytrippler(11))
number_list = [2,6,7,8,10,11,14,4,2,5,6]
filtered_list = list(filter(lambda num:(num>7),number_list))
print(filtered_list)
mapped_list = list(map(lambda num: num %2, number_list))
print(mapped_list)
def addition(n):
    return n + n
numbers = [1,2,3,4]
result = map(addition,numbers)
result2 = map(lambda n: n +n, numbers)
print(list(result))
print(list(result2))
