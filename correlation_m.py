import scipy.stats as stats
import pandas as pd

# Load dataset
df = pd.read_csv("US_Accidents_Cleaned.csv")

#TODO: Define numerical columns for correlation analysis
numerical_cols = ['Severity', 'Start_Lat', 'Start_Lng', 'End_Lat', 'End_Lng', 
                  'Distance(mi)', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 
                  'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']

correlation_results = []

for col in numerical_cols:
    if col != "Severity":  
        #TODO: Drop rows with missing values for 'Severity' and the selected column
        subset1 = df.dropna(subset=['Severity', col])

        #TODO: Compute correlation only if enough data points exist
        if len(subset1) >= 1:
            r, p_value = stats.pearsonr(subset1['Severity'], subset1[col])
        else:
            r, p_value = None, None  

        #TODO: Categorize correlation strength
        if r is None:
            strength = "Not enough data"
        elif 0.0 < abs(r) < 0.1:
            strength = "No correlation"
        elif 0.1 <= abs(r) < 0.3:
            strength = "Low correlation"
        elif 0.3 <= abs(r) < 0.5:
            strength = "Medium correlation"
        elif 0.5 <= abs(r) < 0.7:
            strength = "High correlation"
        elif 0.7 <= abs(r) <= 1:
            strength = "Very high correlation"
        else:
            strength = "Invalid"

        correlation_results.append({
            "Feature": col,
            "Correlation": r,
            "P-value": p_value,
            "Strength": strength
        })
#TODO: Convert correlation results to a DataFrame
correlation_df = pd.DataFrame(correlation_results)

#TODO: Print the correlation DataFrame
print(correlation_df)

import matplotlib.pyplot as plt
import numpy as np
y=np.array(df['Severity'].value_counts(normalize=True))

plt.pie(y,autopct='%1.1f%%' )
plt.show()

x=np.array(df['Crossing'].value_counts(normalize=True))
plt.pie(x,autopct='%1.1f%%' )
plt.show()



#TODO: Save results to a CSV file
...
