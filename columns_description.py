import pandas as pd
import numpy as np
from merge_data import merged_df

def overview_merged_dataset(merged_df):
    print("Merged Dataset Overview:")
    print(merged_df.head())
    print(f"Merged dataset shape: {merged_df.shape}") #(12791, 14)
    print("Infos about the columns : ")
    print(merged_df.info())

#calculating null values in each column
def null_values_summary(merged_df):
    print("\nNull values in each column:")
    print(merged_df.isnull().sum())


def understand_columns_values(merged_df,column_name):
    print(f"\nUnique values for the column {column_name}:")
    print(merged_df[column_name].value_counts())

#loop through all cols
# for col in merged_df.columns:
#     understand_columns_values(merged_df, col)

def identify_null_values(df,col_name):
    filt = df[col_name].isnull() == True
    print(f"\nRows with null values in column {col_name}:")
    print(df.loc[filt,['Id',col_name]])

#identify float columns 

def float_columns_summary(merged_df):
    float_cols = merged_df.select_dtypes(include=['float64']).columns
    print("\nFloat columns summary:")
    for col in float_cols:
        print(f"{col}:")
        print(merged_df[col].describe())
        print("Missing values :")
        identify_null_values(merged_df, col)

# for col in merged_df.select_dtypes(include=['float64']).columns:
#     identify_null_values(merged_df, col)

# float_columns_summary(merged_df)
# null_values_summary(merged_df)

def check_duplicates(df,col_name):
    duplicates = df[col_name].duplicated().any()
    print(f"\nDuplicate counts based on column {col_name}:")
    print(duplicates)

# for col in merged_df.columns:
#     check_duplicates(merged_df, col)

#find duplicate rows based on all columns except 'Id'
# print(merged_df.drop(columns=['Id']).duplicated().sum()) #=> 1
# filt_dup_rows = merged_df.drop(columns=['Id']).duplicated(keep=False) #keep = false to not just show one instance of duplicates
# print(merged_df[filt_dup_rows])