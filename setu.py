# n站色图爬虫
import requests
import os
import re


class SetuSpider:
    def __init__(self):
        self.session = requests.Session() #下载器

    def get_image(self, url):
        """下载图片"""
        # 下载首页面的html
        index_html = self.download(url, encoding= 'utf-8')
        imgList = self.get_image_list(index_html)
        print("喔喔喔！开始下载了！！！")
        print("随时按下 ctrl+c 或者 ctrl+d 停止程序\n")
        #判断是否存在路径，创建文件夹
        index = 0
        path = "色图" + str(index)
        while (os.path.exists(path)):
            index = index + 1
            path = "色图" + str(index)
        #创建文件夹    
        os.mkdir(path)

        #开始下载每一张图片
        for i, j in enumerate(imgList):
            with open(str(path) + '/{0}.jpg'.format(i), 'wb') as file:
                file.write(requests.get(j).content)
                print("成功下载"+ str(i+1) +"张色图！")

        print("喔，好辛苦，下载终了！\n")



    def download(self, url, encoding):
        #下载html源码 （本子的首页）
        response = self.session.get(url)
        response.encoding = encoding
        html = response.text
        return html
    
    def get_image_list(self, index_html):
        divs = re.findall(r'data-src="(.*?)"  src=', index_html, re.S)
        for i,j in enumerate(divs):
            j = j.replace("/t.","/i.")
            j = j.replace("t.png",".png")
            j = j.replace("t.jpg",".jpg")
            divs[i] = j
        return divs


if __name__ == "__main__":
    hentai_url = input("Please enter the magic url from nhentai: \n")
    if "nhentai.net" not in hentai_url:
        print("你好像输错了网址！,送你舰娘的本子")
        hentai_url = 'https://nhentai.net/g/245222/'
    spider = SetuSpider() # instantiate
    spider.get_image(hentai_url)