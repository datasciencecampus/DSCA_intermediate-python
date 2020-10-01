
f, ax = plt.subplots(figsize = (6,8))

# aggregate the data
embark = titanic['embarked'].value_counts(normalize = True)

# labels
cities = {'S':'Southampton', 'Q':'Queenstown', 'C':'Cherbourg'}

# plot the data
ax.bar(x = embark.index, 
       height = embark, 
       tick_label = embark.index.map(cities), 
       color = ['#66c2a5','#fc8d62','#8da0cb'])

# decorate the plot
ax.set_ylabel('Proportion of Passengers')
ax.set_title('Proportion of Titanic Passengers by Embarkation City')