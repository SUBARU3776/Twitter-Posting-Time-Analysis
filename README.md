# Twitter-Posting-Time-Analysis
### このスクリプトは、Twitterのツイート投稿データを読み込み、最近30日間の投稿の時間帯と日付に基づいて散布図を作成するものです。

##### 具体的には、以下のような処理を行っています。

- pandasライブラリをインポートし、matplotlib.pyplot、calendar、pytzもインポートする
- Twitterのツイート投稿データをcsv形式で読み込む
- 投稿日時を日本時間に変換する
- 投稿日と投稿時間を分離する
- 30日以内のデータを抽出する
- グラフの描画領域を設定する
- y軸に曜日と日付を設定する
- 日曜日のラベルを赤色にする
- 投稿時間と日付に基づいて散布図をプロットする
- x軸、y軸の範囲とラベルを設定する
- グリッド線を追加する
- グラフのタイトルを設定する
- 描画する<br>

これによって、30日間でどの時間帯にどのくらいのツイートが投稿されているかがプロットの大きさの違いで可視化されます。


***********************************************************************************************************************************************************************


### This script reads Twitter tweet post data and creates a scatterplot based on the time and date of the posts over the last 30 days.
##### Specifically, the following process is used

- Import pandas library and also import matplotlib.pyplot, calendar, pytz
- Import Twitter tweet posting data in csv format
- Convert posting date and time to Japan time
- Separate posting date from posting time
- Extract data within 30 days
- Set the drawing area of the graph
- Set the day of the week and date on the y-axis
- Turn Sunday labels red
- Plot scatter plots based on posting time and date
- Set x- and y-axis ranges and labels
- Add grid lines
- Set a title for the graph
- Draw the chart<br>

This will visualize how many tweets are posted at any given time over a 30-day period, based on the different sizes of the plots.
<br>
<br>
<br>
![2023-03-30_14h25_06](https://user-images.githubusercontent.com/71259928/229946640-0761f0d8-daf3-4b6a-9ca7-8192d19895d3.png)
