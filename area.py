# area.py
# Chris Tully 2024

def calc_area():
    # Get Length
    length_input = float(input("Please enter the length of the rectangle: "))
    # Get Width
    width_input = float(input("Please enter the width of the rectangle: "))

    # Length and Width should be greater than Zero.
    if (length_input > 0 and width_input > 0):
        
        # Area = Length * Width
        area_calculated = length_input * width_input
        
        # Print out the Area
        print(f"The Area of the rectangle with length {length_input} and width {width_input} is: {area_calculated}")

    else:
        
        print("Both Length and Width should be greater than Zero." )