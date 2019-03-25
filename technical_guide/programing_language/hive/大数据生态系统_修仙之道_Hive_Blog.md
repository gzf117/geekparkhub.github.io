	
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
> Hive 由FaceBook开源并用于解决海量结构化日志的数据统计分析.
> 
> Hive是基于Hadoop的一个数据仓库工具,可以将结构化的数据文件映射为一张数据表,并提供类SQL查询功能.
> 
> 本质是: 将HQL转化成MapReduce程序.
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hive/start_001.jpg)
> 
> 1.Hive处理的数据存储在HDFS.
> 
> 2.Hive分析数据底层的实现是MapReduce.
> 
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
> 支持MapReduce / Teza / Spark 等多种计算引擎,开发者可根据不同的数据处理场景选择合适的计算引擎.
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
> 5.Hive支持开发者自定义函数,开发者可以根据自己的需求来实现自己的函数.
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

> Hive通过给开发者提供的一系列交互接口,接收到开发者的指令(SQL),使用自己的Driver,结合元数据(MetaStore),将这些指令翻译成MapReduce,提交到Hadoop中执行,最后,将执行返回的结果输出到开发者交互接口.
> 
#### 1.用户接口: Client
> CLI (Hive Shell) / JDBC/ODBC (Java访问Hive) / WEBUI (浏览器访问Hive).
#### 2.元数据: Metastore
> 元数据包括: 表名、表所属的数据库(默认是default)、表的拥有者,列/分区字段/表的类型(是否是外部表),表的数据所在目录等.
> 
> 默认存储在自带的derby数据库中,推荐使用MySQL存储Metastore.
#### 3.Hadoop
> 使用HDFS进行存储,使用MapReduce进行计算.
#### 4.驱动器: Driver
> (1) 解析器(SQL  Parser): 将SQL字符串转换成抽象语法树AST,这一步一般都用第三方工具库完成,比如antlr,对AST进行语法分析,比如表是否存在、字段是否存在、SQL语义是否有误.
> 
> (2) 编译器(Physical Plan): 将AST编译生成逻辑执行计划.
> 
> (3) 优化器(Query Optimizer): 对逻辑执行计划进行优化.
> 
> (4) 执行器(Execution): 把逻辑执行计划转换成可以运行的物理计划,对于Hive来说,就是MR & Spark.

### 1.4 HIve & 数据库比较
> 由于Hive采用了类似SQL的查询语言HQL(Hive Query Language),因此很容易将Hive理解为数据库.
> 
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
> 5.以apache-hive-1.2.1-bin.tar.gz 稳定版本 为实例进行安装.

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

#### 5. 配置环境变量
> 在system中配置HIVE_HOME
``` powershell
[root@systemhub711 hive]# vim /etc/profile
```
``` powershell

## SET JAVA_HOME
JAVA_HOME=/opt/module/jdk1.8.0_162
PATH=/opt/module/jdk1.8.0_162/bin:$PATH
export JAVA_HOME PATH

## SET TOMCAT_HOME
TOMCAT_HOME=/opt/module/apache-tomcat
export TOMCAT_HOME

## SET HADOOP_HOME
HADOOP_HOME=/opt/module/hadoop
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin

## SET HIVE_HOME
export HIVE_HOME=/opt/module/hive
export PATH=$PATH:$HIVE_HOME/bin
```
> 配置完毕,按ESC,输入:wq 保存并退退出.
> 
> 更新配置信息
``` powershell
[root@systemhub711 hive]# source /etc/profile
```
> 在hive-env.sh配置HADOOP_HOME路径 & 配置HIVE_CONF_DIR路径
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

