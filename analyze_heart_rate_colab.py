
# 📊 Student Heart Rate Analysis - Google Colab Version
# This script reads heart rate data from an Excel file and analyzes engagement patterns

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files

# Step 1: Upload the Excel file
uploaded = files.upload()

# Step 2: Load the data
file_name = list(uploaded.keys())[0]
df = pd.read_excel(file_name)

# Step 3: Identify heart rate columns (these are MAC-address like or unnamed numeric headers)
heart_rate_columns = df.columns[6:18]

# Step 4: Calculate mean heart rate per row
df["Mean_Heart_Rate"] = df[heart_rate_columns].mean(axis=1)

# Step 5: Group and analyze

def plot_grouped_avg(column_name):
    grouped = df.groupby(column_name)["Mean_Heart_Rate"].mean().sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=grouped.index, y=grouped.values, palette='viridis')
    plt.title(f"Average Heart Rate by {column_name}")
    plt.ylabel("Mean Heart Rate (bpm)")
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

# Step 6: Generate plots
for factor in ["Activity", "Slots", "Location", "Module"]:
    plot_grouped_avg(factor)
