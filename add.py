# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(706, 869)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Block = QWidget()
        self.Block.setObjectName(u"Block")
        self.verticalLayout_2 = QVBoxLayout(self.Block)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.head2_2 = QLabel(self.Block)
        self.head2_2.setObjectName(u"head2_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.head2_2.sizePolicy().hasHeightForWidth())
        self.head2_2.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Agency FB")
        font.setPointSize(16)
        self.head2_2.setFont(font)

        self.horizontalLayout_13.addWidget(self.head2_2)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_52)

        self.label_6 = QLabel(self.Block)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.addBlockBranchComboBox1 = QComboBox(self.Block)
        self.addBlockBranchComboBox1.setObjectName(u"addBlockBranchComboBox1")
        sizePolicy1.setHeightForWidth(self.addBlockBranchComboBox1.sizePolicy().hasHeightForWidth())
        self.addBlockBranchComboBox1.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.addBlockBranchComboBox1)

        self.addBlockBranchComboBox2 = QComboBox(self.Block)
        self.addBlockBranchComboBox2.setObjectName(u"addBlockBranchComboBox2")
        sizePolicy1.setHeightForWidth(self.addBlockBranchComboBox2.sizePolicy().hasHeightForWidth())
        self.addBlockBranchComboBox2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.addBlockBranchComboBox2)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_53)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.addBlockExampleButtom = QPushButton(self.Block)
        self.addBlockExampleButtom.setObjectName(u"addBlockExampleButtom")
        sizePolicy1.setHeightForWidth(self.addBlockExampleButtom.sizePolicy().hasHeightForWidth())
        self.addBlockExampleButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.addBlockExampleButtom)

        self.addBlockClearButtom = QPushButton(self.Block)
        self.addBlockClearButtom.setObjectName(u"addBlockClearButtom")
        sizePolicy1.setHeightForWidth(self.addBlockClearButtom.sizePolicy().hasHeightForWidth())
        self.addBlockClearButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.addBlockClearButtom)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.Block)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.addBlockLibName = QLineEdit(self.Block)
        self.addBlockLibName.setObjectName(u"addBlockLibName")
        sizePolicy1.setHeightForWidth(self.addBlockLibName.sizePolicy().hasHeightForWidth())
        self.addBlockLibName.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.addBlockLibName)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.Block)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.addBlockClassName = QLineEdit(self.Block)
        self.addBlockClassName.setObjectName(u"addBlockClassName")
        sizePolicy1.setHeightForWidth(self.addBlockClassName.sizePolicy().hasHeightForWidth())
        self.addBlockClassName.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.addBlockClassName)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_21)

        self.addBlockColorButtom = QPushButton(self.Block)
        self.addBlockColorButtom.setObjectName(u"addBlockColorButtom")
        sizePolicy1.setHeightForWidth(self.addBlockColorButtom.sizePolicy().hasHeightForWidth())
        self.addBlockColorButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.addBlockColorButtom)

        self.addBlockColorSpinBox = QSpinBox(self.Block)
        self.addBlockColorSpinBox.setObjectName(u"addBlockColorSpinBox")
        sizePolicy1.setHeightForWidth(self.addBlockColorSpinBox.sizePolicy().hasHeightForWidth())
        self.addBlockColorSpinBox.setSizePolicy(sizePolicy1)
        self.addBlockColorSpinBox.setMaximum(16777215)
        self.addBlockColorSpinBox.setDisplayIntegerBase(16)

        self.horizontalLayout.addWidget(self.addBlockColorSpinBox)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_22)

        self.addBlockColorCheckBox = QCheckBox(self.Block)
        self.addBlockColorCheckBox.setObjectName(u"addBlockColorCheckBox")
        sizePolicy1.setHeightForWidth(self.addBlockColorCheckBox.sizePolicy().hasHeightForWidth())
        self.addBlockColorCheckBox.setSizePolicy(sizePolicy1)
        self.addBlockColorCheckBox.setChecked(True)
        self.addBlockColorCheckBox.setTristate(False)

        self.horizontalLayout.addWidget(self.addBlockColorCheckBox)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_23)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_24)

        self.label_9 = QLabel(self.Block)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.addBlockPositionSpinBox = QSpinBox(self.Block)
        self.addBlockPositionSpinBox.setObjectName(u"addBlockPositionSpinBox")
        self.addBlockPositionSpinBox.setMinimum(1)

        self.horizontalLayout_8.addWidget(self.addBlockPositionSpinBox)

        self.label_10 = QLabel(self.Block)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10)

        self.addBlockPositionComboBox = QComboBox(self.Block)
        self.addBlockPositionComboBox.addItem("")
        self.addBlockPositionComboBox.addItem("")
        self.addBlockPositionComboBox.setObjectName(u"addBlockPositionComboBox")
        sizePolicy1.setHeightForWidth(self.addBlockPositionComboBox.sizePolicy().hasHeightForWidth())
        self.addBlockPositionComboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.addBlockPositionComboBox)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_25)

        self.addBlockPositionCheckBox = QCheckBox(self.Block)
        self.addBlockPositionCheckBox.setObjectName(u"addBlockPositionCheckBox")

        self.horizontalLayout_8.addWidget(self.addBlockPositionCheckBox)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_26)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.addBlockConnectCheckBox = QCheckBox(self.Block)
        self.addBlockConnectCheckBox.setObjectName(u"addBlockConnectCheckBox")
        sizePolicy1.setHeightForWidth(self.addBlockConnectCheckBox.sizePolicy().hasHeightForWidth())
        self.addBlockConnectCheckBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_40.addWidget(self.addBlockConnectCheckBox)


        self.verticalLayout.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label = QLabel(self.Block)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_16)

        self.addBlockCodeTextEdit = QPlainTextEdit(self.Block)
        self.addBlockCodeTextEdit.setObjectName(u"addBlockCodeTextEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.addBlockCodeTextEdit.sizePolicy().hasHeightForWidth())
        self.addBlockCodeTextEdit.setSizePolicy(sizePolicy3)
        self.addBlockCodeTextEdit.setPlaceholderText(u"")

        self.verticalLayout.addWidget(self.addBlockCodeTextEdit)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_13 = QLabel(self.Block)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamily(u"Agency FB")
        font1.setPointSize(12)
        self.label_13.setFont(font1)

        self.horizontalLayout_19.addWidget(self.label_13)


        self.verticalLayout.addLayout(self.horizontalLayout_19)

        self.addBlockContentTextEdit = QPlainTextEdit(self.Block)
        self.addBlockContentTextEdit.setObjectName(u"addBlockContentTextEdit")
        sizePolicy3.setHeightForWidth(self.addBlockContentTextEdit.sizePolicy().hasHeightForWidth())
        self.addBlockContentTextEdit.setSizePolicy(sizePolicy3)
        self.addBlockContentTextEdit.setPlaceholderText(u"")

        self.verticalLayout.addWidget(self.addBlockContentTextEdit)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.addBlockGeneraButtom = QPushButton(self.Block)
        self.addBlockGeneraButtom.setObjectName(u"addBlockGeneraButtom")
        sizePolicy1.setHeightForWidth(self.addBlockGeneraButtom.sizePolicy().hasHeightForWidth())
        self.addBlockGeneraButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_20.addWidget(self.addBlockGeneraButtom)


        self.verticalLayout.addLayout(self.horizontalLayout_20)

        self.line_8 = QFrame(self.Block)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_8)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.addBlockBackButtom = QPushButton(self.Block)
        self.addBlockBackButtom.setObjectName(u"addBlockBackButtom")
        sizePolicy1.setHeightForWidth(self.addBlockBackButtom.sizePolicy().hasHeightForWidth())
        self.addBlockBackButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_39.addWidget(self.addBlockBackButtom)


        self.verticalLayout.addLayout(self.horizontalLayout_39)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.Block, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_13 = QVBoxLayout(self.tab_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.head2_4 = QLabel(self.tab_3)
        self.head2_4.setObjectName(u"head2_4")
        sizePolicy1.setHeightForWidth(self.head2_4.sizePolicy().hasHeightForWidth())
        self.head2_4.setSizePolicy(sizePolicy1)
        self.head2_4.setFont(font)

        self.horizontalLayout_37.addWidget(self.head2_4)


        self.verticalLayout_12.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_55)

        self.label_42 = QLabel(self.tab_3)
        self.label_42.setObjectName(u"label_42")
        sizePolicy1.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy1)

        self.horizontalLayout_54.addWidget(self.label_42)

        self.modifyBlockBranchComboBox1 = QComboBox(self.tab_3)
        self.modifyBlockBranchComboBox1.setObjectName(u"modifyBlockBranchComboBox1")
        sizePolicy1.setHeightForWidth(self.modifyBlockBranchComboBox1.sizePolicy().hasHeightForWidth())
        self.modifyBlockBranchComboBox1.setSizePolicy(sizePolicy1)

        self.horizontalLayout_54.addWidget(self.modifyBlockBranchComboBox1)

        self.modifyBlockBranchComboBox2 = QComboBox(self.tab_3)
        self.modifyBlockBranchComboBox2.setObjectName(u"modifyBlockBranchComboBox2")
        sizePolicy1.setHeightForWidth(self.modifyBlockBranchComboBox2.sizePolicy().hasHeightForWidth())
        self.modifyBlockBranchComboBox2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_54.addWidget(self.modifyBlockBranchComboBox2)

        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_54)


        self.verticalLayout_12.addLayout(self.horizontalLayout_54)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalSpacer_58 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_58)

        self.label_45 = QLabel(self.tab_3)
        self.label_45.setObjectName(u"label_45")
        sizePolicy1.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy1)

        self.horizontalLayout_59.addWidget(self.label_45)

        self.modifyBlockPositionSpinBox = QSpinBox(self.tab_3)
        self.modifyBlockPositionSpinBox.setObjectName(u"modifyBlockPositionSpinBox")
        self.modifyBlockPositionSpinBox.setMinimum(1)

        self.horizontalLayout_59.addWidget(self.modifyBlockPositionSpinBox)

        self.label_46 = QLabel(self.tab_3)
        self.label_46.setObjectName(u"label_46")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy4)

        self.horizontalLayout_59.addWidget(self.label_46)

        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_56)


        self.verticalLayout_12.addLayout(self.horizontalLayout_59)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_43 = QLabel(self.tab_3)
        self.label_43.setObjectName(u"label_43")
        sizePolicy1.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy1)

        self.horizontalLayout_56.addWidget(self.label_43)

        self.modifyBlockLibName = QLineEdit(self.tab_3)
        self.modifyBlockLibName.setObjectName(u"modifyBlockLibName")
        sizePolicy1.setHeightForWidth(self.modifyBlockLibName.sizePolicy().hasHeightForWidth())
        self.modifyBlockLibName.setSizePolicy(sizePolicy1)

        self.horizontalLayout_56.addWidget(self.modifyBlockLibName)

        self.modifyBlockLibCheckBox = QCheckBox(self.tab_3)
        self.modifyBlockLibCheckBox.setObjectName(u"modifyBlockLibCheckBox")
        sizePolicy1.setHeightForWidth(self.modifyBlockLibCheckBox.sizePolicy().hasHeightForWidth())
        self.modifyBlockLibCheckBox.setSizePolicy(sizePolicy1)
        self.modifyBlockLibCheckBox.setChecked(True)
        self.modifyBlockLibCheckBox.setTristate(False)

        self.horizontalLayout_56.addWidget(self.modifyBlockLibCheckBox)


        self.verticalLayout_12.addLayout(self.horizontalLayout_56)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_44 = QLabel(self.tab_3)
        self.label_44.setObjectName(u"label_44")
        sizePolicy1.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy1)

        self.horizontalLayout_57.addWidget(self.label_44)

        self.modifyBlockClassName = QLineEdit(self.tab_3)
        self.modifyBlockClassName.setObjectName(u"modifyBlockClassName")
        sizePolicy1.setHeightForWidth(self.modifyBlockClassName.sizePolicy().hasHeightForWidth())
        self.modifyBlockClassName.setSizePolicy(sizePolicy1)

        self.horizontalLayout_57.addWidget(self.modifyBlockClassName)

        self.modifyBlockClassCheckBox = QCheckBox(self.tab_3)
        self.modifyBlockClassCheckBox.setObjectName(u"modifyBlockClassCheckBox")
        sizePolicy1.setHeightForWidth(self.modifyBlockClassCheckBox.sizePolicy().hasHeightForWidth())
        self.modifyBlockClassCheckBox.setSizePolicy(sizePolicy1)
        self.modifyBlockClassCheckBox.setChecked(True)
        self.modifyBlockClassCheckBox.setTristate(False)

        self.horizontalLayout_57.addWidget(self.modifyBlockClassCheckBox)


        self.verticalLayout_12.addLayout(self.horizontalLayout_57)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_51)

        self.modifyBlockColorButtom = QPushButton(self.tab_3)
        self.modifyBlockColorButtom.setObjectName(u"modifyBlockColorButtom")
        sizePolicy1.setHeightForWidth(self.modifyBlockColorButtom.sizePolicy().hasHeightForWidth())
        self.modifyBlockColorButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_58.addWidget(self.modifyBlockColorButtom)

        self.modifyBlockColorSpinBox = QSpinBox(self.tab_3)
        self.modifyBlockColorSpinBox.setObjectName(u"modifyBlockColorSpinBox")
        sizePolicy1.setHeightForWidth(self.modifyBlockColorSpinBox.sizePolicy().hasHeightForWidth())
        self.modifyBlockColorSpinBox.setSizePolicy(sizePolicy1)
        self.modifyBlockColorSpinBox.setMaximum(16777215)
        self.modifyBlockColorSpinBox.setDisplayIntegerBase(16)

        self.horizontalLayout_58.addWidget(self.modifyBlockColorSpinBox)

        self.modifyBlockColorCheckBox = QCheckBox(self.tab_3)
        self.modifyBlockColorCheckBox.setObjectName(u"modifyBlockColorCheckBox")
        sizePolicy1.setHeightForWidth(self.modifyBlockColorCheckBox.sizePolicy().hasHeightForWidth())
        self.modifyBlockColorCheckBox.setSizePolicy(sizePolicy1)
        self.modifyBlockColorCheckBox.setChecked(True)
        self.modifyBlockColorCheckBox.setTristate(False)

        self.horizontalLayout_58.addWidget(self.modifyBlockColorCheckBox)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_49)


        self.verticalLayout_12.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.modifyBlockConnectCheckBox = QCheckBox(self.tab_3)
        self.modifyBlockConnectCheckBox.setObjectName(u"modifyBlockConnectCheckBox")
        sizePolicy1.setHeightForWidth(self.modifyBlockConnectCheckBox.sizePolicy().hasHeightForWidth())
        self.modifyBlockConnectCheckBox.setSizePolicy(sizePolicy1)
        self.modifyBlockConnectCheckBox.setChecked(True)

        self.horizontalLayout_62.addWidget(self.modifyBlockConnectCheckBox)


        self.verticalLayout_12.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_47 = QLabel(self.tab_3)
        self.label_47.setObjectName(u"label_47")
        sizePolicy1.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy1)

        self.horizontalLayout_63.addWidget(self.label_47)


        self.verticalLayout_12.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.modifyBlockCodeTextEdit = QPlainTextEdit(self.tab_3)
        self.modifyBlockCodeTextEdit.setObjectName(u"modifyBlockCodeTextEdit")
        sizePolicy3.setHeightForWidth(self.modifyBlockCodeTextEdit.sizePolicy().hasHeightForWidth())
        self.modifyBlockCodeTextEdit.setSizePolicy(sizePolicy3)
        self.modifyBlockCodeTextEdit.setPlaceholderText(u"")

        self.horizontalLayout_12.addWidget(self.modifyBlockCodeTextEdit)

        self.modifyBlockCodeCheckBox = QCheckBox(self.tab_3)
        self.modifyBlockCodeCheckBox.setObjectName(u"modifyBlockCodeCheckBox")
        sizePolicy1.setHeightForWidth(self.modifyBlockCodeCheckBox.sizePolicy().hasHeightForWidth())
        self.modifyBlockCodeCheckBox.setSizePolicy(sizePolicy1)
        self.modifyBlockCodeCheckBox.setChecked(True)

        self.horizontalLayout_12.addWidget(self.modifyBlockCodeCheckBox)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_48 = QLabel(self.tab_3)
        self.label_48.setObjectName(u"label_48")
        sizePolicy1.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy1)

        self.horizontalLayout_64.addWidget(self.label_48)


        self.verticalLayout_12.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.modifyBlockContentTextEdit = QPlainTextEdit(self.tab_3)
        self.modifyBlockContentTextEdit.setObjectName(u"modifyBlockContentTextEdit")
        sizePolicy3.setHeightForWidth(self.modifyBlockContentTextEdit.sizePolicy().hasHeightForWidth())
        self.modifyBlockContentTextEdit.setSizePolicy(sizePolicy3)
        self.modifyBlockContentTextEdit.setPlaceholderText(u"")

        self.horizontalLayout_4.addWidget(self.modifyBlockContentTextEdit)

        self.modifyBlockContentCheckBox = QCheckBox(self.tab_3)
        self.modifyBlockContentCheckBox.setObjectName(u"modifyBlockContentCheckBox")
        sizePolicy1.setHeightForWidth(self.modifyBlockContentCheckBox.sizePolicy().hasHeightForWidth())
        self.modifyBlockContentCheckBox.setSizePolicy(sizePolicy1)
        self.modifyBlockContentCheckBox.setChecked(True)

        self.horizontalLayout_4.addWidget(self.modifyBlockContentCheckBox)


        self.verticalLayout_12.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.modifyBlockModifyButtom = QPushButton(self.tab_3)
        self.modifyBlockModifyButtom.setObjectName(u"modifyBlockModifyButtom")
        sizePolicy1.setHeightForWidth(self.modifyBlockModifyButtom.sizePolicy().hasHeightForWidth())
        self.modifyBlockModifyButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_65.addWidget(self.modifyBlockModifyButtom)


        self.verticalLayout_12.addLayout(self.horizontalLayout_65)

        self.line_3 = QFrame(self.tab_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_12.addWidget(self.line_3)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.head2_3 = QLabel(self.tab_3)
        self.head2_3.setObjectName(u"head2_3")
        sizePolicy1.setHeightForWidth(self.head2_3.sizePolicy().hasHeightForWidth())
        self.head2_3.setSizePolicy(sizePolicy1)
        self.head2_3.setFont(font)

        self.horizontalLayout_66.addWidget(self.head2_3)


        self.verticalLayout_12.addLayout(self.horizontalLayout_66)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_27)

        self.label_14 = QLabel(self.tab_3)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)

        self.horizontalLayout_60.addWidget(self.label_14)

        self.deleteBlockBranchComboBox1 = QComboBox(self.tab_3)
        self.deleteBlockBranchComboBox1.setObjectName(u"deleteBlockBranchComboBox1")
        sizePolicy1.setHeightForWidth(self.deleteBlockBranchComboBox1.sizePolicy().hasHeightForWidth())
        self.deleteBlockBranchComboBox1.setSizePolicy(sizePolicy1)

        self.horizontalLayout_60.addWidget(self.deleteBlockBranchComboBox1)

        self.deleteBlockBranchComboBox2 = QComboBox(self.tab_3)
        self.deleteBlockBranchComboBox2.setObjectName(u"deleteBlockBranchComboBox2")
        sizePolicy1.setHeightForWidth(self.deleteBlockBranchComboBox2.sizePolicy().hasHeightForWidth())
        self.deleteBlockBranchComboBox2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_60.addWidget(self.deleteBlockBranchComboBox2)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_28)


        self.verticalLayout_12.addLayout(self.horizontalLayout_60)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_42)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_61.addWidget(self.label_2)

        self.deleteBlockPositionSpinBox = QSpinBox(self.tab_3)
        self.deleteBlockPositionSpinBox.setObjectName(u"deleteBlockPositionSpinBox")
        sizePolicy1.setHeightForWidth(self.deleteBlockPositionSpinBox.sizePolicy().hasHeightForWidth())
        self.deleteBlockPositionSpinBox.setSizePolicy(sizePolicy1)
        self.deleteBlockPositionSpinBox.setMinimum(1)
        self.deleteBlockPositionSpinBox.setMaximum(999)

        self.horizontalLayout_61.addWidget(self.deleteBlockPositionSpinBox)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_43)


        self.verticalLayout_12.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.deleteBlockDeleteButtom = QPushButton(self.tab_3)
        self.deleteBlockDeleteButtom.setObjectName(u"deleteBlockDeleteButtom")
        sizePolicy1.setHeightForWidth(self.deleteBlockDeleteButtom.sizePolicy().hasHeightForWidth())
        self.deleteBlockDeleteButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_67.addWidget(self.deleteBlockDeleteButtom)


        self.verticalLayout_12.addLayout(self.horizontalLayout_67)

        self.line_10 = QFrame(self.tab_3)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_12.addWidget(self.line_10)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.modifyBlockBackButtom = QPushButton(self.tab_3)
        self.modifyBlockBackButtom.setObjectName(u"modifyBlockBackButtom")
        sizePolicy1.setHeightForWidth(self.modifyBlockBackButtom.sizePolicy().hasHeightForWidth())
        self.modifyBlockBackButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_68.addWidget(self.modifyBlockBackButtom)


        self.verticalLayout_12.addLayout(self.horizontalLayout_68)


        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_9 = QVBoxLayout(self.tab_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_18 = QLabel(self.tab_5)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setFont(font)

        self.horizontalLayout_34.addWidget(self.label_18)


        self.verticalLayout_8.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_29)

        self.label_19 = QLabel(self.tab_5)
        self.label_19.setObjectName(u"label_19")
        sizePolicy1.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy1)

        self.horizontalLayout_30.addWidget(self.label_19)

        self.addLabelBranchComboBox1 = QComboBox(self.tab_5)
        self.addLabelBranchComboBox1.setObjectName(u"addLabelBranchComboBox1")
        sizePolicy1.setHeightForWidth(self.addLabelBranchComboBox1.sizePolicy().hasHeightForWidth())
        self.addLabelBranchComboBox1.setSizePolicy(sizePolicy1)

        self.horizontalLayout_30.addWidget(self.addLabelBranchComboBox1)

        self.addLabelBranchComboBox2 = QComboBox(self.tab_5)
        self.addLabelBranchComboBox2.setObjectName(u"addLabelBranchComboBox2")

        self.horizontalLayout_30.addWidget(self.addLabelBranchComboBox2)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_30)


        self.verticalLayout_8.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_31)

        self.label_20 = QLabel(self.tab_5)
        self.label_20.setObjectName(u"label_20")
        sizePolicy1.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy1)

        self.horizontalLayout_28.addWidget(self.label_20)

        self.addLabelPositionSpinBox = QSpinBox(self.tab_5)
        self.addLabelPositionSpinBox.setObjectName(u"addLabelPositionSpinBox")
        sizePolicy1.setHeightForWidth(self.addLabelPositionSpinBox.sizePolicy().hasHeightForWidth())
        self.addLabelPositionSpinBox.setSizePolicy(sizePolicy1)
        self.addLabelPositionSpinBox.setMinimum(1)

        self.horizontalLayout_28.addWidget(self.addLabelPositionSpinBox)

        self.addLabelPositionComboBox = QComboBox(self.tab_5)
        self.addLabelPositionComboBox.addItem("")
        self.addLabelPositionComboBox.addItem("")
        self.addLabelPositionComboBox.setObjectName(u"addLabelPositionComboBox")
        sizePolicy1.setHeightForWidth(self.addLabelPositionComboBox.sizePolicy().hasHeightForWidth())
        self.addLabelPositionComboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_28.addWidget(self.addLabelPositionComboBox)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_32)

        self.addLabelPositionCheckBox = QCheckBox(self.tab_5)
        self.addLabelPositionCheckBox.setObjectName(u"addLabelPositionCheckBox")
        sizePolicy1.setHeightForWidth(self.addLabelPositionCheckBox.sizePolicy().hasHeightForWidth())
        self.addLabelPositionCheckBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_28.addWidget(self.addLabelPositionCheckBox)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_33)


        self.verticalLayout_8.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_21 = QLabel(self.tab_5)
        self.label_21.setObjectName(u"label_21")
        sizePolicy1.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy1)

        self.horizontalLayout_33.addWidget(self.label_21)

        self.addLabelContent = QLineEdit(self.tab_5)
        self.addLabelContent.setObjectName(u"addLabelContent")

        self.horizontalLayout_33.addWidget(self.addLabelContent)


        self.verticalLayout_8.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_40)

        self.addLabelGenraButtom = QPushButton(self.tab_5)
        self.addLabelGenraButtom.setObjectName(u"addLabelGenraButtom")
        sizePolicy1.setHeightForWidth(self.addLabelGenraButtom.sizePolicy().hasHeightForWidth())
        self.addLabelGenraButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_29.addWidget(self.addLabelGenraButtom)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_41)


        self.verticalLayout_8.addLayout(self.horizontalLayout_29)

        self.line_2 = QFrame(self.tab_5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_22 = QLabel(self.tab_5)
        self.label_22.setObjectName(u"label_22")
        sizePolicy1.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy1)
        self.label_22.setFont(font)

        self.horizontalLayout_35.addWidget(self.label_22)


        self.verticalLayout_8.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_34)

        self.label_23 = QLabel(self.tab_5)
        self.label_23.setObjectName(u"label_23")
        sizePolicy1.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy1)

        self.horizontalLayout_27.addWidget(self.label_23)

        self.deleteLabelBranchComboBox1 = QComboBox(self.tab_5)
        self.deleteLabelBranchComboBox1.setObjectName(u"deleteLabelBranchComboBox1")
        sizePolicy1.setHeightForWidth(self.deleteLabelBranchComboBox1.sizePolicy().hasHeightForWidth())
        self.deleteLabelBranchComboBox1.setSizePolicy(sizePolicy1)

        self.horizontalLayout_27.addWidget(self.deleteLabelBranchComboBox1)

        self.deleteLabelBranchComboBox2 = QComboBox(self.tab_5)
        self.deleteLabelBranchComboBox2.setObjectName(u"deleteLabelBranchComboBox2")

        self.horizontalLayout_27.addWidget(self.deleteLabelBranchComboBox2)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_35)


        self.verticalLayout_8.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_36)

        self.label_24 = QLabel(self.tab_5)
        self.label_24.setObjectName(u"label_24")
        sizePolicy1.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy1)

        self.horizontalLayout_31.addWidget(self.label_24)

        self.deleteLabelPositionSpinBox = QSpinBox(self.tab_5)
        self.deleteLabelPositionSpinBox.setObjectName(u"deleteLabelPositionSpinBox")
        sizePolicy1.setHeightForWidth(self.deleteLabelPositionSpinBox.sizePolicy().hasHeightForWidth())
        self.deleteLabelPositionSpinBox.setSizePolicy(sizePolicy1)
        self.deleteLabelPositionSpinBox.setMinimum(1)

        self.horizontalLayout_31.addWidget(self.deleteLabelPositionSpinBox)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_37)


        self.verticalLayout_8.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_38)

        self.deleteLabelDeleteButtom = QPushButton(self.tab_5)
        self.deleteLabelDeleteButtom.setObjectName(u"deleteLabelDeleteButtom")
        sizePolicy1.setHeightForWidth(self.deleteLabelDeleteButtom.sizePolicy().hasHeightForWidth())
        self.deleteLabelDeleteButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_32.addWidget(self.deleteLabelDeleteButtom)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_39)


        self.verticalLayout_8.addLayout(self.horizontalLayout_32)

        self.line_6 = QFrame(self.tab_5)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_6)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.addLabelBackButtom = QPushButton(self.tab_5)
        self.addLabelBackButtom.setObjectName(u"addLabelBackButtom")
        sizePolicy1.setHeightForWidth(self.addLabelBackButtom.sizePolicy().hasHeightForWidth())
        self.addLabelBackButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_55.addWidget(self.addLabelBackButtom)


        self.verticalLayout_8.addLayout(self.horizontalLayout_55)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font)

        self.horizontalLayout_44.addWidget(self.label_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.addBigBrachColorButtom = QPushButton(self.tab_2)
        self.addBigBrachColorButtom.setObjectName(u"addBigBrachColorButtom")
        sizePolicy1.setHeightForWidth(self.addBigBrachColorButtom.sizePolicy().hasHeightForWidth())
        self.addBigBrachColorButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_17.addWidget(self.addBigBrachColorButtom)

        self.addBigBrachColorSpinBox = QSpinBox(self.tab_2)
        self.addBigBrachColorSpinBox.setObjectName(u"addBigBrachColorSpinBox")
        sizePolicy1.setHeightForWidth(self.addBigBrachColorSpinBox.sizePolicy().hasHeightForWidth())
        self.addBigBrachColorSpinBox.setSizePolicy(sizePolicy1)
        self.addBigBrachColorSpinBox.setMaximum(16777215)
        self.addBigBrachColorSpinBox.setValue(0)
        self.addBigBrachColorSpinBox.setDisplayIntegerBase(16)

        self.horizontalLayout_17.addWidget(self.addBigBrachColorSpinBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.label_4)

        self.addBigBrachPotionSpinBox = QSpinBox(self.tab_2)
        self.addBigBrachPotionSpinBox.setObjectName(u"addBigBrachPotionSpinBox")
        sizePolicy1.setHeightForWidth(self.addBigBrachPotionSpinBox.sizePolicy().hasHeightForWidth())
        self.addBigBrachPotionSpinBox.setSizePolicy(sizePolicy1)
        self.addBigBrachPotionSpinBox.setMinimum(1)

        self.horizontalLayout_9.addWidget(self.addBigBrachPotionSpinBox)

        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.label_11)

        self.addBigBrachPotionComboBox = QComboBox(self.tab_2)
        self.addBigBrachPotionComboBox.addItem("")
        self.addBigBrachPotionComboBox.addItem("")
        self.addBigBrachPotionComboBox.setObjectName(u"addBigBrachPotionComboBox")
        sizePolicy1.setHeightForWidth(self.addBigBrachPotionComboBox.sizePolicy().hasHeightForWidth())
        self.addBigBrachPotionComboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.addBigBrachPotionComboBox)

        self.addBigBrachPotionCheckBox = QCheckBox(self.tab_2)
        self.addBigBrachPotionCheckBox.setObjectName(u"addBigBrachPotionCheckBox")
        sizePolicy1.setHeightForWidth(self.addBigBrachPotionCheckBox.sizePolicy().hasHeightForWidth())
        self.addBigBrachPotionCheckBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.addBigBrachPotionCheckBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)

        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.label_5)

        self.addBigBrachName = QLineEdit(self.tab_2)
        self.addBigBrachName.setObjectName(u"addBigBrachName")
        sizePolicy1.setHeightForWidth(self.addBigBrachName.sizePolicy().hasHeightForWidth())
        self.addBigBrachName.setSizePolicy(sizePolicy1)

        self.horizontalLayout_11.addWidget(self.addBigBrachName)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.label_12)

        self.addBigBrachFileName = QLineEdit(self.tab_2)
        self.addBigBrachFileName.setObjectName(u"addBigBrachFileName")
        sizePolicy1.setHeightForWidth(self.addBigBrachFileName.sizePolicy().hasHeightForWidth())
        self.addBigBrachFileName.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.addBigBrachFileName)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.addBigBrachNameCheckBox = QCheckBox(self.tab_2)
        self.addBigBrachNameCheckBox.setObjectName(u"addBigBrachNameCheckBox")
        sizePolicy1.setHeightForWidth(self.addBigBrachNameCheckBox.sizePolicy().hasHeightForWidth())
        self.addBigBrachNameCheckBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.addBigBrachNameCheckBox)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_11)

        self.addBigBrachNameButtom = QPushButton(self.tab_2)
        self.addBigBrachNameButtom.setObjectName(u"addBigBrachNameButtom")
        sizePolicy1.setHeightForWidth(self.addBigBrachNameButtom.sizePolicy().hasHeightForWidth())
        self.addBigBrachNameButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_38.addWidget(self.addBigBrachNameButtom)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_12)


        self.verticalLayout_5.addLayout(self.horizontalLayout_38)

        self.line_4 = QFrame(self.tab_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_4)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_25 = QLabel(self.tab_2)
        self.label_25.setObjectName(u"label_25")
        sizePolicy1.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy1)
        self.label_25.setFont(font)

        self.horizontalLayout_45.addWidget(self.label_25)


        self.verticalLayout_5.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_46)

        self.label_26 = QLabel(self.tab_2)
        self.label_26.setObjectName(u"label_26")
        sizePolicy1.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy1)

        self.horizontalLayout_14.addWidget(self.label_26)

        self.deleteBigBranchComboBox = QComboBox(self.tab_2)
        self.deleteBigBranchComboBox.setObjectName(u"deleteBigBranchComboBox")

        self.horizontalLayout_14.addWidget(self.deleteBigBranchComboBox)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_47)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.deleteBigBranchButtom = QPushButton(self.tab_2)
        self.deleteBigBranchButtom.setObjectName(u"deleteBigBranchButtom")
        sizePolicy1.setHeightForWidth(self.deleteBigBranchButtom.sizePolicy().hasHeightForWidth())
        self.deleteBigBranchButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_46.addWidget(self.deleteBigBranchButtom)


        self.verticalLayout_5.addLayout(self.horizontalLayout_46)

        self.line_11 = QFrame(self.tab_2)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_11)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_31 = QLabel(self.tab_2)
        self.label_31.setObjectName(u"label_31")
        sizePolicy1.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy1)
        self.label_31.setFont(font)

        self.horizontalLayout_47.addWidget(self.label_31)


        self.verticalLayout_5.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_50)

        self.label_35 = QLabel(self.tab_2)
        self.label_35.setObjectName(u"label_35")
        sizePolicy1.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.label_35)

        self.modifyBranchNameComboBox = QComboBox(self.tab_2)
        self.modifyBranchNameComboBox.setObjectName(u"modifyBranchNameComboBox")

        self.horizontalLayout_10.addWidget(self.modifyBranchNameComboBox)

        self.modifyBranchPositionComboBox = QComboBox(self.tab_2)
        self.modifyBranchPositionComboBox.addItem("")
        self.modifyBranchPositionComboBox.addItem("")
        self.modifyBranchPositionComboBox.setObjectName(u"modifyBranchPositionComboBox")
        sizePolicy1.setHeightForWidth(self.modifyBranchPositionComboBox.sizePolicy().hasHeightForWidth())
        self.modifyBranchPositionComboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.modifyBranchPositionComboBox)

        self.modifyBranchPositionSpinBox = QSpinBox(self.tab_2)
        self.modifyBranchPositionSpinBox.setObjectName(u"modifyBranchPositionSpinBox")
        sizePolicy1.setHeightForWidth(self.modifyBranchPositionSpinBox.sizePolicy().hasHeightForWidth())
        self.modifyBranchPositionSpinBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.modifyBranchPositionSpinBox)

        self.label_41 = QLabel(self.tab_2)
        self.label_41.setObjectName(u"label_41")
        sizePolicy1.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.label_41)

        self.horizontalSpacer_57 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_57)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.modifyBranchPositionButtom = QPushButton(self.tab_2)
        self.modifyBranchPositionButtom.setObjectName(u"modifyBranchPositionButtom")
        sizePolicy1.setHeightForWidth(self.modifyBranchPositionButtom.sizePolicy().hasHeightForWidth())
        self.modifyBranchPositionButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_69.addWidget(self.modifyBranchPositionButtom)


        self.verticalLayout_5.addLayout(self.horizontalLayout_69)

        self.line_9 = QFrame(self.tab_2)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_9)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.deleteBlockBackButtom = QPushButton(self.tab_2)
        self.deleteBlockBackButtom.setObjectName(u"deleteBlockBackButtom")
        sizePolicy1.setHeightForWidth(self.deleteBlockBackButtom.sizePolicy().hasHeightForWidth())
        self.deleteBlockBackButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_70.addWidget(self.deleteBlockBackButtom)


        self.verticalLayout_5.addLayout(self.horizontalLayout_70)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.tabWidget.addTab(self.tab_2, "")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setFont(font)

        self.horizontalLayout_21.addWidget(self.label_15)


        self.verticalLayout_3.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_13)

        self.addSmallBrachColorButtom = QPushButton(self.widget)
        self.addSmallBrachColorButtom.setObjectName(u"addSmallBrachColorButtom")
        sizePolicy1.setHeightForWidth(self.addSmallBrachColorButtom.sizePolicy().hasHeightForWidth())
        self.addSmallBrachColorButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_18.addWidget(self.addSmallBrachColorButtom)

        self.addSmallBrachColorSpinBox = QSpinBox(self.widget)
        self.addSmallBrachColorSpinBox.setObjectName(u"addSmallBrachColorSpinBox")
        sizePolicy1.setHeightForWidth(self.addSmallBrachColorSpinBox.sizePolicy().hasHeightForWidth())
        self.addSmallBrachColorSpinBox.setSizePolicy(sizePolicy1)
        self.addSmallBrachColorSpinBox.setMaximum(16777215)
        self.addSmallBrachColorSpinBox.setDisplayIntegerBase(16)

        self.horizontalLayout_18.addWidget(self.addSmallBrachColorSpinBox)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_14)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_15)

        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)

        self.horizontalLayout_22.addWidget(self.label_16)

        self.addSmallBrachPotionComboBox = QComboBox(self.widget)
        self.addSmallBrachPotionComboBox.setObjectName(u"addSmallBrachPotionComboBox")
        sizePolicy1.setHeightForWidth(self.addSmallBrachPotionComboBox.sizePolicy().hasHeightForWidth())
        self.addSmallBrachPotionComboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_22.addWidget(self.addSmallBrachPotionComboBox)

        self.label_32 = QLabel(self.widget)
        self.label_32.setObjectName(u"label_32")
        sizePolicy4.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy4)

        self.horizontalLayout_22.addWidget(self.label_32)

        self.addSmallBrachPotionSpinBox = QSpinBox(self.widget)
        self.addSmallBrachPotionSpinBox.setObjectName(u"addSmallBrachPotionSpinBox")
        self.addSmallBrachPotionSpinBox.setMinimum(1)

        self.horizontalLayout_22.addWidget(self.addSmallBrachPotionSpinBox)

        self.label_33 = QLabel(self.widget)
        self.label_33.setObjectName(u"label_33")
        sizePolicy4.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy4)

        self.horizontalLayout_22.addWidget(self.label_33)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_16)


        self.verticalLayout_3.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_17)

        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)

        self.horizontalLayout_23.addWidget(self.label_17)

        self.addSmallBrachName = QLineEdit(self.widget)
        self.addSmallBrachName.setObjectName(u"addSmallBrachName")
        sizePolicy1.setHeightForWidth(self.addSmallBrachName.sizePolicy().hasHeightForWidth())
        self.addSmallBrachName.setSizePolicy(sizePolicy1)

        self.horizontalLayout_23.addWidget(self.addSmallBrachName)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_18)


        self.verticalLayout_3.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_19)

        self.addSmallBrachGeneraButtom = QPushButton(self.widget)
        self.addSmallBrachGeneraButtom.setObjectName(u"addSmallBrachGeneraButtom")
        sizePolicy1.setHeightForWidth(self.addSmallBrachGeneraButtom.sizePolicy().hasHeightForWidth())
        self.addSmallBrachGeneraButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_24.addWidget(self.addSmallBrachGeneraButtom)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_20)


        self.verticalLayout_3.addLayout(self.horizontalLayout_24)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_27 = QLabel(self.widget)
        self.label_27.setObjectName(u"label_27")
        sizePolicy1.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy1)
        self.label_27.setFont(font)

        self.horizontalLayout_41.addWidget(self.label_27)


        self.verticalLayout_3.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_3)

        self.label_28 = QLabel(self.widget)
        self.label_28.setObjectName(u"label_28")
        sizePolicy1.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy1)

        self.horizontalLayout_15.addWidget(self.label_28)

        self.deleteSmallBranchName = QComboBox(self.widget)
        self.deleteSmallBranchName.setObjectName(u"deleteSmallBranchName")
        sizePolicy1.setHeightForWidth(self.deleteSmallBranchName.sizePolicy().hasHeightForWidth())
        self.deleteSmallBranchName.setSizePolicy(sizePolicy1)

        self.horizontalLayout_15.addWidget(self.deleteSmallBranchName)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer)

        self.label_34 = QLabel(self.widget)
        self.label_34.setObjectName(u"label_34")
        sizePolicy1.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy1)

        self.horizontalLayout_25.addWidget(self.label_34)

        self.deleteSmallBranchName2 = QComboBox(self.widget)
        self.deleteSmallBranchName2.setObjectName(u"deleteSmallBranchName2")

        self.horizontalLayout_25.addWidget(self.deleteSmallBranchName2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.deleteSmallBranchButtom = QPushButton(self.widget)
        self.deleteSmallBranchButtom.setObjectName(u"deleteSmallBranchButtom")
        sizePolicy1.setHeightForWidth(self.deleteSmallBranchButtom.sizePolicy().hasHeightForWidth())
        self.deleteSmallBranchButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_71.addWidget(self.deleteSmallBranchButtom)


        self.verticalLayout_3.addLayout(self.horizontalLayout_71)

        self.line_7 = QFrame(self.widget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_7)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.addSmallBrachBackButtom = QPushButton(self.widget)
        self.addSmallBrachBackButtom.setObjectName(u"addSmallBrachBackButtom")
        sizePolicy1.setHeightForWidth(self.addSmallBrachBackButtom.sizePolicy().hasHeightForWidth())
        self.addSmallBrachBackButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_43.addWidget(self.addSmallBrachBackButtom)


        self.verticalLayout_3.addLayout(self.horizontalLayout_43)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.widget, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_11 = QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_29 = QLabel(self.tab)
        self.label_29.setObjectName(u"label_29")
        sizePolicy1.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy1)
        self.label_29.setFont(font)

        self.horizontalLayout_50.addWidget(self.label_29)


        self.verticalLayout_10.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_30 = QLabel(self.tab)
        self.label_30.setObjectName(u"label_30")
        sizePolicy4.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy4)

        self.horizontalLayout_26.addWidget(self.label_30)

        self.importBranchFileUrl = QLineEdit(self.tab)
        self.importBranchFileUrl.setObjectName(u"importBranchFileUrl")

        self.horizontalLayout_26.addWidget(self.importBranchFileUrl)

        self.importBranchSelectButtom = QPushButton(self.tab)
        self.importBranchSelectButtom.setObjectName(u"importBranchSelectButtom")
        sizePolicy1.setHeightForWidth(self.importBranchSelectButtom.sizePolicy().hasHeightForWidth())
        self.importBranchSelectButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_26.addWidget(self.importBranchSelectButtom)


        self.verticalLayout_10.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_5)

        self.label_36 = QLabel(self.tab)
        self.label_36.setObjectName(u"label_36")
        sizePolicy1.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy1)

        self.horizontalLayout_48.addWidget(self.label_36)

        self.importBranchPosition = QSpinBox(self.tab)
        self.importBranchPosition.setObjectName(u"importBranchPosition")
        sizePolicy1.setHeightForWidth(self.importBranchPosition.sizePolicy().hasHeightForWidth())
        self.importBranchPosition.setSizePolicy(sizePolicy1)
        self.importBranchPosition.setMinimum(1)

        self.horizontalLayout_48.addWidget(self.importBranchPosition)

        self.label_39 = QLabel(self.tab)
        self.label_39.setObjectName(u"label_39")
        sizePolicy1.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy1)

        self.horizontalLayout_48.addWidget(self.label_39)

        self.importBranchPositionComboBox = QComboBox(self.tab)
        self.importBranchPositionComboBox.addItem("")
        self.importBranchPositionComboBox.addItem("")
        self.importBranchPositionComboBox.setObjectName(u"importBranchPositionComboBox")
        sizePolicy1.setHeightForWidth(self.importBranchPositionComboBox.sizePolicy().hasHeightForWidth())
        self.importBranchPositionComboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_48.addWidget(self.importBranchPositionComboBox)

        self.importBranchCheckBox = QCheckBox(self.tab)
        self.importBranchCheckBox.setObjectName(u"importBranchCheckBox")
        sizePolicy1.setHeightForWidth(self.importBranchCheckBox.sizePolicy().hasHeightForWidth())
        self.importBranchCheckBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_48.addWidget(self.importBranchCheckBox)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_44)


        self.verticalLayout_10.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.importBranchGerateButtom = QPushButton(self.tab)
        self.importBranchGerateButtom.setObjectName(u"importBranchGerateButtom")
        sizePolicy1.setHeightForWidth(self.importBranchGerateButtom.sizePolicy().hasHeightForWidth())
        self.importBranchGerateButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_51.addWidget(self.importBranchGerateButtom)

        self.inputFromNet = QPushButton(self.tab)
        self.inputFromNet.setObjectName(u"inputFromNet")
        sizePolicy1.setHeightForWidth(self.inputFromNet.sizePolicy().hasHeightForWidth())
        self.inputFromNet.setSizePolicy(sizePolicy1)

        self.horizontalLayout_51.addWidget(self.inputFromNet)


        self.verticalLayout_10.addLayout(self.horizontalLayout_51)

        self.line_5 = QFrame(self.tab)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line_5)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_37 = QLabel(self.tab)
        self.label_37.setObjectName(u"label_37")
        sizePolicy1.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy1)
        self.label_37.setFont(font)

        self.horizontalLayout_52.addWidget(self.label_37)


        self.verticalLayout_10.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_38 = QLabel(self.tab)
        self.label_38.setObjectName(u"label_38")
        sizePolicy1.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy1)

        self.horizontalLayout_36.addWidget(self.label_38)

        self.exportBranchFileUrl = QLineEdit(self.tab)
        self.exportBranchFileUrl.setObjectName(u"exportBranchFileUrl")

        self.horizontalLayout_36.addWidget(self.exportBranchFileUrl)

        self.exportBranchSelectButtom = QPushButton(self.tab)
        self.exportBranchSelectButtom.setObjectName(u"exportBranchSelectButtom")
        sizePolicy1.setHeightForWidth(self.exportBranchSelectButtom.sizePolicy().hasHeightForWidth())
        self.exportBranchSelectButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_36.addWidget(self.exportBranchSelectButtom)


        self.verticalLayout_10.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_45)

        self.label_40 = QLabel(self.tab)
        self.label_40.setObjectName(u"label_40")
        sizePolicy1.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy1)

        self.horizontalLayout_49.addWidget(self.label_40)

        self.exportBranchComboBox = QComboBox(self.tab)
        self.exportBranchComboBox.setObjectName(u"exportBranchComboBox")

        self.horizontalLayout_49.addWidget(self.exportBranchComboBox)

        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_48)


        self.verticalLayout_10.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.exportBranchGeneraButtom = QPushButton(self.tab)
        self.exportBranchGeneraButtom.setObjectName(u"exportBranchGeneraButtom")
        sizePolicy1.setHeightForWidth(self.exportBranchGeneraButtom.sizePolicy().hasHeightForWidth())
        self.exportBranchGeneraButtom.setSizePolicy(sizePolicy1)

        self.horizontalLayout_53.addWidget(self.exportBranchGeneraButtom)

        self.exportToNet = QPushButton(self.tab)
        self.exportToNet.setObjectName(u"exportToNet")
        sizePolicy1.setHeightForWidth(self.exportToNet.sizePolicy().hasHeightForWidth())
        self.exportToNet.setSizePolicy(sizePolicy1)

        self.horizontalLayout_53.addWidget(self.exportToNet)


        self.verticalLayout_10.addLayout(self.horizontalLayout_53)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_6.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.head2_2.setText(QCoreApplication.translate("MainWindow", u"\u589e\u52a0\u5757", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u6240\u5728\u5206\u652f\u540d\u79f0", None))
        self.addBlockExampleButtom.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u4f8b", None))
        self.addBlockClearButtom.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5f15\u7528\u5e93\u540d\u79f0", None))
        self.addBlockLibName.setInputMask("")
        self.addBlockLibName.setText("")
        self.addBlockLibName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5982\uff1acontrol ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5f15\u7528\u7c7b\u540d\u79f0", None))
        self.addBlockClassName.setInputMask("")
        self.addBlockClassName.setText("")
        self.addBlockClassName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5982\uff1ashijue1", None))
        self.addBlockColorButtom.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5757\u7684\u989c\u8272", None))
        self.addBlockColorCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u9ed8\u8ba4\u989c\u8272", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5757\u7684\u521b\u5efa\u4f4d\u7f6e\u5728\u7b2c", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u4e2a\u5757", None))
        self.addBlockPositionComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4e4b\u524d", None))
        self.addBlockPositionComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e4b\u540e", None))

        self.addBlockPositionCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u653e\u5728\u6700\u540e", None))
        self.addBlockConnectCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u4e0a\u4e0b\u63a5", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7801", None))
        self.addBlockCodeTextEdit.setPlainText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u5757\u7684\u5185\u5bb9", None))
        self.addBlockContentTextEdit.setPlainText("")
        self.addBlockGeneraButtom.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u751f\u6210\u7f16\u7a0b\u5757", None))
        self.addBlockBackButtom.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de\u5230\u4e0a\u4e00\u6b65", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Block), QCoreApplication.translate("MainWindow", u"\u589e\u52a0\u5757", None))
        self.head2_4.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5757", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u6240\u5728\u5206\u652f\u540d\u79f0", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u7b2c", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u4e2a\u5757", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u540e\u7684\u5f15\u7528\u5e93\u540d\u79f0\u4e3a", None))
        self.modifyBlockLibName.setInputMask("")
        self.modifyBlockLibName.setText("")
        self.modifyBlockLibName.setPlaceholderText("")
        self.modifyBlockLibCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u4fee\u6539", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u540e\u7684\u5f15\u7528\u7c7b\u540d\u79f0\u4e3a", None))
        self.modifyBlockClassName.setInputMask("")
        self.modifyBlockClassName.setText("")
        self.modifyBlockClassName.setPlaceholderText("")
        self.modifyBlockClassCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u4fee\u6539", None))
        self.modifyBlockColorButtom.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u540e\u5757\u7684\u989c\u8272\u4e3a", None))
        self.modifyBlockColorCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u4fee\u6539", None))
        self.modifyBlockConnectCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u4fee\u6539\u5757\u7684\u5f62\u72b6", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u540e\u7684\u4ee3\u7801", None))
        self.modifyBlockCodeTextEdit.setPlainText("")
        self.modifyBlockCodeCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u4fee\u6539", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u540e\u7684\u5757\u7684\u5185\u5bb9", None))
        self.modifyBlockContentTextEdit.setPlainText("")
        self.modifyBlockContentCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u4fee\u6539", None))
        self.modifyBlockModifyButtom.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u7f16\u7a0b\u5757", None))
        self.head2_3.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5757", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u6240\u5728\u5206\u652f\u540d\u79f0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8981\u5220\u9664\u7684\u5757\u662f\u7b2c\u51e0\u4e2a", None))
        self.deleteBlockDeleteButtom.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5757", None))
        self.modifyBlockBackButtom.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de\u5230\u4e0a\u4e00\u6b65", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u4fee\u6539/\u5220\u9664\u5757", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u589e\u52a0\u6807\u7b7e", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u6240\u5728\u5206\u652f\u540d\u79f0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u6807\u7b7e\u7684\u521b\u5efa\u4f4d\u7f6e\u5728\u7b2c", None))
        self.addLabelPositionComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4e4b\u524d", None))
        self.addLabelPositionComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e4b\u540e", None))

        self.addLabelPositionCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u653e\u5728\u6700\u540e\u9762", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u6807\u7b7e\u5185\u5bb9:", None))
        self.addLabelGenraButtom.setText(QCoreApplication.translate("MainWindow", u"\u589e\u52a0\u6807\u7b7e", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u6807\u7b7e", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u6240\u5728\u5206\u652f\u540d\u79f0:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u8981\u5220\u9664\u7684\u6807\u7b7e\u662f\u7b2c\u51e0\u4e2a", None))
        self.deleteLabelDeleteButtom.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u6807\u7b7e", None))
        self.addLabelBackButtom.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de\u4e0a\u4e00\u6b65", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u589e/\u5220\u6807\u7b7e", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u589e\u52a0\u5927\u5206\u652f", None))
        self.addBigBrachColorButtom.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5206\u652f\u989c\u8272", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5206\u652f\u521b\u5efa\u4f4d\u7f6e\u5728\u7b2c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u4e2a\u5927\u5206\u652f", None))
        self.addBigBrachPotionComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4e4b\u524d", None))
        self.addBigBrachPotionComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e4b\u540e", None))

        self.addBigBrachPotionCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u653e\u5728\u6700\u540e\u9762", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5206\u652f\u540d\u5b57:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u7ed9\u8fd9\u4e2a\u5206\u652f\u4e00\u4e2a\u82f1\u6587\u540d:", None))
        self.addBigBrachNameCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u968f\u673a\u53d6\u540d", None))
        self.addBigBrachNameButtom.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u751f\u6210\u5927\u5206\u652f", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5927\u5206\u652f", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u7684\u5927\u5206\u652f\u7684\u540d\u5b57", None))
        self.deleteBigBranchButtom.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5927\u5206\u652f", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5927\u5206\u652f\u4f4d\u7f6e", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u4ee4\u5927\u5206\u652f", None))
        self.modifyBranchPositionComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4e0a\u79fb", None))
        self.modifyBranchPositionComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e0b\u79fb", None))

        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u4e2a\u5355\u4f4d", None))
        self.modifyBranchPositionButtom.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5927\u5206\u652f\u4f4d\u7f6e", None))
        self.deleteBlockBackButtom.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de\u5230\u4e0a\u4e00\u6b65", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u589e/\u5220\u5927\u5206\u652f", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u589e\u52a0\u5c0f\u5206\u652f", None))
        self.addSmallBrachColorButtom.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5206\u652f\u989c\u8272", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u5206\u652f\u521b\u5efa\u5728", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u7684\u7b2c", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u4e2a\u4f4d\u7f6e", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u5206\u652f\u540d\u5b57", None))
        self.addSmallBrachGeneraButtom.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u751f\u6210\u5c0f\u5206\u652f", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5c0f\u5206\u652f", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u6240\u5728\u5927\u5206\u652f\u540d\u79f0:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u8981\u5220\u9664\u7684\u5c0f\u5206\u652f\u540d\u5b57", None))
        self.deleteSmallBranchButtom.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5c0f\u5206\u652f", None))
        self.addSmallBrachBackButtom.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de\u4e0a\u4e00\u6b65", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"\u589e/\u5220\u5c0f\u5206\u652f", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u5927\u5206\u652f", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u5206\u652f\u6587\u4ef6\u5939\uff1a", None))
        self.importBranchSelectButtom.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u5927\u5206\u652f\u653e\u5728\u7b2c", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u4e2a\u5927\u5206\u652f", None))
        self.importBranchPositionComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4e4b\u540e", None))
        self.importBranchPositionComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e4b\u524d", None))

        self.importBranchCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u653e\u5230\u6700\u540e\u9762", None))
        self.importBranchGerateButtom.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5bfc\u5165\u5927\u5206\u652f", None))
        self.inputFromNet.setText(QCoreApplication.translate("MainWindow", u"\u4ece\u5b98\u7f51\u4e2d\u5bfc\u5165", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u5927\u5206\u652f", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u4f4d\u7f6e\uff1a", None))
        self.exportBranchSelectButtom.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u7684\u5927\u5206\u652f\u7684\u540d\u5b57", None))
        self.exportBranchGeneraButtom.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5bfc\u51fa\u5927\u5206\u652f", None))
        self.exportToNet.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u5230\u5b98\u7f51", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u5bfc\u5165/\u5bfc\u51fa\u5927\u5206\u652f", None))
    # retranslateUi

