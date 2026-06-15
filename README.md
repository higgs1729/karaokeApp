- 使用技術
    - Python
    - PySide6

- アプリ名: カラオケAPP
    - 画面・機能設計
        - MainWindow
            - HeaderWidget
                - アプリ名 :画面上部に大きく"カラオケAPP"と表示
                <!-- - ユーザー情報 :画面右上部にユーザー情報()を表示する -->

            - HomeWigdget     -----------追加
                - 検索ボタン :SearchWidgetへの画面遷移をするためのボタン。   ------------追加
                - 人気曲欄   ------------追加
                - 音量調整設定ボタン(VolumeWidget)  ------------追加
                - 再生設定ボタン(PlayerWidget)   -----------追加
                - 予約管理ボタン

            - SearchWidget
                - 曲名入力欄 :キーワードや曲名やアーティスト名での楽曲検索が可能なテキスト入力欄
                - 検索決定ボタン :曲名入力欄での入力を決定
                - 簡易検索一覧　　　----------追加
                - SongListWidget
                    - 曲一覧

            - SerchresultsWidget　　-----------追加
                - 検索結果一覧　　------追加

            - QueueWidget
                - 予約曲一覧　　--------追加
                - 曲削除
                - 曲順変更

            - MusicNameWidget   ------------追加
                - 曲名表示　　　　------------
                - アーティスト名表示  ------------
                - ジャケット   --------------
                - 歌いだし表示(歌詞の一部)  ---------------
                - 予約ボタン  ---------------

            - KaraokeWidget
                - PlayerWidget
                    - 再生ボタン
                    - 一時停止ボタン
                    - 停止ボタン
                    - 歌いなおしボタン    ---------------追加
                    - シークバー
                    - 再生時間

                - VolumeWidget
                    - メイン音量スライダー      -------------追加(音量スライダー消去)
                    - ミュージック音量スライダー   -------------追加
                    - マイク音量スライダー   ------------追加
                    - ミュートボタン
                
                - MicrophoneWidget   -----------追加(できるかわからないけど)
                    - エコースライダー  ---------------

                - LyricsWidget
                    - 歌詞表示


            - ScoringWidget
                - 採点有効化ボタン
                - 音程判定表示
                - リズム判定表示
                - 得点表示
                - 採点履歴表示

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
                - song_list_widget.py

                - queue_widget.py

                - karaoke_widget.py
                - player_widget.py
                - volume_widget.py
                - microphone_widget.py  -----------追加

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