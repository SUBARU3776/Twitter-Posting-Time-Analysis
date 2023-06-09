import pandas as pd
import matplotlib.pyplot as plt
import calendar
import random

# Read data and convert Date Created to date/time type
df = pd.read_csv('D:\hogehoge.csv')
df['Date Created'] = pd.to_datetime(df['Date Created'])

# Get the latest date of the data
latest_date = df['Date Created'].max()

# Separate posting date and time
df['date'] = df['Date Created'].dt.date
df['hour'] = df['Date Created'].dt.hour

# Extract data with dates within 30 days
cutoff = latest_date.normalize() - pd.Timedelta(days=29)
counts = df[df['Date Created'] >= cutoff].groupby(['date', 'hour', 'source']).size().reset_index(name='count')

# Count the number of posts per source
source_counts = df[df['Date Created'] >= cutoff].groupby(['source']).size().reset_index(name='total_count')

# Sort by number of posts in descending order
source_counts = source_counts.sort_values(by=['total_count'], ascending=False)

# Calculate the percentage for each source
source_counts['percentage'] = source_counts['total_count'] / source_counts['total_count'].sum() * 100

# Rounded to the second decimal place.
source_counts['percentage'] = source_counts['percentage'].round(2)

# Left-align source column text to match width
width = 20
source_counts['source'] = source_counts['source'].apply(lambda x: x.ljust(width))

# Output results
print(source_counts.to_string(index=False, index_names=False, justify='center'))

# Assign random colors according to source
sources = counts['source'].unique()
color_map = {}
for source in sources:
    color_map[source] = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
counts['color'] = counts['source'].map(lambda x: color_map[x])

# Set the graph drawing area
fig, ax = plt.subplots(figsize=(11,7))

# Set the day of the week and date on the y-axis
dates = pd.date_range(start=cutoff, end=latest_date, freq='D')
weekdays = [calendar.day_name[d.weekday()] for d in dates]
labels = [f'{w[:3]} {d.strftime("%m/%d")}' for d, w in zip(dates, weekdays)]
ax.set_yticks(dates)
ax.set_yticklabels(labels)

# Make the label "Sun" red
sun_indices = [i for i, label in enumerate(labels) if "Sun" in label]
for i in sun_indices:
    ax.get_yticklabels()[i].set_color("red")

# Set labels and colors for each source
for source, color in color_map.items():
    data = counts[counts['source'] == source]
    ax.scatter(data['hour'], data['date'], s=data['count']*50, alpha=0.5, c=color, label=source) # マーカーの大きさを決定

# Add a legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='center left', bbox_to_anchor=(1.0, 0.5))

# Set x-axis label and range
ax.set_xlabel('Hour of the day')
ax.set_xlim(-0.5, 23.5)
ax.set_xticks(range(0, 24))

# Add x-axis grid lines
ax.xaxis.grid(True)

# Set y-axis range
ax.set_ylim(cutoff - pd.Timedelta(hours=12), latest_date + pd.Timedelta(hours=12))

# Add y-axis grid lines
ax.yaxis.grid(True)

# Set the title of the graph
ax.set_title('Tweet activity over time')

plt.show()
