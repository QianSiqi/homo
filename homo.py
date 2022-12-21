import easygui
import os
from tkinter.filedialog import *
codes = easygui.codebox('你的代码','homo语言')
include = '''import easygui
import time
say = print
msgbox = easygui.msgbox
ccbox = easygui.ccbox
codebox = easygui.codebox
ynbox = easygui.ynbox
sleep = time.sleep
'''
f = open('test1.homo','w',encoding='utf-8')
f.write(include)
f.write(codes)
f.close()
os.rename('test1.homo','test1.py')
os.system('python test1.py')
os.rename('test1.py','test1.homo')
print('编译完成！')