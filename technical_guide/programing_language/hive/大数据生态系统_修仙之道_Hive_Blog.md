	
# 大数据生态系统 修仙之道 Hive Blog

@(2019-03-18)[ Docs Language:简体中文 & English|Programing Language:Hive|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)|![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg) | ![GitHub repo size in bytes](https://img.shields.io/github/repo-size/geekparkhub/geekparkhub.github.io.svg) | GeekDeveloper:[JEEP-711](https://github.com/jeep711)|Github:[github.com/geekparkhub](https://github.com/geekparkhub)|Gitee:[gitee.com/geekparkhub](https://gitee.com/geekparkhub) ]

##  🐘 Hive Technology 修仙之道 炼气化神 🐘

![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hive/hive.jpg)

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


## 1. Hive 基本概述
### 1.1 🤔 什么是Hive 🤔
> Hive 由FaceBook开源并用于解决海量结构化日志的数据统计.
> 
> Hive是基于Hadoop的一个数据仓库工具,可以将结构化的数据文件映射为一张数据表,并提供类SQL查询功能.
> 
> 本质是: 将HQL转化成MapReduce程序.
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hive/start_001.jpg)
> 
> 1.Hive处理的数据存储在HDFS.
> 2.Hive分析数据底层的实现是MapReduce.
> 3.执行程序运行在Yarn上.

### 1.1.2 Hive 特性
> Hive作为数据仓库软件,使用类SQL的HiveQL语言实现数据查询,所有Hive数据均存储在Hadoop分布式文件系统中,Hive具有以下特征.
> 
> 使用HiveQL以类似SQL查询方式轻松访问数据,将HQL查询转换为MapReduce的任务在Hadoop集群上执行,完成ETL(提取 / 转换 / 加载 / 报表 / 数据分析)等数据仓库任务.
> 
> 多种文件格式的元数据服务,包括TextFile / SequuenceFile / RCFile / ORCFile,其中默认格式为TextFile.
> 
> 直接访问HDFS文件或其他数据存储系统(如: HBase)中的文件.
> 
> 支持MapReduce / Teza / Spark等多种计算引擎,开发者可根据不同的数据处理场景选择合适的计算引擎.
> 
> 支持HPL/SQL程序语言,HPL/SQL是一种混合异构的语言,可以理解几乎任何现有的过程性SQL语言的语法和语义,有助于将传统数据仓库的业务逻辑迁移到Hadoop上,在Hadoop上实现ETL流程的有效方式.
> 
> 可以通过HiveLLAP,Yarn进行秒级别的查询检索,LLAP结合了持久查询服务器和优化的内存缓存,使Hive能够立即启动查询,避免不必要的磁盘开销,提供较佳的查询检索效率.


### 1.1.3 Hive 应用场景
> Hive构建在Hadoop文件系统之上,Hive不提供实时的查询和基于行级数据的更新操作,不适合需要低延时作用的应用,如联机事务处理相关应用.
| 类别       | 具体应用场景 |
| :-------- | :--------:|
| 数据挖掘    |   用户行为分析 / 兴趣分区 / 区域展示 |
| 非实时分析挖掘    |   日志分析 / 文本分析 |
| 数据汇总   |   用户点击量统计 / 流量统计  |
| 数据仓库   |   数据抽取 / 数据加载 / 数据转换 |


 

### 1.2 HIve 优缺点
#### 优点
> 1.操作接口采用类SQL语法,提供快速开发的能力(简单容易上手).
> 2.避免了去写MapReduce,减少开发人员的学习成本.
> 3.Hive的执行延迟比较高,因此Hive常用于数据分析,对实时性要求不高的场合.
> 4.Hive优势在于处理大数据,对于处理小数据没有优势,因为Hive的执行延迟比较高.
> 5.Hive支持用户自定义函数,用户可以根据自己的需求来实现自己的函数.
#### 缺点
> 1.Hive的HQL表达能力有限
> (1) 迭代式算法无法表达.
> (2) 数据挖掘方面不擅长.
> 
> 2.Hive的效率比较低
> (1) Hive自动生成的MapReduce作业,通常情况下不够智能化.
> (2) Hive调优比较困难,粒度较粗.

### 1.3 HIve 架构原理 🤔🤔🤔

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hive/start_002.jpg)

> Hive通过给用户提供的一系列交互接口,接收到用户的指令(SQL),使用自己的Driver,结合元数据(MetaStore),将这些指令翻译成MapReduce,提交到Hadoop中执行,最后,将执行返回的结果输出到用户交互接口.
> 
#### 1.用户接口: Client
> CLI (Hive Shell) / JDBC/ODBC(Java访问Hive) / WEBUI(浏览器访问Hive).
#### 2.元数据: Metastore
> 元数据包括: 表名、表所属的数据库(默认是default)、表的拥有者,列/分区字段/表的类型(是否是外部表),表的数据所在目录等.
> 
> 默认存储在自带的derby数据库中,推荐使用MySQL存储Metastore.
#### 3.Hadoop
> 使用HDFS进行存储,使用MapReduce进行计算.
#### 4.驱动器:Driver
> (1) 解析器(SQL  Parser): 将SQL字符串转换成抽象语法树AST,这一步一般都用第三方工具库完成,比如antlr,对AST进行语法分析,比如表是否存在、字段是否存在、SQL语义是否有误.
> 
> (2) 编译器(Physical Plan): 将AST编译生成逻辑执行计划.
> 
> (3) 优化器(Query Optimizer): 对逻辑执行计划进行优化.
> 
> (4) 执行器(Execution): 把逻辑执行计划转换成可以运行的物理计划,对于Hive来说,就是MR & Spark.

