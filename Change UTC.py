import pandas as pd
from datetime import timedelta

# データを読み込む
df = pd.read_csv(r'hoge:\hogehoge.csv')

# 'created_at'列を日時型に変換する
df['created_at'] = pd.to_datetime(df['created_at'])

# 日本時間から現地時間に変換する
df['created_at'] = df['created_at'] - timedelta(hours=2)  # 日本時間から時間を引く
df['created_at'] = df['created_at'].dt.tz_localize('Asia/Tokyo')  # 日本時間をタイムゾーンとして設定
df['created_at'] = df['created_at'].dt.tz_convert('hogehoge/hoge')  # 任意の現地時間に変換（例：Europe/Berlin）

# 日付のフォーマットを変更する
df['created_at'] = df['created_at'].dt.strftime("%Y/%m/%d %H:%M:%S")

# 結果を表示する
print(df['created_at'])

# ファイル名を生成する
file_name = pd.Timestamp.now().strftime("%Y%m%d%H%M%S") + "_converted.csv"

# データをCSVファイルとして保存する
df.to_csv(file_name, index=False)
print("変換後のデータをCSVファイルとして保存しました。ファイル名: " + file_name) # ファイル名は適当に指定してください