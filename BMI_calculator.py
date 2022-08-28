height = input("Please type your height in cm: ")
weight = input("Please type your weight in kg: ")

result = (float(weight) ) / (float(height) / 100) ** 2
result = int(result)
print("Your result: " + str(result))