seconds = int(input("Enter the number of seconds: "))

hours = seconds // 3600
remaining_seconds = seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(hours, "hours,", minutes, "minutes,", seconds, "seconds")
