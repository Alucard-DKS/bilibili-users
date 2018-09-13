#引入需要的函数库
from requests import *    #从服务器端获得信息的第三方库
import random              #用于构建随机数的python自带库
import multiprocessing as mp    #用于多线程的python自带库
import time                #用于添加延迟的python自带库
import sys                  #用于显示进度条信息
my_headers = [              #浏览器头
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]
proxy_list = [              #代理池
    "119.5.1.54:808"
    "122.237.104.200:80"
    "61.138.33.20:808"
    "180.119.141.231:8118"
    "223.244.252.58:45744"
    "116.192.172.131:52198"
    "116.1.11.19:80"
    "119.5.1.54:808"
]
class ShowProcess():        #显示进度条
    i = 0 
    max_steps = 0           #最大执行步数（循环次数）
    max_arrow = 50          #最大箭头数（进度条长度）
    infoDone = 'done'
    def __init__(self, max_steps, infoDone = 'Done'): #初始化
        self.max_steps = max_steps
        self.i = 0
        self.infoDone = infoDone    
    def show_process(self, i=None):     #显示函数
        if i is not None:
            self.i = i
        else:
            self.i += 1
        num_arrow = int(self.i * self.max_arrow / self.max_steps) #计算显示的箭头数量
        num_line = self.max_arrow - num_arrow           #计算显示的‘-’数量
        percent = self.i * 100.0 / self.max_steps        #计算完成进度
        process_bar = '[' + '>' * num_arrow + '-' * num_line + ']'\
                      + '%.2f' % percent + '%' + '\r'  #输出的字符串，‘\r’表示不换行回到最左边
        sys.stdout.write(process_bar)               #输出字符串（进度条）
        sys.stdout.flush()             
        if self.i >= self.max_steps:            #结束
            self.close()
    def close(self):                        #完成之后输出一行话
        print('')
        print(self.infoDone)
        self.i = 0

def getRandom_num():            #从五十万个视频中随机取出5000组
    av=[]
    for i in range(500):
        n = random.randint(31000000,31500000)
        if n not in av:
            av.append(n)
    return av

def multicore(av):      #多线程
    pool = mp.Pool()
    res = pool.map(getData,av)
    return res

def getData(aid):           #获得含有有播放，收藏，投币等数据的原始数据
    time.sleep(0.1)                     #增加每次获得的延迟，避免反爬
    proxy = random.choice(proxy_list)   
    proxies = {'http':proxy}            #代理ip，避免反爬
    header = random.choice(my_headers)  #加浏览器头，避免反爬
    base_url="https://api.bilibili.com/x/web-interface/archive/stat?aid=" 
    url=base_url+str(aid)
    try:
        data=get(url,headers={'User-Agent':header},proxies = proxies )
        data.raise_for_status()
        data.encoding="utf-8"
        return data.text + "\n"
    except:
        return ""
if __name__ == "__main__":
    n1=0
    n2=10
    av = getRandom_num()
    print("job-1 over!\n")
    object = open("text.txt","a")
    n = int(len(av)/10)-1
    process_bar = ShowProcess(n , 'job-2 over!\n')  #设置一个进度条对象
    for j in range(10,len(av),10):
        n2 = j
        data = multicore(av[n1:n2])
        for i in range(10):
            object.write(data[i])
        n1 = j
        process_bar.show_process()
    object.close()

