calculation_to_unit = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_unit}"


def validate_and_execute():
    try:
        user_days = int(num_of_days_element)
        if user_days > 0:
            my_result = days_to_units(user_days)
            print(my_result)
        elif user_days == 0:
            print("Zero is not valid value")
        else:
            print("you entered negative number, no conversion for you")
    except ValueError:
        print("Invalid input value, your input is not a valid number!!!")
    if user_input == "exit":
        print("Bye bye")

user_input = ""

while user_input != "exit":
    user_input = input("Hey user, enter number of days as a coma separated list and I will convert it to hours!\n")

    for num_of_days_element in user_input.split(","):
        validate_and_execute()