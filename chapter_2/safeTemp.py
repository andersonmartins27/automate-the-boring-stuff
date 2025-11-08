scale = input("Enter C or F to indicate Celsius or Fahrenheit: ").upper()
degrees = float(input("Enter the number of degrees: "))

if scale == "C":
    if 16 <= degrees <= 38:
        print("Safe")
    else:
        print("Dangerous")
elif scale == "F":
    if 60.8 <= degrees <= 100.4:
        print("Safe")
    else:
        print("Dangerous")