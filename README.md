# Twitter-Posting-Time-Analysis
### このスクリプトは、Twitterのツイート投稿データを読み込み、最近30日間の投稿の時間帯と日付に基づいて散布図を作成するものです。

##### 具体的には、以下のような処理を行っています。

- データの中から最新の日時を取得する。
- 投稿日と投稿時間を分離する。
- 30日以内のツイートを抽出する。
- 投稿元（source）ごとの投稿数をカウントする。
- 投稿数の降順でソートする。
- 投稿元ごとの割合を計算する。
- 結果を表示する。
- sourceに応じてランダムな色を割り当てる。
- グラフの描画領域を設定する。
- y軸に曜日と日付を設定する。
- source毎にラベルと色を設定する。
- 凡例を追加する。
- x軸のラベルと範囲を設定する。
- x軸のグリッド線を追加する。
- y軸の範囲を設定する。
- y軸のグリッド線を追加する。
- グラフのタイトルを設定する。
- グラフを表示する。<br>

これによって、30日間でどの時間帯にどのくらいのツイートが投稿されているかがプロットの大きさの違いで可視化されます。<br>
sourceごとの投稿数を円グラフなどの形で可視化するために使用できるデータを生成することができます。<br>
また、時間と日付にわたるツイートの投稿パターンを視覚化するために使用することもできます。

***********************************************************************************************************************************************************************


### This script reads Twitter tweet post data and creates a scatterplot based on the time and date of the posts over the last 30 days.
##### Specifically, the following process is used

- Get the latest date and time from the data.
- Separate the posting date from the posting time.
- Extract tweets within 30 days.
- Count the number of posts by source.
- Sort in descending order of the number of posts.
- Calculate the percentage of each source.
- Display the results.
- Assign a random color according to the source.
- Set the drawing area for the graph.
- Set the day of the week and date on the y-axis.
- Set labels and colors for each source.
- Add a legend.
- Set labels and ranges for the x-axis.
- Add grid lines for x-axis.
- Set the range of y-axis.
- Add a grid line for y-axis
- Set a title for the graph
- Displaying a graph<br>

This allows visualization of how many tweets are posted at any given time over a 30-day period by the size of the plots.<br>
It can generate data that can be used to visualize the number of posts per SOURCE in the form of a pie chart or similar.<br>
It can also be used to visualize the pattern of tweets posted over time and date.<br>

![2023-03-30_14h25_06](https://user-images.githubusercontent.com/71259928/229946640-0761f0d8-daf3-4b6a-9ca7-8192d19895d3.png)
