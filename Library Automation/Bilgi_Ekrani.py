# Form implementation generated from reading ui file 'bilgi_ekrani.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Bilgi_Ekrani(object):
    def setupUi(self, Bilgi_Ekrani):
        Bilgi_Ekrani.setObjectName("Bilgi_Ekrani")
        Bilgi_Ekrani.resize(1413, 750)
        font = QtGui.QFont()
        font.setPointSize(14)
        Bilgi_Ekrani.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=Bilgi_Ekrani)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(80, 100, 471, 461))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 30, 361, 291))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.kITAPIDLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.kITAPIDLabel.setFont(font)
        self.kITAPIDLabel.setObjectName("kITAPIDLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.kITAPIDLabel)
        self.kITAPIDLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.kITAPIDLineEdit.setObjectName("kITAPIDLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.kITAPIDLineEdit)
        self.SERINOguncel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SERINOguncel.setFont(font)
        self.SERINOguncel.setObjectName("SERINOguncel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.SERINOguncel)
        self.sERINOguncel = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.sERINOguncel.setObjectName("sERINOguncel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.sERINOguncel)
        self.kITAPADILabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.kITAPADILabel.setFont(font)
        self.kITAPADILabel.setObjectName("kITAPADILabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.kITAPADILabel)
        self.kITAPADILineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.kITAPADILineEdit.setObjectName("kITAPADILineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.kITAPADILineEdit)
        self.yAZARADILabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.yAZARADILabel.setFont(font)
        self.yAZARADILabel.setObjectName("yAZARADILabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.yAZARADILabel)
        self.yAZARADILineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.yAZARADILineEdit.setObjectName("yAZARADILineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.yAZARADILineEdit)
        self.yAYINEVILabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.yAYINEVILabel.setFont(font)
        self.yAYINEVILabel.setObjectName("yAYINEVILabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.yAYINEVILabel)
        self.yAYINEVILineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.yAYINEVILineEdit.setObjectName("yAYINEVILineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.yAYINEVILineEdit)
        self.kITAPTESLIMLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.kITAPTESLIMLabel.setFont(font)
        self.kITAPTESLIMLabel.setObjectName("kITAPTESLIMLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.kITAPTESLIMLabel)
        self.kITAPTESLIMComboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.kITAPTESLIMComboBox.setObjectName("kITAPTESLIMComboBox")
        self.kITAPTESLIMComboBox.addItem("")
        self.kITAPTESLIMComboBox.addItem("")
        self.kITAPTESLIMComboBox.addItem("")
        self.kITAPTESLIMComboBox.addItem("")
        self.kITAPTESLIMComboBox.addItem("")
        self.kITAPTESLIMComboBox.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.kITAPTESLIMComboBox)
        self.tESLIMTARIHILabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tESLIMTARIHILabel.setFont(font)
        self.tESLIMTARIHILabel.setObjectName("tESLIMTARIHILabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.tESLIMTARIHILabel)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.formLayoutWidget)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dateEdit)
        self.btn_sil = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        self.btn_sil.setObjectName("btn_sil")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.btn_sil)
        self.btn_guncelle = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        self.btn_guncelle.setObjectName("btn_guncelle")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.btn_guncelle)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(590, 100, 741, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(610, 490, 421, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(parent=self.groupBox_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(50, 30, 311, 91))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.SERINOBILGI = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.SERINOBILGI.setObjectName("SERINOBILGI")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.SERINOBILGI)
        self.sERINObilgi = QtWidgets.QLineEdit(parent=self.formLayoutWidget_2)
        self.sERINObilgi.setObjectName("sERINObilgi")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.sERINObilgi)
        self.pushButton = QtWidgets.QPushButton(parent=self.formLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pushButton)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 10, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_geri = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_geri.setGeometry(QtCore.QRect(30, 10, 121, 41))
        self.btn_geri.setObjectName("btn_geri")
        Bilgi_Ekrani.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Bilgi_Ekrani)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1413, 31))
        self.menubar.setObjectName("menubar")
        Bilgi_Ekrani.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Bilgi_Ekrani)
        self.statusbar.setObjectName("statusbar")
        Bilgi_Ekrani.setStatusBar(self.statusbar)

        self.retranslateUi(Bilgi_Ekrani)
        self.kITAPTESLIMComboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Bilgi_Ekrani)

    def retranslateUi(self, Bilgi_Ekrani):
        _translate = QtCore.QCoreApplication.translate
        Bilgi_Ekrani.setWindowTitle(_translate("Bilgi_Ekrani", "MainWindow"))
        self.groupBox.setTitle(_translate("Bilgi_Ekrani", "KİTAP İŞLEMLERİ"))
        self.kITAPIDLabel.setText(_translate("Bilgi_Ekrani", "KITAP ID"))
        self.SERINOguncel.setText(_translate("Bilgi_Ekrani", "SERI NO"))
        self.kITAPADILabel.setText(_translate("Bilgi_Ekrani", "KITAP ADI"))
        self.yAZARADILabel.setText(_translate("Bilgi_Ekrani", "YAZAR ADI"))
        self.yAYINEVILabel.setText(_translate("Bilgi_Ekrani", "YAYIN EVI"))
        self.kITAPTESLIMLabel.setText(_translate("Bilgi_Ekrani", "KATEGORILER"))
        self.kITAPTESLIMComboBox.setItemText(0, _translate("Bilgi_Ekrani", "BİLİM KURGU"))
        self.kITAPTESLIMComboBox.setItemText(1, _translate("Bilgi_Ekrani", "PSİKOLOJİ"))
        self.kITAPTESLIMComboBox.setItemText(2, _translate("Bilgi_Ekrani", "EĞİTİM"))
        self.kITAPTESLIMComboBox.setItemText(3, _translate("Bilgi_Ekrani", "DÜNYA KLASİKLERİ"))
        self.kITAPTESLIMComboBox.setItemText(4, _translate("Bilgi_Ekrani", "TÜRK KLASİKLERİ"))
        self.kITAPTESLIMComboBox.setItemText(5, _translate("Bilgi_Ekrani", "FANTEZİ"))
        self.tESLIMTARIHILabel.setText(_translate("Bilgi_Ekrani", "TESLIM TARIHI"))
        self.btn_sil.setText(_translate("Bilgi_Ekrani", "SİL"))
        self.btn_guncelle.setText(_translate("Bilgi_Ekrani", "GÜNCELLE"))
        self.groupBox_2.setTitle(_translate("Bilgi_Ekrani", "KİTAP ARA"))
        self.SERINOBILGI.setText(_translate("Bilgi_Ekrani", "SERI NO"))
        self.pushButton.setText(_translate("Bilgi_Ekrani", "ARA"))
        self.label.setText(_translate("Bilgi_Ekrani", "BİLGİ EKRANI"))
        self.btn_geri.setText(_translate("Bilgi_Ekrani", "GERİ"))