import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pathlib
import itertools

# https://python-charts.com/seaborn/themes/
sns.set_style(style='darkgrid')

# Load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris = pd.read_csv(url, header=None, names=columns)

# write dataset to csv
iris.to_csv('iris.csv', index=False)

# write variable summary to file as markdown table
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_markdown.html
iris.describe(include='all').to_markdown('iris_description.md')

chart_folder = pathlib.Path('charts')
if not chart_folder.exists():
    chart_folder.mkdir()

columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
names = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']

for column, name in zip(columns, names):
    plt.figure(figsize=(12,8))
    sns.histplot(iris[column], bins=20)
    plt.title(f'Histogram of {name}')
    plt.xlabel(f'{name} (cm)')
    plt.ylabel('Frequency')
    plt.savefig(chart_folder/f'{column}_histogram.png')
    plt.close()

# all in one pairplot of histograms and scatterplots
# https://seaborn.pydata.org/generated/seaborn.pairplot.html
plt.figure(figsize=(12,8))
sns.pairplot(iris, hue='species')
plt.savefig(chart_folder/'paired_scatterplot.png')
plt.close()

# scatterplot for each combination of 2 variables
# destructure the pairs of (name, column) tuples into sets of 1 and 2
# https://docs.python.org/3/library/itertools.html#itertools.combinations
for (name1, col1), (name2, col2) in itertools.combinations([*zip(names, columns)], 2):
    plt.figure(figsize=(12,8))
    sns.scatterplot(data=iris, x=col1, y=col2, hue='species')
    plt.title(f'Scatterplot of {name1} vs {name2}')
    plt.xlabel(f'{name1} (cm)')
    plt.ylabel(f'{name2} (cm)')
    plt.savefig(chart_folder/f'{col1}_vs_{col2}.png')
    plt.close()
