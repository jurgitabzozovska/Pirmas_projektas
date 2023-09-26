import seaborn as sns
from bs4 import BeautifulSoup
import requests
import pandas as pd
import psycopg2
import numpy as np
import matplotlib.pyplot as plt

# BARPLOT
# df = pd.DataFrame({"category": ["a", "b", "a", "b"], "reiksme":[1,2,3,4]})
# sns.barplot(data=df, x = "category", y = "reiksme")
# plt.show()

# LINEPLOT
# df = pd.DataFrame({"category": ["a", "b", "a", "b"], "reiksme":[1,2,3,4]})
# sns.lineplot(data= df, x = "category", y = "reiksme")
# plt.show()

# COUNTPLOT
# df = pd.DataFrame({"category": ["a", "b", "a", "b"], "reiksme":[1,2,3,4]})
# sns.countplot(data = df, y = "reiksme")
# plt.show()

# BOXPLOT
# df = pd.DataFrame({"category": ["a", "b", "a", "b"], "reiksme":[1,2,3,4]})
# sns.boxplot(data= df, x = "category", y = "reiksme")
# plt.show()

# PAIRPLOT
# df = pd.DataFrame({"category": ["a", "b", "a", "b"], "reiksme":[1,2,3,4]})
# sns.pairplot(df)
# plt.show()

# KAZKAS NEGERAI
# df = pd.DataFrame({"category": ["a", "b", "a", "b"], "reiksme":[1,2,3,4]})
# sns.lmplot(data= df, x = "category", y = "reiksme")
# plt.show()

# HEATMAP
# df2=np.random.rand(5,4)
# sns.heatmap(df2, annot=True, cmap="coolwarm")
# plt.show()

# data = sns.load_dataset("tips")
# sns.histplot(data=data, x="total_bill", kde=True)
# plt.show()