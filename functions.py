import requests
import time
import json


class search:
    songnum = 100
    currentPage = 1
    songname = ""
    songmid = []
    url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?aggr=1&cr=1&flag_qc=0&p=[当前页数]&n=[数量]&w=[歌曲名]"


    @property
    def api(self):
        return self.url\
        .replace("[当前页数]",str(self.currentPage))\
        .replace("[数量]",str(self.songnum))\
        .replace("[歌曲名]",self.songname)


    def begin(self):
        self.songmid=[]
        while self.songname == "":
            self.songname = input("请输入要搜索的歌曲名：")
        else:
            req = requests.get(self.api)
            if req.status_code == 200:
                pass
            else:
                print("出错了，再试试看")
                self.songname=""
                self.begin()
                return
            temp = req.text
            left = temp.find("(") + 1
            right = temp.rfind(")")
            temp = temp[left:right]
            musicDict = json.loads(temp)
            for one in musicDict["data"]["song"]["list"]:
                temp = ""
                for singers in one["singer"]:
                    temp += singers["name"] + "/"
                temp = temp[:-1]
                self.songmid.append(one["songmid"])
                print(len(self.songmid),one["songname"],temp,one["songmid"])
            temp = input("请选择要下载的歌曲：")

            req = requests.get("https://api.233i.cn/qqmusic/?songmid="+self.songmid[int(temp)-1])
            print(req.text)





class song:
    songname = ""



