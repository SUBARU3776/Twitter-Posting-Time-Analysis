import pandas as pd
from datetime import timedelta

# Read data
df = pd.read_csv(r'hoge:\hogehoge.csv')

# 'created_at'列を日時型に変換する
df['created_at'] = pd.to_datetime(df['created_at'])

# 日本時間から現地時間に変換する
df['created_at'] = df['created_at'] - timedelta(hours=**)  # Subtract time difference from Japan time
df['created_at'] = df['created_at'].dt.tz_localize('Asia/Tokyo')  # Set Japan time as time zone
df['created_at'] = df['created_at'].dt.tz_convert('hogehoge/hoge')  # Convert to any local time (e.g. Europe/Berlin)

# Change the date format
df['created_at'] = df['created_at'].dt.strftime("%Y/%m/%d %H:%M:%S")

# Display results
print(df['created_at'])

# generate a file name
file_name = pd.Timestamp.now().strftime("%Y%m%d%H%M%S") + "_converted.csv"

# Save data as a CSV file
df.to_csv(file_name, index=False) # Please specify the file name as appropriate.
print("Saved converted data as CSV file. File name:" + file_name) 
