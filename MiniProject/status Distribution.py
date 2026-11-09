import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("secondary data.csv")

# Plot pie chart
data['Status'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("Water Status Distribution")
plt.ylabel("")
plt.show()
