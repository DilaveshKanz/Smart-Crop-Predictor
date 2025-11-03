import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    data=pd.read_csv('dataset.csv')
except FileNotFoundError:
    print("The file 'data.csv' was not found.")
    exit()

print(data.head())
data.info()

print(f"Unique Crops : ({len(data['label'].unique())})")
print(data['label'].unique())

plt.figure(figsize=(18,6))
sns.countplot(y='label' , data=data, palette='magma' , hue='label' , legend=False)
plt.title('Distribution of Crops')
plt.xlabel('Count')
plt.ylabel('Crop')
plt.tight_layout()
plt.savefig('crop_distribution.png')
print("done!")
