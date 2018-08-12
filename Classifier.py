import os
from PIL import Image
import shutil


#分辨率阈值
size_gate=1920*1080
#横屏壁纸分类目录
dir_name='Pixiv_WallPapers'
#竖屏壁纸分类目录
dir_name_mobile='Pixiv_WallPapers_Mobile'
#Pad壁纸目录
dir_name_pad='Pixiv_WallPapers_Pad'

#扫描当前目录文件
files=[file for file in os.listdir() if os.path.isfile(file)]

images=[]
HighResolution=[]
WallPapers=[]
WallPapers_Mobile=[]
WallPapers_Pad=[]
Hor_count=0
Ver_count=0
Sqr_count=0
HighResolution_count=0
#建立分类目录（不可缺少！否则shutil.move函数有歧义会导致文件丢失！）
if dir_name not in os.listdir():
	os.mkdir(dir_name)
if dir_name_mobile not in os.listdir():
	os.mkdir(dir_name_mobile)
if dir_name_pad not in os.listdir():
	os.mkdir(dir_name_pad)
	
#找到图片文件
for file in files:
	end=file.split(sep='.')[-1]
	if end=='jpg' or end=='png':
		images.append(file)
#分类
for image in images:
	image_inst=Image.open(image)
	if image_inst.size[0]*image_inst.size[1]>=size_gate:
		HighResolution_count=HighResolution_count+1
		HighResolution.append(image)
		rate=image_inst.size[0]/image_inst.size[1]
		if rate>1.2 and rate<2.5:
			Hor_count=Hor_count+1
			WallPapers.append(image)
		if rate>0.4 and rate<0.8:
			Ver_count=Ver_count+1
			WallPapers_Mobile.append(image)
		if rate>0.8 and rate<1.2:
			Sqr_count=Sqr_count+1
			WallPapers_Pad.append(image)
			

#移动横屏壁纸
for WallPaper in WallPapers:
	shutil.move(WallPaper,dir_name)
#纵屏壁纸	
for WallPaper in WallPapers_Mobile:
	shutil.move(WallPaper,dir_name_mobile)
#Pad壁纸
for WallPaper in WallPapers_Pad:
	shutil.move(WallPaper,dir_name_pad)	

	
print('Found '+str(HighResolution_count)+' high resolution picture(s).')
print(str(Hor_count)+' are for PC.')
print(str(Ver_count)+' are for mobile phone.')	
print(str(Sqr_count)+' are for Pad.')
os.system('pause')