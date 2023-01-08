
from ast import MatchAs


height=float(input("type your height: "))
weight=float(input("type your weight: "))

if height > 5:
    height=height/100

bmi=weight/height**2
print("BMI:",bmi)