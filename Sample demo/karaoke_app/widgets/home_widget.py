"""
HomeWidget

アプリ起動後の最初の画面。各機能への入口となるボタン群を表示する。

(注) README.md の「フォルダ構成」には home_widget.py の記載がありませんでしたが、
「画面・機能設計」に HomeWidget の定義があるため、本スキャフォルドで追加しています。
"""
from PySide6.QtWidgets import QVBoxLayout, QWidget

from karaoke_app.components.buttons.primary_button import PrimaryButton
from karaoke_app.components.buttons.secondary_button import SecondaryButton


class HomeWidget(QWidget):
    """ホーム画面。各画面への遷移ボタンを保持する。"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("HomeWidget")

        layout = QVBoxLayout(self)

        self.search_button = PrimaryButton("検索")
        self.popular_songs_button = SecondaryButton("人気曲")
        self.volume_settings_button = SecondaryButton("音量調整設定")
        self.player_settings_button = SecondaryButton("再生設定")
        self.queue_management_button = SecondaryButton("予約管理")

        for button in (
            self.search_button,
            self.popular_songs_button,
            self.volume_settings_button,
            self.player_settings_button,
            self.queue_management_button,
        ):
            layout.addWidget(button)

        layout.addStretch()
