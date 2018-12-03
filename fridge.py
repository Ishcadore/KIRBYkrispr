#Entire fridge
import tkinter as tk
from tkinter import ttk
import datetime
from datetime import *
from PIL import Image, ImageTk
import tkinter.font as tkFont

from os import path
import sys
sys.path.append(path.abspath("C:/Users/Johnsi3/Desktop/comp sci/PyProjects"))

import calendar as cal
from calendar import *

##from fruit
data_household = ('Johnson', 'Foxchase', 'Doylestown', 'PA', 18901, datetime(2018, 10, 31), 100)
data_household1 = ('Mitnick', 'Bitchcity', 'Mahwah', 'NJ', 26319, datetime(2018, 11, 7), 101)
households = [data_household, data_household1]
def switchHouse(num):
    info = []
    #for row in result_set:
    for row in households[num]:
        info.append(row)
        print ("%s" % (row))
    return (info)
def showData():
    print('%s' % listData)
    return listData
def view(data):
    label = tk.Label(root, text='%s' % (data))
    label.grid()
class Application(object):
    def say_hi(self, x):
        print("%s" % x)   
    
    def greet(self):
        q = switchHouse(0)
        #self.label = Label(text=showData())
        #self.label.pack()
        w = tk.Message(text=q)
        w.grid()
        
    def foodMenu(self, fruit):
        if(fruit== "Banana"):
            insprites = App(frame, root)
            App.createWid(insprites)
            print("Banana")
        else:
            print("%s" % fruit)
            a = tk.Message(text=fruit)
            a.grid()
        #frame.bind("<Button-3>", popup)    

    def createWidgets(self, master):
        self.QUIT = ttk.Button(frame)
        self.QUIT["text"] = "QUIT"
        #self.QUIT["bg"]   = "#8EF0F7"
        self.QUIT["command"] =  master.quit

        self.QUIT.grid({"padx": "20"})

        self.hi_there = ttk.Button(frame)
        self.hi_there["text"] = "show",
        self.hi_there["command"] = lambda: switchHouse(0)
        #something here to update global variable

        self.hi_there.grid({"padx": "40"})
        
        #self.view = Button(self)
        #self.view["text"] = "view",
        #self.view["command"] = lambda: view(listData)

        #self.view.pack({"side": "left"})      
        ##
        self.label = ttk.Label(master, text="Show Contents of CrisperDraw")
        self.label.grid()

        self.greet_button = ttk.Button(master, text="Greet", command=self.greet)
        self.greet_button.grid()
                

        self.close_button = ttk.Button(master, text="Close", command=master.quit)
        self.close_button.grid()

        ##Alternative in sperate window : win = Toplevel(master)
        win = self.master
        
        #self.menu = Menu(master, tearoff=0)
        #root.option_add('*tearOff', FALSE)
        #master.config(menu=menu)
        #menubar = Menu(win)
        menubar = tk.Menu(win)
        win['menu'] = menubar
        
        
        menu_file = tk.Menu(menubar)
        menu_edit = tk.Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')
        menubar.add_cascade(menu=menu_edit, label='Edit')        
        menu_file.add_command(label='New', command=self.greet)
        menu_file.add_command(label='Open...', command=self.greet)
        menu_file.add_command(label='Close', command=self.greet)               
        menu_file.add_command(label="Strawberries", command=lambda: self.foodMenu("Strawberries"))
        menu_file.add_command(label="Spinach", command=lambda: self.foodMenu("Spinach")) 
        menu_file.add_command(label="Banana", command=lambda: self.foodMenu("Banana")) 
        
        menu_edit.add_command(label="view", command=lambda: view(switchHouse(1)))
                              
        self.food_button = ttk.Button(master, text="Food Menu", command=lambda: self.foodMenu("Banana"))
#        #self.food_button.pack()         
        
        
               

    def __init__(self, frame, master):
        self.master = master
        
        #tk.Frame.__init__(self, master)
        self.createWidgets(master)
        
        #x = tkcalendar
        #x.test()
        #x._today()

#        #self.pack()
##Sprite Control
fruit = ""
def fruitChange():
    #fruit = k
    return "sp"
class App(object):
    def createWid(self):        
        
        self.spritesheet = tk.PhotoImage(file="%s.gif" % fruitChange())
        self.num_sprintes = 1
        self.last_img = None
        self.images = self.subimage(0, 0, 20, 20)
        self.canvas = tk.Canvas(width=48, height=32)
        self.canvas.grid()
        self.updateimage(0)          
    def subimage(self, l, t, r, b):
        dst = tk.PhotoImage()
        dst.tk.call(dst, 'copy', self.spritesheet, '-from', l, t, r, b, '-to', 0, 0)
        return dst

    def updateimage(self, sprite):
        self.canvas.delete(self.last_img)
        self.last_img = self.canvas.create_image(16, 18, image=self.images)
        root.after(100, self.updateimage, (sprite+1) % self.num_sprintes)
    def _get_image(self):
        self.spritesheet = tk.PhotoImage(file="%s.gif" % fruitChange())
        self.images = self.subimage(0, 0, 32, 32)
        return self.spritesheet
    def __init__(self, frame, master):
        self.master = master
        
        self.createWid()
        
        frame.grid()
        #frame.pack()
