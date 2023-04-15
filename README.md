# Twitter-Posting-Time-Analysis
### このスクリプトは、Twitterのツイート投稿データを読み込み、30日間の投稿の時間帯と日付に基づいて散布図を作成するものです。

##### 具体的には、以下のような処理を行っています。

- データを読み込み、日時型に変換する。
- 投稿日と投稿時間を分離し、30日間のデータを抽出する。
- 一時間当たりの投稿数と"source"の割合を計算する。
- "source"に応じてランダムな色を割り当てる。
- グラフの描画領域を設定し、x軸に時間、y軸に曜日と日付を設定する。
- 一時間当たりの投稿数に応じてマーカーの大きさを決定する。
- グラフを表示する。


これによって、30日間でどの時間帯にどのくらいのツイートが投稿されているかがプロットの大きさの違いで可視化されます。<br>
sourceごとの投稿数を円グラフなどの形で可視化するために使用できるデータを生成することができます。<br>
- ##### v2.0で"color_map"の定義を削除し、counts dfのsource列をループしてランダムな色を割り当てるようにしました。これにより、未知の"source値"にも対応が可能となります。

***********************************************************************************************************************************************************************


### This script reads Twitter tweet post data and creates a scatterplot based on the time and date of the posts over a 30-day period.
##### Specifically, the following processes are performed.<br>

- Reads the data and converts it to date/time type.
- Separate the posting date from the posting time and extract the data for the 30-day period.
- Calculate the number of posts per hour and the ratio of "source".
- Assign a random color to the "source".
- Set the drawing area of the graph with time on the x-axis and the day of the week and date on the y-axis.
- Determine the size of the markers according to the number of posts per hour.
- Display the graph.<br>
<br>
This will visualize how many tweets are posted at any given time over a 30-day period by the size of the plots.<br>
Generate data that can be used to visualize the number of posts per "source" in the form of a pie chart or similar.
![2023-04-15_13h57_56](https://user-images.githubusercontent.com/71259928/232188418-2653b38d-a3bc-4312-8726-5eee0f64cf0f.png)

- ##### In v2.0, the "color_map" definition was removed and a random color is assigned by looping through the source column of the counts df. This allows for unknown "source values" to be handled.
