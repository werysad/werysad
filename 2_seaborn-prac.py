import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())
sns.lineplot(x="tip", y="total_bill", data=tips)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())
#shows gender male female diff colour 
sns.lineplot(x="tip", y="total_bill", data=tips,
             hue="sex", style="sex", markers=True)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())
#shows grouped gender male female diff colour without maker
sns.lineplot(x="tip", y="total_bill", data=tips, hue="sex")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())
sns.histplot(data=tips['tip'], kde=True)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())
#barplot 
sns.barplot(x='sex', y='tip', data=tips)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())

#boxplot 
sns.boxplot(x='day', y='tip', data=tips, hue='sex')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())
#scatter plot 
sns.scatterplot(x='tip', y='total_bill', data=tips)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())
#strip plot
sns.stripplot(x='day', y='tip', data=tips, hue='sex', dodge=True)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
#heatmap
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='Purples')

plt.show()
