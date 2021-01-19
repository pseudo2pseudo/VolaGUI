#! /usr/bin/env python
#  -*- coding: utf-8 -*-

import sys
import subprocess
import webbrowser

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
    path = w.TEPath.get()
    if path == '':
        print('Please enter Path !')
        return
    with open("imageinfo", "w") as file:
        proc = []
        proc.append(subprocess.Popen(
            ['./volatility_2.6_lin64_standalone','-f',path,'imageinfo'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            shell=False,
            ))
        file.write(proc[0].communicate()[0])
        file.close()
    with open("imageinfo", "r") as file:
        w.TextImageInfo.insert(tk.END, file.read())
        file.close()
    sys.stdout.flush()

def start_click(self):
    path = w.TEPath.get()
    if path == '':
        print('Please enter Path !')
        return
    profile = '--profile='
    profile = profile + w.TEProfile.get()
    if profile == '--profile=':
        print('Please enter Profile !')
        return
    with open("psxview", "w") as file:
        proc = []
        proc.append(subprocess.Popen(
            ['./volatility_2.6_lin64_standalone','-f',path,profile,'psxview'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            shell=False,
            ))
        file.write(proc[0].communicate()[0])
        file.close()
    with open("pstree", "w") as file:
        proc = []
        proc.append(subprocess.Popen(
            ['./volatility_2.6_lin64_standalone','-f',path,profile,'pstree'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            shell=False,
            ))
        file.write(proc[0].communicate()[0])
        file.close()
    with open("psxview", "r") as file:
        w.TextPsxview.insert(tk.END, file.read())
        file.close()
    with open("pstree", "r") as file:
        w.TextPstree.insert(tk.END,file.read())
        file.close()
    sys.stdout.flush()

def connscan_click(self):
    path = w.TEPath.get()
    if path == '':
        print('Please enter Path !')
        return
    profile = '--profile='
    profile = profile + w.TEProfile.get()
    if profile == '--profile=':
        print('Please enter Profile !')
        return
    with open("connscan", "w") as file:
        proc = []
        proc.append(subprocess.Popen(
            ['./volatility_2.6_lin64_standalone','-f',path,profile,'connscan'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            shell=False,
            ))
        file.write(proc[0].communicate()[0])
        file.close()
    with open("connscan", "r") as file:
        w.TextNetworking.insert(tk.END, file.read())
        file.close()
    sys.stdout.flush()

def dlllist_click(self):
    path = w.TEPath.get()
    if path == '':
        print('Please enter Path !')
        return
    pid = w.TEPidD.get()
    if pid == '':
        print('Please enter PID !')
        return
    profile = '--profile='
    profile = profile + w.TEProfile.get()
    if profile == '--profile=':
        print('Please enter Profile !')
        return
    with open("dlllist", "w") as file:
        proc = []
        proc.append(subprocess.Popen(
            ['./volatility_2.6_lin64_standalone','-f',path,profile,'dlllist','-p',pid],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            shell=False,
            ))
        file.write(proc[0].communicate()[0])
        file.close()
    with open("dlllist", "r") as file:
        w.TextDlllist.insert(tk.END, file.read())
        file.close()
    sys.stdout.flush()

def dumpd_click(self):
    path = w.TEPath.get()
    if path == '':
        print('Please enter Path !')
        return
    profile = '--profile='
    profile = profile + w.TEProfile.get()
    if profile == '--profile=':
        print('Please enter Profile !')
        return
    pathDump = w.TEPathD.get()
    if pathDump == '':
        print('Please enter Path Dump !')
        return
    proc = []
    proc.append(subprocess.Popen(
        ['./volatility_2.6_lin64_standalone','-f',path,profile,'dumpregistry -D',pathDump],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        shell=False,
        ))
    sys.stdout.flush()

def dumpp_click(self):
    pid = w.TEPidD.get()
    if pid == '':
        print('Please enter PID !')
        return
    path = w.TEPath.get()
    if path == '':
        print('Please enter Path !')
        return
    profile = '--profile='
    profile = profile + w.TEProfile.get()
    if profile == '--profile=':
        print('Please enter Profile !')
        return
    pathDump = w.TEPathP.get()
    if pathDump == '':
        print('Please enter Path Dump !')
        return
    proc = []
    proc.append(subprocess.Popen(
        ['./volatility_2.6_lin64_standalone','-f',path,profile,'procdump -D',pathDump,'-p',pid],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        shell=False,
        ))
    sys.stdout.flush()

def execute_click(self):
    path = w.TEPath.get()
    if path == '':
        print('Please enter Path !')
        return
    profile = '--profile='
    profile = profile + w.TEProfile.get()
    if profile == '--profile=':
        print('Please enter Profile !')
        return
    command = w.TECommand.get()
    if command == '':
        print('Please enter COmmand !')
        return
    with open("advanced", "w") as file:
        proc = []
        proc.append(subprocess.Popen(
            ['./volatility_2.6_lin64_standalone','-f',path,profile,command],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            shell=False,
            ))
        file.write(proc[0].communicate()[0])
        file.close()
    with open("advanced", "r") as file:
        w.TextAdvanced.insert(tk.END, file.read())
        file.close()
    sys.stdout.flush()

def netscan_click(self):
    path = w.TEPath.get()
    if path == '':
        print('Please enter Path !')
        return
    profile = '--profile='
    profile = profile + w.TEProfile.get()
    if profile == '--profile=':
        print('Please enter Profile !')
        return
    with open("netscan", "w") as file:
        proc = []
        proc.append(subprocess.Popen(
            ['./volatility_2.6_lin64_standalone','-f',path,profile,'netscan'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            shell=False,
            ))
        file.write(proc[0].communicate()[0])
        file.close()
    with open("netscan", "r") as file:
        w.TextNetworking.insert(tk.END, file.read())
        file.close()
    sys.stdout.flush()

def openVirusTotald_click(self):
    url = 'https://virustotal.com/gui/'
    webbrowser.get(using='firefox').open(url, new=0)
    sys.stdout.flush()

def openVirusTotalp_click(self):
    url = 'https://virustotal.com/gui/'
    webbrowser.get(using='firefox').open(url, new=0)
    sys.stdout.flush()

def sockets_click(self):
    path = w.TEPath.get()
    if path == '':
        print('Please enter Path !')
        return
    profile = '--profile='
    profile = profile + w.TEProfile.get()
    if profile == '--profile=':
        print('Please enter Profile !')
        return
    with open("sockets", "w") as file:
        proc = []
        proc.append(subprocess.Popen(
            ['./volatility_2.6_lin64_standalone','-f',path,profile,'sockets'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            shell=False,
            ))
        file.write(proc[0].communicate()[0])
        file.close()
    with open("sockets", "r") as file:
        w.TextNetworking.insert(tk.END, file.read())
        file.close()
    sys.stdout.flush()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import volagui
    volagui.vp_start_gui()





