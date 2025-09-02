import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("movieData.csv")
# print(df)
# (a) Average rating per genre
Rating_avg = df.groupby("Genre")["UserRating"].mean()
print(Rating_avg)
# (b) Top 10 movies by rating
top_movie = df.sort_values(by="UserRating" , ascending=False).head(10)
print(top_movie)
# (c) Rating trends over time (average rating by year)
trend = df.groupby("ReleaseYear")["UserRating"].mean()
print(trend)

# (d) Recommend movies based on genre similarity
def recomend_by_genre(movie_title):
    genre = df.loc[df["Title"] == movie_title, "Genre"].values[0]
    recomendation = df[df["Genre"] == genre].sort_values(by="UserRating" , ascending = False).head(5)
    return recomendation[["Title" , "UserRating"]]
print(recomend_by_genre("Journey Beyond"))