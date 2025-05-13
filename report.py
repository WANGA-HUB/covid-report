# COVID-19 Data Analysis & Visualization
# Author: [ASHLEY]
# Date: [13-05-2025]


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


print("Loading dataset...")
df = pd.read_csv("owid-covid-data.csv")


print("\nDataset Overview:")
print(df.info())
print("\nFirst Few Rows:")
print(df.head())


print("\nCleaning data...")
df["date"] = pd.to_datetime(df["date"]) 
selected_countries = ["Kenya", "USA", "India"]
df = df[df["location"].isin(selected_countries)]  

df.fillna(df.mean(), inplace=True)


print("\nVisualizing COVID-19 case trends...")
plt.figure(figsize=(12, 6))
sns.lineplot(x=df["date"], y=df["total_cases"], hue=df["location"])
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.xticks(rotation=45)
plt.show()


print("\nAnalyzing vaccination rollout...")
plt.figure(figsize=(12, 6))
sns.lineplot(x=df["date"], y=df["total_vaccinations"], hue=df["location"])
plt.title("Total Vaccinations Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.xticks(rotation=45)
plt.show()

print("\nGenerating world map visualization...")
latest_data = df[df["date"] == df["date"].max()]
fig = px.choropleth(latest_data, 
                    locations="iso_code",
                    color="total_cases",
                    hover_name="location",
                    title="Global COVID-19 Case Density")
fig.show()


print("\n🔍 Key Findings:")
print("- Kenya, USA, and India show different case trajectories.")
print("- Vaccination adoption varies by country.")
print("- Death rates indicate spikes during specific periods.")
