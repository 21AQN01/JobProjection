import pandas as pd

# Load raw data, skip first title row
df = pd.read_excel("raw_data/employPerDeg.xlsx", sheet_name="Table 5.2", skiprows=1)

# rename columns
df.columns = [
    "Education",
    "Employment_2024",
    "Employment_2034",
    "Employment_dist_2024",
    "Employment_dist_2034",
    "Numeric_Change",
    "Percent_Change",
    "Median_Wage_2024"
]

#remove all na row
df = df.dropna()

# Save processed data as json
df.to_json("data/processed.json", orient="records")

# if want to run row by row like in Jupyter notebook, install Jupyter extension for VSCode and designate cells using # %%
# print(df.head())