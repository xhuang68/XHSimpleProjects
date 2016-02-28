#------------------ title -----------------------
#   program:     web_crawler_2
#   version:     0.1
#   author:      xiao huang
#   date:        20150311
#   language:    Python 2.7.9
#   step:        press "Enter" to start reading
#                the top daily articles from the
#                Qiushibaike input "exit" to end
#                the process
#------------------ title -----------------------


import urllib2
import re
import thread    
import time    


#----------- the class to process web content -----------
class Web_Crawler:

    def __init__(self):
        self.page = 1
        self.pages = []  # current loading pages [[[2 items], [2 items], ...], [[2 items], [2 items], ...]]
        self.enable = False

    # to down load the content and return all the selected contents(in one page) in a list
    # return [[time, content], [time, content], ...]
    def getPage(self, page):
        complete_url = "http://www.qiushibaike.com/hot/page/" + page
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
        all_items = re.findall(r'<div.*?class="content".*?title="(.*?)">(.*?)</div>', page_unicode, re.S)

        items = []
        for item in all_items:
            # item[0] is time, item[1] is content
            items.append([item[0].replace("\n", ""), item[1].replace("\n", "")])
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

    def showPage(self, current_page, page):
        for item in current_page:
            print "Page #" + str(page) + " " + item[0] + " " + item[1]
            user_input = raw_input()
            if user_input == "exit":
                self.enable = False
                break

    def start(self):
        self.enable = True
        current_page_num = self.page

        thread.start_new_thread(self.loadPage, ())  # start a new thread to load the page

        print "Downloading ..."

        while self.enable:

            if self.pages:

                self.showPage(self.pages[0], current_page_num)
                del self.pages[0]
                current_page_num += 1
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
                the top daily articles from the
                Qiushibaike input "exit" to end
                the process
------------------------------------------------
"""
print 'Press "Enter" to start'
raw_input()
instance = Web_Crawler()
instance.start()