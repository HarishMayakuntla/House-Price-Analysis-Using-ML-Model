# Data Dictionary 

## Dataset: Bengaluru House Data

This data dictionary describes the variables used in the 
Bengaluru House Price Prediction Project.

| Column | Data Type | Description |
|--------|-----------|-------------|
| `area_type` | Categorical | Type of area measurement used for the property |
| `availability` | Categorical | Availability status of the property |
| `location` | Categorical | Location of the property |
| `size` | Categorical | Property size, usually represented in BHK |
| `society` | Categorical | Name of the society or residential community |
| `total_sqft` | Numerical / Text | Total area of the property in square feet |
| `bath` | Numerical | Number of bathrooms |
| `balcony` | Numerical | Number of balconies |
| `price` | Numerical | Property price |

## Target Variable

`price`

The objective of this project is to predict the price of a
house based on the available property features.

## Categorical Features

- `area_type`
- `availability`
- `location`
- `size`
- `society`

## Numerical Features

- `total_sqft`
- `bath`
- `balcony`

## Notes

- Some columns may contain missing values.
- The `size` column can be transformed to extract BHK.
- The `total_sqft` column may require data cleaning.
- Categorical features will be encoded before model training.
