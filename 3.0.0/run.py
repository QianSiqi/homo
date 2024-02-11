import os
dir = open('cfg\\pydir','r',encoding='utf-8')
r = dir.read()
os.system(r + ' ./tmp.py')