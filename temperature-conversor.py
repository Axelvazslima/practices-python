# Temperature conversor

def temperatureConversor():
    print("Enter a temperature scale followed by it's temperature value(e.g. C and 10 for 10 degrees Celsius).\nThe code will convert the temperature to the other two scales (Fahrenheit and Kelvin) and display the results.")
    celsius = ["ºC", "C", "CELSIUS", "Cº"]
    fahrenheit = ["ºF", "F", "FAHRENHEIT", "Fº"]
    kelvin = ["KELVIN", "K"]
    scale = input("What scale are you using? ")
    temp = float(input("How hot is there? "))
    if scale.upper() in celsius:
        c = temp
        f = (c * 1.8) + 32
        k = c + 273.15
        print(f"Your temperature is {c}ºC, so it's {f}ºF and {k}K")
    if scale.upper() in fahrenheit:
        f = temp
        c = (f - 32)/(9/5)
        k = (f+459.67) * 5/9
        print(f"Your temperature is {f}ºF, so it's {c}ºC and {k}K")
    if scale.upper() in kelvin:
        k = temp
        c = k-273.15
        f = (((k-273.15)*9)/5)+32
        print(f"Your temperature is {k}K, so it's {c}ºC and {f}ºF")


temperatureConversor()
