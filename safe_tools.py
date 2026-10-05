#Function 1 - safe_divide

#Returns a / b, or the text Cannot divide by zero if b is 0.

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"



    #Function 2 - safe_number

#Turns text into a whole number, or returns Not a number if it cannot.

def safe_number(text):
    try:
        return int(text)
    except ValueError:
        return "Not a number"


    #Function 3 - get_field

#Looks up a key in a dictionary, or returns Field not found if the key is missing.

def get_field(learner, key):
    try:
        return learner[key]
    except KeyError:
        return "Field not found"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_number("42"))
print(safe_number("abc"))

learner = {"name": "Amina", "score": 82}
print(get_field(learner, "score"))
print(get_field(learner, "email"))