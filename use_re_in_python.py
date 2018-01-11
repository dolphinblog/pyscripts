# coding:utf-8

# an example showing how to get specific string 
# by using re in python

import os
import codecs
import re

posts = os.listdir('./_posts/')

p = re.compile(r'title:\s(.*?)\n') # 编译出pattern

def replace_sp_chars(s):
    for sp in ['\'','"','[',']',' ','（','）','・']:
        s = s.replace(sp,'_')
    return s

titleToTitle = {}

for post in posts:
    with codecs.open('./_posts/'+post,'r','utf-8') as f:
        text = f.read()
        ms = re.findall(p, text) #查找所有文本中的pattern

        f.close()
        for m in ms:
            m = replace_sp_chars(m)
            titleToTitle[post]= m

for k,v in titleToTitle.items():
    os.rename('./_posts/'+k,'./_posts/'+v+'.md')
    print('./_posts/'+k,' => ','./_posts/'+v+'.md')


