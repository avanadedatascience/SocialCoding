import seaborn as sns
sns.set(style="whitegrid")

# Load the example Titanic dataset
titanic = pd.read_csv('titanic.csv', sep=',')

# Draw a nested barplot to show survival for class and sex
g = sns.catplot(x="pclass", y="survived", hue="sex", data=titanic,
                height=6, kind="bar", palette="muted")
g.despine(left=True)
g.set_ylabels("survival probability")