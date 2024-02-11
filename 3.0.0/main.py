import easygui
import sys
import os
from tkinter.filedialog import *
try:
    pydir = open('.\cfg\pydir','r',encoding='utf-8')
    dirrd = pydir.read()
    pydir.close
except FileNotFoundError:
    os.mkdir('cfg')
    npydir = open('./cfg\pydir','w+',encoding='utf-8')
    npydir.write(input('python dir>') + 'python.exe')
    npydir.close
    ninc = open('./cfg\include','w+',encoding='utf-8')
    ninc.write('''import os
import time
command = os.system
sleep = time.sleep
rename = os.rename''')
    ninc.close
    print('Done!')
if easygui.ccbox('New or open?','enter',choices=('New','Open')):
    code = easygui.codebox('Enter code.','EDIT')
else:
    op = askopenfilename(filetypes=[('homo file','*.*')])
    g = open(op,'r',encoding='utf-8')
    fg = g.read()
    f = open(op,'w+',encoding='utf-8')      
    code = easygui.codebox('Enter code.','EDIT',text=fg)
i = easygui.buttonbox('Save?','Save?',('Save!','No!'))
if i == 'Save!':
    save = asksaveasfilename(filetypes=[('homo file','*.*')])
    sv = open(save,'w+',encoding='utf-8')
    try:
        sv.write(code)
    except TypeError:
        sv.write('  ')
elif i == 'No!':
    sys.exit()
inc = open('./cfg\\include','r',encoding='utf-8')
include = inc.read()
rdd = include + '\n' + code
s = open('tmp.py','w+',encoding='utf-8')
s.write(rdd)
s.close