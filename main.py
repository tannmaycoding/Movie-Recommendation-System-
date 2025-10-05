"""
This is a movie recommendation system which uses your recently watched movies and movies you can continue watching to recommend new movies of same language and category
"""
import pandas as pd

# Read the excel sheets
df = pd.read_excel("Test.xlsx", sheet_name="Recently Watched")
df2 = pd.read_excel("Test.xlsx", sheet_name="Continue Watching")
df3 = pd.read_excel("Test.xlsx", sheet_name="Movies")

# Filter the dataframes to get liked movies
rwl = df[df.Liked == True]
cwl = df2[(df2["Liked"] == True) & (df2['Duration Seen(min)'] > df2["Total Duration(min)"] // 10)]

# Combine the liked movies from rwl and cwl
combined_liked = pd.concat([rwl, cwl])

# Get unique movies, languages, and categories from the combined liked DataFrame
combined_movies = combined_liked.Movie.unique()
combined_languages = combined_liked.Language.unique()
combined_categories = combined_liked.Category.unique()

# Filter df3 based on the combined movies, languages, and categories
filtered_df3 = pd.DataFrame(df3[
    (df3.Movie.isin(combined_movies)) &
    (df3.Language.isin(combined_languages)) &
    (df3.Category.isin(combined_categories))
], columns=["Movie", "Language", "Category"])

print(filtered_df3)
