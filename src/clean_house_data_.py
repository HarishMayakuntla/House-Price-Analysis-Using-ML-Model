

import pandas as pd
import numpy as np

df=pd.read_csv(r"C:\Users\mayak\OneDrive\Desktop\fastapi\cleaned_house_data.csv") # load data

df.head()  # check the dataset

df.shape #  include the dimenstions

df.select_dtypes(include='str').columns # categorical features

df.select_dtypes(include=np.number).columns  # numeric Features

df.isnull().sum() # check null values

df.isna().sum()/len(df)*100 # percentage of null values 

df=df.drop('society',axis=1) # drop unnessery feature

df.shape # check again dimentions

# fill null values using mode method for categorical columns
df['location']=df['location'].fillna(df['location'].mode()[0])
df['size']=df['size'].fillna(df['size'].mode()[0])

# explore  and  check with outliers and use mean or median methods to solve null values 

df['bath'].mean()  # usin mean check outlier is near to outlier or not

# check outlier of bath feature

Q1=df['bath'].quantile(0.25)
Q3=df['bath'].quantile(0.75)
IQR=Q3-Q1
lower=Q1-1.5*IQR
upper=Q3+1.5*IQR
outliers=df[(df['bath']<lower)|(df['bath']>upper)]
print('25% range:',lower)
print('75% range:',upper)
print('outlier range :',len(outliers))

# check outlier of balcony feature

Q1=df['balcony'].quantile(0.25)
Q3=df['balcony'].quantile(0.75)
IQR=Q3-Q1
lower=Q1-1.5*IQR
upper=Q3+1.5*IQR
outliers=df[(df['balcony']<lower)|(df['balcony']>upper)]
print('25% range:',lower)
print('75% range:',upper)
print('outlier range :',len(outliers))

# so, here the outliers are there is no relation with mean methods so we can use median fill null values 

df['bath']=df['bath'].fillna(df['bath'].median())
df['balcony']=df['balcony'].fillna(df['balcony'].median())

df.duplicated().sum() #  check duplicates values

df=df.drop_duplicates() # remove duplicates values

df.duplicated().sum() # again check it once there duplicate values hava or not

# remove extra white spaces to avoid minor issues
df['location'] = df['location'].str.strip()
df['size'] = df['size'].str.strip()

# create new feature to change str to float like 2BHk to 2.0 for machine easy to understand
df['BHK'] = df['size'].str.extract(r'(\d+)').astype(float)

# check comparision with new created feature and previous one
df[['size', 'BHK']].head(10)

# here feature contain the range like 2000-35000 like here we do avarage and take as avarage value
def convert_sqft_to_num(x):
    try:
        if '-' in str(x):
            tokens = str(x).split('-')
            return (float(tokens[0]) + float(tokens[1])) / 2

        return float(x)

    except:
        return np.nan

df['total_sqft'] = df['total_sqft'].apply(convert_sqft_to_num)  # apply  function to  feature 

df['total_sqft'].head(10) # check where it change or not

df['total_sqft'].isnull().sum()  # after modification there is a chance to crate some null , duplicate values   

df = df.dropna(subset=['total_sqft']) # check remove null values there no use with research don't do blindly 

df['total_sqft'].isnull().sum() #  check it once

# here i check any negive relatio with features 

print("BHK <= 0:", (df['BHK'] <= 0).sum())
print("total_sqft <= 0:", (df['total_sqft'] <= 0).sum())
print("bath <= 0:", (df['bath'] <= 0).sum())

df.isnull().sum() # finally once we need to check null values

df.duplicated().sum() # finally once we need to check duplicated values

df[df.duplicated()] # check where it spefically there

df=df.drop_duplicates() # if some duplicates exists remove 

df.duplicated().sum() # finally check the duplicates

df.to_csv("cleaned_house_data.csv", index=False) # save toanother csv to ferform next ones
