1,此脚本用来下载runoob教程为pdf文件,可用来给学习者来打印下来.
  pdf文件已经下载至 runoob 文件夹.
  若想下载至您的本地,运行
      python3 runoob_crawl.py

2,运行时会包含的错误:
    ERROR:gpu_process_transport_factory.cc(967)] Lost UI shared context.
这是chrome内在一个小bug,新版本已经修复.

3,merge_pdf_with_toc.py可用来合并pdf,并添加TOC,非常强大.(copy自国外的牛人)

4,可以在js.txt设置html的字体,宽度,样式,再保存到pdf

5,保存html网页至pdf的一些尝试:
         ①:用selenium只能下载一张长图pdf,很不完美.
         ②:用phantomjs可以下载可编辑的pdf,但是 不能分页,pdf高度难以设置

6,google-chrome --print-to-pdf 保存pdf非常好用,pdf会自动分页.

7,最后一个阿里云网页格式解析错误中断了下载,手动下载最后三个项目.




