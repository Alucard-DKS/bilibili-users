import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'#将全局字体改为中文

#读取清洗过的数据
old_ = []#视频编号,观看数,收藏数,投币数,推荐数
old_ = np.loadtxt("text.csv", delimiter=",",dtype=np.int,skiprows=1)

			#分析数据，并绘制图形：

#1，视频播放量饼状图
a = old_[0:,1] #取出播放量为a
a_new = [0,0,0,0,0,0]#计数，分别对应不同量级的播放
for a_i in a:
	if a_i < 10:
		a_new[0] += 1
	elif a_i < 100:
		a_new[1] += 1
	elif a_i < 1000:
		a_new[2] += 1
	elif a_i < 10000:
		a_new[3] += 1
	elif a_i < 100000:
		a_new[4] += 1
	else:
		a_new[5] += 1
names = []
name = [u"个位",u"十位",u"百位",u"千位",u"万位",u"十万以上"] #名称
for i in name:
	names.append(i+"播放量") 
colors = ['gray','blue','green','yellow','red','purple','black']#颜色
s = sum(a_new)
s_new = []
for i in a_new:
	s_new.append(i/s*100)
explode = (0, 0.1, 0, 0, 0, 0.2)#突出度

plt.figure()
patches, l_text, p_text = plt.pie(a_new, explode=explode, labels=names,colors=colors,#绘制饼状图的函数
                                       labeldistance=1.1, autopct='%1.1f%%', shadow=False,
                                       startangle=90, pctdistance=0.6)
plt.axis('equal')
plt.title('播放量占比统计',fontsize=20)
plt.savefig('播放量占比统计',dpi=600)
plt.show()

#2,播放量，投币，收藏前三
def pq(s,m):
	p1=np.where( m == s[-1] )
	q1=old_[0:,0][p1]
	p2=np.where( m == s[-2] )
	q2=old_[0:,0][p2]
	p3=np.where( m == s[-3] )
	q3=old_[0:,0][p3]
	return [q1,q2,q3]

b = old_[0:,2]#收藏
c = old_[0:,3]#投币
d = old_[0:,4]#推荐
aa = sorted(a)
bb = sorted(b)
cc = sorted(c)
aaa=pq(aa,a)
bbb=pq(bb,b)
ccc=pq(cc,c)
file = open('aid.txt','w')
file.write(str(aaa)+"\n")
file.write(str(bbb)+"\n")
file.write(str(ccc)+"\n")
file.close()

#3,绘制散点图（硬币数-播放量）
plt.scatter(a, c, marker = 'o',color = 'blue', s = 4 ,label = '点')
plt.legend(loc = 'best')
plt.xlabel('横轴：播放量',fontsize=15,color='green')
plt.ylabel('纵轴：投币数',fontsize=15)
plt.title('散点图（硬币数-播放量）',fontsize=20)
plt.savefig('散点图',dpi=1080) 
plt.show()

#4,参与率分析用户活跃度
a_v = np.mean(a)
b_v = np.mean(b)
c_v = np.mean(c)
d_v = np.mean(d)
num = [a_v/b_v, a_v/c_v, a_v/d_v]
name_list = ['收藏','投币','点赞']
plt.bar(range(len(num)), num, color='rgb',tick_label=name_list)
plt.title('用户参与度',fontsize=20)
plt.xlabel('横轴：每一次收藏（投币/点赞）',fontsize=15,color='green')
plt.ylabel('纵轴：播放量',fontsize=15)
plt.savefig('用户参与度',dpi=1080) 
plt.show()

