
# simple boxplot
f, ax = plt.subplots(figsize = (6,6))

# remove na values
fare = titanic[titanic['fare'].notnull()]

# make a boxplot
grps = fare.groupby('embarked')['fare']

ax.boxplot([grps.get_group('S'),grps.get_group('Q'),grps.get_group('C')],
           labels=['Southampton', 'Queenstown', 'Cherbourg'])

# label the y axis
ax.set_ylabel('Fare');