##Calendar Part
def get_calendar(locale, fwday):
    # instantiate proper calendar class
    if locale is None:
        return cal.TextCalendar(fwday)
    else:
        return cal.LocaleTextCalendar(fwday, locale)
    
def _today():
    now = datetime.now()
    day = now.day
    month = now.month
    year = now.year
    #print("%s /" % str(month), str(day), str(year))
    return(month, day, year)

class Calendar(object):
    # XXX ToDo: cget and configure
    
    datetime = datetime(2017, 1, 1)
    timedelta = timedelta()
    def add(self, attr):
        if attr=='sp':
            self._show_selection(text, bbox, self.root_pic1b)
    def remove(self, attr):
        if attr=='sp':
            self._show_selection(text, bbox, self.io)    

    def __init__(self, master, **kw):
        """
        WIDGET-SPECIFIC OPTIONS

            locale, firstweekday, year, month, selectbackground,
            selectforeground
        """
        # remove custom options from kw before initializating ttk.Frame
        fwday = kw.pop('firstweekday', cal.SUNDAY)
        year = kw.pop('year', datetime.now().year)
        month = kw.pop('month', self.datetime.now().month)
        locale = kw.pop('locale', None)
        sel_bg = kw.pop('selectbackground', '#ecffc4')
        sel_fg = kw.pop('selectforeground', '#05640e')

        self._date = datetime(year, month, 1)
        self._selection = None # no date selected

        super(Calendar, self).__init__()

        self._cal = get_calendar(locale, fwday)

        self.__setup_styles()       # creates custom styles
        self.__place_widgets()      # pack/grid used widgets
        self.__config_calendar()    # adjust calendar columns and setup tags
        # configure a canvas, and proper bindings, for selecting dates
        self.__setup_selection(sel_bg, sel_fg)

        
        #Image and Image reference creation, The root list of sprites used is created here
        root_pic1 = Image.open('sb.png')                           # Open the image like this first
        root_pic2 = Image.open('sp.png')
        root_pic3 = Image.open('sb3.png')
        root_pic4 = Image.open('sb.gif')
        root_pic5 = Image.open('sp.gif')
        root_pic6 = Image.open('sb3.gif')
        self.root_pic1b = ImageTk.PhotoImage(root_pic1)
        self.root_pic2b = ImageTk.PhotoImage(root_pic2)  
        self.root_pic3b = ImageTk.PhotoImage(root_pic3)  
        self.root_pic4b = ImageTk.PhotoImage(root_pic4)  
        self.root_pic5b = ImageTk.PhotoImage(root_pic5)  
        self.root_pic6b = ImageTk.PhotoImage(root_pic6)
        self.img= [root_pic1, root_pic2, root_pic3, root_pic4, root_pic5, root_pic6, root_pic1, root_pic1, root_pic2, root_pic3, root_pic4, root_pic5, root_pic6, root_pic1, root_pic1]
        self.imgs= [self.root_pic1b, self.root_pic2b, self.root_pic3b, self.root_pic4b, self.root_pic5b, self.root_pic6b, self.root_pic1b, self.root_pic1b, self.root_pic2b, self.root_pic3b, self.root_pic4b, self.root_pic5b, self.root_pic6b, self.root_pic1b, self.root_pic1b]
        i = Image.open("new.png")
        self.io = ImageTk.PhotoImage(Image.open("new.png"))        
        
        # store items ids, used for insertion later
        v = ['Sunday', '','Monday', '','Tuesday','', 'Wednesday','', 'Thursday','', 'Friday','', 'Saturday','']
        self._items = [self._calendar.insert('', 'end', values=v) for _ in range(7)]
        
        self.greet_button = ttk.Button(master, text="Add Strawberry", command=self.add('sb'))
        self.greet_button.grid() 
        
        self.greet_button = ttk.Button(master, text="Remove Strawberry", command=self.remove('sb'))
        self.greet_button.grid()         
        
        # insert dates in the currently empty calendar
        
        self._build_calendar()
        # set the minimal size for the widget
     
        self._calendar.bind('<Map>', self.__minsize)

    def __setitem__(self, item, value):
        if item in ('year', 'month'):
            raise AttributeError("attribute '%s' is not writeable" % item)
        elif item == 'selectbackground':
            self._canvas['background'] = value
        elif item == 'selectforeground':
            self._canvas.itemconfigure(self._canvas.text, item=value)
        else:
            ttk.Frame.__setitem__(self, item, value)
            

    def __getitem__(self, item):
        if item in ('year', 'month'):
            return getattr(self._date, item)
        elif item == 'selectbackground':
            return self._canvas['background']
        elif item == 'selectforeground':
            return self._canvas.itemcget(self._canvas.text, 'fill')   
        else:
            r = ttk.tclobjs_to_py({item: ttk.Frame.__getitem__(self, item)}) 
            return r[item]

    def __setup_styles(self):
        # custom ttk styles
        #style = 
        arrow_layout = lambda dir: (
            [('Button.focus', {'children': [('Button.%sarrow' % dir, None)]})]
        )
        styles.layout('L.TButton', arrow_layout('left'))
        styles.layout('R.TButton', arrow_layout('right'))

    def __place_widgets(self):
        # header frame and its widgets
        hframe = frame
        lbtn = ttk.Button(hframe, style='L.TButton', command=self._prev_month)
        rbtn = ttk.Button(hframe, style='R.TButton', command=self._next_month)
        self._header = ttk.Label(hframe, width=14, anchor='center')
        # the calendar
        self._calendar = ttk.Treeview(show='', selectmode='none', height=7, colum=14)

