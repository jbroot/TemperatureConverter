#!/usr/bin/python

#Script approximating Celsius to Fahrenheit conversion and vice versa

def celsiusToFahrenheit(cTemp):
	return (cTemp*9/5)+32

def fahrenheitToCelsius(fTemp):
	return (fTemp-32)*(5.0/9)

print("Welcome to the Temperature Conversion Program")
while(1):
	choice = raw_input("""Main Menu
1. Fahrenheit to Celsius
2. Celsius to Fahrenheit
3. Exit program

Please enter 1, 2 or 3: """)
	if choice == "3":
		break;
	elif choice == "1":
		#Fahrenheit to celsius
		try:
			fTemp= float(raw_input("Please enter degrees Fahrenheit: "))
			print("%.1f degrees Fahrenheit equals %.1f degrees Celsius" % (fTemp, fahrenheitToCelsius(fTemp)))
		except:
			print("Invalid entry.\n")
	elif choice == "2":
		#celsius to fahrenheit
		try:
			cTemp= float(raw_input("Please enter degrees Celsius: "))
			print("%.1f degrees Celsius equals %.1f degrees Fahrenheit" % (cTemp, celsiusToFahrenheit(cTemp)))
		except:
			print("Invalid entry.\n")
	else:
		print('That input is not valid')
