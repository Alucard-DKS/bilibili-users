from requests import *
from bs4 import *

base_url="https://api.bilibili.com/x/web-interface/archive/stat?aid="
av={'aid':'28023328'}
valid_num = 0
invalid_num =0

def getData(url):
    try:
        data=get(url,params=av)
        data.raise_for_status()
        data.encoding="utf-8"
        return data
    except:
        return "获取异常"

if __name__ == "__main__":
    object = open("text.txt","w")
    for i in range(0,100):
        url=base_url+av['aid']
        data=getData(url)
        if "权限" in data.text:
              invalid_num+=1
              av['aid']=str(eval(av['aid'])+1)
        else:      
            object.write(data.text+'\n')
            av['aid']=str(eval(av['aid'])+1)
            valid_num+=1
    object.write("total:100 valid: "+str(valid_num)+" invalid: "+str(invalid_num))
    object.close()
