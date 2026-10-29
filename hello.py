from datetime import datetime
print("hello world")
# Get current date and time
now = datetime.now()

# Format to show only the time (Hour:Minute:Second)
print("Time only:", now.strftime("%H:%M:%S"))
# Output: 09:09:15

