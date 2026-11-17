# NOKIA 5510 MENU PROGRAM

while True:

    main_menu = """
List of menu functions

Press 1 for Phone book
Press 2 for Message
Press 3 for Chat
Press 4 for Call register
Press 5 for Tone
Press 6 for Setting
Press 7 for Call divert
Press 8 for Games
Press 9 for Calculator
Press 10 for Reminder
Press 11 for Clock
Press 12 for Profiles
Press 13 for SIM services
Press 0 to Exit

"""

    print(main_menu)
    main_menu_list = int(input("Main menu: "))

    match main_menu_list:

        case 1:
            print("Phone book")

            phone_book = """
Press 1 to Search
Press 2 to Service Nos
Press 3 to Add name
Press 4 to Remove
Press 5 to Edit
Press 6 to Assign tone
Press 7 to Send business card
Press 8 to Option
Press 9 to Speed dials
Press 10 to Voice tags
"""

            print(phone_book)
            phone_book_list = int(input("Phone book: "))

            match phone_book_list:

                case 1:
                    print("Search")

                case 2:
                    print("Service Nos")

                case 3:
                    print("Add name")

                case 4:
                    print("Remove")

                case 5:
                    print("Edit")

                case 6:
                    print("Assign tone")

                case 7:
                    print("Send business card")

                case 8:
                    print("Option")

                    option = """
Press 1: Type of view
Press 2: Memory status
"""

                    print(option)
                    option_list = int(input("Option: "))

                    match option_list:

                        case 1:
                            print("Type of view")

                        case 2:
                            print("Memory status")

                        case _:
                            print("Invalid selection")

                case 9:
                    print("Speed dials")

                case 10:
                    print("Voice tags")

                case _:
                    print("Invalid selection")


        case 2:
            print("Message")

            message = """
Press 1: Write message
Press 2: Inbox
Press 3: Outbox
Press 4: Picture message
Press 5: Template
Press 6: Smileys
Press 7: Message setting
Press 8: Info service
Press 9: Voice mailbox number
Press 10: Service command editor
"""

            print(message)
            message_list = int(input("Message: "))

            match message_list:

                case 1:
                    print("Write message")

                case 2:
                    print("Inbox")

                case 3:
                    print("Outbox")

                case 4:
                    print("Picture message")

                case 5:
                    print("Template")

                case 6:
                    print("Smileys")

                case 7:
                    print("Message setting")

                    message_setting = """
Press 1: Set
Press 2: Command
"""

                    print(message_setting)
                    message_setting_list = int(input("Message setting: "))

                    match message_setting_list:

                        case 1:
                            print("Set")

                        case 2:
                            print("Command")

                        case _:
                            print("Invalid selection")

                case 8:
                    print("Info service")

                case 9:
                    print("Voice mailbox number")

                case 10:
                    print("Service command editor")

                case _:
                    print("Invalid input")


        case 3:
            print("Chat Menu")


        case 4:
            print("Call Register")

            call_register = """
Press 1: Missed call
Press 2: Received call
Press 3: Dialled number
Press 4: Clear recent call lists
Press 5: Show call duration
Press 6: Show call costs
Press 7: Call cost settings
Press 8: Prepaid credit
"""

            print(call_register)
            call_register_list = int(input("Call register: "))

            match call_register_list:

                case 1:
                    print("Missed call")

                case 2:
                    print("Received call")

                case 3:
                    print("Dialled number")

                case 4:
                    print("Clear recent call lists")

                case 5:
                    print("Show call duration")

                    show_call_duration = """
Press 1: Last call duration
Press 2: All calls' duration
Press 3: Received calls
Press 4: Dialled calls duration
Press 5: Clear times
"""

                    print(show_call_duration)
                    call_duration_list = int(input("Show call duration: "))

                    match call_duration_list:

                        case 1:
                            print("Last call duration")

                        case 2:
                            print("All calls' duration")

                        case 3:
                            print("Received calls")

                        case 4:
                            print("Dialled calls duration")

                        case 5:
                            print("Clear times")

                        case _:
                            print("Invalid selection")

                case 6:
                    print("Show call costs")

                    show_call_cost = """
Press 1: Last cost
Press 2: All calls' cost
Press 3: Clear counter
"""

                    print(show_call_cost)
                    show_call_cost_list = int(input("Show call cost: "))

                    match show_call_cost_list:

                        case 1:
                            print("Last cost")

                        case 2:
                            print("All calls' cost")

                        case 3:
                            print("Clear counter")

                        case _:
                            print("Invalid selection")

                case 7:
                    print("Call cost settings")

                    call_cost_settings = """
Press 1: Call cost limit
Press 2: Show cost in
"""

                    print(call_cost_settings)
                    call_cost_setting_list = int(input("Call cost settings: "))

                    match call_cost_setting_list:

                        case 1:
                            print("Call cost limit")

                        case 2:
                            print("Show cost in")

                        case _:
                            print("Invalid selection")

                case 8:
                    print("Prepaid credit")

                case _:
                    print("Invalid selection")


        case 5:
            print("Tone Menu")

            tone_menu = """
Press 1: Ringing tone
Press 2: Ringing volume
Press 3: Incoming call alert
Press 4: Composer
Press 5: Message alert tone
Press 6: Warning and game tone
Press 7: Vibrating alert
Press 8: Screen Saver
"""

            print(tone_menu)
            tone_menu_list = int(input("Tone menu: "))

            match tone_menu_list:

                case 1:
                    print("Ringing tone")

                case 2:
                    print("Ringing volume")

                case 3:
                    print("Incoming call alert")

                case 4:
                    print("Composer")

                case 5:
                    print("Message alert tone")

                case 6:
                    print("Warning and game tone")

                case 7:
                    print("Vibrating alert")

                case 8:
                    print("Screen Saver")

                case _:
                    print("Invalid selection")


        case 6:
            print("Setting Menu")

            setting_menu = """
Press 1: Call setting
Press 2: Phone setting
Press 3: Security setting
Press 4: Restore factory setting
"""

            print(setting_menu)
            setting_menu_list = int(input("Setting menu: "))

            match setting_menu_list:

                case 1:
                    print("Call setting")

                    call_setting_menu = """
Press 1: Automatic redial
Press 2: Speed dialling
Press 3: Call waiting
Press 4: Own number sending
Press 5: Phone line in use
Press 6: Automatic answer
"""

                    print(call_setting_menu)
                    call_setting_menu_list = int(input("Call setting menu: "))

                    match call_setting_menu_list:

                        case 1:
                            print("Automatic redial")

                        case 2:
                            print("Speed dialling")

                        case 3:
                            print("Call waiting")

                        case 4:
                            print("Own number sending")

                        case 5:
                            print("Phone line in use")

                        case 6:
                            print("Automatic answer")

                        case _:
                            print("Invalid selection")


                case 2:
                    print("Phone setting")

                    phone_setting_menu = """
Press 1: Language
Press 2: Call info display
Press 3: Welcome note
Press 4: Network selection
Press 5: Lights
Press 6: Confirm SIM service action
"""

                    print(phone_setting_menu)
                    phone_setting_menu_list = int(input("Phone setting: "))

                    match phone_setting_menu_list:

                        case 1:
                            print("Language")

                        case 2:
                            print("Call info display")

                        case 3:
                            print("Welcome note")

                        case 4:
                            print("Network selection")

                        case 5:
                            print("Lights")

                        case 6:
                            print("Confirm SIM service action")

                        case _:
                            print("Invalid selection")


                case 3:
                    print("Security setting")

                    security_setting_menu = """
Press 1: Phone security
Press 2: PIN code
Press 3: Call barring service
Press 4: Fixed dialling
Press 5: Closed user group
Press 6: Change access code
"""

                    print(security_setting_menu)
                    security_setting_menu_list = int(input("Security setting: "))

                    match security_setting_menu_list:

                        case 1:
                            print("Phone security")

                        case 2:
                            print("PIN code")

                        case 3:
                            print("Call barring service")

                        case 4:
                            print("Fixed dialling")

                        case 5:
                            print("Closed user group")

                        case 6:
                            print("Change access code")

                        case _:
                            print("Invalid selection")


                case 4:
                    print("Restore factory setting")

                case _:
                    print("Invalid selection")


        case 7:
            print("Call divert Menu")


        case 8:
            print("Games Menu")


        case 9:
            print("Calculator Menu")


        case 10:
            print("Reminder Menu")


        case 11:
            print("Clock Menu")

            clock_menu = """
Press 1: Alarm clock
Press 2: Clock setting
Press 3: Date setting
Press 4: Stopwatch
Press 5: Countdown
Press 6: Auto update of date and time
"""

            print(clock_menu)
            clock_menu_list = int(input("Clock menu: "))

            match clock_menu_list:

                case 1:
                    print("Alarm clock")

                case 2:
                    print("Clock setting")

                case 3:
                    print("Date setting")

                case 4:
                    print("Stopwatch")

                case 5:
                    print("Countdown")

                case 6:
                    print("Auto update of date and time")

                case _:
                    print("Invalid selection")


        case 12:
            print("Profile Menu")


        case 13:
            print("SIM service Menu")


        case 0:
            print("Thank you for using Nokia 5510!")
            break


        case _:
            print("Invalid selection. Please try again.")