### 2.2 启动Hadoop集群
#### 2.2.3 启动 HDFS Service
``` powershell
[root@systemhub511 ~]# cd /opt/module/hadoop/
[root@systemhub511 hadoop]# start-dfs.sh
```
#### 2.2.4 启动 Yarn Service
``` powershell
[root@systemhub611 ~]# cd /opt/module/hadoop/
[root@systemhub611 hadoop]# start-yarn.sh
```
#### 2.2.5 jps 查看集群进程
``` powershell
[root@systemhub511 hadoop]# jps
11121 NameNode
15719 Jps
11323 DataNode
15118 NodeManager
[root@systemhub511 hadoop]# 

[root@systemhub611 hadoop]# jps
9106 NodeManager
5865 DataNode
10650 Jps
7629 ResourceManager
[root@systemhub611 hadoop]# 

[root@systemhub711 hadoop]# jps
3089 Jps
30667 DataNode
1629 NodeManager
30974 SecondaryNameNode
[root@systemhub711 hadoop]# 
```
#### 2.2.6 在HDFS上创建目录
> 创建/tmp和/user/hive/warehouse两个目录并修改同组权限为可写
```
[root@systemhub611 hadoop]# hadoop fs -mkdir /tmp
[root@systemhub511 hadoop]# hadoop fs -mkdir -p  /user/hive/warehouse
```
```
[root@systemhub511 hadoop]# hadoop fs -chmod 777 /tmp
[root@systemhub511 hadoop]# hadoop fs -chmod 777 /user/hive/warehouse
```

#### 2.2.7 Hive基本操作
##### 2.2.7.1 启动 Hive Service
``` powershell
[root@systemhub711 hive]# bin/hive
Logging initialized using configuration in jar:file:/opt/module/hive/lib/hive-common-1.2.1.jar!/hive-log4j.properties
hive> 
```
##### 2.2.7.2 查看数据库
```
hive> show databases;
OK
default
Time taken: 0.039 seconds, Fetched: 1 row(s) 
```
##### 2.2.7.3 打开默认数据库
```
hive> use default;
OK
Time taken: 0.06 seconds
hive> 
```
##### 2.2.7.4 显示default数据库中的表
```
hive> show tables;
OK
Time taken: 0.136 seconds
hive> 
```
##### 2.2.7.5 创建一张表
```
hive> create table test(id int,name string);
OK
Time taken: 0.584 seconds
```
##### 2.2.7.6 显示数据库中有几张表
```
hive> show tables;
OK
test
Time taken: 0.043 seconds, Fetched: 1 row(s)
hive> 
```
##### 2.2.7.7 查看表的结构
```
hive> desc test;
OK
id                      int                                         
name                    string                                      
Time taken: 0.181 seconds, Fetched: 2 row(s)
hive> 
```
##### 2.2.7.8 向表中插入数据
```
hive> insert into test values(1,"TestUser001");
Query ID = root_20190325104557_f36e7f6e-0254-4e4e-9216-60f08042dabb
Total jobs = 3
Launching Job 1 out of 3
Number of reduce tasks is set to 0 since there's no reduce operator
Starting Job = job_1553477836311_0001, Tracking URL = http://systemhub611:8088/proxy/application_1553477836311_0001/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553477836311_0001
Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 0
2019-03-25 10:46:18,198 Stage-1 map = 0%,  reduce = 0%
2019-03-25 10:46:26,679 Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 1.96 sec
MapReduce Total cumulative CPU time: 1 seconds 960 msec
Ended Job = job_1553477836311_0001
Stage-4 is selected by condition resolver.
Stage-3 is filtered out by condition resolver.
Stage-5 is filtered out by condition resolver.
Moving data to: hdfs://systemhub511:9000/user/hive/warehouse/test/.hive-staging_hive_2019-03-25_10-45-57_843_1729594574229184317-1/-ext-10000
Loading data to table default.test
Table default.test stats: [numFiles=1, numRows=1, totalSize=14, rawDataSize=13]
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 1   Cumulative CPU: 1.96 sec   HDFS Read: 3566 HDFS Write: 82 SUCCESS
Total MapReduce CPU Time Spent: 1 seconds 960 msec
OK
Time taken: 31.477 seconds
hive> 
```
##### 2.2.7.9 查询表中数据
```
hive> select * from test;
OK
1       TestUser001
Time taken: 0.144 seconds, Fetched: 1 row(s)
hive>
```
##### 2.2.7.10 退出hive
```
hive> quit;
[root@systemhub711 hive]# 
```

