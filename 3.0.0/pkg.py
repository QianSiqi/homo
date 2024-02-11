import easygui
if easygui.ccbox('Mode:','Mode',('insert','remove')):
    ins = easygui.enterbox('Enter:','Enter')
    o = open('./cfg\include','a',encoding='utf-8')
    o.write('\n' + ins)
else:
    op = open('./cfg\include','r',encoding='utf-8')
    rd = op.read()
    r = open('./cfg\include','w+',encoding='utf-8')
    re = easygui.enterbox('Enter:','Enter')
    #print(rd)
    rd.replace(re,'')
    print(rd)
    r.write(rd)