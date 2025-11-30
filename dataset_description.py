import pandas as pd
import numpy as np

df_test = pd.read_csv('dataset/test.tsv', sep='\t',header=None)
df_train = pd.read_csv('dataset/train.tsv', sep='\t',header=None)
df_validation = pd.read_csv('dataset/valid.tsv', sep='\t',header=None)

dataset_description = "A BENCHMARK DATASET FOR FAKE NEWS DETECTION"
dataset_source = "LIAR dataset from https://www.cs.ucsb.edu/~william/data/liar_dataset.zip"

columns = pd.Series([
    'Id',
    'Label',
    'Statement',
    'Subject',
    'Speaker',
    'Speaker Job Title',
    'State Info',
    'Party Affiliation',
    'Barely True Counts',
    'False Counts',
    'Half True Counts',
    'Mostly True Counts',
    'Pants on Fire Counts',
    'Context',

])

def describe_dataset(df, name):
    print("The dataset is divided into three parts: training, validation, and test sets.")
    print(f"Dataset source {dataset_source}")
    print(f"{name} set:")
    print(f"Number of samples: {len(df)}")

def format(df,name): 
    print(f"\n{name} set:")
    print(df.head())
    print(f'df.shape: {df.shape}')
    print("\nStatistical summary:")
    print(df.describe(include='all'))

def understand_data(df,name):
    print(f"\n{name} set:")
    print("Columns and their data types:")
    print(columns)
    print(df.isnull().sum())



    
# format(df_train,"Training")
# understand_data(df_train,"Training")