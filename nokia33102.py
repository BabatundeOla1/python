def nokia():
	main_menu() == """ 	   Main menu 
	-------------------------
	1 -> Phone book
	2 -> Message
	3 -> Chat
	4 -> Call Register
	5 -> Tones
	6 -> Settings 
	7 -> Call Diverting 
	8 -> Games
	9 -> Calculator
	10 -> Reminders
	11 -> Clock
	12 -> Profile 
	13 -> SIM Service
	-------------------------
		Enter a number:
	"""

menu = input(main_menu)

match menu: 

	case'1': 
		print("Phone Book\n")

		phone_book = input("1: Search\n2: Service No\n3: Add name\n4: Erase\n5: Edit\n6: Assign tone\n7: Send b'card\n8: Options\n9: Speed dial\n10: Voice tags\n")

		match phone_book:

			case'1':
				print("Search")

			case'2': 
				print("Service")

			case'3':
				print("Add name")

			case'4': 
				print("Erase")

			case'5':
				print("Edit")

			case'6': 
				print("Assign tone")

			case'7':
				print("Send b'card")

			case'8': 
				print("Options")
				options = input("1: Search book\n2: Service NOs")

				match options: 

					case'1': 
						print("Types of views")

					case'2': 
						print("Memory status")

				
			case'9':
				print("Speed dial")

			case'10':
				print("Voice tags")

			
	case'3': 
		print("Chat")


	
