import pandas as pd

# Load the dataset
data = pd.read_csv('dataset.csv')

# Drop all columns that contain 'Unnamed' in their name
data = data.drop(columns=data.filter(like='Unnamed').columns)

# Display first 20 rows
print(data.head(20))

# Save cleaned data back to CSV
data.to_csv('dataset.csv', index=False)
