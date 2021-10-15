# Conditional statements


# Working with numbers
age = 15
# we begin conditional statements with an 'if' keyword, then the condition to be tested on
# these conditions can have operators -> >, <, >=, <=, and != are all ways of evaluating statements
if age > 18:
    # after the conditional, write a colon at the end of the line (:)
    # the code to execute if the above condition is evaluated to true (indented!)
    print("You can vote!")
else:
    # the code to execute if the above condition fails -- in any other scenario
    print("You can't vote.")

# we can also have more than one conditions to check, in case the first one evaluates to false

# we can combine conditions using the keywords 'and' and 'or'
if age < 19 and age > 14:
    print("You are a high school student.")
# shorthand for 'else if' - if the first statement is false, check this condition
elif age <= 14 and age >= 12:
    print("You are a middle school student.")

elif age < 12:
    print("You are an elementary school student.")
# if all of these conditions are still false
else:
    print("You are not a student!")
