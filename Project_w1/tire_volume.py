#I added a looping feature different calculation for volume tire
from datetime import datetime 
import math 
current_date = datetime.now() 
width = float(input("Enter the width of the tire in mm: "))
ratio = float(input("Enter the aspect of the ratio of the tire: "))
diameter = float(input("Enter the diameter of the tire in inches: "))

volume = (math.pi * width ** 2 * ratio) * (width * ratio + 2540 * diameter) / 10000000000

print(f"The approximate volume is {volume: .2f} liters")
with open("volumes.txt", mode="a") as volumes_file:
    print(f"{current_date:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume: .2f} liters", file=volumes_file)

restart = input("Would you like to calculate another tire volume? (yes or no): ")
if restart.lower() == 'yes':
    import tire_volume
else:
    print("Thank you for using the tire volume calculator. Have a nice day!🎈")