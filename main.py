

def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"


def validate_and_execute():
    try:
        user_days = int(days_and_unit_disctionary["days"])
        if user_days > 0:
            calculated_value = days_to_units(user_days, days_and_unit_disctionary["unit"])
            print(calculated_value)
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
    user_input = input("Hey user, enter number of days and coversion unit!\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_disctionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_disctionary)
    validate_and_execute()


