import pandas as pd
import matplotlib.pyplot as plt
import calendar
import pytz

# データを読み込み、created_atを日時型に変換する
df = pd.read_csv('D:\Python\Postman\Hidetoshi_H_.csv')
df['created_at'] = pd.to_datetime(df['created_at'], utc=True).dt.tz_convert('Asia/Tokyo')

# 投稿日と投稿時間を分離する
df['date'] = df['created_at'].dt.date
df['hour'] = df['created_at'].dt.hour

# 日付が30日以内のデータを抽出する
cutoff = pd.Timestamp.now(tz=pytz.timezone('Asia/Tokyo')).normalize() - pd.Timedelta(days=29)
counts = df[df['created_at'] >= cutoff].groupby(['date', 'hour']).size().reset_index(name='count')

# グラフの描画領域を設定する
fig, ax = plt.subplots(figsize=(10,6))

# y軸に曜日と日付を設定する
cutoff = pd.Timestamp.now(tz=pytz.timezone('Asia/Tokyo')).normalize() - pd.Timedelta(days=29)
dates = pd.date_range(start=cutoff - pd.Timedelta(hours=12), end=pd.Timestamp.now(tz=pytz.timezone('Asia/Tokyo')) + pd.Timedelta(hours=12), freq='D')
weekdays = [calendar.day_name[d.weekday()] for d in dates]
labels = [f'{w[:3]} {d.strftime("%m/%d")}' for d, w in zip(dates, weekdays)]
ax.set_yticks(dates)
ax.set_yticklabels(labels)

# 最初のラベルを空の文字列に設定する
labels[0] = ""

ax.set_yticks(dates)
ax.set_yticklabels(labels)

# "Sun"のラベルを赤色にする
sun_indices = [i for i, label in enumerate(labels) if "Sun" in label]
for i in sun_indices:
    ax.get_yticklabels()[i].set_color("red")

# プロットする
ax.scatter(counts['hour'], counts['date'], s=counts['count']*20, alpha=0.5)

# x軸のラベルと範囲を設定する
ax.set_xlabel('Hour of the day')
ax.set_xlim(-0.5, 23.5)
ax.set_xticks(range(0, 24))

# x軸のグリッド線を追加する
ax.xaxis.grid(True)

# y軸の範囲を設定する
ax.set_ylim(cutoff - pd.Timedelta(hours=12), pd.Timestamp.now(tz=pytz.timezone('Asia/Tokyo')) + pd.Timedelta(hours=12))

# y軸のグリッド線を追加する
ax.yaxis.grid(True)

# グラフのタイトルを設定する
ax.set_title('Tweet activity over time')

plt.show()