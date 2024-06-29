# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expense.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_Dialog(object):
    def setupUi(self, Dialog, listValues):
        Dialog.setObjectName("Dialog")
        Dialog.resize(521, 514)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(160, 430, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 70, 441, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.txtAmount = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtAmount.setObjectName("txtAmount")
        self.gridLayout.addWidget(self.txtAmount, 5, 1, 1, 1)
        self.lblCategoryID = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblCategoryID.setObjectName("lblCategoryID")
        self.gridLayout.addWidget(self.lblCategoryID, 2, 0, 1, 1)
        self.txtExpense = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtExpense.setObjectName("txtExpense")
        self.gridLayout.addWidget(self.txtExpense, 4, 1, 1, 1)
        self.lblExpenseID = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblExpenseID.setObjectName("lblExpenseID")
        self.gridLayout.addWidget(self.lblExpenseID, 1, 0, 1, 1)
        self.lblExpense = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblExpense.setObjectName("lblExpense")
        self.gridLayout.addWidget(self.lblExpense, 4, 0, 1, 1)
        self.txtExpenseID = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtExpenseID.setObjectName("txtExpenseID")
        self.txtExpenseID.setReadOnly(True)
        self.gridLayout.addWidget(self.txtExpenseID, 1, 1, 1, 1)
        self.lblExpenseDate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblExpenseDate.setObjectName("lblExpenseDate")
        self.gridLayout.addWidget(self.lblExpenseDate, 3, 0, 1, 1)
        self.lblAmount = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblAmount.setObjectName("lblAmount")
        self.gridLayout.addWidget(self.lblAmount, 5, 0, 1, 1)
        self.lblNotes = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblNotes.setObjectName("lblNotes")
        self.gridLayout.addWidget(self.lblNotes, 6, 0, 1, 1)
        self.txtNotes = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtNotes.setObjectName("txtNotes")
        self.gridLayout.addWidget(self.txtNotes, 6, 1, 1, 1)
        self.cmbCategoryID = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cmbCategoryID.setObjectName("cmbCategoryID")
        self.gridLayout.addWidget(self.cmbCategoryID, 2, 1, 1, 1)
        self.timeExpenseDate = QtWidgets.QDateTimeEdit(self.gridLayoutWidget)
        self.timeExpenseDate.setObjectName("timeExpenseDate")
        self.gridLayout.addWidget(self.timeExpenseDate, 3, 1, 1, 1)

        self.timeExpenseDate.setCalendarPopup(True)    ##set CalendarPopup as true to show the pop up calendar


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.listValues = listValues
        self.initialSetup()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblCategoryID.setText(_translate("Dialog", "Category ID"))
        self.lblExpenseID.setText(_translate("Dialog", "Expense ID"))
        self.lblExpense.setText(_translate("Dialog", "Expense"))
        self.lblExpenseDate.setText(_translate("Dialog", "Expense Date"))
        self.lblAmount.setText(_translate("Dialog", "Amount"))
        self.lblNotes.setText(_translate("Dialog", "Notes"))


###################  END UI GENERATION #######################
    def initialSetup(self):
        self.setupDatabase()
        self.setComboBox()
        self.setValues()




########################################################################
#                                                                      #
#                           Events                                     #
#                                                                      #
########################################################################



    def setValues(self):
        if self.listValues == None:
            return
        self.txtExpenseID.setText(str(self.listValues[0]))
        self.cmbCategoryID.setCurrentText(str(self.listValues[1]))
        self.timeExpenseDate.setDateTime(QtCore.QDateTime.fromString(self.listValues[2], "yyyy-MM-dd HH:mm:ss"))
        self.txtExpense.setText(self.listValues[3])
        self.txtAmount.setText(self.listValues[4])
        self.txtNotes.setText(self.listValues[5])


    def getValues(self):
        listResult = []
        listResult.append(self.txtExpenseID.text())
        listResult.append(self.cmbCategoryID.currentText())  # 获取选定项目的 category ID
        listResult.append(self.timeExpenseDate.text())
        listResult.append(self.txtExpense.text())
        listResult.append(self.txtAmount.text())
        listResult.append(self.txtNotes.text())

        return listResult




########################################################################
#                                                                      #
#                           DATABASE                                   #
#                                                                      #
########################################################################


    def setupDatabase(self):
        self.connect()
        print("-----Database Connected-----")

    def connect(self):
        self.cnx = mysql.connector.connect(user="root",
                                           password="12345678",
                                           host="127.0.0.1",
                                           database="homework04")

    def setComboBox(self):
        if self.cnx:
            cursor = self.cnx.cursor()
            query = "SELECT category_ID, category FROM categories"
            cursor.execute(query)
            results = cursor.fetchall()

            for row in results:
                item_text = []
                item_text.append("Category_ID: {")
                item_text.append(row[0])
                item_text.append("}, Category: {")
                item_text.append(row[1])
                item_text.append("}")

                inner_text = "Category_ID: {}, Category: {}".format(row[0], row[1])
                self.cmbCategoryID.addItem(inner_text, item_text[1])


            cursor.close()
            print("combobox Set")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog, None)
    Dialog.show()
    sys.exit(app.exec_())
