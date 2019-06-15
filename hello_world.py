
print("Hello Dojo")

apples = input("How many apples would you like to buy? ")

apple_cost = .50

try:

    total = int(apples) * apple_cost

    print(total)

except ValueError:

    print("Error - You have to enter a number")


