import json

#每个line为一个视频数据，分为可访问（正常视频）的和不可访问的（已被删除的视频）
global normal
normal = 0
global un_normal
un_normal = 0

#以csv的格式存放清洗数据， 文件名text.csv
file = open("text.csv","a")
file.write("视频编号,观看数,收藏数,投币数,推荐数\n")

#数据的第一次清洗
def clear(dicte):
	global normal
	global un_normal
	if dicte["message"] != "0":
		un_normal += 1#计数反常视频
	else:
		normal += 1#计数
		data = dicte["data"]

		aid = str(data["aid"])#视频编号
		view = str(data["view"])#观看数	
		favorite = str(data["favorite"])#收藏数
		coin = str(data["coin"])#硬币数
		like = str(data["like"])#点赞数

		#存放清洗数据
		conent = aid+","+view+","+favorite+","+coin+","+like
		file.write(conent)
		file.write('\n')
		

f = open("text.txt","r+") #打开原始数据
for line in f:
	if line != "获取异常":
	#每次处理一行，数据为字典样式
		dicte = json.loads(line)
		clear(dicte)
print(normal)
print(un_normal)
f.close()
file.close()