# This script just calculates the amount of tip the customer should pay
# based on her/his check of the food.

check = int(input("Check amount: $  "))

tip_percentage = int(
    input("Percentage of the check you want to pay as a tip: % ")
)

tip = check * (tip_percentage / 100)

print("Tip: $ " + str(tip))
