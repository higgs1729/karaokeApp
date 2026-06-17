- 使用技術
    - Python
    - PySide6

- アプリ名: カラオケAPP
    - 画面・機能設計
        - MainWindow
            - HeaderWidget
                - アプリ名 :画面上部に大きく"カラオケAPP"と表示
                <!-- - ユーザー情報 :画面右上部にユーザー情報()を表示する -->

            - HomeWigdget
                - 検索ボタン :SearchWidgetへの画面遷移をするためのボタン。   
                - 人気曲欄 :人気曲を一覧にした画面への画面遷移のボタン
                - 音量調整設定ボタン(VolumeWidget) :VolumeWidgetへの画面遷移のボタン
                - 再生設定ボタン(PlayerWidget):PlayerWidgetへの画面遷移ボタン
                - 予約管理ボタン :QueueWidgetの予約曲一覧への画面遷移ボタン

            - SearchWidget
                - 曲名入力欄 :キーワードや曲名やアーティスト名での楽曲検索が可能なテキスト入力欄
                - 検索決定ボタン :曲名入力欄での入力を決定
                - 簡易検索一覧 :ジャンルや年代などで分けて曲を検索できる
                - SongListWidget
                    - 曲一覧 :song_list_widget.pyの一覧を表示する

            - SerchresultsWidget
                - 検索結果一覧 :検索決定ボタンを押した後に出る画面。検索内容に応じて返す曲が変わる

            - QueueWidget
                - 予約曲一覧 :MusicNameWidgetの予約ボタンで予約した曲を一覧にして表示する
                - 曲削除 :予約した曲の中から曲を削除できる
                - 曲順変更 :予約曲一覧の中から曲をドラッグして順番を変更できる

            - MusicNameWidget
                - 曲名表示 :画面上部左側に曲名を表示する
                - アーティスト名表示 :曲名の下にアーティスト名を表示する
                - ジャケット :画面上部右側にジャケットを表示する
                - 歌いだし表示(歌詞の一部) :画面左下側に菓子の一部を表示する
                - 予約ボタン :画面右下側にQueueWidgetの予約曲に追加する

            - KaraokeWidget
                - PlayerWidget
                    - 再生ボタン :予約した曲の一番目の曲を再生する
                    - 一時停止ボタン :再生中の曲を一時停止する
                    - 停止ボタン :再生中の曲を強制終了する
                    - 歌いなおしボタン :再生中の曲をはじめから再生しなおす
                    - シークバー :曲の再生している部分を示すスライダー、動かして再生する場所を変えられる
                    - 再生時間 :再生している曲の長さと再生しているタイミングの時間を表示する

                - VolumeWidget
                    - メイン音量スライダー :画面上部に位置し、全体の音量を調整するスライダー
                    - ミュージック音量スライダー :メイン音量スライダーの下に位置し、BGMの音量を調整するスライダー
                    - マイク音量スライダー :ミュージック音量スライダーの下に位置し、マイクから拾った音の大きさを調整するスライダー
                    - ミュートボタン :画面右下側に位置し、すべての音をミュートするボタン
                
                - MicrophoneWidget
                    - エコースライダー :音の響きを調整するスライダー

                - LyricsWidget
                    - 歌詞表示 :歌詞の全体を表示する

            - ScoringWidget
                - 採点有効化ボタン :採点のON/OFFを切り替えるボタン
                - 音程判定表示 :音程判定表示のON/OFFを切り替えるボタン
                - リズム判定表示 :リズム判定表示のON/OFFを切り替えるボタン
                - 得点表示 :得点を表示するボタン
                - 採点履歴表示 :採点履歴を表示するボタン

    - フォルダ構成
        - karaoke_app
            - main.py

            - components
                - buttons
                    - primary_button.py
                    - secondary_button.py
                    - icon_button.py

                - inputs
                    - text_input.py

                - labels
                    - title_label.py

                - cards
                    - card_widget.py

            - widgets
                - header_widget.py
                - search_widget.py
                - serchresult_widget.py
                - song_list_widget.py
                - queue_widget.py

                - karaoke_widget.py

                - player_widget.py
                - volume_widget.py
                - microphone_widget.py
                - lyrics_widget.py
                
                - scoring_widget.py

            - models
                - song.py
                - queue.py
                - score.py

            - controllers
                - search_controller.py
                - queue_controller.py
                - player_controller.py
                - scoring_controller.py

            - resources
                - icons
                - images
                - styles

            - data
                - songs
                - lyrics
                - scores

---     

- 補足
    - chatgpt URL 
        - https://chatgpt.com/share/6a2914ec-47d0-83ab-b449-5d00ce7041a9

    - tryingフォルダ
        - pyside6の仕様などを把握するためのスペーズ
        - 本アプリの特定の機能に対する責務を持つものではない        