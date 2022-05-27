from PySide6 import QtWidgets
from PySide6.QtWidgets import *

from SqliteHelper import *

from PySide6.QtUiTools import QUiLoader # 引入 UiLoader
from PySide6.QtCore import QFile, QIODevice
import sys


app = QApplication(sys.argv)

ui_file_name = "test.ui"
ui_file = QFile(ui_file_name)
if not ui_file.open(QIODevice.ReadOnly):
    print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
    sys.exit(-1)


loader = QUiLoader()
window = loader.load(ui_file)
ui_file.close()
if not window:
    print(loader.errorString())
    sys.exit(-1)

# SqliteHelper('test.db').create_table()

def loadData():
    helper = SqliteHelper("test.db")
    users = helper.select("SELECT * FROM users")

    for row_number,user in enumerate(users):
        window.tableWidget.insertRow(row_number)
        for column_number,data in enumerate(user):
            cell = QtWidgets.QTableWidgetItem(str(data))
            window.tableWidget.setItem(row_number,column_number,cell)
        
window.pushButton.clicked.connect(loadData)


window.show()
app.exec()
