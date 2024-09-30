import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the dataset
file_path = r'C:/Users/Raymond/Desktop/Machine Learning/online+retail+ii/online_retail_II.csv'
df = pd.read_csv(file_path)

# Calculate the mode of the 'Customer ID' column
customer_id_mode = df['Customer ID'].mode()[0]

# Fill missing values in the 'Customer ID' column with the mode
df['Customer ID'].fillna(customer_id_mode, inplace=True)

# Capitalize all letters in the 'Description' column
df['Description'] = df['Description'].str.upper()

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert negative values to positive in 'Quantity' and 'UnitPrice' columns
df['Quantity'] = df['Quantity'].abs()
df['Price'] = df['Price'].abs()

# Convert 'InvoiceDate' to datetime format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create additional features: year, month, day, and time
df['InvoiceDate2'] = df['InvoiceDate'].dt.strftime('%Y-%m-%d')
df['InvoiceTime'] = df['InvoiceDate'].dt.time

# Drop the original 'InvoiceDate' column
df.drop(columns=['InvoiceDate'], inplace=True)

# One-hot encode the 'Country' column
df = pd.get_dummies(df, columns=['Country'], drop_first=True)

# Save the cleaned dataset back to a CSV file
cleaned_file_path = r'C:/Users/Raymond/Desktop/Machine Learning/online+retail+ii/online_retail_II_cleaned.csv'
df.to_csv(cleaned_file_path, index=False)

print("Missing 'Customer ID' values have been filled with the mode, 'Description' column capitalized, negative values converted to positive, duplicates removed, date-time features added, 'Country' field one-hot encoded, and saved to a new file.")