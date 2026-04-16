import seaborn as sns
import matplotlib.pyplot as plt

data=sns.load_dataset("titanic")
print(data.head())

sns.countplot(data["sex"],palette="winter")
plt.show()

sns.countplot(data["class"], palette="husl")
plt.show()

sns.countplot(data=data,x="sex",hue="survived",palette="spring")
plt.show()

sns.countplot(data=data,x="class",hue="survived",palette="autumn")
plt.show()

sns.heatmap(data.corr(numeric_only=True),cmap="viridis")
plt.show()

data.hist(figsize=(12,12))
plt.show()

sns.barplot(data=data,x="embark_town",y="fare")
plt.show()