import java
import sys
from javax.swing import JFrame
from javax.swing import JButton
from javax.swing import JPanel
from javax.swing import BoxLayout
from java.awt import *
from java.lang import *

from java.util import Timer
from java.util import TimerTask

from threading import Thread
import random

g_item_region = Region(632,119,498,780)
g_item_count_default = 3600 
g_item_count = 0

g_panel_region = Region(1189,300,517,419)

running = True
check_teamviewer = False

teamviewer_count = 0
teamviewer_image = Pattern("1460954429422.png").targetOffset(190,58)

g_task1_pattern = None
g_task2_pattern = None
g_task_list = None

g_act_count_default = 20

class ToolFrame(java.lang.Runnable):
    def run(self):
        self.frame = frame = JFrame('MainFrame', defaultCloseOperation = JFrame.DISPOSE_ON_CLOSE)
        self.addButtons(frame.getContentPane())
        frame.size = (180, 450)
        frame.visible = 1 

        self.frame = frame

    def addButtons(self, container):
        pane = JPanel()
        pane.layout = BoxLayout(pane, BoxLayout.Y_AXIS)
        
        pane.add(JButton(u"R1", actionPerformed = self.task1))
        pane.add(JButton(u"R2", actionPerformed = self.task2))
        pane.add(JButton(u"R3", actionPerformed = self.task3))
        pane.add(JButton(u"R4", actionPerformed = self.task4))
        pane.add(JButton(u"R5", actionPerformed = self.task5))
        pane.add(JButton(u"2 Items", actionPerformed = self.taskAA2))
        pane.add(JButton(u"3 Items", actionPerformed = self.taskAA3))
        pane.add(JButton(u"開拓", actionPerformed = self.taskA3))
        pane.add(JButton(u"Stop", actionPerformed = self.stop))
        pane.add(JButton(u"Exit", actionPerformed = self.quit))
        container.add(pane)

    def doTask(self, target):
        global running, g_item_count, teamviewer_count
        running = True
        g_item_count = g_item_count_default
        
        if check_teamviewer:
            teamviewer_count = 120
        task = Thread(target=target)
        task.start()

    def task1(self, event):
        global g_task1_pattern, g_act_count_default
        g_act_count_default = 20
        item1 = Pattern("item1.png").similar(0.80)
        
        g_task1_pattern = item1
        
        self.doTask(my_task1)

    def task2(self, event):
        global g_task1_pattern, g_act_count_default
        g_act_count_default = 20
        item2 = Pattern("item2.png").similar(0.80)
        g_task1_pattern = item2
        
        self.doTask(my_task1)

    def task3(self, event):
        global g_task1_pattern, g_act_count_default
        g_act_count_default = 20
        item3 = Pattern("item3.png").similar(0.85)
        g_task1_pattern = item3
        
        self.doTask(my_task1)

    def task4(self, event):
        global g_task1_pattern, g_act_count_default
        g_act_count_default = 20
        item4 = Pattern("item4.png").similar(0.85)
        
        g_task1_pattern = item4
        
        self.doTask(my_task1)

    def task5(self, event):
        global g_task1_pattern, g_act_count_default
        g_act_count_default = 20
        item5 = Pattern("item5.png").similar(0.80)
        g_task1_pattern = item5
        
        self.doTask(my_task1)
    
    def taskAA2(self, event):
        global g_task1_pattern, g_task2_pattern, g_task_list 
        global g_act_count_default 
        g_act_count_default = 20
        mk1 = Pattern("mk1.png").similar(0.85)
        mk2 = Pattern("1461888623122.png").similar(0.85)
        g_task1_pattern = mk1
        g_task2_pattern = mk2
        g_task_list = [mk1, mk2]
        
        self.doTask(my_task2)

    def taskAA3(self, event):
        global g_task1_pattern, g_task2_pattern, g_task_list
        global g_act_count_default 
        g_act_count_default = 20
        a3mk1 = Pattern("a3mk1.png").similar(0.85).targetOffset(7,-1)
        a3mk2 = Pattern("1461888623122.png").similar(0.85)
        a3mk3 = Pattern("a3mk3.png").similar(0.85)
        g_task_list = [a3mk1, a3mk2, a3mk3]
        
        self.doTask(my_task2)

    def taskA3(self, event):
        global g_task1_pattern, g_act_count_default
        g_act_count_default = 120
        drop1 = Pattern("drop1.png").similar(0.85).targetOffset(-1,-1)
        g_task1_pattern = drop1
        
        self.doTask(my_task3)
 
    def stop(self, event):
        global running
        running = False
    
    def quit(self, event):
        global running
        running = False
        self.frame.dispose()

    def __del__(self):
        print('Deconstructor')

def stopHandler():
    global running
    running = False
    print('stopHandler')

Env.addHotkey(Key.ESC,KeyModifier.CTRL, stopHandler)

g_act_count = 0
def reset_act_count():
    global g_act_count 
    g_act_count = g_act_count_default
    
def act_count():
    global g_act_count, running, g_item_count
    g_item_count -= 1
    g_act_count -= 1
    if (g_act_count < 0 or g_item_count < 0):
        running = False

pt_temp = Location(645, 505)

def my_panel():
   
    btn = g_panel_region.exists(Pattern("1461627156036.png").similar(0.85).targetOffset(-58,8)) 
    if btn: 
        pt = btn.getTarget()        
        g_panel_region.doubleClick(pt)
        mouseMove(pt.offset(5,0))
        g_panel_region.doubleClick(pt.offset(-1,0))
        reset_act_count()
        mouseMove(pt.offset(-200,0))
        return    
    else:
        #print("4")    
        act_count()
        wait(1)

def check_teamviewer():
    global teamviewer_count
    if teamviewer_count > 0:
        teamviewer_count -= 1
        tv = exists(teamviewer_image)
        if tv:
            doubleClick(tv)
    

def my_task1():
    switchApp(u"魔力寶貝II")
    global g_item_count, g_item_region
    while (running and g_item_count > 0):
        check_teamviewer()
       
        item = g_item_region.exists(g_task1_pattern) 
        if item:
            pt = item.getTarget()
            doubleClick(pt)
            mouseMove(pt.offset(-3,0))
            doubleClick(pt.offset(2,0))
            mouseMove(pt_temp)
            reset_act_count()
            #print("1")

        if (running == False):
            break

        #print("2")
        my_panel()

def my_task2():
    switchApp(u"魔力寶貝II")
    global g_item_count, g_item_region
    while (running and g_item_count > 0):
        check_teamviewer()
        #print("000")
        for pattern in g_task_list:
            item = g_item_region.exists(pattern) 
            if item and running:
                pt = item.getTarget()
                doubleClick(pt)
                mouseMove(pt.offset(-3,0))
                doubleClick(pt.offset(2,0))
                mouseMove(pt_temp)
                reset_act_count()
                #print("001")
            #print("002")

        if (running == False):
            break

        #print("2")
        my_panel()

def my_task3():
    switchApp(u"魔力寶貝II")
    global g_item_count, g_item_region
    while (running and g_item_count > 0):
        check_teamviewer()

        for i in range(6):
            item = g_item_region.exists(g_task1_pattern) 
            if item and running:
                pt = item.getTarget()
                doubleClick(pt)
                mouseMove(pt.offset(5,0))
                doubleClick(pt.offset(3,0))
                mouseMove(pt.offset(5,0))
                doubleClick(pt.offset(-3,0))
                mouseMove(pt_temp)
                reset_act_count()
            else:
                break

        if (running == False):
            break

        #print("2")
        my_panel()

if __name__ == '__main__':
     EventQueue.invokeLater(ToolFrame())