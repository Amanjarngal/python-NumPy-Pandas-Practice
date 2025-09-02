import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("health_fitness_dataset.csv")

df["Age Group"] =  pd.cut(df["Age"] , bins=[18,30,40,50,60] , labels=["18-30","31-40","41-50","51-60"])
avg_activity = df.groupby("Age Group")[["Steps Walked", "Calories Burned", "Sleep Hours", "Water Intake"]].mean()
print(avg_activity)

print("")

correlation = df["Sleep Hours"].corr(df["Calories Burned"])
print(correlation)

print("")

df["Fitness Score"] = df["Steps Walked"]*0.6 +df["Calories Burned"] * 0.4
fittest_user = df.sort_values("Fitness Score" , ascending=False).head(5)
print( fittest_user[["UserID","Steps Walked","Calories Burned","Fitness Score"]])

avg_activity[["Steps Walked","Calories Burned"]].plot(kind='bar' ,figsize=(8,5))
plt.title("Average Steps & Calories Burned by Age Group")
plt.ylabel("Average")
plt.show()

# Plot trends of activity levels (Steps & Sleep Hours)
plt.figure(figsize=(10,5))
plt.plot(df["UserID"], df["Steps Walked"], marker='o', label="Steps Walked")
plt.plot(df["UserID"], df["Sleep Hours"]*2000, marker='s', label="Sleep Hours (scaled x2000)")
plt.title("Trends of Activity Levels")
plt.xlabel("User ID")
plt.ylabel("Activity Level")
plt.legend()
plt.show()