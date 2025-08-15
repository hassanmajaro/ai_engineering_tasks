''' Task3: Days and Activities Pairing
    Stores days of the week in a tuple and ask the user to input an activity for three specific days.
        Use dictionary comprehension to pair days and activities
        Print the dictionary
    Requirements:
        use tuple for days
        use {day: activity for day, activity in zip(...., ....)}.
    Tip: Research on how to use zip()
'''
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
day1_activity = input(f"Input activity for {days[0]}: ")
day2_activity = input(f"Input activity for {days[1]}: ")
day3_activity = input(f"Input activity for {days[2]}: ")
day4_activity = input(f"Input activity for {days[3]}: ")
day5_activity = input(f"Input activity for {days[4]}: ")
day6_activity = input(f"Input activity for {days[5]}: ")
day7_activity = input(f"Input activity for {days[6]}: ")

activity = [day1_activity, day2_activity, day3_activity, day4_activity, day5_activity, day6_activity, day7_activity]
print(dict(zip(days, activity)))