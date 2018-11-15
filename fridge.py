#Entire fridge
import tkinter as tk
from tkinter import ttk
import datetime
from datetime import *

import calendar as cal
from calendar import *
import tkinter.font as tkFont
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
class Application(object):
    def say_hi(self, x):
        print("%s" % x)   
    
    def greet(self):
        q = switchHouse(0)
        #self.label = Label(text=showData())
        #self.label.pack()
        w = tk.Message(text=q)
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
        self.label.pack()

        self.greet_button = ttk.Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()
                

        self.close_button = ttk.Button(master, text="Close", command=master.quit)
        self.close_button.pack()

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
        
        menu_edit.add_command(label="view", command=lambda: view(listData))
                              
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
        self.images = self.subimage(0, 0, 32, 32)
        self.canvas = tk.Canvas(width=100, height=100)
        self.canvas.pack()
        self.updateimage(0)          
    def subimage(self, l, t, r, b):
        print(l,t,r,b)
        dst = tk.PhotoImage()
        dst.tk.call(dst, 'copy', self.spritesheet, '-from', l, t, r, b, '-to', 0, 0)
        return dst

    def updateimage(self, sprite):
        self.canvas.delete(self.last_img)
        self.last_img = self.canvas.create_image(16, 24, image=self.images)
        root.after(100, self.updateimage, (sprite+1) % self.num_sprintes)
        
    def __init__(self, frame, master):
        self.master = master
        
        self.createWid()
        
        frame.pack()
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

    #datetime = calendar.datetime.date
    datetime = datetime(2017, 1, 1)
    timedelta = timedelta()

    def __init__(self, master, **kw):
        """
        WIDGET-SPECIFIC OPTIONS

            locale, firstweekday, year, month, selectbackground,
            selectforeground
        """
        # remove custom options from kw before initializating ttk.Frame
        fwday = kw.pop('firstweekday', cal.MONDAY)
        year = kw.pop('year', datetime.now().year)
        month = kw.pop('month', self.datetime.now().month)
        locale = kw.pop('locale', None)
        sel_bg = kw.pop('selectbackground', '#ecffc4')
        sel_fg = kw.pop('selectforeground', '#05640e')

        self._date = datetime(year, month, 1)
        self._selection = None # no date selected


        ##bug below
        #ttk.Frame.__init__(self, master, **kw)
        super(Calendar, self).__init__()

        self._cal = get_calendar(locale, fwday)

        self.__setup_styles()       # creates custom styles
        self.__place_widgets()      # pack/grid used widgets
        self.__config_calendar()    # adjust calendar columns and setup tags
        # configure a canvas, and proper bindings, for selecting dates
        self.__setup_selection(sel_bg, sel_fg)

        # store items ids, used for insertion later
        self._items = [self._calendar.insert('', 'end', values='')
                            for _ in range(6)]
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
        # Bug below
        #style = ttk.Style(self.master)
        #style = 
        arrow_layout = lambda dir: (
            [('Button.focus', {'children': [('Button.%sarrow' % dir, None)]})]
        )
        styles.layout('L.TButton', arrow_layout('left'))
        styles.layout('R.TButton', arrow_layout('right'))

    def __place_widgets(self):
        # header frame and its widgets
        #hframe = ttk.Frame(self)
        hframe = frame
        lbtn = ttk.Button(hframe, style='L.TButton', command=self._prev_month)
        rbtn = ttk.Button(hframe, style='R.TButton', command=self._next_month)
        self._header = ttk.Label(hframe, width=15, anchor='center')
        # the calendar
        self._calendar = ttk.Treeview(show='', selectmode='none', height=7)

        # pack the widgets
        
#        #hframe.pack(in_=self, side='top', pady=4, anchor='center')
        hframe.pack()
        lbtn.grid(in_=hframe)
        self._header.grid(in_=hframe, column=1, row=0, padx=12)
        rbtn.grid(in_=hframe, column=2, row=0)
        