### 1.4 HIve & 数据库比较
> 由于Hive采用了类似SQL的查询语言HQL(Hive Query Language),因此很容易将Hive理解为数据库.
> 其实从结构上来看,Hive和数据库除了拥有类似的查询语言,再无类似之处,数据库可以用在Online的应用中,但是Hive是为数据仓库而设计的,清楚这一点,有助于从应用角度理解Hive的特性.
#### 1.4.1 查询语言
> 由于SQL被广泛的应用在数据仓库中,因此,专门针对Hive的特性设计了类SQL的查询语言HQL,熟悉SQL开发的开发者可以很方便的使用Hive进行开发.
#### 1.4.2 数据存储位置
> Hive是建立在Hadoop之上的,所有Hive的数据都是存储在HDFS中的,而数据库则可以将数据保存在块设备或者本地文件系统中.
#### 1.4.3 数据更新
> 由于Hive是针对数据仓库应用设计的,而数据仓库的内容是读多写少的,因此Hive中不建议对数据的改写,所有的数据都是在加载的时候确定好的.
> 
> 而数据库中的数据通常是需要经常进行修改的,因此可以使用`INSERTINTO...VALUES`添加数据,使用`UPDATE...SET`修改数据.
#### 1.4.4 索引
> Hive在加载数据的过程中不会对数据进行任何处理,甚至不会对数据进行扫描,因此也没有对数据中的某些Key建立索引.
> 
> Hive要访问数据中满足条件的特定值时,需要暴力扫描整个数据,因此访问延迟较高.
> 
> 由于MapReduce的引入,Hive可以并行访问数据,因此即使没有索引,对于大数据量的访问,Hive仍然可以体现出优势.
> 
> 数据库中,通常会针对一个或者几个列建立索引,因此对于少量的特定条件的数据的访问,数据库可以有很高的效率,较低的延迟,由于数据的访问延迟较高,决定了Hive不适合在线数据查询.
#### 1.4.5 执行
> Hive中大多数查询的执行是通过Hadoop提供的MapReduce来实现的,而数据库通常有自己的执行引擎.
#### 1.4.6 执行延迟
> Hive在查询数据的时候,由于没有索引,需要扫描整个数据表,因此延迟较高,另外一个导致Hive执行延迟高的因素是MapReduce框架.
> 
> 由于MapReduce本身具有较高的延迟,因此在利用MapReduce执行Hive查询时,也会有较高的延迟,相对的数据库的执行延迟较低,当然,这个低是有条件的,即数据规模较小,当数据规模大到超过数据库的处理能力的时候,Hive的并行计算显然能体现出优势.
#### 1.4.7 可扩展性
> 由于Hive是建立在Hadoop之上的,因此Hive的可扩展性是和Hadoop的可扩展性是一致的(世界上最大的Hadoop集群在Yahoo!,2009年的规模在4000台节点左右),而数据库由于ACID语义的严格限制,扩展行非常有限,目前最先进的并行数据库Oracle在理论上的扩展能力也只有100台左右.
#### 1.4.8 数据规模
> 由于Hive建立在集群上并可以利用MapReduce并行计算,因此可以支持很大规模的数据,对应的数据库可以支持的数据规模较小.

