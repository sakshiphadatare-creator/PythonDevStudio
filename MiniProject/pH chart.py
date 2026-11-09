import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("secondary data.csv")

# Group pH values into categories
ph_range = pd.cut(data['pH'], bins=[0, 6.5, 7, 7.5, 14], labels=['Acidic', 'Slightly Acidic', 'Neutral', 'Alkaline'])

# Plot pie chart
ph_range.value_counts().plot.pie(autopct='%1.1f%%')
plt.title("pH Range Distribution")
plt.ylabel("")  # Hide y-axis label
plt.show()