#        #self._calendar.pack(in_=self, expand=1, fill='both', side='bottom')
        self._calendar.pack()
    def __config_calendar(self):
        cols = self._cal.formatweekheader(3).split()
        self._calendar['columns'] = cols
        self._calendar.tag_configure('header', background='grey90')
        self._calendar.insert('', 'end', values=cols, tag='header')
        # adjust its columns width
        font = tkFont.Font()
        maxwidth = max(font.measure(col) for col in cols)
        for col in cols:
            self._calendar.column(col, width=maxwidth, minwidth=maxwidth,
                anchor='e')

    def __setup_selection(self, sel_bg, sel_fg):
        self._font = tkFont.Font()
        self._canvas = canvas = tk.Canvas(self._calendar,
            background=sel_bg, borderwidth=0, highlightthickness=0)
        canvas.text = canvas.create_text(0, 0, fill=sel_fg, anchor='w')

        canvas.bind('<ButtonPress-1>', lambda evt: canvas.place_forget())
        self._calendar.bind('<Configure>', lambda evt: canvas.place_forget())
        self._calendar.bind('<ButtonPress-1>', self._pressed)

    def __minsize(self, evt):
        width, height = self._calendar.master.geometry().split('x')
        height = height[:height.index('+')]
        self._calendar.master.minsize(width, height)

    def _build_calendar(self):
#        #sc.test("sp")
        year, month = self._date.year, self._date.month
        #print(str(year) + " " + str(month) + " " + str(self._date.day))
        
        # update header text (Month, YEAR)
        header = self._cal.formatmonthname(year, month, 0)
        self._header['text'] = header.title()
        
        # update calendar shown dates
        cal = self._cal.monthdayscalendar(year, month)
        
        for indx, item in enumerate(self._items):
            week = cal[indx] if indx < len(cal) else []
            
            x = 0
            specday = (self._date.month, x, self._date.year)
            today = _today() 
            
            months = []
            weeks = []
            for i in range(0, len(cal)):            
                for day in week:
                    if(day == today[1]):
                        weeks.append("Today")
                        
                    else:
                        weeks.append(day)
            print(months)
            print(weeks)
            
            #fmt_week = [('%02d' % day) if day else '' for day in week]
            self._calendar.item(item, values=weeks)
            
    ###  
    
    ###
    def _show_selection(self, text, bbox):
        """Configure canvas for a new selection."""
        x, y, width, height = bbox

        textw = self._font.measure(text)

        canvas = self._canvas
        canvas.configure(width=width, height=height)
        canvas.coords(canvas.text, width - textw, height / 2 - 1)
        canvas.itemconfigure(canvas.text, text=text)
        canvas.place(in_=self._calendar, x=x, y=y)

    # Callbacks

    def _pressed(self, evt):
        """Clicked somewhere in the calendar."""
        x, y, widget = evt.x, evt.y, evt.widget
        item = widget.identify_row(y)
        column = widget.identify_column(x)

        if not column or not item in self._items:
            # clicked in the weekdays row or just outside the columns
            return

        item_values = widget.item(item)['values']
        if not len(item_values): # row is empty for this month
            return

        text = item_values[int(column[1]) - 1]
        if not text: # date is empty
            return

        bbox = widget.bbox(item, column)
        if not bbox: # calendar not visible yet
            return

        # update and then show selection
        text = '%02d' % text
        self._selection = (text, item, column)
        self._show_selection(text, bbox)

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
        self._date = self._date + timedelta(
            days=cal.monthrange(year, month)[1] + 1)
        self._date = datetime(self._date.year, self._date.month, 1)
        self._build_calendar() # reconstruct calendar

    # Properties

    @property
    def selection(self):
        """Return a datetime representing the current selected date."""
        if not self._selection:
            return None

        year, month = self._date.year, self._date.month
        return self.datetime(year, month, int(self._selection[0]))
##Control
def test(parent):
    #root = parent
    
    #import sys
    #if 'win' not in sys.platform:
    
    
    #ttkcal = Calendar(firstweekday=calendar.SUNDAY)
    ttkcal = Calendar(parent, firstweekday=cal.SUNDAY)
    info = Application(frame, parent)
    sprites = App(frame, parent)
#    #ttkcal.pack(expand=1, fill='both')  
    parent.mainloop()
    parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("My Refrigerator")
    #BAD LINE #tk.Frame.__init__(root)
    frame = tk.Frame(root,  width=480, height=180)
    styles = ttk.Style()
    styles.theme_use('clam')    
    frame.pack()
    test(root)
    #root.destroy()
