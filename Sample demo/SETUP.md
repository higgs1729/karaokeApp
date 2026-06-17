# セットアップ・実行方法

このフォルダは README.md(画面・機能設計、フォルダ構成)をもとに生成した
プロジェクトの雛形です。各ファイルにはクラス定義と最低限のUI配置のみが
入っており、実際の機能(検索処理、再生処理、採点処理など)は TODO コメント
の箇所に実装していく想定です。

## 1. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

(Python 3.10 以降を推奨します)

## 2. アプリの起動

このディレクトリ(karaoke_app フォルダの一つ上の階層)で次を実行してください。

```bash
python -m karaoke_app.main
```

`karaoke_app` を Python パッケージとして認識させるため、`python karaoke_app/main.py`
のような直接実行ではなく `-m` オプションでの実行を推奨します。

## README.md との差分・補足

- `画面・機能設計` には `HomeWidget` と `MusicNameWidget` がありましたが、
  `フォルダ構成` には対応するファイルの記載がなかったため、本雛形では
  `widgets/home_widget.py` と `widgets/music_name_widget.py` を追加しています。
- `serchresult_widget.py` / `SerchresultsWidget` は README.md の表記をそのまま
  使用しています(`search_result` のtypoの可能性があります)。
- `MainWindow` は単体のファイルではなく `main.py` 内に実装し、
  `QStackedWidget` で各画面を切り替える形にしています。
- ボタンのクリックと画面遷移は仮の対応関係で接続しているので、
  実際の画面遷移ルールに合わせて `main.py` の `_connect_navigation()` を
  調整してください。
