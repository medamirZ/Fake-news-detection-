from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from merge_data import merged_df

float_cols = merged_df.select_dtypes(include=['float64']).columns

def plott(df,col) :
    
        plt.figure(figsize=(8, 6))
        plt.hist(df[col].dropna(), bins=30, color='blue', alpha=0.7)
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.grid(axis='y', alpha=0.75)
        plt.show()
        
plott(merged_df,'Barely True Counts')