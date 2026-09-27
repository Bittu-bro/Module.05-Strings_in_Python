name = "Bittu"
age = 18.33
height = 5.5
is_student = True
language = "python"
laptop = "macbook"
course = "B.Sc Physics"
result = round(age * height, 2)

print(f" '' {name} '' a {age} yrs old boy and he is {height} foot tall boy.")
print(f"My name is {name}. \nAnd I am learning {language}. \nI use a {laptop}")
print(f"Name: {name} \nAge: {age}\nCourse: {course}")
print(f"{round(age * height, 2)}")
print(f"{age * height}")



first_number = int(input("Enter the 1st Number !"))
second_number = int(input("Enter the 2nd Number !"))


addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
floor_division = first_number // second_number
division  = first_number / second_number
remainder = first_number % second_number
power = first_number ** second_number

print(f"""

Your Addition is: '{addition}'. And, Your boolean value is here '{bool(addition)}'
Your Subtraction is:'{subtraction}' . And, Your boolean value is here '{bool(subtraction)}'.
Your Multiplication is:'{multiplication}' . And, Your boolean value is here '{bool(multiplication)}'.

""")




print("Your Floor Division is: '", floor_division, "' . And, Your boolean value is here '",bool(floor_division),"' .")

print("Your Division in float value is: '", division, "' . And, Your boolean value is here '",bool(division),"' .")

print("Your Remainder in float value is: '", remainder, "' . And, Your boolean value is here '",bool(remainder),"' .")

print("Your Power in float value is: '", power, "' . And, Your boolean value is here '",bool(power),"' .")
    
