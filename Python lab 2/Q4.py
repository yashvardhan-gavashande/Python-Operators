# Program to find the greatest of three numbers

# Print the question
print("Question 4: Write a program to calculate the greatest of three numbers\n")

# Define three numbers
number1 = 10
number2 = 15
number3 = 12

# Check which number is the greatest
if number1 >= number2 and number1 >= number3:
    greatestNumber = number1
elif number2 >= number1 and number2 >= number3:
    greatestNumber = number2
else:
    greatestNumber = number3

print("The greatest number is:", greatestNumber)
