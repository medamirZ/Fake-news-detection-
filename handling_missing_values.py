import pandas as pd
import numpy as np
from merge_data import merged_df

def handle_speaker_job_title(df) :
    speaker_group = df.groupby('Speaker')
    trump_speaker_group = speaker_group.get_group('donald-trump')
    obama_speaker_group = speaker_group.get_group('barack-obama')
    clinton_speaker_group = speaker_group.get_group('hillary-clinton')
    romney_speaker_group = speaker_group.get_group('mitt-romney')
    mccain_speaker_group = speaker_group.get_group('john-mccain')
    print(mccain_speaker_group[['Speaker','Speaker Job Title']].value_counts())
    
def handle_missing_speaker_job_title(df):
    missing_speaker_job_grp = df.groupby('Speaker')
    print(f"Sum : {df['Speaker Job Title'].isna().sum()}") #3568
    df.fillna({'Speaker Job Title':'Unknown'}, inplace=True)
    print(f"Sum : {df['Speaker Job Title'].isna().sum()}") #0 all NA values replaced with 'Unknown'
    #Now get Unknown values
    filt = df['Speaker Job Title'] == 'Unknown'
    print(df.loc[filt, ['Id','Speaker','Speaker Job Title']])
    #group by Unknown Speaker Job Title
    speaker_job_grp = df.groupby('Speaker Job Title')
    uknown_grp = speaker_job_grp.get_group('Unknown')
    print(uknown_grp[['Id','Speaker','Speaker Job Title']].value_counts())
    


def get_speaker_value_counts(df):
    print("\nSpeaker Value Counts:")
    print(df['Speaker'].value_counts())

# get_speaker_value_counts(merged_df)
# handle_speaker_job_title(merged_df)

handle_missing_speaker_job_title(merged_df)