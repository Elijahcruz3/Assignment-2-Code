#Course Grade Stats

import pandas as pd

# Specify the filename directly
file_name = 'StudentInfo_test1.tsv'

# TODO: Read in file_name as a dataframe
def read_data(file_name):
    return pd.read_csv(file_name, sep='\t')

# TODO: Output the max scores of each assignment
def get_max_scores(df):
    return df.max(numeric_only=True).to_string()

# TODO: Output the median scores of each assignment
def get_median_scores(df):
    return df.median(numeric_only=True).to_string()

# TODO: Output the average scores of each assignment
def get_average_scores(df):
    return df.mean(numeric_only=True).to_string()

# TODO: Output the standard deviation of each assignment
def get_std_deviation(df):
    return df.std(numeric_only=True).to_string()

# Read the data
df = read_data(file_name)

# TODO: Output rows by descending Final scores
sorted_df = df.sort_values(by='Final', ascending=False)
print(sorted_df.to_string(index=False))

print("\nMax Scores:")
print(get_max_scores(df))

print("\nMedian Scores:")
print(get_median_scores(df))

print("\nAverage Scores:")
print(get_average_scores(df))

print("\nStandard Deviation:")
print(get_std_deviation(df))