# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/crantila/Documents/ELVIS/programs/vis/qt/new_main_window.ui'
#
# Created: Mon Sep  3 23:29:25 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.function_menu = QtGui.QWidget(self.centralwidget)
        self.function_menu.setObjectName(_fromUtf8("function_menu"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.function_menu)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_analyze = QtGui.QToolButton(self.function_menu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/analyze.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_analyze.setIcon(icon)
        self.btn_analyze.setIconSize(QtCore.QSize(64, 64))
        self.btn_analyze.setCheckable(True)
        self.btn_analyze.setChecked(True)
        self.btn_analyze.setAutoExclusive(True)
        self.btn_analyze.setAutoRaise(True)
        self.btn_analyze.setObjectName(_fromUtf8("btn_analyze"))
        self.horizontalLayout.addWidget(self.btn_analyze)
        self.btn_show = QtGui.QToolButton(self.function_menu)
        self.btn_show.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/show_results.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_show.setIcon(icon1)
        self.btn_show.setIconSize(QtCore.QSize(64, 64))
        self.btn_show.setCheckable(True)
        self.btn_show.setAutoExclusive(True)
        self.btn_show.setAutoRaise(True)
        self.btn_show.setObjectName(_fromUtf8("btn_show"))
        self.horizontalLayout.addWidget(self.btn_show)
        self.btn_settings = QtGui.QToolButton(self.function_menu)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_settings.setIcon(icon2)
        self.btn_settings.setIconSize(QtCore.QSize(64, 64))
        self.btn_settings.setCheckable(True)
        self.btn_settings.setAutoExclusive(True)
        self.btn_settings.setAutoRaise(True)
        self.btn_settings.setObjectName(_fromUtf8("btn_settings"))
        self.horizontalLayout.addWidget(self.btn_settings)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_about = QtGui.QToolButton(self.function_menu)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/help-about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_about.setIcon(icon3)
        self.btn_about.setIconSize(QtCore.QSize(64, 64))
        self.btn_about.setCheckable(True)
        self.btn_about.setAutoExclusive(True)
        self.btn_about.setAutoRaise(True)
        self.btn_about.setObjectName(_fromUtf8("btn_about"))
        self.horizontalLayout.addWidget(self.btn_about)
        self.verticalLayout.addWidget(self.function_menu)
        self.main_screen = QtGui.QStackedWidget(self.centralwidget)
        self.main_screen.setObjectName(_fromUtf8("main_screen"))
        self.page_analyze = QtGui.QWidget()
        self.page_analyze.setObjectName(_fromUtf8("page_analyze"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page_analyze)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.page_analyze)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.widget_3 = QtGui.QWidget(self.groupBox)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.widget_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.btn_file_add = QtGui.QPushButton(self.widget_4)
        self.btn_file_add.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/list-add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_file_add.setIcon(icon4)
        self.btn_file_add.setIconSize(QtCore.QSize(22, 22))
        self.btn_file_add.setFlat(True)
        self.btn_file_add.setObjectName(_fromUtf8("btn_file_add"))
        self.horizontalLayout_4.addWidget(self.btn_file_add)
        self.btn_file_remove = QtGui.QPushButton(self.widget_4)
        self.btn_file_remove.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/list-remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_file_remove.setIcon(icon5)
        self.btn_file_remove.setIconSize(QtCore.QSize(22, 22))
        self.btn_file_remove.setFlat(True)
        self.btn_file_remove.setObjectName(_fromUtf8("btn_file_remove"))
        self.horizontalLayout_4.addWidget(self.btn_file_remove)
        self.verticalLayout_7.addWidget(self.widget_4)
        self.txt_file_list = QtGui.QPlainTextEdit(self.widget_3)
        self.txt_file_list.setObjectName(_fromUtf8("txt_file_list"))
        self.verticalLayout_7.addWidget(self.txt_file_list)
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.widget_2 = QtGui.QWidget(self.groupBox)
        self.widget_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.label_4 = QtGui.QLabel(self.widget_2)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_8.addWidget(self.label_4)
        self.line_files_n = QtGui.QLineEdit(self.widget_2)
        self.line_files_n.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.line_files_n.setObjectName(_fromUtf8("line_files_n"))
        self.verticalLayout_8.addWidget(self.line_files_n)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem3)
        self.btn_files_analyze = QtGui.QPushButton(self.widget_2)
        self.btn_files_analyze.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/start-analysis.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_files_analyze.setIcon(icon6)
        self.btn_files_analyze.setIconSize(QtCore.QSize(32, 32))
        self.btn_files_analyze.setObjectName(_fromUtf8("btn_files_analyze"))
        self.verticalLayout_8.addWidget(self.btn_files_analyze)
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.main_screen.addWidget(self.page_analyze)
        self.page_show = QtGui.QWidget()
        self.page_show.setObjectName(_fromUtf8("page_show"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page_show)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.page_show)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.rdo_chart = QtGui.QRadioButton(self.groupBox_5)
        self.rdo_chart.setChecked(True)
        self.rdo_chart.setObjectName(_fromUtf8("rdo_chart"))
        self.verticalLayout_9.addWidget(self.rdo_chart)
        self.rdo_score = QtGui.QRadioButton(self.groupBox_5)
        self.rdo_score.setObjectName(_fromUtf8("rdo_score"))
        self.verticalLayout_9.addWidget(self.rdo_score)
        self.rdo_targeted_score = QtGui.QRadioButton(self.groupBox_5)
        self.rdo_targeted_score.setObjectName(_fromUtf8("rdo_targeted_score"))
        self.verticalLayout_9.addWidget(self.rdo_targeted_score)
        self.rdo_list = QtGui.QRadioButton(self.groupBox_5)
        self.rdo_list.setObjectName(_fromUtf8("rdo_list"))
        self.verticalLayout_9.addWidget(self.rdo_list)
        self.gridLayout.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.groupBox_n = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_n.setObjectName(_fromUtf8("groupBox_n"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.groupBox_n)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_n)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_12.addWidget(self.lineEdit)
        self.gridLayout.addWidget(self.groupBox_n, 0, 3, 1, 1)
        self.groupBox_sorted_by = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_sorted_by.setObjectName(_fromUtf8("groupBox_sorted_by"))
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.groupBox_sorted_by)
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.rdo_frequency = QtGui.QRadioButton(self.groupBox_sorted_by)
        self.rdo_frequency.setChecked(True)
        self.rdo_frequency.setObjectName(_fromUtf8("rdo_frequency"))
        self.verticalLayout_16.addWidget(self.rdo_frequency)
        self.rdo_name = QtGui.QRadioButton(self.groupBox_sorted_by)
        self.rdo_name.setObjectName(_fromUtf8("rdo_name"))
        self.verticalLayout_16.addWidget(self.rdo_name)
        self.gridLayout.addWidget(self.groupBox_sorted_by, 3, 0, 1, 2)
        self.groupBox_10 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_10.setTitle(_fromUtf8(""))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.label_5 = QtGui.QLabel(self.groupBox_10)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_14.addWidget(self.label_5)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_10)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout_14.addWidget(self.lineEdit_2)
        self.lbl_most_common = QtGui.QLabel(self.groupBox_10)
        self.lbl_most_common.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_most_common.setObjectName(_fromUtf8("lbl_most_common"))
        self.verticalLayout_14.addWidget(self.lbl_most_common)
        self.gridLayout.addWidget(self.groupBox_10, 1, 0, 1, 2)
        self.groupBox_sort_order = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_sort_order.setObjectName(_fromUtf8("groupBox_sort_order"))
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.groupBox_sort_order)
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.rdo_descending = QtGui.QRadioButton(self.groupBox_sort_order)
        self.rdo_descending.setChecked(True)
        self.rdo_descending.setObjectName(_fromUtf8("rdo_descending"))
        self.verticalLayout_17.addWidget(self.rdo_descending)
        self.rdo_ascending = QtGui.QRadioButton(self.groupBox_sort_order)
        self.rdo_ascending.setObjectName(_fromUtf8("rdo_ascending"))
        self.verticalLayout_17.addWidget(self.rdo_ascending)
        self.gridLayout.addWidget(self.groupBox_sort_order, 3, 2, 1, 2)
        self.groupBox_11 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_11.setTitle(_fromUtf8(""))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.groupBox_11)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.lbl_exclude_if_fewer = QtGui.QLabel(self.groupBox_11)
        self.lbl_exclude_if_fewer.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_exclude_if_fewer.setObjectName(_fromUtf8("lbl_exclude_if_fewer"))
        self.verticalLayout_15.addWidget(self.lbl_exclude_if_fewer)
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_11)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.verticalLayout_15.addWidget(self.lineEdit_3)
        self.label_8 = QtGui.QLabel(self.groupBox_11)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_15.addWidget(self.label_8)
        self.gridLayout.addWidget(self.groupBox_11, 1, 2, 1, 2)
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.rdo_heedQuality = QtGui.QRadioButton(self.groupBox_6)
        self.rdo_heedQuality.setObjectName(_fromUtf8("rdo_heedQuality"))
        self.verticalLayout_10.addWidget(self.rdo_heedQuality)
        self.rdo_noHeedQuality = QtGui.QRadioButton(self.groupBox_6)
        self.rdo_noHeedQuality.setChecked(True)
        self.rdo_noHeedQuality.setObjectName(_fromUtf8("rdo_noHeedQuality"))
        self.verticalLayout_10.addWidget(self.rdo_noHeedQuality)
        self.gridLayout.addWidget(self.groupBox_6, 2, 2, 1, 2)
        self.groupBox_9 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.rdo_compound = QtGui.QRadioButton(self.groupBox_9)
        self.rdo_compound.setChecked(True)
        self.rdo_compound.setObjectName(_fromUtf8("rdo_compound"))
        self.verticalLayout_13.addWidget(self.rdo_compound)
        self.rdo_simple = QtGui.QRadioButton(self.groupBox_9)
        self.rdo_simple.setObjectName(_fromUtf8("rdo_simple"))
        self.verticalLayout_13.addWidget(self.rdo_simple)
        self.gridLayout.addWidget(self.groupBox_9, 2, 0, 1, 2)
        self.groupBox_7 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.rdo_intervals = QtGui.QRadioButton(self.groupBox_7)
        self.rdo_intervals.setObjectName(_fromUtf8("rdo_intervals"))
        self.verticalLayout_11.addWidget(self.rdo_intervals)
        self.rdo_ngrams = QtGui.QRadioButton(self.groupBox_7)
        self.rdo_ngrams.setChecked(True)
        self.rdo_ngrams.setObjectName(_fromUtf8("rdo_ngrams"))
        self.verticalLayout_11.addWidget(self.rdo_ngrams)
        self.gridLayout.addWidget(self.groupBox_7, 0, 1, 1, 2)
        self.btn_show_results = QtGui.QPushButton(self.groupBox_2)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/show_checkmark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_show_results.setIcon(icon7)
        self.btn_show_results.setIconSize(QtCore.QSize(64, 64))
        self.btn_show_results.setObjectName(_fromUtf8("btn_show_results"))
        self.gridLayout.addWidget(self.btn_show_results, 3, 5, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 4, 1, 1)
        self.groupBox_targeted_score = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_targeted_score.setEnabled(False)
        self.groupBox_targeted_score.setObjectName(_fromUtf8("groupBox_targeted_score"))
        self.verticalLayout_18 = QtGui.QVBoxLayout(self.groupBox_targeted_score)
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.label_9 = QtGui.QLabel(self.groupBox_targeted_score)
        self.label_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_18.addWidget(self.label_9)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_targeted_score)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.pushButton = QtGui.QPushButton(self.groupBox_targeted_score)
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setIcon(icon4)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_18.addLayout(self.horizontalLayout_2)
        self.label_10 = QtGui.QLabel(self.groupBox_targeted_score)
        self.label_10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_18.addWidget(self.label_10)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_targeted_score)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.horizontalLayout_5.addWidget(self.lineEdit_5)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_targeted_score)
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout_18.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_targeted_score)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.frame = QtGui.QFrame(self.groupBox_targeted_score)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_6.addWidget(self.frame)
        self.verticalLayout_18.addLayout(self.horizontalLayout_6)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox_targeted_score)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout_18.addWidget(self.plainTextEdit)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem5)
        self.gridLayout.addWidget(self.groupBox_targeted_score, 0, 4, 3, 2)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.main_screen.addWidget(self.page_show)
        self.page_working = QtGui.QWidget()
        self.page_working.setObjectName(_fromUtf8("page_working"))
        self.verticalLayout_21 = QtGui.QVBoxLayout(self.page_working)
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem6)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.pushButton_7 = QtGui.QPushButton(self.page_working)
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/working.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setIconSize(QtCore.QSize(64, 64))
        self.pushButton_7.setCheckable(False)
        self.pushButton_7.setChecked(False)
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout_8.addWidget(self.pushButton_7)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.verticalLayout_21.addLayout(self.horizontalLayout_8)
        self.lbl_status_text = QtGui.QLabel(self.page_working)
        self.lbl_status_text.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lbl_status_text.setObjectName(_fromUtf8("lbl_status_text"))
        self.verticalLayout_21.addWidget(self.lbl_status_text)
        self.progress_bar = QtGui.QProgressBar(self.page_working)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName(_fromUtf8("progress_bar"))
        self.verticalLayout_21.addWidget(self.progress_bar)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem9)
        self.main_screen.addWidget(self.page_working)
        self.page_settings = QtGui.QWidget()
        self.page_settings.setObjectName(_fromUtf8("page_settings"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.page_settings)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox_3 = QtGui.QGroupBox(self.page_settings)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_20 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_20.setObjectName(_fromUtf8("verticalLayout_20"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_7.addWidget(self.label_11)
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.horizontalLayout_7.addWidget(self.lineEdit_6)
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_7.addWidget(self.pushButton_4)
        self.verticalLayout_20.addLayout(self.horizontalLayout_7)
        self.groupBox_15 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_15.setObjectName(_fromUtf8("groupBox_15"))
        self.verticalLayout_19 = QtGui.QVBoxLayout(self.groupBox_15)
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_15)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout_19.addWidget(self.pushButton_5)
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_15)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.verticalLayout_19.addWidget(self.pushButton_6)
        self.verticalLayout_20.addWidget(self.groupBox_15)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.main_screen.addWidget(self.page_settings)
        self.page_about = QtGui.QWidget()
        self.page_about.setObjectName(_fromUtf8("page_about"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.page_about)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox_4 = QtGui.QGroupBox(self.page_about)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_6.addWidget(self.label)
        self.line = QtGui.QFrame(self.groupBox_4)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_6.addWidget(self.line)
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_6.addWidget(self.label_2)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.main_screen.addWidget(self.page_about)
        self.verticalLayout.addWidget(self.main_screen)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.label_4.setBuddy(self.line_files_n)

        self.retranslateUi(MainWindow)
        self.main_screen.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "vis", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_settings.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_about.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Analyze", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Files to Analyze:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Which values of n?", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_files_analyze.setText(QtGui.QApplication.translate("MainWindow", "&Start Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Show Results", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindow", "Output Format", None, QtGui.QApplication.UnicodeUTF8))
        self.rdo_chart.setText(QtGui.QApplication.translate("MainWindow", "Chart/Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.rdo_score.setText(QtGui.QApplication.translate("MainWindow", "Summary Score", None, QtGui.QApplication.UnicodeUTF8))
        self.rdo_targeted_score.setText(QtGui.QApplication.translate("MainWindow", "Targeted Score", None, QtGui.QApplication.UnicodeUTF8))
        self.rdo_list.setText(QtGui.QApplication.translate("MainWindow", "List", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_n.setTitle(QtGui.QApplication.translate("MainWindow", "Values of N", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_sorted_by.setTitle(QtGui.QApplication.translate("MainWindow", "Sorted by...", None, QtGui.QApplication.UnicodeUTF8))
        self.rdo_frequency.setText(QtGui.QApplication.translate("MainWindow", "frequency", None, QtGui.QApplication.UnicodeUTF8))
        self.rdo_name.setText(QtGui.QApplication.translate("MainWindow", "triangle", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Output the", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_most_common.setText(QtGui.QApplication.translate("MainWindow", "most common triangles.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_sort_order.setTitle(QtGui.QApplication.translate("MainWindow", "Sort Order", None, QtGui.QApplication.UnicodeUTF8))
        self.rdo_descending.setText(QtGui.QApplication.translate("MainWindow", "Descending (High to Low)", None, QtGui.QApplication.UnicodeUTF8))
        self.rdo_ascending.setText(QtGui.QApplication.translate("MainWindow", "Ascending (Low to High)", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_exclude_if_fewer.setText(QtGui.QApplication.translate("MainWindow", "Exclude triangles with fewer than", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "occurrences.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("MainWindow", "Interval Quality", None, QtGui.QApplication.UnicodeUTF8))
        self.rdo_heedQuality.setText(QtGui.QApplication.translate("MainWindow", "Display", None, QtGui.QApplication.UnicodeUTF8))
        self.rdo_noHeedQuality.setText(QtGui.QApplication.translate("MainWindow", "Ignore", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_9.setTitle(QtGui.QApplication.translate("MainWindow", "Octaves", None, QtGui.QApplication.UnicodeUTF8))
        self.rdo_compound.setText(QtGui.QApplication.translate("MainWindow", "Compound Intervals", None, QtGui.QApplication.UnicodeUTF8))
        self.rdo_simple.setText(QtGui.QApplication.translate("MainWindow", "Simple Intervals", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("MainWindow", "What to Display", None, QtGui.QApplication.UnicodeUTF8))
        self.rdo_intervals.setText(QtGui.QApplication.translate("MainWindow", "Intervals", None, QtGui.QApplication.UnicodeUTF8))
        self.rdo_ngrams.setText(QtGui.QApplication.translate("MainWindow", "Triangles/n-grams", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_show_results.setText(QtGui.QApplication.translate("MainWindow", "Show", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_targeted_score.setTitle(QtGui.QApplication.translate("MainWindow", "Targeted Score", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Annotate this triangle in colour:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Annotate this triangle in black:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Choose Colour", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_status_text.setText(QtGui.QApplication.translate("MainWindow", "Please wait...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Change Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Offset between Intervals:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_6.setText(QtGui.QApplication.translate("MainWindow", "0.5", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "Set", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_15.setTitle(QtGui.QApplication.translate("MainWindow", "Load or Save Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "Load Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("MainWindow", "Save Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Information about vis", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">vis (pre-Milestone 4)</span></p><p>Copyright (c) 2012 Christopher Antila and Jamie Klassen</p><p>This program is free software: you can redistribute it and/or modify<br/>it under the terms of the GNU General Public License as published by<br/>the Free Software Foundation, either version 3 of the License, or<br/>(at your option) any later version.</p><p>This program is distributed in the hope that it will be useful,<br/>but WITHOUT ANY WARRANTY; without even the implied warranty of<br/>MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the<br/>GNU General Public License for more details.</p><p>You should have received a copy of the GNU General Public License<br/>along with this program. If not, see &lt;http://www.gnu.org/licenses/&gt;.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>vis was written as part of McGill University\'s contribution to the ELVIS project.<br/>For more information about ELVIS, please refer to our <a href=\"http://elvis.music.mcgill.ca/\"><span style=\" text-decoration: underline; color:#0057ae;\">web site</span></a>.</p><p>Funding for ELVIS was provided by the following organizations:<br/>- SSHRC (Social Sciences and Humanities Research Council) of Canada<br/>- NEH (National Endowment for the Humanities) of the United States of America<br/>- The Digging into Data Challenge</p><p>vis is written in the Python programming language, and relies on the following<br/>software, all released under free licences:<br/>- <a href=\"http://mit.edu/music21/\"><span style=\" text-decoration: underline; color:#0057ae;\">music21<br/></span></a>- <a href=\"http://www.riverbankcomputing.co.uk/software/pyqt/download\"><span style=\" text-decoration: underline; color:#0057ae;\">PyQt4</span></a><br/>- <a href=\"http://www.oxygen-icons.org/\"><span style=\" text-decoration: underline; color:#0057ae;\">Oxygen Icons</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
