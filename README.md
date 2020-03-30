## 功能
此脚本用来下载runoob教程为pdf文件,可用来给学习者打印或者离线学习.pdf文件已经下载至 runoob 文件夹.若想下载至您的本地,请运行
  `python3 runoob_crawl.py`

## 您可设置pdf内样式
   在clean.js设置html的字体,宽度,样式,再保存到pdf
   
## 运行时会包含的错误:
   `ERROR:gpu_process_transport_factory.cc(967)] Lost UI shared context`
   这是chrome内在一个小bug,新版本已经修复.


## html网页转换至pdf的一些尝试:
   - 用selenium只能下载一张长图pdf,很不完美.
   - 用phantomjs可以下载文字可选中的pdf,但是不能分页,pdf高度也难以设置
   - google-chrome --print-to-pdf 保存pdf非常好用,pdf会自动分页.
   - 用`merge_pdf_with_toc.py`来合并pdf,并可添加TOC,非常强大.(参考的国外牛人)
   - 谢谢@flyfreeme的提醒，导致消失的原因是jquery，加了行`sed -i '/<script.jquery.</script>/d' ./full_page/$page_pr.html`解决了。




