from datetime import date, datetime
# Get today's date
today = date.today()

# Get current date and time
now = datetime.now()

# Display results
print("Today's Date:", today)
print("Current Date and Time:", now)

# Display date components
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)