import pandas as pd
import matplotlib.pyplot as plt

# TODO: Load dataset; replace this csv to your file
df = pd.read_csv("filtered_data.csv")

# Step 1: Handling the format
# TODO: Remove extra precision if exists

# TODO: Extract relevant time-based features

# TODO: Fix missing values for numerical columns
# TODO: Ensure Severity is numeric



# Pie Charts
severity_counts = df['Severity'].value_counts(normalize=True) * 100


# Road conditions presence
# Bar Plots
# Accident Cases vs Hours
hourly_counts = df['Hour'].value_counts().sort_index()
hour_of_the_day=df['Hour']

sns.hisplot(hour_of_the_day, hourly_counts)

# Accident Cases vs Months


# Accident Cases vs Different Temperature


# Accident Cases vs Different Humidity


# Accident Cases vs Wind Speed
