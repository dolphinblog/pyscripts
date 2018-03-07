# coding:utf-8

# 脚本作用: 第一个tag如果是`函数`,将其替换为`function`

import os
import codecs
import re

postPath = '/home/vin/projects/dolphinblog/source/_posts/'
posts = os.listdir(postPath)

p = re.compile(r'(tags:\n\s+-\s+)(函数)(\n)') # 编译出pattern

for post in posts:
    postWithPath = os.path.join(postPath, post)
    if os.path.isfile(postWithPath):
        with codecs.open(postWithPath,'r+','utf-8') as f:
            text = f.read()
            text = p.sub(r'\1function\3', text) #`\1`表示第一组内容, 即`(tags:\n\s+-\s+)`匹配到的内容
            f.seek(0)
            f.truncate()
            f.write(text)
            print(post + ' is done.')
