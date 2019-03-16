
# coding: utf-8

# In[57]:


import sys,re,os
import time
from PyPDF2 import utils, PdfFileReader, PdfFileWriter

from urllib.request import urlopen#用于获取网页
from bs4 import BeautifulSoup#用于解析网页
import collections

import subprocess
import shutil


# In[58]:


def crawl(crawl_url):
    html = urlopen(crawl_url)
    bsObj = BeautifulSoup(html, 'html.parser')
    left_col = bsObj.find_all(name='div',id='leftcolumn',attrs={"class":"design"})

    # print(left_col)

    html_list = left_col[0].find_all(name='a')
    html_dict = collections.OrderedDict()
    for html in html_list:
        if not html['href'].startswith('http'):
            val = "/".join(crawl_url.split("/")[0:-1]) + "/" + html['href']
            html_dict[html.string.strip()] = val
        else:
            html_dict[html.string.strip()] = html['href']

    return html_dict


# In[59]:


def html2pdf(dic):
    for ite in dic:
        #pdf_rename = ite.replace("/", "_").replace("&", "_").replace("$", "_").replace(" ", "_").replace("(", "_").replace(")", "_")
        pdf_rename = ite.replace("`","_").replace("~","_").replace("!","_").replace("@","_").replace("#","_").replace("$","_").replace("%","_").replace("^","_").replace("&","_").replace("*","_").replace("(","_").replace(")","_").replace("-","_").replace("=","_").replace(")","_").replace("+","_").replace("[","_").replace("]","_").replace("\\","_").replace("{","_").replace("}","_").replace("|","_").replace(";","_").replace("'","_").replace(":","_").replace("\"","_").replace("<","_").replace(">","_").replace("?","_").replace(",","_").replace(".","_").replace("/","_").replace(" ","_")
        output = subprocess.call('sh html2pdf.sh %s %s' %(dic[ite],pdf_rename),shell=True)
        if output != 0:
            print("Error in transfer html to pdf")


# In[60]:


def merge_pdfs(dic,chapter_name):
    filenames = []
    for ite in dic:
        pdf_rename = "./pdfs/" + ite.replace("`","_").replace("~","_").replace("!","_").replace("@","_").replace("#","_").replace("$","_").replace("%","_").replace("^","_").replace("&","_").replace("*","_").replace("(","_").replace(")","_").replace("-","_").replace("=","_").replace(")","_").replace("+","_").replace("[","_").replace("]","_").replace("\\","_").replace("{","_").replace("}","_").replace("|","_").replace(";","_").replace("'","_").replace(":","_").replace("\"","_").replace("<","_").replace(">","_").replace("?","_").replace(",","_").replace(".","_").replace("/","_").replace(" ","_") + ".pdf"
        filenames.append(pdf_rename)
    merge_pdf_core(chapter_name,filenames)


# In[61]:


# Original author Nicholas Kim, modified by Yan Pashkovsky
# New license - GPL v3
def merge_pdf_core(chapter_name,filenames):
#     options, filenames = options,filenames
#     print(options, filenames)
    output_pdf_name = chapter_name + ".pdf"
    files_to_merge = []

    # get PDF files
    for f in filenames:
        try:
            next_pdf_file = PdfFileReader(open(f, "rb"))
        except(utils.PdfReadError):
            print >>sys.stderr, "%s is not a valid PDF file." % f
            sys.exit(1)
        except(IOError):
            print >>sys.stderr, "%s could not be found." % f
            sys.exit(1)
        else:
            files_to_merge.append(next_pdf_file)

    # merge page by page
    output_pdf_stream = PdfFileWriter()
    j=0
    k=0
    for f in files_to_merge:
        for i in range(f.numPages):
            output_pdf_stream.addPage(f.getPage(i))
            if i==0:
                output_pdf_stream.addBookmark(str(filenames[k]).split("/")[-1].split(".")[-2],j)
            j = j + 1
        k += 1

    # create output pdf file
    try:
        output_pdf_file = open(output_pdf_name, "wb")
        output_pdf_stream.write(output_pdf_file)
    finally:
        output_pdf_file.close()

    # print "%s successfully created." % output_pdf_name


# In[62]:


def get_and_merge(URL,chapter_name):
    DIC = crawl(URL)
    html2pdf(DIC)
    merge_pdfs(DIC,chapter_name)


# In[63]:


# get_and_merge("http://www.runoob.com/memcached/memcached-tutorial.html",'【学习 memcached】')


# In[66]:


def main():
    url ="http://www.runoob.com/"
    html = urlopen(url)
    bsObj = BeautifulSoup(html, 'html.parser')
    pageClassPattern = re.compile("codelist codelist-desktop cate\d")
    middle_col = bsObj.find_all(name='div',attrs={"class":pageClassPattern})

    dic_total = collections.OrderedDict()
    for iii in middle_col:
        catalog = str(iii.h2).split("</i>")[-1].split("</h2>")[0].strip().replace("/", "_").replace("$", "_").replace(" ", "_").replace("(", "_").replace(")", "_")
        html_list = iii.find_all(name='a')
        dd = collections.OrderedDict()
        for ii in html_list:
            dd[ii.h4.string.strip()] = "http:" + ii['href']
        dic_total[catalog] = dd

    for i in dic_total:
        FILE_PATH = "./runoob/%s"%(i)
        if os.path.exists(FILE_PATH): 
            print('dir exists')
        else:
            os.makedirs(FILE_PATH)

    for fold in dic_total:
        for link in dic_total[fold]:
            get_and_merge(dic_total[fold][link],link)
            print("finish one")
            shutil.move("%s.pdf"%(link),"./runoob/%s"%(fold))
    print("All runoob was downloaded !")


# In[67]:


if __name__ == "__main__":
    main()

