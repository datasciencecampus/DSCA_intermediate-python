
# Stage 1

# make pclass_count object
pclass_count = titanic['pclass'].value_counts()

# Make figure and axis
f, ax = plt.subplots(figsize = (8,8))

# Plot pie chart (comment out to avoid overlapping pie charts)
ax.pie(pclass_count, labels = pclass_count.index)

# Stage 2

ax.pie(pclass_count,
       labels = pclass_count.index,
       textprops = {'fontsize':12},
       colors = ['#a6cee3','#1f78b4','#b2df8a'],
       autopct = '%.1f')

ax.set_title("Titanic Passengers by Passenger Class")

# Stage 3

# Save the figure
f.savefig('../Save/pie_chart.png',dpi=200,bbox_inches='tight')