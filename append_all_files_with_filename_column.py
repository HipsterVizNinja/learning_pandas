import pandas as pd
import glob

df_all = pd.DataFrame()

for f in glob.glob("input wild card file/path"):

    df = pd.read_csv(f, header=None) # make sure to apply correct settings (sep, parse_dates, headers, missing_values)
    df["origin"] = f #add a column with a csv name
    df_all = df_all.append(df) #append new df to the "master" dataframe

    df_all.to_csv("output file")
    print(f)
