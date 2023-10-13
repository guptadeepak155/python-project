Height=float(input("Enter your height in centimeter:"))
Weight=float(input("Enter your Weight in Kilogram:"))
Height=Height/100
BMI=Weight/(Height*Height)
print("your Body Mass Index(BMI) is:%d",BMI)
if(BMI>0):
	if(BMI<=16):
		print("\nyou are severely underweight")
		print("you must gain your wieght to look fit")
	elif(BMI<=18.5):
		print("\nyou are underweight")
		print("we suggest you to gain your weight ")
	elif(BMI<=25):
		print(" \ncongratulations!! you are Healthy")
	elif(BMI<=30):
		print("\nyou are overweight")
		print("we advice you to lose your weight \nthen you will look fit")
	else: print("you are severely overweight")
else:("\n enter valid detail")