## 2. Hive 安装部署
### 2.1 Hive Download Link
> 1.Hive官网: [hive.apache.org/](http://hive.apache.org/)
> 
> 2.Hive文档: [cwiki.apache.org/confluence/display/Hive/](https://cwiki.apache.org/confluence/display/Hive/GettingStarted)
> 
> 3.Github: [github.com/apache/hive](https://github.com/apache/hive)
> 
> 4.Download Link: [archive.apache.org/dist/hive/](http://archive.apache.org/dist/hive/)
> 
> 5. 以apache-hive-1.2.1-bin.tar.gz 稳定版本 为实例进行安装.

#### 1. 将apache-hive-1.2.1-bin.tar.gz上传至 linux system/opt/software目录下
``` powershell
[root@systemhub711 ~]# cd /opt/software/
[root@systemhub711 software]# ll
total 526728
-rw-r--r--. 1 root root  92834839 Mar 24 23:51 apache-hive-1.2.1-bin.tar.gz
-rwxrwxrwx. 1 root root   9621331 Jan 14 09:36 apache-tomcat-8.5.33.tar.gz
-rwxrwxrwx. 1 root root 212046774 Jan 24 20:37 hadoop-2.7.2.tar.gz
-rwxrwxrwx. 1 root root 189815615 Jan 14 10:22 jdk-8u162-linux-x64.tar.gz
-rwxrwxrwx. 1 root root  35042811 Jan 17 19:18 zookeeper-3.4.10.tar.gz
```
#### 2. 解压apache-hive-1.2.1-bin.tar.gz 至 /opt/module/目录下
``` powershell
[root@systemhub711 software]# tar -zxvf apache-hive-1.2.1-bin.tar.gz -C /opt/module/
apache-hive-1.2.1-bin/NOTICE
apache-hive-1.2.1-bin/LICENSE
apache-hive-1.2.1-bin/README.txt
apache-hive-1.2.1-bin/RELEASE_NOTES.txt
apache-hive-1.2.1-bin/examples/files/emp.txt
apache-hive-1.2.1-bin/examples/files/type_evolution.avro
apache-hive-1.2.1-bin/examples/files/extrapolate_stats_partial.txt
apache-hive-1.2.1-bin/examples/files/lineitem.txt
```
#### 3. 修改apache-hive-1.2.1-bin.tar.gz包名称更改为hive
``` powershell
[root@systemhub711 software]# cd ..
[root@systemhub711 opt]# cd module/
[root@systemhub711 module]# ll
total 20
drwxr-xr-x.  8 root root 4096 Mar 24 23:53 apache-hive-1.2.1-bin
drwxr-xr-x.  9 root root 4096 Feb 24 21:55 apache-tomcat
drwxr-xr-x. 12 root root 4096 Feb 27 14:24 hadoop
drwxr-xr-x.  8 uucp  143 4096 Dec 20  2017 jdk1.8.0_162
drwxr-xr-x. 10 1001 1001 4096 Mar 23  2017 zookeeper
[root@systemhub711 module]# mv apache-hive-1.2.1-bin hive
[root@systemhub711 module]# ll
total 20
drwxr-xr-x.  9 root root 4096 Feb 24 21:55 apache-tomcat
drwxr-xr-x. 12 root root 4096 Feb 27 14:24 hadoop
drwxr-xr-x.  8 root root 4096 Mar 24 23:53 hive
drwxr-xr-x.  8 uucp  143 4096 Dec 20  2017 jdk1.8.0_162
drwxr-xr-x. 10 1001 1001 4096 Mar 23  2017 zookeeper
[root@systemhub711 module]# 
```
#### 4. 修改/opt/module/hive/conf目录下hive-env.sh.template名称更改为hive-env.sh
``` powershell
[root@systemhub711 module]# cd /opt/module/hive/conf
[root@systemhub711 conf]# ll
total 188
-rw-rw-r--. 1 root root   1139 Apr 30  2015 beeline-log4j.properties.template
-rw-rw-r--. 1 root root 168431 Jun 19  2015 hive-default.xml.template
-rw-rw-r--. 1 root root   2378 Apr 30  2015 hive-env.sh.template
-rw-rw-r--. 1 root root   2662 Apr 30  2015 hive-exec-log4j.properties.template
-rw-rw-r--. 1 root root   3050 Apr 30  2015 hive-log4j.properties.template
-rw-rw-r--. 1 root root   1593 Apr 30  2015 ivysettings.xml
[root@systemhub711 conf]# mv hive-env.sh.template hive-env.sh
[root@systemhub711 conf]# ll
total 188
-rw-rw-r--. 1 root root   1139 Apr 30  2015 beeline-log4j.properties.template
-rw-rw-r--. 1 root root 168431 Jun 19  2015 hive-default.xml.template
-rw-rw-r--. 1 root root   2378 Apr 30  2015 hive-env.sh
-rw-rw-r--. 1 root root   2662 Apr 30  2015 hive-exec-log4j.properties.template
-rw-rw-r--. 1 root root   3050 Apr 30  2015 hive-log4j.properties.template
-rw-rw-r--. 1 root root   1593 Apr 30  2015 ivysettings.xml
[root@systemhub711 conf]# 
```

#### 5. 配置hive-env.sh文件
> 配置HADOOP_HOME路径 & 配置HIVE_CONF_DIR路径
``` powershell
[root@systemhub711 conf]# echo $HADOOP_HOME
/opt/module/hadoop
[root@systemhub711 conf]# vim hive-env.sh
```
> 配置完毕,按ESC,输入:wq 保存并退退出.
``` powershell
#   fi
# fi

# The heap size of the jvm stared by hive shell script can be controlled via:
#
# export HADOOP_HEAPSIZE=1024
#
# Larger heap size may be required when running queries over large number of files or partitions. 
# By default hive shell scripts use a heap size of 256 (MB).  Larger heap size would also be 
# appropriate for hive server (hwi etc).

# Set HADOOP_HOME to point to a specific hadoop install directory
export HADOOP_HOME=/opt/module/hadoop

# Hive Configuration Directory can be controlled by:
export HIVE_CONF_DIR=/opt/module/hive/conf
```

## 🔒 尚未解锁 正在学习探索中... 尽情期待 Blog更新! 🔒

## 3. Hive 数据定义
## 4. DDL 数据定义
## 5. DML 数据操作
## 6. 查询
## 7. 函数
## 8. 压缩 & 存储
## 9. 企业级调优 

## 10. 修仙之道 技术架构迭代 登峰造极之势
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