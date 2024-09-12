def convert_inches():
    while True:
        inches = float(input("Enter a value in inches: "))

        print("Select the target unit for conversion:")
        print("1. Feet")
        print("2. Meters")
        print("3. Centimeters")

        choice = int(input("Enter your choice (1/2/3): "))

        if choice == 1:
            feet = inches / 12
            print(f"{inches} inches is equal to {feet} feet.")
        elif choice == 2:
            meters = inches / 39.37
            print(f"{inches} inches is equal to {meters} meters.")
        elif choice == 3:
            centimeters = inches * 2.54
            print(f"{inches} inches is equal to {centimeters} centimeters.")
        else:
            print("Invalid choice. Please try again.")

        repeat = input("Do you want to repeat? (Yes/No): ")
        if repeat.lower() != "yes":
            break

convert_inches()
