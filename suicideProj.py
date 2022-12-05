import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gdp_country = pd.read_csv(r"C:\Users\cash america\Downloads\csvData (1).csv")
suicide_country = pd.read_csv(r"C:\Users\cash america\Downloads\csvData.csv")


dataset = gdp_country.merge(suicide_country, on='country', how='inner')[['country', 'rate2019both', 'rate2019female','rate2019male', 'gdpPerCapita']]
dataset['menToWomen'] = dataset['rate2019male'] / dataset['rate2019female']
dataset_clean = dataset.sort_values(by='rate2019both', ascending=False).head(25)

plt.clf()
choose_data = dataset_clean
sns.set_palette('Purples')

sns.barplot(choose_data, x='country', y='rate2019both')
plt.setp(sns.barplot(choose_data, x='country', y='rate2019both').get_xticklabels(), rotation=90)




plt.show()
