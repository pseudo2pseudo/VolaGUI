#! /usr/bin/env python
#  -*- coding: utf-8 -*-

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

import volagui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = VolaGUI (root)
    volagui_support.init(root, top)
    root.mainloop()

w = None
def create_VolaGUI(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_VolaGUI(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = VolaGUI (w)
    volagui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_VolaGUI():
    global w
    w.destroy()
    w = None

class VolaGUI:
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

        top.geometry("800x600+405+145")
        top.minsize(1, 1)
        top.maxsize(1585, 870)
        top.resizable(1,  1)
        top.title("VolaGUI")
        top.configure(highlightcolor="black")

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.Tabs = ttk.Notebook(top)
        self.Tabs.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Tabs.configure(takefocus="")
        self.Tabs_general_1 = tk.Frame(self.Tabs)
        self.Tabs.add(self.Tabs_general_1, padding=3)
        self.Tabs.tab(0, text="General",compound="left",underline="-1",)
        self.Tabs_processes_1 = tk.Frame(self.Tabs)
        self.Tabs.add(self.Tabs_processes_1, padding=3)
        self.Tabs.tab(1, text="Processes",compound="left",underline="-1",)
        self.Tabs_dll_1 = tk.Frame(self.Tabs)
        self.Tabs.add(self.Tabs_dll_1, padding=3)
        self.Tabs.tab(2, text="DLL & Registry",compound="none",underline="-1",)
        self.Tabs_networking_1 = tk.Frame(self.Tabs)
        self.Tabs.add(self.Tabs_networking_1, padding=3)
        self.Tabs.tab(3, text="Networking",compound="none",underline="-1",)
        self.Tabs_advanced_1 = tk.Frame(self.Tabs)
        self.Tabs.add(self.Tabs_advanced_1, padding=3)
        self.Tabs.tab(4, text="Advanced",compound="none",underline="-1",)

        self.TEPath = ttk.Entry(self.Tabs_general_1)
        self.TEPath.place(relx=0.238, rely=0.052, relheight=0.037
                , relwidth=0.569)
        self.TEPath.configure(takefocus="")
        self.TEPath.configure(cursor="xterm")
        self.tooltip_font = "TkDefaultFont"
        self.TEPath_tooltip = \
        ToolTip(self.TEPath, self.tooltip_font, '''Path''')

        self.TLabel1 = ttk.Label(self.Tabs_general_1)
        self.TLabel1.place(relx=0.039, rely=0.052, height=19, width=142)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Image Memory Path :''')

        self.TBImageInfo = ttk.Button(self.Tabs_general_1)
        self.TBImageInfo.place(relx=0.84, rely=0.044, height=28, width=83)
        self.TBImageInfo.configure(takefocus="")
        self.TBImageInfo.configure(text='''Image Info''')
        self.TBImageInfo.configure(compound='none')
        self.TBImageInfo.bind('<Button-1>',volagui_support.imageInfo_click)

        self.TLabel2 = ttk.Label(self.Tabs_general_1)
        self.TLabel2.place(relx=0.079, rely=0.873, height=19, width=111)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''Choose Profile :''')

        self.TBStartAnalysis = ttk.Button(self.Tabs_general_1)
        self.TBStartAnalysis.place(relx=0.687, rely=0.869, height=28, width=113)
        self.TBStartAnalysis.configure(takefocus="")
        self.TBStartAnalysis.configure(text='''Start Analysis''')
        self.TBStartAnalysis.bind('<Button-1>',volagui_support.start_click)

        self.TEProfile = ttk.Entry(self.Tabs_general_1)
        self.TEProfile.place(relx=0.229, rely=0.871, relheight=0.037
                , relwidth=0.293)
        self.TEProfile.configure(takefocus="")
        self.TEProfile.configure(cursor="xterm")
        self.tooltip_font = "TkDefaultFont"
        self.TEProfile_tooltip = \
        ToolTip(self.TEProfile, self.tooltip_font, '''Choose Profile''')

        self.TextImageInfo = tk.Text(self.Tabs_general_1)
        self.TextImageInfo.place(relx=0.025, rely=0.122, relheight=0.669
                , relwidth=0.947)
        self.TextImageInfo.configure(background="white")
        self.TextImageInfo.configure(font="TkTextFont")
        self.TextImageInfo.configure(selectbackground="blue")
        self.TextImageInfo.configure(selectforeground="white")
        self.TextImageInfo.configure(wrap="word")

        self.TLabel3 = ttk.Label(self.Tabs_processes_1)
        self.TLabel3.place(relx=0.038, rely=0.012, height=19, width=72)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''psxview''')

        self.TLabel4 = ttk.Label(self.Tabs_processes_1)
        self.TLabel4.place(relx=0.039, rely=0.416, height=19, width=52)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="TkDefaultFont")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(anchor='w')
        self.TLabel4.configure(justify='left')
        self.TLabel4.configure(text='''pstree''')

        self.TLabel5 = ttk.Label(self.Tabs_processes_1)
        self.TLabel5.place(relx=0.038, rely=0.817, height=19, width=112)
        self.TLabel5.configure(background="#d9d9d9")
        self.TLabel5.configure(foreground="#000000")
        self.TLabel5.configure(font="TkDefaultFont")
        self.TLabel5.configure(relief="flat")
        self.TLabel5.configure(anchor='w')
        self.TLabel5.configure(justify='left')
        self.TLabel5.configure(text='''Dump Process :''')

        self.TLabel6 = ttk.Label(self.Tabs_processes_1)
        self.TLabel6.place(relx=0.04, rely=0.862, height=19, width=43)
        self.TLabel6.configure(background="#d9d9d9")
        self.TLabel6.configure(foreground="#000000")
        self.TLabel6.configure(font="TkDefaultFont")
        self.TLabel6.configure(relief="flat")
        self.TLabel6.configure(anchor='w')
        self.TLabel6.configure(justify='left')
        self.TLabel6.configure(text='''PID :''')

        self.TEPid = ttk.Entry(self.Tabs_processes_1)
        self.TEPid.place(relx=0.1, rely=0.861, relheight=0.037, relwidth=0.119)
        self.TEPid.configure(takefocus="")
        self.TEPid.configure(cursor="xterm")

        self.TLabel7 = ttk.Label(self.Tabs_processes_1)
        self.TLabel7.place(relx=0.238, rely=0.864, height=19, width=42)
        self.TLabel7.configure(background="#d9d9d9")
        self.TLabel7.configure(foreground="#000000")
        self.TLabel7.configure(font="TkDefaultFont")
        self.TLabel7.configure(relief="flat")
        self.TLabel7.configure(anchor='w')
        self.TLabel7.configure(justify='left')
        self.TLabel7.configure(text='''Path :''')

        self.TEPathP = ttk.Entry(self.Tabs_processes_1)
        self.TEPathP.place(relx=0.301, rely=0.861, relheight=0.037
                , relwidth=0.644)
        self.TEPathP.configure(takefocus="")
        self.TEPathP.configure(cursor="xterm")

        self.TBDumpP = ttk.Button(self.Tabs_processes_1)
        self.TBDumpP.place(relx=0.326, rely=0.923, height=28, width=83)
        self.TBDumpP.configure(takefocus="")
        self.TBDumpP.configure(text='''Dump''')
        self.TBDumpP.bind('<Button-1>',volagui_support.dumpp_click)

        self.TVirusTotalP = ttk.Button(self.Tabs_processes_1)
        self.TVirusTotalP.place(relx=0.464, rely=0.923, height=28, width=123)
        self.TVirusTotalP.configure(takefocus="")
        self.TVirusTotalP.configure(text='''Open Virus Total''')
        self.TVirusTotalP.bind('<Button-1>',volagui_support.openVirusTotalp_click)

        self.TextPsxview = tk.Text(self.Tabs_processes_1)
        self.TextPsxview.place(relx=0.025, rely=0.059, relheight=0.347
                , relwidth=0.952)
        self.TextPsxview.configure(background="white")
        self.TextPsxview.configure(font="TkTextFont")
        self.TextPsxview.configure(selectbackground="blue")
        self.TextPsxview.configure(selectforeground="white")
        self.TextPsxview.configure(wrap="word")

        self.TextPstree = tk.Text(self.Tabs_processes_1)
        self.TextPstree.place(relx=0.025, rely=0.46, relheight=0.347
                , relwidth=0.952)
        self.TextPstree.configure(background="white")
        self.TextPstree.configure(font="TkTextFont")
        self.TextPstree.configure(selectbackground="blue")
        self.TextPstree.configure(selectforeground="white")
        self.TextPstree.configure(wrap="word")

        self.TLabel9 = ttk.Label(self.Tabs_dll_1)
        self.TLabel9.place(relx=0.226, rely=0.028, height=19, width=83)
        self.TLabel9.configure(background="#d9d9d9")
        self.TLabel9.configure(foreground="#000000")
        self.TLabel9.configure(font="TkDefaultFont")
        self.TLabel9.configure(relief="flat")
        self.TLabel9.configure(anchor='w')
        self.TLabel9.configure(justify='left')
        self.TLabel9.configure(text='''Select PID :''')

        self.TEPidD = ttk.Entry(self.Tabs_dll_1)
        self.TEPidD.place(relx=0.338, rely=0.026, relheight=0.037
                , relwidth=0.118)
        self.TEPidD.configure(takefocus="")
        self.TEPidD.configure(cursor="xterm")

        self.TLabel10 = ttk.Label(self.Tabs_dll_1)
        self.TLabel10.place(relx=0.038, rely=0.789, height=19, width=114)
        self.TLabel10.configure(background="#d9d9d9")
        self.TLabel10.configure(foreground="#000000")
        self.TLabel10.configure(font="TkDefaultFont")
        self.TLabel10.configure(relief="flat")
        self.TLabel10.configure(anchor='w')
        self.TLabel10.configure(justify='left')
        self.TLabel10.configure(text='''Dump Registry :''')

        self.TLabel12 = ttk.Label(self.Tabs_dll_1)
        self.TLabel12.place(relx=0.188, rely=0.836, height=19, width=42)
        self.TLabel12.configure(background="#d9d9d9")
        self.TLabel12.configure(foreground="#000000")
        self.TLabel12.configure(font="TkDefaultFont")
        self.TLabel12.configure(relief="flat")
        self.TLabel12.configure(anchor='w')
        self.TLabel12.configure(justify='left')
        self.TLabel12.configure(text='''Path :''')

        self.TEPathD = ttk.Entry(self.Tabs_dll_1)
        self.TEPathD.place(relx=0.263, rely=0.836, relheight=0.037
                , relwidth=0.581)
        self.TEPathD.configure(takefocus="")
        self.TEPathD.configure(cursor="xterm")

        self.TBDumpD = ttk.Button(self.Tabs_dll_1)
        self.TBDumpD.place(relx=0.338, rely=0.906, height=28, width=83)
        self.TBDumpD.configure(takefocus="")
        self.TBDumpD.configure(text='''Dump''')
        self.TBDumpD.bind('<Button-1>',volagui_support.dumpd_click)

        self.TBVirusTotalD = ttk.Button(self.Tabs_dll_1)
        self.TBVirusTotalD.place(relx=0.514, rely=0.906, height=28, width=123)
        self.TBVirusTotalD.configure(takefocus="")
        self.TBVirusTotalD.configure(text='''Open Virus Total''')
        self.TBVirusTotalD.bind('<Button-1>',volagui_support.openVirusTotald_click)

        self.TextDlllist = tk.Text(self.Tabs_dll_1)
        self.TextDlllist.place(relx=0.025, rely=0.087, relheight=0.686
                , relwidth=0.947)
        self.TextDlllist.configure(background="white")
        self.TextDlllist.configure(font="TkTextFont")
        self.TextDlllist.configure(selectbackground="blue")
        self.TextDlllist.configure(selectforeground="white")
        self.TextDlllist.configure(wrap="word")

        self.TBDlllist = tk.Button(self.Tabs_dll_1)
        self.TBDlllist.place(relx=0.564, rely=0.017, height=31, width=71)
        self.TBDlllist.configure(text='''dlllist''')
        self.TBDlllist.bind('<Button-1>',volagui_support.dlllist_click)

        self.TextNetworking = tk.Text(self.Tabs_networking_1)
        self.TextNetworking.place(relx=0.025, rely=0.087, relheight=0.878
                , relwidth=0.947)
        self.TextNetworking.configure(background="white")
        self.TextNetworking.configure(font="TkTextFont")
        self.TextNetworking.configure(selectbackground="blue")
        self.TextNetworking.configure(selectforeground="white")
        self.TextNetworking.configure(wrap="word")

        self.TBnetscan = tk.Button(self.Tabs_networking_1)
        self.TBnetscan.place(relx=0.213, rely=0.017, height=31, width=71)
        self.TBnetscan.configure(text='''netscan''')
        self.TBnetscan.bind('<Button-1>',volagui_support.netscan_click)

        self.TBconnscan = tk.Button(self.Tabs_networking_1)
        self.TBconnscan.place(relx=0.439, rely=0.017, height=31, width=71)
        self.TBconnscan.configure(text='''connscan''')
        self.TBconnscan.bind('<Button-1>',volagui_support.connscan_click)

        self.TBsockets = tk.Button(self.Tabs_networking_1)
        self.TBsockets.place(relx=0.677, rely=0.017, height=31, width=71)
        self.TBsockets.configure(text='''sockets''')
        self.TBsockets.bind('<Button-1>',volagui_support.sockets_click)

        self.TextAdvanced = tk.Text(self.Tabs_advanced_1)
        self.TextAdvanced.place(relx=0.025, rely=0.157, relheight=0.808
                , relwidth=0.947)
        self.TextAdvanced.configure(background="white")
        self.TextAdvanced.configure(font="TkTextFont")
        self.TextAdvanced.configure(selectbackground="blue")
        self.TextAdvanced.configure(selectforeground="white")
        self.TextAdvanced.configure(wrap="word")

        self.Label1 = tk.Label(self.Tabs_advanced_1)
        self.Label1.place(relx=0.016, rely=0.03, height=21, width=300)
        self.Label1.configure(text='''$ volatility -f dump.mem ''')

        self.TECommand = tk.Entry(self.Tabs_advanced_1)
        self.TECommand.place(relx=0.393, rely=0.026, height=23, relwidth=0.571)
        self.TECommand.configure(background="white")
        self.TECommand.configure(font="TkFixedFont")
        self.tooltip_font = "TkDefaultFont"
        self.TECommand_tooltip = \
        ToolTip(self.TECommand, self.tooltip_font, '''input command''')

        self.TBExecute = tk.Button(self.Tabs_advanced_1)
        self.TBExecute.place(relx=0.439, rely=0.087, height=31, width=71)
        self.TBExecute.configure(text='''Execute''')
        self.TBExecute.bind('<Button-1>',volagui_support.execute_click)

# ======================================================
# Support code for Balloon Help (also called tooltips).
# Found the original code at:
# http://code.activestate.com/recipes/576688-tooltip-for-tkinter/
# Modified by Rozen to remove Tkinter import statements and to receive
# the font as an argument.
# ======================================================

from time import time, localtime, strftime

class ToolTip(tk.Toplevel):
    """
    Provides a ToolTip widget for Tkinter.
    To apply a ToolTip to any Tkinter widget, simply pass the widget to the
    ToolTip constructor
    """
    def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                 delay=0.5, follow=True):
        """
        Initialize the ToolTip

        Arguments:
          wdgt: The widget this ToolTip is assigned to
          tooltip_font: Font to be used
          msg:  A static string message assigned to the ToolTip
          msgFunc: A function that retrieves a string to use as the ToolTip text
          delay:   The delay in seconds before the ToolTip appears(may be float)
          follow:  If True, the ToolTip follows motion, otherwise hides
        """
        self.wdgt = wdgt
        # The parent of the ToolTip is the parent of the ToolTips widget
        self.parent = self.wdgt.master
        # Initalise the Toplevel
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        # Hide initially
        self.withdraw()
        # The ToolTip Toplevel should have no frame or title bar
        self.overrideredirect(True)

        # The msgVar will contain the text displayed by the ToolTip
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        # The text of the ToolTip is displayed in a Message widget
        tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                font=tooltip_font,
                aspect=1000).grid()

        # Add bindings to the widget.  This will NOT override
        # bindings that the widget already has
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')

    def spawn(self, event=None):
        """
        Spawn the ToolTip.  This simply makes the ToolTip eligible for display.
        Usually this is caused by entering the widget

        Arguments:
          event: The event that called this funciton
        """
        self.visible = 1
        # The after function takes a time argument in milliseconds
        self.after(int(self.delay * 1000), self.show)

    def show(self):
        """
        Displays the ToolTip if the time delay has been long enough
        """
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()

    def move(self, event):
        """
        Processes motion within the widget.
        Arguments:
          event: The event that called this function
        """
        self.lastMotion = time()
        # If the follow flag is not set, motion within the
        # widget will make the ToolTip disappear
        #
        if self.follow is False:
            self.withdraw()
            self.visible = 1

        # Offset the ToolTip 10x10 pixes southwest of the pointer
        self.geometry('+%i+%i' % (event.x_root+20, event.y_root-10))
        try:
            # Try to call the message function.  Will not change
            # the message if the message function is None or
            # the message function fails
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)

    def hide(self, event=None):
        """
        Hides the ToolTip.  Usually this is caused by leaving the widget
        Arguments:
          event: The event that called this function
        """
        self.visible = 0
        self.withdraw()

    def update(self, msg):
        """
        Updates the Tooltip with a new message. Added by Rozen
        """
        self.msgVar.set(msg)

# ===========================================================
#                   End of Class ToolTip
# ===========================================================

if __name__ == '__main__':
    vp_start_gui()





