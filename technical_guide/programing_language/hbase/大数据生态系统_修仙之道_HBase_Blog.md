# 大数据生态系统 修仙之道 HBase Blog

@(2019-04-10)[ Docs Language:简体中文 & English|Programing Language:HBase|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)|![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg) | ![GitHub repo size in bytes](https://img.shields.io/github/repo-size/geekparkhub/geekparkhub.github.io.svg) | GeekDeveloper:[JEEP-711](https://github.com/jeep711)|Github:[github.com/geekparkhub](https://github.com/geekparkhub)|Gitee:[gitee.com/geekparkhub](https://gitee.com/geekparkhub) ]

##  🐘 HBase Technology 修仙之道 炼虚合道 🐘

![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hbase/hbase.jpg)

- **极客实验室是极客国际公园旗下为未来而构建的极客社区;**
- **我们正在构建一个活跃的小众社区,汇聚众多优秀开发者与设计师;**
- **关注极具创新精神的前沿技术&分享交流&项目合作机会等互联网行业服务;**
- **Open开放 `·` Creation创想 `|` OpenSource开放成就梦想 GeekParkHub共建前所未见!**
- **Future Vision : Establishment of the Geek Foundation;**
- **GeekParkHub GithubHome:**<https://github.com/geekparkhub>
- **GeekParkHub GiteeHome:**<https://gitee.com/geekparkhub>
- **欢迎贡献`各领域开源野生Blog`&`笔记`&`文章`&`片段`&`分享`&`创想`&`OpenSource Project`&`Code`&`Code Review`**
- 🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈 issues: [geekparkhub.github.io/issues](https://github.com/geekparkhub/geekparkhub.github.io/issues) 🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈
- **`Official Public Email`**
- Group Email：<geekparkhub@outlook.com> —— <hackerparkhub@outlook.com> —— <hackerpark@hotmail.com>
- User Email：<jeep711.home.@gmail.com> —— <jeep-711@outlook.com>
- System Email：<systemhub-711@outlook.com>
- Service Email：<servicehub-711@outlook.com>


-------------------


[TOC]



## 1. HBase 简介

### 1.1 什么是HBase
- HBase的原型是Google的BigTable论文,受到了该论文思想启发,目前作为Hadoop子项目来开发维护,用于支持结构化的数据存储.
- 官方网站：http://hbase.apache.org
- 2006年Google发表BigTable白皮书
- 2006年开始开发HBase
- 2008年北京成功开奥运会,程序员默默地将HBase开发成Hadoop的子项目
- 2010年HBase成为Apache顶级项目

> HBase是一个`高可靠性`、`高性能`、`面向列`、`可伸缩分布式存储`系统,利用HBase技术可在廉价PC Server上搭建起大规模结构化存储集群.
> 
> HBase目标是存储并处理大型数据,更具体来说是仅需使用普通的硬件配置,就能够处理由成千上万行和列所组成大型数据.
> 
> HBase是Google Bigtable开源实现,但是也有很多不同之处,比如 : Google Bigtable利用GFS作为其文件存储系统,HBase利用Hadoop HDFS作为其文件存储系统,Google运行MapReduce来处理Bigtable中的海量数据,HBase同样利用Hadoop MapReduce来处理HBase中海量数据,Google Bigtable利用Chubby作为协同服务,HBase利用Zookeeper作为对应.

### 1.2 HBase 特点
#### 1.2.1 海量存储
> HBase适合存储PB级别海量数据,在PB级别数据以及采用廉价PC存储情况下,能在几十到百毫秒内返回数据,这与HBase极易扩展性息息相关,正式因为HBase良好的扩展性,才为海量数据存储提供了便利.
#### 1.2.2 列式存储
> 列式存储也就是列族存储,HBase是根据列族来存储数据,列族下面可以有非常之多的列,列族在创建表示就必须指定.

#### 1.2.3 极易扩展
> HBase扩展性主要体现在 : 
> 基于上层处理能力(RegionServer)的扩展
> 基于存储扩展(HDFS)
> 通过横向添加RegionServer机器,进行水平扩展,提升HBase上层处理能力,提升HBase服务更多Region能力.

#### 1.2.4 高并发
> 由于大部分使用HBase架构,都是采用廉价PC,因此单个I/O延迟其实并不小,一般在几十到几百毫秒之间,高并发其实是在并发情况下,HBase单个I/O延迟下降并不多,能获得高并发,低延时服务.

#### 1.2.5 稀疏
> 稀疏主要针对HBase列的灵活性,在列族中,可以指定任意列,在列数据为空的情况下,是不会占用存储空间.


### 1.3 HBase 架构

### 1.4 HBase 角色


## 2. HBase 部署
## 3. HBase Shell
## 4. HBase 数据结构
## 5. HBase 原理
## 6. HBase API
## 7. HBase 优化













## 7. 修仙之道 技术架构迭代 登峰造极之势
![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/main/technical_framework.jpg)


-----

## 💡如何对该开源文档进行贡献💡

1. Blog内容大多是手敲,所以难免会有笔误,你可以帮我找错别字。
2. 很多知识点我可能没有涉及到,所以你可以对其他知识点进行补充。
3. 现有的知识点难免存在不完善或者错误,所以你可以对已有知识点的修改/补充。
4. 💡欢迎贡献`各领域开源野生Blog`&`笔记`&`文章`&`片段`&`分享`&`创想`&`OpenSource Project`&`Code`&`Code Review`
5. 🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈 issues: [geekparkhub.github.io/issues](https://github.com/geekparkhub/geekparkhub.github.io/issues) 🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈

### 希望每一篇文章都能够对读者们提供帮助与提升,这乃是每一位笔者的初衷                          


-----


## 💌感谢您的阅读 欢迎您的留言与建议💌

- FaceBook：[JEEP SevenEleven](https://www.facebook.com/profile.php?id=100018099483403)
- Twitter：[@JEEP7ll](https://twitter.com/JEEP7ll)
- Sina Weibo: [@JEEP-711](https://weibo.com/JEEP511)
- GeekParkHub GithubHome：<https://github.com/geekparkhub>
- GeekParkHub GiteeHome：<https://gitee.com/geekparkhub>
- Blog GardenHome：<http://www.cnblogs.com/JEEP711/>
- W3C/BlogHome：<https://www.w3cschool.cn/jeep711blog/>
- CSDN/BlogHome：<http://blog.csdn.net/jeep911>
- 51CTO/BlogHome：<http://jeep711.blog.51cto.com/>
- **`Official Public Email`**
- Group Email：<geekparkhub@outlook.com> —— <hackerparkhub@outlook.com> —— <hackerpark@hotmail.com>
- User Email：<jeep711.home.@gmail.com> —— <jeep-711@outlook.com>
- System Email：<systemhub-711@outlook.com>
- Service Email：<servicehub-711@outlook.com>



### 捐助 项目的发展离不开你的支持,请开发者喝杯☕Coffee☕吧!
![enter image description here](https://www.geekparkhub.com/docs/images/pay.jpg)

#### `致谢`：
**捐助时请备注 UserName**
| ID| UserName | Donation | Money | Consume |
|:-| :-------- | --------:| :--: |:--: |
|1 | Object | WeChatPay |  5RMB | 一杯可乐 | 
|2| 泰迪熊看月亮  | AliPay |  20RMB  | 一杯咖啡 | 
|3| 修仙道长  | WeChatPay |  10RMB | 两杯可乐 | 


## License 开源协议
[Apache License Version 2.0](https://github.com/geekparkhub/geekparkhub.github.io/blob/master/LICENSE)

---------