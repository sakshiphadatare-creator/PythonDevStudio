import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv("secondary data.csv")

# Get column names
x = data.columns[0]
y = data.columns[1]

# Plot a bar chart using the first two columns
plt.bar(data[x], data[y], color="blue")
plt.xlabel(x)
plt.ylabel(y)
plt.title("Bar Chart")
plt.xticks(rotation=45)
plt.show()

# Group pH values into categories
ph_range = pd.cut(data['pH'], bins=[0, 6.5, 7, 7.5, 14], labels=['Acidic', 'Slightly Acidic', 'Neutral', 'Alkaline'])

# Plot pie chart
ph_range.value_counts().plot.pie(autopct='%1.1f%%')
plt.title("pH Range Distribution")
plt.ylabel("")  # Hide y-axis label
plt.show()

# Plot pie chart
data['Source'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("Source Distribution")
plt.ylabel("")
plt.show()

# Plot pie chart
data['Status'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("Water Status Distribution")
plt.ylabel("")
plt.show()
