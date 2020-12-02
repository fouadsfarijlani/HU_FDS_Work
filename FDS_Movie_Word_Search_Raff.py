import pandas as pd

# Reads data and creates dataframe
df = pd.read_csv("wiki_movie_plots_deduped.csv")

# Subsetting: create a new df with only Title, Release Year, Origin/Ethnicity, Plot
new_df = df[["Title", "Origin/Ethnicity", "Plot"]].copy()

# Change the column names to Title, Year, Origin, Plot
new_df.rename(columns={"Origin/Ethnicity":"Origin"},inplace=True)

# Create a function allowing for word to be searched.
def add_word_present(word):
    new_df[word + "_Films"] = df["Plot"].str.contains(word).astype(int)

# Create a function allowing for percentage of films to be comapred against other origins.
def compare_origins2(word):
    add_word_present(word)
    global new_df
    new_df["Total_Films"] = 1
    new_df = new_df.groupby("Origin").sum()
    new_df["Percentage_" + word] = round((new_df[word + "_Films"] / new_df["Total_Films"]) * 100,2)
    new_df = new_df.groupby("Origin").sum()
    new_df = new_df.sort_values(by=["Percentage_" + word], ascending=False)
    new_df = new_df.reset_index()
    print(new_df)

# User input   
user_input = input("What do you want to search for? ")
compare_origins2(user_input)



