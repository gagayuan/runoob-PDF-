1,此脚本用来下载runoob教程为pdf文件,可用来给学习者来打印下来.
  pdf文件已经下载至 runoob 文件夹.
  若想下载至您的本地,运行
      python3 runoob_crawl.py

2,运行时会包含的错误:
    ERROR:gpu_process_transport_factory.cc(967)] Lost UI shared context.
这是chrome内在一个小bug,新版本已经修复.

3,merge_pdf_with_toc.py可用来合并pdf,并添加TOC,非常强大.(copy自国外的牛人)

4,可以在clean.js设置html的字体,宽度,样式,再保存到pdf

5,html网页转换至pdf的一些尝试:
         ①:用selenium只能下载一张长图pdf,很不完美.
         ②:用phantomjs可以下载文字可选中的pdf,但是不能分页,pdf高度也难以设置

6,google-chrome --print-to-pdf 保存pdf非常好用,pdf会自动分页.

7,有四五个教程貌似什么原因解析错误中断了下载,又手动下载了下.

8，谢谢@flyfreeme的提醒，导致消失的原因是jquery，加了一行
sed -i '/<script.jquery.</script>/d' ./full_page/$page_pr.html
解决了这个问题。




