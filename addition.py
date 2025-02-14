# Function to add two numbers
def add_numbers(a, b,c):
    return a + b +c

# Input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Compute sum
sum_result = add_numbers(num1, num2,num3)

# Display result
print(f"The sum of {num1} and {num2} and {num3} is {sum_result}")
