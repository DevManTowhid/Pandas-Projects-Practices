

import pandas as pd
import random

# Generate dummy data
data = {
    "ID": list(range(1, 51)),
    "Name": [random.choice(["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Hannah", "Isaac", "Jack"]) for _ in range(50)],
    "Age": [random.randint(20, 60) for _ in range(50)],
    "City": [random.choice(["New York", "London", "Berlin", "Tokyo", "Paris", "Toronto", "Sydney", "Dubai"]) for _ in range(50)],
    "Salary": [random.randint(30000, 120000) for _ in range(50)],
    "Department": [random.choice(["HR", "IT", "Finance", "Marketing", "Sales", "Engineering"]) for _ in range(50)]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("large_dummy_data.csv", index=False)

print("CSV file 'large_dummy_data.csv' created successfully!")


# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("dummy_data.csv", index=False)

print("CSV file 'dummy_data.csv' created successfully!")
