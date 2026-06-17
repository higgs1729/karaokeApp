from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout
from components.buttons.primary_button import PrimaryButton
from components.buttons.secondary_button import SecondaryButton


class HomeWidget(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.mw = main_window
        self.setObjectName("HomeWidget")
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)

        grid = QGridLayout()
        grid.setSpacing(16)

        btn_search = PrimaryButton("🔍 曲を検索")
        btn_popular = PrimaryButton("🌟 人気曲")
        btn_volume = SecondaryButton("🔊 音量設定")
        btn_player = SecondaryButton("▶ 再生設定")
        btn_queue = PrimaryButton("📋 予約管理")

        btn_search.clicked.connect(lambda: self.mw.navigate_to(1))
        btn_popular.clicked.connect(lambda: self.mw.navigate_to(3))
        btn_queue.clicked.connect(lambda: self.mw.navigate_to(4))
        btn_volume.clicked.connect(lambda: self.mw.navigate_to(5))  # KaraokeWidget内
        btn_player.clicked.connect(lambda: self.mw.navigate_to(5))

        grid.addWidget(btn_search, 0, 0)
        grid.addWidget(btn_popular, 0, 1)
        grid.addWidget(btn_queue, 1, 0)
        grid.addWidget(btn_volume, 1, 1)
        grid.addWidget(btn_player, 2, 0, 1, 2)

        layout.addStretch()
        layout.addLayout(grid)
        layout.addStretch()
