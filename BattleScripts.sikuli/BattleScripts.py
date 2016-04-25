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

mode = 0
mouse_pos = None

alliance_pos = [
        Location(1194, 592)
        #Location(1097, 613), Location(1194, 592),Location(1291, 576), #1
        #Location(1149, 670),Location(1267, 646),Location(1362, 622),  #2
        ]
enemy_pos = [
        Location(899, 519),Location(1007, 502),Location(1108, 492),Location(1202, 481),Location(1286, 465), #1
        Location(868, 457),Location(964, 454),Location(1047, 443),Location(1130, 434),Location(1201, 426), #2
        Location(850, 421),Location(934, 417),Location(1003, 409),Location(1035, 400),Location(1100, 395) #3
        ]
# Check app pos, Left, Bottom, Right, Top
check_pos = Location(1156, 596)
check_teamviewer = 0
check_battle = 0

kCountBattle = 1500
kCountTeamviewer = 15

class BattleTask(TimerTask):
    def run(self):
        global mode
        global check_teamviewer, check_battle
        #print("Timer task fired.")
        
        if check_teamviewer > 0:
            check_teamviewer -= 1
        if check_teamviewer > 0 and exists("1460954429422.png"):
            click(Pattern("1460954429422.png").targetOffset(190,53))
                        
            
        if mode <= 0:
            return

        if check_battle > 0:
            check_battle -= 1
            #print("check_battle: %d" % check_battle)
            
        if check_battle > 0 and exists("1460584421757.png"):
            self.battleMode()
        
    def battleMode(self):
        if mode == 2: #Alliance
            #print('Alliance mode')
            a = random.choice(alliance_pos)
            click(a)
        elif mode == 1: #Enemy
            #print('Enemy mode')
            b = random.sample(enemy_pos, 5)
            for a in b: 
                click(a)
        elif mode == 4: #Get current mouse pos
            global mouse_pos
            #print('Current mouse pos')
            if mouse_pos:
                click(mouse_pos)
            else:
                mouse_pos = Env.getMouseLocation()
        else:
            #print('In battle, do nothing')
            pass       
class MainFrame(java.lang.Runnable):
    def __init__(self):
        self.timer = None
        self.frame = None
        
    def run(self):
        frame = JFrame('MainFrame', defaultCloseOperation = JFrame.DISPOSE_ON_CLOSE)
        self.addButtons(frame.getContentPane())
        frame.size = (300, 175)
        frame.visible = 1 

        self.frame = frame
        self.startTimerTask()
    
    def startTimerTask(self):
        if self.timer:
            self.timer.cancel()
        
        self.timer = Timer()
        self.timer.schedule(BattleTask(), 100, 5000)

    def stopTimerTask(self):
        if self.timer:
            self.timer.cancel()

    def addButtons(self, container):
        pane = JPanel()
        pane.layout = BoxLayout(pane, BoxLayout.Y_AXIS)
        pane.add(JButton("Alliance", actionPerformed=self.clickAlliance))
        pane.add(JButton("Enemy", actionPerformed=self.clickEnemy))
        pane.add(JButton("None", actionPerformed=self.noMode))
        pane.add(JButton("CheckPos", actionPerformed=self.checkPos))
        pane.add(JButton("GetMousePos", actionPerformed=self.getCurrentPos))
        pane.add(JButton("Exit", actionPerformed=self.stop))
        container.add(pane)
                    
    mode = 0 
    def clickAlliance(self, event):
        '''Click self hero or ...'''
        print('Click Alliance')
        global mode, check_teamviewer, check_battle
        check_teamviewer = kCountTeamviewer
        check_battle = kCountBattle
        
        mode = 2

    def clickEnemy(self, event):
        '''Click enemy'''
        global mode, check_teamviewer, check_battle
        check_teamviewer = kCountTeamviewer
        check_battle = kCountBattle
          
        print('Click enemy')
        mode = 1 

    def noMode(self,event):
        global mode, check_teamviewer, check_battle
        
        check_teamviewer = 0
        check_battle = 0
        mode = 0
        print('No mode')

    def checkPos(self,event):
        global mode
        mode = 0
        mouseMove(check_pos)
        
    def getCurrentPos(self, event):
        global mode
        print('Start to Get mouse pos')
        mode = 4
        Thread.sleep(3000)
        print('Get mouse pos')
        mouse_pos = Env.getMouseLocation()
        print('Current mouse pos: x:' + mouse_pos.x + ' y:' + mouse_pos.y)

    def stop(self, event):
        if self.timer:
            self.timer.cancel()
        self.frame.dispose()
        self.dispose()

    def __del__(self):
        if self.timer:
            self.timer.cancel()
            
        print('Deconstructor')
                                
if __name__ == '__main__':
    EventQueue.invokeLater(MainFrame())