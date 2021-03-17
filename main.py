calculation_to_unit = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_unit}"


def validate_and_execute():
    try:
        user_days = int(user_input)
        if user_days > 0:
            my_result = days_to_units(user_days)
            print(my_result)
        elif user_days == 0:
            print("Zero is not valid value")
    except ValueError:
        print("Invalid input value, your input is not a valid number!!!")

user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")

validate_and_execute()