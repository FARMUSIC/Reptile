# 爬取三国演义所有的标题和章节内容
import requests,re
from bs4 import BeautifulSoup
header={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}
url="https://www.shicimingju.com/book/sanguoyanyi.html"
#对指定url发起请求的携带参数的，并且参数已经过处理
response = requests.get(url=url,headers=header)
s=response.text
soup = BeautifulSoup(s,'lxml')
#解析章节标题
l=soup.select('.book-mulu a')
for i in l[:4]:
    param=i['href']
    t=i.text
    url_i="https://www.shicimingju.com"+str(param)
    response_i = requests.get(url=url_i,headers=header).text
    soup_i=BeautifulSoup(response_i,'lxml')
    with open('sanguo.txt','a+', encoding="utf-8") as fp:
            fp.write(i.text+'\n')
    div_c=soup_i.select('.chapter_content>p')
    for j in div_c:
        with open('sanguo.txt','a+', encoding="utf-8") as fp:
            fp.write(j.text+'\n')

print('爷爬完了!')
        


