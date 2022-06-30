#INTERFACE/TELA
import sys
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import interface_support as tela
from config import *

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    tela.set_Tk_var()
    top = KeyLight (root)
    tela.init(root, top)
    root.mainloop()

w = None
def create_KeyLight(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_KeyLight(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    tela.set_Tk_var()
    top = KeyLight (w)
    tela.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_KeyLight():
    global w
    w.destroy()
    w = None

class KeyLight:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+284+394")
        top.minsize(1, 1)
        top.maxsize(1009, 738)
        top.resizable(1, 1)
        top.title("Key Light Configurações")
        top.configure(borderwidth="1")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.033, rely=0.067, relheight=0.167
                , relwidth=0.608)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")

        self.TCombobox1 = ttk.Combobox(self.Frame1)
        self.TCombobox1.place(relx=0.137, rely=0.133, relheight=0.227
                , relwidth=0.493)
        self.value_list = entradas #['a','b','c',]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(textvariable=tela.combobox)
        self.TCombobox1.configure(takefocus="")
        #self.TCombobox1.name("TCombobox1")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.027, rely=0.027, height=27, width=41)
        self.Label1.configure(text='''Input''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.036, rely=0.533, height=17, width=41)
        self.Label2.configure(text='''Output''')

        self.TCombobox2 = ttk.Combobox(self.Frame1)
        self.TCombobox2.place(relx=0.173, rely=0.533, relheight=0.227
                , relwidth=0.458)
        self.value_list = saidas #['a','b','c',]
        self.TCombobox2.configure(values=self.value_list)
        self.TCombobox2.configure(textvariable=tela.combobox2)
        self.TCombobox2.configure(takefocus="")

        self.Checkbutton1 = tk.Checkbutton(self.Frame1)
        self.Checkbutton1.place(relx=0.658, rely=0.533, relheight=0.253
                , relwidth=0.148)
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''Active''')
        self.Checkbutton1.configure(variable=tela.che52)

        self.Checkbutton2 = tk.Checkbutton(top)
        self.Checkbutton2.place(relx=0.7, rely=0.067, relheight=0.042,
                relwidth=0.122)
        self.Checkbutton2.configure(justify='left')
        self.Checkbutton2.configure(text='''Fullscreen''')
        self.Checkbutton2.configure(variable=tela.che44)

        self.TCombobox3 = ttk.Combobox(top)
        self.TCombobox3.place(relx=0.173, rely=0.5, relheight=0.04
                , relwidth=0.458)
        self.value_list = ['Bars','Plane','c',]
        self.TCombobox3.configure(values=self.value_list)
        self.TCombobox3.configure(textvariable=tela.combobox3)
        self.TCombobox3.configure(takefocus="")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)
#FIM INTERFACE/TELA
