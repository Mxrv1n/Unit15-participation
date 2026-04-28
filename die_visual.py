import plotly.express as px

from die import Die

#create a D6 
die = Die()

#make some rolls, and store results in a list
results =[]
for roll_num in range(10000000):
    result = die.roll()
    results.append(result)

#analyze results
frequencies = []
toss_results = range(1, die.num_sides + 1)
for value in toss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

#visualize results
fig = px.bar(x=toss_results, y=frequencies)
fig.show()