import pandas as pd

# # Load raw data, skip first title row
# df = pd.read_excel("raw_data/employPerDeg.xlsx", sheet_name="Table 5.2")

# # rename columns
# df.columns = [
#     "Education",
#     "Employment_2024",
#     "Employment_2034",
#     "Employment_dist_2024",
#     "Employment_dist_2034",
#     "Numeric_Change",
#     "Percent_Change",
#     "Median_Wage_2024"
# ]

# #remove all na row
# df = df.dropna()

#load in main file
main_df = pd.read_csv("raw_data/fieldStudyEarning.csv")

# clean data
# Let's only keep bachelor's for this first part 
main_df = main_df[main_df["CREDDESC"] == "Bachelor's Degree"] 

main_df = main_df.replace(["PS", "NA"], pd.NA) # Treating privacy surpression and NA as NAns

# change column type from object to numeric to aggergate
cols = [
    "EARN_MDN_4YR_NAT",
    "EARN_P25_4YR_NAT",
    "EARN_P75_4YR_NAT"
]

main_df[cols] = main_df[cols].apply(pd.to_numeric, errors="coerce")

#join majors by their CIPCODE and aggergate by their mean values
major_df = (
    main_df
    .groupby("CIPCODE", as_index=False)
    .agg({
        "CIPDESC": "first",
        "EARN_MDN_4YR_NAT": "mean",
        "EARN_P25_4YR_NAT": "mean",
        "EARN_P75_4YR_NAT": "mean"
    })
)
major_df.head(5)
major_df.shape
major_df["CIPCODE"].duplicated().sum()

# Save processed data as csv
main_df.to_csv("data/collegeScorecardEarn.csv", index=False)

# Save processed data as json
#main_df.to_json("data/processed.json", orient="records")

# if want to run row by row like in Jupyter notebook, install Jupyter extension for VSCode and designate cells using # %%
# print(df.head())

