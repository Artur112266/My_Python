print("hello, we are playing 21")

import random as r
import time

start = input("if you want to start first enter (y) otherwise(no): ") == "y" 
name = input("What is your name? ")
point = 0

while True:
	if start:
		user = int(input("please enter the number (1, 2, 3)"))
		comp = r.randint(1, 3)

		if user >= 1 and user <= 3:
			if point >= 21:
				print(name, "you lost")
				break
			else:
				print(name, point, "+", user, "=", point + user)
				point += user
				if point >= 21:
					print('you lost', name)
					break
			if point == 20:
				comp = 1
				print('comp', point, "+", "comp", "=", point + comp)
				print("comp lost")
				break
			elif point == 17 or point == 18 or point == 19:
				comp = 20 - point
				print("comp", point, "+", comp, "=", comp + point)
				point += comp
			
			elif point == 13 or point == 14 or point == 15:
				comp = 16 - point
				print("comp", point, "+", comp, "=", comp + point)
				point += comp

			else:
				time.sleep(1)
				print("comp", point, "+", comp, "=", comp + point)
				point += comp
	else:
		comp = r.randint(1, 3)
		if point == 20:
			comp = 1
			print('comp', point, "+", "comp", "=", point + comp)
			print("comp lost")
			break
		elif point == 17 or point == 18 or point == 19:
			comp = 20 - point
			print("comp", point, "+", comp, "=", comp + point)
			point += comp
		
		elif point == 13 or point == 14 or point == 15:
			comp = 16 - point
			print("comp", point, "+", comp, "=", comp + point)
			point += comp


		else:
			time.sleep(1)
			print("comp", point, "+", comp, "=", comp + point)
			point += comp

				
		if point >= 21:
			print(name, "you lost")
			break
		
		else:
			user = int(input("please enter the number (1, 2, 3)"))
	

			if user >= 1 and user <= 3:
				print(name, point, "+", user, "=", point + user)
				point += user
				if point >= 21:
					print('you lost', name)
					break
			

