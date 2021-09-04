print("Please turn on your computer.")
boot = input("Did your computer boot up? (Y/N): ").lower()
if boot == "y":
    print("Proceed to login.")
else:
    plugged_in = input("Is your computer plugged in? (Y/N): ").lower()
    if plugged_in == "y":
        print("Sorry, your computer appears to be broken.")
    else:
        print("Please plug in your computer.")
        fixed = input("Did this fix the problem? (Y/N): ").lower()
        if fixed == "y":
            print("Proceed to login.")
        else:
            print("Sorry, your computer appears to be broken.")

