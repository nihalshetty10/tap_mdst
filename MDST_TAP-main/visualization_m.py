import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# TODO: Load dataset; replace this csv to your file
df = pd.read_csv("US_Accidents_Cleaned.csv")

# Step 1: Handling the format
# TODO: Remove extra precision if exists

# TODO: Extract relevant time-based features

# TODO: Fix missing values for numerical columns
# TODO: Ensure Severity is numeric



# Pie Charts
severity_counts = df['Severity'].value_counts(normalize=True) * 100
# Bar Plots
# Accident Cases vs Hours
print("Hello")

hourly_counts = df['Hour_of_Day'].value_counts().sort_index()

# Accident Cases vs Months
hour_of_the_day=df['Hour_of_Day']

sns.histplot(hour_of_the_day, bins=24, kde=True)
plt.show()
# Accident Cases vs Different Temperature


# Accident Cases vs Different Humidity


# Accident Cases vs Wind Speed
