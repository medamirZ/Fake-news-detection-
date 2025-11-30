import pandas as pd 
import numpy as np
from dataset_description import df_train, df_validation, df_test, columns

df_test.columns = columns
df_train.columns = columns
df_validation.columns = columns

def merge_datasets(df1, df2, df3):
    merged_df = pd.concat([df1, df2, df3], ignore_index=True)
    return merged_df

merged_df = merge_datasets(df_train, df_validation, df_test)
# print("Merged Dataset:")
# print(merged_df.shape)
