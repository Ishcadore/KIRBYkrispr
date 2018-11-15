import mysql.connector
import tkinter as tk
from tkinter import *
import datetime
from datetime import *

from os import path
import sys
sys.path.append(path.abspath("C:/Users/Johnsi3/Desktop/comp sci/PyProjects"))

import tkcalendar

################################################################################################
#cnx = mysql.connector.connect(user='root', password='drowssap',
#                              host='127.0.0.1',
#                              database='fruitdb')
#cursor = cnx.cursor()
##numrows = cur.execute("SELECT first_name FROM users")


#add_household = ("INSERT INTO household "
#               "(last_name, street, city, state, zip, date_entered, house_id) "
#               "VALUES (%s, %s, %s, %s, %s, %s, %s)")
#data_household = ('Johnson', 'Foxchase', 'Doylestown', 'PA', 18901, date(2018, 10, 31), 100)
#data_household1 = ('Mitnick', 'Bitchcity', 'Mahwah', 'NJ', 26319, date(2018, 11, 7), 101)
## Insert new household
#households = [data_household, data_household1]
###
#listData = []

data_household = ('Johnson', 'Foxchase', 'Doylestown', 'PA', 18901, date(2018, 10, 31), 100)
data_household1 = ('Mitnick', 'Bitchcity', 'Mahwah', 'NJ', 26319, date(2018, 11, 7), 101)
households = [data_household, data_household1]

def switchHouse(num):
    
    #cursor.execute(add_household, households[num])
    #emp_no = cursor.lastrowid
    ## Print results
    ##cursor.execute("SELECT * FROM household")
    #cursor.execute("SELECT * FROM household")
    #result_set = cursor.fetchone()
    info = []
    #for row in result_set:
    for row in households[num]:
        info.append(row)
        print ("%s" % (row))
    return (info)


def showData():
    print('%s' % listData)
    return listData            
#---
listData = switchHouse(1)
showData()
listData = switchHouse(0)
showData()
#---
def view(data):
    label = tk.Label(root, text='%s' % (data))
    label.pack()

##app part
class Application(tk.Frame):
    def say_hi(self, x):
        print("%s" % x)   
    
    def greet(self):
        q = showData()
        #self.label = Label(text=showData())
        #self.label.pack()
        w = Message(text=q)
        w.pack()
        
    def foodMenu(self, fruit):
        if(fruit== "Banana"):
            print("Banana")
        else:
            print("%s" % fruit)
            a = Message(text=fruit)
            a.pack()
        #frame.bind("<Button-3>", popup)    

    def createWidgets(self, master):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        #self.QUIT["bg"]   = "#8EF0F7"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "show",
        self.hi_there["command"] = lambda: switchHouse(0)
        #something here to update global variable

        self.hi_there.pack({"side": "left"})
        
        #self.view = Button(self)
        #self.view["text"] = "view",
        #self.view["command"] = lambda: view(listData)

        #self.view.pack({"side": "left"})      
        ##
        self.label = Label(master, text="Show Contents of CrisperDraw")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()
                

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        ##Alternative in sperate window : win = Toplevel(master)
        win = self.master
        
        self.menu = Menu(master, tearoff=0)
        #root.option_add('*tearOff', FALSE)
        #master.config(menu=menu)
        #menubar = Menu(win)
        menubar = Menu(master)
        #win['menu'] = menubar
        
        
        menu_file = Menu(menubar)
        menu_edit = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')
        menubar.add_cascade(menu=menu_edit, label='Edit')        
        menu_file.add_command(label='New', command=self.greet)
        menu_file.add_command(label='Open...', command=self.greet)
        menu_file.add_command(label='Close', command=self.greet)               
        menu_file.add_command(label="Strawberries", command=lambda: self.foodMenu("Strawberries"))
        menu_file.add_command(label="Spinach", command=lambda: self.foodMenu("Spinach")) 
        
        menu_edit.add_command(label="view", command=lambda: view(listData))
                              
        self.food_button = Button(master, text="Food Menu", command=lambda: self.foodMenu("Banana"))
        self.food_button.pack()         
        
        
               

    def __init__(self, frame, master):
        self.master = master
        super(Application, self).__init__()
        #tk.Frame.__init__(self, master)
        self.createWidgets(master)
        
        #x = tkcalendar
        #x.test()
        #x._today()

        self.pack()
def test(frame, parent):
    fruity = Application(frame, parent)
    fruity.pack()
if __name__ == '__main__':
    root = tk.Tk()
    root.title("My Refrigerator")
    tk.Frame.__init__(root)
    frame = tk.Frame(root,  width=480, height=180)    
    test(frame, root)

#cnx.close()
