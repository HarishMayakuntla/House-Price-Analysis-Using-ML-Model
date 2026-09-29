

import pandas as pd
import numpy as np

df=pd.read_csv(r"C:\Users\mayak\OneDrive\Desktop\fastapi\cleaned_house_data.csv")

df.head()

df.shape

df.select_dtypes(include='str').columns

df.select_dtypes(include=np.number).columns

df.isnull().sum()

df.isna().sum()/len(df)*100

df=df.drop('society',axis=1)

df.shape

df['location']=df['location'].fillna(df['location'].mode()[0])
df['size']=df['size'].fillna(df['size'].mode()[0])

Q1=df['bath'].quantile(0.25)
Q3=df['bath'].quantile(0.75)
IQR=Q3-Q1
lower=Q1-1.5*IQR
upper=Q3+1.5*IQR
outliers=df[(df['bath']<lower)|(df['bath']>upper)]
print('25% range:',lower)
print('75% range:',upper)
print('outlier range :',len(outliers))

df['bath'].value_counts()

Q1=df['balcony'].quantile(0.25)
Q3=df['balcony'].quantile(0.75)
IQR=Q3-Q1
lower=Q1-1.5*IQR
upper=Q3+1.5*IQR
outliers=df[(df['balcony']<lower)|(df['balcony']>upper)]
print('25% range:',lower)
print('75% range:',upper)
print('outlier range :',len(outliers))

df['balcony'].value_counts()

df['bath']=df['bath'].fillna(df['bath'].median())
df['balcony']=df['balcony'].fillna(df['balcony'].median())

df.duplicated().sum()

df=df.drop_duplicates()

df.duplicated().sum()

df['location'] = df['location'].str.strip()
df['size'] = df['size'].str.strip()

df['BHK'] = df['size'].str.extract(r'(\d+)').astype(float)

df[['size', 'BHK']].head(10)

def convert_sqft_to_num(x):
    try:
        if '-' in str(x):
            tokens = str(x).split('-')
            return (float(tokens[0]) + float(tokens[1])) / 2

        return float(x)

    except:
        return np.nan

df['total_sqft'] = df['total_sqft'].apply(convert_sqft_to_num)

df['total_sqft'].head(10)

df['total_sqft'].isnull().sum()

df = df.dropna(subset=['total_sqft'])

df['total_sqft'].isnull().sum()

print("BHK <= 0:", (df['BHK'] <= 0).sum())
print("total_sqft <= 0:", (df['total_sqft'] <= 0).sum())
print("bath <= 0:", (df['bath'] <= 0).sum())

df.isnull().sum()

df.duplicated().sum()

df[df.duplicated()]

df=df.drop_duplicates()

df.duplicated().sum()

df.to_csv("cleaned_house_data.csv", index=False)