# lisst = [12, 35, 1, 6, 65,78, 98, 100, -100]
# x = lisst[0]
# for i in lisst:
# 	if i > x:
# 		x = i
# print(x)


# lisst = [12, 35, 1, 6, 65,78, 98, 100, -100]
# x = lisst[0]
# for i in lisst:
# 	if i < x:
# 		x = i
# print(x)

# lisst = [12, 35, 1, 6, 65,78, 98, 100, 100]
# x = 0
# for i in lisst:
# 	x += i
# print(x)

# lisst = [12, 353, 1, 16, 65,78, 198, 100, 100, 10, -675, 8, 14]
# x = 0
# for i in lisst:
# 	x += i
# 	print(x)
# x /= len(lisst)
# print(x)

# lisst = [12, 33, 1, 16, 65,78, 18, 10, 10, 8, 14]
# x = 1
# for i in lisst:
# 	x *= i
# print(x)

# list1 = [12, 33, 1, 16, 65,78, 18, 10, 8, 14]
# list2 = [353, 0, 78, 198, 100, 100, -675, 8, 14]
# for i in list1:
# 	if i in list2:
# 		print('ok')
# 		print(i)
# 		break

# list1 = [12, 33, 1, 16, 65,78, 18, 10, 8, 14]
# list2 = [353, 12, 78, 198, 100, 100, -675, 8, 14]
# for i in list1:
# 	for j in list2:
# 		if i % j == 0:
# 			print (i)


# blot
import random

Armen = []
Artur = []
mast = ["sirt ", "qyap ", "xach ", "ghar "]
qar = ['9', '10', 'J', 'Q', 'K', 'T']
kalod = []
for i in mast:
	for j in qar:
		result = i +j
		kalod.append(result)
random.shuffle(kalod)
 
for i in range(5):
	x = kalod.pop()
	Armen.append(x)
	y = kalod.pop()
	Artur.append(y)
trump = kalod.pop()
Armen.sort()
Artur.sort()

print('              Armen',Armen)
print('')
print('              Artur',Artur)
print('')
print('              trump',trump)
print('')

choice = input('You want to take this trump? ')
print('')

if choice:
	Armen.append(trump)
	for i in range(2):
		x = kalod.pop()
		Armen.append(x)
	for i in range(3):
		y  = kalod.pop()
		Artur.append(y)	
Armen.sort()
Artur.sort()


print('Armen',Armen)
print('')
print('Artur',Artur)
print('')	









