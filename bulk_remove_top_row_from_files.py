import pandas as pd

directory = 'file directory'
os.chdir(directory)
for filename in glob('*.csv'):
    df = pd.read_csv(filename)

    df = df.iloc[1:]

    df.to_csv('file-path'+filename+'_clean.csv', index = False, header=False)

    print(filename)
