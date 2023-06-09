import pandas as pd
import matplotlib.pyplot as plt
import calendar
import pytz

# Read data and convert created_at to date/time type
df = pd.read_csv('*:\hoge\hogehoge.csv')
df['created_at'] = pd.to_datetime(df['created_at'], utc=True).dt.tz_convert('Asia/Tokyo')

# Separate posting date and time
df['date'] = df['created_at'].dt.date
df['hour'] = df['created_at'].dt.hour

# Extract data with dates within 30 days
cutoff = pd.Timestamp.now(tz=pytz.timezone('Asia/Tokyo')).normalize() - pd.Timedelta(days=29)
counts = df[df['created_at'] >= cutoff].groupby(['date', 'hour']).size().reset_index(name='count')

# Set the graph drawing area
fig, ax = plt.subplots(figsize=(10,6))

# Set the day of the week and date on the y-axis
cutoff = pd.Timestamp.now(tz=pytz.timezone('Asia/Tokyo')).normalize() - pd.Timedelta(days=29)
dates = pd.date_range(start=cutoff - pd.Timedelta(hours=12), end=pd.Timestamp.now(tz=pytz.timezone('Asia/Tokyo')) + pd.Timedelta(hours=12), freq='D')
weekdays = [calendar.day_name[d.weekday()] for d in dates]
labels = [f'{w[:3]} {d.strftime("%m/%d")}' for d, w in zip(dates, weekdays)]
ax.set_yticks(dates)
ax.set_yticklabels(labels)

# Set the first label to an empty string
labels[0] = ""

ax.set_yticks(dates)
ax.set_yticklabels(labels)

# Make the label "Sun" red
sun_indices = [i for i, label in enumerate(labels) if "Sun" in label]
for i in sun_indices:
    ax.get_yticklabels()[i].set_color("red")

# Plotting.
ax.scatter(counts['hour'], counts['date'], s=counts['count']*20, alpha=0.5)

# Set x-axis label and range
ax.set_xlabel('Hour of the day')
ax.set_xlim(-0.5, 23.5)
ax.set_xticks(range(0, 24))

# Add x-axis grid lines
ax.xaxis.grid(True)

# Set y-axis range
ax.set_ylim(cutoff - pd.Timedelta(hours=12), pd.Timestamp.now(tz=pytz.timezone('Asia/Tokyo')) + pd.Timedelta(hours=12))

# Add y-axis grid lines
ax.yaxis.grid(True)

# Set the title of the graph
ax.set_title('Tweet activity over time')

plt.show()
