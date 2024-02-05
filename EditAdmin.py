
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QLineEdit

from ComboCheckBox import QComboCheckBox
from db import sql_execute
from sqls import *


class EditAdmin(object):
    # 界面设计
    def setupUi(self, Form, adminId):
        Form.setObjectName("Form")
        Form.resize(360, 279)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 54, 12))
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        admin = sql_execute(getAdminById(adminId))[0]
        self.textEdit = QtWidgets.QLineEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(100, 30, 181, 31))
        self.textEdit.setText(admin[1])
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QLineEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(100, 80, 181, 31))
        self.textEdit_2.setText(admin[3])
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 54, 12))
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.textEdit_3 = QComboCheckBox(Form)

        class_dict = []
        try:
            # 不为超级管理员
            if admin[4] != '0':
                data4 = admin[4].split(',')
                for d in data4:
                    class_dict.append(d)
        except Exception as e:
            pass

        # 获取班级列表（供老师选择来管理）
        classlist = sql_execute(getClassList('0', ''))
        for class_ in classlist:
            self.textEdit_3.add_item('%d.%s' % (class_[0], class_[1]),
                                     flag=admin[4] == '0' or str(class_[0]) in class_dict)
        self.textEdit_3.setGeometry(QtCore.QRect(100, 130, 181, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(23, 140, 71, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")

        # 提交按钮
        self.pushButton.clicked.connect(lambda: self.updateAdmin(adminId, Form))

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 220, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        # 取消按钮
        self.pushButton_2.clicked.connect(lambda: Form.hide())

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 220, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        # 重置密码按钮
        self.pushButton_3.clicked.connect(lambda: self.resetPassw(adminId, Form))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # 重新翻译（针对性修改）
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "EDIT ADMIN"))
        self.label.setText(_translate("Form", "USERNAME:"))
        self.label_2.setText(_translate("Form", "MARK:"))
        self.label_3.setText(_translate("Form", "TEAM:"))
        self.pushButton.setText(_translate("Form", "SUBMIT"))
        self.pushButton_2.setText(_translate("Form", "CANCEL"))
        self.pushButton_3.setText(_translate("Form", "RESET PASSWORD"))

    # 功能实现（修改用户名）
    def updateAdmin(self, adminId, Form):
        username = self.textEdit.text()
        mark = self.textEdit_2.text()
        classids = self.textEdit_3.get_class_text()
        sql_execute(updateAdminById(adminId, username, mark, classids))
        QMessageBox.about(Form, 'SUCCESSFUL!', "Please refresh the list data")
        Form.hide()

    # 功能实现（重置密码）
    def resetPassw(self, adminId, Form):
        text, okPressed = QInputDialog.getText(Form, "RESET PASSWORD", "NEW PASSWORD", QLineEdit.Normal, '')
        if okPressed:
            try:
                sql_execute(resetAdminPasswById(adminId, text))
                QMessageBox.about(Form, 'SUCCESSFULLY', 'RESET SUCCESSFUL')
            except Exception as e:
                QMessageBox.critical(Form, 'FAIL', 'RETRY\n')
            Form.hide()


# 测试
if __name__ == "__main__":
    import sys
    App = QApplication(sys.argv)  # 创建QApplication对象，作为GUI主程序入口
    aw = EditAdmin()  # 创建主窗体对象，实例化Ui_MainWindow
    w = QMainWindow()  # 实例化QMainWindow类
    aw.setupUi(w, 1)  # 主窗体对象调用setupUi方法，对QMainWindow对象进行设置
    w.show()  # 显示主窗体
    w.setWindowTitle('Python Sailing Management System')
    sys.exit(App.exec_())  # 循环中等待退出程序
