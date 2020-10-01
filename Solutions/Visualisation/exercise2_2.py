
# create child variable
titanic['child'] = (titanic['age'] < 18).astype(int)

# create a figure and an axis instance
fig, ax = plt.subplots(figsize=(8,4))

# Get survivor proportions by passenger classes
titanic.groupby('child')['survived'].mean().plot(kind='bar', color = ['hotpink','goldenrod'], ax=ax)

# Decorate
ax.set_title('Titanic Passenger Survival by Age Group')
ax.set_ylabel('Proportion of Passengers Survived')
ax.set_xlabel('Age Group')
ax.set_xticklabels(['Adult', 'Child'], rotation = 0);