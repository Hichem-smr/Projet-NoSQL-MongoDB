# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 471)
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        MainWindow.setSizeIncrement(QtCore.QSize(500, 500))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(2000, 2000))
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 621, 451))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.widget_4 = QtWidgets.QWidget(self.groupBox)
        self.widget_4.setEnabled(True)
        self.widget_4.setGeometry(QtCore.QRect(4, 7, 613, 170))
        self.widget_4.setMinimumSize(QtCore.QSize(500, 170))
        self.widget_4.setAutoFillBackground(True)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Manual = QtWidgets.QPushButton(self.widget_4)
        self.Manual.setMaximumSize(QtCore.QSize(100, 50))
        self.Manual.setObjectName("Manual")
        self.verticalLayout_5.addWidget(self.Manual)
        self.widget_2 = QtWidgets.QWidget(self.widget_4)
        self.widget_2.setAutoFillBackground(True)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.DB_tree = QtWidgets.QTreeWidget(self.widget_2)
        self.DB_tree.setAutoFillBackground(True)
        self.DB_tree.setObjectName("DB_tree")
        self.verticalLayout_3.addWidget(self.DB_tree)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Connect_db = QtWidgets.QPushButton(self.widget_2)
        self.Connect_db.setObjectName("Connect_db")
        self.horizontalLayout.addWidget(self.Connect_db)
        self.Disconnect_db = QtWidgets.QPushButton(self.widget_2)
        self.Disconnect_db.setEnabled(False)
        self.Disconnect_db.setObjectName("Disconnect_db")
        self.horizontalLayout.addWidget(self.Disconnect_db)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Layout_0 = QtWidgets.QHBoxLayout()
        self.Layout_0.setObjectName("Layout_0")
        self.req_1 = QtWidgets.QRadioButton(self.widget_2)
        self.req_1.setEnabled(False)
        self.req_1.setObjectName("req_1")
        self.Layout_0.addWidget(self.req_1)
        self.req_2 = QtWidgets.QRadioButton(self.widget_2)
        self.req_2.setEnabled(False)
        self.req_2.setObjectName("req_2")
        self.Layout_0.addWidget(self.req_2)
        self.req_3 = QtWidgets.QRadioButton(self.widget_2)
        self.req_3.setEnabled(False)
        self.req_3.setObjectName("req_3")
        self.Layout_0.addWidget(self.req_3)
        self.req_4 = QtWidgets.QRadioButton(self.widget_2)
        self.req_4.setEnabled(False)
        self.req_4.setObjectName("req_4")
        self.Layout_0.addWidget(self.req_4)
        self.req_5 = QtWidgets.QRadioButton(self.widget_2)
        self.req_5.setEnabled(False)
        self.req_5.setObjectName("req_5")
        self.Layout_0.addWidget(self.req_5)
        self.verticalLayout_2.addLayout(self.Layout_0)
        self.Layout_2 = QtWidgets.QHBoxLayout()
        self.Layout_2.setContentsMargins(-1, -1, 3, -1)
        self.Layout_2.setObjectName("Layout_2")
        self.req_6 = QtWidgets.QRadioButton(self.widget_2)
        self.req_6.setEnabled(False)
        self.req_6.setObjectName("req_6")
        self.Layout_2.addWidget(self.req_6)
        self.req_7 = QtWidgets.QRadioButton(self.widget_2)
        self.req_7.setEnabled(False)
        self.req_7.setObjectName("req_7")
        self.Layout_2.addWidget(self.req_7)
        self.req_8 = QtWidgets.QRadioButton(self.widget_2)
        self.req_8.setEnabled(False)
        self.req_8.setObjectName("req_8")
        self.Layout_2.addWidget(self.req_8)
        self.req_9 = QtWidgets.QRadioButton(self.widget_2)
        self.req_9.setEnabled(False)
        self.req_9.setObjectName("req_9")
        self.Layout_2.addWidget(self.req_9)
        self.req_10 = QtWidgets.QRadioButton(self.widget_2)
        self.req_10.setEnabled(False)
        self.req_10.setObjectName("req_10")
        self.Layout_2.addWidget(self.req_10)
        self.verticalLayout_2.addLayout(self.Layout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.req_11 = QtWidgets.QRadioButton(self.widget_2)
        self.req_11.setEnabled(False)
        self.req_11.setObjectName("req_11")
        self.horizontalLayout_5.addWidget(self.req_11)
        self.req_12 = QtWidgets.QRadioButton(self.widget_2)
        self.req_12.setEnabled(False)
        self.req_12.setObjectName("req_12")
        self.horizontalLayout_5.addWidget(self.req_12)
        self.req_13 = QtWidgets.QRadioButton(self.widget_2)
        self.req_13.setEnabled(False)
        self.req_13.setObjectName("req_13")
        self.horizontalLayout_5.addWidget(self.req_13)
        self.req_14 = QtWidgets.QRadioButton(self.widget_2)
        self.req_14.setEnabled(False)
        self.req_14.setObjectName("req_14")
        self.horizontalLayout_5.addWidget(self.req_14)
        self.req_15 = QtWidgets.QRadioButton(self.widget_2)
        self.req_15.setEnabled(False)
        self.req_15.setObjectName("req_15")
        self.horizontalLayout_5.addWidget(self.req_15)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(4, 183, 600, 250))
        self.widget.setMinimumSize(QtCore.QSize(600, 250))
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.TableQuery = QtWidgets.QTableWidget(self.widget)
        self.TableQuery.setObjectName("TableQuery")
        self.TableQuery.setColumnCount(0)
        self.TableQuery.setRowCount(0)
        self.verticalLayout_4.addWidget(self.TableQuery)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.QueryExecute = QtWidgets.QPushButton(self.widget)
        self.QueryExecute.setEnabled(False)
        self.QueryExecute.setCheckable(False)
        self.QueryExecute.setObjectName("QueryExecute")
        self.horizontalLayout_6.addWidget(self.QueryExecute)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Manual.setText(_translate("MainWindow", "Manual"))
        self.DB_tree.headerItem().setText(0, _translate("MainWindow", "DB"))
        self.Connect_db.setText(_translate("MainWindow", "Connect"))
        self.Disconnect_db.setText(_translate("MainWindow", "Disconnect"))
        self.req_1.setText(_translate("MainWindow", "1"))
        self.req_2.setText(_translate("MainWindow", "2"))
        self.req_3.setText(_translate("MainWindow", "3"))
        self.req_4.setText(_translate("MainWindow", "4"))
        self.req_5.setText(_translate("MainWindow", "5"))
        self.req_6.setText(_translate("MainWindow", "6"))
        self.req_7.setText(_translate("MainWindow", "7"))
        self.req_8.setText(_translate("MainWindow", "8"))
        self.req_9.setText(_translate("MainWindow", "9"))
        self.req_10.setText(_translate("MainWindow", "10"))
        self.req_11.setText(_translate("MainWindow", "11"))
        self.req_12.setText(_translate("MainWindow", "12"))
        self.req_13.setText(_translate("MainWindow", "13"))
        self.req_14.setText(_translate("MainWindow", "14"))
        self.req_15.setText(_translate("MainWindow", "15"))
        self.QueryExecute.setText(_translate("MainWindow", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())