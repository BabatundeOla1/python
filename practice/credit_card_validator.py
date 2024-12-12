#Master_card 
#Starts with 5

#Visa_Card 
#starts with 4

#Verve_Card 
#Stsrts with 6



def validate_credit_card(card_number):

	if card_number < "1":
		return "Value Error"

	elif card_number.startswith("4"):
		return "valid"
		
	elif len(card_number) == 16:
		return  "This is a valid Visa card."

	elif card_number.startswith("5"):
		return "valid"

	if len(card_number) == 14:
		return  "This is a valid Visa card."

	else:
		return "Invalid"



print("This is visa card")
validate_credit_card("412341234123")
