# A 2 dimensional array is an array of arrays
two_dimensional_letters = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
# Here is how you would index into a 2d array
two_dimensional_letters[0][2]
# Will have a value of 'c'

# Reading user input is easy - just use the input() function in python as the value you set a variable equal to
# Inside the input function is a string that will be prompted to the user for this input
name = input("Type your name here: ")

# If you need to work with numbers and user input, use the int() function to convert a string (default from input() function) to an integer
age = int(input("Enter your age: "))
age += 5
# Remember, must only concatenate or add up strings to strings, you can't add integers to strings
print("You will be " + str(age) + " years old in 5 years.")

# Conditionals consist of code to execute if a condition is true, and code to execute if otherwise
# Conditionals depend on true/false values, which we use the boolean data type for (True / False)
havingFun = True
if havingFun:
    # Execute your code here if you are having fun!
    print("I am having fun! :)")
else:
    # Execute your code here if you are NOT having fun!
    print("I am NOT having fun :(")
