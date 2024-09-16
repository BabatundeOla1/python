daily_successful_delivery = int(input("Enter number of successful delivery for the day: "))

BASE_PAY = 5000
	
def calculate_wages(successful_delivery):
		
	if successful_delivery <= 50:
		amountPerParcel = 160
		
	elif 50 < successful_delivery <= 59:
		amountPerParcel = 200

	elif 60 < successful_delivery <= 69:	
		amountPerParcel = 250
		
	elif successful_delivery >= 70:
		amountPerParcel = 500
		
	else:
		return "invalid number of deliveries"


	wages = successful_delivery * amountPerParcel + BASE_PAY
	
	return wages

print(calculate_wages(daily_successful_delivery))
