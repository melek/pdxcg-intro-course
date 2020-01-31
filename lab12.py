'''
Lab 12: Unit converter 
Assignment by Lionel Di Giacomo
1/29/2020
'''
import sys

debug = False
precision = 2
start_message = f"Starting Unit Converter with default precision of {precision}. Run with --help or -h for usage options."

if len(sys.argv) > 1:
    for arg_index in range(len(sys.argv)):
        if sys.argv[arg_index] in ["-h", "--help"]:
            print(f"Usage: {sys.argv[0]} [-h|--help] [-d|--debug] [-p|--precision INTEGER/None]")
            exit()
        if sys.argv[arg_index] in ["-d", "-pd", "-dp","--debug"]:
            debug = True
            start_message = "Info: Debug mode enabled."
        if sys.argv[arg_index] in ["-p", "-pd", "-dp", "--precision"]:
            if len(sys.argv) == arg_index + 1:
                break
            else: 
                new_precision = sys.argv[arg_index + 1]
                if(new_precision in ["None", "0"]):
                    precision = None
                    start_message = f"Info: Precision set to None."
                elif(new_precision.isdigit()):
                    precision = int(new_precision)
                    start_message = f"Info: Precision set to {precision}."
                else:
                    start_message = f"Warning: Provided precision {new_precision} an invalid parameter. Defaulting to a precision of {precision}."

print(start_message + "\n")
    
unit_names = {
    "meter" : "meters",
    "meters" : "meters",
    "m" : "meters",
    "kilometer" : "kilometers",
    "kilometers" : "kilometers",
    "km" : "kilometers",
    "yard" : "yards",
    "yards" : "yards",
    "y" : "yards",
    "foot" : "feet",
    "feet" : "feet",
    "ft" : "feet",
    "'" : "feet",
    "mile" : "miles",
    "miles" : "miles",
    "mi" : "miles",
    "inch" : "inches",
    "inches" : "inches",
    "in" : "inches",
    "\"" : "inches", 
    "centimeter" : "centimeters",
    "centimeters" : "centimeters",
    "cm" : "centimeters",
    "millimeter": "millimeters",
    "millimeters": "millimeters",
    "mm": "millimeters"
}

unit_values = {
    "meters": 1,
    "kilometers": 1000,
    "yards": 0.9144,
    "feet": 0.3048,
    "miles": 1609.34,
    "inches": 0.0254,
    "centimeters": .01,
    "millimeters": .001  
}

# A function to collect a valid, positive integer.
def validIntInput(prompt, max_input = 2147483647, default = None):
    while True: 
        menu_input = input(prompt)
        if menu_input == "" and default != None:
            return int(default)
        elif(menu_input.isdigit() == False):
            print("Please guess a positive number.")
            continue
        else:
            menu_input = int(menu_input)
        if(menu_input < 1 or menu_input > max_input):
            print(f"{menu_input} is too big! Pick a number up to {max_input}.")
            continue
        else:
            return menu_input

# A function to collect a valid unit string
def validUnitInput(prompt = "Please select a unit: "):
    user_input = None
    repeat_input = False
    while user_input not in list(unit_names.keys()):
        if repeat_input:
            print("Please enter a valid unit of distance (abbreviations are ok). Valid values are:\n" + str(", ".join(list(unit_names.keys()))))
        else: 
            repeat_input = True
        user_input = input(prompt)
    return user_input

measurement = validIntInput("What is the distance measurement (number only?): ")
measurement_units = validUnitInput("What units are the measurement in?: ")
target_units = validUnitInput("What units would you like to convert the distance to?: ")

unit_in_meters = unit_values[unit_names[measurement_units]]
measurement_in_meters = measurement * unit_in_meters
target_unit_factor = unit_values[unit_names[target_units]]
target_measurement = round(measurement_in_meters / target_unit_factor, precision)

if(debug):
    print("units_in_meters: " + str(unit_in_meters))
    print("measurement_in_meters: " + str(measurement_in_meters))
    print("target_unit_factor: " + str(target_unit_factor))
    print("target_measurement: " + str(target_measurement))

print(f"{measurement} {measurement_units} to {unit_names[target_units]} = {target_measurement}")