#### 2.2.8 Hive实操案例
##### 2.2.8.1 将本地文件导入Hive中
> 需求: 将本地 /opt/module/datas/test.txt,这个目录下的数据导入到hive的test(id int, name string)数据表中.
###### 1.数据准备
> 在/opt/module/目录下创建datas
> 
> 在/opt/module/datas/目录下创建test.txt文件并添加数据,以Tab键间隔
```
[root@systemhub711 ~]# cd /opt/module/
[root@systemhub711 module]# mkdir datas
[root@systemhub711 module]# cd datas/
[root@systemhub711 datas]# touch test.txt
[root@systemhub711 datas]# ll
total 0
-rw-r--r--. 1 root root 0 Mar 25 16:02 test.txt
[root@systemhub711 datas]#
[root@systemhub711 datas]# vim test.txt
```
```
1       TestUser001
2       TestUser002
3       TestUser003
4       TestUser004
```
###### 2.启动 Hadoop集群 & Hive
```
[root@systemhub711 ~]# cd /opt/module/hive/
[root@systemhub711 hive]# bin/hive
Logging initialized using configuration in jar:file:/opt/module/hive/lib/hive-common-1.2.1.jar!/hive-log4j.properties
hive>
```
###### 3.创建test001数据表,并声明文件分隔符"\t"
```
hive> create table test001(id int,name string) row format delimited fields terminated by "\t";
OK
Time taken: 0.222 seconds
hive> 
```
###### 4.将文件加载到数据表中
```
hive> load data local inpath "/opt/module/datas/test.txt" into table test001;
Loading data to table default.test
Table default.test stats: [numFiles=1, totalSize=56]
OK
Time taken: 0.479 seconds
hive>
```
###### 5.查询数据
```
hive> select * from test;
OK
1       TestUser001
2       TestUser002
3       TestUser003
4       TestUser004
Time taken: 0.076 seconds, Fetched: 4 row(s)
hive> 
```
##### 2.2.8.2 MySql安装
###### 1.安装包准备
> 查看mysql是否安装,如果安装了,卸载mysql.
```
[root@systemhub711 ~]# rpm -qa|grep mysql
mysql-libs-5.1.71-1.el6.x86_64
[root@systemhub711 ~]# rpm -e --nodeps mysql-libs-5.1.71-1.el6.x86_64
[root@systemhub711 ~]# 
```
> 解压mysql-libs.zip文件到当前目录.
```
[root@systemhub711 ~]# cd /opt/software/
[root@systemhub711 software]# unzip mysql-libs.zip
Archive:  mysql-libs.zip
   creating: mysql-libs/
  inflating: mysql-libs/MySQL-client-5.6.24-1.el6.x86_64.rpm  
  inflating: mysql-libs/mysql-connector-java-5.1.27.tar.gz  
  inflating: mysql-libs/MySQL-server-5.6.24-1.el6.x86_64.rpm  
```

