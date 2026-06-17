"""
カラオケAPP エントリーポイント

MainWindow を起動し、HeaderWidget と各画面(QStackedWidget で切り替え)を表示する。

実行方法:
    プロジェクトルート(karaoke_app フォルダの一つ上の階層)で次を実行する。
        python -m karaoke_app.main
"""
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QVBoxLayout, QWidget

from karaoke_app.widgets.header_widget import HeaderWidget
from karaoke_app.widgets.home_widget import HomeWidget
from karaoke_app.widgets.karaoke_widget import KaraokeWidget
from karaoke_app.widgets.music_name_widget import MusicNameWidget
from karaoke_app.widgets.queue_widget import QueueWidget
from karaoke_app.widgets.scoring_widget import ScoringWidget
from karaoke_app.widgets.search_widget import SearchWidget
from karaoke_app.widgets.serchresult_widget import SerchresultsWidget


class MainWindow(QMainWindow):
    """アプリ全体のメインウィンドウ。"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("カラオケAPP")
        self.resize(960, 640)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        root_layout = QVBoxLayout(central_widget)
        root_layout.setContentsMargins(0, 0, 0, 0)

        self.header_widget = HeaderWidget()
        root_layout.addWidget(self.header_widget)

        self.stacked_widget = QStackedWidget()
        root_layout.addWidget(self.stacked_widget)

        # 各画面を生成し、QStackedWidget に登録する
        self.home_widget = HomeWidget()
        self.search_widget = SearchWidget()
        self.search_results_widget = SerchresultsWidget()
        self.queue_widget = QueueWidget()
        self.music_name_widget = MusicNameWidget()
        self.karaoke_widget = KaraokeWidget()
        self.scoring_widget = ScoringWidget()

        for widget in (
            self.home_widget,
            self.search_widget,
            self.search_results_widget,
            self.queue_widget,
            self.music_name_widget,
            self.karaoke_widget,
            self.scoring_widget,
        ):
            self.stacked_widget.addWidget(widget)

        self._connect_navigation()
        self.stacked_widget.setCurrentWidget(self.home_widget)

    def _connect_navigation(self) -> None:
        """ホーム画面の各ボタンと画面遷移を結びつける(仮の遷移先)。"""
        self.home_widget.search_button.clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.search_widget)
        )
        self.home_widget.volume_settings_button.clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.karaoke_widget)
        )
        self.home_widget.player_settings_button.clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.karaoke_widget)
        )
        self.home_widget.queue_management_button.clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.queue_widget)
        )
        self.search_widget.search_button.clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.search_results_widget)
        )


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
