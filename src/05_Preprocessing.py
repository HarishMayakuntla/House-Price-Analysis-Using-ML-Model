import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import OneHotEncoder,StandardScaler 
from sklearn.compose import ColumnTransformer

df=pd.read_csv(r"C:\Users\mayak\OneDrive\Desktop\fastapi\feature_engineered_data.xls") # load data, before we done cleaned_dataset to create feature_engineering_data

df.head() # check the top five rows for data understanding

df.shape # check the dimentions

x=df.drop('price',axis=1) # create the input features
y=df['price'] # create output(target) feature

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42) # split the data for training ,testing 

num_cols=x.select_dtypes(include=np.number).columns # separate numeric features for scaling
num_cols

cat_cols=x.select_dtypes(include='str').columns # separate the catogorical featues for encoding why machine cannot understands text so we convert matric
cat_cols

preprocessing=ColumnTransformer(        # using to appaly preprocessing techniques to different columns of dataset
    transformers=[
        ('numerical',StandardScaler(),num_cols),
        ('catogirical',OneHotEncoder(handle_unknown='ignore'),cat_cols)
    ]
)

# i check here to it follows same shape or different
print("X_train:", x_train.shape)
print("X_test :", x_test.shape)
print("y_train:", y_train.shape)
print("y_test :", y_test.shape)


x_train_processed=preprocessing.fit_transform(x_train)  #the model should learn from the train data
x_test_processed=preprocessing.transform(x_test) # here same but only transform the same data


# again chech it's shape for clarity about any changes occurs or not
print("X_train_processed:", x_train_processed.shape)
print("X_test_processed :", x_test_processed.shape)

print("y_train:", y_train.shape)
print("y_test :", y_test.shape)

# i created a dataframe to save the data
X_train_processed_df = pd.DataFrame(
    x_train_processed
)

X_test_processed_df = pd.DataFrame(
    x_test_processed
)


# save the train test data as a csv files to perform next problems
X_train_processed_df.to_csv(
    "X_train_processed.csv",
    index=False
)

X_test_processed_df.to_csv(
    "X_test_processed.csv",
    index=False
)

y_train.to_csv(
    "y_train.csv",
    index=False
)

y_test.to_csv(
    "y_test.csv",
    index=False
)

