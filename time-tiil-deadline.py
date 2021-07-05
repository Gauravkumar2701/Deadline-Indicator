from  datetime import datetime

user_input = input("Enter your goal and deadline separated by semicolon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date=datetime.datetime.strptime(deadline,"%d.%m.%Y")

today_date=datetime.datetime.today()

Time_remaining=deadline_date-today_date

print(f"Time remaining for completing your {goal} is {Time_remaining.days} days and {int(Time_remaining.total_seconds()/60/60)} hours")