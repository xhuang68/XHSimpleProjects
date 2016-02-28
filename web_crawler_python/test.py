# -*- coding: utf-8 -*-
import bs4
import re
import urllib2


patter1 = r'<h3 class="title"><a href=.*?title="(.*?)" target="_blank" >.*?</a></h3>'

s = u"""
<div class="content" id="content-8">
			<h3 class="title"><a href="http://www.xiaohua.com/read/9/24265/" title="估计他手法也不对，谁还试试？" target="_blank" >估计他手法也不对，谁还试试？</a></h3>
			<div class="detail">
			<div class="txtbox fn-left" id="txtbox-24265" ><div class="contFont" style="margin: 0px; padding: 0px 26px 0px 28px; border: 0px;">
			<div class="imgbox" style="margin: 0px 0px 19px; padding: 0px; border: 0px; overflow: hidden; position: relative; font-size: 16px; font-family: 微软雅黑; color: rgb(43, 43, 43); line-height: 28px; zoom: 1;">
			<div id="showcontent_1174102" class="humordatacontent  imgboxBtn" style="margin: 0px; padding: 0px; border: 0px; max-height: 700px; overflow: hidden; position: relative;">
			女同事瘦高胸小，刚跟老公在一起的时候自卑不让他摸，他很牛掰的跟她说，是她之前的男朋友不行手法不对，跟他在一起后包大，然后跟他在一起6年后，同事突然想起这事就质问他为什么还是那么小，他不屑的说“当年我哪知道，这是死面饼子发不起来”
			</div>
			</div>
			</div>
			</div>
			</div>
			<div class="function">
				<div class="function-box">
					<ul class="key">
					   <li class="ding"><a href="javascript:void(0);" onclick="clickud(24265,'up');"  class="good"><span id="scoreup-24265">2</span></a></li>
					   <li class="step"><a href="javascript:void(0);" onclick="clickud(24265,'down');"  class="bad"><span id="scoredown-24265">0</span></a></li>
					</ul>
					<div class="tags"><span>标签：</span><!--0.0000--></div>
				</div>
			</div>
		</div>
		<div class="s-shadow">
		</div>
		<div class="clear15">
		</div>
"""

#r'<div class="content" id="content-8">(.*?)</div>'

# t = re.findall(r'')

items = re.findall(r'<div class="content" id="content-8">([\s\S]*?)</div>', s, re.S)

for item in items:
    title = re.findall(r'title="(.*?)"', item, re.S)
    print title[0]

    detail = re.findall(r'<div class="detail">([\s\S]*$)', item, re.S)

    soup = bs4.BeautifulSoup(detail[0])


    print soup.get_text().replace(" ", "").replace("\n", "").replace("\t", "")
    print "test"


complete_url = "http://www.xiaohua.com/duanzi/index_" + str(2) + ".html"
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
headers = {'User-Agent': user_agent}
req = urllib2.Request(complete_url, headers=headers)
response = urllib2.urlopen(req)
page_html = response.read()

page_unicode = page_html.decode("utf-8")

all_items = re.findall(r'<div class="content" id=".*?">([\s\S]*?)</div>', page_unicode, re.S)

print all_items[0]

for item in all_items:
    title = re.findall(r'title="(.*?)"', item, re.S)
    print title[0]

    detail = re.findall(r'<div class="detail">([\s\S]*$)', item, re.S)

    soup = bs4.BeautifulSoup(detail[0])


    print soup.get_text().replace(" ", "").replace("\n", "").replace("\t", "")
    print "test"





