def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def main():
    try:
        temperature = float(input("Enter temperature value: "))
        unit = input("Enter temperature unit (C/F/K): ").upper()
        convert_to = input("Enter unit to convert to (C/F/K): ").upper()

        if unit == "C":
            if convert_to == "F":
                result = celsius_to_fahrenheit(temperature)
            elif convert_to == "K":
                result = celsius_to_kelvin(temperature)
            else:
                print("Invalid conversion.")
        elif unit == "F":
            if convert_to == "C":
                result = fahrenheit_to_celsius(temperature)
            elif convert_to == "K":
                result = celsius_to_kelvin(fahrenheit_to_celsius(temperature))
            else:
                print("Invalid conversion.")
        elif unit == "K":
            if convert_to == "C":
                result = temperature - 273.15
            elif convert_to == "F":
                result = celsius_to_fahrenheit(temperature - 273.15)
            else:
                print("Invalid conversion.")
        else:
            print("Invalid unit.")

        print(f"{temperature} {unit} is equal to {result} {convert_to}")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")
		
	else:
		print("Conversion successful.")

    finally:
        print("Temperature conversion complete.")

	

if __name__ == "__main__":
    main()
