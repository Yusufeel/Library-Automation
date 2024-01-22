from PyQt6 import uic

with open("../Menu_Ekrani.py", "w", encoding='utf-8') as pencere:
    uic.compileUi("menu.ui",pencere)
