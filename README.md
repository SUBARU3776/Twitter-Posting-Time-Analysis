# Twitter-Posting-Time-Analysis
このスクリプトは、Twitterのツイート投稿データを読み込み、最近30日間の投稿の時間帯と日付に基づいて散布図を作成するものです。具体的には、以下のような処理を行っています。

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
