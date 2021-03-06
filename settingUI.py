# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import tkinter as tk
from PIL import ImageTk, Image

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(640, 480))
        mainWindow.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/Settings.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setWindowOpacity(1.0)
        mainWindow.setAutoFillBackground(True)
        mainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 210, 461, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(25, 25))
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.hcc_tab = QtWidgets.QWidget()
        self.hcc_tab.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.hcc_tab.setObjectName("hcc_tab")
        self.label_fistSF = QtWidgets.QLabel(self.hcc_tab)
        self.label_fistSF.setGeometry(QtCore.QRect(20, 40, 121, 20))
        self.label_fistSF.setObjectName("label_fistSF")
        self.label_fistN = QtWidgets.QLabel(self.hcc_tab)
        self.label_fistN.setGeometry(QtCore.QRect(20, 80, 121, 20))
        self.label_fistN.setObjectName("label_fistN")
        self.label_palmSF = QtWidgets.QLabel(self.hcc_tab)
        self.label_palmSF.setGeometry(QtCore.QRect(20, 120, 131, 20))
        self.label_palmSF.setObjectName("label_palmSF")
        self.label_palmN = QtWidgets.QLabel(self.hcc_tab)
        self.label_palmN.setGeometry(QtCore.QRect(20, 160, 121, 20))
        self.label_palmN.setObjectName("label_palmN")
        self.spinBox_fistN = QtWidgets.QSpinBox(self.hcc_tab)
        self.spinBox_fistN.setGeometry(QtCore.QRect(150, 80, 71, 22))
        self.spinBox_fistN.setMinimum(1)
        self.spinBox_fistN.setMaximum(30)
        self.spinBox_fistN.setProperty("value", 3)
        self.spinBox_fistN.setObjectName("spinBox_fistN")
        self.spinBox_palmN = QtWidgets.QSpinBox(self.hcc_tab)
        self.spinBox_palmN.setGeometry(QtCore.QRect(150, 160, 71, 22))
        self.spinBox_palmN.setMinimum(1)
        self.spinBox_palmN.setMaximum(30)
        self.spinBox_palmN.setProperty("value", 7)
        self.spinBox_palmN.setObjectName("spinBox_palmN")
        self.label_blurSize = QtWidgets.QLabel(self.hcc_tab)
        self.label_blurSize.setGeometry(QtCore.QRect(260, 40, 121, 20))
        self.label_blurSize.setObjectName("label_blurSize")
        self.spinBox_blurSize = QtWidgets.QSpinBox(self.hcc_tab)
        self.spinBox_blurSize.setGeometry(QtCore.QRect(380, 40, 71, 22))
        self.spinBox_blurSize.setMinimum(1)
        self.spinBox_blurSize.setMaximum(9)
        self.spinBox_blurSize.setSingleStep(2)
        self.spinBox_blurSize.setProperty("value", 3)
        self.spinBox_blurSize.setObjectName("spinBox_blurSize")
        self.label_frameInputSize = QtWidgets.QLabel(self.hcc_tab)
        self.label_frameInputSize.setGeometry(QtCore.QRect(260, 80, 121, 20))
        self.label_frameInputSize.setObjectName("label_frameInputSize")
        self.label_movingAvgSize = QtWidgets.QLabel(self.hcc_tab)
        self.label_movingAvgSize.setGeometry(QtCore.QRect(260, 120, 131, 20))
        self.label_movingAvgSize.setObjectName("label_movingAvgSize")
        self.spinBox_movingAvgSize = QtWidgets.QSpinBox(self.hcc_tab)
        self.spinBox_movingAvgSize.setGeometry(QtCore.QRect(380, 120, 71, 22))
        self.spinBox_movingAvgSize.setMinimum(2)
        self.spinBox_movingAvgSize.setMaximum(50)
        self.spinBox_movingAvgSize.setProperty("value", 5)
        self.spinBox_movingAvgSize.setObjectName("spinBox_movingAvgSize")
        self.pushButton_saveHcc = QtWidgets.QPushButton(self.hcc_tab)
        self.pushButton_saveHcc.setGeometry(QtCore.QRect(260, 163, 191, 31))
        self.pushButton_saveHcc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_saveHcc.setAutoDefault(False)
        self.pushButton_saveHcc.setDefault(False)
        self.pushButton_saveHcc.setFlat(False)
        self.pushButton_saveHcc.setObjectName("pushButton_saveHcc")
        self.spinBox_fistSF = QtWidgets.QDoubleSpinBox(self.hcc_tab)
        self.spinBox_fistSF.setGeometry(QtCore.QRect(150, 40, 71, 22))
        self.spinBox_fistSF.setDecimals(2)
        self.spinBox_fistSF.setMinimum(1.01)
        self.spinBox_fistSF.setMaximum(1.99)
        self.spinBox_fistSF.setSingleStep(0.01)
        self.spinBox_fistSF.setProperty("value", 1.2)
        self.spinBox_fistSF.setObjectName("spinBox_fistSF")
        self.spinBox_palmSF = QtWidgets.QDoubleSpinBox(self.hcc_tab)
        self.spinBox_palmSF.setGeometry(QtCore.QRect(150, 120, 71, 22))
        self.spinBox_palmSF.setMinimum(1.01)
        self.spinBox_palmSF.setMaximum(1.99)
        self.spinBox_palmSF.setSingleStep(0.01)
        self.spinBox_palmSF.setProperty("value", 1.07)
        self.spinBox_palmSF.setObjectName("spinBox_palmSF")
        self.spinBox_frameInputSize = QtWidgets.QDoubleSpinBox(self.hcc_tab)
        self.spinBox_frameInputSize.setGeometry(QtCore.QRect(380, 80, 71, 22))
        self.spinBox_frameInputSize.setMinimum(0.1)
        self.spinBox_frameInputSize.setMaximum(5.0)
        self.spinBox_frameInputSize.setSingleStep(0.1)
        self.spinBox_frameInputSize.setProperty("value", 0.6)
        self.spinBox_frameInputSize.setObjectName("spinBox_frameInputSize")
        self.tabWidget.addTab(self.hcc_tab, "")
        self.hsv_tab = QtWidgets.QWidget()
        self.hsv_tab.setObjectName("hsv_tab")
        self.label_4 = QtWidgets.QLabel(self.hsv_tab)
        self.label_4.setGeometry(QtCore.QRect(40, 50, 361, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.hsv_tab)
        self.label_5.setGeometry(QtCore.QRect(40, 100, 361, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.hsv_tab, "")
        self.cnn_tab = QtWidgets.QWidget()
        self.cnn_tab.setObjectName("cnn_tab")
        self.label_6 = QtWidgets.QLabel(self.cnn_tab)
        self.label_6.setGeometry(QtCore.QRect(40, 100, 361, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.cnn_tab)
        self.label_7.setGeometry(QtCore.QRect(40, 50, 361, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.cnn_tab, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 321, 41))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 561, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 561, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(561, 71))
        self.label_3.setMaximumSize(QtCore.QSize(561, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.pushButton_Instruction = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Instruction.setGeometry(QtCore.QRect(30, 170, 121, 31))
        self.pushButton_Instruction.setObjectName("pushButton_Instruction")
        self.spinBox_camID = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_camID.setGeometry(QtCore.QRect(570, 280, 41, 22))
        self.spinBox_camID.setMaximum(5)
        self.spinBox_camID.setObjectName("cam_id")
        self.label_cameraID = QtWidgets.QLabel(self.centralwidget)
        self.label_cameraID.setGeometry(QtCore.QRect(490, 280, 71, 20))
        self.label_cameraID.setObjectName("label_cameraID")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(480, 220, 141, 211))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.checkBox_showWin = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_showWin.setGeometry(QtCore.QRect(10, 100, 111, 20))
        self.checkBox_showWin.setObjectName("checkBox_showWin")
        self.checkBox_showWin.setChecked(True)
        self.checkBox_showDetBorder = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_showDetBorder.setGeometry(QtCore.QRect(10, 130, 131, 20))
        self.checkBox_showDetBorder.setCheckable(True)
        self.checkBox_showDetBorder.setObjectName("checkBox_showDetBorder")
        self.checkBox_showDetBorder.setChecked(True)
        self.groupBox.raise_()
        self.tabWidget.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton_Instruction.raise_()
        self.spinBox_camID.raise_()
        self.label_cameraID.raise_()
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.pushButton_Instruction.clicked.connect(self.showInstruction)

        self.packedSetupVal = None
        self.pushButton_saveHcc.clicked.connect(self.getVal)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def getPackedVal(self):
        global parameters
        parameters = self.packedSetupVal

    def cekbox(self):
        print(self.checkBox_showDetBorder.checkState())

    def getVal(self):
        fistSF = self.spinBox_fistSF.value()
        fistN = self.spinBox_fistN.value()
        palmSF = self.spinBox_palmSF.value()
        palmN = self.spinBox_palmN.value()
        blurSize = self.spinBox_blurSize.value()
        inputSize = self.spinBox_frameInputSize.value()
        avgSize = self.spinBox_movingAvgSize.value()

        cam_id = self.spinBox_camID.value()
        showWin = self.checkBox_showWin.checkState()
        showBorder = self.checkBox_showDetBorder.checkState()

        self.packedSetupVal = [[fistSF, fistN, palmSF, palmN, blurSize,inputSize,avgSize],[cam_id,showWin, showBorder]]
        global parameters
        parameters = self.packedSetupVal

    def showInstruction(self):
        root = tk.Tk()
        root.title('Instructions')
        root.iconbitmap('assets/init/logo1.ico')
        inst_img = ImageTk.PhotoImage(Image.open('assets/instruction/hcc_instructions.png'))
        label1 = tk.Label(root, image=inst_img)
        label1.pack()
        root.mainloop()

    def showpop(self):
        msg = QMessageBox()
        msg.setWindowTitle("Wrong Camera ID")
        msg.setText('Make sure you set the right Camera ID before run!')
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        #msg.setInformativeText('Info nih')
        #msg.setDetailedText('detailss')
        x = msg.exec_()

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Settings"))
        self.label_fistSF.setText(_translate("mainWindow", "Fist Scale Factor"))
        self.label_fistN.setText(_translate("mainWindow", "Fist Neighbour"))
        self.label_palmSF.setText(_translate("mainWindow", "Palm Scale Factor"))
        self.label_palmN.setText(_translate("mainWindow", "Palm Neighbour"))
        self.label_blurSize.setText(_translate("mainWindow", "Blur Kernel Size"))
        self.label_frameInputSize.setText(_translate("mainWindow", "Max Input Size"))
        self.label_movingAvgSize.setText(_translate("mainWindow", "Moving Avg. Size"))
        self.pushButton_saveHcc.setText(_translate("mainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hcc_tab), _translate("mainWindow", "     HCC     "))
        self.label_4.setText(_translate("mainWindow", "THIS FEATURE WILL AVAILABLE ON THE FUTURE VERSION!"))
        self.label_5.setText(_translate("mainWindow", "STAY UPDATE AT TARASERA.ORG"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hsv_tab), _translate("mainWindow", "     HSV     "))
        self.label_6.setText(_translate("mainWindow", "STAY UPDATE AT TARASERA.ORG"))
        self.label_7.setText(_translate("mainWindow", "THIS FEATURE WILL AVAILABLE ON THE FUTURE VERSION!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cnn_tab), _translate("mainWindow", "     CNN     "))
        self.label.setText(_translate("mainWindow", "NOTES:"))
        self.label_2.setText(_translate("mainWindow", "Make sure you have read the instructions before changing the parameters below!"))
        self.label_3.setText(_translate("mainWindow", "These parameters have been set to suit general devices specification. On some device might work, but on the other cases you have to change it to get the best performance! (PRESS ESC TO QUIT FROM DETECTION WINDOW"))
        self.pushButton_Instruction.setText(_translate("mainWindow", "Instructions"))
        self.label_cameraID.setText(_translate("mainWindow", "Camera ID"))
        self.groupBox.setTitle(_translate("mainWindow", "Vision Setting"))
        self.checkBox_showWin.setText(_translate("mainWindow", "Show Window"))
        self.checkBox_showDetBorder.setText(_translate("mainWindow", "Show Det. Border"))


"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    app.exec_()"""

parameters = None

def run():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    app.exec_()

def getParameters():
    return parameters