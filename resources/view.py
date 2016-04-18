# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Mon Apr 18 20:45:27 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainView(object):
    def setupUi(self, MainView):
        MainView.setObjectName("MainView")
        MainView.resize(792, 480)
        self.centralwidget = QtGui.QWidget(MainView)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        MainView.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuWindows = QtGui.QMenu(self.menubar)
        self.menuWindows.setObjectName("menuWindows")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainView.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainView)
        self.statusbar.setObjectName("statusbar")
        MainView.setStatusBar(self.statusbar)
        self.open = QtGui.QAction(MainView)
        self.open.setObjectName("open")
        self.save = QtGui.QAction(MainView)
        self.save.setObjectName("save")
        self.save_as = QtGui.QAction(MainView)
        self.save_as.setObjectName("save_as")
        self.actionNew = QtGui.QAction(MainView)
        self.actionNew.setObjectName("actionNew")
        self.actionCopy_as = QtGui.QAction(MainView)
        self.actionCopy_as.setObjectName("actionCopy_as")
        self.actionExit = QtGui.QAction(MainView)
        self.actionExit.setObjectName("actionExit")
        self.insert_row = QtGui.QAction(MainView)
        self.insert_row.setObjectName("insert_row")
        self.actionInsert_into_databse = QtGui.QAction(MainView)
        self.actionInsert_into_databse.setObjectName("actionInsert_into_databse")
        self.actionDatabase_Credentials = QtGui.QAction(MainView)
        self.actionDatabase_Credentials.setObjectName("actionDatabase_Credentials")
        self.actionSave_config = QtGui.QAction(MainView)
        self.actionSave_config.setObjectName("actionSave_config")
        self.actionLoad_Config = QtGui.QAction(MainView)
        self.actionLoad_Config.setObjectName("actionLoad_Config")
        self.actionUndo = QtGui.QAction(MainView)
        self.actionUndo.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtGui.QAction(MainView)
        self.actionRedo.setObjectName("actionRedo")
        self.menuFile.addAction(self.open)
        self.menuFile.addAction(self.save)
        self.menuFile.addAction(self.save_as)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopy_as)
        self.menuEdit.addAction(self.insert_row)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionInsert_into_databse)
        self.menuEdit.addAction(self.actionDatabase_Credentials)
        self.menuEdit.addAction(self.actionSave_config)
        self.menuEdit.addAction(self.actionLoad_Config)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainView)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), MainView.close)
        QtCore.QMetaObject.connectSlotsByName(MainView)

    def retranslateUi(self, MainView):
        MainView.setWindowTitle(QtGui.QApplication.translate("MainView", "asd", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setStatusTip(QtGui.QApplication.translate("MainView", "asdasdasd", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainView", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainView", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuWindows.setTitle(QtGui.QApplication.translate("MainView", "Windows", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainView", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.open.setText(QtGui.QApplication.translate("MainView", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.open.setStatusTip(QtGui.QApplication.translate("MainView", "Open File", None, QtGui.QApplication.UnicodeUTF8))
        self.open.setShortcut(QtGui.QApplication.translate("MainView", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.save.setText(QtGui.QApplication.translate("MainView", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.save.setStatusTip(QtGui.QApplication.translate("MainView", "Save file", None, QtGui.QApplication.UnicodeUTF8))
        self.save.setShortcut(QtGui.QApplication.translate("MainView", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.save_as.setText(QtGui.QApplication.translate("MainView", "Save as", None, QtGui.QApplication.UnicodeUTF8))
        self.save_as.setStatusTip(QtGui.QApplication.translate("MainView", "Save file with specific name", None, QtGui.QApplication.UnicodeUTF8))
        self.save_as.setShortcut(QtGui.QApplication.translate("MainView", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainView", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setStatusTip(QtGui.QApplication.translate("MainView", "New file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("MainView", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy_as.setText(QtGui.QApplication.translate("MainView", "Copy CS", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy_as.setStatusTip(QtGui.QApplication.translate("MainView", "Copy Create Script", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainView", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setStatusTip(QtGui.QApplication.translate("MainView", "Exit program", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainView", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.insert_row.setText(QtGui.QApplication.translate("MainView", "Insert Row", None, QtGui.QApplication.UnicodeUTF8))
        self.insert_row.setShortcut(QtGui.QApplication.translate("MainView", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsert_into_databse.setText(QtGui.QApplication.translate("MainView", "Insert into database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDatabase_Credentials.setText(QtGui.QApplication.translate("MainView", "Database Credentials", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_config.setText(QtGui.QApplication.translate("MainView", "Save config", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Config.setText(QtGui.QApplication.translate("MainView", "Load Config", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setText(QtGui.QApplication.translate("MainView", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setShortcut(QtGui.QApplication.translate("MainView", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setText(QtGui.QApplication.translate("MainView", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setShortcut(QtGui.QApplication.translate("MainView", "Ctrl+Y", None, QtGui.QApplication.UnicodeUTF8))

