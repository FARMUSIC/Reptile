'''
 聚焦爬虫：爬取页面中指定的内容

 通用爬虫+数据解析
 数据解析
        * 正则
        * bs4
        * xpath
数据解析原理：
        * 解析的局部内容存在标签中
        * 进行指定标签的定位
        * 标签或标签对应属性中进行提取（解析）
'''

#正则表达式

#爬取糗事百科的图片
# https://www.qiushibaike.com/imgrank/
import requests,re,os
#创建文件夹
if not os.path.exists('./qiutulibs'):
    os.mkdir('./qiutulibs')
header={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}
for i in range(1,10):
    url="https://www.qiushibaike.com/imgrank/page/"+str(i)
    #text 字符串 content 二进制 json 对象
    data = requests.get(url=url,headers=header).text
    #聚焦爬虫进行图片解析
    '''
    <div class="thumb">
    <a href="/article/123505691" target="_blank">
    <img src="//pic.qiushibaike.com/system/pictures/12350/123505691/medium/EKFI0OG370S8Z130.jpg" alt="糗事#123505691" class="illustration" width="100%" height="auto">
    </a>
    </div>
    '''
    # print(data)
    # 正则表达式
    ex=r'<div class="thumb">.*?<img src="(.*?)" alt=.*?</div>'
    img_src=re.findall(ex,data,re.S)
    # print(img_src)
    #https://pic.qiushibaike.com/system/pictures/12350/123505691/medium/EKFI0OG370S8Z130.jpg
    for src in img_src:
        img_url='https:'+src
        #对指定url发起请求的携带参数的，并且参数已经过处理
        img_data = requests.get(url=img_url,headers=header).content
        #生成图片名称
        img_name=src.split('/')[-1]
        #生成图片存储路径
        img_path='./qiutulibs/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)

        break


print('over')








