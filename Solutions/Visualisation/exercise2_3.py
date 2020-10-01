
f, ax = plt.subplots(figsize=(10,6))

# Make histogram, 25 bins looks reasonable.
ax.hist(titanic['age'], bins = 25, color = 'coral')

# decorate
ax.set_ylabel('Frequency')
ax.set_xlabel('Passenger Age')
ax.set_title('Age Distribution of Titanic Passengers')