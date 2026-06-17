import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QVBoxLayout, QWidget

from widgets.header_widget import HeaderWidget
from widgets.home_widget import HomeWidget
from widgets.search_widget import SearchWidget
from widgets.serchresult_widget import SearchResultWidget
from widgets.song_list_widget import SongListWidget
from widgets.queue_widget import QueueWidget
from widgets.karaoke_widget import KaraokeWidget
from widgets.scoring_widget import ScoringWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("カラオケAPP")
        self.resize(1280, 720)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Header
        self.header = HeaderWidget()
        layout.addWidget(self.header)

        # Stacked widget for screen transitions
        self.stack = QStackedWidget()
        layout.addWidget(self.stack)

        # Pages
        self.home_widget = HomeWidget(self)
        self.search_widget = SearchWidget(self)
        self.search_result_widget = SearchResultWidget(self)
        self.song_list_widget = SongListWidget(self)
        self.queue_widget = QueueWidget(self)
        self.karaoke_widget = KaraokeWidget(self)
        self.scoring_widget = ScoringWidget(self)

        self.stack.addWidget(self.home_widget)        # index 0
        self.stack.addWidget(self.search_widget)      # index 1
        self.stack.addWidget(self.search_result_widget)  # index 2
        self.stack.addWidget(self.song_list_widget)   # index 3
        self.stack.addWidget(self.queue_widget)       # index 4
        self.stack.addWidget(self.karaoke_widget)     # index 5
        self.stack.addWidget(self.scoring_widget)     # index 6

        self.stack.setCurrentIndex(0)

    def navigate_to(self, index: int):
        self.stack.setCurrentIndex(index)


def main():
    app = QApplication(sys.argv)

    # Load global stylesheet
    try:
        with open("resources/styles/main.qss", "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        pass

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