#        #self._calendar.configure(yscroll=scrollbar)

        # Grid the widgets
        hframe.grid()
        lbtn.grid(in_=hframe)
        self._header.grid(in_=hframe, column=1, row=0, padx=12)
        rbtn.grid(in_=hframe, column=3, row=0)
        self._calendar.grid()
    def __config_calendar(self):
        ## This Controls the number of columns
        cols = self._cal.formatweekheader(14).split()
        #print(cols)
        daysnimages = ['Sunday','','Monday','','Tuesday','','Wednesday','','Thursday','','Friday','', 'Saturday','']
        self._calendar['columns'] = daysnimages
        
        self._calendar.tag_configure('header', background='#00ff99')
        self._calendar.insert('', 'end', values=daysnimages, tag='header')
        
        # adjust its columns width
        font = tkFont.Font()
        #maxwidth = max(font.measure(col) for col in daysnimages)
        
        maxwidth=75
        for col in daysnimages:
            #self._calendar["displaycolumns"]=col
            self._calendar.column(col, width=maxwidth, minwidth=0,anchor='e', stretch=True)

    def __setup_selection(self, sel_bg, sel_fg):
        self._font = tkFont.Font()
        self._canvas = canvas = tk.Canvas(self._calendar,
            background=sel_bg, borderwidth=0, highlightthickness=0)
        canvas.text = canvas.create_text(0, 0, fill=sel_fg, anchor='e')
        canvas.image = canvas.create_image(32, 10, image='')
        
        canvas.bind('<ButtonPress-1>', lambda evt: canvas.place_forget())
        self._calendar.bind('<Configure>', lambda evt: canvas.place_forget())
        self._calendar.bind('<ButtonPress-1>', self._pressed)

    def __minsize(self, evt):
        width, height = self._calendar.master.geometry().split('x')
        height = height[:height.index('+')]
        
        self._calendar.master.minsize(width, height)

    def _build_calendar(self):
        year, month = self._date.year, self._date.month
        
        # update header text (Month, YEAR)
        header = self._cal.formatmonthname(year, month, 0)
        self._header['text'] = header.title()
        
        # update calendar shown dates
        cal = self._cal.monthdayscalendar(year, month)
        #print(cal[0:6])
        for indx, item in enumerate(self._items):
            week = cal[indx] if indx < len(cal) else []
            x = 0
            specday = (self._date.month, x, self._date.year)
            today = _today() 
            weeks = []
            #daysnimages = ['Sunday', 'Image','Monday', 'Image','Tuesday','Image', 'Wednesday','Image', 'Thursday','Image', 'Friday','Image', 'Saturday','Image']
            for x in range(14):
                self._calendar.column(x, anchor="e", width=75)
            for day in week: 
                if (day == today[1]):
                    if(month==today[0]):
                        if(year==today[2]):
                            weeks.append("Today " + str(day))
                            weeks.append(' ')
                    elif(month==today[0]+1):
                        if(year==today[2]):
                            weeks.append("Next Month " + str(day))
                            weeks.append(" ")
                    elif(month==today[0]-1):
                        if(year==today[2]):
                            weeks.append("Last Month " + str(day))
                            weeks.append(" ")
                    else:
                        ##Month Intervals
                        weeks.append("" + str(day))
                        weeks.append(" ")
                
                else:
                    if day==0:
                        weeks.append('')
                    else:
                        weeks.append(day)
                    weeks.append(" ")
                
            else:
                weeks.append(' ')
                #self._calendar.tag_configure('Sunday', image=self.root_pic2b)
                #weeks.append(self.root_pic2b)
                #self._calendar.item(item, values=weeks)   
            
            self._calendar.item(item, values=weeks)
            
    ###
    def _show_selection(self, text, bbox, img):
        """Configure canvas for a new selection."""
        x, y, width, height = bbox

        textw = self._font.measure(text)
        
        canvas = self._canvas
        canvas.configure(width=width, height=height)
        canvas.coords(canvas.text, width - textw, height / 2 - 1)
        canvas.itemconfigure(canvas.text, text=text)
        
        canvas.itemconfigure(canvas.image, image= self.io)
        canvas.create_image([10,10], image=self.io)
        if img!=self.io:
            #canvas.itemconfigure(canvas.image, image= self.root_pic1b)
            canvas.create_image([10,10], image=img)
        else:
            #canvas.itemconfigure(canvas.image, image=self.root_pic2b)
            canvas.create_image([10,10], image=self.io)
        canvas.place(in_=self._calendar, x=x, y=y)

    # Callbacks

    def _pressed(self, evt):
        """Clicked somewhere in the calendar."""
        x, y, widget = evt.x, evt.y, evt.widget
        item = widget.identify_row(y)
        column = widget.identify_column(x)
        col_vals = []
        for idx in range(1,15):
            col_vals.append(idx)
        #print(column, item, self._items, column[1:3])
        if not column or not item in self._items:
            # clicked in the weekdays row or just outside the columns
            return
        
        if (int(column[1:3])==11 and int(item[3])==7) or (int(column[1:3])==12 and int(item[3])==7) or (int(column[1:3])==13 and int(item[3])==7) or (int(column[1:3])==14 and int(item[3])==7):
            return
        item_values = widget.item(item)['values']
        #print(widget.item(item)['values'])
        if not len(item_values): # row is empty for this month
            return
        #print(column)
        #text = item_values[int(column[1])-1]
        
        #text = item_values[int(self._calendar.bbox(item)[0])-1]
        q=self._calendar.identify("item", column[1:3], item[3])
        print ("you clicked on", column[1:3], item[3], x, y)
        text = item_values[int(column[1:3])-1]

        if not text: # date is empty
            return

        bbox = widget.bbox(item, column)
        #bbox = self._calendar.bbox(item)
        
        if not bbox: # calendar not visible yet
            return
        # update and then show selection
        print(column[1:3])
        if int(column[1:3])==2 or int(column[1:3])==4 or int(column[1:3])==6 or int(column[1:3])==8 or int(column[1:3])==10 or int(column[1:3])==12 or int(column[1:3])==14:
            text = text
            self._selection = (text,item, column)
            self._show_selection(text, bbox, self.root_pic1b)
        else:
            text = text
            self._selection = (text,item, column)
            self._show_selection(text, bbox, self.io)
        
        #self._selection = (text,item, column)
        
        #self._show_selection(text, bbox, self.root_pic1b) 

    def _prev_month(self):
        """Updated calendar to show the previous month."""
        self._canvas.place_forget()

        self._date = self._date - timedelta(days=1)
        self._date = datetime(self._date.year, self._date.month, 1)
        self._build_calendar() # reconstuct calendar

    def _next_month(self):
        """Update calendar to show the next month."""
        self._canvas.place_forget()

        year, month = self._date.year, self._date.month
        self._date = self._date + timedelta(days=cal.monthrange(year, month)[1] + 1)
        self._date = datetime(self._date.year, self._date.month, 1)
        self._build_calendar() # reconstruct calendar

    # Properties

    @property
    def selection(self):
        """Return a datetime or image representing the current selected date."""
        #if not self._selection:
            #return None

        year, month = self._date.year, self._date.month  
        return self.datetime(year, month, self._selection[0])
    
def on_configure(evt):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))

##Control
def test(parent):
    ttkcal = Calendar(parent, firstweekday=cal.SUNDAY)
    sprites = App(frame, parent)
    info = Application(frame, parent)  
    parent.mainloop()
    parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("My Refrigerator")
    #Scrollbar
    canvas = tk.Canvas(root)
    frame = tk.Frame(canvas, width=600, height=380)
    
    scrollbar = tk.Scrollbar(root, command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky='nw', rowspan=9, columnspan=9)
    canvas.configure(yscrollcommand = scrollbar.set)
    
    canvas.bind('<Configure>', on_configure)
    canvas.create_window((0,0), window=frame, anchor='nw')
    canvas.grid()
     
    styles = ttk.Style()
    styles.theme_use('clam')  
    
    frame.grid()
    
    test(root)
