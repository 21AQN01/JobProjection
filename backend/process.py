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
# Save processed data as json
#main_df.to_json("data/processed.json", orient="records")

# if want to run row by row like in Jupyter notebook, install Jupyter extension for VSCode and designate cells using # %%
# print(df.head())
#######-------------------------------------------------------------
import pandas as pd

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
major_df["CIPCODE"].duplicated().sum()



# Load in the second table
numEmployWages_df = pd.read_excel("raw_data/employPerDeg.xlsx")

# Change table rows to numeric
numEmployWages_df.iloc[:, 1:] = numEmployWages_df.iloc[:, 1:].apply(pd.to_numeric, errors="coerce")

# Clean and only keep the needed columns
numEmployWages_df = numEmployWages_df.drop(columns=["Employment distribution, percent, 2024", 
                                                    "Employment distribution, percent, 2034"])
# Load in the third table, 
bachHigher_df = pd.read_excel("raw_data/bachelors_and_higher.xlsx")

# Change table rows to numeric
bachHigher_df.iloc[:, 1:] = bachHigher_df.iloc[:, 1:].apply(pd.to_numeric, errors="coerce")

# Get rid of the subcolumns MOE and keep numbers subcolumns
bachHigher_df = bachHigher_df.iloc[:, [0] + list(range(1, len(bachHigher_df.columns), 2))]

# Rename col to Occupation andremove Total row
bachHigher_df = bachHigher_df.rename(columns={"Field of Degree2": "Occupation"})
bachHigher_df = bachHigher_df.iloc[2:].reset_index(drop=True)

#Remove unecessary footnotes
bachHigher_df["Occupation"] = bachHigher_df["Occupation"].str.replace(
    r"[¹²³⁴⁵⁶⁷⁸⁹⁰]", "", regex=True
)

# Load in the fourth table, do the same as third table
grad_df = pd.read_excel("raw_data/graddeg.xlsx")

# Change table rows to numeric
grad_df.iloc[:, 1:] = grad_df.iloc[:, 1:].apply(pd.to_numeric, errors="coerce")

# Get rid of the subcolumns MOE and keep numbers subcolumns
grad_df = grad_df.iloc[:, [0] + list(range(1, len(grad_df.columns), 2))]

# Rename col to Occupation andremove Total row
grad_df = grad_df.rename(columns={"Field of Degree2": "Occupation"})
grad_df = grad_df.iloc[2:].reset_index(drop=True)

#Remove unecessary footnotes
grad_df["Occupation"] = grad_df["Occupation"].str.replace(
    r"[¹²³⁴⁵⁶⁷⁸⁹⁰]", "", regex=True
)

# Load in the fifth table
roadmap_df = pd.read_excel("raw_data/roadmap.xlsx")

# drop nas and make sure column titles are clean
roadmap_df = roadmap_df.dropna(how="all")
roadmap_df = roadmap_df.dropna(axis=1, how="all")
roadmap_df.columns = roadmap_df.columns.str.strip()

#keep code as strings and not numbers
roadmap_df["CIP2020Code"] = roadmap_df["CIP2020Code"].astype(str).str.strip()
roadmap_df["SOC2018Code"] = roadmap_df["SOC2018Code"].astype(str).str.strip()

# Save processed data as clean files
main_df.to_csv("data/collegeScorecardEarn.csv", index=False)
numEmployWages_df.to_csv("data/employPerDeg.csv", index=False)
bachHigher_df.to_csv("data/bachelors_and_higher.csv", index=False)
grad_df.to_csv("data/graddeg.csv", index=False)
roadmap_df.to_csv("data/roadmap.csv", index=False)
roadmap_df.to_json("data/roadmap.json", orient="records")


