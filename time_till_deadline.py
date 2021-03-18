import datetime

user_input = input("Enter your goal with your deadline separated with colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today = datetime.datetime.today()
#calculation how many days from now till deadline

time_till_days_to_deadline = deadline_date - today
print(f"Dear user time remaining for your goal: {int(time_till_days_to_deadline.total_seconds() / 60 / 60)} hours")
print(input_list)