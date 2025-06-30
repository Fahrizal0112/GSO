from PyQt5 import QtCore, QtGui, QtWidgets
from settings import Ui_MainWindow as Settings_UI
from step2 import Ui_MainWindow as Step2_UI
import datetime
import cv2
import numpy as np
import json
import os
import glob
from PyQt5.QtWidgets import QMessageBox, QAction, QMenu


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1470, 820)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 570, 1461, 51))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()                                    
        icon.addPixmap(QtGui.QPixmap("../../../../Downloads/setting-5-svgrepo-com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 90, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 1171, 41))
        self.label_2.setStyleSheet("background-color: red;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"qproperty-alignment: \'AlignCenter\';\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 1451, 41))
        self.label_3.setStyleSheet("background-color: black;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"qproperty-alignment: \'AlignCenter\';\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1360, 10, 60, 16))
        self.label_4.setObjectName("label_4")
        self.labelTime = QtWidgets.QLabel(self.centralwidget)
        self.labelTime.setGeometry(QtCore.QRect(10, 20, 221, 16))
        self.labelTime.setObjectName("labelTime")
        self.frame = QtWidgets.QLabel(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(250, 160, 701, 391))
        self.frame.setText("")
        self.frame.setObjectName("frame")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(220, 650, 91, 61))
        self.toolButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../Downloads/play-svgrepo-com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(20, 20))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(690, 650, 91, 61))
        self.toolButton_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../Downloads/stop-svgrepo-com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon2)
        self.toolButton_2.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(1170, 650, 91, 61))
        self.toolButton_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../Downloads/camera-svgrepo-com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon3)
        self.toolButton_3.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_3.setObjectName("toolButton_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1240, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1200, 130, 251, 71))
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1200, 270, 251, 71))
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1210, 230, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1200, 390, 251, 71))
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1270, 350, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 140, 60, 16))
        self.label_11.setObjectName("label_11")
        # self.filterButton = QtWidgets.QPushButton(self.centralwidget)
        # self.filterButton.setGeometry(QtCore.QRect(960, 650, 120, 61))
        # self.filterButton.setText("Filter Mode")
        # self.filterButton.setObjectName("filterButton")
        # self.filterButton.clicked.connect(self.toggle_filter_mode)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 140, 1171, 20))
        self.label_12.setStyleSheet("background-color: black;\n"
                           "color: white;\n"
                           "font-weight: bold;\n"
                           "font-size: 12pt;\n"
                           "qproperty-alignment: \'AlignCenter\';\n")
        self.label_12.setText("PATTERN 1")
        self.label_12.setObjectName("label_12")
        
        # Inisialisasi nilai threshold SEBELUM membuat komponen UI yang menggunakannya
        self.template_matching_threshold = 0.5
        
        # Container untuk progress bar dan threshold indicator
        self.progress_container = QtWidgets.QFrame(self.centralwidget)
        self.progress_container.setGeometry(QtCore.QRect(1200, 480, 251, 40))
        self.progress_container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.progress_container.setObjectName("progress_container")
        
        # Progress bar untuk nilai kecocokan
        self.match_progress_bar = QtWidgets.QProgressBar(self.progress_container)
        self.match_progress_bar.setGeometry(QtCore.QRect(0, 0, 251, 40))
        self.match_progress_bar.setMinimum(0)
        self.match_progress_bar.setMaximum(100)
        self.match_progress_bar.setValue(0)
        self.match_progress_bar.setTextVisible(True)
        self.match_progress_bar.setFormat("%v%")
        self.match_progress_bar.setObjectName("match_progress_bar")
        
        # Styling progress bar dengan warna hijau saja
        self.match_progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid grey;
                border-radius: 5px;
                text-align: center;
                font-size: 16pt;
                font-weight: bold;
                background-color: #f0f0f0;
            }
            
            QProgressBar::chunk {
                background-color: #00AA00;  /* Warna hijau solid */
            }
        """)
        
        # Kotak indikator threshold
        self.threshold_box = QtWidgets.QFrame(self.progress_container)
        self.threshold_box.setObjectName("threshold_box")
        self.threshold_box.setStyleSheet("background-color: transparent; border: 3px solid black;")
        
        # Label untuk nilai persentase di bawah progress bar
        self.label_match_percentage = QtWidgets.QLabel(self.centralwidget)
        self.label_match_percentage.setGeometry(QtCore.QRect(1200, 525, 251, 30))
        self.label_match_percentage.setStyleSheet("font-size: 14pt; font-weight: bold; qproperty-alignment: 'AlignCenter';")
        self.label_match_percentage.setText("0.00%")
        self.label_match_percentage.setObjectName("label_match_percentage")
        
        # Label judul untuk nilai kecocokan
        self.label_match_title = QtWidgets.QLabel(self.centralwidget)
        self.label_match_title.setGeometry(QtCore.QRect(1200, 450, 251, 30))
        self.label_match_title.setStyleSheet("font-size: 14pt; font-weight: bold; qproperty-alignment: 'AlignCenter';")
        self.label_match_title.setText("Nilai Kecocokan")
        self.label_match_title.setObjectName("label_match_title")
        
        # # Label nilai threshold
        # self.label_threshold_marker = QtWidgets.QLabel(self.centralwidget)
        # self.label_threshold_marker.setGeometry(QtCore.QRect(1200, 455, 251, 20))
        # self.label_threshold_marker.setStyleSheet("font-size: 10pt; color: #555; font-weight: bold; qproperty-alignment: 'AlignRight';")
        # self.label_threshold_marker.setText(f"Threshold: {int(self.template_matching_threshold * 100)}%")
        # self.label_threshold_marker.setObjectName("label_threshold_marker")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1470, 36))
        self.menubar.setObjectName("menubar")
        self.menuChange_Password = QtWidgets.QMenu(self.menubar)
        self.menuChange_Password.setObjectName("menuChange_Password")
        self.menuModels = QtWidgets.QMenu(self.menubar)
        self.menuModels.setObjectName("menuModels")
        self.menuModels.setTitle("Models")
        self.menuUser = QtWidgets.QMenu(self.menubar)
        self.menuUser.setObjectName("menuUser")
        self.menuCamera = QtWidgets.QMenu(self.menubar)
        self.menuCamera.setObjectName("menuCamera")
        self.menuPattern = QtWidgets.QMenu(self.menubar)
        self.menuPattern.setObjectName("menuPattern")
        self.menuPattern.setTitle("Pattern")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionModel_1 = QtWidgets.QAction(MainWindow)
        self.actionModel_1.setObjectName("actionModel_1")
        self.actionModel_2 = QtWidgets.QAction(MainWindow)
        self.actionModel_2.setObjectName("actionModel_2")
        self.actionModel_3 = QtWidgets.QAction(MainWindow)
        self.actionModel_3.setObjectName("actionModel_3")
        self.actionModel_4 = QtWidgets.QAction(MainWindow)
        self.actionModel_4.setObjectName("actionModel_4")
        self.actionModel_5 = QtWidgets.QAction(MainWindow)
        self.actionModel_5.setObjectName("actionModel_5")
        self.actionPattern_1 = QAction(MainWindow)
        self.actionPattern_1.setText("Pattern 1")
        self.actionPattern_1.setObjectName("actionPattern_1")
        self.actionPattern_2 = QAction(MainWindow)
        self.actionPattern_2.setText("Pattern 2")
        self.actionPattern_2.setObjectName("actionPattern_2")
        self.actionPattern_3 = QAction(MainWindow)
        self.actionPattern_3.setText("Pattern 3")
        self.actionPattern_3.setObjectName("actionPattern_3")
        self.actionPattern_4 = QAction(MainWindow)
        self.actionPattern_4.setText("Pattern 4")
        self.actionPattern_4.setObjectName("actionPattern_4")
        self.actionPattern_5 = QAction(MainWindow)
        self.actionPattern_5.setText("Pattern 5")
        self.actionPattern_5.setObjectName("actionPattern_5")
        self.actionCamera_0 = QtWidgets.QAction(MainWindow)
        self.actionCamera_0.setObjectName("actionCamera_0")
        self.actionCamera_1 = QtWidgets.QAction(MainWindow)
        self.actionCamera_1.setObjectName("actionCamera_1")
        self.actionCamera_2 = QtWidgets.QAction(MainWindow)
        self.actionCamera_2.setObjectName("actionCamera_2")
        self.actionCamera_3 = QtWidgets.QAction(MainWindow)
        self.actionCamera_3.setObjectName("actionCamera_3")
        self.actionRefresh_Cameras = QtWidgets.QAction(MainWindow)
        self.actionRefresh_Cameras.setObjectName("actionRefresh_Cameras")
        
        self.camera_index = 0
        self.available_cameras = []

        # Tambahkan actions ke menu Camera
        self.menuCamera.addAction(self.actionCamera_0)
        self.menuCamera.addAction(self.actionCamera_1)
        self.menuCamera.addAction(self.actionCamera_2)
        self.menuCamera.addAction(self.actionCamera_3)
        self.menuCamera.addSeparator()
        self.menuCamera.addAction(self.actionRefresh_Cameras)
        
        self.menuModels.addAction(self.actionModel_1)
        self.menuModels.addAction(self.actionModel_2)
        self.menuModels.addAction(self.actionModel_3)
        self.menuModels.addAction(self.actionModel_4)
        self.menuModels.addAction(self.actionModel_5)
        self.menubar.addAction(self.menuChange_Password.menuAction())
        self.menubar.addAction(self.menuModels.menuAction())
        self.menubar.addAction(self.menuUser.menuAction())
        self.menubar.addAction(self.menuCamera.menuAction())
        self.menubar.addAction(self.menuPattern.menuAction())

        # Tambahkan pattern ke menu Pattern, bukan menu Models
        self.menuPattern.addAction(self.actionPattern_1)
        self.menuPattern.addAction(self.actionPattern_2)
        self.menuPattern.addAction(self.actionPattern_3)
        self.menuPattern.addAction(self.actionPattern_4)
        self.menuPattern.addAction(self.actionPattern_5)

        self.MainWindow = MainWindow
        
        self.process_active = False
        self.idle_start_time = datetime.datetime.now()
        
        self.pushButton_4.clicked.connect(self.open_settings)
        
        self.toolButton_3.clicked.connect(self.toggle_camera)
        
        self.toolButton.clicked.connect(self.start_process)
        self.toolButton_2.clicked.connect(self.stop_process)
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()
        
        self.camera = None
        self.camera_active = False
        self.camera_timer = QtCore.QTimer()
        self.camera_timer.timeout.connect(self.update_camera)
        
        self.camera_geometry = {
            "x": 250,
            "y": 160,
            "width": 701,
            "height": 391
        }
        
        # Inisialisasi ROI dengan ukuran yang lebih besar
        roi_width = 300
        roi_height = 300
        
        roi_x = self.camera_geometry["x"] + (self.camera_geometry["width"] - roi_width) // 2
        roi_y = self.camera_geometry["y"] + (self.camera_geometry["height"] - roi_height) // 2
        
        # Hanya gunakan satu ROI untuk deteksi
        self.roi = {"x": roi_x, "y": roi_y, "w": roi_width, "h": roi_height}
        
        # Simpan hasil inspeksi terakhir
        self.last_inspection_result = None
        
        self.frame.setMouseTracking(True)
        self.frame.mousePressEvent = self.mouse_press_event
        self.frame.mouseReleaseEvent = self.mouse_release_event
        self.frame.mouseMoveEvent = self.mouse_move_event
        
        self.label_6.setText("IDLE")
        self.label_7.setText("WAITING")
        self.label_9.setText("0")
        
        # Inisialisasi semua atribut terlebih dahulu
        self.models_dir = "models"
        self.current_model = 1
        self.current_pattern = 1
        self.templates = {}
        
        # Load nama model terlebih dahulu
        self.model_names = {}
        self.load_model_names()
        
        # Load nama pattern
        self.pattern_names = {}
        self.load_pattern_names()
        
        # Kamus untuk menyimpan ROI per model dan pattern
        self.roi_per_pattern = {}
        
        # Load ROI dari file jika ada
        self.load_roi_settings()
        
        # Kemudian load templates
        self.load_templates()
        
        # Update label setelah semua inisialisasi selesai
        self.update_model_label()
        self.update_pattern_label()
        
        self.actionModel_1.triggered.connect(lambda: self.select_model(1))
        self.actionModel_2.triggered.connect(lambda: self.select_model(2))
        self.actionModel_3.triggered.connect(lambda: self.select_model(3))
        self.actionModel_4.triggered.connect(lambda: self.select_model(4))
        self.actionModel_5.triggered.connect(lambda: self.select_model(5))
        
        # Koneksi action Pattern ke fungsi handler
        self.actionPattern_1.triggered.connect(lambda: self.select_pattern(1))
        self.actionPattern_2.triggered.connect(lambda: self.select_pattern(2))
        self.actionPattern_3.triggered.connect(lambda: self.select_pattern(3))
        self.actionPattern_4.triggered.connect(lambda: self.select_pattern(4))
        self.actionPattern_5.triggered.connect(lambda: self.select_pattern(5))
        
        # Koneksi actions kamera
        self.actionCamera_0.triggered.connect(lambda: self.select_camera(0))
        self.actionCamera_1.triggered.connect(lambda: self.select_camera(1))
        self.actionCamera_2.triggered.connect(lambda: self.select_camera(2))
        self.actionCamera_3.triggered.connect(lambda: self.select_camera(3))
        self.actionRefresh_Cameras.triggered.connect(self.refresh_cameras)
        
        # Refresh daftar kamera saat startup
        self.refresh_cameras()
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Inisialisasi nilai kecocokan
        self.current_match_value = 0.0
        
        # Update tampilan threshold
        self.update_threshold_marker()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "Setting"))
        self.label.setText(_translate("MainWindow", "STEP: 1"))
        self.label_2.setText(_translate("MainWindow", "FAIL"))
        self.label_3.setText(_translate("MainWindow", "K0WL EXPORT"))
        self.label_4.setText(_translate("MainWindow", "Admin"))
        self.labelTime.setText(_translate("MainWindow", "LabelTime"))
        self.toolButton.setText(_translate("MainWindow", "RUN"))
        self.toolButton_2.setText(_translate("MainWindow", "STOP"))
        self.toolButton_3.setText(_translate("MainWindow", "CAMERA"))
        self.label_5.setText(_translate("MainWindow", "STEP PROCESS"))
        self.label_8.setText(_translate("MainWindow", "INSPECTION RESULT"))
        self.label_10.setText(_translate("MainWindow", "IDLE TIME"))
        self.label_11.setText(_translate("MainWindow", "STEP 1"))
        self.menuChange_Password.setTitle(_translate("MainWindow", "Change Password"))
        self.menuModels.setTitle(_translate("MainWindow", "Models"))
        self.menuUser.setTitle(_translate("MainWindow", "User"))
        self.menuCamera.setTitle(_translate("MainWindow", "Camera"))
        self.actionModel_1.setText(_translate("MainWindow", "Model 1"))
        self.actionModel_2.setText(_translate("MainWindow", "Model 2"))
        self.actionModel_3.setText(_translate("MainWindow", "Model 3"))
        self.actionModel_4.setText(_translate("MainWindow", "Model 4"))
        self.actionModel_5.setText(_translate("MainWindow", "Model 5"))
        self.actionPattern_1.setText(_translate("MainWindow", "Pattern 1"))
        self.actionPattern_2.setText(_translate("MainWindow", "Pattern 2"))
        self.actionPattern_3.setText(_translate("MainWindow", "Pattern 3"))
        self.actionPattern_4.setText(_translate("MainWindow", "Pattern 4"))
        self.actionPattern_5.setText(_translate("MainWindow", "Pattern 5"))
        self.label_12.setText(_translate("MainWindow", "PATTERN 1"))
        self.label_match_title.setText(_translate("MainWindow", "Nilai Kecocokan"))

        # Set text untuk actions kamera
        self.actionCamera_0.setText(_translate("MainWindow", "Camera 0"))
        self.actionCamera_1.setText(_translate("MainWindow", "Camera 1"))
        self.actionCamera_2.setText(_translate("MainWindow", "Camera 2"))
        self.actionCamera_3.setText(_translate("MainWindow", "Camera 3"))
        self.actionRefresh_Cameras.setText(_translate("MainWindow", "Refresh Cameras"))

    def open_settings(self):
        if self.process_active:
            QMessageBox.warning(self.MainWindow, "Peringatan", 
                              "Harap hentikan proses deteksi terlebih dahulu sebelum membuka pengaturan.")
            return
        
        self.settings_window = QtWidgets.QMainWindow()
        self.settings_ui = Settings_UI()
        self.settings_ui.setupUi(self.settings_window)
        
        self.settings_ui.toolButton_2.clicked.connect(self.get_roi_from_settings)
        
        self.settings_ui.toolButton_3.clicked.connect(self.adjust_roi_center)
        
        self.settings_ui.label_6.setText(str(self.roi["x"]))
        self.settings_ui.label_12.setText(str(self.roi["y"]))
        self.settings_ui.label_8.setText(str(self.roi["w"]))
        self.settings_ui.label_11.setText(str(self.roi["h"]))
        
        self.settings_ui.textEdit_2.setText(f"{self.template_matching_threshold*100:.2f}%")
        
        if hasattr(self.settings_ui, 'label_17'):
            self.settings_ui.label_17.setText(f"Threshold saat ini: {self.template_matching_threshold*100:.2f}%")
        
        self.settings_ui.comboBox.setCurrentIndex(self.current_model - 1)
        
        self.settings_ui.toolButton_3.clicked.connect(self.save_settings)
        
        # Set nama model saat ini ke textEdit
        model_name = self.model_names.get(str(self.current_model), f"Model {self.current_model}")
        self.settings_ui.textEdit.setText(model_name)
        
        # Tambahkan informasi pattern ke settings UI
        self.settings_ui.comboBox_2 = QtWidgets.QComboBox(self.settings_ui.centralwidget)
        self.settings_ui.comboBox_2.setGeometry(QtCore.QRect(1020, 460, 191, 26))
        self.settings_ui.comboBox_2.setObjectName("comboBox_2")
        for i in range(1, 6):
            self.settings_ui.comboBox_2.addItem(f"{i}")
        
        self.settings_ui.label_18 = QtWidgets.QLabel(self.settings_ui.centralwidget)
        self.settings_ui.label_18.setGeometry(QtCore.QRect(890, 460, 101, 16))
        self.settings_ui.label_18.setText("Pattern :")
        self.settings_ui.label_18.setObjectName("label_18")
        
        # Set current pattern
        self.settings_ui.comboBox_2.setCurrentIndex(self.current_pattern - 1)
        
        # Set nama pattern saat ini ke textEdit
        model_key = str(self.current_model)
        pattern_key = str(self.current_pattern)
        if model_key in self.pattern_names and pattern_key in self.pattern_names[model_key]:
            pattern_name = self.pattern_names[model_key][pattern_key]
        else:
            pattern_name = f"Pattern {self.current_pattern}"
        
        self.settings_ui.textEdit_3 = QtWidgets.QTextEdit(self.settings_ui.centralwidget)
        self.settings_ui.textEdit_3.setGeometry(QtCore.QRect(1020, 490, 181, 31))
        self.settings_ui.textEdit_3.setObjectName("textEdit_3")
        self.settings_ui.textEdit_3.setText(pattern_name)
        
        self.settings_ui.label_19 = QtWidgets.QLabel(self.settings_ui.centralwidget)
        self.settings_ui.label_19.setGeometry(QtCore.QRect(890, 490, 121, 16))
        self.settings_ui.label_19.setText("Nama Pattern :")
        self.settings_ui.label_19.setObjectName("label_19")
        
        # Connect pattern combobox
        self.settings_ui.comboBox_2.currentIndexChanged.connect(self.settings_pattern_changed)
        
        self.settings_window.show()
    
    def toggle_camera(self):
        if self.camera_active:
            self.stop_camera()
        else:
            self.start_camera()
    
    def start_camera(self):
        if self.camera is None:
            self.camera = cv2.VideoCapture(self.camera_index)
            if not self.camera.isOpened():
                print(f"Error: Tidak dapat membuka kamera {self.camera_index}")
                QMessageBox.critical(self.MainWindow, "Error", 
                                   f"Tidak dapat membuka Camera {self.camera_index}!")
                return
            else:
                print(f"Kamera {self.camera_index} berhasil dibuka")
        
        self.camera_active = True
        self.camera_timer.start(30)
        self.toolButton_3.setText("STOP CAMERA")
        
        QtCore.QTimer.singleShot(500, self.center_roi)

    def center_roi(self):
        """Tempatkan ROI di tengah dengan ukuran yang fleksibel"""
        # Gunakan ukuran yang proporsional dengan ukuran frame
        frame_width = self.camera_geometry["width"]
        frame_height = self.camera_geometry["height"]
        
        # Ukuran ROI sekitar 60% dari ukuran frame (bisa disesuaikan)
        roi_width = int(frame_width * 0.6)
        roi_height = int(frame_height * 0.6)
        
        # Hitung posisi tengah
        roi_x = (frame_width - roi_width) // 2
        roi_y = (frame_height - roi_height) // 2
        
        # Pastikan ROI berada dalam batas frame
        roi_x = max(0, roi_x)
        roi_y = max(0, roi_y)
        roi_width = min(roi_width, frame_width - roi_x)
        roi_height = min(roi_height, frame_height - roi_y)
        
        self.roi = {"x": roi_x, "y": roi_y, "w": roi_width, "h": roi_height}
        
        print(f"ROI berhasil ditempatkan di tengah dengan ukuran {roi_width}x{roi_height}: x={self.roi['x']}, y={self.roi['y']}, w={self.roi['w']}, h={self.roi['h']}")
    
    def stop_camera(self):
        self.camera_active = False
        self.camera_timer.stop()
        self.toolButton_3.setText("CAMERA")
        blank_image = np.zeros((self.frame.height(), self.frame.width(), 3), dtype=np.uint8)
        self.display_image(blank_image)
        
        # Tutup kamera
        if self.camera is not None:
            self.camera.release()
            self.camera = None
            print(f"Kamera {self.camera_index} ditutup")

    def update_camera(self):
        """Update tampilan kamera dengan satu bounding box untuk deteksi"""
        if self.camera_active and self.camera is not None:
            ret, frame = self.camera.read()
            if ret:
                # Konversi ke RGB untuk tampilan PyQt
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                # Resize frame sesuai dengan ukuran label
                frame_rgb = cv2.resize(frame_rgb, (self.camera_geometry["width"], self.camera_geometry["height"]))
                
                # Simpan frame saat ini
                self.current_frame = frame_rgb.copy()
                
                # Terapkan filter berdasarkan mode tampilan
                filtered_frame = self.apply_filter(frame_rgb)
                
                # Gambar ROI utama untuk deteksi dengan warna yang jelas
                cv2.rectangle(
                    filtered_frame, 
                    (self.roi["x"], self.roi["y"]), 
                    (self.roi["x"] + self.roi["w"], self.roi["y"] + self.roi["h"]), 
                    (0, 255, 0),  # Warna hijau untuk ROI utama
                    2  # Ketebalan garis yang lebih tebal
                )
                
                # Tambahkan label untuk ROI utama
                cv2.putText(
                    filtered_frame,
                    f"Detection Area (Model {self.current_model})",
                    (self.roi["x"], self.roi["y"] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    1
                )
                
                # Tampilkan hasil inspeksi terakhir jika ada
                if hasattr(self, 'last_inspection_result') and self.last_inspection_result is not None:
                    status = self.last_inspection_result.get('status', '')
                    reason = self.last_inspection_result.get('reason', '')
                    
                    if status == "OK":
                        color = (0, 255, 0)  # Hijau untuk OK
                        cv2.putText(
                            filtered_frame,
                            "OK",
                            (self.roi["x"] + 10, self.roi["y"] + 30),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            color,
                            2
                        )
                    elif status == "NG":
                        color = (0, 0, 255)  # Merah untuk NG
                        cv2.putText(
                            filtered_frame,
                            "NG",
                            (self.roi["x"] + 10, self.roi["y"] + 30),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            color,
                            2
                        )
            
                self.display_image(filtered_frame)
    
    def apply_filter(self, frame):
        """Terapkan filter pada frame berdasarkan mode yang dipilih"""
        # Jika belum ada atribut filter_mode, buat dengan nilai default 'normal'
        if not hasattr(self, 'filter_mode'):
            self.filter_mode = 'normal'
        
        # Frame asli tanpa filter
        if self.filter_mode == 'normal':
            return frame
        
        # Konversi ke grayscale untuk beberapa filter
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        
        # Edge detection dengan Canny
        if self.filter_mode == 'edges':
            edges = cv2.Canny(gray, 30, 150)
            return cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
        
        # Enhanced detail dengan CLAHE dan sharpening
        elif self.filter_mode == 'enhanced':
            # Tingkatkan kontras dengan CLAHE
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            gray_eq = clahe.apply(gray)
            
            # Sharpening untuk detail
            kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
            sharpened = cv2.filter2D(gray_eq, -1, kernel)
            
            # Deteksi tepi dengan Sobel
            sobelx = cv2.Sobel(sharpened, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(sharpened, cv2.CV_64F, 0, 1, ksize=3)
            sobel = cv2.magnitude(sobelx, sobely)
            sobel = cv2.normalize(sobel, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
            
            # Gabungkan hasil
            enhanced = cv2.cvtColor(sharpened, cv2.COLOR_GRAY2RGB)
            enhanced_color = frame.copy()
            
            # Overlay tepi pada gambar berwarna
            edge_mask = sobel > 50
            enhanced_color[edge_mask] = [0, 255, 255]  # Highlight tepi dengan warna kuning
            
            return enhanced_color
        
        # Threshold untuk menonjolkan perbedaan intensitas
        elif self.filter_mode == 'threshold':
            _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            return cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)
        
        # Hue saturation value untuk deteksi warna
        elif self.filter_mode == 'hsv':
            hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
            h, s, v = cv2.split(hsv)
            # Tingkatkan saturasi untuk melihat perbedaan warna lebih jelas
            s = cv2.multiply(s, 1.5)
            s = np.clip(s, 0, 255).astype(np.uint8)
            merged = cv2.merge([h, s, v])
            return cv2.cvtColor(merged, cv2.COLOR_HSV2RGB)
        
        # Mode default jika tidak ada yang cocok
        else:
            return frame
    
    def display_image(self, img):
        img = cv2.resize(img, (self.camera_geometry["width"], self.camera_geometry["height"]))
        
        h, w, ch = img.shape
        bytes_per_line = ch * w
        qt_image = QtGui.QImage(img.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        
        pixmap = QtGui.QPixmap.fromImage(qt_image)
        self.frame.setPixmap(pixmap)
    
    def mouse_press_event(self, event):
        """Handler untuk mouse press yang hanya mengatur ROI utama"""
        if not self.camera_active:
            return
        
        # Hitung koordinat relatif terhadap frame kamera
        # Koordinat absolut dikurangi dengan posisi frame kamera
        mouse_x = event.pos().x()
        mouse_y = event.pos().y()
        
        # Periksa apakah klik berada di dalam area frame kamera
        if (0 <= mouse_x <= self.camera_geometry["width"] and 
            0 <= mouse_y <= self.camera_geometry["height"]):
            
            # Cek apakah klik di dalam ROI
            if (self.roi["x"] <= mouse_x <= self.roi["x"] + self.roi["w"] and 
                self.roi["y"] <= mouse_y <= self.roi["y"] + self.roi["h"]):
                # Mulai drag ROI
                self.dragging_roi = True
                self.drag_start_x = mouse_x
                self.drag_start_y = mouse_y
                self.drag_roi_start = self.roi.copy()
                print(f"Mulai drag ROI dari posisi: {mouse_x}, {mouse_y}")
            else:
                # Mulai membuat ROI baru
                self.creating_roi = True
                self.roi_start_point = (mouse_x, mouse_y)
                print(f"Mulai membuat ROI baru dari posisi: {mouse_x}, {mouse_y}")
    
    def mouse_move_event(self, event):
        """Handler untuk mouse move yang hanya mengatur ROI utama"""
        if not self.camera_active:
            return
        
        # Hitung koordinat relatif terhadap frame kamera
        mouse_x = event.pos().x()
        mouse_y = event.pos().y()
        
        if hasattr(self, 'dragging_roi') and self.dragging_roi:
            # Pindahkan ROI
            dx = mouse_x - self.drag_start_x
            dy = mouse_y - self.drag_start_y
            
            self.roi["x"] = max(0, min(self.camera_geometry["width"] - self.roi["w"], 
                                      self.drag_roi_start["x"] + dx))
            self.roi["y"] = max(0, min(self.camera_geometry["height"] - self.roi["h"], 
                                      self.drag_roi_start["y"] + dy))
            
            print(f"Dragging ROI ke: {self.roi['x']}, {self.roi['y']}")
        
        elif hasattr(self, 'creating_roi') and self.creating_roi and hasattr(self, 'roi_start_point'):
            # Buat ROI baru
            start_x, start_y = self.roi_start_point
            width = mouse_x - start_x
            height = mouse_y - start_y
            
            # Update ROI sementara untuk visualisasi
            self.temp_roi = {
                "x": start_x if width >= 0 else mouse_x,
                "y": start_y if height >= 0 else mouse_y,
                "w": abs(width),
                "h": abs(height)
            }
            
            print(f"Creating ROI: {self.temp_roi}")
    
    def mouse_release_event(self, event):
        """Handler untuk mouse release yang hanya mengatur ROI utama"""
        if not self.camera_active:
            return
        
        # Hitung koordinat relatif terhadap frame kamera
        mouse_x = event.pos().x()
        mouse_y = event.pos().y()
        
        if hasattr(self, 'dragging_roi') and self.dragging_roi:
            self.dragging_roi = False
            print(f"ROI selesai dipindahkan ke: {self.roi['x']}, {self.roi['y']}")
        
        elif hasattr(self, 'creating_roi') and self.creating_roi and hasattr(self, 'temp_roi'):
            # Tetapkan ROI baru jika ukurannya valid
            if self.temp_roi["w"] > 20 and self.temp_roi["h"] > 20:
                self.roi = self.temp_roi.copy()
                print(f"ROI baru dibuat: x={self.roi['x']}, y={self.roi['y']}, w={self.roi['w']}, h={self.roi['h']}")
            else:
                print(f"ROI terlalu kecil, minimal 20x20 piksel")
            
            self.creating_roi = False
            if hasattr(self, 'temp_roi'):
                delattr(self, 'temp_roi')
    
    def start_process(self):
        if not self.camera_active:
            self.start_camera()
            QtCore.QTimer.singleShot(1000, self._start_continuous_detection)
        else:
            self._start_continuous_detection()
    
    def _start_continuous_detection(self):
        self.process_active = True
        self.label_6.setText("RUNNING")
        self.label_2.setText("PROCESSING")
        self.label_2.setStyleSheet("background-color: yellow; color: black; font-weight: bold; font-size: 16pt; qproperty-alignment: 'AlignCenter';")
        
        self.idle_start_time = datetime.datetime.now()
        
        self.pushButton_4.setEnabled(False)
        
        self.detection_timer = QtCore.QTimer()
        self.detection_timer.timeout.connect(self._process_current_frame)
        self.detection_timer.start(500)
        
        print("Mode deteksi berkelanjutan aktif")
    
    def _process_current_frame(self):
        if not self.process_active or not self.camera_active:
            return
        
        if self.camera is not None and self.camera.isOpened():
            ret, frame = self.camera.read()
            if ret:
                frame = cv2.resize(frame, (self.camera_geometry["width"], self.camera_geometry["height"]))
                
                y1 = max(0, self.roi["y"])
                y2 = min(self.camera_geometry["height"], self.roi["y"] + self.roi["h"])
                x1 = max(0, self.roi["x"])
                x2 = min(self.camera_geometry["width"], self.roi["x"] + self.roi["w"])
                
                if y2 > y1 and x2 > x1:
                    roi_img = frame[y1:y2, x1:x2]
                    
                    try:
                        match_result, best_match = self.match_template(roi_img)
                        self.process_result(match_result, best_match)
                    except Exception as e:
                        print(f"Error saat template matching: {e}")
                        import traceback
                        traceback.print_exc()
                        self.process_result(False, None)
                        
                        # Reset nilai kecocokan jika terjadi error
                        self.current_match_value = 0.0
                        self.update_match_value_display()
                else:
                    print("Error: ROI tidak valid")
                    self.process_result(False, None)
                    
                    # Reset nilai kecocokan jika ROI tidak valid
                    self.current_match_value = 0.0
                    self.update_match_value_display()
            else:
                print("Error: Tidak dapat membaca frame")
                self.process_result(False, None)
                
                # Reset nilai kecocokan jika tidak dapat membaca frame
                self.current_match_value = 0.0
                self.update_match_value_display()
        else:
            print("Error: Kamera tidak tersedia")
            self.process_result(False, None)
            
            # Reset nilai kecocokan jika kamera tidak tersedia
            self.current_match_value = 0.0
            self.update_match_value_display()
    
    def match_template(self, image):
        # Dapatkan template untuk model dan pattern saat ini
        model_templates = self.templates.get(self.current_model, {}).get(self.current_pattern, [])
        if not model_templates:
            print(f"Tidak ada template di Model {self.current_model}, Pattern {self.current_pattern}")
            return False, None
        
        best_match_val = -1
        best_match_template = None
        best_match_details = {}
        
        image_copy = image.copy()
        
        def extract_features(img):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            
            h, s, v = cv2.split(hsv)
            b, g, r = cv2.split(img)
            
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            gray_eq = clahe.apply(gray)
            
            edges_canny = cv2.Canny(gray_eq, 30, 150)
            sobelx = cv2.Sobel(gray_eq, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(gray_eq, cv2.CV_64F, 0, 1, ksize=3)
            sobel_combined = cv2.magnitude(sobelx, sobely)
            sobel_combined = cv2.convertScaleAbs(sobel_combined)
            
            kernels = []
            for theta in range(0, 180, 45):
                theta = theta / 180 * np.pi
                for sigma in [3, 5]:
                    for lambd in [5, 10]:
                        for gamma in [0.5, 1]:
                            kernel = cv2.getGaborKernel((21, 21), sigma, theta, lambd, gamma, 0, ktype=cv2.CV_32F)
                            kernels.append(kernel)
            
            gabor_responses = []
            for kernel in kernels[:4]:
                gabor_response = cv2.filter2D(gray_eq, cv2.CV_8UC3, kernel)
                gabor_responses.append(gabor_response)
            
            try:
                from skimage.feature import hog
                hog_features, hog_image = hog(
                    gray_eq, 
                    orientations=8, 
                    pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), 
                    visualize=True,
                    block_norm='L2-Hys'
                )
                hog_image = (hog_image * 255).astype(np.uint8)
            except:
                hog_image = np.zeros_like(gray_eq)
            
            _, thresh = cv2.threshold(gray_eq, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            
            return {
                'gray': gray,
                'gray_eq': gray_eq,
                'edges': edges_canny,
                'sobel': sobel_combined,
                'hsv': hsv,
                'h_channel': h,
                's_channel': s,
                'v_channel': v,
                'gabor': gabor_responses,
                'hog': hog_image,
                'thresh': thresh
            }
        
        def detect_defects(img_features, template_features):
            defects = {}
            
            # Tingkatkan sensitivitas deteksi tepi untuk mengenali perbedaan seperti keychain
            edge_diff = cv2.absdiff(img_features['edges'], template_features['edges'])
            _, edge_thresh = cv2.threshold(edge_diff, 20, 255, cv2.THRESH_BINARY)  # Turunkan threshold
            edge_defect_ratio = np.sum(edge_thresh) / (edge_thresh.size * 255)
            
            # Hitung perbedaan gabor
            gabor_diffs = []
            for i in range(len(img_features['gabor'])):
                if i < len(template_features['gabor']):
                    diff = cv2.absdiff(img_features['gabor'][i], template_features['gabor'][i])
                    gabor_diffs.append(np.mean(diff))
            
            # Hitung skor defect gabor
            gabor_defect_score = np.mean(gabor_diffs) / 255 if gabor_diffs else 0
            
            # Hitung perbedaan hsv
            hsv_diff = cv2.absdiff(img_features['hsv'], template_features['hsv'])
            hsv_defect_score = np.mean(hsv_diff) / 255
            
            # Hitung perbedaan grayscale
            gray_diff = cv2.absdiff(img_features['gray_eq'], template_features['gray_eq'])
            _, gray_thresh = cv2.threshold(gray_diff, 30, 255, cv2.THRESH_BINARY)
            gray_defect_ratio = np.sum(gray_thresh) / (gray_thresh.size * 255)
            
            # Hitung perbedaan HOG
            hog_diff = cv2.absdiff(img_features['hog'], template_features['hog'])
            hog_defect_score = np.mean(hog_diff) / 255
            
            # Tingkatkan sensitivitas pada area tepi/outline objek
            contours, _ = cv2.findContours(edge_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            significant_defects = [cnt for cnt in contours if cv2.contourArea(cnt) > 20]
            
            # Perhatikan perubahan bentuk outline yang bisa menunjukkan keberadaan aksesoris
            shape_difference = 0
            if len(contours) > 0:
                # Hitung perbedaan area kontur
                img_contour_area = sum([cv2.contourArea(cnt) for cnt in contours])
                
                # Bandingkan dengan template
                template_edge_diff = cv2.Canny(template_features['gray_eq'], 30, 150)
                template_contours, _ = cv2.findContours(template_edge_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                template_contour_area = sum([cv2.contourArea(cnt) for cnt in template_contours]) if len(template_contours) > 0 else 0
                
                # Hitung perbedaan relatif area kontur
                if template_contour_area > 0:
                    shape_difference = abs(img_contour_area - template_contour_area) / template_contour_area
            
            # Tambahkan deteksi komponen yang berbeda (seperti keychain)
            # Bagi gambar menjadi grid dan bandingkan setiap area
            grid_size = 5  # 5x5 grid
            h, w = img_features['gray'].shape
            cell_h, cell_w = h // grid_size, w // grid_size
            
            cell_differences = []
            for i in range(grid_size):
                for j in range(grid_size):
                    y1, y2 = i * cell_h, (i + 1) * cell_h
                    x1, x2 = j * cell_w, (j + 1) * cell_w
                    
                    if y2 <= h and x2 <= w:
                        img_cell = img_features['gray'][y1:y2, x1:x2]
                        template_cell = template_features['gray'][y1:y2, x1:x2]
                        
                        cell_diff = cv2.absdiff(img_cell, template_cell)
                        cell_diff_score = np.mean(cell_diff) / 255.0
                        cell_differences.append(cell_diff_score)
            
            # Cari sel dengan perbedaan tertinggi (mungkin mengandung keychain)
            max_cell_diff = max(cell_differences) if cell_differences else 0
            
            # Tingkatkan bobot untuk fitur yang dapat mendeteksi aksesoris seperti keychain
            weights = [0.25, 0.15, 0.15, 0.15, 0.1, 0.2]  # Tambahkan bobot untuk shape_difference
            defect_score = (
                edge_defect_ratio * weights[0] +
                gabor_defect_score * weights[1] +
                hsv_defect_score * weights[2] +
                gray_defect_ratio * weights[3] +
                hog_defect_score * weights[4] +
                shape_difference * weights[5]  # Tambahkan faktor bentuk
            )
            
            # Tambahkan pengecekan maksimum perbedaan sel untuk deteksi komponen tambahan
            is_accessory_detected = max_cell_diff > 0.3  # Threshold untuk deteksi aksesoris
            
            defect_map = gray_thresh.copy()
            
            return {
                'score': defect_score,
                'edge_ratio': edge_defect_ratio,
                'gabor_score': gabor_defect_score,
                'color_score': hsv_defect_score,
                'intensity_score': gray_defect_ratio,
                'hog_score': hog_defect_score,
                'shape_difference': shape_difference,
                'max_cell_difference': max_cell_diff,
                'defect_count': len(significant_defects),
                'defect_map': defect_map,
                'accessory_detected': is_accessory_detected,
                'is_defective': defect_score > 0.15 or len(significant_defects) > 3 or is_accessory_detected
            }
        
        def compute_similarity(img_features, template_features):
            similarities = {}
            
            # Tingkatkan sensitivitas pada area tepi
            try:
                from skimage.metrics import structural_similarity as ssim
                ssim_gray, _ = ssim(img_features['gray_eq'], template_features['gray_eq'], full=True)
                ssim_edges, _ = ssim(img_features['edges'], template_features['edges'], full=True)
                similarities['ssim_gray'] = ssim_gray
                similarities['ssim_edges'] = ssim_edges
            except ImportError:
                similarities['ssim_gray'] = 0.5
                similarities['ssim_edges'] = 0.5
            
            # Tambahkan perbandingan histogram yang lebih detail
            hist_gray1 = cv2.calcHist([img_features['gray']], [0], None, [256], [0, 256])
            hist_gray2 = cv2.calcHist([template_features['gray']], [0], None, [256], [0, 256])
            hist_h1 = cv2.calcHist([img_features['h_channel']], [0], None, [180], [0, 180])
            hist_h2 = cv2.calcHist([template_features['h_channel']], [0], None, [180], [0, 180])
            
            # Bagi gambar menjadi region dan bandingkan histogramnya secara terpisah
            h, w = img_features['gray'].shape
            regions = [(0, 0, w//2, h//2), (w//2, 0, w, h//2), (0, h//2, w//2, h), (w//2, h//2, w, h)]
            
            region_similarities = []
            for x1, y1, x2, y2 in regions:
                img_region = img_features['gray'][y1:y2, x1:x2]
                template_region = template_features['gray'][y1:y2, x1:x2]
                
                hist_img_region = cv2.calcHist([img_region], [0], None, [64], [0, 256])
                hist_template_region = cv2.calcHist([template_region], [0], None, [64], [0, 256])
                
                region_similarity = cv2.compareHist(hist_img_region, hist_template_region, cv2.HISTCMP_CORREL)
                region_similarities.append(region_similarity)
            
            # Gunakan nilai terendah dari kesamaan region untuk mendeteksi perbedaan lokal
            similarities['min_region_similarity'] = min(region_similarities)
            
            # Perhitungan kesamaan lainnya tetap sama
            similarities['hist_gray'] = cv2.compareHist(hist_gray1, hist_gray2, cv2.HISTCMP_CORREL)
            similarities['hist_hue'] = cv2.compareHist(hist_h1, hist_h2, cv2.HISTCMP_CORREL)
            
            # Sesuaikan bobot untuk memberikan penekanan lebih pada perbedaan lokal
            weights = {
                'ssim_gray': 0.1,
                'ssim_edges': 0.15,
                'hist_gray': 0.1,
                'hist_hue': 0.1,
                'template_5': 0.1,
                'template_4': 0.05,
                'orb': 0.15,
                'hog': 0.1,
                'min_region_similarity': 0.25  # Bobot tinggi untuk perbedaan region lokal
            }
            
            # Hitung skor gabungan dengan pembobotan baru
            combined_score = sum(similarities.get(k, 0) * v for k, v in weights.items() if k in similarities)
            
            # Penalti untuk perbedaan region yang signifikan (seperti keychain yang hilang)
            if similarities['min_region_similarity'] < 0.7:
                combined_score *= 0.85  # Kurangi skor jika ada perbedaan region signifikan
            
            similarities['combined'] = combined_score
            
            return combined_score, similarities
        
        # Ekstrak fitur ROI image sekali saja untuk performa
        print(f"Mengekstrak fitur dari ROI image...")
        img_features = extract_features(image_copy)
        
        # Log informasi tentang jumlah template yang akan diperiksa
        print(f"Akan memeriksa {len(model_templates)} template dari Model {self.current_model}, Pattern {self.current_pattern}")
        
        # Hanya periksa template dari model yang dipilih
        for i, template_data in enumerate(model_templates):
            template = template_data["image"].copy()
            
            if template.shape[0] != image.shape[0] or template.shape[1] != image.shape[1]:
                template = cv2.resize(template, (image.shape[1], image.shape[0]))
            
            print(f"Mencocokkan dengan template {i+1}/{len(model_templates)}: {template_data['name']}")
            template_features = extract_features(template)
            
            print(f"Mendeteksi cacat pada template {i}...")
            defect_info = detect_defects(img_features, template_features)
            
            print(f"Template {i} - Analisis Cacat:")
            print(f"  - Skor cacat keseluruhan: {defect_info['score']*100:.2f}%")
            print(f"  - Jumlah cacat terdeteksi: {defect_info['defect_count']}")
            print(f"  - Status: {'CACAT' if defect_info['is_defective'] else 'BAIK'}")
            
            print(f"Menghitung kesamaan dengan template {i}...")
            similarity, detailed_scores = compute_similarity(img_features, template_features)
            
            print(f"Template {i} - Analisis Kesamaan:")
            for method, score in detailed_scores.items():
                print(f"  - Metrik {method}: {score*100:.2f}%")
            
            print(f"Template {i} - Nilai kecocokan gabungan: {similarity*100:.2f}%")
            
            if similarity > best_match_val:
                best_match_val = similarity
                best_match_template = template_data
                best_match_details = {
                    'similarity': detailed_scores,
                    'defects': defect_info,
                    'features': {
                        'img': img_features,
                        'template': template_features
                    }
                }
        
        # Di bagian akhir fungsi, setelah mendapatkan best_match_val:
        self.current_match_value = best_match_val
        
        # Update label nilai kecocokan
        self.update_match_value_display()
        
        print("\nHasil Analisis Akhir:")
        print(f"Nilai kecocokan terbaik: {best_match_val*100:.2f}% (Threshold: {self.template_matching_threshold*100:.2f}%)")
        
        is_match = False
        reason = ""
        
        if best_match_template is not None and best_match_details:
            defect_info = best_match_details['defects']
            similarity_info = best_match_details['similarity']
            
            if best_match_val >= self.template_matching_threshold:
                is_match = True
                reason = f"Kecocokan di atas threshold ({best_match_val*100:.2f}%)"
            else:
                is_match = False
                reason = f"Kecocokan di bawah threshold ({best_match_val*100:.2f}%)"
        else:
            is_match = False
            reason = "Tidak ada template yang cocok"
        
        status = "OK" if is_match else "NG"
        print(f"Status Part: {status}")
        print(f"Alasan: {reason}")
        
        if hasattr(self, 'last_inspection_details'):
            self.last_inspection_details = {
                'status': status,
                'reason': reason,
                'match_value': best_match_val,
                'defect_info': defect_info if best_match_template else None
            }
        else:
            setattr(self, 'last_inspection_details', {
                'status': status,
                'reason': reason,
                'match_value': best_match_val,
                'defect_info': defect_info if best_match_template else None
            })
        
        return is_match, best_match_template
    
    def process_result(self, match_result, best_match=None):
        if not self.process_active:
            return
        
        result = "PASS" if match_result else "FAIL"
        
        inspection_details = getattr(self, 'last_inspection_details', {})
        status = inspection_details.get('status', "OK" if match_result else "NG")
        match_value = inspection_details.get('match_value', 0)
        
        # Simpan hasil inspeksi terakhir untuk ditampilkan di frame
        self.last_inspection_result = {
            'status': status,
            'match_value': match_value,
            'timestamp': datetime.datetime.now().isoformat()
        }
        
        self.label_7.setText(result)
        
        if result == "PASS":
            self.label_2.setText("PASS")
            self.label_2.setStyleSheet("background-color: green; color: white; font-weight: bold; font-size: 16pt; qproperty-alignment: 'AlignCenter';")
            
            print(f"Hasil inspeksi: PASS - Part OK")
            print(f"Nilai kecocokan: {match_value*100:.2f}%")
            
        else:
            self.label_2.setText("FAIL")
            self.label_2.setStyleSheet("background-color: red; color: white; font-weight: bold; font-size: 16pt; qproperty-alignment: 'AlignCenter';")
            
            print(f"Hasil inspeksi: FAIL - Part NG")
            print(f"Nilai kecocokan: {match_value*100:.2f}%")
        
        # Catat hasil inspeksi ke log file
        with open("inspection_log.txt", "a") as log_file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"[{timestamp}] Status: {status}, Nilai: {match_value*100:.2f}%\n")
    
    def stop_process(self):
        self.process_active = False
        
        if hasattr(self, 'detection_timer') and self.detection_timer.isActive():
            self.detection_timer.stop()
        
        self.label_6.setText("IDLE")
        self.label_2.setText("STOPPED")
        self.label_2.setStyleSheet("background-color: gray; color: white; font-weight: bold; font-size: 16pt; qproperty-alignment: 'AlignCenter';")
        
        self.pushButton_4.setEnabled(True)
        
        self.idle_start_time = datetime.datetime.now()
        
        # Reset nilai kecocokan saat proses dihentikan
        self.current_match_value = 0.0
        self.update_match_value_display()
        
        print("Mode deteksi berkelanjutan dinonaktifkan")
    
    def update_time(self):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.labelTime.setText(current_time)
        
        if hasattr(self, 'idle_start_time'):
            idle_seconds = int((datetime.datetime.now() - self.idle_start_time).total_seconds())
            self.label_9.setText(str(idle_seconds))
    
    def get_roi_from_settings(self):
        try:
            x = int(self.settings_ui.label_6.text())
            y = int(self.settings_ui.label_12.text())
            w = int(self.settings_ui.label_8.text())
            h = int(self.settings_ui.label_11.text())
            self.roi = {"x": x, "y": y, "w": w, "h": h}
            print(f"ROI berhasil diperbarui dari settings: x={x}, y={y}, w={w}, h={h}")
            
            # Simpan ROI untuk model dan pattern saat ini
            model_key = str(self.current_model)
            pattern_key = str(self.current_pattern)
            
            if model_key not in self.roi_per_pattern:
                self.roi_per_pattern[model_key] = {}
            
            self.roi_per_pattern[model_key][pattern_key] = {"x": x, "y": y, "w": w, "h": h}
            self.save_roi_settings()
            
            # Perbarui nama model jika diubah di settings
            try:
                if hasattr(self.settings_ui, 'model_names'):
                    self.model_names = self.settings_ui.model_names.copy()
                    self.update_model_label()
            except Exception as e:
                print(f"Error saat mengambil nama model dari settings: {e}")
            
            # Perbarui nama pattern jika diubah di settings
            try:
                if hasattr(self.settings_ui, 'pattern_names'):
                    self.pattern_names = self.settings_ui.pattern_names.copy()
                    self.update_pattern_label()
            except Exception as e:
                print(f"Error saat mengambil nama pattern dari settings: {e}")
        except (ValueError, AttributeError) as e:
            print(f"Error saat mengambil ROI dari settings: {e}")

    def closeEvent(self, event):
        # Pastikan kamera ditutup saat aplikasi ditutup
        if self.camera is not None:
            self.camera.release()
        event.accept()

    def add_center_box(self):
        if not self.camera_active:
            return
            
        center_x = self.frame.width() // 2 - 50
        center_y = self.frame.height() // 2 - 50
        box_w = 300
        box_h = 300
        
        center_box = {
            "x": center_x,
            "y": center_y,
            "w": box_w,
            "h": box_h,
            "label": "center_object",
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        self.bounding_boxes.append(center_box)
        self.save_bounding_boxes()

    def adjust_roi_center(self):
        self.center_roi()

    def open_step2(self):
        if self.camera_active:
            self.stop_camera()
        
        self.step2_window = QtWidgets.QMainWindow()
        self.step2_ui = Step2_UI()
        self.step2_ui.setupUi(self.step2_window)
        
        self.setup_step2_functions()
        
        self.step2_window.show()

    def setup_step2_functions(self):
        if hasattr(self.step2_ui, 'toolButton_3'):
            self.step2_ui.toolButton_3.clicked.connect(self.step2_toggle_camera)
        
        if hasattr(self.step2_ui, 'toolButton'):
            self.step2_ui.toolButton.clicked.connect(self.step2_start_process)
        
        if hasattr(self.step2_ui, 'toolButton_2'):
            self.step2_ui.toolButton_2.clicked.connect(self.step2_stop_process)
        
        if hasattr(self.step2_ui, 'pushButton_4'):
            self.step2_ui.pushButton_4.clicked.connect(self.open_settings)
        
        self.step2_timer = QtCore.QTimer()
        self.step2_timer.timeout.connect(self.step2_update_time)
        self.step2_timer.start(1000)
        
        self.step2_ui.label_6.setText("IDLE")
        self.step2_ui.label_7.setText("WAITING")
        self.step2_ui.label_9.setText("0")
        self.step2_ui.label_11.setText("STEP 2")

    def step2_toggle_camera(self):
        pass

    def step2_start_process(self):
        pass

    def step2_stop_process(self):
        pass

    def step2_update_time(self):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if hasattr(self.step2_ui, 'labelTime'):
            self.step2_ui.labelTime.setText(current_time)

    def load_templates(self):
        """Muat template dari direktori models dengan struktur baru"""
        if not os.path.exists(self.models_dir):
            os.makedirs(self.models_dir)
            for model in range(1, 6):
                model_dir = os.path.join(self.models_dir, f"model{model}")
                os.makedirs(model_dir, exist_ok=True)
                for pattern in range(1, 6):
                    pattern_dir = os.path.join(model_dir, f"pattern{pattern}")
                    os.makedirs(pattern_dir, exist_ok=True)
            
            QMessageBox.information(self.MainWindow, "Info", 
                                   f"Struktur folder models telah dibuat di {os.path.abspath(self.models_dir)}.\n"
                                   "Silakan tambahkan gambar template di folder models/model[1-5]/pattern[1-5]/")
        
        self.templates = {}
        for model in range(1, 6):
            model_dir = os.path.join(self.models_dir, f"model{model}")
            os.makedirs(model_dir, exist_ok=True)
            
            self.templates[model] = {}
            
            for pattern in range(1, 6):
                pattern_dir = os.path.join(model_dir, f"pattern{pattern}")
                os.makedirs(pattern_dir, exist_ok=True)
                
                image_files = glob.glob(os.path.join(pattern_dir, "*.jpg")) + \
                             glob.glob(os.path.join(pattern_dir, "*.png")) + \
                             glob.glob(os.path.join(pattern_dir, "*.jpeg"))
                
                pattern_templates = []
                for img_path in image_files:
                    try:
                        # Muat template dengan ukuran asli
                        template = cv2.imread(img_path)
                        if template is not None:
                            if len(template.shape) == 2:
                                template = cv2.cvtColor(template, cv2.COLOR_GRAY2BGR)
                            elif template.shape[2] == 4:
                                template = cv2.cvtColor(template, cv2.COLOR_RGBA2BGR)
                            
                            # Simpan template dengan ukuran asli
                            pattern_templates.append({
                                "path": img_path,
                                "image": template,
                                "name": os.path.basename(img_path),
                                "original_size": template.shape[:2]
                            })
                            print(f"Template berhasil dimuat: {img_path} (ukuran: {template.shape})")
                    except Exception as e:
                        print(f"Error saat memuat template {img_path}: {e}")
                
                self.templates[model][pattern] = pattern_templates
        
        # Update labels
        try:
            if hasattr(self, 'model_names'):
                self.update_model_label()
            if hasattr(self, 'pattern_names') and hasattr(self, 'current_pattern'):
                self.update_pattern_label()
            else:
                print("Peringatan: model_names atau pattern_names belum diinisialisasi")
                self.label_11.setText(f"MODEL {self.current_model}")
                if hasattr(self, 'current_pattern'):
                    self.label_12.setText(f"PATTERN {self.current_pattern}")
        except Exception as e:
            print(f"Error saat memperbarui label: {e}")
            self.label_11.setText(f"MODEL {self.current_model}")
            if hasattr(self, 'current_pattern'):
                self.label_12.setText(f"PATTERN 1")
    
    def select_model(self, model_number):
        if 1 <= model_number <= 5:
            self.current_model = model_number
            self.update_model_label()
            
            # Reset template cache saat model berubah
            if hasattr(self, 'template_cache'):
                self.template_cache = {}
            
            # Jika dalam mode deteksi, segera inisialisasi cache baru
            if self.process_active:
                self._init_template_cache()
            
            if len(self.templates.get(model_number, [])) == 0:
                QMessageBox.warning(self.MainWindow, "Peringatan", 
                                   f"Tidak ada template di Model {model_number}.\n"
                                   f"Silakan tambahkan gambar template di folder models/model{model_number}/pattern[1-5]/")
    def refresh_cameras(self):
        print("Mencari kamera yang tersedia...")
        self.available_cameras = []
        
        for i in range(4):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                ret, frame = cap.read()
                if ret:
                    self.available_cameras.append(i)
                    print(f"Kamera {i} tersedia")
                else:
                    print(f"Kamera {i} tidak dapat membaca frame")
                cap.release()
            else:
                print(f"Kamera {i} tidak dapat dibuka")
        
        camera_actions = [
            self.actionCamera_0,
            self.actionCamera_1, 
            self.actionCamera_2,
            self.actionCamera_3
        ]
        
        for i, action in enumerate(camera_actions):
            if i in self.available_cameras:
                action.setEnabled(True)
                if i == self.camera_index:
                    action.setChecked(True)
                    action.setText(f"Camera {i} (Active)")
                else:
                    action.setChecked(False)
                    action.setText(f"Camera {i}")  
            else:
                action.setEnabled(False)
                action.setChecked(False)
                action.setText(f"Camera {i} (Not Available)")
        
        if not self.available_cameras:
            QMessageBox.warning(self.MainWindow, "Peringatan", 
                            "Tidak ada kamera yang tersedia!")
        else:
            print(f"Total kamera tersedia: {len(self.available_cameras)}")
            if self.camera_index not in self.available_cameras:
                # Jika kamera saat ini tidak tersedia, pilih kamera pertama yang tersedia
                self.camera_index = self.available_cameras[0]
                print(f"Beralih ke kamera {self.camera_index}")

    def select_camera(self, camera_index):
        if camera_index not in self.available_cameras:
            QMessageBox.warning(self.MainWindow,"Warning",f"Kamera {camera_index} tidak tersedia")
            return
        was_active = self.camera_active
        if was_active:
            self.stop_camera()
        if self.camera is not None:
            self.camera.release()
            self.camera = None
        old_index = self.camera_index
        self.camera_index = camera_index

        print(f"Beralih dari kamera {old_index} ke kamera {camera_index}")
        self.refresh_cameras()

        if was_active:
            QtCore.QTimer.singleShot(580, self.start_camera)
        QMessageBox.information(self.MainWindow, "info",f"Kamera berhasil beralih ke camera {camera_index}")

    
    def update_model_label(self):
        """Update label model dan nama model di header"""
        self.label_11.setText(f"MODEL {self.current_model}")
        
        # Update nama model di header (label_3)
        if hasattr(self, 'model_names'):
            model_name = self.model_names.get(str(self.current_model), f"Model {self.current_model}")
        else:
            model_name = f"Model {self.current_model}"
        
        self.label_3.setText(model_name)
        
        template_count = len(self.templates.get(self.current_model, []))
        print(f"Model {self.current_model} ({model_name}) dipilih dengan {template_count} template")
    
    def save_settings(self):
        """Simpan pengaturan dan tampilkan popup konfirmasi"""
        print("Fungsi save_settings() dipanggil")
        
        try:
            # Simpan nama model
            model_name = self.settings_ui.textEdit.toPlainText().strip()
            if model_name:
                self.model_names[str(self.current_model)] = model_name
                self.save_model_names()
                print(f"Nama model {self.current_model} diubah menjadi: {model_name}")
            
            # Simpan nama pattern
            pattern_name = self.settings_ui.textEdit_3.toPlainText().strip()
            if pattern_name:
                model_key = str(self.current_model)
                pattern_key = str(self.current_pattern)
                
                if model_key not in self.pattern_names:
                    self.pattern_names[model_key] = {}
                
                self.pattern_names[model_key][pattern_key] = pattern_name
                self.save_pattern_names()
                print(f"Nama pattern {self.current_pattern} diubah menjadi: {pattern_name}")
            
            # Simpan ROI untuk model dan pattern saat ini
            try:
                x = int(self.settings_ui.label_6.text())
                y = int(self.settings_ui.label_12.text())
                w = int(self.settings_ui.label_8.text())
                h = int(self.settings_ui.label_11.text())
                
                if w > 0 and h > 0:
                    model_key = str(self.current_model)
                    pattern_key = str(self.current_pattern)
                    
                    if model_key not in self.roi_per_pattern:
                        self.roi_per_pattern[model_key] = {}
                    
                    self.roi_per_pattern[model_key][pattern_key] = {"x": x, "y": y, "w": w, "h": h}
                    self.save_roi_settings()
                    
                    # Update ROI saat ini jika model dan pattern yang diubah adalah yang aktif
                    if self.current_model == int(model_key) and self.current_pattern == int(pattern_key):
                        self.roi = {"x": x, "y": y, "w": w, "h": h}
                    
                    print(f"ROI untuk Model {model_key}, Pattern {pattern_key} berhasil diubah: x={x}, y={y}, w={w}, h={h}")
            except ValueError:
                print("Error: Nilai ROI harus berupa angka")
            
            # Simpan threshold
            try:
                threshold_text = self.settings_ui.textEdit_2.toPlainText()
                if threshold_text:
                    if threshold_text.endswith('%'):
                        threshold = float(threshold_text.rstrip('%')) / 100.0
                    else:
                        threshold = float(threshold_text)
                    
                    if 0 <= threshold <= 1:
                        self.template_matching_threshold = threshold
                        # Update marker threshold setelah nilai threshold diubah
                        self.update_threshold_marker()
                        print(f"Threshold template matching berhasil diubah menjadi: {threshold*100:.2f}%")
            except ValueError:
                print("Error: Format threshold tidak valid")
            
            # Tampilkan popup konfirmasi
            QMessageBox.information(
                self.MainWindow,
                "Sukses",
                "Pengaturan berhasil disimpan",
                QMessageBox.Ok
            )
            
            # Update label setelah pengaturan disimpan
            self.update_model_label()
            self.update_pattern_label()
            
        except Exception as e:
            print(f"Error dalam save_settings: {e}")
            import traceback
            traceback.print_exc()
            QMessageBox.critical(
                self.MainWindow,
                "Error",
                f"Terjadi kesalahan saat menyimpan pengaturan: {str(e)}",
                QMessageBox.Ok
            )
    
    def settings_pattern_changed(self):
        """Handler saat pattern berubah di settings"""
        try:
            new_pattern = int(self.settings_ui.comboBox_2.currentText())
            old_pattern = self.current_pattern
            
            if new_pattern != old_pattern:
                # Update pattern saat ini
                self.current_pattern = new_pattern
                
                # Update nama pattern di textEdit
                model_key = str(self.current_model)
                pattern_key = str(self.current_pattern)
                if model_key in self.pattern_names and pattern_key in self.pattern_names[model_key]:
                    pattern_name = self.pattern_names[model_key][pattern_key]
                else:
                    pattern_name = f"Pattern {self.current_pattern}"
                
                self.settings_ui.textEdit_3.setText(pattern_name)
                
                # Update ROI sesuai dengan pattern yang dipilih
                if model_key in self.roi_per_pattern and pattern_key in self.roi_per_pattern[model_key]:
                    roi_settings = self.roi_per_pattern[model_key][pattern_key]
                    
                    # Update input fields
                    self.settings_ui.label_6.setText(str(roi_settings["x"]))
                    self.settings_ui.label_12.setText(str(roi_settings["y"]))
                    self.settings_ui.label_8.setText(str(roi_settings["w"]))
                    self.settings_ui.label_11.setText(str(roi_settings["h"]))
                
                print(f"Pattern di settings berubah ke: {new_pattern}")
        except Exception as e:
            print(f"Error saat mengubah pattern di settings: {e}")
    
    def load_pattern_names(self):
        """Muat nama pattern dari file jika ada, atau gunakan default"""
        try:
            if os.path.exists("pattern_names.json"):
                import json
                with open("pattern_names.json", "r") as f:
                    self.pattern_names = json.load(f)
                    print("Nama pattern berhasil dimuat dari file")
            else:
                # Default nama pattern
                self.pattern_names = {
                    "1": {
                        "1": "Whole Device",
                        "2": "Screen",
                        "3": "Keyboard",
                        "4": "Touchpad",
                        "5": "Ports"
                    },
                    "2": {
                        "1": "Pattern 1",
                        "2": "Pattern 2",
                        "3": "Pattern 3",
                        "4": "Pattern 4",
                        "5": "Pattern 5"
                    },
                    "3": {
                        "1": "Pattern 1",
                        "2": "Pattern 2",
                        "3": "Pattern 3",
                        "4": "Pattern 4",
                        "5": "Pattern 5"
                    },
                    "4": {
                        "1": "Pattern 1",
                        "2": "Pattern 2",
                        "3": "Pattern 3",
                        "4": "Pattern 4",
                        "5": "Pattern 5"
                    },
                    "5": {
                        "1": "Pattern 1",
                        "2": "Pattern 2",
                        "3": "Pattern 3",
                        "4": "Pattern 4",
                        "5": "Pattern 5"
                    }
                }
                self.save_pattern_names()
                print("Menggunakan nama pattern default")
        except Exception as e:
            print(f"Error saat memuat nama pattern: {e}")
    
    def save_pattern_names(self):
        """Simpan nama pattern ke file"""
        try:
            import json
            with open("pattern_names.json", "w") as f:
                json.dump(self.pattern_names, f)
            print("Nama pattern berhasil disimpan ke file")
        except Exception as e:
            print(f"Error saat menyimpan nama pattern: {e}")
    
    def load_roi_settings(self):
        """Muat pengaturan ROI untuk setiap model dan pattern"""
        try:
            if os.path.exists("roi_settings.json"):
                import json
                with open("roi_settings.json", "r") as f:
                    self.roi_per_pattern = json.load(f)
                    print("Pengaturan ROI berhasil dimuat dari file")
            else:
                # Inisialisasi struktur default
                for model in range(1, 6):
                    for pattern in range(1, 6):
                        self.set_default_roi(model, pattern)
                
                self.save_roi_settings()
                print("Menggunakan pengaturan ROI default")
        except Exception as e:
            print(f"Error saat memuat pengaturan ROI: {e}")
            # Inisialisasi dengan nilai default jika terjadi error
            for model in range(1, 6):
                for pattern in range(1, 6):
                    self.set_default_roi(model, pattern)
    
    def set_default_roi(self, model, pattern):
        """Set ROI default untuk model dan pattern tertentu dengan ukuran fleksibel"""
        # Ukuran yang proporsional dengan ukuran frame
        frame_width = self.camera_geometry["width"]
        frame_height = self.camera_geometry["height"]
        
        # Ukuran ROI sekitar 60% dari ukuran frame
        roi_width = int(frame_width * 0.6)
        roi_height = int(frame_height * 0.6)
        
        # Tempatkan ROI di tengah
        roi_x = (frame_width - roi_width) // 2
        roi_y = (frame_height - roi_height) // 2
        
        # Buat key untuk model dan pattern
        model_key = str(model)
        pattern_key = str(pattern)
        
        # Pastikan kamus untuk model sudah ada
        if model_key not in self.roi_per_pattern:
            self.roi_per_pattern[model_key] = {}
        
        # Set nilai ROI
        self.roi_per_pattern[model_key][pattern_key] = {
            "x": roi_x,
            "y": roi_y,
            "w": roi_width,
            "h": roi_height
        }
    
    def save_roi_settings(self):
        """Simpan pengaturan ROI ke file"""
        try:
            import json
            with open("roi_settings.json", "w") as f:
                json.dump(self.roi_per_pattern, f)
            print("Pengaturan ROI berhasil disimpan ke file")
        except Exception as e:
            print(f"Error saat menyimpan pengaturan ROI: {e}")
    
    def select_pattern(self, pattern_number):
        """Handler untuk pemilihan pattern"""
        if 1 <= pattern_number <= 5:
            self.current_pattern = pattern_number
            self.update_pattern_label()
            
            # Atur ROI sesuai dengan model dan pattern saat ini
            model_key = str(self.current_model)
            pattern_key = str(self.current_pattern)
            
            try:
                if model_key in self.roi_per_pattern and pattern_key in self.roi_per_pattern[model_key]:
                    roi_settings = self.roi_per_pattern[model_key][pattern_key]
                    self.roi = roi_settings.copy()
                    print(f"ROI untuk Model {self.current_model}, Pattern {self.current_pattern} berhasil dimuat")
                else:
                    # Jika pengaturan ROI belum ada, set nilai default
                    self.set_default_roi(self.current_model, self.current_pattern)
                    self.roi = self.roi_per_pattern[model_key][pattern_key].copy()
                    print(f"Menggunakan ROI default untuk Model {self.current_model}, Pattern {self.current_pattern}")
            except Exception as e:
                print(f"Error saat mengatur ROI untuk pattern: {e}")
    
    def update_pattern_label(self):
        """Update label pattern"""
        model_key = str(self.current_model)
        pattern_key = str(self.current_pattern)
        
        # Dapatkan nama pattern jika ada, atau gunakan default
        if model_key in self.pattern_names and pattern_key in self.pattern_names[model_key]:
            pattern_name = self.pattern_names[model_key][pattern_key]
        else:
            pattern_name = f"Pattern {self.current_pattern}"
        
        self.label_12.setText(f"PATTERN {self.current_pattern}: {pattern_name}")
        print(f"Pattern aktif: {self.current_pattern} ({pattern_name})")
    
    def load_model_names(self):
        """Muat nama model dari file jika ada, atau gunakan default"""
        try:
            if os.path.exists("model_names.json"):
                import json
                with open("model_names.json", "r") as f:
                    self.model_names = json.load(f)
                    print("Nama model berhasil dimuat dari file")
            else:
                # Default nama model
                self.model_names = {
                    "1": "K0WL EXPORT",
                    "2": "Model 2",
                    "3": "Model 3",
                    "4": "Model 4",
                    "5": "Model 5"
                }
                print("Menggunakan nama model default")
        except Exception as e:
            print(f"Error saat memuat nama model: {e}")
            # Default nama model jika terjadi error
            self.model_names = {
                "1": "K0WL EXPORT",
                "2": "Model 2",
                "3": "Model 3",
                "4": "Model 4",
                "5": "Model 5"
            }

    def save_model_names(self):
        """Simpan nama model ke file"""
        try:
            import json
            with open("model_names.json", "w") as f:
                json.dump(self.model_names, f)
            print("Nama model berhasil disimpan ke file")
        except Exception as e:
            print(f"Error saat menyimpan nama model: {e}")

    def toggle_filter_mode(self):
        """Ubah mode filter kamera"""
        filter_modes = ['normal', 'edges', 'enhanced', 'threshold', 'hsv']
        
        if not hasattr(self, 'filter_mode'):
            self.filter_mode = 'normal'
        
        # Dapatkan indeks mode saat ini dan hitung mode berikutnya
        current_index = filter_modes.index(self.filter_mode)
        next_index = (current_index + 1) % len(filter_modes)
        self.filter_mode = filter_modes[next_index]
        
        # Update label atau tombol untuk menunjukkan mode saat ini
        print(f"Mode filter diubah ke: {self.filter_mode}")
        
        # Tambahkan informasi filter mode pada label_5
        if self.filter_mode == 'normal':
            self.label_5.setText("STEP PROCESS (Normal)")
        elif self.filter_mode == 'edges':
            self.label_5.setText("STEP PROCESS (Edge Detection)")
        elif self.filter_mode == 'enhanced':
            self.label_5.setText("STEP PROCESS (Enhanced Detail)")
        elif self.filter_mode == 'threshold':
            self.label_5.setText("STEP PROCESS (Threshold)")
        elif self.filter_mode == 'hsv':
            self.label_5.setText("STEP PROCESS (Color Highlight)")

    def update_match_value_display(self):
        """Update tampilan nilai kecocokan pada progress bar"""
        if hasattr(self, 'current_match_value'):
            match_percentage = self.current_match_value * 100
            
            # Update nilai progress bar
            self.match_progress_bar.setValue(int(match_percentage))
            
            # Update label persentase
            self.label_match_percentage.setText(f"{match_percentage:.2f}%")
            
            # Ubah warna berdasarkan nilai kecocokan
            if match_percentage >= self.template_matching_threshold * 100:
                self.label_match_percentage.setStyleSheet("font-size: 14pt; font-weight: bold; color: green; qproperty-alignment: 'AlignCenter';")
                # Tambahkan indikator PASS
                self.label_match_percentage.setText(f"{match_percentage:.2f}% (PASS)")
            else:
                self.label_match_percentage.setStyleSheet("font-size: 14pt; font-weight: bold; color: red; qproperty-alignment: 'AlignCenter';")
                # Tambahkan indikator FAIL
                self.label_match_percentage.setText(f"{match_percentage:.2f}% (FAIL)")
        else:
            # Jika belum ada nilai kecocokan
            self.match_progress_bar.setValue(0)
            self.label_match_percentage.setText("0.00%")
            self.label_match_percentage.setStyleSheet("font-size: 14pt; font-weight: bold; color: black; qproperty-alignment: 'AlignCenter';")

    def update_threshold_marker(self):
        """Update tampilan marker threshold pada progress bar"""
        threshold_percentage = self.template_matching_threshold * 100
        
        # Update label threshold
        # self.label_threshold_marker.setText(f"Threshold: {threshold_percentage:.0f}%")
        
        # Update posisi dan ukuran kotak threshold
        progress_width = self.match_progress_bar.width()
        threshold_position = int(progress_width * threshold_percentage / 100)
        
        # Posisikan kotak threshold di progress bar
        self.threshold_box.setGeometry(QtCore.QRect(threshold_position - 5, 0, 10, self.match_progress_bar.height()))
        
        # Ubah warna kotak threshold berdasarkan nilai
        if threshold_percentage >= 70:
            color = "darkgreen"
        elif threshold_percentage >= 50:
            color = "darkblue"
        else:
            color = "darkred"
        
        self.threshold_box.setStyleSheet(f"background-color: transparent; border: 3px solid {color};")
        
        # Tambahkan label threshold di atas kotak
        # threshold_text = f"{threshold_percentage:.0f}%"
        # self.label_threshold_marker.setText(f"Threshold: {threshold_text}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
