def end():
    # Terminates the execution.

    exit(0)


def choice_error():
    # Print an error message in case the user selects a wrong action.

    print("Choice does not exist")


def menu():
    # Print a menu with all the functionality.

    # Returns:
        # The choice of the user.

    print("=" * 30 + "\n\t\t\tMENU\n" + "=" * 30)
    descriptions = ["Scan for Devices",
                    "Select and take over Discovered Devices",
                    "View Monitored Devices",
                    "Take Screen Shot",
                    "Exfiltrate File",
                    "Upload Payload",
                    "Review Stolen Data",
                    "Exit"]
    for num, func in enumerate(descriptions):
        print("[-->", num, func)

    choice = input(">>> ")
    return choice


menu()
