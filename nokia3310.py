main_menu = """ 	   Main menu 
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
						print("Search book")

					case'2': 
						print("Service NOs")

			case'9':
				print("Speed dial")

			case'10':
				print("Voice tags")

	case'2': 
		print("Message\n")

		Message = input("1: Write message\n2: Inbox\n3: Outbox\n4: Picture message\n5: Templates\n6: Smileys\n7: Message settings\n8: Info service\n9: Voice mailbox number\n10: Service command Operator\n")
				
		match Message: 

			case'1':
				print("Write message")

			case'2': 
				print("Inbox")

			case'3':
				print("Outbox")

			case'4': 
				print("Picture message")

			case'5':
				print("Templates")

			case'6': 
				print("Smileys")

			case'7':
				print("Message setting\n")
				message_settings = input("1: Set 1\n2: Common")

				match message_settings: 

					case'1': 
						print("Set")
						set = input("1: Message centre number\n2: Message sent as\n3: Message validity")
						
						match set:
			
							case'1':
								print("Message centre number")

							case'2': 
								print("Message sent as")

							case'3': 
								print("Message validity")

					case'2': 
						print("Common")
						common = input("1: Delivery reports\n2: Reply via same centre\n3: Character support")
				
						match common:

							case'1': 
								print("Delivery reports")

							case'2': 
								print("Reply via same centre")

							case'3': 
								print("Character suppor")

			case'8': 
				print("Info service")
			
			case'9':
				print("Voice mailbox number")

			case'10': 
				print("Service command operator")

	case'3': 
		print("Chat")


	case'4': 
		print("Call Register\n")

		call_register = input("1: Missed call\n2: Received calls\n3: Dialled numbers\n4: Erase recent calls list\n5: Show call duration\n6: Show call costs\n7: Call cost settings\n8: Prepaid credit") 

		match call_register:
			
			case'1': 
				print("Missed calls")

			case'2': 
				print("Received calls")

			case'3': 
				print("Dialled numbers")

			case'4': 
				print("Erase recent calls list")

			case'5': 
				print("Show call duration\n")

				show_call_duration = input("1: Last call duration\n2: All call's duration\n3: Received call's duration\n4: Dailled call's duration\n5: Clear timers")

				match show_call_duration: 

					case'1': 
						print("Delivery reports")

					case'2': 
						print("Reply via same centre")

					case'3': 
						print("Received call's duration")

					case'4': 
						print("4: Dailled call's duration")

					case'5': 
						print("5: Clear timers")
	
			case'6': 
				print("Show call costs")
				
				show_all_costs = input("1: Last call cost\n2: All call's cost\n3: Clear counters")

				match show_call_costs:

					case'1': 
						print("Last call cost")

					case'2': 
						print("All calls' cost")

					case'3': 
						print("Clear counters")

			case'7': 
				print("Call cost settings")
				
				call_cost_settings = input("1: call cost limit\n2: Show costs in")

				match call_cost_settings: 

					case'1':
						print("call cost limit")

					case'2': 
						print("Show costs in")

			case'8': 
				print("8: Prepaid credit")

	case'5': 
		print("Tones\n")

		tones = input("1: Ringing tones\n2: Ringing volume\n3: Incoming call alert\n4: Composer\n5: Message alert tone\n6: Keypad tones\n7: Warning and game tones\n8: Vibrating alert\n9: Screen saver\n")
	
		match tones:

			case'1': 
				print("Ringing tones")

			case'2':
				print("Ringing volume")

			case'3':
				println("Incoming call alert")

			case'4':
				print("Composer")

			case'5':
				print("Message alert tone")

			case'6':
				print("Keypad tones")

			case'7':
				print("Warning and game tones")

			case'8':
				print("Vibrating alert")
		
			case'9':
				print("Screen saver\n")

	case'6':
		print("Settings\n")

		settings = input("1: Call setting\n2: Phone settings\n3: Security settings\n4: Restore factory settings\n")

		match settings:

			case'1':
				print("Call setting\n")
				
				call_setting = input("1: Automatic redial\n2: Speed dialling\n3: Call waitng options\n4: Own number sending\n5: Phone line in use\n6: Automatic answer\n")
				
				match call_setting:

					case'1':
						print("Automatic redial")

					case'2':
						print("Speed dialling")

					case'3':
						print("Call waitng options")

					case'4':
						print("Own number sending")
					
					case'5':
						print("Phone line in use")

					case'6':
						print("Automatic answer")

			case'2':
				print("Phone setting\n")

				phone_setting = input("1: Language\n2: Cell info display\n3: Welcome note\n4: Network selection\n5: Lights\n6: Confirm SIM service actions\n")
				
				match phone_setting:

					case'1':
						print("Language")

					case'2':
						print("Cell info display")

					case'3':
						print("Welcome note")

					case'4':
						print("Network selection")
					
					case'5':
						print("Lights")

					case'6':
						print("Confirm SIM service actions")

			case'3':
				print("Security setting\n")

				security_setting = input("1: PIN code request\n2: Call barring service\n3: Fixed dialling\n4: Closed user group\n5: Phone security\n6: Change access codes\n")

				match security_setting: 

					case'1':
						print("PIN code request")

					case'2':
						print("Call barring service")

					case'3':
						print("Fixed dialling")

					case'4':
						print("Closed user group")
					
					case'5':
						print("Phone security")

					case'6':
						print("Change access codes")

			case'4':
				print("Restore factory setting")

	case'7': 
		print("Call divert")

	case'8':
		print("Games")

	case'9':
		print("Calculator")

	case'10':
		print("Remainders")

	case'11':
		print("Clock\n")

		clock = input("1: Alarm clock\n2: Clock settings\n3: Date setting\n4: Stopwatch\n5: Countdown timer\n6: Auto update of date and time\n")

		match clock:
			
			case'1': 
				print("Alarm clock")

			case'2':
				print("Clock settings")

			case'3':
				println("Date setting")

			case'4':
				print("Stopwatch")

			case'5':
				print("Countdown timer")

			case'6':
				print("Auto update of date and time")

	case'12':
		print("Profile")

	case'13':
		print("Sim service")		





