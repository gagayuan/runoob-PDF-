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
sed -i '/<script.*jquery.*<\/script>/d' ./full_page/$page_pr.html
sed -i '/<head>/ r clean.js' ./full_page/$page_pr.html


if [ ! -d pdfs  ];then
  mkdir pdfs
  wait_excuted=`google-chrome --headless --disable-gpu --print-to-pdf=./pdfs/$page_pr.pdf ./full_page/$page_pr.html`
  mv ./pdfs/$page_pr.pdf ./pdfs/$2.pdf
else
  wait_excuted=`google-chrome --headless --disable-gpu --print-to-pdf=./pdfs/$page_pr.pdf ./full_page/$page_pr.html`
  mv ./pdfs/$page_pr.pdf ./pdfs/$2.pdf
fi