##### 2.2.8.3 安装MySql服务端
> 安装mysql服务端
```
[root@systemhub711 mysql-libs]# rpm -ivh MySQL-server-5.6.24-1.el6.x86_64.rpm
Preparing...                ########################################### [100%]
   1:MySQL-server           ########################################### [100%]
```
> 安装mysql客户端
```
[root@systemhub711 mysql-libs]# rpm -ivh MySQL-client-5.6.24-1.el6.x86_64.rpm
Preparing...                ########################################### [100%]
   1:MySQL-client           ########################################### [100%]
[root@systemhub711 mysql-libs]# 
```
> 查看产生的随机密码
```
[root@systemhub711 mysql-libs]# cat /root/.mysql_secret
# The random password set for the root user at Mon Mar 25 17:28:10 2019 (local time): 3krFauiObIJZG_xd
[root@systemhub711 mysql-libs]# 
```
> 查看mysql状态 并 开启服务
```
[root@systemhub711 mysql-libs]# service mysql status
MySQL is not running                                       [失败]
[root@systemhub711 mysql-libs]# service mysql start
Starting MySQL..                                           [确定]
```
> 登录mysql
```
[root@systemhub711 mysql-libs]# mysql -uroot -p3krFauiObIJZG_xd
Warning: Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.6.24

Copyright (c) 2000, 2015, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
mysql> 
```
> 设置自定义登录密码
```
mysql> set password=password("000000");
Query OK, 0 rows affected (0.01 sec)
mysql> 
```
##### 2.2.8.4 MySql无主机配置
> 配置只要是root用户+password,即可在任何主机上都能登录MySQL数据库.
> 
> 登录mysql
```
[root@systemhub711 mysql-libs]# mysql -uroot -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 3
Server version: 5.6.24 MySQL Community Server (GPL)

Copyright (c) 2000, 2015, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
mysql> 
```
> 显示当前数据库
```
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| test               |
+--------------------+
4 rows in set (0.01 sec)

mysql> 
```
> 进入mysql数据库
```
mysql> use mysql;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A
Database changed
mysql>
```
> 查询mysql数据库中的所有表
```
mysql> show tables;
+---------------------------+
| Tables_in_mysql           |
+---------------------------+
| columns_priv              |
| db                        |
| event                     |
| func                      |
| general_log               |
| help_category             |
| help_keyword              |
| help_relation             |
| help_topic                |
| innodb_index_stats        |
| innodb_table_stats        |
| ndb_binlog_index          |
| plugin                    |
| proc                      |
| procs_priv                |
| proxies_priv              |
| servers                   |
| slave_master_info         |
| slave_relay_log_info      |
| slave_worker_info         |
| slow_log                  |
| tables_priv               |
| time_zone                 |
| time_zone_leap_second     |
| time_zone_name            |
| time_zone_transition      |
| time_zone_transition_type |
| user                      |
+---------------------------+
28 rows in set (0.00 sec)
mysql>
```
> 查询user数据表
```
mysql> select User, Host, Password from user;
+------+--------------+-------------------------------------------+
| User | Host         | Password                                  |
+------+--------------+-------------------------------------------+
| root | localhost    | *032197AE5731D4664921A6CCAC7CFCE6A0698693 |
| root | systemhub711 | *DB2C3C3C317DE3F3FEFF12C9A60985CA29A7BBCD |
| root | 127.0.0.1    | *DB2C3C3C317DE3F3FEFF12C9A60985CA29A7BBCD |
| root | ::1          | *DB2C3C3C317DE3F3FEFF12C9A60985CA29A7BBCD |
+------+--------------+-------------------------------------------+
4 rows in set (0.01 sec)
mysql> 
```
> 修改user表,把Host表内容修改为`%`
```
mysql> update user set host='%' where host='localhost';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select User, Host, Password from user;
+------+--------------+-------------------------------------------+
| User | Host         | Password                                  |
+------+--------------+-------------------------------------------+
| root | %            | *032197AE5731D4664921A6CCAC7CFCE6A0698693 |
| root | systemhub711 | *DB2C3C3C317DE3F3FEFF12C9A60985CA29A7BBCD |
| root | 127.0.0.1    | *DB2C3C3C317DE3F3FEFF12C9A60985CA29A7BBCD |
| root | ::1          | *DB2C3C3C317DE3F3FEFF12C9A60985CA29A7BBCD |
+------+--------------+-------------------------------------------+
4 rows in set (0.00 sec)
mysql> 
```
> 删除root用户的其他host
```
mysql> delete from user where Host='systemhub711';
Query OK, 1 row affected (0.00 sec)

mysql> delete from user where Host='127.0.0.1';
Query OK, 1 row affected (0.00 sec)

mysql> delete from user where Host='::1';
Query OK, 1 row affected (0.00 sec)

mysql> select User, Host, Password from user;
+------+------+-------------------------------------------+
| User | Host | Password                                  |
+------+------+-------------------------------------------+
| root | %    | *032197AE5731D4664921A6CCAC7CFCE6A0698693 |
+------+------+-------------------------------------------+
1 row in set (0.00 sec)
mysql> 
```
> 刷新
```
mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)
mysql> 
```
> 退出
```
mysql> exit;
Bye
[root@systemhub711 mysql-libs]# 
```

