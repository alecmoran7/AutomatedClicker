from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication, QPushButton 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import clickUI
import random
import pyautogui, time


class clickMacro(QtWidgets.QMainWindow, clickUI.Ui_MainWindow):
    allTimes = []
    allPositions = []
    nextPosition = None
    nextTime = None
    all_x_positions = []
    all_y_positions = []
    waitForSeconds = 3

    def __init__(self, parent = None):
        super(clickMacro, self).__init__(parent)
        self.setupUi(self)
        self.executeButton.clicked.connect(self.executeHandler)                     # Button - Execute
        self.clearListButton.clicked.connect(self.clearListHandler)                 # Button - Clear List
        self.loadButton.clicked.connect(self.loadHandler)                           # Button - Load
        self.saveButton.clicked.connect(self.saveHandler)                           # Button - Save
        self.secondSelector.valueChanged.connect(self.secondHandler)                # Numerical selector - Seconds
        self.positionButton.clicked.connect(self.positionHandler)                   # Button - Select Position 
        self.clearPositionButton.clicked.connect(self.clearPositionHandler)         # Button - Clear Position 
        self.scheduleSelector.dateTimeChanged.connect(self.scheduleSelectorHandler) # Button - Select Position 
        self.addToScheduleButton.clicked.connect(self.addToScheduleHandler)         # Button - Add to Schedule
        self.scheduleTable.setColumnCount(2)
        self.scheduleTable.setColumnWidth(0, 155)
        self.scheduleTable.setColumnWidth(1, 170)
        self.scheduleTable.setHorizontalHeaderLabels(["Time", "Mouse Position"])
        

    def executeHandler(self):
        pass

    def clearListHandler(self):
        pass

    def loadHandler(self):
        pass

    def saveHandler(self):
        pass

    def secondHandler(self):
        self.waitForSeconds = self.secondSelector.value()
        print("waitForTime changed to " + str(self.waitForSeconds) + " seconds.")
        pass

    def positionHandler(self):
        print("Sleeping for " + str(self.waitForSeconds) + " seconds.")
        time.sleep(self.waitForSeconds)
        self.nextPosition = pyautogui.position()
        # self.allPositions.append(nextPosition)
        self.positionDisplay.setText(str(self.nextPosition).replace("Point",""))
        pass

    def clearPositionHandler(self):
        self.positionDisplay.setText("N/A")
        self.nextTime = None
        pass

    def scheduleSelectorHandler(self):
        print("Selected time is: " + str(self.scheduleSelector.dateTime()))
        selectedTime = str(self.scheduleSelector.dateTime()).replace(' ','').split(',')
        print("Time array: " + str(selectedTime))
        s_hour = selectedTime[3]
        s_minute = selectedTime[4]
        s_month = selectedTime[1]
        s_day = selectedTime[2]
        self.nextTime = s_month + "/" + s_day + " @ " + s_hour + ":" + s_minute
        print("Selected time is " + self.nextTime)
        pass

    def addToScheduleHandler(self):
        if (self. nextTime is not None and self.nextPosition is not None):
            self.allPositions.append(self.nextPosition)
            self.allTimes.append(self.nextTime)
            nextRowNum = self.scheduleTable.rowCount()
            self.scheduleTable.insertRow(nextRowNum)
            self.scheduleTable.setItem(nextRowNum, 0, QtWidgets.QTableWidgetItem(str(self.nextTime)))
            self.scheduleTable.setItem(nextRowNum, 1, QtWidgets.QTableWidgetItem(str(self.nextPosition).replace("Point","")))
            self.scheduleTable.show()
        pass

def main():
    app = QApplication(sys.argv)
    form = clickMacro()
    form.show()
    app.exec()

if __name__ == '__main__':
    main()
