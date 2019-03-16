#!/bin/bash

if [ ! -d full_page  ];then
  mkdir full_page
  wget -k --level=1 $1 -P ./full_page/
else
  wget -k --level=1 $1 -P ./full_page/
fi

var=$1
page_name=${var##*/}
page_pr=${page_name%%.*}
sed -i '/<head>/ r js.txt' ./full_page/$page_pr.html

if [ ! -d pdfs  ];then
  mkdir pdfs
  google-chrome --headless --disable-gpu --print-to-pdf=./pdfs/$page_pr.pdf ./full_page/$page_pr.html
  mv ./pdfs/$page_pr.pdf ./pdfs/$2.pdf
else
  google-chrome --headless --disable-gpu --print-to-pdf=./pdfs/$page_pr.pdf ./full_page/$page_pr.html
  mv ./pdfs/$page_pr.pdf ./pdfs/$2.pdf
fi

