# -*- coding: utf-8 -*-

#------------------ title -----------------------
#   program:     web_crawler_3
#   version:     0.1
#   author:      xiao huang
#   date:        20150312
#   language:    Python 2.7.9
#   step:        press "Enter" to start reading
#                the top daily jokes from the
#                Xiaohua.com input "exit" to end
#                the process
#------------------ title -----------------------


import urllib2
import re
import thread
import time
import bs4


#----------- the class to process web content -----------
class Web_Crawler:

    def __init__(self):
        self.page = 2
        self.pages = []  # current loading pages [[[2 items], [2 items], ...], [[2 items], [2 items], ...]]
        self.enable = False

    # to down load the content and return all the selected contents(in one page) in a list
    # return [[time, content], [time, content], ...]
    def getPage(self, page):
        complete_url = "http://www.xiaohua.com/duanzi/index_" + page + ".html"
        # fake headers
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
        headers = {'User-Agent': user_agent}
        # read page
        req = urllib2.Request(complete_url, headers=headers)
        response = urllib2.urlopen(req)
        page_html = response.read()
        # decode: other -> utf-8
        # encode: utf-8 -> other
        page_unicode = page_html.decode("utf-8")

        # use regex to find all need <div>
        # . -> any char
        # *? repeat any times, but the shortest match
        # pattern = re.compile(r'<div.*?class="content".*?title="(.*?)">(.*?)</div>')
        all_items = re.findall(r'<div class="content" id=".*?">([\s\S]*?)</div>', page_unicode, re.S)

        items = []
        for item in all_items:
            titles = re.findall(r'title="(.*?)"', item, re.S)
            if len(titles) == 0:
                titles = ["这个笑话"]
            title = titles[0]
            # print title[0]

            detail = re.findall(r'<div class="detail">([\s\S]*$)', item, re.S)
            if len(detail) == 0:
                detail = ["还没写好^_^"]
            soup = bs4.BeautifulSoup(detail[0])
            #print soup.get_text().replace(" ", "").replace("\n", "").replace("\t", "")
            content = soup.get_text().replace(" ", "").replace("\n", "").replace("\t", "")

            # item[0] is title, item[1] is content
            items.append([title, content])
        return items

    # this is a thread executing with the main program
    # loadPage will call getPage if pages[] length is less than 3
    # else it will sleep for 1 sec
    def loadPage(self):
        while self.enable:
            if len(self.pages) < 3:
                try:
                    new_page = self.getPage(str(self.page))
                    self.page += 1
                    self.pages.append(new_page)
                    # print str(self.page) + ": " + str(self.pages)
                except:
                    print "Connection error. Please try later."
            else:
                time.sleep(1)

    def showPage(self, current_page):
        for item in current_page:
            print item[0] + ":"
            print item[1]
            user_input = raw_input()
            if user_input == "exit":
                self.enable = False
                break

    def start(self):
        self.enable = True

        thread.start_new_thread(self.loadPage, ())  # start a new thread to load the page

        print "Downloading ..."

        while self.enable:

            if self.pages:

                self.showPage(self.pages[0])
                del self.pages[0]
#----------- the class to process web content -----------


#----------- main program -----------

print """
------------------------------------------------
   program:     web_crawler_2
   version:     0.1
   author:      xiao huang
   date:        20150311
   language:    Python 2.7.9
   step:        press "Enter" to start reading
                the top daily jokes from the
                Xiaohua.com input "exit" to end
                the process
------------------------------------------------
"""
print 'Press "Enter" to start'
raw_input()
instance = Web_Crawler()
instance.start()