import pandas as pd
import os

# Load TSV file
df = pd.read_csv("amazon_reviews_us_Major_Appliances_v1_00.tsv", sep="\t", on_bad_lines="skip")

# Convert to CSV
df.to_csv("major_applicances.csv", index=False)


print("Conversion completed successfully!")

# Load TSV file
df = pd.read_csv("amazon_reviews_us_Electronics_v1_00.tsv", sep="\t", on_bad_lines="skip")

# Convert to CSV
df.to_csv("electronics.csv", index=False)


print("Conversion completed successfully!")

# Load TSV file
df = pd.read_csv("amazon_reviews_us_Personal_Care_Appliances_v1_00.tsv", sep="\t", on_bad_lines="skip")

# Convert to CSV
df.to_csv("personal_care_appliances.csv", index=False)


print("Conversion completed successfully!")

# Load TSV file
df = pd.read_csv("amazon_reviews_us_Furniture_v1_00.tsv", sep="\t", on_bad_lines="skip")

# Convert to CSV
df.to_csv("furniture.csv", index=False)


print("Conversion completed successfully!")

import pandas as pd
import glob

# List of CSV files to merge
csv_files = ["furniture.csv", "electronics.csv", "major_applicances.csv", "personal_care_appliances.csv"]

# Read and concatenate all CSVs into one DataFrame
df = pd.concat([pd.read_csv(file, on_bad_lines="skip") for file in csv_files], ignore_index=True)

# Save the merged dataset as a new CSV
df.to_csv("merged_reviews.csv", index=False)

print("Merged CSV file saved as 'merged_reviews.csv'.")


