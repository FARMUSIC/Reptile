# #简单网站采集
# #爬取必应首页的页面数据
import requests,re
# #指定url
# url="https://cn.bing.com/"
# response = requests.get(url=url)
# #text 字符串形式的响应数据
# page_text = response.text
# print(page_text)

# with open('./bing.html','w', encoding="utf-8") as fp:
#     fp.write(page_text)
# print('爬取结束')


#网页采集器
#反爬机制 
#UA检测：门户网站的服务器监测请求对应载体的身份标识为某一款浏览器，则为正常请求；如果载体身份标识不是基于浏览器，则请求不正常，载体为爬虫
#UA 请求载体的身份标识
#UA 伪装 使得爬虫对应的身份标识伪装成浏览器，将UA封装进入进入字典
#Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36
header={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}
url="https://www.sogou.com/sogou?"
#处理url携带的参数：封装进入字典
keyword=input("搜索框：")
param={
    'query':keyword
}
print(param)
#对指定url发起请求的携带参数的，并且参数已经过处理
response = requests.get(url=url,params=param,headers=header)
#response = requests.get(url="https://cn.bing.com/search?q=%E5%BC%A0%E6%99%93%E6%B3%A2&qs=n&form=QBLH&sp=-1&pq=%E5%BC%A0xiao+bo&sc=0-8&sk=&cvid=11C8571A0B944E3485CB9206739F971C")
if response.encoding == 'ISO-8859-1':
    if requests.utils.get_encodings_from_content(response.text) == []:
        encoding = response.apparent_encoding
    else:
        encoding = requests.utils.get_encodings_from_content(response.text)[0]
        
    if re.match('^utf-8',encoding.lower()):
        content = response.text.encode('ISO-8859-1').decode('utf-8','ignore')
    elif re.match('^utf-16',encoding.lower()):
        content = response.text.encode('ISO-8859-1').decode('utf-16','ignore')
    elif encoding.lower() == 'gb2312':
        content = response.text.encode('ISO-8859-1').decode('gb2312','ignore')
    elif encoding.lower() == 'gbk':
        content = response.text.encode('ISO-8859-1').decode('gbk','ignore')#以上基本涵盖了所有中文编码，如果还有乱码，则用上面的函数打印出乱码的编码，再添加解码即可。
    else:
          pass
else:
    content = response.text
print(content[:200])
filename = keyword+'.html'
with open(filename,'w', encoding="utf-8") as fp:
     fp.write(content)
print("采集成功！")


# #中文网站编码问题 https://www.jianshu.com/p/ae9255711d27
# import requests,re
# r = requests.get('http://lib.tjufe.edu.cn/')

# #print(r.headers['content-type'])
# #print(r.encoding)
# #print(r.apparent_encoding)
# #print(requests.utils.get_encodings_from_content(r.text))

# if r.encoding == 'ISO-8859-1':
#     if requests.utils.get_encodings_from_content(r.text) == []:
#         encoding = r.apparent_encoding
#     else:
#         encoding = requests.utils.get_encodings_from_content(r.text)[0]
        
#     if re.match('^utf-8',encoding.lower()):
#         content = r.text.encode('ISO-8859-1').decode('utf-8','ignore')
#     elif re.match('^utf-16',encoding.lower()):
#         content = r.text.encode('ISO-8859-1').decode('utf-16','ignore')
#     elif encoding.lower() == 'gb2312':
#         content = r.text.encode('ISO-8859-1').decode('gb2312','ignore')
#     elif encoding.lower() == 'gbk':
#         content = r.text.encode('ISO-8859-1').decode('gbk','ignore')#以上基本涵盖了所有中文编码，如果还有乱码，则用上面的函数打印出乱码的编码，再添加解码即可。
#     else:
#           pass
# else:
#     content = r.text
# print(content[:200])


