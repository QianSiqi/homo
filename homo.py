import easygui
import os
from tkinter.filedialog import *
include = '''import easygui
import time
import os
say = print
msgbox = easygui.msgbox
ccbox = easygui.ccbox
codebox = easygui.codebox
ynbox = easygui.ynbox
sleep = time.sleep
command = os.system
rename = os.rename
'''
if easygui.ccbox('请选择操作','选择：',choices=('打开','新建')):
    op = askopenfilename(filetypes=[('homo文件','*.homo')])
    f = open(op,'r',encoding='utf-8')
    txt = f.read()
    codes = easygui.codebox('你的代码','homo语言',text=txt)
    fw = open(op,'w',encoding='utf-8')
    if easygui.ccbox('保存吗？','选择：',choices=('保存','不保存')):
        if include not in txt:
            fw.write(include)
        fw.write(codes)
    fw.close()
    f.close()
    opp = op.replace('.homo','.py')
    os.rename(op,opp)
    os.system('python ' + opp)
    os.rename(opp,op)
    print('编译完成！')
    dl = open(op,'w',encoding='utf-8')
    dl.truncate()
    dl.write(codes)
    dl.close()
else:
    new = asksaveasfilename(filetypes=[('homo文件','*.homo')])
    new = new + '.homo'
    codess = easygui.codebox('你的代码','homo语言')
    fww = open(new,'w',encoding='utf-8')
    fww.write(include)
    fww.write(codess)
    fww.close()
    oppp = new.replace('.homo','.py')
    os.rename(new,oppp)
    os.system('python ' + oppp)
    os.rename(oppp,new)
    print('编译完成！')
    dll = open(new,'w',encoding='utf-8')
    dll.truncate()
    dll.write(codess)
    dll.close()
