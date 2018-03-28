# coding=utf-8

import jieba
from wordcloud import WordCloud
from PIL import Image #install pillow but import PIL stead
import numpy as np

import matplotlib.pyplot as plt

with open('./19th_report.txt','r',encoding='utf-8') as f:
    nineteenth_report_text = f.read()

cut_text = ' '.join(jieba.cut(nineteenth_report_text))

# color_mask = imread('./china_blue.png')
china_mask = np.array(Image.open("./china_jpg_must.jpg")) #注意：png底图无法生成形状

cloud = WordCloud(
	background_color='white',
	#background_color=None, # 导致底色为黑色
	mask=china_mask,
	max_words=20000,
	font_path="./MSYH.TTC",
	max_font_size=120
)

#生成词云图片
word_cloud = cloud.generate(cut_text)
word_cloud.to_file('outcome.png') #保存为png要比jpg清楚

#弹出一个窗口显示
#plt.imshow(word_cloud)  
#plt.show()
