import functools

from PyQt6.QtWidgets import QPushButton, QMessageBox

from MODULE3.Exercise64.models.OfficialEmployee import OfficialEmployee
from MODULE3.Exercise64.models.StaffManagement import StaffManagement
from MODULE3.Exercise64.models.TemporaryEmployee import TemporaryEmployee
from MODULE3.Exercise64.ui.MainWindow64 import Ui_MainWindow


class MainWindow64Ext(Ui_MainWindow):
    def __init__(self):
        self.sm=StaffManagement()
    def setupUI(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonSave.clicked.connect(self.process_save_employee)
    def process_save_employee(self):
        if self.checkBoxOfficial.isChecked():
            emp=OfficialEmployee()
        else:
            emp=TemporaryEmployee()
        emp.id=self.lineEditId.text()
        emp.idcard=self.lineEditIdCard.text()
        emp.name=self.lineEditName.text()
        emp.birthday=self.lineEditBirthday.text()
        self.sm.add_employee(emp)
        self.display_employee_layout()
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def display_employee_layout(self):
        self.clearLayout(self.verticalLayoutButton)
        for i in range(len(self.sm.database)):
            x=self.sm.database[i]
            title = f"{x.id}-{x.name}-{x.birthday}"
            btn = QPushButton(text=title)
            if isinstance(x,OfficialEmployee):
                btn.setStyleSheet("background-color: rgb(217,124,209);")
            else:
                btn.setStyleSheet("background-color: rgb(188,247,243);")
            self.verticalLayoutButton.addWidget(btn)
            btn.clicked.connect(functools.partial(self.show_detail,i))

    def show_detail(self,i):
        self.selected_index=i
        emp=self.sm.database[i]
        #show emp chi tiet len giao dien (lam sau)
        self.lineEditId.setText(emp.id)
        self.lineEditIdCard.setText(emp.idcard)
        self.lineEditName.setText(emp.name)
        self.lineEditBirthday.setText(emp.birthday)
        if isinstance(emp, OfficialEmployee):
            self.checkBoxOfficial.setChecked(True)
        else:
            self.checkBoxOfficial.setChecked(False)



    def clear_employee_detail(self):
        self.lineEditId.clear()
        self.lineEditIdCard.clear()
        self.lineEditName.clear()
        self.lineEditBirthday.clear()
        self.checkBoxOfficial.setChecked(False)



