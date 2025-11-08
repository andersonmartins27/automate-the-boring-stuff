scale = input("Enter C or F to indicate Celsius or Fahrenheit: ").upper()
degrees = float(input("Enter the number of degrees: "))

if (scale == "C" and (16 <= degrees <= 38)) or (scale == "F" and (60.8 <= degrees <= 100.4)):
    print("Safe")
else:
    print("Dangerous")
