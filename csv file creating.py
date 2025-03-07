import pandas as pd

# Create dummy data
data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [25, 30, 22, 35, 28],
    "City": ["New York", "London", "Berlin", "Tokyo", "Paris"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("dummy_data.csv", index=False)

print("CSV file 'dummy_data.csv' created successfully!")
