# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FP_Window2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
player_connect=sqlite3.connect("Final_project.db")
player_cursor=player_connect.cursor()

class Ui_secondWindow(object):
    def setupUi(self, secondWindow):
        secondWindow.setObjectName("secondWindow")
        secondWindow.resize(600, 400)
        self.label = QtWidgets.QLabel(secondWindow)
        self.label.setGeometry(QtCore.QRect(150, 10, 281, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(secondWindow)
        self.line.setGeometry(QtCore.QRect(20, 60, 561, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(secondWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 110, 561, 271))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.player_names = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.player_names.setFont(font)
        self.player_names.setObjectName("player_names")
        self.horizontalLayout.addWidget(self.player_names)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.player_points = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.player_points.setFont(font)
        self.player_points.setObjectName("player_points")
        self.horizontalLayout.addWidget(self.player_points)
        self.label_2 = QtWidgets.QLabel(secondWindow)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(secondWindow)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(330, 80, 171, 25))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.team_points = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.team_points.setFont(font)
        self.team_points.setObjectName("team_points")
        self.horizontalLayout_2.addWidget(self.team_points)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(secondWindow)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(160, 40, 271, 25))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.teamname_label = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.teamname_label.setFont(font)
        self.teamname_label.setObjectName("teamname_label")
        self.horizontalLayout_3.addWidget(self.teamname_label)

        self.retranslateUi(secondWindow)
        QtCore.QMetaObject.connectSlotsByName(secondWindow)

        #my lines
        self.show_playernames()
        self.show_teamname()
        self.show_teampoints()
        self.show_playerpoints()
        
    def retranslateUi(self, secondWindow):
        _translate = QtCore.QCoreApplication.translate
        secondWindow.setWindowTitle(_translate("secondWindow", "Form"))
        self.label.setText(_translate("secondWindow", "Evaluate performance of your fantasy team"))
        self.label_2.setText(_translate("secondWindow", "Players"))
        self.label_3.setText(_translate("secondWindow", "Points"))
        self.label_4.setText(_translate("secondWindow", "Team Name"))

    #my lines        
    def show_playernames(self):
        try:
            player_cursor.execute("SELECT Players FROM teams;")
            players=player_cursor.fetchall()
            for player in players:
                self.player_names.addItem(player[0])
        except sqlite3.Error as e:
            failure_msg = QMessageBox()
            failure_msg.setWindowTitle("Failure!")
            failure_msg.setText(f"Error in adding the team players! {e}")
            failure_msg.setIcon(QMessageBox.Critical)
            failure_msg.exec_()

    def show_teamname(self):
        try:
            player_cursor.execute("SELECT Name FROM teams WHERE Name!='None';")
            name=str(player_cursor.fetchall())
            self.teamname_label.setText(name.strip("[]").strip("()").strip("','"))
        except sqlite3.Error as e:
            failure_msg = QMessageBox()
            failure_msg.setWindowTitle("Failure!")
            failure_msg.setText(f"Error in showing the team name! {e}")
            failure_msg.setIcon(QMessageBox.Critical)
            failure_msg.exec_()

    def show_teampoints(self):
        try:
            player_cursor.execute("SELECT Value FROM teams;")
            points=player_cursor.fetchall()
            total_points = 0
            for point in points:
                if point[0] is not None:
                    total_points += point[0]
            self.team_points.setText(str(total_points))
        except sqlite3.Error as e:
            failure_msg = QMessageBox()
            failure_msg.setWindowTitle("Failure!")
            failure_msg.setText(f"Error in showing the team points! {e}")
            failure_msg.setIcon(QMessageBox.Critical)
            failure_msg.exec_()
        
    def show_playerpoints(self):
        try:
            player_cursor.execute("SELECT Value FROM teams;")
            points=player_cursor.fetchall()
            for point in points:
                if str(point[0])!="None":
                    self.player_points.addItem(str(point[0]))
        except sqlite3.Error as e:
            failure_msg = QMessageBox()
            failure_msg.setWindowTitle("Failure!")
            failure_msg.setText(f"Error in adding the team players' points! {e}")
            failure_msg.setIcon(QMessageBox.Critical)
            failure_msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    secondWindow = QtWidgets.QWidget()
    ui = Ui_secondWindow()
    ui.setupUi(secondWindow)
    secondWindow.show()
    sys.exit(app.exec_())
