def to_kilos(weight):
    return round(float(weight) / 2.205, 2)


def to_cm(height_in_inches):
    return round(float(height_in_inches) * 2.54, 2)


name = "Jay Womack"
age = 35  # about to be 36...
height = 72  # inches
weight = 195  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"Hos teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
print(f"My weight in Kilos is {to_kilos(weight)}.")
print(f"My height in inches is {to_cm(height)}.")