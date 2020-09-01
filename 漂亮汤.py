#bs4 进行数据解析 bs4  lxml
'''
1.实例化BeautifulSoup对象，并且将页面源码数据加载入该对象中
 -本地文件加载
    fp=open('./o.html','r',encoding='UTF-8')
    soup = BeautifulSoup(fp,'lxml')
 -网络数据获取
2.通过BeautifulSou相关属性和方法操作
'''

#对象实例化

from bs4 import BeautifulSoup
fp=open('./o.html','r',encoding='UTF-8')
soup = BeautifulSoup(fp,'lxml')
#soup.tagName 返回第一次出现的标签  soup.p
#soup.find()  soup.find_all()  属性查找  结果—列表
#soup.find('p',class_='title')  属性定位


#soup.select('.sister')  id/类/标签 选择器  最终返回一个列表
#层级选择器 soup.select('.sister > span')  仅支持层级定位，不支持索引定位，输出结果为列表，> 表示连续层级  空格 表示多个层级



#获取标签的文本 
'''
- soup.a.text/get_text() 获取标签中所有的文本内容
- soup.a.string()  获取标签中的直系内容
'''
#获取标签的属性值 soup.a['class']
print(soup.p['class'])
