# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(845, 638)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 0, 809, 579))
        self.tabWidget.setMinimumSize(QtCore.QSize(809, 579))
        self.tabWidget.setMaximumSize(QtCore.QSize(0, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.tabCategory = QtWidgets.QWidget()
        self.tabCategory.setObjectName("tabCategory")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tabCategory)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 641, 501))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tblCategory = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tblCategory.setObjectName("tblCategory")
        self.tblCategory.setColumnCount(2)
        self.tblCategory.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblCategory.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCategory.setHorizontalHeaderItem(1, item)
        self.horizontalLayout.addWidget(self.tblCategory)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tabCategory)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(670, 60, 121, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAdd = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout.addWidget(self.btnAdd)
        self.btnEdit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnEdit.setObjectName("btnEdit")
        self.verticalLayout.addWidget(self.btnEdit)
        self.btnDelete = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnDelete.setObjectName("btnDelete")
        self.verticalLayout.addWidget(self.btnDelete)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.tabWidget.addTab(self.tabCategory, "")
        self.tabExpenses = QtWidgets.QWidget()
        self.tabExpenses.setObjectName("tabExpenses")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tabExpenses)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 641, 501))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tblExpenses = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        self.tblExpenses.setObjectName("tblExpenses")
        self.tblExpenses.setColumnCount(6)
        self.tblExpenses.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblExpenses.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblExpenses.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblExpenses.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblExpenses.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblExpenses.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblExpenses.setHorizontalHeaderItem(5, item)
        self.horizontalLayout_2.addWidget(self.tblExpenses)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tabExpenses)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(670, 60, 121, 421))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnAddExpense = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnAddExpense.setObjectName("btnAddExpense")
        self.verticalLayout_2.addWidget(self.btnAddExpense)
        self.btnEditExpense = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnEditExpense.setObjectName("btnEditExpense")
        self.verticalLayout_2.addWidget(self.btnEditExpense)
        self.btnDeleteExpense = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnDeleteExpense.setObjectName("btnDeleteExpense")
        self.verticalLayout_2.addWidget(self.btnDeleteExpense)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.tabWidget.addTab(self.tabExpenses, "")
        self.tabReports = QtWidgets.QWidget()
        self.tabReports.setObjectName("tabReports")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tabReports)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 40, 641, 461))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.horizontalLayoutWidget_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tabReports)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(660, 50, 141, 471))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnGenerate = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnGenerate.setObjectName("btnGenerate")
        self.verticalLayout_3.addWidget(self.btnGenerate)
        self.btnGenerateByDate = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnGenerateByDate.setObjectName("btnGenerateByDate")
        self.verticalLayout_3.addWidget(self.btnGenerateByDate)
        self.btnMonthlyExpense = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnMonthlyExpense.setObjectName("btnMonthlyExpense")
        self.verticalLayout_3.addWidget(self.btnMonthlyExpense)
        self.btnYearlyExpense = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnYearlyExpense.setObjectName("btnYearlyExpense")
        self.verticalLayout_3.addWidget(self.btnYearlyExpense)
        self.btnQuarterExpense = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnQuarterExpense.setObjectName("btnQuarterExpense")
        self.verticalLayout_3.addWidget(self.btnQuarterExpense)
        self.btnFindMostCategoryID = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnFindMostCategoryID.setObjectName("btnFindMostCategoryID")
        self.verticalLayout_3.addWidget(self.btnFindMostCategoryID)
        self.btnExcel = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnExcel.setObjectName("btnExcel")
        self.verticalLayout_3.addWidget(self.btnExcel)
        self.btnGenerateAndImport = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnGenerateAndImport.setObjectName("btnGenerateAndImport")
        self.verticalLayout_3.addWidget(self.btnGenerateAndImport)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tabReports)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(60, 0, 554, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblFrom = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.lblFrom.setObjectName("lblFrom")
        self.horizontalLayout_4.addWidget(self.lblFrom)
        self.txtFromYear = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.txtFromYear.setObjectName("txtFromYear")
        self.horizontalLayout_4.addWidget(self.txtFromYear)
        self.lblFromMonth = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.lblFromMonth.setObjectName("lblFromMonth")
        self.horizontalLayout_4.addWidget(self.lblFromMonth)
        self.txtFromMonth = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.txtFromMonth.setObjectName("txtFromMonth")
        self.horizontalLayout_4.addWidget(self.txtFromMonth)
        self.lblFromDay = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.lblFromDay.setObjectName("lblFromDay")
        self.horizontalLayout_4.addWidget(self.lblFromDay)
        self.txtFromDay = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.txtFromDay.setObjectName("txtFromDay")
        self.horizontalLayout_4.addWidget(self.txtFromDay)
        self.lblTo = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.lblTo.setObjectName("lblTo")
        self.horizontalLayout_4.addWidget(self.lblTo)
        self.txtToYear = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.txtToYear.setObjectName("txtToYear")
        self.horizontalLayout_4.addWidget(self.txtToYear)
        self.lblToMonth = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.lblToMonth.setObjectName("lblToMonth")
        self.horizontalLayout_4.addWidget(self.lblToMonth)
        self.txtToMonth = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.txtToMonth.setObjectName("txtToMonth")
        self.horizontalLayout_4.addWidget(self.txtToMonth)
        self.lblToDay = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.lblToDay.setObjectName("lblToDay")
        self.horizontalLayout_4.addWidget(self.lblToDay)
        self.txtToDay = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.txtToDay.setObjectName("txtToDay")
        self.horizontalLayout_4.addWidget(self.txtToDay)
        self.txtTotal = QtWidgets.QLineEdit(self.tabReports)
        self.txtTotal.setGeometry(QtCore.QRect(100, 495, 461, 61))
        self.txtTotal.setText("")
        self.txtTotal.setObjectName("txtTotal")
        self.tabWidget.addTab(self.tabReports, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        item = self.tblCategory.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Category ID"))
        item = self.tblCategory.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Category"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnEdit.setText(_translate("MainWindow", "Edit"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCategory), _translate("MainWindow", "Categories"))
        item = self.tblExpenses.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Expense_ID"))
        item = self.tblExpenses.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "category ID"))
        item = self.tblExpenses.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Expense Date"))
        item = self.tblExpenses.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Expense"))
        item = self.tblExpenses.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.tblExpenses.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Notes"))
        self.btnAddExpense.setText(_translate("MainWindow", "Add"))
        self.btnEditExpense.setText(_translate("MainWindow", "Edit"))
        self.btnDeleteExpense.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabExpenses), _translate("MainWindow", "Expenses"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Expense ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Category ID"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Expense Date"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Expense"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Total Amount"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Notes"))
        self.btnGenerate.setText(_translate("MainWindow", "Generate"))
        self.btnGenerateByDate.setText(_translate("MainWindow", "GenerateByDate"))
        self.btnMonthlyExpense.setText(_translate("MainWindow", "MonthExpense"))
        self.btnYearlyExpense.setText(_translate("MainWindow", "YearExpense"))
        self.btnQuarterExpense.setText(_translate("MainWindow", "QuarterExpense"))
        self.btnFindMostCategoryID.setText(_translate("MainWindow", "MostCategory"))
        self.btnExcel.setText(_translate("MainWindow", "Generate Excel "))
        self.btnGenerateAndImport.setText(_translate("MainWindow", "Generate&&Import"))
        self.lblFrom.setText(_translate("MainWindow", "FROM YEAR"))
        self.lblFromMonth.setText(_translate("MainWindow", "MONTH"))
        self.lblFromDay.setText(_translate("MainWindow", "DAY"))
        self.lblTo.setText(_translate("MainWindow", "  TO YEAR"))
        self.lblToMonth.setText(_translate("MainWindow", "MONTH"))
        self.lblToDay.setText(_translate("MainWindow", "DAY"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabReports), _translate("MainWindow", "Reports"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
