import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("secondary data.csv")

# Plot a bar chart using the first two columns
x = df.columns[0]
y = df.columns[1]

plt.bar(df[x], df[y], color="blue")
plt.xlabel(x)
plt.ylabel(y)
plt.title("Bar Chart")
plt.xticks(rotation=45)
plt.show()


# Show first 5 rows
#print(df.head())