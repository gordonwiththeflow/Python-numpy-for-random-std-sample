import numpy as np

# Set the daily standard deviation
daily_std_dev = 1.0  # Adjust as needed based on your requirements

# Calculate the standard deviation for a 100-day period
total_days = 100
total_std_dev = daily_std_dev * 5

# Generate a random sample
random_sample = np.random.normal(loc=0, scale=total_std_dev, size=total_days)

# Print the random sample
print(random_sample)