##### 2.2.8.5 配置Metastore到MySql
> 1.在/opt/module/hive/conf目录下创建hive-site.xml配置文件.
```
[root@systemhub711 ~]# cd /opt/module/hive/conf/
[root@systemhub711 conf]# touch hive-site.xml
[root@systemhub711 conf]# vim hive-site.xml
```
> 2.根据官方文档配置参数,拷贝数据到hive-site.xml配置文件中 | [Hive官方配置文档](https://cwiki.apache.org/confluence/display/Hive/AdminManual+Metastore+Administration).
``` xml
<?xml version="1.0" encoding="utf-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <property>
      <name>javax.jdo.option.ConnectionURL</name>
      <value>jdbc:mysql://systemhub711:3306/metastore?createDatabaseIfNotExist=true</value>
      <description>JDBC connect string for a JDBC metastore</description>
    </property>

    <property>
      <name>javax.jdo.option.ConnectionDriverName</name>
      <value>com.mysql.jdbc.Driver</value>
      <description>Driver class name for a JDBC metastore</description>
    </property>

    <property>
       <name>javax.jdo.option.ConnectionUserName</name>
       <value>root</value>
       <description>username to use against metastore database</description>
    </property>

    <property>
       <name>javax.jdo.option.ConnectionPassword</name>
       <value>000000</value>
       <description>passwordto use against metastore database</description>
    </property>

</configuration>
```
> 驱动拷贝
> 将/opt/software/mysql-libs目录下解压mysql-connector-java-5.1.27.tar.gz驱动包.
```
[root@systemhub711 opt]# cd software/mysql-libs
[root@systemhub711 mysql-libs]# tar -zvxf mysql-connector-java-5.1.27.tar.gz
mysql-connector-java-5.1.27/
mysql-connector-java-5.1.27/docs/
mysql-connector-java-5.1.27/src/
mysql-connector-java-5.1.27/src/com/
mysql-connector-java-5.1.27/src/com/mysql/
mysql-connector-java-5.1.27/src/com/mysql/jdbc/
mysql-connector-java-5.1.27/src/com/mysql/jdbc/authentication/
```
> 将mysql-connector-java-5.1.27-bin.jar到/opt/module/hive/lib/
```
[root@systemhub711 mysql-libs]# cd mysql-connector-java-5.1.27
[root@systemhub711 mysql-connector-java-5.1.27]# ll
total 1272
-rw-r--r--. 1 root root  47173 Oct 24  2013 build.xml
-rw-r--r--. 1 root root 222520 Oct 24  2013 CHANGES
-rw-r--r--. 1 root root  18122 Oct 24  2013 COPYING
drwxr-xr-x. 2 root root   4096 Mar 25 20:56 docs
-rw-r--r--. 1 root root 872303 Oct 24  2013 mysql-connector-java-5.1.27-bin.jar
-rw-r--r--. 1 root root  61423 Oct 24  2013 README
-rw-r--r--. 1 root root  63674 Oct 24  2013 README.txt
drwxr-xr-x. 7 root root   4096 Oct 24  2013 src
[root@systemhub711 mysql-connector-java-5.1.27]# cp mysql-connector-java-5.1.27-bin.jar /opt/module/hive/lib/
[root@systemhub711 mysql-connector-java-5.1.27]# cd /opt/module/hive/lib/
[root@systemhub711 lib]# ll
-rw-r--r--.  1 root root   872303 Mar 25 20:58 mysql-connector-java-5.1.27-bin.jar
```
> 配置完毕后,先启动MySQL,查看有几个数据库,依然还是四个.
```
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| test               |
+--------------------+
4 rows in set (0.01 sec)
mysql> 
```
> 再次打开多个窗口,分别启动hive.
```
[root@systemhub711 hive]# bin/hive

Logging initialized using configuration in jar:file:/opt/module/hive/lib/hive-common-1.2.1.jar!/hive-log4j.properties
hive>
```
> 启动hive后,回到MySQL窗口查看数据库,显示增加了metastore数据库.
```
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| metastore          |
| mysql              |
| performance_schema |
| test               |
+--------------------+
5 rows in set (0.00 sec)
mysql> 
```
> 去metastore数据库 喽一眼.
```
mysql> use metastore;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A
Database changed
mysql> show tables;
+---------------------------+
| Tables_in_metastore       |
+---------------------------+
| BUCKETING_COLS            |
| CDS                       |
| COLUMNS_V2                |
| DATABASE_PARAMS           |
| DBS                       |
| FUNCS                     |
| FUNC_RU                   |
| GLOBAL_PRIVS              |
| PARTITIONS                |
| PARTITION_KEYS            |
| PARTITION_KEY_VALS        |
| PARTITION_PARAMS          |
| PART_COL_STATS            |
| ROLES                     |
| SDS                       |
| SD_PARAMS                 |
| SEQUENCE_TABLE            |
| SERDES                    |
| SERDE_PARAMS              |
| SKEWED_COL_NAMES          |
| SKEWED_COL_VALUE_LOC_MAP  |
| SKEWED_STRING_LIST        |
| SKEWED_STRING_LIST_VALUES |
| SKEWED_VALUES             |
| SORT_COLS                 |
| TABLE_PARAMS              |
| TAB_COL_STATS             |
| TBLS                      |
| VERSION                   |
+---------------------------+
29 rows in set (0.00 sec)
mysql>
```

##### 2.2.8.6 Hive常用交互命令
###### 1. Hive 帮助指令
```
[root@systemhub711 hive]# bin/hive -help
usage: hive
 -d,--define <key=value>          Variable subsitution to apply to hive
                                  commands. e.g. -d A=B or --define A=B
    --database <databasename>     Specify the database to use
 -e <quoted-query-string>         SQL from command line
 -f <filename>                    SQL from files
 -H,--help                        Print help information
    --hiveconf <property=value>   Use value for given property
    --hivevar <key=value>         Variable subsitution to apply to hive
                                  commands. e.g. --hivevar A=B
 -i <filename>                    Initialization SQL file
 -S,--silent                      Silent mode in interactive shell
 -v,--verbose                     Verbose mode (echo executed SQL to the
                                  console)
[root@systemhub711 hive]# 
```

###### 2. -e 不进入hive交互窗口,即可执行sql语句
```
[root@systemhub711 hive]# bin/hive -e "select * from test";

Logging initialized using configuration in jar:file:/opt/module/hive/lib/hive-common-1.2.1.jar!/hive-log4j.properties
OK
1       TestUser001
2       TestUser002
3       TestUser003
4       TestUser004
Time taken: 2.328 seconds, Fetched: 4 row(s)
[root@systemhub711 hive]# 
```

###### 3. -f 执行脚本中,执行sql语句
> 在/opt/module/datas目录下创建 test_hivef.hql文件
```
[root@systemhub711 hive]# cd ..
[root@systemhub711 module]# cd datas/
[root@systemhub711 datas]# touch test_hivef.hql
[root@systemhub711 datas]# ll
total 4
-rw-r--r--. 1 root root  0 Mar 25 22:24 test_hivef.hql
-rw-r--r--. 1 root root 56 Mar 25 16:46 test.txt
[root@systemhub711 datas]# vim test_hivef.hql
```
> 文件中写入正确的sql语句
```
select * from test;
```
> 执行文件中的sql语句
```
[root@systemhub711 datas]# cd /opt/module/hive/
[root@systemhub711 hive]# bin/hive -f /opt/module/datas/test_hivef.hql

Logging initialized using configuration in jar:file:/opt/module/hive/lib/hive-common-1.2.1.jar!/hive-log4j.properties
OK
1       TestUser001
2       TestUser002
3       TestUser003
4       TestUser004
Time taken: 2.012 seconds, Fetched: 4 row(s)
[root@systemhub711 hive]#
```
> 执行文件中的sql语句并将结果写入文件中
```
[root@systemhub711 hive]# bin/hive -f /opt/module/datas/test_hivef.hql > /opt/module/datas/test_hivef_result.txt

Logging initialized using configuration in jar:file:/opt/module/hive/lib/hive-common-1.2.1.jar!/hive-log4j.properties
OK
Time taken: 1.794 seconds, Fetched: 4 row(s)
[root@systemhub711 hive]# cat /opt/module/datas/test_hivef_result.txt
1       TestUser001
2       TestUser002
3       TestUser003
4       TestUser004
[root@systemhub711 hive]# 
```

##### 2.2.8.7 Hive 其他命令操作
###### 2.2.8.7.1 退出hive窗口
> 在新版的oracle数据库中两个退出指令已经没有区别了,在以前的版本是有区别.
> exit:先隐性提交数据,再退出; quit:不提交数据,退出;
```
[root@systemhub711 hive]# bin/hive
Logging initialized using configuration in jar:file:/opt/module/hive/lib/hive-common-1.2.1.jar!/hive-log4j.properties
hive> quit;
[root@systemhub711 hive]# 
[root@systemhub711 hive]# bin/hive
Logging initialized using configuration in jar:file:/opt/module/hive/lib/hive-common-1.2.1.jar!/hive-log4j.properties
hive> exit;
[root@systemhub711 hive]# 
```
###### 2.2.8.7.2 在Hive CLI命令窗口中查看hdfs文件系统
```
hive> dfs -ls / ;
Found 3 items
drwxr-xr-x   - root supergroup          0 2019-01-27 14:35 /group
drwxrwxrwx   - root supergroup          0 2019-01-25 10:09 /tmp
drwxr-xr-x   - root supergroup          0 2019-01-25 09:58 /user
hive> 
```
###### 2.2.8.7.3 在Hive CLI命令窗口中查看hdfs本地系统
```
hive> ! ls /opt/module;
apache-tomcat
datas
hadoop
hive
jdk1.8.0_162
zookeeper
hive> 
```
###### 2.2.8.7.4 查看在Hive中输入所有历史命令
> 进入到当前用户的根目录执行历史命令.
```
[root@systemhub711 module]# cd
[root@systemhub711 ~]# cat .hivehistory
show databases;
show databases;
use default;
show tables;
create table test(id int,name string);
show tables;
insert into test(1,"TestUser001");
insert into test value(1,"TestUser001");
insert into test values(1,"TestUser001");
select * form test;
select * from test;
desc test;
quit;
load data local inpath "/opt/module/datas/test.txt" into table test;
select * form test;
select * from test;
drop table test;
create table test(id int,name string) row format delimited fields terminated by "\t";
load data local inpath "/opt/module/datas/test.txt" into table test;
select * from test;
exit;
[root@systemhub711 ~]# 
```

##### 2.2.8.8 Hive常见属性配置
###### 2.2.8.8.1 Hive数据仓库位置配置
> 1.Default数据仓库最原始位置是在hdfs上的: /user/hive/warehouse路径下.
> 
> 2.在仓库目录下,没有对默认的数据库default创建文件夹,如果某张数据表属于default数据库,直接会在数据仓库目录下创建一个文件夹.
> 
> 3.修改default数据仓库原始位置.
> 1.在hive-site.xml配置文件中追加一下配置信息.
``` xml
<property>
  <name>hive.metastore.warehouse.dir</name>
  <value>/user/hive/warehouse</value>
  <description>location of default database for the warehouse</description>
</property>
```
###### 2.2.8.8.2 配置查询后信息显示
> 1.在hive-site.xml文件中添加如下配置信息,就可以实现显示当前数据库,以及查询表的头信息配置.
``` xml
<property> 
  <name>hive.cli.print.header</name>  
  <value>true</value> 
</property>

<property> 
  <name>hive.cli.print.current.db</name>  
  <value>true</value> 
</property>
```
> 2.重新启动hive,对比配置前后差异.
> 
> 配置前.
```
hive> select * from test;
OK
1       TestUser001
2       TestUser002
3       TestUser003
4       TestUser004
Time taken: 0.808 seconds, Fetched: 4 row(s)
hive> 
```

> 配置后.
```
hive (default)> select * from test;
OK
test.id test.name
1       TestUser001
2       TestUser002
3       TestUser003
4       TestUser004
Time taken: 1.708 seconds, Fetched: 4 row(s)
hive (default)> 
```

###### 2.2.8.8.3 Hive运行日志信息配置
> 1.Hive的log默认存放在/tmp/root/hive.log目录下(当前用户名下).
> 2.修改hive的log存放日志到/opt/module/hive/logs
> 2.1将hive-log4j.properties.template文件名称修改为hive-log4j.properties
```
[root@systemhub711 conf]# pwd
/opt/module/hive/conf
[root@systemhub711 conf]# ll
total 192
-rw-rw-r--. 1 root root   1139 Apr 30  2015 beeline-log4j.properties.template
-rw-rw-r--. 1 root root 168431 Jun 19  2015 hive-default.xml.template
-rw-rw-r--. 1 root root   2401 Mar 25 00:10 hive-env.sh
-rw-rw-r--. 1 root root   2662 Apr 30  2015 hive-exec-log4j.properties.template
-rw-rw-r--. 1 root root   3050 Apr 30  2015 hive-log4j.properties.template
-rw-r--r--. 1 root root   1416 Mar 25 23:11 hive-site.xml
-rw-rw-r--. 1 root root   1593 Apr 30  2015 ivysettings.xml
[root@systemhub711 conf]# mv hive-log4j.properties.template hive-log4j.properties
[root@systemhub711 conf]# ll
total 192
-rw-rw-r--. 1 root root   1139 Apr 30  2015 beeline-log4j.properties.template
-rw-rw-r--. 1 root root 168431 Jun 19  2015 hive-default.xml.template
-rw-rw-r--. 1 root root   2401 Mar 25 00:10 hive-env.sh
-rw-rw-r--. 1 root root   2662 Apr 30  2015 hive-exec-log4j.properties.template
-rw-rw-r--. 1 root root   3050 Apr 30  2015 hive-log4j.properties
-rw-r--r--. 1 root root   1416 Mar 25 23:11 hive-site.xml
-rw-rw-r--. 1 root root   1593 Apr 30  2015 ivysettings.xml
[root@systemhub711 conf]# 
```
> 在hive-log4j.properties配置文件中修改log存放位置.
```
[root@systemhub711 conf]# vim hive-log4j.properties
```

```
-rw-r--r--. 1 root root   1416 Mar 25 23:11 hive-site.xml
-rw-rw-r--. 1 root root   1593 Apr 30  2015 ivysettings.xml
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Define some default values that can be overridden by system properties
hive.log.threshold=ALL
hive.root.logger=INFO,DRFA
hive.log.dir=/opt/module/hive/logs
```

###### 2.2.8.8.4 参数配置方式
> 1.查看当前所有的配置信息.
```
hive (default)> set;
_hive.hdfs.session.path=/tmp/hive/root/3227b090-9545-485f-bae7-b9b31cadc61d
_hive.local.session.path=/tmp/root/3227b090-9545-485f-bae7-b9b31cadc61d
_hive.tmp_table_space=/tmp/hive/root/3227b090-9545-485f-bae7-b9b31cadc61d/_tmp_space.db
datanucleus.autoCreateSchema=true
datanucleus.autoStartMechanismMode=checked
datanucleus.cache.level2=false
datanucleus.cache.level2.type=none
datanucleus.connectionPoolingType=BONECP
datanucleus.fixedDatastore=false
```

> 2.参数的配置三种方式.
> 
> 2.1 配置文件方式
> 
> 默认配置文件: hive-default.xml
> 
> 开发者自定义配置文件: hive-site.xml
> 
> 注意: 开发者自定义配置会覆盖默认配置,另外,Hive也会读入Hadoop的配置,因为Hive是作为Hadoop的客户端启动的,Hive的配置会覆盖Hadoop的配置,配置文件的设定对本机启动的所有Hive进程都有效.
> 
> 2.2 命令行参数方式
> 
> 启动Hive时,可以在命令行添加`-hiveconf param=value`来设定参数.
> `仅对本次hive启动有效`
```
[root@systemhub711 hive]# bin/hive -hiveconf mapred.reduce.tasks=10
Logging initialized using configuration in file:/opt/module/hive/conf/hive-log4j.properties
hive (default)> 
```
> 查看参数设置
```
hive (default)> set mapred.reduce.tasks;
mapred.reduce.tasks=10
hive (default)> 
```
> 2.3 参数声明方式
> 可以在HQL中使用SET关键字设定参数.
> `仅对本次hive启动有效`
```
[root@systemhub711 hive]# bin/hive -hiveconf mapred.reduce.tasks=100
Logging initialized using configuration in file:/opt/module/hive/conf/hive-log4j.properties
hive (default)> 
```
> 查看参数设置
```
hive (default)> set mapred.reduce.tasks;
mapred.reduce.tasks=100
hive (default)> 
```
> 上述三种设定方式的优先级依次递增.
> 
> 即配置文件 `<` 命令行参数 `<` 参数声明.
> 
> 注意某些系统级的参数,例如log4j相关的设定,必须用前两种方式设定,因为那些参数的读取在会话建立以前已经完成了.


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