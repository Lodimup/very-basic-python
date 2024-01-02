"""
BMI Calculator
BMI Table
Underweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater
"""

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = weight / (height ** 2)

weight_class = ""

if bmi < 18.5:
    weight_class = "Underweight"
elif bmi < 25:
    weight_class = "Normal weight"
elif bmi < 30:
    weight_class = "Overweight"
else:
    weight_class = "Obesity"

ideal_weight = ((24.9 + 18.5) / 2) * (height ** 2)
weight_gain = ideal_weight - weight

print(f"Your BMI is {bmi:.2f} and you are {weight_class}. You need to gain(loss) {weight_gain:.2f} kg to reach ideal weight.")
















# ideal_weight = ((24.9 + 18.5) / 2) * (height ** 2)
# weight_gain = ideal_weight - weight

# print(f"Your BMI is {bmi:.2f} and you are {result}. You need to gain(loss) {weight_gain:.2f} kg to reach ideal weight.")