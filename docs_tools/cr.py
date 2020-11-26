
import os 
import time
import datetime
#html 2markdown
from markdownify import markdownify








curr_time = datetime.datetime.now()
# print(curr_time)
time_str = curr_time.strftime("%Y-%m-%d")



title = input("post:")

subtitle=''
tags=["niubi","haha"]
bigimg=[{"src": "/img/path.jpg", "des": "Path"}]
main_text="<h1>Hello, World!</h1>"
main_text = markdownify(main_text)

name=f'{time_str}-{title}.md'
file_path=os.path.join(os.getcwd(),'content/post/',name)
f1 = open(file_path,'w+')

head=f"""
---
title: {title}
subtitle: {subtitle}
date: {time_str}
tags: {tags}

---


{main_text}
"""


# 写入文件
f1.write(head)
#关闭文件
f1.close()

