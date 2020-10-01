
# sharey as both axis will be survived proportion.
f, (ax1, ax2) = plt.subplots(1,2,figsize=(12,6), sharey = True)

# Plot ax1
titanic.groupby('child')['survived'].mean().plot(kind='bar', ax=ax1)
# decorate ax1
ax1.set_xticklabels(['Adult','Child'], rotation = 0)
ax1.set_xlabel('Age Group')
ax1.set_ylabel('Proportion of Passengers who Survived')

# Plot ax2
titanic['lone_passenger'] = ((titanic['sibsp'] == 0) & (titanic['parch'] == 0)).astype(int)
titanic.groupby('lone_passenger')['survived'].mean().plot(kind='bar', color = ['darkcyan','deeppink'], ax=ax2)
# decorate ax2
ax2.set_xticklabels(['Passenger in Group','Lone Passenger'], rotation = 0)
ax2.set_xlabel('Passenger Status')

# Add a figure title
f.suptitle("Titanic Survival by Passenger Age and by Group Status");