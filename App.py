import sys
import os
import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout,
    QListWidget, QGridLayout, QPushButton,
    QScrollArea, QGroupBox
)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import Qt


class ClipboardApp(QWidget):
    
    def __init__(self):

        super().__init__()

        self.setWindowTitle("문자표 클립보드")
        self.setFixedSize(555, 400)

        mainLayout = QHBoxLayout(self)
        self.listWidget = QListWidget()
        self.listWidget.clicked.connect(self.onFileSelected)
        self.listWidget.setStyleSheet(
        """
            QListWidget {
                background-color: white;
                border: 1px solid #ccc;
                font-size: 13px;
                
            }
            QListWidget::item:hover {
                background-color: #e0e0e0;
            }
            QListWidget::item:selected {
                background-color: #a0c4ff;
                color: black;
                font-weight: bold;
            }
        """)
        
        mainLayout.addWidget(self.listWidget, 1)

        self.grid = QGridLayout()
        self.grid.setAlignment(Qt.AlignTop)
        self.grid.setSpacing(0)  
        self.grid.setContentsMargins(0, 0, 0, 0)  

        self.scroll = QScrollArea()
        self.charGroup = QGroupBox()        
        self.charGroup.setLayout(self.grid)
        self.scroll.setWidget(self.charGroup)
        self.scroll.setWidgetResizable(True)
        mainLayout.addWidget(self.scroll, 4)

        if getattr(sys, 'frozen', False):
            BASE_DIR = sys._MEIPASS  
        else:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        IconPath = os.path.join(BASE_DIR, 'Public', 'icon.jpg')
        self.setWindowIcon(QIcon(IconPath))
        self.DictFolder = os.path.join(BASE_DIR, "Dictionary")

        self.loadFiles()

    # 파일 불러오기
    def loadFiles(self):
        if os.path.exists(self.DictFolder):
            
            files = [f for f in os.listdir(self.DictFolder) if f.endswith(".json")]
            
            for json_file in files:
                try:
                    file_name = os.path.splitext(json_file)[0]
                    self.listWidget.addItem(file_name)
                except:
                    pass

    # 클립보드
    def copyTo(self, char):
        QApplication.clipboard().setText(char)

    # 파일 데이터 불러오기
    def onFileSelected(self):

        item = self.listWidget.currentItem()

        if item:
            json_file = item.text() + ".json"
            file_path = os.path.join(self.DictFolder, json_file)

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.drawGrid(data)

            except Exception as e:
                pass 

    # 그리기 분기
    def drawFlag(self, char, code):

        flag = True
        if char == "﹧" or char.strip()=="": 
            if code:
                try:
                    tmp = chr(int(code, 16))
                    if tmp == "﹧" or char.strip()=="":
                        flag = False  
                    char = tmp
                except ValueError:
                    flag = False  
            else:
                flag = False  

        return flag

    # 파일 데이터 그리기
    def drawGrid(self, characters):

        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().setParent(None)

        cnt = 0
        for item in characters:
            
            char = item.get("char", "")
            code = item.get("code", "")


            if self.drawFlag(char,code) == False:
                continue

            btn = QPushButton(char)
            btn.setFixedSize(40, 40)
            btn.setFixedSize(40, 40)
            btn.setStyleSheet("""
                QPushButton {
                    font-size: 24px;
                    font-weight: bold;
                    background-color: white;
                    border: 1px solid #ccc;
                    border-radius: 0px;
                    padding: 0px;
                    margin: 0px;
                    qproperty-iconSize: 40px;
                }
                QPushButton:hover {
                    background-color: #eee;
                }
                QPushButton:pressed {
                    background-color: #ddd;
                }
            """)

            btn.clicked.connect(lambda _, c=char: self.copyTo(c))

            # 행/열
            row = cnt // 10
            col = cnt % 10
            self.grid.addWidget(btn, row, col)

            cnt+=1

if __name__ == "__main__":

    App = QApplication(sys.argv)
    font = QFont("Malgun Gothic")
    App.setFont(font)

    clipboardApp = ClipboardApp()
    clipboardApp.show()

    sys.exit(App.exec_())
