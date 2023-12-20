import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
species_info = pd.read_csv('species_info.csv')
observations = pd.read_csv('observations.csv')

print(species_info.head())
print(species_info.info())
print(species_info.isnull().sum())
print(species_info['category'].unique())
print(species_info['category'].value_counts())
# Vascular Plant = 4470, Bird = 521, Nonvascular Plant = 333, Mammal = 214, Fish = 127, Amphibian = 80, Reptile = 79

print(observations.head())
print(observations.info())
print(observations.describe())
# Count = 23296
print(observations.isnull().sum())
print(observations['park_name'].unique())
print(observations['park_name'].value_counts())
# Great Smoky Mountains, Yosemite, Bryce, Yellowstone National Parks = 5824 each

# Data Visualizaiton of species
category_counts = species_info['category'].value_counts()
plt.figure(figsize=(8, 6))
category_counts.plot(kind='bar', color='green')
plt.title('Distribution of Species Categories')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Pie Chart to better understand proportions of species
df = pd.read_csv('species_info.csv')
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Categories', pad=20)  
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.axis('equal') 
plt.tight_layout()
plt.show()

# Histogram to visualize distribution of observations across all parks
total_observations = observations.groupby('park_name')['observations'].sum()
plt.figure(figsize=(8, 6))
total_observations.plot(kind='bar', color='skyblue')
plt.xlabel('Park Name')
plt.ylabel('Total Observations')
plt.title('Histogram of Total Observations Across Parks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Histogram of each park
park_A = observations[observations['park_name'] == 'Great Smoky Mountains National Park']['observations']
park_B = observations[observations['park_name'] == 'Yosemite National Park']['observations']
park_C = observations[observations['park_name'] == 'Bryce National Park']['observations']
park_D = observations[observations['park_name'] == 'Yellowstone National Park']['observations']

plt.figure(figsize=(10, 6))
plt.hist([park_A, park_B, park_C, park_D], bins=100, alpha=0.7, label=['Great Smoky Mountains National Park', 'Yosemite National Park', 'Bryce National Park', 'Yellowstone National Park'])
plt.xlabel('Number of Observations')
plt.ylabel('Frequency')
plt.title('Distribution of Observations across Parks')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# We can perform an inner merge on two dfs, since they share scientific name column for each specie.
merged_df = pd.merge(observations, species_info, on='scientific_name', how='left')
print(merged_df.head())
print(merged_df.columns.tolist())
category_counts = merged_df.groupby(['park_name', 'category']).size().unstack()
plt.figure(figsize=(10, 6))
categories = category_counts.columns.tolist()
num_categories = len(categories)
bar_width = 0.8 / num_categories 

for i, category in enumerate(categories):
    positions = [x + i * bar_width for x in range(len(category_counts.index))]
    plt.bar(positions, category_counts[category], width=bar_width, label=category)
custom_labels = ['Bryce', 'Yellowstone', 'Yosemite', 'Grand Canyon']

plt.xticks([r + (0.8 / 2) for r in range(len(category_counts.index))], custom_labels, rotation=45)
plt.title('Count of Species Categories in Each Park')
plt.xlabel('Park Name')
plt.ylabel('Count')
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')  # Place legend outside the plot
plt.tight_layout()
plt.show()
