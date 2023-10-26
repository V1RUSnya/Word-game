# -*- coding: cp1251 -*-
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(412, 562)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 411, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.guessLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.guessLayout.setContentsMargins(0, 0, 0, 0)
        self.guessLayout.setObjectName("guessLayout")
        self.line_20 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_20.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_20.setObjectName("line_20")
        self.guessLayout.addWidget(self.line_20, 4, 3, 1, 1)
        self.line_18 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_18.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_18.setObjectName("line_18")
        self.guessLayout.addWidget(self.line_18, 3, 8, 1, 1)
        self.L32 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L32.setText("")
        self.L32.setObjectName("L32")
        self.guessLayout.addWidget(self.L32, 4, 2, 1, 1)
        self.L31 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L31.setText("")
        self.L31.setObjectName("L31")
        self.guessLayout.addWidget(self.L31, 4, 0, 1, 1)
        self.line_21 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_21.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_21.setObjectName("line_21")
        self.guessLayout.addWidget(self.line_21, 4, 5, 1, 1)
        self.line_16 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_16.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_16.setObjectName("line_16")
        self.guessLayout.addWidget(self.line_16, 3, 4, 1, 1)
        self.L34 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L34.setText("")
        self.L34.setObjectName("L34")
        self.guessLayout.addWidget(self.L34, 4, 6, 1, 1)
        self.L33 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L33.setText("")
        self.L33.setObjectName("L33")
        self.guessLayout.addWidget(self.L33, 4, 4, 1, 1)
        self.line_17 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_17.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_17.setObjectName("line_17")
        self.guessLayout.addWidget(self.line_17, 3, 6, 1, 1)
        self.line_14 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_14.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_14.setObjectName("line_14")
        self.guessLayout.addWidget(self.line_14, 3, 0, 1, 1)
        self.line_11 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_11.setObjectName("line_11")
        self.guessLayout.addWidget(self.line_11, 2, 3, 1, 1)
        self.line_13 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_13.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_13.setObjectName("line_13")
        self.guessLayout.addWidget(self.line_13, 2, 7, 1, 1)
        self.line_15 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_15.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_15.setObjectName("line_15")
        self.guessLayout.addWidget(self.line_15, 3, 2, 1, 1)
        self.line_12 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_12.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_12.setObjectName("line_12")
        self.guessLayout.addWidget(self.line_12, 2, 5, 1, 1)
        self.L22 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L22.setText("")
        self.L22.setObjectName("L22")
        self.guessLayout.addWidget(self.L22, 2, 2, 1, 1)
        self.line_10 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_10.setObjectName("line_10")
        self.guessLayout.addWidget(self.line_10, 2, 1, 1, 1)
        self.L24 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L24.setText("")
        self.L24.setObjectName("L24")
        self.guessLayout.addWidget(self.L24, 2, 6, 1, 1)
        self.L25 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L25.setText("")
        self.L25.setObjectName("L25")
        self.guessLayout.addWidget(self.L25, 2, 8, 1, 1)
        self.L21 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L21.setText("")
        self.L21.setObjectName("L21")
        self.guessLayout.addWidget(self.L21, 2, 0, 1, 1)
        self.L23 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L23.setText("")
        self.L23.setObjectName("L23")
        self.guessLayout.addWidget(self.L23, 2, 4, 1, 1)
        self.line_23 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_23.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_23.setObjectName("line_23")
        self.guessLayout.addWidget(self.line_23, 5, 0, 1, 1)
        self.L42 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L42.setText("")
        self.L42.setObjectName("L42")
        self.guessLayout.addWidget(self.L42, 6, 2, 1, 1)
        self.L35 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L35.setText("")
        self.L35.setObjectName("L35")
        self.guessLayout.addWidget(self.L35, 4, 8, 1, 1)
        self.line_19 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_19.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_19.setObjectName("line_19")
        self.guessLayout.addWidget(self.line_19, 4, 1, 1, 1)
        self.line_27 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_27.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_27.setObjectName("line_27")
        self.guessLayout.addWidget(self.line_27, 5, 8, 1, 1)
        self.line_25 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_25.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_25.setObjectName("line_25")
        self.guessLayout.addWidget(self.line_25, 5, 4, 1, 1)
        self.line_22 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_22.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_22.setObjectName("line_22")
        self.guessLayout.addWidget(self.line_22, 4, 7, 1, 1)
        self.L43 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L43.setText("")
        self.L43.setObjectName("L43")
        self.guessLayout.addWidget(self.L43, 6, 4, 1, 1)
        self.line_26 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_26.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_26.setObjectName("line_26")
        self.guessLayout.addWidget(self.line_26, 5, 6, 1, 1)
        self.line_30 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_30.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_30.setObjectName("line_30")
        self.guessLayout.addWidget(self.line_30, 6, 3, 1, 1)
        self.line_29 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_29.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_29.setObjectName("line_29")
        self.guessLayout.addWidget(self.line_29, 6, 5, 1, 1)
        self.line_24 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_24.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_24.setObjectName("line_24")
        self.guessLayout.addWidget(self.line_24, 5, 2, 1, 1)
        self.line_28 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_28.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_28.setObjectName("line_28")
        self.guessLayout.addWidget(self.line_28, 6, 7, 1, 1)
        self.L44 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L44.setText("")
        self.L44.setObjectName("L44")
        self.guessLayout.addWidget(self.L44, 6, 6, 1, 1)
        self.L45 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L45.setText("")
        self.L45.setObjectName("L45")
        self.guessLayout.addWidget(self.L45, 6, 8, 1, 1)
        self.L41 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L41.setText("")
        self.L41.setObjectName("L41")
        self.guessLayout.addWidget(self.L41, 6, 0, 1, 1)
        self.line_31 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_31.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_31.setObjectName("line_31")
        self.guessLayout.addWidget(self.line_31, 6, 1, 1, 1)
        self.L51 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L51.setText("")
        self.L51.setObjectName("L51")
        self.guessLayout.addWidget(self.L51, 8, 0, 1, 1)
        self.L53 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L53.setText("")
        self.L53.setObjectName("L53")
        self.guessLayout.addWidget(self.L53, 8, 4, 1, 1)
        self.L52 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L52.setText("")
        self.L52.setObjectName("L52")
        self.guessLayout.addWidget(self.L52, 8, 2, 1, 1)
        self.L55 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L55.setText("")
        self.L55.setObjectName("L55")
        self.guessLayout.addWidget(self.L55, 8, 8, 1, 1)
        self.line_6 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.guessLayout.addWidget(self.line_6, 1, 0, 1, 1)
        self.L54 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L54.setText("")
        self.L54.setObjectName("L54")
        self.guessLayout.addWidget(self.L54, 8, 6, 1, 1)
        self.line_5 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.guessLayout.addWidget(self.line_5, 1, 2, 1, 1)
        self.L13 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L13.setText("")
        self.L13.setObjectName("L13")
        self.guessLayout.addWidget(self.L13, 0, 4, 1, 1)
        self.L11 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L11.setText("")
        self.L11.setObjectName("L11")
        self.guessLayout.addWidget(self.L11, 0, 0, 1, 1)
        self.L15 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L15.setText("")
        self.L15.setObjectName("L15")
        self.guessLayout.addWidget(self.L15, 0, 8, 1, 1)
        self.L14 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L14.setText("")
        self.L14.setObjectName("L14")
        self.guessLayout.addWidget(self.L14, 0, 6, 1, 1)
        self.line_9 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_9.setObjectName("line_9")
        self.guessLayout.addWidget(self.line_9, 1, 6, 1, 1)
        self.line = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.guessLayout.addWidget(self.line, 0, 1, 1, 1)
        self.L12 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.L12.setText("")
        self.L12.setObjectName("L12")
        self.guessLayout.addWidget(self.L12, 0, 2, 1, 1)
        self.line_3 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.guessLayout.addWidget(self.line_3, 0, 5, 1, 1)
        self.line_2 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.guessLayout.addWidget(self.line_2, 0, 3, 1, 1)
        self.line_8 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_8.setObjectName("line_8")
        self.guessLayout.addWidget(self.line_8, 1, 8, 1, 1)
        self.line_4 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.guessLayout.addWidget(self.line_4, 0, 7, 1, 1)
        self.line_7 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_7.setObjectName("line_7")
        self.guessLayout.addWidget(self.line_7, 1, 4, 1, 1)
        self.line_38 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_38.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_38.setObjectName("line_38")
        self.guessLayout.addWidget(self.line_38, 5, 1, 1, 1)
        self.line_32 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_32.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_32.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_32.setObjectName("line_32")
        self.guessLayout.addWidget(self.line_32, 7, 8, 1, 1)
        self.line_33 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_33.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_33.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_33.setObjectName("line_33")
        self.guessLayout.addWidget(self.line_33, 7, 6, 1, 1)
        self.line_37 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_37.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_37.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_37.setObjectName("line_37")
        self.guessLayout.addWidget(self.line_37, 7, 1, 1, 1)
        self.line_35 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_35.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_35.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_35.setObjectName("line_35")
        self.guessLayout.addWidget(self.line_35, 7, 2, 1, 1)
        self.line_36 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_36.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_36.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_36.setObjectName("line_36")
        self.guessLayout.addWidget(self.line_36, 7, 0, 1, 1)
        self.line_39 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_39.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_39.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_39.setObjectName("line_39")
        self.guessLayout.addWidget(self.line_39, 3, 1, 1, 1)
        self.line_34 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_34.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_34.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_34.setObjectName("line_34")
        self.guessLayout.addWidget(self.line_34, 7, 4, 1, 1)
        self.line_41 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_41.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_41.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_41.setObjectName("line_41")
        self.guessLayout.addWidget(self.line_41, 1, 3, 1, 1)
        self.line_45 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_45.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_45.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_45.setObjectName("line_45")
        self.guessLayout.addWidget(self.line_45, 7, 5, 1, 1)
        self.line_46 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_46.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_46.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_46.setObjectName("line_46")
        self.guessLayout.addWidget(self.line_46, 5, 5, 1, 1)
        self.line_43 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_43.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_43.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_43.setObjectName("line_43")
        self.guessLayout.addWidget(self.line_43, 3, 3, 1, 1)
        self.line_42 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_42.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_42.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_42.setObjectName("line_42")
        self.guessLayout.addWidget(self.line_42, 5, 3, 1, 1)
        self.line_44 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_44.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_44.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_44.setObjectName("line_44")
        self.guessLayout.addWidget(self.line_44, 7, 3, 1, 1)
        self.line_47 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_47.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_47.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_47.setObjectName("line_47")
        self.guessLayout.addWidget(self.line_47, 3, 5, 1, 1)
        self.line_40 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_40.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_40.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_40.setObjectName("line_40")
        self.guessLayout.addWidget(self.line_40, 1, 1, 1, 1)
        self.line_48 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_48.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_48.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_48.setObjectName("line_48")
        self.guessLayout.addWidget(self.line_48, 1, 5, 1, 1)
        self.line_49 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_49.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_49.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_49.setObjectName("line_49")
        self.guessLayout.addWidget(self.line_49, 1, 7, 1, 1)
        self.line_54 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_54.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_54.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_54.setObjectName("line_54")
        self.guessLayout.addWidget(self.line_54, 8, 5, 1, 1)
        self.line_50 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_50.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_50.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_50.setObjectName("line_50")
        self.guessLayout.addWidget(self.line_50, 3, 7, 1, 1)
        self.line_53 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_53.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_53.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_53.setObjectName("line_53")
        self.guessLayout.addWidget(self.line_53, 8, 7, 1, 1)
        self.line_52 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_52.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_52.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_52.setObjectName("line_52")
        self.guessLayout.addWidget(self.line_52, 7, 7, 1, 1)
        self.line_55 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_55.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_55.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_55.setObjectName("line_55")
        self.guessLayout.addWidget(self.line_55, 8, 3, 1, 1)
        self.line_51 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_51.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_51.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_51.setObjectName("line_51")
        self.guessLayout.addWidget(self.line_51, 5, 7, 1, 1)
        self.line_56 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_56.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_56.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_56.setObjectName("line_56")
        self.guessLayout.addWidget(self.line_56, 8, 1, 1, 1)
        self.line_66 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_66.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_66.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_66.setObjectName("line_66")
        self.guessLayout.addWidget(self.line_66, 9, 0, 1, 1)
        self.line_67 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_67.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_67.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_67.setObjectName("line_67")
        self.guessLayout.addWidget(self.line_67, 9, 2, 1, 1)
        self.line_68 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_68.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_68.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_68.setObjectName("line_68")
        self.guessLayout.addWidget(self.line_68, 9, 4, 1, 1)
        self.line_69 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_69.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_69.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_69.setObjectName("line_69")
        self.guessLayout.addWidget(self.line_69, 9, 6, 1, 1)
        self.line_70 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line_70.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_70.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_70.setObjectName("line_70")
        self.guessLayout.addWidget(self.line_70, 9, 8, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 380, 411, 71))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.AnswerLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.AnswerLayout.setContentsMargins(0, 0, 0, 0)
        self.AnswerLayout.setObjectName("AnswerLayout")
        self.A1 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.A1.setText("")
        self.A1.setObjectName("A1")
        self.AnswerLayout.addWidget(self.A1, 1, 0, 1, 1)
        self.line_62 = QtWidgets.QFrame(parent=self.gridLayoutWidget_2)
        self.line_62.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_62.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_62.setObjectName("line_62")
        self.AnswerLayout.addWidget(self.line_62, 0, 2, 1, 1)
        self.line_61 = QtWidgets.QFrame(parent=self.gridLayoutWidget_2)
        self.line_61.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_61.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_61.setObjectName("line_61")
        self.AnswerLayout.addWidget(self.line_61, 0, 0, 1, 1)
        self.line_60 = QtWidgets.QFrame(parent=self.gridLayoutWidget_2)
        self.line_60.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_60.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_60.setObjectName("line_60")
        self.AnswerLayout.addWidget(self.line_60, 1, 7, 1, 1)
        self.line_63 = QtWidgets.QFrame(parent=self.gridLayoutWidget_2)
        self.line_63.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_63.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_63.setObjectName("line_63")
        self.AnswerLayout.addWidget(self.line_63, 0, 4, 1, 1)
        self.line_58 = QtWidgets.QFrame(parent=self.gridLayoutWidget_2)
        self.line_58.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_58.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_58.setObjectName("line_58")
        self.AnswerLayout.addWidget(self.line_58, 1, 3, 1, 1)
        self.line_59 = QtWidgets.QFrame(parent=self.gridLayoutWidget_2)
        self.line_59.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_59.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_59.setObjectName("line_59")
        self.AnswerLayout.addWidget(self.line_59, 1, 5, 1, 1)
        self.line_64 = QtWidgets.QFrame(parent=self.gridLayoutWidget_2)
        self.line_64.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_64.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_64.setObjectName("line_64")
        self.AnswerLayout.addWidget(self.line_64, 0, 6, 1, 1)
        self.A5 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.A5.setText("")
        self.A5.setObjectName("A5")
        self.AnswerLayout.addWidget(self.A5, 1, 8, 1, 1)
        self.line_57 = QtWidgets.QFrame(parent=self.gridLayoutWidget_2)
        self.line_57.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_57.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_57.setObjectName("line_57")
        self.AnswerLayout.addWidget(self.line_57, 1, 1, 1, 1)
        self.A3 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.A3.setText("")
        self.A3.setObjectName("A3")
        self.AnswerLayout.addWidget(self.A3, 1, 4, 1, 1)
        self.line_65 = QtWidgets.QFrame(parent=self.gridLayoutWidget_2)
        self.line_65.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_65.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_65.setObjectName("line_65")
        self.AnswerLayout.addWidget(self.line_65, 0, 8, 1, 1)
        self.A4 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.A4.setText("")
        self.A4.setObjectName("A4")
        self.AnswerLayout.addWidget(self.A4, 1, 6, 1, 1)
        self.A2 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.A2.setText("")
        self.A2.setObjectName("A2")
        self.AnswerLayout.addWidget(self.A2, 1, 2, 1, 1)
        self.line_71 = QtWidgets.QFrame(parent=self.gridLayoutWidget_2)
        self.line_71.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_71.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_71.setObjectName("line_71")
        self.AnswerLayout.addWidget(self.line_71, 2, 6, 1, 1)
        self.line_72 = QtWidgets.QFrame(parent=self.gridLayoutWidget_2)
        self.line_72.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_72.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_72.setObjectName("line_72")
        self.AnswerLayout.addWidget(self.line_72, 2, 8, 1, 1)
        self.line_73 = QtWidgets.QFrame(parent=self.gridLayoutWidget_2)
        self.line_73.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_73.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_73.setObjectName("line_73")
        self.AnswerLayout.addWidget(self.line_73, 2, 4, 1, 1)
        self.line_74 = QtWidgets.QFrame(parent=self.gridLayoutWidget_2)
        self.line_74.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_74.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_74.setObjectName("line_74")
        self.AnswerLayout.addWidget(self.line_74, 2, 2, 1, 1)
        self.line_75 = QtWidgets.QFrame(parent=self.gridLayoutWidget_2)
        self.line_75.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_75.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_75.setObjectName("line_75")
        
        
        self.font = QFont()
        self.font.setPointSize(24)
        self.L11.setFont(self.font)
        self.L12.setFont(self.font)
        self.L13.setFont(self.font)
        self.L14.setFont(self.font)
        self.L15.setFont(self.font)
        
        self.L21.setFont(self.font)
        self.L22.setFont(self.font)
        self.L23.setFont(self.font)
        self.L24.setFont(self.font)
        self.L25.setFont(self.font)

        self.L31.setFont(self.font)
        self.L32.setFont(self.font)
        self.L33.setFont(self.font)
        self.L34.setFont(self.font)
        self.L35.setFont(self.font)

        self.L41.setFont(self.font)
        self.L42.setFont(self.font)
        self.L43.setFont(self.font)
        self.L44.setFont(self.font)
        self.L45.setFont(self.font)
        
        self.L51.setFont(self.font)
        self.L52.setFont(self.font)
        self.L53.setFont(self.font)
        self.L54.setFont(self.font)
        self.L55.setFont(self.font)
        
        self.A1.setStyleSheet("background-color: black;")
        self.A2.setStyleSheet("background-color: black;")
        self.A3.setStyleSheet("background-color: black;")
        self.A4.setStyleSheet("background-color: black;")
        self.A5.setStyleSheet("background-color: black;")
        
        self.A1.setFont(self.font)
        self.A2.setFont(self.font)
        self.A3.setFont(self.font)
        self.A4.setFont(self.font)
        self.A5.setFont(self.font)
        
        
        
        self.AnswerLayout.addWidget(self.line_75, 2, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 450, 411, 111))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.keyboardLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.keyboardLayout.setContentsMargins(0, 0, 0, 0)
        self.keyboardLayout.setObjectName("keyboardLayout")
        self.But14 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But14.setObjectName("But14")
        self.keyboardLayout.addWidget(self.But14, 1, 1, 1, 1)
        self.But18 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But18.setObjectName("But18")
        self.keyboardLayout.addWidget(self.But18, 1, 5, 1, 1)
        self.But17 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But17.setObjectName("But17")
        self.keyboardLayout.addWidget(self.But17, 1, 4, 1, 1)
        self.But16 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But16.setObjectName("But16")
        self.keyboardLayout.addWidget(self.But16, 1, 3, 1, 1)
        self.But19 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But19.setObjectName("But19")
        self.keyboardLayout.addWidget(self.But19, 1, 6, 1, 1)
        self.But1 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But1.setObjectName("But1")
        self.keyboardLayout.addWidget(self.But1, 0, 0, 1, 1)
        self.But10 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But10.setObjectName("But10")
        self.keyboardLayout.addWidget(self.But10, 0, 9, 1, 1)
        self.But11 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But11.setObjectName("But11")
        self.keyboardLayout.addWidget(self.But11, 0, 10, 1, 1)
        self.But12 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But12.setObjectName("But12")
        self.keyboardLayout.addWidget(self.But12, 0, 11, 1, 1)
        self.But7 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But7.setObjectName("But7")
        self.keyboardLayout.addWidget(self.But7, 0, 6, 1, 1)
        self.But6 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But6.setObjectName("But6")
        self.keyboardLayout.addWidget(self.But6, 0, 5, 1, 1)
        self.But5 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But5.setObjectName("But5")
        self.keyboardLayout.addWidget(self.But5, 0, 4, 1, 1)
        self.But2 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But2.setObjectName("But2")
        self.keyboardLayout.addWidget(self.But2, 0, 1, 1, 1)
        self.But4 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But4.setObjectName("But4")
        self.keyboardLayout.addWidget(self.But4, 0, 3, 1, 1)
        self.But3 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But3.setObjectName("But3")
        self.keyboardLayout.addWidget(self.But3, 0, 2, 1, 1)
        self.But13 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But13.setObjectName("But13")
        self.keyboardLayout.addWidget(self.But13, 1, 0, 1, 1)
        self.But15 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But15.setObjectName("But15")
        self.keyboardLayout.addWidget(self.But15, 1, 2, 1, 1)
        self.But9 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But9.setObjectName("But9")
        self.keyboardLayout.addWidget(self.But9, 0, 8, 1, 1)
        self.But8 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But8.setObjectName("But8")
        self.keyboardLayout.addWidget(self.But8, 0, 7, 1, 1)
        self.But22 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But22.setObjectName("But22")
        self.keyboardLayout.addWidget(self.But22, 1, 9, 1, 1)
        self.But20 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But20.setObjectName("But20")
        self.keyboardLayout.addWidget(self.But20, 1, 7, 1, 1)
        self.But23 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But23.setObjectName("But23")
        self.keyboardLayout.addWidget(self.But23, 1, 10, 1, 1)
        self.But21 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But21.setObjectName("But21")
        self.keyboardLayout.addWidget(self.But21, 1, 8, 1, 1)
        self.But32 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But32.setObjectName("But32")
        self.keyboardLayout.addWidget(self.But32, 2, 9, 1, 1)
        self.But31 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But31.setObjectName("But31")
        self.keyboardLayout.addWidget(self.But31, 2, 8, 1, 1)
        self.But30 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But30.setObjectName("But30")
        self.keyboardLayout.addWidget(self.But30, 2, 7, 1, 1)
        self.But29 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But29.setObjectName("But29")
        self.keyboardLayout.addWidget(self.But29, 2, 6, 1, 1)
        self.But28 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But28.setObjectName("But28")
        self.keyboardLayout.addWidget(self.But28, 2, 5, 1, 1)
        self.But27 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But27.setObjectName("But27")
        self.keyboardLayout.addWidget(self.But27, 2, 4, 1, 1)
        self.But26 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But26.setObjectName("But26")
        self.keyboardLayout.addWidget(self.But26, 2, 3, 1, 1)
        self.But25 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But25.setObjectName("But25")
        self.keyboardLayout.addWidget(self.But25, 2, 2, 1, 1)
        self.But24 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.But24.setObjectName("But24")
        self.keyboardLayout.addWidget(self.But24, 2, 1, 1, 1)
        
        def ProgressGame(num, label):
            tt = label[3]
            Space = " "*3
            if num == 11:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==0 and found == False:
                              self.L11.setStyleSheet("background-color: green;")
                              self.A1.setStyleSheet("")
                              self.A1.setText(Space + tt)
                              found = True
                         elif i!=0 and not found:
                              self.L11.setStyleSheet("background-color: yellow;")
            if num == 12:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==1 and found == False:
                              self.L12.setStyleSheet("background-color: green;")
                              self.A2.setStyleSheet("")
                              self.A2.setText(Space + tt)
                              found = True
                         elif i!=1 and not found:
                              self.L12.setStyleSheet("background-color: yellow;")
            if num == 13:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==2 and found == False:
                              self.L13.setStyleSheet("background-color: green;")
                              self.A3.setStyleSheet("")
                              self.A3.setText(Space + tt)
                              found = True
                         elif i!=2 and not found:
                              self.L13.setStyleSheet("background-color: yellow;")
            if num == 14:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==3 and found == False:
                              self.L14.setStyleSheet("background-color: green;")
                              self.A4.setStyleSheet("")
                              self.A4.setText(Space + tt)
                              found = True
                         elif i!=3 and not found:
                              self.L14.setStyleSheet("background-color: yellow;")
            if num == 15:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==4 and found == False:
                              self.L15.setStyleSheet("background-color: green;")
                              self.A5.setStyleSheet("")
                              self.A5.setText(Space + tt)
                              found = True
                         elif i!=4 and not found:
                              self.L15.setStyleSheet("background-color: yellow;")
            if num == 21:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==0 and found == False:
                              self.L21.setStyleSheet("background-color: green;")
                              self.A1.setStyleSheet("")
                              self.A1.setText(Space + tt)
                              found = True
                         elif i!=0 and not found:
                              self.L21.setStyleSheet("background-color: yellow;")
            if num == 22:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==1 and found == False:
                              self.L22.setStyleSheet("background-color: green;")
                              self.A2.setStyleSheet("")
                              self.A2.setText(Space + tt)
                              found = True
                         elif i!=1 and not found:
                              self.L22.setStyleSheet("background-color: yellow;")
            if num == 23:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==2 and found == False:
                              self.L23.setStyleSheet("background-color: green;")
                              self.A3.setStyleSheet("")
                              self.A3.setText(Space + tt)
                              found = True
                         elif i!=2 and not found:
                              self.L23.setStyleSheet("background-color: yellow;")
            if num == 24:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==3 and found == False:
                              self.L24.setStyleSheet("background-color: green;")
                              self.A4.setStyleSheet("")
                              self.A4.setText(Space + tt)
                              found = True
                         elif i!=3 and not found:
                              self.L24.setStyleSheet("background-color: yellow;")
            if num == 25:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==4 and found == False:
                              self.L25.setStyleSheet("background-color: green;")
                              self.A5.setStyleSheet("")
                              self.A5.setText(Space + tt)
                              found = True
                         elif i!=4 and not found:
                              self.L25.setStyleSheet("background-color: yellow;")
            if num == 31:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==0 and found == False:
                              self.L31.setStyleSheet("background-color: green;")
                              self.A1.setStyleSheet("")
                              self.A1.setText(Space + tt)
                              found = True
                         elif i!=0 and not found:
                              self.L31.setStyleSheet("background-color: yellow;")
            if num == 32:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==1 and found == False:
                              self.L32.setStyleSheet("background-color: green;")
                              self.A2.setStyleSheet("")
                              self.A2.setText(Space + tt)
                              found = True
                         elif i!=1 and not found:
                              self.L32.setStyleSheet("background-color: yellow;")
            if num == 33:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==2 and found == False:
                              self.L33.setStyleSheet("background-color: green;")
                              self.A3.setStyleSheet("")
                              self.A3.setText(Space + tt)
                              found = True
                         elif i!=2 and not found:
                              self.L33.setStyleSheet("background-color: yellow;")
            if num == 34:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==3 and found == False:
                              self.L34.setStyleSheet("background-color: green;")
                              self.A4.setStyleSheet("")
                              self.A4.setText(Space + tt)
                              found = True
                         elif i!=3 and not found:
                              self.L34.setStyleSheet("background-color: yellow;")
            if num == 35:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==4 and found == False:
                              self.L35.setStyleSheet("background-color: green;")
                              self.A5.setStyleSheet("")
                              self.A5.setText(Space + tt)
                              found = True
                         elif i!=4 and not found:
                              self.L35.setStyleSheet("background-color: yellow;")
            if num == 41:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==0 and found == False:
                              self.L41.setStyleSheet("background-color: green;")
                              self.A1.setStyleSheet("")
                              self.A1.setText(Space + tt)
                              found = True
                         elif i!=0 and not found:
                              self.L41.setStyleSheet("background-color: yellow;")
            if num == 42:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==1 and found == False:
                              self.L42.setStyleSheet("background-color: green;")
                              self.A2.setStyleSheet("")
                              self.A2.setText(Space + tt)
                              found = True
                         elif i!=1 and not found:
                              self.L42.setStyleSheet("background-color: yellow;")
            if num == 43:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==2 and found == False:
                              self.L43.setStyleSheet("background-color: green;")
                              self.A3.setStyleSheet("")
                              self.A3.setText(Space + tt)
                              found = True
                         elif i!=2 and not found:
                              self.L43.setStyleSheet("background-color: yellow;")
            if num == 44:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==3 and found == False:
                              self.L44.setStyleSheet("background-color: green;")
                              self.A4.setStyleSheet("")
                              self.A4.setText(Space + tt)
                              found = True
                         elif i!=3 and not found:
                              self.L44.setStyleSheet("background-color: yellow;")
            if num == 45:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==4 and found == False:
                              self.L45.setStyleSheet("background-color: green;")
                              self.A5.setStyleSheet("")
                              self.A5.setText(Space + tt)
                              found = True
                         elif i!=4 and not found:
                              self.L45.setStyleSheet("background-color: yellow;")
            if num == 51:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==0 and found == False:
                              self.L51.setStyleSheet("background-color: green;")
                              self.A1.setStyleSheet("")
                              self.A1.setText(Space + tt)
                              found = True
                         elif i!=0 and not found:
                              self.L51.setStyleSheet("background-color: yellow;")
            if num == 52:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==1 and found == False:
                              self.L52.setStyleSheet("background-color: green;")
                              self.A2.setStyleSheet("")
                              self.A2.setText(Space + tt)
                              found = True
                         elif i!=1 and not found:
                              self.L52.setStyleSheet("background-color: yellow;")
            if num == 53:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==2 and found == False:
                              self.L53.setStyleSheet("background-color: green;")
                              self.A3.setStyleSheet("")
                              self.A3.setText(Space + tt)
                              found = True
                         elif i!=2 and not found:
                              self.L53.setStyleSheet("background-color: yellow;")
            if num == 54:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==3 and found == False:
                              self.L54.setStyleSheet("background-color: green;")
                              self.A4.setStyleSheet("")
                              self.A4.setText(Space + tt)
                              found = True
                         elif i!=3 and not found:
                              self.L54.setStyleSheet("background-color: yellow;")
            if num == 55:
                found = False
                for i in range (0,5):
                     if self.currentAnswer[i] == tt:
                         #print("Буква " + self.currentAnswer[i] + " соответствует букве из " + str(i) + " колонки")
                         if i==4 and found == False:
                              self.L55.setStyleSheet("background-color: green;")
                              self.A5.setStyleSheet("")
                              self.A5.setText(Space + tt)
                              found = True
                         elif i!=4 and not found:
                              self.L55.setStyleSheet("background-color: yellow;")
        
        def ButtonClicked(letter):
            Space = " "*3
            if self.lineSelector == 0:
                if self.L11.text() == "":
                    self.L11.setText(Space + letter)
                    check = True
                elif  self.L12.text() == "":
                    self.L12.setText(Space + letter)
                elif  self.L13.text() == "":
                    self.L13.setText(Space + letter)
                elif  self.L14.text() == "":
                    self.L14.setText(Space + letter)
                elif  self.L15.text() == "":
                    self.L15.setText(Space + letter)
                    ProgressGame(11,self.L11.text())
                    ProgressGame(12,self.L12.text())
                    ProgressGame(13,self.L13.text())
                    ProgressGame(14,self.L14.text())
                    ProgressGame(15,self.L15.text()) 
                    self.lineSelector += 1
                
            elif self.lineSelector == 1:
                if self.L21.text() == "":
                    self.L21.setText(Space + letter)
                elif  self.L22.text() == "":
                    self.L22.setText(Space + letter)
                elif  self.L23.text() == "":
                    self.L23.setText(Space + letter)
                elif  self.L24.text() == "":
                    self.L24.setText(Space + letter)
                elif  self.L25.text() == "":
                    self.L25.setText(Space + letter)
                    ProgressGame(21,self.L21.text())
                    ProgressGame(22,self.L22.text())
                    ProgressGame(23,self.L23.text())
                    ProgressGame(24,self.L24.text())
                    ProgressGame(25,self.L25.text())
                    self.lineSelector += 1
                    
            elif self.lineSelector == 2:
                if self.L31.text() == "":
                    self.L31.setText(Space + letter)
                elif  self.L32.text() == "":
                    self.L32.setText(Space + letter)
                elif  self.L33.text() == "":
                    self.L33.setText(Space + letter)
                elif  self.L34.text() == "":
                    self.L34.setText(Space + letter)
                elif  self.L35.text() == "":
                    self.L35.setText(Space + letter)
                    ProgressGame(31,self.L31.text())
                    ProgressGame(32,self.L32.text())
                    ProgressGame(33,self.L33.text())
                    ProgressGame(34,self.L34.text())
                    ProgressGame(35,self.L35.text())
                    self.lineSelector += 1
                
            elif self.lineSelector == 3:
                if self.L41.text() == "":
                    self.L41.setText(Space + letter)
                elif  self.L42.text() == "":
                    self.L42.setText(Space + letter)
                elif  self.L43.text() == "":
                    self.L43.setText(Space + letter)
                elif  self.L44.text() == "":
                    self.L44.setText(Space + letter)
                elif  self.L45.text() == "":
                    self.L45.setText(Space + letter)
                    ProgressGame(41,self.L41.text())
                    ProgressGame(42,self.L42.text())
                    ProgressGame(43,self.L43.text())
                    ProgressGame(44,self.L44.text())
                    ProgressGame(45,self.L45.text())
                    self.lineSelector += 1
                    
            elif self.lineSelector == 4:
                if self.L51.text() == "":
                    self.L51.setText(Space + letter)
                elif  self.L52.text() == "":
                    self.L52.setText(Space + letter)
                elif  self.L53.text() == "":
                    self.L53.setText(Space + letter)
                elif  self.L54.text() == "":
                    self.L54.setText(Space + letter)
                elif  self.L55.text() == "":
                    self.L55.setText(Space + letter)
                    ProgressGame(51,self.L51.text())
                    ProgressGame(52,self.L52.text())
                    ProgressGame(53,self.L53.text())
                    ProgressGame(54,self.L54.text())
                    ProgressGame(55,self.L55.text())
                    result()
                
        def result():
            Space = " "*3    
            self.A1.setStyleSheet("")
            self.A2.setStyleSheet("")
            self.A3.setStyleSheet("")
            self.A4.setStyleSheet("")
            self.A5.setStyleSheet("")
            self.A1.setText(Space + self.currentAnswer[0])
            self.A2.setText(Space + self.currentAnswer[1])
            self.A3.setText(Space + self.currentAnswer[2])
            self.A4.setText(Space + self.currentAnswer[3])
            self.A5.setText(Space + self.currentAnswer[4])
                
            
        self.But1.clicked.connect(lambda: ButtonClicked("й"))
        self.But2.clicked.connect(lambda: ButtonClicked("ц"))
        self.But3.clicked.connect(lambda: ButtonClicked("у"))
        self.But4.clicked.connect(lambda: ButtonClicked("к"))
        self.But5.clicked.connect(lambda: ButtonClicked("е"))
        self.But6.clicked.connect(lambda: ButtonClicked("н"))
        self.But7.clicked.connect(lambda: ButtonClicked("г"))
        self.But8.clicked.connect(lambda: ButtonClicked("ш"))
        self.But9.clicked.connect(lambda: ButtonClicked("щ"))
        self.But10.clicked.connect(lambda: ButtonClicked("з"))
        self.But11.clicked.connect(lambda: ButtonClicked("х"))
        self.But12.clicked.connect(lambda: ButtonClicked("ъ"))
        self.But13.clicked.connect(lambda: ButtonClicked("ф"))
        self.But14.clicked.connect(lambda: ButtonClicked("ы"))
        self.But15.clicked.connect(lambda: ButtonClicked("в"))
        self.But16.clicked.connect(lambda: ButtonClicked("а"))
        self.But17.clicked.connect(lambda: ButtonClicked("п"))
        self.But18.clicked.connect(lambda: ButtonClicked("р"))
        self.But19.clicked.connect(lambda: ButtonClicked("о"))
        self.But20.clicked.connect(lambda: ButtonClicked("л"))
        self.But21.clicked.connect(lambda: ButtonClicked("д"))
        self.But22.clicked.connect(lambda: ButtonClicked("ж"))
        self.But23.clicked.connect(lambda: ButtonClicked("э"))
        self.But24.clicked.connect(lambda: ButtonClicked("я"))
        self.But25.clicked.connect(lambda: ButtonClicked("ч"))
        self.But26.clicked.connect(lambda: ButtonClicked("с"))
        self.But27.clicked.connect(lambda: ButtonClicked("м"))
        self.But28.clicked.connect(lambda: ButtonClicked("и"))
        self.But29.clicked.connect(lambda: ButtonClicked("т"))
        self.But30.clicked.connect(lambda: ButtonClicked("ь"))
        self.But31.clicked.connect(lambda: ButtonClicked("б"))
        self.But32.clicked.connect(lambda: ButtonClicked("ю"))

        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Word Game (RUS)"))
        self.But14.setText(_translate("MainWindow", "Ы"))
        self.But18.setText(_translate("MainWindow", "Р"))
        self.But17.setText(_translate("MainWindow", "П"))
        self.But16.setText(_translate("MainWindow", "А"))
        self.But19.setText(_translate("MainWindow", "О"))
        self.But1.setText(_translate("MainWindow", "Й"))
        self.But10.setText(_translate("MainWindow", "З"))
        self.But11.setText(_translate("MainWindow", "Х"))
        self.But12.setText(_translate("MainWindow", "Ъ"))
        self.But7.setText(_translate("MainWindow", "Г"))
        self.But6.setText(_translate("MainWindow", "Н"))
        self.But5.setText(_translate("MainWindow", "Е"))
        self.But2.setText(_translate("MainWindow", "Ц"))
        self.But4.setText(_translate("MainWindow", "К"))
        self.But3.setText(_translate("MainWindow", "У"))
        self.But13.setText(_translate("MainWindow", "Ф"))
        self.But15.setText(_translate("MainWindow", "В"))
        self.But9.setText(_translate("MainWindow", "Щ"))
        self.But8.setText(_translate("MainWindow", "Ш"))
        self.But22.setText(_translate("MainWindow", "Ж"))
        self.But20.setText(_translate("MainWindow", "Л"))
        self.But23.setText(_translate("MainWindow", "Э"))
        self.But21.setText(_translate("MainWindow", "Д"))
        self.But32.setText(_translate("MainWindow", "Ю"))
        self.But31.setText(_translate("MainWindow", "Б"))
        self.But30.setText(_translate("MainWindow", "Ь"))
        self.But29.setText(_translate("MainWindow", "Т"))
        self.But28.setText(_translate("MainWindow", "И"))
        self.But27.setText(_translate("MainWindow", "М"))
        self.But26.setText(_translate("MainWindow", "С"))
        self.But25.setText(_translate("MainWindow", "Ч"))
        self.But24.setText(_translate("MainWindow", "Я"))
        
    def SetAnswer(self,answ):
        self.currentAnswer = answ
        self.lineSelector = 0


while(True):
    print("Введите слово из 5 букв")
    a = input()
    #a = "абвгд"
    if len(a) == 5:
        break
    else:
        print("Ошибка, повторите снова!")
        
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.SetAnswer(a)
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())
