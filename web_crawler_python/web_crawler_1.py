#---------------- title ----------------
# program:  web_crawler_1 (Baidu Tieba thread web crawler)
# version:  0.1
# author:   xiao huang
# date:     20150309
# language: Python 2.7.9
# step:     input the Baidu Tieba thread address(delete the last page number), set up the start page and end page
# function: download the correlating page and save as the lacal .html file
#---------------- title ----------------


import urllib2

# define the main function
def web_crawler_1(tieba_url, start_page, end_page):

    for i in range(start_page, end_page + 1):

        f_name = str(i) + '.html'
        new_file = open(f_name, 'w')

        print 'Downloading the #' + str(i) + ' page file ...'
        print 'Saving as file ' + f_name + ' ...'

        complete_url = tieba_url + str(i)
        req = urllib2.Request(complete_url)
        response = urllib2.urlopen(req)
        html = response.read()

        new_file.write(html)
        new_file.close()

    print 'Dowloading finished.'

#---------------- argument ----------------

# this gives a test sample (this is one of threads in BIT's Tieba in Baidu)
# tieba_url = 'http://tieba.baidu.com/p/2501134464?pn='
# start_page = 1
# end_page = 5

tieba_url = str(raw_input('Input your Tieba thread address, and delete the number after "pn=":\n'))
start_page = int(raw_input('Input the start page:\n'))
end_page = int(raw_input('Input the end page:\n'))
#---------------- argument ----------------

# invoke
web_crawler_1(tieba_url, start_page, end_page)