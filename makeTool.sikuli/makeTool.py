import java
import sys
from javax.swing import JFrame
from javax.swing import JButton
from javax.swing import JPanel
from javax.swing import BoxLayout
from java.awt import EventQueue
from java.lang import *

from java.util import Timer
from java.util import TimerTask

from threading import Thread
import random

items = 3

class ToolFrame(java.lang.Runnable):
    def run(self):
        frame = JFrame('MainFrame', defaultCloseOperation = JFrame.DISPOSE_ON_CLOSE)
        self.addButtons(frame.getContentPane())
        frame.size = (300, 175)
        frame.visible = 1 

        self.frame = frame

    def addButtons(self, container):
        pane = JPanel()
        pane.layout = BoxLayout(pane, BoxLayout.Y_AXIS)

        pane.add(JButton(u"附加屬性", actionPerformed = self.task1))

        container.add(pane)

    def task1(self):
        global items
        while (items > 0):
            if exists("1461368954522.png"):
                doubleClick(Pattern("1461368990463.png").similar(0.80))
                doubleClick(Pattern("1461369010638.png").similar(0.80))
                wait("1461369086629.png", 2)
                click(Pattern("1461369086629.png").similar(0.80).targetOffset(-65,7))
                wait(3)
                
                items -= 1  
                
            
            
            
        
        

    def stop(self):
        self.dispose()

    def __del__(self):
        print('Deconstructor')

if __name__ == '__main__':
     EventQueue.invokeLater(ToolFrame())