import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("students.csv")
df.fillna(df.mean(numeric_only=True), inplace = True)

df["TotalScore"] = df[["MathScore","ScienceScore","EnglishScore"]].sum(axis=1)
df["Result"] = np.where(df["TotalScore"] >= 120 , "Pass" , "Fail")
gendere_avg = df.groupby("Gender")[["MathScore","ScienceScore","EnglishScore"]].mean

top_student = df.sort_values(by="TotalScore" , ascending=False).head(5)

df["NormalizedStudyHours"] = (df["StudyHours"] - df["StudyHours"].min()) / (df["StudyHours"].max() - df["StudyHours"].min())

df.to_csv("updatedStudent.csv" )

plt.bar(df["Name"] , df["TotalScore"])
plt.xticks(rotation = 45)
plt.title("Student Total Scores")
plt.show()