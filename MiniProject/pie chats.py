"""import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("secondary data.csv")

# Step 2: Create a 1x3 grid for the remaining pie charts
fig, chart = plt.subplots(1, 3, figsize=(18, 10)) #6

# pH Range
ph_groups = pd.cut(data['pH'], bins=[0, 6.5, 7, 7.5, 14], labels=['Acidic', 'Slightly Acidic', 'Neutral', 'Alkaline'])
ph_groups.value_counts().plot.pie(
    autopct='%1.1f%%', startangle=140, shadow=True
)
chart[0, 1].set_title("pH Range Distribution")

# Source
data['Source'].value_counts().plot.pie(
    autopct='%1.1f%%', startangle=140, shadow=True
)
chart[1, 0].set_title("Source Distribution")

# Status
data['Status'].value_counts().plot.pie(
    autopct='%1.1f%%', startangle=140, shadow=True
)
chart[1, 1].set_title("Water Status Distribution")

plt.tight_layout()
plt.show()"""


import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("secondary data.csv")

# Create one row with 3 pie charts
fig, charts = plt.subplots(1, 3, figsize=(18, 6))

# pH Range chart
ph_range = pd.cut(data['pH'], bins=[0, 6.5, 7, 7.5, 14], labels=['Acidic', 'Slightly Acidic', 'Neutral', 'Alkaline'])
charts[0].pie(ph_range.value_counts(), labels=ph_range.value_counts().index, autopct='%1.1f%%')
charts[0].set_title("pH Range")

# Source chart
charts[1].pie(data['Source'].value_counts(), labels=data['Source'].value_counts().index, autopct='%1.1f%%')
charts[1].set_title("Source")

# Status chart
charts[2].pie(data['Status'].value_counts(), labels=data['Status'].value_counts().index, autopct='%1.1f%%')
charts[2].set_title("Status")

# Show all charts together
plt.tight_layout()
plt.show()