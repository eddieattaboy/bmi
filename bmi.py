def bmimet() :
	metresult = (in_kg) / ((in_cm)/100.0)/((in_cm)/100.0)
	print "Your BMI is %.2f" %round(metresult,2)

def bmiimp() :
	outputcm = in_inch*2.54
	outputftcm = in_feet*30.48
	outputkg = in_lb*0.4536
	
	impresult = outputkg / (((outputcm + outputftcm)/100.0)*((outputcm + outputftcm)/100.0))
	print "Your BMI is %.2f" % round(impresult,2)


print "Welcome to the BMI calculator"

while True :
	unit = raw_input("Will you be entering in imperial or metric units?\n>")

	if unit.lower() == 'imperial' :
		while True:
			try:
				in_feet = float(raw_input("Please enter your height, Feet only. You'll enter inches next\n>"))
				break
			except ValueError:
				print "Please enter without units or letters"
		
		while True:
			try:
				in_inch = float(raw_input("Inches now\n>"))
				break
			except ValueError:
				print "Please enter without units or letters"
				
		while True:	
			try:
				in_lb = float(raw_input("Please enter your weight in Pounds\n>"))
				break
			except ValueError:
				print "Please enter without units or letters"
				
		bmiimp()
		break		

	elif unit.lower() == 'metric' :
		while True:
			try:
				in_cm = float(raw_input("Please enter your height in Centimeters\n>"))
				break
			except ValueError:
				print "Please enter without units or letters"
				
		while True:	
			try:
				in_kg = float(raw_input("Please enter your weight in Kilograms\n>"))
				break
			except ValueError:
				print "Please enter without units or letters"
				
		bmimet()
		break
    
	else :
		print 'Please enter "imperial" or "metric"'
