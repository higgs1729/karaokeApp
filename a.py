# minimal_pyside6.py
import sys
from PySide6.QtWidgets import QApplication, QLabel

def main():
    # QApplication: アプリ全体を管理するオブジェクト
    app = QApplication(sys.argv)

    # QLabel: シンプルなテキスト表示ウィジェット
    label = QLabel("Hello, PySide6!")
    label.resize(300, 100)  # ウィンドウサイズ
    label.show()  # 表示

    # イベントループ開始
    sys.exit(app.exec())

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"エラーが発生しました: {e}")