import math
def height_in_feet_inches(height):
    return f" {str(math.floor(height/12))}' {str(height % 12)}\""


print("How old are you?", end=' ')
age = int(input())
print("How tall are you in inches?", end=' ')
height = int(input())
print("How much do you weigh in lbs?", end=' ')
weight = int(input())

print(f"So, you're {age} years old, {height_in_feet_inches(height)} tall and {weight} lbs.")