import requests
from bs4 import BeautifulSoup
import bs4
import re

def getHTMLText(url,kv):
	try:
		r = requests.get(url,timeout = 30,headers = kv)
		r.raise_for_status()
		r.encoding = ('utf-8')
		print("suc")
		return r.text
	except:
		return""


if __name__ == '__main__':
        fi = open("input.txt","r")
        for i in range(9):
                avhao = fi.readline()
                avhao = re.sub("\n","",avhao)
                url = "https://www.bilibili.com/video/av"+avhao
                print(url)
                kv = {'user-agent':'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124'}
                html = getHTMLText(url,kv)
                soup = BeautifulSoup(html,"html.parser")
                f = open("output.txt","a")
                if i <3:
                        a = str(i+1)
                        f.write("播放量第"+a+"名的视频"+"\n")
                if i >2 and i<6:
                        a = str(i-2)
                        f.write("收藏量第"+a+"名的视频"+"\n")
                if i >5 and i<9:
                        a = str(i-5)
                        f.write("投币数第"+a+"名的视频"+"\n")
                f.close()
                try:
                        f = open("output.txt","a")
                        name = soup.find_all("meta",itemprop="keywords")
                        st1 = str(name[0])
                        ste1 = re.sub("[A-Za-z\!\%\[\]\\。<=->/哔哩站弹幕]", "", st1)
                        ste1 = ste1.replace("\"", "")
                        f.write("视频标题与标签"+"\n"+ste1+"\n")
                        f.close()
                except:
                        f = open("output.txt","a")
                        f.write("视频标题中存在无法识别的字符\n")
                        f.close()
                try:
                        author = soup.find_all("meta",itemprop="author")
                        st2 = str(author[0])
                        ste2 = re.sub("[A-Za-z\!\%\[\]\\。<=->/哔哩站弹幕]", "", st2)
                        ste2=ste2.replace("\"", "")
                        f = open("output.txt","a")
                        f.write("up主名字"+"\n"+ste2+"\n")
                        f.close()
                except:
                        f = open("output.txt","a")
                        f.write("up主名字中存在无法识别的字符\n")
                        f.close()
                try:
                        comment = soup.find_all("meta",itemprop="comment")
                        st3 = str(comment[0])
                        ste3 = re.sub("[A-Za-z\!\%\[\]\\。<=->/哔哩站弹幕]", "", st3)
                        ste3=ste3.replace("\"", "")
                        f = open("output.txt","a")
                        f.write("热评"+"\n"+ste3+"\n\n")
                        f.close()
                except:
                        f = open("output.txt","a")
                        f.write("热评中存在无法识别的字符\n\n")
                        f.close()
        fi.close()
