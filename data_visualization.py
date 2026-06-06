import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books_dataset.csv")

# Count ratings
rating_counts = df["Rating"].value_counts()

# Create bar chart
plt.figure(figsize=(8,5))
rating_counts.plot(kind="bar")

plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.tight_layout()

# Save chart
plt.savefig("rating_distribution.png")

plt.show()

print("Visualization created successfully!")