# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataMarker(object):
    def setupUi(self, DataMarker):
        DataMarker.setObjectName("DataMarker")
        DataMarker.resize(866, 557)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DataMarker.sizePolicy().hasHeightForWidth())
        DataMarker.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        DataMarker.setFont(font)
        DataMarker.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(DataMarker)
        self.gridLayout.setObjectName("gridLayout")
        self.ShowWidget = QtWidgets.QWidget(DataMarker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.ShowWidget.sizePolicy().hasHeightForWidth())
        self.ShowWidget.setSizePolicy(sizePolicy)
        self.ShowWidget.setObjectName("ShowWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ShowWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.VideoWidget = QtWidgets.QWidget(self.ShowWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoWidget.sizePolicy().hasHeightForWidth())
        self.VideoWidget.setSizePolicy(sizePolicy)
        self.VideoWidget.setStyleSheet("")
        self.VideoWidget.setObjectName("VideoWidget")
        self.horizontalLayout.addWidget(self.VideoWidget)
        self.GraphWidget = QtWidgets.QWidget(self.ShowWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GraphWidget.sizePolicy().hasHeightForWidth())
        self.GraphWidget.setSizePolicy(sizePolicy)
        self.GraphWidget.setStyleSheet("")
        self.GraphWidget.setObjectName("GraphWidget")
        self.horizontalLayout.addWidget(self.GraphWidget)
        self.gridLayout.addWidget(self.ShowWidget, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(DataMarker)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.InputWidget = QtWidgets.QWidget(DataMarker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.InputWidget.sizePolicy().hasHeightForWidth())
        self.InputWidget.setSizePolicy(sizePolicy)
        self.InputWidget.setObjectName("InputWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.InputWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SetWidget = QtWidgets.QWidget(self.InputWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.SetWidget.sizePolicy().hasHeightForWidth())
        self.SetWidget.setSizePolicy(sizePolicy)
        self.SetWidget.setObjectName("SetWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.SetWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.VideoSetWidget = QtWidgets.QWidget(self.SetWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.VideoSetWidget.setFont(font)
        self.VideoSetWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.VideoSetWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.VideoSetWidget.setStyleSheet("")
        self.VideoSetWidget.setObjectName("VideoSetWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.VideoSetWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.VideoSetLabel = QtWidgets.QLabel(self.VideoSetWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoSetLabel.sizePolicy().hasHeightForWidth())
        self.VideoSetLabel.setSizePolicy(sizePolicy)
        self.VideoSetLabel.setObjectName("VideoSetLabel")
        self.verticalLayout_3.addWidget(self.VideoSetLabel)
        self.widget_2 = QtWidgets.QWidget(self.VideoSetWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.widget_2.setFont(font)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setContentsMargins(0, 9, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.PlayButton = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlayButton.sizePolicy().hasHeightForWidth())
        self.PlayButton.setSizePolicy(sizePolicy)
        self.PlayButton.setObjectName("PlayButton")
        self.horizontalLayout_6.addWidget(self.PlayButton)
        self.StopButton = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StopButton.sizePolicy().hasHeightForWidth())
        self.StopButton.setSizePolicy(sizePolicy)
        self.StopButton.setObjectName("StopButton")
        self.horizontalLayout_6.addWidget(self.StopButton)
        self.horizontalLayout_5.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.StepSpinBox = QtWidgets.QSpinBox(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StepSpinBox.sizePolicy().hasHeightForWidth())
        self.StepSpinBox.setSizePolicy(sizePolicy)
        self.StepSpinBox.setMinimum(30)
        self.StepSpinBox.setMaximum(200000000)
        self.StepSpinBox.setSingleStep(10)
        self.StepSpinBox.setProperty("value", 30)
        self.StepSpinBox.setObjectName("StepSpinBox")
        self.verticalLayout_4.addWidget(self.StepSpinBox)
        self.horizontalLayout_5.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.TimeSpinBox = QtWidgets.QSpinBox(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TimeSpinBox.sizePolicy().hasHeightForWidth())
        self.TimeSpinBox.setSizePolicy(sizePolicy)
        self.TimeSpinBox.setMaximum(200000000)
        self.TimeSpinBox.setSingleStep(30)
        self.TimeSpinBox.setProperty("value", 0)
        self.TimeSpinBox.setObjectName("TimeSpinBox")
        self.verticalLayout_5.addWidget(self.TimeSpinBox)
        self.horizontalLayout_5.addWidget(self.widget_5)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.horizontalLayout_2.addWidget(self.VideoSetWidget)
        self.GraphSetWidget = QtWidgets.QWidget(self.SetWidget)
        self.GraphSetWidget.setStyleSheet("")
        self.GraphSetWidget.setObjectName("GraphSetWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.GraphSetWidget)
        self.verticalLayout_6.setContentsMargins(9, -1, 9, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.GraphSetWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.widget_6 = QtWidgets.QWidget(self.GraphSetWidget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setContentsMargins(0, 9, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_7 = QtWidgets.QWidget(self.widget_6)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ApplyButton = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ApplyButton.sizePolicy().hasHeightForWidth())
        self.ApplyButton.setSizePolicy(sizePolicy)
        self.ApplyButton.setObjectName("ApplyButton")
        self.horizontalLayout_8.addWidget(self.ApplyButton)
        self.horizontalLayout_7.addWidget(self.widget_7)
        self.widget_10 = QtWidgets.QWidget(self.widget_6)
        self.widget_10.setObjectName("widget_10")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_10)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.DataTypeLabel = QtWidgets.QLabel(self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DataTypeLabel.sizePolicy().hasHeightForWidth())
        self.DataTypeLabel.setSizePolicy(sizePolicy)
        self.DataTypeLabel.setObjectName("DataTypeLabel")
        self.gridLayout_2.addWidget(self.DataTypeLabel, 0, 0, 1, 1)
        self.AcceRadio = QtWidgets.QRadioButton(self.widget_10)
        self.AcceRadio.setChecked(True)
        self.AcceRadio.setObjectName("AcceRadio")
        self.gridLayout_2.addWidget(self.AcceRadio, 0, 1, 1, 1)
        self.GyroRadio = QtWidgets.QRadioButton(self.widget_10)
        self.GyroRadio.setObjectName("GyroRadio")
        self.gridLayout_2.addWidget(self.GyroRadio, 1, 1, 1, 1)
        self.RotateRadio = QtWidgets.QRadioButton(self.widget_10)
        self.RotateRadio.setObjectName("RotateRadio")
        self.gridLayout_2.addWidget(self.RotateRadio, 1, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.widget_10)
        self.widget_9 = QtWidgets.QWidget(self.widget_6)
        self.widget_9.setObjectName("widget_9")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_9)
        self.gridLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.DataTypeLabel_2 = QtWidgets.QLabel(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DataTypeLabel_2.sizePolicy().hasHeightForWidth())
        self.DataTypeLabel_2.setSizePolicy(sizePolicy)
        self.DataTypeLabel_2.setObjectName("DataTypeLabel_2")
        self.gridLayout_3.addWidget(self.DataTypeLabel_2, 0, 0, 1, 1)
        self.XCheck = QtWidgets.QCheckBox(self.widget_9)
        self.XCheck.setChecked(True)
        self.XCheck.setObjectName("XCheck")
        self.gridLayout_3.addWidget(self.XCheck, 0, 1, 1, 1)
        self.YCheck = QtWidgets.QCheckBox(self.widget_9)
        self.YCheck.setChecked(True)
        self.YCheck.setObjectName("YCheck")
        self.gridLayout_3.addWidget(self.YCheck, 1, 0, 1, 1)
        self.ZCheck = QtWidgets.QCheckBox(self.widget_9)
        self.ZCheck.setChecked(True)
        self.ZCheck.setObjectName("ZCheck")
        self.gridLayout_3.addWidget(self.ZCheck, 1, 1, 1, 1)
        self.horizontalLayout_7.addWidget(self.widget_9)
        self.widget_8 = QtWidgets.QWidget(self.widget_6)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.RangeSpinBox = QtWidgets.QSpinBox(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RangeSpinBox.sizePolicy().hasHeightForWidth())
        self.RangeSpinBox.setSizePolicy(sizePolicy)
        self.RangeSpinBox.setMinimum(1000)
        self.RangeSpinBox.setMaximum(100000)
        self.RangeSpinBox.setSingleStep(1000)
        self.RangeSpinBox.setProperty("value", 1000)
        self.RangeSpinBox.setObjectName("RangeSpinBox")
        self.verticalLayout_7.addWidget(self.RangeSpinBox)
        self.horizontalLayout_7.addWidget(self.widget_8)
        self.verticalLayout_6.addWidget(self.widget_6)
        self.horizontalLayout_2.addWidget(self.GraphSetWidget)
        self.verticalLayout.addWidget(self.SetWidget)
        self.TagWidget = QtWidgets.QWidget(self.InputWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.TagWidget.sizePolicy().hasHeightForWidth())
        self.TagWidget.setSizePolicy(sizePolicy)
        self.TagWidget.setObjectName("TagWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.TagWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.TagFolderWidget = QtWidgets.QWidget(self.TagWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TagFolderWidget.sizePolicy().hasHeightForWidth())
        self.TagFolderWidget.setSizePolicy(sizePolicy)
        self.TagFolderWidget.setStyleSheet("")
        self.TagFolderWidget.setObjectName("TagFolderWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.TagFolderWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TagFolderLabel = QtWidgets.QLabel(self.TagFolderWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TagFolderLabel.sizePolicy().hasHeightForWidth())
        self.TagFolderLabel.setSizePolicy(sizePolicy)
        self.TagFolderLabel.setObjectName("TagFolderLabel")
        self.verticalLayout_2.addWidget(self.TagFolderLabel)
        self.widget_21 = QtWidgets.QWidget(self.TagFolderWidget)
        self.widget_21.setObjectName("widget_21")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_21)
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.widget = QtWidgets.QWidget(self.widget_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 9, 0, 9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.SelectFolderButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SelectFolderButton.sizePolicy().hasHeightForWidth())
        self.SelectFolderButton.setSizePolicy(sizePolicy)
        self.SelectFolderButton.setObjectName("SelectFolderButton")
        self.horizontalLayout_4.addWidget(self.SelectFolderButton)
        self.TagStartButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TagStartButton.sizePolicy().hasHeightForWidth())
        self.TagStartButton.setSizePolicy(sizePolicy)
        self.TagStartButton.setObjectName("TagStartButton")
        self.horizontalLayout_4.addWidget(self.TagStartButton)
        self.verticalLayout_12.addWidget(self.widget)
        self.TagFolderLineEdit = QtWidgets.QLineEdit(self.widget_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.TagFolderLineEdit.sizePolicy().hasHeightForWidth())
        self.TagFolderLineEdit.setSizePolicy(sizePolicy)
        self.TagFolderLineEdit.setReadOnly(True)
        self.TagFolderLineEdit.setObjectName("TagFolderLineEdit")
        self.verticalLayout_12.addWidget(self.TagFolderLineEdit)
        self.verticalLayout_2.addWidget(self.widget_21)
        self.horizontalLayout_3.addWidget(self.TagFolderWidget)
        self.TagSetWidget = QtWidgets.QWidget(self.TagWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TagSetWidget.sizePolicy().hasHeightForWidth())
        self.TagSetWidget.setSizePolicy(sizePolicy)
        self.TagSetWidget.setStyleSheet("")
        self.TagSetWidget.setObjectName("TagSetWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.TagSetWidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.TagSetLabel = QtWidgets.QLabel(self.TagSetWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TagSetLabel.sizePolicy().hasHeightForWidth())
        self.TagSetLabel.setSizePolicy(sizePolicy)
        self.TagSetLabel.setObjectName("TagSetLabel")
        self.verticalLayout_8.addWidget(self.TagSetLabel)
        self.widget_11 = QtWidgets.QWidget(self.TagSetWidget)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.widget_12 = QtWidgets.QWidget(self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy)
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_12)
        self.verticalLayout_9.setContentsMargins(9, 0, 9, 0)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_16 = QtWidgets.QWidget(self.widget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy)
        self.widget_16.setObjectName("widget_16")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_16)
        self.horizontalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.SaveButton = QtWidgets.QPushButton(self.widget_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveButton.sizePolicy().hasHeightForWidth())
        self.SaveButton.setSizePolicy(sizePolicy)
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalLayout_10.addWidget(self.SaveButton)
        self.CancelButton = QtWidgets.QPushButton(self.widget_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CancelButton.sizePolicy().hasHeightForWidth())
        self.CancelButton.setSizePolicy(sizePolicy)
        self.CancelButton.setObjectName("CancelButton")
        self.horizontalLayout_10.addWidget(self.CancelButton)
        self.verticalLayout_9.addWidget(self.widget_16)
        self.SaveLineEdit = QtWidgets.QLineEdit(self.widget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.SaveLineEdit.sizePolicy().hasHeightForWidth())
        self.SaveLineEdit.setSizePolicy(sizePolicy)
        self.SaveLineEdit.setReadOnly(True)
        self.SaveLineEdit.setObjectName("SaveLineEdit")
        self.verticalLayout_9.addWidget(self.SaveLineEdit)
        self.horizontalLayout_9.addWidget(self.widget_12)
        self.widget_15 = QtWidgets.QWidget(self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy)
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_15)
        self.verticalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_5 = QtWidgets.QLabel(self.widget_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_10.addWidget(self.label_5)
        self.widget_22 = QtWidgets.QWidget(self.widget_15)
        self.widget_22.setObjectName("widget_22")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_22)
        self.gridLayout_4.setContentsMargins(9, 0, 9, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.XLineEdit = QtWidgets.QLineEdit(self.widget_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.XLineEdit.sizePolicy().hasHeightForWidth())
        self.XLineEdit.setSizePolicy(sizePolicy)
        self.XLineEdit.setObjectName("XLineEdit")
        self.gridLayout_4.addWidget(self.XLineEdit, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1)
        self.YLineEdit = QtWidgets.QLineEdit(self.widget_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.YLineEdit.sizePolicy().hasHeightForWidth())
        self.YLineEdit.setSizePolicy(sizePolicy)
        self.YLineEdit.setObjectName("YLineEdit")
        self.gridLayout_4.addWidget(self.YLineEdit, 1, 1, 1, 1)
        self.verticalLayout_10.addWidget(self.widget_22)
        self.horizontalLayout_9.addWidget(self.widget_15)
        self.widget_13 = QtWidgets.QWidget(self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy)
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.widget_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_11.addWidget(self.label_8)
        self.widget_17 = QtWidgets.QWidget(self.widget_13)
        self.widget_17.setObjectName("widget_17")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_17)
        self.gridLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_9 = QtWidgets.QLabel(self.widget_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)
        self.TypeComboBox = QtWidgets.QComboBox(self.widget_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TypeComboBox.sizePolicy().hasHeightForWidth())
        self.TypeComboBox.setSizePolicy(sizePolicy)
        self.TypeComboBox.setObjectName("TypeComboBox")
        self.gridLayout_5.addWidget(self.TypeComboBox, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 1, 0, 1, 1)
        self.EvalComboBox = QtWidgets.QComboBox(self.widget_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EvalComboBox.sizePolicy().hasHeightForWidth())
        self.EvalComboBox.setSizePolicy(sizePolicy)
        self.EvalComboBox.setObjectName("EvalComboBox")
        self.gridLayout_5.addWidget(self.EvalComboBox, 1, 1, 1, 1)
        self.verticalLayout_11.addWidget(self.widget_17)
        self.horizontalLayout_9.addWidget(self.widget_13)
        self.widget_14 = QtWidgets.QWidget(self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy)
        self.widget_14.setObjectName("widget_14")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_14)
        self.verticalLayout_13.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_11 = QtWidgets.QLabel(self.widget_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_13.addWidget(self.label_11)
        self.widget_18 = QtWidgets.QWidget(self.widget_14)
        self.widget_18.setObjectName("widget_18")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_18)
        self.gridLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.StartLineEdit = QtWidgets.QLineEdit(self.widget_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartLineEdit.sizePolicy().hasHeightForWidth())
        self.StartLineEdit.setSizePolicy(sizePolicy)
        self.StartLineEdit.setReadOnly(True)
        self.StartLineEdit.setObjectName("StartLineEdit")
        self.gridLayout_6.addWidget(self.StartLineEdit, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 1, 0, 1, 1)
        self.EndLineEdit = QtWidgets.QLineEdit(self.widget_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EndLineEdit.sizePolicy().hasHeightForWidth())
        self.EndLineEdit.setSizePolicy(sizePolicy)
        self.EndLineEdit.setReadOnly(True)
        self.EndLineEdit.setObjectName("EndLineEdit")
        self.gridLayout_6.addWidget(self.EndLineEdit, 1, 1, 1, 1)
        self.verticalLayout_13.addWidget(self.widget_18)
        self.horizontalLayout_9.addWidget(self.widget_14)
        self.verticalLayout_8.addWidget(self.widget_11)
        self.horizontalLayout_3.addWidget(self.TagSetWidget)
        self.verticalLayout.addWidget(self.TagWidget)
        self.gridLayout.addWidget(self.InputWidget, 3, 0, 1, 1)

        self.retranslateUi(DataMarker)
        QtCore.QMetaObject.connectSlotsByName(DataMarker)

    def retranslateUi(self, DataMarker):
        _translate = QtCore.QCoreApplication.translate
        DataMarker.setWindowTitle(_translate("DataMarker", "DataMarker"))
        self.VideoSetLabel.setText(_translate("DataMarker", " Video Setting"))
        self.PlayButton.setText(_translate("DataMarker", "Play"))
        self.StopButton.setText(_translate("DataMarker", "Stop"))
        self.label.setText(_translate("DataMarker", "Step (ms)"))
        self.label_2.setText(_translate("DataMarker", "Time (ms)"))
        self.label_3.setText(_translate("DataMarker", " Graph Setting"))
        self.ApplyButton.setText(_translate("DataMarker", "Apply"))
        self.DataTypeLabel.setText(_translate("DataMarker", "Data Type"))
        self.AcceRadio.setText(_translate("DataMarker", "Acce"))
        self.GyroRadio.setText(_translate("DataMarker", "Gyro"))
        self.RotateRadio.setText(_translate("DataMarker", "Rotate"))
        self.DataTypeLabel_2.setText(_translate("DataMarker", "Axis"))
        self.XCheck.setText(_translate("DataMarker", "X"))
        self.YCheck.setText(_translate("DataMarker", "Y"))
        self.ZCheck.setText(_translate("DataMarker", "Z"))
        self.label_4.setText(_translate("DataMarker", "Range (ms)"))
        self.TagFolderLabel.setText(_translate("DataMarker", " Select Folder"))
        self.SelectFolderButton.setText(_translate("DataMarker", "Select"))
        self.TagStartButton.setText(_translate("DataMarker", "Start"))
        self.TagSetLabel.setText(_translate("DataMarker", " Tag Setting"))
        self.SaveButton.setText(_translate("DataMarker", "Save"))
        self.CancelButton.setText(_translate("DataMarker", "Cancel"))
        self.label_5.setText(_translate("DataMarker", "Position"))
        self.label_6.setText(_translate("DataMarker", "X:"))
        self.label_7.setText(_translate("DataMarker", "Y:"))
        self.label_8.setText(_translate("DataMarker", "Action"))
        self.label_9.setText(_translate("DataMarker", "Type:"))
        self.label_10.setText(_translate("DataMarker", "Eval:"))
        self.label_11.setText(_translate("DataMarker", "Section (ms)"))
        self.label_12.setText(_translate("DataMarker", "Start:"))
        self.label_13.setText(_translate("DataMarker", "End:"))
