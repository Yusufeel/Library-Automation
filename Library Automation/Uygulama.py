from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from Bilgi_Ekrani import *
from Giris_Paneli import *
from Kayit_Ekrani import *
from Menu_Ekrani import *
import sqlite3
import sys

con = sqlite3.connect("Kutuphane.db")
crsr = con.cursor()


class Giris_Paneli(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Login_Screen()
        self.ui.setupUi(self)
        self.ui.btn_giris.clicked.connect(self.Giris_Kontrol)

    def Giris_Kontrol(self):
        ka = self.ui.txt_ka.text()
        sfr = self.ui.txt_sfr.text()
        crsr.execute(f"SELECT * FROM Kullanicilar WHERE Kullanici_Adi = '{ka}' AND Kullanici_Sifre = '{sfr}'")
        kisi = crsr.fetchone()

        if kisi:
            QMessageBox.information(None, "Bilgi", "GİRİŞ BAŞARILI")
            self.hide()
            self.menu=Menu_Ekrani()
            self.menu.show()
        else:
            QMessageBox.critical(None, "Bilgi", "GİRİŞ BAŞARISIZ")
class Menu_Ekrani(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Menu_Screen()
        self.ui.setupUi(self)
        self.ui.btn_kitap_ekle.clicked.connect(self.Kitap_Ekle_EkraniAc)
        self.ui.btn_kitap_bilgileri.clicked.connect(self.Kitap_Bilgileri_EkraniAc)
    def Kitap_Ekle_EkraniAc(self):
        self.hide()
        self.kitap_ekle=Kayit_Ekrani()
        self.kitap_ekle.show()
    def Kitap_Bilgileri_EkraniAc(self):
        self.hide()
        self.kitap_bilgi = Bilgi_Ekrani()
        self.kitap_bilgi.show()
class Kayit_Ekrani(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Kayit_Ekrani()
        self.ui.setupUi(self)
        self.ui.btn_kaydet.clicked.connect(self.Kitap_Kaydet)
        kategoriler = [" ","Bilim Kurgu", "Polisiye", "Fantastik","Dünya Klasikleri","Türk Klasikleri","Siyasi","Eğitim"]
        self.ui.cmb_kategori_kayit.addItems(kategoriler)
    def Kitap_Kaydet(self):
        kitap=self.ui.txt_ad_kayit.text()
        yazar=self.ui.txt_yazar_kayit.text()
        yayinevi=self.ui.txt_yayinevi_kayit.text()
        seri_no=self.ui.txt_serino_kayit.text()
        kategori=self.ui.cmb_kategori_kayit.currentText()
        teslim_tarihi=self.ui.teslimTarihiDateEdit.date().toString("yyyy-mm-dd")
        crsr.execute(f"insert into Kitaplar('KtpSeriNo','KtpAd','YzrAd','YayınEvi','Kategori','TeslimTarihi') values('{seri_no}','{kitap}','{yazar}','{yayinevi}','{kategori}','{teslim_tarihi}') ")
        con.commit()

class Bilgi_Ekrani(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Bilgi_Ekrani()
        self.ui.setupUi(self)
        self.HerKitabiGetir()
        self.ui.pushButton.clicked.connect(self.KitapAra)
        self.ui.tableWidget.cellClicked.connect(self.HucredenVeriAl)

    def HerKitabiGetir(self):
        crsr.execute("Select * from Kitaplar")
        veriler=crsr.fetchall()
        basliklar=[baslik[0] for baslik in crsr.description]
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.tableWidget.setRowCount(len(veriler))
        self.ui.tableWidget.setColumnCount(len(veriler[0]))

        for sutun_sayisi, baslik in enumerate(basliklar):
            item = QTableWidgetItem(baslik)
            self.ui.tableWidget.setHorizontalHeaderItem(sutun_sayisi, item)

        for satir_sayisi, satir_verileri in enumerate(veriler):
            for sutun_sayisi, kitap_verisi in enumerate(satir_verileri):
                item = QTableWidgetItem(str(kitap_verisi))
                self.ui.tableWidget.setItem(satir_sayisi, sutun_sayisi, item)


    def KitapAra(self):
        if(self.ui.sERINObilgi.text().strip()==""):
            crsr.execute("Select * from Kitaplar")
            veriler=crsr.fetchall()
            self.ui.tableWidget.setRowCount(len(veriler))
            self.ui.tableWidget.setColumnCount(len(veriler[0]))

            for satir_sayisi, satir_verileri in enumerate(veriler):
                for sutun_sayisi, kitap_verisi in enumerate(satir_verileri):
                    item = QTableWidgetItem(str(kitap_verisi))
                    self.ui.tableWidget.setItem(satir_sayisi, sutun_sayisi, item)
        else:
            seri_no=self.ui.sERINObilgi.text()
            crsr.execute(f"Select * from Kitaplar where KtpSeriNo='{seri_no}'")
            kitap=crsr.fetchall()
            self.ui.tableWidget.setRowCount(len(kitap))
            self.ui.tableWidget.setColumnCount(len(kitap[0]))

            for satir_sayisi, satir_verileri in enumerate(kitap):
                for sutun_sayisi, kitap_verisi in enumerate(satir_verileri):
                    item = QTableWidgetItem(str(kitap_verisi))
                    self.ui.tableWidget.setItem(satir_sayisi, sutun_sayisi, item)

            self.ui.sERINObilgi.setText("")


    def HucredenVeriAl(self,satir):
        satir_verisi=[]
        for i in range(self.ui.tableWidget.columnCount()):
            item=self.ui.tableWidget.item(satir,i)
            if item is not None:
                satir_verisi.append(item.text())
            else:
                satir_verisi.append(None)

        print(satir_verisi)
        self.ui.kITAPIDLineEdit.setText(satir_verisi[0])
        self.ui.sERINOguncel.setText(satir_verisi[1])
        self.ui.kITAPADILineEdit.setText(satir_verisi[2])
        self.ui.yAZARADILineEdit.setText(satir_verisi[3])
        self.ui.yAYINEVILineEdit.setText(satir_verisi[4])
        self.ui.kITAPTESLIMComboBox.setCurrentText(satir_verisi[5])
        self.ui.dateEdit.setSpecialValueText(satir_verisi[6])

def Uygulama():
    app = QApplication(sys.argv)
    pencere = Giris_Paneli()
    pencere.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    Uygulama()
