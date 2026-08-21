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
# Rename columns
numEmployWages_df.columns = [
    "Education",
    "Employment_2024",
    "Employment_2034",
    "Emp_Numeric_Change",
    "Emp_Percent_Change",
    "Median_Wage_2024"
]

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

#strip period from job title
roadmap_df["CIP2020Title"] = roadmap_df["CIP2020Title"].str.replace(".", "", regex=False)

# Save processed data as clean files
main_df.to_csv("data/collegeScorecardEarn.csv", index=False)

numEmployWages_df.to_csv("data/employPerDeg.csv", index=False)
numEmployWages_df.to_json("data/employPerDeg.json", orient="records")

major_df["CIPDESC"] = major_df["CIPDESC"].str.replace(".", "", regex=False)
# sort by median income
major_df = major_df.sort_values("EARN_MDN_4YR_NAT", ascending=False)
major_df.to_csv("data/majorEarnings.csv", index=False)
major_df.to_json("data/majorEarnings.json", orient="records")


bachHigher_df.to_csv("data/bachelors_and_higher.csv", index=False)

grad_df.to_csv("data/graddeg.csv", index=False)

roadmap_df.to_csv("data/roadmap.csv", index=False)

roadmap_df.to_json("data/roadmap.json", orient="records")

# Combining some BLS tables (oocupations/employment/roadmap)
df1 = pd.read_excel("raw_data/occupation.xlsx")
df2 = pd.read_excel("raw_data/oews_2025.xlsx")

# Cleaning occupation table
projections_df = df1[[
    "2024 National Employment Matrix code",
    "2024 National Employment Matrix title",
    "Employment, 2024",
    "Employment, 2034",
    "Employment change, numeric, 2024–34",
    "Employment change, percent, 2024–34",
    "Occupational openings, 2024–34 annual average",
    "Median annual wage, dollars, 2024[1]",
    "Typical education needed for entry"
]].copy()

projections_df = projections_df.rename(columns={
    "2024 National Employment Matrix code": "SOCCode",
    "2024 National Employment Matrix title": "Occupation",
    "Employment, 2024": "Employment_2024",
    "Employment, 2034": "Employment_2034",
    "Employment change, numeric, 2024–34": "Employment_Change",
    "Employment change, percent, 2024–34": "Employment_Growth_Percent",
    "Occupational openings, 2024–34 annual average": "Annual_Openings",
    "Median annual wage, dollars, 2024[1]": "Median_Wage_2024",
    "Typical education needed for entry": "Typical_Education"
})

# Cleaning owes table
oews_df = df2[[
    "OCC_CODE",
    "OCC_TITLE",
    "TOT_EMP",
    "A_MEAN",
    "A_MEDIAN",
    "A_PCT10",
    "A_PCT25",
    "A_PCT75",
    "A_PCT90"
]].copy()

oews_df = oews_df.rename(columns={
    "OCC_CODE": "SOCCode",
    "OCC_TITLE": "Occupation",
    "TOT_EMP": "Employment_Current",
    "A_MEAN": "Mean_Wage",
    "A_MEDIAN": "Median_Wage",
    "A_PCT10": "Wage_P10",
    "A_PCT25": "Wage_P25",
    "A_PCT75": "Wage_P75",
    "A_PCT90": "Wage_P90"
})

# Merging roadmap to occupations
roadmap_bls_df = roadmap_df.merge(
    projections_df,
    left_on="SOC2018Code",
    right_on="SOCCode",
    how="left"
)

# Merging the new roadmap/occupation table to the owes table
roadmap_bls_df = roadmap_bls_df.merge(
    oews_df,
    left_on="SOC2018Code",
    right_on="SOCCode",
    how="left",
    suffixes=("_projection", "_oews")
)


# Cleaning and renaming columns to make it easier to understand
final_df = roadmap_bls_df[[
    "CIP2020Code",
    "CIP2020Title",
    "SOC2018Code",
    "SOC2018Title",
    "Employment_Current",
    "Mean_Wage",
    "Median_Wage",
    "Wage_P10",
    "Wage_P25",
    "Wage_P75",
    "Wage_P90",
    "Employment_2024",
    "Employment_2034",
    "Employment_Change",
    "Employment_Growth_Percent",
    "Annual_Openings",
    "Typical_Education"
]].copy()

final_df = final_df.rename(columns={
    "CIP2020Code": "Major_Code",
    "CIP2020Title": "Major",
    "SOC2018Code": "Occupation_Code",
    "SOC2018Title": "Occupation",
    "Employment_Current": "Current_Employment",
    "Mean_Wage": "Mean_Wage",
    "Median_Wage": "Current_Median_Wage",
    "Wage_P10": "Wage_P10",
    "Wage_P25": "Wage_P25",
    "Wage_P75": "Wage_P75",
    "Wage_P90": "Wage_P90"
})

# Saving to files
final_df.to_csv("data/career_roadmap.csv", index=False)
final_df.to_json("data/career_roadmap.json", orient="records")