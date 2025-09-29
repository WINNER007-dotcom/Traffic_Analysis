import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
# Taking Raw Data from the year 2022-2025
data = {"Location": ["Ring Road","NH-8","Ring Road","NH-8","MG Road","MG Road","Dwarka Mor","Dwarka Mor","Connaught Place","Connaught Place"],
    "Time": ["08:00","18:00","09:00","19:00","08:30","18:30","09:15","19:15","08:45","18:45"],
    "Vehicles": [120,300,150,320,200,350,100,280,250,400],
    "Accident": [1,3,0,2,0,1,0,4,1,0],
    "Congestion_Level": ["High","Very High","Medium","Very High","High","Very High","Medium","Very High","High","Very High"],
    "Deaths": [3,1,2,2,0,1,4,0,2,1],
    "Injuries": [5,10,2,8,1,6,0,3,7,12],
    "Weather": ["Clear","Rainy","Clear","Rainy","Clear","Rainy","Clear","Rainy","Clear","Rainy"],
    "Date": ["23-08-2023","17-08-2024","24-08-2025","22-08-2022","25-08-2023","16-08-2024","26-08-2023","19-08-2024","21-08-2023","27-08-2024"]}
# Creating a DataFrame
df = pd.DataFrame(data)
# Save raw data
df.to_csv("traffic_data.csv", index=False)
# Accidents per Location
acc_count = df.groupby("Location", as_index=False)["Accident"].sum()
acc_count.to_html("accidents_table.html", index=False)
# Injuries & Deaths
injury_death = df.groupby("Location", as_index=False)[["Injuries","Deaths"]].sum()
injury_death.to_html("injury_death.html", index=False)
# Combined Analysis
combined = df.groupby("Location", as_index=False).agg({"Accident":"sum", "Injuries":"sum", "Deaths":"sum"})
combined.to_html("combined.html", index=False)
# Combined Bar Chart
fig = plt.figure(figsize=(8,5))
x = range(len(combined["Location"]))
plt.bar(x, combined["Accident"], width=0.25, label="Accidents")
plt.bar([i+0.25 for i in x], combined["Injuries"], width=0.25, label="Injuries")
plt.bar([i+0.50 for i in x], combined["Deaths"], width=0.25, label="Deaths")
plt.xticks([i+0.25 for i in x], combined["Location"], rotation=45)
plt.title("Accidents, Injuries & Deaths per Location")
plt.ylabel("Count")
plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
plt.legend()
fig.savefig("accidents.png")
plt.close(fig)
# Accidents by Weather (Pie Chart)
weather_summary = df.groupby("Weather")["Accident"].sum()
fig2 = plt.figure(figsize=(5,5))
plt.pie(weather_summary, labels=weather_summary.index, autopct="%1.0f%%")  
plt.title("Accidents by Weather Conditions")
fig2.savefig("weather.png")
plt.close(fig2)
# Congestion Levels
cong_count = df["Congestion_Level"].value_counts()
fig3 = plt.figure(figsize=(6,4))
plt.bar(cong_count.index, cong_count.values, color="orange")
plt.title("Congestion Level Distribution")
plt.ylabel("Frequency of Accidents")
plt.xlabel("Congestion Level")
plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
fig3.savefig("congestion.png")
plt.close(fig3)





