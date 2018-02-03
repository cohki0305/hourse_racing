import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('./data/tips.csv',index_col='UID',encoding = "ISO-8859-1")
cat_var = df.dtypes.loc[df.dtypes=='object'].index
df[cat_var].apply(lambda x: len(x.unique()))

le = LabelEncoder()
le.fit(df)
# for var in cat_var:
#     df[var] = le.fit_transform(df[var])

def data():
    X = df[['Tipster', 'Track', 'Horse', 'Bet Type', 'Odds']]
    y = df.Result.values
    return X, y
