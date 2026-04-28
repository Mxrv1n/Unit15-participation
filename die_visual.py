import plotly.express as px

from die import Die

#create a D6 
die1 = Die()
die2 = Die(10)

#make some rolls, and store results in a list
results =[]
number_of_rolls = 50_000
for roll_num in range(number_of_rolls):
    result = die1.roll() + die2.roll()
    results.append(result)

#analyze results
frequencies = []
max_result = die1.num_sides + die2.num_sides
toss_results = range(2, max_result + 1)
for value in toss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

#visualize results
title= f"Results of rolling two D6 {number_of_rolls:,} times"
labels = {'x': 'Result', 'y': 'Frequency'}
fig = px.bar(x=toss_results, y=frequencies, title=title, labels=labels)

#further customize chart
fig.update_layout(xaxis_dtick=1)

fig.write_html('die_visual_d6d10.html')
fig.show()