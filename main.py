#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main entry point untuk aplikasi GSO
"""

import sys
from PyQt5 import QtWidgets
from login import Ui_MainWindow as Login_UI

def main():
    """Fungsi utama untuk menjalankan aplikasi"""
    app = QtWidgets.QApplication(sys.argv)
    
    # Set style sheet untuk aplikasi (opsional)
    app.setStyle("Fusion")
    
    # Buat window login
    main_window = QtWidgets.QMainWindow()
    ui = Login_UI()
    ui.setupUi(main_window)
    
    # Tampilkan window login
    main_window.show()
    
    # Jalankan aplikasi
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 