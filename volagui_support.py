#! /usr/bin/env python
#  -*- coding: utf-8 -*-

import sys
import subprocess

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

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def imageInfo_click(self):
    with open("imageinfo", "w") as file:
        proc = []
        proc.append(subprocess.Popen(
            ['./volatility_2.6_lin64_standalone','-f','','imageinfo'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            shell=False,
            ))
        file.write(proc[0].communicate()[0])
        file.close()
    
    with open("imageinfo", "r") as file:
        w.TextImageInfo.insert(tk.END, file.read())
    sys.stdout.flush()

def start_click():
    print('volagui_support.start_click')
    sys.stdout.flush()

def connscan_click():
    print('volagui_support.connscan_click')
    sys.stdout.flush()

def dlllist_click():
    print('volagui_support.dlllist_click')
    sys.stdout.flush()

def dumpd_click():
    print('volagui_support.dumpd_click')
    sys.stdout.flush()

def dumpp_click():
    print('volagui_support.dumpp_click')
    sys.stdout.flush()

def execute_click():
    print('volagui_support.execute_click')
    sys.stdout.flush()

def netscan_click():
    print('volagui_support.netscan_click')
    sys.stdout.flush()

def openVirusTotald_click():
    print('volagui_support.openVirusTotald_click')
    sys.stdout.flush()

def openVirusTotalp_click():
    print('volagui_support.openVirusTotalp_click')
    sys.stdout.flush()

def sockets_click():
    print('volagui_support.sockets_click')
    sys.stdout.flush()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import volagui
    volagui.vp_start_gui()





