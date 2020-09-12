
import pandas as pd
pd.options.mode.chained_assignment = None


def cleanupDF(table):
    df = table.df
    # Read and clean column names
    title = df.iloc[0]
    years = [i.split('\n')[-1] for i in title[1:]]
    labels = [title[0]]
    labels.extend(years)
    # Changing column names
    df.columns = labels
    # Deleting first row (now column names)
    df = df[1:]
    # Setting the first column as index
    cleanCounty = df['County'].map(lambda x: x.replace('\n', ''))
    df['County'] = cleanCounty
    df = df.set_index(df.columns[0])
    # Delete 'Total' row
    if (df.index == 'Total').any():
        df = df.drop('Total')
    # Return cleaned up DF
    return df