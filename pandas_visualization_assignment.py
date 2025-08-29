# ===============================
# 📊 Data Analysis & Visualization Assignment
# ===============================

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# Task 1: Load and Explore Dataset
# ===============================

try:
    # Option 1: Load your own CSV file
    # df = pd.read_csv("your_dataset.csv")

    # Option 2: Use sklearn's Iris dataset (built-in for easy access)
    from sklearn.datasets import load_iris
    iris = load_iris(as_frame=True)
    df = iris.frame

    print("✅ Dataset loaded successfully!")
except FileNotFoundError:
    print("❌ Error: The dataset file was not found.")
except Exception as e:
    print(f"❌ An error occurred: {e}")

# Show first rows
print("\nFirst 5 rows of the dataset:")
display(df.head())

# Data types & missing values
print("\nDataset info:")
print(df.info())

print("\nMissing values check:")
print(df.isnull().sum())

# ===============================
# Task 2: Basic Data Analysis
# ===============================

# Basic statistics
print("\nBasic statistics:")
display(df.describe())

# Group by species and compute mean
print("\nMean values per species:")
grouped = df.groupby("target").mean()
display(grouped)

# Pattern/observation (printed as text)
print("\nObservation: Different iris species have distinct average petal/sepal sizes.")

# ===============================
# Task 3: Data Visualization
# ===============================

# 1. Line chart (example: petal length over index, per species)
plt.figure(figsize=(8,5))
for species in df["target"].unique():
    species_data = df[df["target"] == species]
    plt.plot(species_data.index, species_data["petal length (cm)"], label=f"Species {species}")
plt.title("Petal Length Trend per Species")
plt.xlabel("Index")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart (average petal length per species)
plt.figure(figsize=(6,4))
sns.barplot(x="target", y="petal length (cm)", data=df, ci=None)
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal length)
plt.figure(figsize=(6,4))
plt.hist(df["sepal length (cm)"], bins=15, edgecolor="black")
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (sepal length vs petal length)
plt.figure(figsize=(6,4))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="target", data=df, palette="deep")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
