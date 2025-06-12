from PyQt5 import QtCore, QtGui, QtWidgets
from settings import Ui_MainWindow as Settings_UI
from step2 import Ui_MainWindow as Step2_UI
import datetime
import cv2
import numpy as np
import json
import os
import glob
from PyQt5.QtWidgets import QMessageBox


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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1470, 36))
        self.menubar.setObjectName("menubar")
        self.menuChange_Password = QtWidgets.QMenu(self.menubar)
        self.menuChange_Password.setObjectName("menuChange_Password")
        self.menuModels = QtWidgets.QMenu(self.menubar)
        self.menuModels.setObjectName("menuModels")
        self.menuUser = QtWidgets.QMenu(self.menubar)
        self.menuUser.setObjectName("menuUser")
        self.menuCamera = QtWidgets.QMenu(self.menubar)
        self.menuCamera.setObjectName("menuCamera")
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
        self.menuModels.addAction(self.actionModel_1)
        self.menuModels.addAction(self.actionModel_2)
        self.menuModels.addAction(self.actionModel_3)
        self.menuModels.addAction(self.actionModel_4)
        self.menuModels.addAction(self.actionModel_5)
        self.menubar.addAction(self.menuChange_Password.menuAction())
        self.menubar.addAction(self.menuModels.menuAction())
        self.menubar.addAction(self.menuUser.menuAction())
        self.menubar.addAction(self.menuCamera.menuAction())

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
        
        roi_width = 100
        roi_height = 100
        
        roi_x = self.camera_geometry["x"] + (self.camera_geometry["width"] - roi_width) // 2
        roi_y = self.camera_geometry["y"] + (self.camera_geometry["height"] - roi_height) // 2
        
        self.roi = {"x": roi_x, "y": roi_y, "w": roi_width, "h": roi_height}
        self.bounding_boxes = []
        self.current_box = None
        self.drawing_box = False
        self.selected_box_index = -1
        self.dragging_box = False
        
        
        self.roi_timer = QtCore.QTimer()
        self.roi_timer.setSingleShot(True)
        self.roi_timer.timeout.connect(self.center_roi)
        
        self.frame.setMouseTracking(True)
        self.frame.mousePressEvent = self.mouse_press_event
        self.frame.mouseReleaseEvent = self.mouse_release_event
        self.frame.mouseMoveEvent = self.mouse_move_event
        
        self.label_6.setText("IDLE")
        self.label_7.setText("WAITING")
        self.label_9.setText("0")
        
        self.load_bounding_boxes()

        self.models_dir = "models"
        self.current_model = 1
        self.templates = {}
        self.template_matching_threshold = 0.8
        
        self.actionModel_1.triggered.connect(lambda: self.select_model(1))
        self.actionModel_2.triggered.connect(lambda: self.select_model(2))
        self.actionModel_3.triggered.connect(lambda: self.select_model(3))
        self.actionModel_4.triggered.connect(lambda: self.select_model(4))
        self.actionModel_5.triggered.connect(lambda: self.select_model(5))
        
        self.load_templates()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        
        self.settings_window.show()
    
    def toggle_camera(self):
        if self.camera_active:
            self.stop_camera()
        else:
            self.start_camera()
    
    def start_camera(self):
        if self.camera is None:
            self.camera = cv2.VideoCapture(0)
            if not self.camera.isOpened():
                print("Error: Tidak dapat membuka kamera")
                return
        
        self.camera_active = True
        self.camera_timer.start(30)
        self.toolButton_3.setText("STOP CAMERA")
        
        QtCore.QTimer.singleShot(500, self.center_roi)
    
    def center_roi(self):
        roi_width = 100
        roi_height = 100
        
        roi_x = (self.camera_geometry["width"] - roi_width) // 2
        roi_y = (self.camera_geometry["height"] - roi_height) // 2
        
        self.roi = {"x": roi_x, "y": roi_y, "w": roi_width, "h": roi_height}
        
        print(f"ROI berhasil ditempatkan di tengah: x={self.roi['x']}, y={self.roi['y']}, w={self.roi['w']}, h={self.roi['h']}")
    
    def stop_camera(self):
        self.camera_active = False
        self.camera_timer.stop()
        self.toolButton_3.setText("CAMERA")
        blank_image = np.zeros((self.frame.height(), self.frame.width(), 3), dtype=np.uint8)
        self.display_image(blank_image)
    
    def update_camera(self):
        if self.camera_active and self.camera is not None:
            ret, frame = self.camera.read()
            if ret:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                frame_rgb = cv2.resize(frame_rgb, (self.camera_geometry["width"], self.camera_geometry["height"]))
                
                self.current_frame = frame_rgb.copy()
                
                cv2.rectangle(
                    frame_rgb, 
                    (self.roi["x"], self.roi["y"]), 
                    (self.roi["x"] + self.roi["w"], self.roi["y"] + self.roi["h"]), 
                    (255, 0, 0),
                    1
                )
                
                for i, box in enumerate(self.bounding_boxes):
                    if not hasattr(self, 'selected_box_index'):
                        self.selected_box_index = -1
                        
                    color = (255, 0, 0)
                    thickness = 1
                    
                    if i == self.selected_box_index:
                        color = (0, 0, 255)
                        thickness = 2
                    
                    if "x" in box and "y" in box and "w" in box and "h" in box:
                        cv2.rectangle(
                            frame_rgb,
                            (box["x"], box["y"]),
                            (box["x"] + box["w"], box["y"] + box["h"]),
                            color,
                            thickness
                        )
                
                if hasattr(self, 'drawing_box') and self.drawing_box and self.current_box:
                    cv2.rectangle(
                        frame_rgb,
                        (self.current_box["x"], self.current_box["y"]),
                        (self.current_box["x"] + self.current_box["w"], self.current_box["y"] + self.current_box["h"]),
                        (0, 255, 255),
                        1
                    )
                
                self.display_image(frame_rgb)
    
    def display_image(self, img):
        img = cv2.resize(img, (self.camera_geometry["width"], self.camera_geometry["height"]))
        
        h, w, ch = img.shape
        bytes_per_line = ch * w
        qt_image = QtGui.QImage(img.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        
        pixmap = QtGui.QPixmap.fromImage(qt_image)
        self.frame.setPixmap(pixmap)
    
    def mouse_press_event(self, event):
        if not self.camera_active:
            return
            
        x, y = event.x() - self.camera_geometry["x"], event.y() - self.camera_geometry["y"]
        
        for i, box in enumerate(self.bounding_boxes):
            if (box["x"] <= x <= box["x"] + box["w"] and 
                box["y"] <= y <= box["y"] + box["h"]):
                self.selected_box_index = i
                self.dragging_box = True
                self.drag_start_x = x
                self.drag_start_y = y
                return
        
        self.selected_box_index = -1
        self.drawing_box = True
        self.current_box = {"x": x, "y": y, "w": 0, "h": 0}
    
    def mouse_move_event(self, event):
        if not self.camera_active:
            return
            
        x, y = event.x() - self.camera_geometry["x"], event.y() - self.camera_geometry["y"]
        
        if self.drawing_box and self.current_box:
            self.current_box["w"] = x - self.current_box["x"]
            self.current_box["h"] = y - self.current_box["y"]
        
        elif self.dragging_box and self.selected_box_index >= 0:
            dx = x - self.drag_start_x
            dy = y - self.drag_start_y
            
            self.bounding_boxes[self.selected_box_index]["x"] += dx
            self.bounding_boxes[self.selected_box_index]["y"] += dy
            
            self.drag_start_x = x
            self.drag_start_y = y
    
    def mouse_release_event(self, event):
        if self.drawing_box and self.current_box:
            if self.current_box["w"] < 0:
                self.current_box["x"] += self.current_box["w"]
                self.current_box["w"] = abs(self.current_box["w"])
            
            if self.current_box["h"] < 0:
                self.current_box["y"] += self.current_box["h"]
                self.current_box["h"] = abs(self.current_box["h"])
            
            if self.current_box["w"] > 10 and self.current_box["h"] > 10:
                self.current_box["timestamp"] = datetime.datetime.now().isoformat()
                self.current_box["label"] = ""
                
                self.bounding_boxes.append(self.current_box)
                self.save_bounding_boxes()
            
            self.current_box = None
            self.drawing_box = False
        
        elif self.dragging_box:
            self.dragging_box = False
            self.save_bounding_boxes()
    
    def save_bounding_boxes(self, filename="bounding_boxes.json"):
        with open(filename, 'w') as f:
            json.dump(self.bounding_boxes, f, indent=4)
    
    def load_bounding_boxes(self, filename="bounding_boxes.json"):
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as f:
                    self.bounding_boxes = json.load(f)
            except Exception as e:
                print(f"Error loading bounding boxes: {e}")
                self.bounding_boxes = []
    
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
                        self.process_result(False, None)
                else:
                    print("Error: ROI tidak valid")
                    self.process_result(False, None)
            else:
                print("Error: Tidak dapat membaca frame")
                self.process_result(False, None)
        else:
            print("Error: Kamera tidak tersedia")
            self.process_result(False, None)
    
    def match_template(self, image):
        model_templates = self.templates.get(self.current_model, [])
        if not model_templates:
            print(f"Tidak ada template di Model {self.current_model}")
            return False, None
        
        best_match_val = -1
        best_match_template = None
        best_match_loc = None
        
        image_copy = image.copy()
        
        def preprocess_image(img):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            normalized = clahe.apply(gray)
            
            denoised = cv2.bilateralFilter(normalized, 9, 75, 75)
            
            edges = cv2.Canny(denoised, 50, 150)
            
            result = cv2.addWeighted(denoised, 0.7, edges, 0.3, 0)
            
            return result
        
        def compute_similarity(img1, img2):
            try:
                from skimage.metrics import structural_similarity as ssim
                score_ssim, _ = ssim(img1, img2, full=True)
            except ImportError:
                score_ssim = 0.5
            
            hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
            hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
            score_hist = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
            
            mse = np.mean((img1.astype(np.float32) - img2.astype(np.float32)) ** 2)
            score_mse = 1 / (1 + mse)
            
            result = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)
            _, score_tm, _, _ = cv2.minMaxLoc(result)
            
            weights = [0.3, 0.3, 0.2, 0.2]
            combined_score = (score_ssim * weights[0] + 
                             score_hist * weights[1] + 
                             score_mse * weights[2] + 
                             score_tm * weights[3])
            
            if score_hist > 0.7:
                combined_score = combined_score * 1.2
                
            scores = {
                "SSIM": score_ssim,
                "Histogram": score_hist,
                "MSE": score_mse,
                "TemplateMatching": score_tm,
                "Combined": combined_score
            }
            
            return combined_score, scores
        
        methods = [
            (cv2.TM_CCORR_NORMED, "CCORR_NORMED"),
            (cv2.TM_SQDIFF_NORMED, "SQDIFF_NORMED"),
            (cv2.TM_CCOEFF_NORMED, "CCOEFF_NORMED")
        ]
        
        for i, template_data in enumerate(model_templates):
            template = template_data["image"].copy()
            
            preprocessed_image = preprocess_image(image_copy)
            preprocessed_template = preprocess_image(template)
            
            similarity, detailed_scores = compute_similarity(preprocessed_image, preprocessed_template)
            
            for method, score in detailed_scores.items():
                print(f"Template {i} - Metode {method}: Nilai kecocokan = {score*100:.2f}%")
            
            print(f"Template {i} - Nilai kecocokan gabungan: {similarity*100:.2f}%")
            
            method_results = []
            
            for method, method_name in methods:
                result = cv2.matchTemplate(preprocessed_image, preprocessed_template, method)
                
                if method == cv2.TM_SQDIFF_NORMED:
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
                    current_val = 1.0 - min_val
                    current_loc = min_loc
                else:
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
                    current_val = max_val
                    current_loc = max_loc
                
                method_results.append((method_name, current_val, current_loc))
                
                print(f"Template {i} - Metode {method_name}: Nilai kecocokan = {current_val*100:.2f}%")
            
            avg_match_val = sum(res[1] for res in method_results) / len(method_results)
            print(f"Template {i} - Nilai kecocokan rata-rata: {avg_match_val*100:.2f}%")
            
            if similarity > best_match_val:
                best_match_val = similarity
                best_match_template = template_data
                
                for method_name, val, loc in method_results:
                    if method_name == "CCOEFF_NORMED":
                        best_match_loc = loc
        
        print(f"Nilai kecocokan terbaik: {best_match_val*100:.2f}% (Threshold: {self.template_matching_threshold*100:.2f}%)")
        
        if best_match_val >= self.template_matching_threshold:
            is_match = True
            print(f"Gambar COCOK: Nilai kecocokan ({best_match_val*100:.2f}%) melebihi threshold ({self.template_matching_threshold*100:.2f}%)")
        elif best_match_val > 0.25:
            print(f"Gambar COCOK: Nilai kecocokan ({best_match_val*100:.2f}%) cukup signifikan")
            is_match = True
        elif best_match_val > 0.15 and "Histogram" in detailed_scores and detailed_scores["Histogram"] > 0.4:
            print(f"Gambar COCOK: Nilai kecocokan ({best_match_val*100:.2f}%) dengan histogram tinggi ({detailed_scores['Histogram']*100:.2f}%)")
            is_match = True
        else:
            print(f"Gambar TIDAK COCOK: Nilai kecocokan ({best_match_val*100:.2f}%) terlalu rendah")
            is_match = False
        
        return is_match, best_match_template
    
    def process_result(self, match_result, best_match=None):
        if not self.process_active:
            return
        
        result = "PASS" if match_result else "FAIL"
        
        self.label_7.setText(result)
        
        if result == "PASS":
            self.label_2.setText("PASS")
            self.label_2.setStyleSheet("background-color: green; color: white; font-weight: bold; font-size: 16pt; qproperty-alignment: 'AlignCenter';")
            
            print("Hasil inspeksi: PASS - Gambar cocok dengan template")
            
            if self.camera_active and self.camera is not None:
                detection_box = {
                    "x": self.roi["x"],
                    "y": self.roi["y"],
                    "w": self.roi["w"],
                    "h": self.roi["h"],
                    "label": "",
                    "timestamp": datetime.datetime.now().isoformat()
                }
                
                self.bounding_boxes = [box for box in self.bounding_boxes 
                                      if box.get("timestamp", "") != detection_box["timestamp"]]
                
                self.bounding_boxes.append(detection_box)
                self.save_bounding_boxes()
                
                print("Bounding box berhasil ditambahkan pada objek yang cocok")
            
            # Dalam mode deteksi berkelanjutan, jangan buka Step2 secara otomatis
            # Pengguna harus menghentikan proses terlebih dahulu
        else:
            self.label_2.setText("FAIL")
            self.label_2.setStyleSheet("background-color: red; color: white; font-weight: bold; font-size: 16pt; qproperty-alignment: 'AlignCenter';")
            
            print("Hasil inspeksi: FAIL - Gambar tidak cocok dengan template")
            
            # Hapus bounding box lama jika ada
            current_timestamp = datetime.datetime.now().isoformat()
            self.bounding_boxes = [box for box in self.bounding_boxes 
                                  if not (datetime.datetime.now() - datetime.datetime.fromisoformat(box.get("timestamp", current_timestamp))).total_seconds() < 5]
            self.save_bounding_boxes()
    
    def stop_process(self):
        self.process_active = False
        
        if hasattr(self, 'detection_timer') and self.detection_timer.isActive():
            self.detection_timer.stop()
        
        self.label_6.setText("IDLE")
        self.label_2.setText("STOPPED")
        self.label_2.setStyleSheet("background-color: gray; color: white; font-weight: bold; font-size: 16pt; qproperty-alignment: 'AlignCenter';")
        
        self.pushButton_4.setEnabled(True)
        
        self.idle_start_time = datetime.datetime.now()
        
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
        except (ValueError, AttributeError) as e:
            print(f"Error saat mengambil ROI dari settings: {e}")

    def closeEvent(self, event):
        if self.camera is not None:
            self.camera.release()
        
        self.save_bounding_boxes()

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
        if not os.path.exists(self.models_dir):
            os.makedirs(self.models_dir)
            for i in range(1, 6):
                os.makedirs(os.path.join(self.models_dir, f"model{i}"), exist_ok=True)
            
            QMessageBox.information(self.MainWindow, "Info", 
                                   f"Folder models telah dibuat di {os.path.abspath(self.models_dir)}.\n"
                                   "Silakan tambahkan gambar template di folder tersebut.")
        
        self.templates = {}
        for i in range(1, 6):
            model_dir = os.path.join(self.models_dir, f"model{i}")
            os.makedirs(model_dir, exist_ok=True)
            
            image_files = glob.glob(os.path.join(model_dir, "*.jpg")) + \
                         glob.glob(os.path.join(model_dir, "*.png")) + \
                         glob.glob(os.path.join(model_dir, "*.jpeg"))
            
            model_templates = []
            for img_path in image_files:
                try:
                    template = cv2.imread(img_path)
                    if template is not None:
                        if len(template.shape) == 2:
                            template = cv2.cvtColor(template, cv2.COLOR_GRAY2BGR)
                        elif template.shape[2] == 4:
                            template = cv2.cvtColor(template, cv2.COLOR_RGBA2BGR)
                        
                        model_templates.append({
                            "path": img_path,
                            "image": template,
                            "name": os.path.basename(img_path)
                        })
                        print(f"Template berhasil dimuat: {img_path} (ukuran: {template.shape})")
                except Exception as e:
                    print(f"Error saat memuat template {img_path}: {e}")
            
            self.templates[i] = model_templates
        
        self.update_model_label()
    
    def select_model(self, model_number):
        if 1 <= model_number <= 5:
            self.current_model = model_number
            self.update_model_label()
            
            if len(self.templates.get(model_number, [])) == 0:
                QMessageBox.warning(self.MainWindow, "Peringatan", 
                                   f"Tidak ada template di Model {model_number}.\n"
                                   f"Silakan tambahkan gambar template di folder models/model{model_number}/")
    
    def update_model_label(self):
        self.label_11.setText(f"MODEL {self.current_model}")
        
        template_count = len(self.templates.get(self.current_model, []))
        print(f"Model {self.current_model} dipilih dengan {template_count} template")
    
    def save_settings(self):
        try:
            threshold_text = self.settings_ui.textEdit_2.toPlainText()
            if threshold_text:
                if threshold_text.endswith('%'):
                    try:
                        threshold = float(threshold_text.rstrip('%')) / 100.0
                    except ValueError:
                        threshold = float(threshold_text)
                else:
                    threshold = float(threshold_text)
                
                if 0 <= threshold <= 1:
                    self.template_matching_threshold = threshold
                    print(f"Threshold template matching berhasil diubah menjadi: {threshold*100:.2f}%")
                else:
                    QMessageBox.warning(self.settings_window, "Peringatan", 
                                      "Threshold harus berada di antara 0 dan 1 (atau 0% dan 100%)")
            
            model_index = self.settings_ui.comboBox.currentIndex()
            if 0 <= model_index <= 4:
                self.select_model(model_index + 1)
        except Exception as e:
            print(f"Error saat menyimpan pengaturan: {e}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
