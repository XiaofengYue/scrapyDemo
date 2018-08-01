# scrapyDemo
从零开始Scrapy框架的学习，希望你我日有所进

## 介绍每个文件夹的功能及能学到的东西
  >按照我个人的学习之路排序


## **tutorial**（初步训练和自己写了个新手demo）
---
#### 了解Scrapy 最好的方法便是看官方手册（强烈推荐，介绍的很全面）
> https://docs.scrapy.org/en/latest/

#### 开启项目(了解文件夹的框架)
> scrapy startproject tutorial

#### 了解蜘蛛的初步写法 (按着手册敲样例)
>
```
第一种
# 程序自动请求start_urls列表的网页，并且自动交由parse函数下一步操作
Class quoteSpider(scrapy.Spider):
  # 蜘蛛的名字 也是运行的时候需要的名字
  name = "quote"
  # 存放需要请求的网页列表
  start_urls = ['www.baidu.com']
  
  # 执行完请求网页start_urls之后，得到response，通常在里面解析获得想要的数据
  def parse(self, response):
      pass
      
第二种
# 第一种就好比于程序自动将start_urls 放入start_requests函数中执行，并且默认的回调函数是parse
# 这里是进行重写这两个方法,方便用户添加自己的操作
Class quoteSpider(scrapy.Spider):
  # 蜘蛛的名字 也是运行的时候需要的名字
  name = "quote"
  
  # 程序的请求网页
  def start_requests(self):
      yield scrapy.Request(url='www.baidu.com', callback=self.parse_url)
      
  # 执行完请求网页start_urls之后，得到response，通常在里面解析获得想要的数据
  def parse_url(self, response):
      pass
```
>
#### Pipelines的用处和(初步使用及设置)

##### settings中设置Pipelines
* 解析时的yield item，会自动在pipelines.py中加工(比如存入数据库),我这里便是学习的存入mysql
* 如果我们要在pipelines中加工，则必须现在settings中打开pipelines的开关，settings顾名思义就是全局的设置
```
# 文件里默认注释掉了，去掉注释就好，添加自己的管道
ITEM_PIPELINES = {
    # 添加管道的文字的由来
    # tutorial文件里面的pipelines(一个py文件)里面的我们写的类(SaikrMysqlPipeline)
    # 后面的数字是优先级,一般0-1000中随便写
    'tutorial.pipelines.SaikrMysqlPipeline': 400
}
```

##### Pipelines中的方法
```
def open_spider(self, spider):
    # 蜘蛛打开管道 (可以做比如说连接数据库)

def def process_item(self, item, spider):
    # 处理item事务，还记得我们在蜘蛛解析时候的yield item吗，我们打开settings里的管道后，item会传送到这里加工

def close_spider(self, spider):
    # 蜘蛛关闭管道 (这里我做的是关闭数据库)
```

##### 一个item可以有多个管道处理
* settings中再加一个管道就好了

##### tutorial中的saikr便是爬取赛氪网存入数据库以及写入文本的demo







