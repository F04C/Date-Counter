from datetime import datetime

# Start date
start_date = datetime(2021, 4, 27)

# Current date
end_date = datetime.now()

# Difference in days
days_difference = (end_date - start_date).days

# Print the result
print("Number of days between April 27, 2021, and today:", days_difference)
