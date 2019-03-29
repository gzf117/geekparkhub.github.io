	
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


## 3. Hive 数据类型
### 3.1 基本数据类型
> 对于Hive的String类型相当于数据库的varchar类型,该类型是一个可变的字符串,不过它不能声明其中最多能存储多少个字符,理论上它可以存储2GB的字符数.

| Hive 数据类型      |  Java 数据类型 |   长度   |   数值   |
| :--------: | :--------:| :------: | :------: |
| TINYINT    |   byte |  1byte有符号整数  |  20  |
| SMALINT    |   short |  2byte有符号整数  |  20  |
| INT    |   int |  4byte有符号整数  |  20  |
| BIGINT    |   long |  8byte有符号整数  |  20  |
| BOOLEAN    |   boolean |  布尔类型,true或者false  |  TRUE / FALSE  |
| FLOAT    |   float |  单精度浮点数  |  3.14159  |
| DOUBLE    |   double |  双精度浮点数  |  3.14159  |
| STRING    |   string |  字符串类型,可以指定字符集,可以使用单引号或者双引号  |  'now is the time' /  "for all good men"  |
| TIMESTAMP    |   |  时间类型  |   |
| BINARY    |   |  字节数组  |    |

### 3.2 集合数据类型
> Hive有三种复杂数据类型ARRAY、MAP 和STRUCT,ARRAY和MAP与Java中的Array和Map类似,而STRUCT与C语言中的Struct类似,它封装了一个命名字段集合,复杂数据类型允许任意层次的嵌套.
> 
| 数据类型      |     描述 |   语法示例   |
| :--------: | :--------:| :------: |
| STRUCT    |   和c语言中的struct类似,都可以通过“点”符号访问元素内容,例如如果某个列的数据类型是STRUCT{first  STRING,last STRING},那么第1个元素可以通过字段.first来引用. |  struct()  |
| MAP | MAP是一组键-值对元组集合,使用数组表示法可以访问数据,例如如果某个列的数据类型是MAP,其中键->值对是’first’->’John’和’last’->’Doe’,那么可以通过字段名[‘last’]获取最后一个元素. | map() |
| ARRAY | 数组是一组具有相同类型和名称的变量的集合,这些变量称为数组的元素,每个数组元素都有一个编号,编号从零开始,例如数组值为[‘John’, ‘Doe’],那么第2个元素可以通过数组名[1]进行引用. | Array() |

#### 3.2.1 案例实操
##### 3.2.1.1 用JSON格式来表示其数据结构.
``` json
{
    "name": "TestUser",
    // Array 列表
    "friends": ["TestUser001" , "TestUser002"] ,
    // Map 键值
    "children": {
        "TestUser003": "003",
        "TestUser004": "004"
    },
    // Struct 结构
    "address": {
        "street": "china",
        "city": "beijing"
    }
}
```

##### 3.2.1.2 基于上述数据结构,在Hive里创建对应的表,并导入数据.
> 创建本地测试文件test001.txt
> 
> 注: MAP,STRUCT和ARRAY里的元素间关系都可以用同一个字符`_`下划线表示.
```
TestUser,TestUser001_TestUser002,TestUser003:003_TestUser004:004,china_beijing
DemoUser,DemoUser001_DemoUser002,DemoUser003:003_DemoUser004:004,china_beijing
```
> 在Hive创建test测试表
> 
> SQL File
``` sql
create table test001(
name string,
firends array<string>,
children map<string,int>,
address struct<street:string,city:string>
)
row format delimited fields terminated by ','
collection items terminated by '_'
map keys terminated by ':'
lines terminated by '\n';
```
> 字段解释
```
表示列分隔符
row format delimited fields terminated by ','

表示MAP STRUCT 和 ARRAY 分隔符(数据分割符号)
collection items terminated by '_'

表示MAP中的key与value分隔符
map keys terminated by ':'

表示行分隔符
lines terminated by '\n';
```
> create table
```
hive (default)> set hive.cli.print.current.db=true;
hive (default)> create table test001(
              > name string,
              > firends array<string>,
              > children map<string,int>,
              > address struct<street:string,city:string>
              > )
              > row format delimited fields terminated by ','
              > collection items terminated by '_'
              > map keys terminated by ':'
              > lines terminated by '\n';
OK
Time taken: 0.269 seconds
hive (default)> show tables;
OK
tab_name
test
test001
Time taken: 0.053 seconds, Fetched: 2 row(s)
hive (default)> 
```
> 导入文本数据到测试表
```
hive (default)> load data local inpath '/opt/module/datas/test001.txt' into table test001;
Loading data to table default.test001
Table default.test001 stats: [numFiles=1, totalSize=158]
OK
Time taken: 1.268 seconds
hive (default)> 
```
> 查询全部数据
```
hive (default)> select * from test001;
OK
test001.name    test001.firends test001.children        test001.address
TestUser        ["TestUser001","TestUser002"]   {"TestUser003":3,"TestUser004":4}       {"street":"china","city":"beijing"}
DemoUser        ["DemoUser001","DemoUser002"]   {"DemoUser003":3,"DemoUser004":4}       {"street":"china","city":"beijing"}
Time taken: 0.121 seconds, Fetched: 2 row(s)
hive (default)>	
```
> 查询三种集合列表数据
> 以下分别是ARRAY / MAP / STRUCT的访问方式.
```
hive (default)> select firends[1],children['TestUser003'],address.city from test001 where name="TestUser";
OK
_c0     _c1     city
TestUser002     3       beijing
Time taken: 0.32 seconds, Fetched: 1 row(s)
hive (default)>
```

### 3.3 类型转化
> Hive的原子数据类型是可以进行隐式转换的,类似于Java的类型转换.
> 
> 例如某表达式使用INT类型,TINYINT会自动转换为INT类型,但是Hive不会进行反向转化.
> 
> 例如,某表达式使用TINYINT类型,INT不会自动转换为TINYINT类型,它会返回错误,除非使用`CAST`操作.
#### 3.3.1 隐式类型转换规则
> 1.任何整数类型都可以隐式地转换为一个范围更广的类型,如TINYINT可以转换成INT,INT可以转换成BIGINT.
> 
> 2.所有整数类型、FLOAT和STRING类型都可以隐式地转换成DOUBLE.
> 
> 3.TINYINT,SMALLINT,INT都可以转换为FLOAT.
> 
> 4.BOOLEAN类型不可以转换为任何其它的类型.

#### 3.3.2 使用CAST显示进行数据类型转换
> 例如`CAST('1' AS INT)`将把字符串`'1'` 转换成整数1,如果强制类型转换失败,如执行`CAST('X' AS INT)`,表达式返回空值NULL.

## 4. DDL 数据定义
> DDL(Data Definition Language)数据库模式定义语言,是用于描述数据库中要存储的现实世界实体的语言.

### 4.1 创建数据库
> 创建一个数据库,数据库在HDFS上的默认存储路径是/user/hive/warehouse/*.db
> 
> 避免要创建的数据库已经存在错误,增加if not exists判断.
```
hive (default)> create database if not exists hive_db;
OK
Time taken: 0.131 seconds
hive (default)> 
```
> 当前创建的数据库会存放指定在HDFS路径.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hive/start_003.jpg)

### 4.2 查询数据库
#### 4.2.1 显示数据库
> 1.显示数据库
```
hive (default)> show databases;
OK
database_name
default
hive_db
Time taken: 0.131 seconds, Fetched: 2 row(s)
hive (default)> 
```
> 2.过滤显示查询的数据库
```
hive (default)> show databases like 'hive_db*';
OK
database_name
hive_db
Time taken: 0.039 seconds, Fetched: 1 row(s)
hive (default)> 
```
#### 4.2.2 查看数据库详情
> 1.显示数据库信息
```
hive (default)> desc database hive_db;
OK
db_name comment location        owner_name      owner_type      parameters
hive_db         hdfs://systemhub511:9000/user/hive/warehouse/hive_db.db root    USER    
Time taken: 0.042 seconds, Fetched: 1 row(s)
hive (default)> 
```
> 2.显示数据库详细信息
```
hive (default)> desc database extended hive_db;
OK
db_name comment location        owner_name      owner_type      parameters
hive_db         hdfs://systemhub511:9000/user/hive/warehouse/hive_db.db root    USER    
Time taken: 0.027 seconds, Fetched: 1 row(s)
hive (default)> 
```
#### 4.2.3 切换当前数据库
```
hive (default)> use hive_db;
OK
Time taken: 0.028 seconds
hive (hive_db)> 
```

### 4.3 修改数据库
> 用户可以使用`ALTER  DATABASE`命令为某个数据库的`DBPROPERTIES`设置键-值对属性值,来描述这个数据库的属性信息.
> 
> 数据库的其他元数据信息都是不可更改的,包括数据库名和数据库所在的目录位置.
```
hive (hive_db)> alter database hive_db set dbproperties('createtime'='2090-00-00');
OK
Time taken: 0.073 seconds
hive (hive_db)> desc database extended hive_db;
OK
db_name comment location        owner_name      owner_type      parameters
hive_db         hdfs://systemhub511:9000/user/hive/warehouse/hive_db.db root    USER    {createtime=2090-00-00}
Time taken: 0.034 seconds, Fetched: 1 row(s)
hive (hive_db)> 
```

### 4.4 删除数据库
> 如果数据库不为空,可以采用`cascade`命令,强制删除.
```
hive (default)> drop database hive_db cascade;
Time taken: 0.034 seconds
```

### 4.5 创建表
#### 4.5.1 建表语法
``` sql
CREATE [EXTERNAL] TABLE [IF NOT EXISTS] table_name 
[(col_name data_type [COMMENT col_comment], ...)] 
[COMMENT table_comment] 
[PARTITIONED BY (col_name data_type [COMMENT col_comment], ...)] 
[CLUSTERED BY (col_name, col_name, ...) 
[SORTED BY (col_name [ASC|DESC], ...)] 
INTO num_buckets BUCKETS] 
[ROW FORMAT row_format] 
[STORED AS file_format] 
[LOCATION hdfs_path]
```
> 字段解释说明
> 
> 1.`CREATE  TABLE` 创建一个指定名字的表,如果相同名字的表已经存在,则抛出异常,用户可以用`IF NOT EXISTS` 选项来忽略这个异常.
> 
> 2.`EXTERNAL`关键字可以让用户创建一个外部表,在建表的同时指定一个指向实际数据的路径(LOCATION)Hive创建内部表时,会将数据移动到数据仓库指向的路径,若创建外部表,仅记录数据所在的路径,不对数据的位置做任何改变,在删除表的时候,内部表的元数据和数据会被一起删除,而外部表只删除元数据,不删除数据.
> 
> 3.`COMMENT`: 为表和列添加注释.
> 
> 4.`PARTITIONED BY`创建分区表.
> 
> 5.`CLUSTERED BY`创建分桶表.
> 
> 6.`SORTED BY`不常用.
> 
> 7.`ROW FORMAT DELIMITED  [FIELDS TERMINATED BY char] [COLLECTIONITEMS TERMINATED BY char]`
> `[MAP KEYS TERMINATED BY char] [LINES TERMINATED BY char]  SERDE serde_name [WITH SERDEPROPERTIES (property_name=property_value, property_name=property_value, ...)]`
> 
> 开发者在建表的时候可以自定义SerDe或者使用自带的SerDe,如果没有指定ROW FORMAT 或者ROW FORMAT DELIMITED,将会使用自带的SerDe,在建表的时候,用户还需要为表指定列,开发者在指定表的列的同时也会指定自定义的SerDe,Hive通过SerDe确定表的具体的列的数据.
> 
> 8.`STORED AS` 指定存储文件类型.
> 常用的存储文件类型: `SEQUENCEFILE(二进制序列文件)`,`TEXTFILE(文本)`,`RCFILE(列式存储格式文件)`,如果文件数据是纯文本,可以使用`STORED  AS  TEXTFILE`,如果数据需要压缩,使用`STORED AS SEQUENCEFILE`.
> 
> 9.`LOCATION`: 指定表在HDFS上的存储位置.
> 
> 10.`LIKE`允许开发者复制现有的表结构,但是不复制数据.

#### 4.5.2 管理表
##### 4.5.2.1 理论
> 默认创建的表都是所谓的管理表,有时也被称为内部表.
> 
> 因为这种表,Hive会或多或少地制着数据的生命周期.
> 
> Hive默认情况下会将这些表的数据存储在由配置项`hive.metastore.warehouse.dir`(例如/user/hive/warehouse)所定义的目录的子目录下,当删除一个管理表时,Hive也会删除这个表中数据,管理表不适合和其他工具共享数据.

##### 4.5.2.2 案例实操
> 1.普通创建表.
```
hive (default)> create table if not exists test004(id int, name string)row format delimited fields terminated by '\t' stored as textfile location '/user/hive/warehouse/test004';
OK
Time taken: 0.098 seconds
hive (default)> 
```
> 2.根据查询结果创建表(查询的结果会添加到新创建的表中).
```
hive (default)> show tables;
OK
tab_name
test
test001
Time taken: 0.056 seconds, Fetched: 2 row(s)
hive (default)> create table test002 as select * from test001;
Query ID = root_20190328000840_11ef1852-3fee-44f5-a4d4-a15042411c6a
Total jobs = 3
Launching Job 1 out of 3
Number of reduce tasks is set to 0 since there's no reduce operator
Starting Job = job_1553696946343_0001, Tracking URL = http://systemhub611:8088/proxy/application_1553696946343_0001/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553696946343_0001
Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 0
Stage-1 map = 0%,  reduce = 0%
Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 1.34 sec
MapReduce Total cumulative CPU time: 1 seconds 340 msec
Ended Job = job_1553696946343_0001
Stage-4 is selected by condition resolver.
Stage-3 is filtered out by condition resolver.
Stage-5 is filtered out by condition resolver.
Moving data to: hdfs://systemhub511:9000/user/hive/warehouse/.hive-staging_hive_2019-03-28_00-08-40_557_7477541425251721483-1/-ext-10001
Moving data to: hdfs://systemhub511:9000/user/hive/warehouse/test002
Table default.test002 stats: [numFiles=1, numRows=2, totalSize=150, rawDataSize=148]
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 1   Cumulative CPU: 1.34 sec   HDFS Read: 3913 HDFS Write: 222 SUCCESS
Total MapReduce CPU Time Spent: 1 seconds 340 msec
OK
test001.name    test001.firends test001.children        test001.address
Time taken: 33.974 seconds
hive (default)> show tables;
OK
tab_name
test
test001
test002
Time taken: 0.041 seconds, Fetched: 3 row(s)
hive (default)> select * from test002;
OK
test002.name    test002.firends test002.children        test002.address
TestUser        ["TestUser001","TestUser002"]   {"TestUser003":3,"TestUser004":4}       {"street":"china","city":"beijing"}
DemoUser        ["DemoUser001","DemoUser002"]   {"DemoUser003":3,"DemoUser004":4}       {"street":"china","city":"beijing"}
Time taken: 0.157 seconds, Fetched: 2 row(s)
hive (default)> 
```
> 3.根据已经存在的表结构创建表.
```
hive (default)> create table test003 like test;
OK
Time taken: 0.116 seconds
hive (default)> select * from test003;
OK
test003.id      test003.name
Time taken: 0.066 seconds
hive (default)> 
```
> 4.查询表的类型.
```
hive (default)> desc formatted test002;
OK
col_name        data_type       comment
# col_name              data_type               comment             
                 
name                    string                                      
firends                 array<string>                               
children                map<string,int>                             
address                 struct<street:string,city:string>                           
                 
# Detailed Table Information             
Database:               default                  
Owner:                  root                         
LastAccessTime:         UNKNOWN                  
Protect Mode:           None                     
Retention:              0                        
Location:               hdfs://systemhub511:9000/user/hive/warehouse/test002     
Table Type:             MANAGED_TABLE            
Table Parameters:                
        COLUMN_STATS_ACCURATE   true                
        numFiles                1                   
        numRows                 2                   
        rawDataSize             148                 
        totalSize               150                 
        transient_lastDdlTime   1553702954          
                 
# Storage Information            
SerDe Library:          org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe       
InputFormat:            org.apache.hadoop.mapred.TextInputFormat         
OutputFormat:           org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat       
Compressed:             No                       
Num Buckets:            -1                       
Bucket Columns:         []                       
Sort Columns:           []                       
Storage Desc Params:             
        serialization.format    1                   
Time taken: 0.179 seconds, Fetched: 34 row(s)
hive (default)> 
```
#### 4.5.3 外部表
##### 4.5.3.1 理论
> 因为表是外部表,所有Hive并非认为其完全拥有这份数据,删除该表并不会删除掉这份数据,不过描述表的元数据信息会被删除掉.
##### 4.5.3.2 管理表和外部表的使用场景
> 每天将收集到的网站日志定期流入HDFS文本文件,在外部表(原始日志表)基础上做大量的统计分析,用到的中间表、结果表使用内部表存储,数据通过SELECT+INSERT进入内部表.


##### 4.5.3.3 案例实操
> 分别创建部门和员工外部表,并向表中导入数据.
###### 1.原始数据
> dept.txt & emp.txt
```
[root@systemhub711 ~]# cd /opt/module/datas/
[root@systemhub711 datas]# vim dept.txt

50      ACCOUNTING      1900
60      RESEARCH        1800
70      SALES           1700
80      OPERATIONS      1700
```
###### 2.建表语句
```
[root@systemhub711 datas]# vim emp.txt

7369    SMITH   CLERKSKLD       7902    1980-12-17      800.00  20
7499    ALLTE   SALESMANS       7689    1987-02-23      1600.00 300.00  30
7521    WAROS   SJDHHJDJX       7869    1984-06-12      1250.18 500.00  30
7566    JOSSS   JDHYHDSDS       4545    1874-05-15      2894.25 20
7654    SOCTD   MANSJUSSD       4855    1996-02-14      2852.30 30
7698    ADAMS   JUSHHWESD       4552    1985-05-16      25524.02        30
7782    JAMSK   KIHNGSEHN       7769    1991-06-23      1100.00 20
7788    FOESS   CLAEDFDFD       7698    1994-09-17      950.00  30
7939    KINGS   CLADDJHEW       7566    1993-07-12      3000.00 20
```
> 创建部门表
```
hive (default)> create external table dept(deptid int,dname string,loc int)
> row format delimited fields terminated by '\t';
OK
Time taken: 0.137 seconds
hive (default)> 
```
> 创建员工表
```
hive (default)> create external table if not exists emp(empno int,ename string,job string,mgr int,hiredate string,sal double,comm double,deptno int)
> row format delimited fields terminated by '\t';
OK
Time taken: 0.121 seconds
hive (default)> 
```
###### 3.向外部表中导入数据
```
hive (default)> load data local inpath '/opt/module/datas/dept.txt' into table dept;
Loading data to table default.dept
Table default.dept stats: [numFiles=1, totalSize=70]
OK
Time taken: 0.535 seconds
hive (default)>
```
```
hive (default)> load data local inpath '/opt/module/datas/emp.txt' into table emp;
Loading data to table default.emp
Table default.emp stats: [numFiles=1, totalSize=445]
OK
Time taken: 0.302 seconds
hive (default)> 
```
###### 4.查看创建的表
```
hive (default)> select * from dept;
OK
dept.deptid     dept.dname      dept.loc
50      ACCOUNTING      1900
60      RESEARCH        1800
70      SALES   NULL
80      OPERATIONS      1700
Time taken: 0.098 seconds, Fetched: 4 row(s)
hive (default)> select * from emp;
OK
emp.empno       emp.ename       emp.job emp.mgr emp.hiredate    emp.sal emp.comm        emp.deptno
7369    SMITH   CLERKSKLD       7902    1980-12-17      800.0   20.0    NULL
7499    ALLTE   SALESMANS       7689    1987-02-23      1600.0  300.0   30
7521    WAROS   SJDHHJDJX       7869    1984-06-12      1250.18 500.0   30
7566    JOSSS   JDHYHDSDS       4545    1874-05-15      2894.25 20.0    NULL
7654    SOCTD   MANSJUSSD       4855    1996-02-14      2852.3  30.0    NULL
7698    ADAMS   JUSHHWESD       4552    1985-05-16      25524.02        30.0    NULL
7782    JAMSK   KIHNGSEHN       7769    1991-06-23      1100.0  20.0    NULL
7788    FOESS   CLAEDFDFD       7698    1994-09-17      950.0   30.0    NULL
7939    KINGS   CLADDJHEW       7566    1993-07-12      3000.0  20.0    NULL
Time taken: 0.063 seconds, Fetched: 9 row(s)
hive (default)> 
```
###### 5.查看表格式化数据
```
hive (default)> desc formatted dept;
OK
col_name        data_type       comment
# col_name              data_type               comment             
                 
deptid                  int                                         
dname                   string                                      
loc                     int                                         
                 
# Detailed Table Information             
Database:               default                  
Owner:                  root                        
LastAccessTime:         UNKNOWN                  
Protect Mode:           None                     
Retention:              0                        
Location:               hdfs://systemhub511:9000/user/hive/warehouse/dept        
Table Type:             EXTERNAL_TABLE           
Table Parameters:                
        COLUMN_STATS_ACCURATE   true                
        EXTERNAL                TRUE                
        numFiles                1                   
        totalSize               70                  
        transient_lastDdlTime   1553705763          
                 
# Storage Information            
SerDe Library:          org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe       
InputFormat:            org.apache.hadoop.mapred.TextInputFormat         
OutputFormat:           org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat       
Compressed:             No                       
Num Buckets:            -1                       
Bucket Columns:         []                       
Sort Columns:           []                       
Storage Desc Params:             
        field.delim             \t                  
        serialization.format    \t                  
Time taken: 0.159 seconds, Fetched: 33 row(s)
hive (default)> 
```
###### 6.删除外部dept数据表,并查看结果
> 通过查看结果来看,只是删除了描述表的元数据信息,而不会删除该数据表的元数据.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hive/start_004.jpg)
> 可通过再次创建外部dept数据表,依旧可以查看到dept元数据所在.
```
hive (default)> create external table if not exists dept(deptid int,dname string,loc int)row format delimited fields terminated by '\t';
OK
Time taken: 0.039 seconds
hive (default)> select * from dept;
OK
dept.deptid     dept.dname      dept.loc
50      ACCOUNTING      1900
60      RESEARCH        1800
70      SALES   NULL
80      OPERATIONS      1700
Time taken: 0.06 seconds, Fetched: 4 row(s)
hive (default)> 
```
#### 4.5.4 管理部与外部表相互转换 
> 注: ('EXTERNAL'='TRUE') & ('EXTERNAL'='FALSE') 为固定写法,区分大小写.
##### 查询内部表数据表类型
```
hive (default)> desc formatted test001;
Table Type:             MANAGED_TABLE  
```
##### 修改内部表为外部表
```
alter table test001 set tblproperties('EXTERNAL'='TRUE');
```
##### 查询外部表数据表类型
```
hive (default)> desc formatted test001;
Table Type:             EXTERNAL_TABLE  
```
##### 修改外部表为内部表
```
alter table test001 set tblproperties('EXTERNAL'='FALSE');
```
##### 查询内部表数据表类型
```
hive (default)> desc formatted test001;
Table Type:             MANAGED_TABLE  
```


### 4.6 分区表
> 分区表实际上就是对应一个HDFS文件系统上的独立的文件夹,该文件夹下是该分区所有的数据文件,Hive中的分区就是分目录,把一个大的数据集根据业务需要分割成小的数据集,在查询时通过WHERE子句中的表达式选择查询所需要的指定的分区,这样的查询效率会提高很多.
#### 4.6.1 创建分区表语法
```
hive (default)> create table dept_partition(deptno int, dname string, loc string)
              > partitioned by (month string)
              > row format delimited fields terminated by '\t';
OK
Time taken: 0.614 seconds
hive (default)> 
```
#### 4.6.2 加载数据到分区表中
```
hive (default)> load data local inpath '/opt/module/datas/dept.txt'into table default.dept_partition partition(month='2020-00-00');
Loading data to table default.dept_partition partition (month=2020-00-00)
Partition default.dept_partition{month=2020-00-00} stats: [numFiles=1, numRows=0, totalSize=70, rawDataSize=0]
OK
Time taken: 2.37 seconds
hive (default)> load data local inpath '/opt/module/datas/dept.txt'into table default.dept_partition partition(month='2020-00-01');
Loading data to table default.dept_partition partition (month=2020-00-01)
Partition default.dept_partition{month=2020-00-01} stats: [numFiles=1, numRows=0, totalSize=70, rawDataSize=0]
OK
Time taken: 0.701 seconds
hive (default)> load data local inpath '/opt/module/datas/dept.txt'into table default.dept_partition partition(month='2020-00-02');
Loading data to table default.dept_partition partition (month=2020-00-02)
Partition default.dept_partition{month=2020-00-02} stats: [numFiles=1, numRows=0, totalSize=70, rawDataSize=0]
OK
Time taken: 0.558 seconds
hive (default)> load data local inpath '/opt/module/datas/dept.txt'into table default.dept_partition partition(month='2020-00-03');
Loading data to table default.dept_partition partition (month=2020-00-03)
Partition default.dept_partition{month=2020-00-03} stats: [numFiles=1, numRows=0, totalSize=70, rawDataSize=0]
OK
Time taken: 0.46 seconds
hive (default)> load data local inpath '/opt/module/datas/dept.txt'into table default.dept_partition partition(month='2020-00-04');
Loading data to table default.dept_partition partition (month=2020-00-04)
Partition default.dept_partition{month=2020-00-04} stats: [numFiles=1, numRows=0, totalSize=70, rawDataSize=0]
OK
Time taken: 0.461 seconds
hive (default)> load data local inpath '/opt/module/datas/dept.txt'into table default.dept_partition partition(month='2020-00-05');
Loading data to table default.dept_partition partition (month=2020-00-05)
Partition default.dept_partition{month=2020-00-05} stats: [numFiles=1, numRows=0, totalSize=70, rawDataSize=0]
OK
Time taken: 0.422 seconds
hive (default)>
```
#### 4.6.3 查询分区表中数据
##### 4.6.3.1 单分区查询
```
hive (default)> select * from dept_partition where month='2020-00-05';
OK
dept_partition.deptno   dept_partition.dname    dept_partition.loc      dept_partition.month
50      ACCOUNTING      1900    2020-00-05
60      RESEARCH        1800    2020-00-05
70      SALES           2020-00-05
80      OPERATIONS      1700    2020-00-05
Time taken: 1.186 seconds, Fetched: 4 row(s)
hive (default)>
```
##### 4.6.3.2 多分区联合查询
```
hive (default)> select * from dept_partition where month='2020-00-05'
              > union
              > select * from dept_partition where month='2020-00-04'
              > union
              > select * from dept_partition where month='2020-00-03'
              > union
              > select * from dept_partition where month='2020-00-02'
              > union
              > select * from dept_partition where month='2020-00-01';
Query ID = root_201346_e7c134f9-1082-4bd6-9588-951592861d78
Total jobs = 4
Launching Job 1 out of 4
Number of reduce tasks not specified. Estimated from input data size: 1
In order to change the average load for a reducer (in bytes):
  set hive.exec.reducers.bytes.per.reducer=<number>
In order to limit the maximum number of reducers:
  set hive.exec.reducers.max=<number>
In order to set a constant number of reducers:
  set mapreduce.job.reduces=<number>
Starting Job = job_1553737906374_0001, Tracking URL = http://systemhub611:8088/proxy/application_1553737906374_0001/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553737906374_0001
Hadoop job information for Stage-1: number of mappers: 2; number of reducers: 1
Stage-1 map = 0%,  reduce = 0%
Stage-1 map = 50%,  reduce = 0%, Cumulative CPU 1.5 sec
Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 3.42 sec
Stage-1 map = 100%,  reduce = 100%, Cumulative CPU 5.2 sec
MapReduce Total cumulative CPU time: 5 seconds 200 msec
Ended Job = job_1553737906374_0001
Launching Job 2 out of 4
Number of reduce tasks not specified. Estimated from input data size: 1
In order to change the average load for a reducer (in bytes):
  set hive.exec.reducers.bytes.per.reducer=<number>
In order to limit the maximum number of reducers:
  set hive.exec.reducers.max=<number>
In order to set a constant number of reducers:
  set mapreduce.job.reduces=<number>
Starting Job = job_1553737906374_0002, Tracking URL = http://systemhub611:8088/proxy/application_1553737906374_0002/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553737906374_0002
Hadoop job information for Stage-2: number of mappers: 2; number of reducers: 1
Stage-2 map = 0%,  reduce = 0%
Stage-2 map = 100%,  reduce = 0%, Cumulative CPU 2.87 sec
Stage-2 map = 100%,  reduce = 100%, Cumulative CPU 4.42 sec
MapReduce Total cumulative CPU time: 4 seconds 420 msec
Ended Job = job_1553737906374_0002
Launching Job 3 out of 4
Number of reduce tasks not specified. Estimated from input data size: 1
In order to change the average load for a reducer (in bytes):
  set hive.exec.reducers.bytes.per.reducer=<number>
In order to limit the maximum number of reducers:
  set hive.exec.reducers.max=<number>
In order to set a constant number of reducers:
  set mapreduce.job.reduces=<number>
Starting Job = job_1553737906374_0003, Tracking URL = http://systemhub611:8088/proxy/application_1553737906374_0003/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553737906374_0003
Hadoop job information for Stage-3: number of mappers: 2; number of reducers: 1
Stage-3 map = 0%,  reduce = 0%
Stage-3 map = 100%,  reduce = 0%, Cumulative CPU 2.67 sec
Stage-3 map = 100%,  reduce = 100%, Cumulative CPU 4.41 sec
MapReduce Total cumulative CPU time: 4 seconds 410 msec
Ended Job = job_1553737906374_0003
Launching Job 4 out of 4
Number of reduce tasks not specified. Estimated from input data size: 1
In order to change the average load for a reducer (in bytes):
  set hive.exec.reducers.bytes.per.reducer=<number>
In order to limit the maximum number of reducers:
  set hive.exec.reducers.max=<number>
In order to set a constant number of reducers:
  set mapreduce.job.reduces=<number>
Starting Job = job_1553737906374_0004, Tracking URL = http://systemhub611:8088/proxy/application_1553737906374_0004/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553737906374_0004
Hadoop job information for Stage-4: number of mappers: 2; number of reducers: 1
Stage-4 map = 0%,  reduce = 0%
Stage-4 map = 50%,  reduce = 0%, Cumulative CPU 1.21 sec
Stage-4 map = 100%,  reduce = 0%, Cumulative CPU 2.61 sec
Stage-4 map = 100%,  reduce = 100%, Cumulative CPU 4.5 sec
MapReduce Total cumulative CPU time: 4 seconds 500 msec
Ended Job = job_1553737906374_0004
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 2  Reduce: 1   Cumulative CPU: 5.2 sec   HDFS Read: 15645 HDFS Write: 434 SUCCESS
Stage-Stage-2: Map: 2  Reduce: 1   Cumulative CPU: 4.42 sec   HDFS Read: 14689 HDFS Write: 603 SUCCESS
Stage-Stage-3: Map: 2  Reduce: 1   Cumulative CPU: 4.41 sec   HDFS Read: 14810 HDFS Write: 772 SUCCESS
Stage-Stage-4: Map: 2  Reduce: 1   Cumulative CPU: 4.5 sec   HDFS Read: 15517 HDFS Write: 545 SUCCESS
Total MapReduce CPU Time Spent: 18 seconds 530 msec
OK
_u5.deptno      _u5.dname       _u5.loc _u5.month
50      ACCOUNTING      1900    2020-00-01
50      ACCOUNTING      1900    2020-00-02
50      ACCOUNTING      1900    2020-00-03
50      ACCOUNTING      1900    2020-00-04
50      ACCOUNTING      1900    2020-00-05
60      RESEARCH        1800    2020-00-01
60      RESEARCH        1800    2020-00-02
60      RESEARCH        1800    2020-00-03
60      RESEARCH        1800    2020-00-04
60      RESEARCH        1800    2020-00-05
70      SALES           2020-00-01
70      SALES           2020-00-02
70      SALES           2020-00-03
70      SALES           2020-00-04
70      SALES           2020-00-05
80      OPERATIONS      1700    2020-00-01
80      OPERATIONS      1700    2020-00-02
80      OPERATIONS      1700    2020-00-03
80      OPERATIONS      1700    2020-00-04
80      OPERATIONS      1700    2020-00-05
Time taken: 164.191 seconds, Fetched: 20 row(s)
hive (default)>
```

#### 4.6.4 增加分区
##### 4.6.4.1 创建单个分区
```
hive (default)> alter table dept_partition add partition(month='2020-00-06');
OK
Time taken: 0.501 seconds
hive (default)> 	
```
##### 4.6.4.2 同时创建多个分区
```
hive (default)> alter table dept_partition add partition(month='2020-00-07') partition(month='2020-00-08');
OK
Time taken: 0.184 seconds
hive (default)> 
```
#### 4.6.5 删除分区
##### 4.6.1 删除单个分区
```
hive (default)> alter table dept_partition drop partition(month='2020-00-06');
Dropped the partition month=2020-00-06
OK
Time taken: 0.273 seconds
hive (default)> 
```
##### 4.6.2 同时删除多个分区
```
hive (default)> alter table dept_partition drop partition(month='2020-00-07'),partition(month='2020-00-08');
Dropped the partition month=2020-00-07
Dropped the partition month=2020-00-08
OK
Time taken: 0.837 seconds
hive (default)> 
```
#### 4.6.6 查看分区表有多少分区
```
hive (default)> show partitions dept_partition;
OK
partition
month=2020-00-00
month=2020-00-01
month=2020-00-02
month=2020-00-03
month=2020-00-04
month=2020-00-05
Time taken: 0.155 seconds, Fetched: 6 row(s)
hive (default)> 
```

#### 4.6.7 查看分区表结构
```
hive (default)> desc formatted dept_partition;
OK
col_name        data_type       comment
# col_name              data_type               comment             
                 
deptno                  int                                         
dname                   string                                      
loc                     string                                      
                 
# Partition Information          
# col_name              data_type               comment             
                 
month                   string                                      
                 
# Detailed Table Information             
Database:               default                  
Owner:                  root                        
LastAccessTime:         UNKNOWN                  
Protect Mode:           None                     
Retention:              0                        
Location:               hdfs://systemhub511:9000/user/hive/warehouse/dept_partition      
Table Type:             MANAGED_TABLE            
Table Parameters:                
        transient_lastDdlTime   1553753699          
                 
# Storage Information            
SerDe Library:          org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe       
InputFormat:            org.apache.hadoop.mapred.TextInputFormat         
OutputFormat:           org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat       
Compressed:             No                       
Num Buckets:            -1                       
Bucket Columns:         []                       
Sort Columns:           []                       
Storage Desc Params:             
        field.delim             \t                  
        serialization.format    \t                  
Time taken: 0.183 seconds, Fetched: 34 row(s)
hive (default)>
```

#### 4.6.8 分区表注意事项
##### 4.6.8.1 创建二级分区表
```
hive (default)> create table dept_partition002(deptno int, dname string, loc string)
              > partitioned by (month string,day string)
              > row format delimited fields terminated by '\t';
OK
Time taken: 0.215 seconds
hive (default)> 
```
##### 4.6.8.2 加载数据
###### 4.6.8.2.1 加载数据到二级分区表
```
hive (default)> load data local inpath '/opt/module/datas/dept.txt'into table default.dept_partition002 partition(month='2020-00-06', day='0101');
Loading data to table default.dept_partition002 partition (month=2020-00-06, day=0101)
Partition default.dept_partition002{month=2020-00-06, day=0101} stats: [numFiles=1, numRows=0, totalSize=70, rawDataSize=0]
OK
Time taken: 1.914 seconds
hive (default)> 
```
###### 4.6.8.2.2 查询分区数据
```
hive (default)> select * from dept_partition002 where month='2020-00-06' and day='0101';
OK
dept_partition002.deptno        dept_partition002.dname dept_partition002.loc   dept_partition002.month dept_partition002.day
50      ACCOUNTING      1900    2020-00-06      0101
60      RESEARCH        1800    2020-00-06      0101
70      SALES           2020-00-06      0101
80      OPERATIONS      1700    2020-00-06      0101
Time taken: 0.284 seconds, Fetched: 4 row(s)
hive (default)>  
```
##### 4.6.8.3 将数据直接上传到分区目录,让分区表与数据产生关联的方式
###### 4.6.8.3.1 方式一: 上传数据后修复
> 上传数据
```
hive (default)> dfs -mkdir -p /user/hive/warehouse/dept_partition/month=2020-00-10;
hive (default)> 
```
> 查询数据(查询不到刚上传的数据)
```
hive (default)> select * from dept_partition where month='2020-00-10';
OK
dept_partition.deptno   dept_partition.dname    dept_partition.loc      dept_partition.month
Time taken: 0.147 seconds
hive (default)> 
```
> 执行修复命令
```
hive (default)> msck repair table dept_partition;
OK
Partitions not in metastore:    dept_partition:month=2020-00-10
Repair: Added partition to metastore dept_partition:month=2020-00-10
Time taken: 0.297 seconds, Fetched: 2 row(s)
hive (default)> 
```

###### 4.6.8.3.2 方式二: 上传数据后添加分区
> 上传数据
```
hive (default)> dfs -mkdir -p /user/hive/warehouse/dept_partition/month=2020-00-12;
hive (default)> 
```
> 执行添加分区
```
alter table dept_partition drop partition(month='2020-00-06',day='0101');
OK
Time taken: 0.273 seconds
hive (default)> 
```
> 查询数据
```
hive (default)> select * from dept_partition002 where month='2020-00-06' and day='0101';
OK
dept_partition002.deptno        dept_partition002.dname dept_partition002.loc   dept_partition002.month dept_partition002.day
50      ACCOUNTING      1900    2020-00-06      0101
60      RESEARCH        1800    2020-00-06      0101
70      SALES           2020-00-06      0101
80      OPERATIONS      1700    2020-00-06      0101
Time taken: 0.284 seconds, Fetched: 4 row(s)
hive (default)>  
```
###### 4.6.8.3.3 方式三: 上传数据后load数据到分区
> 创建目录
```
hive (default)> dfs -mkdir -p /user/hive/warehouse/dept_partition/month=2020-00-06/day=0101;
hive (default)> 
```
> 上传数据
```
hive (default)> load data local inpath '/opt/module/datas/dept.txt'into table default.dept_partition partition(month='2020-00-06', day='0101');
```
> 查询数据
```
hive (default)> select * from dept_partition where month='2020-00-06' and day='0101';
OK
dept_partition002.deptno        dept_partition002.dname dept_partition002.loc   dept_partition002.month dept_partition002.day
50      ACCOUNTING      1900    2020-00-06      0101
60      RESEARCH        1800    2020-00-06      0101
70      SALES           2020-00-06      0101
80      OPERATIONS      1700    2020-00-06      0101
Time taken: 0.284 seconds, Fetched: 4 row(s)
hive (default)>  
```

### 4.7 修改表
#### 4.7.1 重命名表
##### 4.7.1.1 语法
``` sql
ALTER TABLE table_name RENAME TO new_table_name;
```
##### 4.7.1.2 实操案例
```
hive (default)> alter table dept_partition002 rename to dept_partition003;
OK
Time taken: 0.324 seconds
hive (default)> 
```
#### 4.7.2 增加/修改/替换列信息
##### 4.7.2.1 语法
###### 4.7.2.1.1 更新列
```
ALTER   TABLE   table_name   CHANGE   [COLUMN]   col_old_name   col_new_name column_type [COMMENT col_comment] [FIRST|AFTER column_name]
```
###### 4.7.2.1.2 增加和替换列
```
ALTER    TABLE    table_name    ADD|REPLACE    COLUMNS    (col_name    data_type [COMMENT col_comment], ...)
```
> 注：ADD是代表新增一字段,字段位置在所有列后面(partition列前),REPLACE则是表示替换表中所有字段.

##### 4.7.2.2 实操案例
###### 4.7.2.2.1 查询表结构
```
hive (default)> desc dept_partition;
OK
col_name        data_type       comment
deptno                  int                                         
dname                   string                                      
loc                     string                                      
month                   string                                      
                 
# Partition Information          
# col_name              data_type               comment             
                 
month                   string                                      
Time taken: 0.122 seconds, Fetched: 9 row(s)
hive (default)> 
```
###### 4.7.2.2.2 添加列
```
hive (default)> alter table dept_partition add columns(deptdesc string);
OK
Time taken: 0.133 seconds
hive (default)>
```
> 查询表结构
```
hive (default)> desc dept_partition;
OK
col_name        data_type       comment
deptno                  int                                         
dname                   string                                      
loc                     string                                      
deptdesc                string                                      
month                   string                                      
                 
# Partition Information          
# col_name              data_type               comment             
                 
month                   string                                      
Time taken: 0.09 seconds, Fetched: 10 row(s)
hive (default)> 
```
###### 4.7.2.2.3 更新列
```
hive (default)> alter table dept_partition change column deptdesc desc int;
OK
Time taken: 0.113 seconds
hive (default)> 
```
> 查询表结构
```
hive (default)> desc dept_partition;
OK
col_name        data_type       comment
deptno                  int                                         
dname                   string                                      
loc                     string                                      
desc                    int                                         
month                   string                                      
                 
# Partition Information          
# col_name              data_type               comment             
                 
month                   string                                      
Time taken: 0.093 seconds, Fetched: 10 row(s)
hive (default)> 
```
###### 4.7.2.2.4 替换列
```
hive (default)> alter table dept_partition replace columns(deptno string,dname string,loc string);
OK
Time taken: 0.084 seconds
hive (default)> 
```
> 查询表结构
```
hive (default)> desc dept_partition;
OK
col_name        data_type       comment
deptno                  string                                      
dname                   string                                      
loc                     string                                      
month                   string                                      
                 
# Partition Information          
# col_name              data_type               comment             
                 
month                   string                                      
Time taken: 0.094 seconds, Fetched: 9 row(s)
hive (default)> 
```
###### 4.7.2.2.5 删除表
```
hive (default)> drop table dept_partition003;
OK
Time taken: 0.343 seconds
hive (default)> 
```

## 5. DML 数据操作
> DML(Data Manipulation Language)数据操纵语言,负责对数据库对象运行数据访问工作的指令集.

### 5.1 数据导入
#### 5.1.1 (Load 模式)向表中装载数据
##### 5.1.1.1 语法
```
load  data  [local]  inpath  'FilePath'  [overwrite]  into  table  TableName [partition (partcol1=val1,...)];
```
> 1.`load data`: 表示加载数据.
> 
> 2.`local`: 表示从本地加载数据到hive表,否则从HDFS加载数据到hive表.
> 
> 3.`inpath`: 表示加载数据的路径.
> 
> 4.`into table`: 表示加载到哪张数据表.
> 
> 5.`TableName`: 表示具体数据表.
> 
> 6.`overwrite`: 表示覆盖表中已有数据,否则表示追加.
> 
> 7.`partition`: 表示上传到指定分区.

##### 5.1.2.2 实操案例
###### 5.1.2.2.1 创建一张数据表
```
hive (default)> create table test005(id string,name string)row format delimited fields terminated by '\t';
OK
Time taken: 0.081 seconds
hive (default)> 
```
###### 5.1.2.2.2 加载本地文件到hive
```
hive (default)> load data local inpath '/opt/module/datas/test.txt' into table test005;
Loading data to table default.test005
Table default.test005 stats: [numFiles=1, totalSize=56]
OK
Time taken: 0.322 seconds
hive (default)> 
```
###### 5.1.2.2.3 加载HDFS文件到hive中
> 上传文件到HDFS
```
hive (default)> dfs -mkdir -p /user/geekparkhub/hive;
hive (default)> dfs -put /opt/module/datas/test.txt /user/geekparkhub/hive/test.txt;
```
###### 5.1.2.2.4 加载数据覆盖表中已有的数据
> 加载数据覆盖表中已有的数据
```
hive (default)> load data inpath '/user/geekparkhub/hive/test.txt' overwrite into table test005;
Loading data to table default.test005
Table default.test005 stats: [numFiles=1, numRows=0, totalSize=56, rawDataSize=0]
OK
Time taken: 0.21 seconds
hive (default)> 
```

#### 5.1.2 (Insert 模式) 通过查询语句向表中插入数据
##### 5.1.2.1 基本模式插入 (根据单张表查询结果)
```
hive (default)> insert overwrite table dept_partition002 partition(month='2020-00-11') select id, name from dept_partition where month='2020-00-12';
```
##### 5.1.2.2 多插入模式 (根据多张表查询结果)
```
hive (default)> from dept_partition
insert overwrite table dept_partition002 partition(month='2020-00-13')
select id, name where month='2020-00-10'
insert overwrite table dept_partition002 partition(month='2020-00-14')
select id, name where month='2020-00-10';
```

#### 5.1.3 (As Select 模式) 查询语句中创建表并加载数据
> 根据查询结果创建表 (查询的结果会添加到新创建的表中)
```
create table if not exists test006 as select * from test;
```
#### 5.1.4 创建表时通过Location指定加载数据路径
##### 5.1.4.1 创建表,并指定在HDFS上的位置
```
hive (default)> create table test007 like test;
OK
Time taken: 0.108 seconds
hive (default)>
```
##### 5.1.4.2 上传数据到hdfs上
```
hive (default)> dfs -put /opt/module/datas/test.txt /user/hive/warehouse/test007;
```
##### 5.1.4.3 查询数据
```
hive (default)> select * from test007;
OK
test007.id      test007.name
1       TestUser001
2       TestUser002
3       TestUser003
4       TestUser004
Time taken: 0.087 seconds, Fetched: 4 row(s)
hive (default)> 
```

#### 5.1.5 Import数据到指定Hive表中
> 先用export导出后,再将数据导入.
```
hive (default)> import table test006 from
              > '/user/geekparkhub/export/test002';
Copying data from hdfs://systemhub511:9000/user/geekparkhub/export/test002/data
Copying file: hdfs://systemhub511:9000/user/geekparkhub/export/test002/data/test.txt
Loading data to table default.test006
OK
Time taken: 0.571 seconds
hive (default)> 
```

### 5.2 数据导出
#### 5.2.1 Insert 导出
##### 5.2.1 将查询的结果导出到本地
```
hive (default)> insert overwrite local directory '/opt/module/datas/export/test'
              > select * from test;
Query ID = root_20190328214019_01955e31-2364-4c10-8661-cafb4bd9bb38
Total jobs = 1
Launching Job 1 out of 1
Number of reduce tasks is set to 0 since there's no reduce operator
Starting Job = job_1553780256887_0003, Tracking URL = http://systemhub611:8088/proxy/application_1553780256887_0003/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553780256887_0003
Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 0
Stage-1 map = 0%,  reduce = 0%
Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 1.35 sec
MapReduce Total cumulative CPU time: 1 seconds 350 msec
Ended Job = job_1553780256887_0003
Copying data to local directory /opt/module/datas/export/test
Copying data to local directory /opt/module/datas/export/test
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 1   Cumulative CPU: 1.35 sec   HDFS Read: 2982 HDFS Write: 56 SUCCESS
Total MapReduce CPU Time Spent: 1 seconds 350 msec
OK
test.id test.name
Time taken: 24.917 seconds
hive (default)> 
```
```
[root@systemhub711 ~]# cat /opt/module/datas/export/test/000000_0
1TestUser001
2TestUser002
3TestUser003
4TestUser004
[root@systemhub711 ~]# 
```
##### 5.2.2 将查询的结果格式化导出到本地
```
hive (default)> insert overwrite local directory '/opt/module/datas/export/test001'
              > row format delimited fields terminated by '\t'
              > select * from test;
Query ID = root_20190328214116_2a678b33-dc52-4aef-97d4-7c4932d14dc2
Total jobs = 1
Launching Job 1 out of 1
Number of reduce tasks is set to 0 since there's no reduce operator
Starting Job = job_1553780256887_0004, Tracking URL = http://systemhub611:8088/proxy/application_1553780256887_0004/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553780256887_0004
Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 0
Stage-1 map = 0%,  reduce = 0%
Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 1.32 sec
MapReduce Total cumulative CPU time: 1 seconds 320 msec
Ended Job = job_1553780256887_0004
Copying data to local directory /opt/module/datas/export/test001
Copying data to local directory /opt/module/datas/export/test001
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 1   Cumulative CPU: 1.32 sec   HDFS Read: 2995 HDFS Write: 56 SUCCESS
Total MapReduce CPU Time Spent: 1 seconds 320 msec
OK
test.id test.name
Time taken: 24.856 seconds
hive (default)> 
```
```
[root@systemhub711 ~]# cat /opt/module/datas/export/test001/000000_0
1       TestUser001
2       TestUser002
3       TestUser003
4       TestUser004
[root@systemhub711 ~]# 
```
##### 5.2.3 将查询的结果导出到HDFS
```
hive (default)> insert overwrite directory '/user/geekparkhub/export/test'
              > row format delimited fields terminated by '\t'
              > select * from test;
Query ID = root_20190328214749_261af019-2978-43a9-99be-4cce6bf63837
Total jobs = 3
Launching Job 1 out of 3
Number of reduce tasks is set to 0 since there's no reduce operator
Starting Job = job_1553780256887_0005, Tracking URL = http://systemhub611:8088/proxy/application_1553780256887_0005/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553780256887_0005
Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 0
Stage-1 map = 0%,  reduce = 0%
Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 1.3 sec
MapReduce Total cumulative CPU time: 1 seconds 300 msec
Ended Job = job_1553780256887_0005
Stage-3 is selected by condition resolver.
Stage-2 is filtered out by condition resolver.
Stage-4 is filtered out by condition resolver.
Moving data to: hdfs://systemhub511:9000/user/geekparkhub/export/test/.hive-staging_hive_2019-03-28_21-47-49_139_9022836247083242678-1/-ext-10000
Moving data to: /user/geekparkhub/export/test
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 1   Cumulative CPU: 1.3 sec   HDFS Read: 2983 HDFS Write: 56 SUCCESS
Total MapReduce CPU Time Spent: 1 seconds 300 msec
OK
test.id test.name
Time taken: 24.801 seconds
hive (default)> 
```
```
hive (default)> dfs -cat /user/geekparkhub/export/test/*;
1       TestUser001
2       TestUser002
3       TestUser003
4       TestUser004
hive (default)> 
```

#### 5.2.2 Hadoop指令导出到本地
```
hive (default)> dfs -get /user/hive/warehouse/dept_partition/month=2020-00-00/dept.txt /opt/module/datas/test002.txt;
hive (default)> 
```
#### 5.2.3 Hive Shell指令导出
```
[root@systemhub711 hive]# bin/hive -e 'select * from test;' > /opt/module/datas/test002.txt; 

Logging initialized using configuration in file:/opt/module/hive/conf/hive-log4j.properties
OK
Time taken: 2.32 seconds, Fetched: 4 row(s)
[root@systemhub711 hive]# 
```
#### 5.2.4 Export导出到HDFS上
```
hive (default)> export table test to '/user/geekparkhub/export/test002';
Copying data from file:/tmp/root/16f13154-2779-4719-89d3-3453b1468948/hive_411_6501223345710054079-1/-local-10000/_metadata
Copying file: file:/tmp/root/16f13154-2779-4719-89d3-3453b1468948/hive_411_6501223345710054079-1/-local-10000/_metadata
Copying data from hdfs://systemhub511:9000/user/hive/warehouse/test
Copying file: hdfs://systemhub511:9000/user/hive/warehouse/test/test.txt
OK
Time taken: 0.458 seconds
hive (default)>
hive (default)> dfs -cat /user/geekparkhub/export/test002/data/test.txt;
1       TestUser001
2       TestUser002
3       TestUser003
4       TestUser004
hive (default)> 
```

### 5.3 清除表中数据 (Truncate)
> 注意: Truncate只能删除管理表,不能删除外部表中数据
```
hive (default)> select * from test007;
OK
test007.id      test007.name
1       TestUser001
2       TestUser002
3       TestUser003
4       TestUser004
Time taken: 0.079 seconds, Fetched: 4 row(s)
hive (default)> truncate table test007;
OK
Time taken: 0.083 seconds
hive (default)> select * from test007;
OK
test007.id      test007.name
Time taken: 0.078 seconds
hive (default)> 
```

## 6. 查询
> 查询基本语法
```
[WITH CommonTableExpression (, CommonTableExpression)*]
(Note: Only available starting with Hive0.13.0)
SELECT [ALL | DISTINCT] select_expr, select_expr, ...
FROM table_reference
[WHERE where_condition]
[GROUP BY col_list]
[ORDER BY col_list]
[CLUSTER BY col_list| [DISTRIBUTE BY col_list] [SORT BY col_list]]
[LIMIT number]
```

### 6.1 基本查询 (Select...From)
#### 6.1.1 全表和特定列查询
> 注意:
> 
> 1.SQL 语言大小写不敏感.
> 
> 2.SQL 可以写在一行或者多行.
> 
> 3.关键字不能被缩写也不能分行.
> 
> 4.各子句一般要分行写.
> 
> 5.使用缩进提高语句的可读性.
##### 6.1.1.1 全表查询
```
hive (default)> select * from emp;
OK
emp.empno       emp.ename       emp.job emp.mgr emp.hiredate    emp.sal emp.comm        emp.deptno
7369    SMITH   CLERKSKLD       7902    1980-12-17      800.0   20.0    
7499    ALLTE   SALESMANS       7689    1987-02-23      1600.0  300.0   30
7521    WAROS   SJDHHJDJX       7869    1984-06-12      1250.18 500.0    
Time taken: 0.129 seconds, Fetched: 9 row(s)
hive (default)> 
```
##### 6.1.1.2 选择特定列查询
```
hive (default)> select empno,ename from emp;
OK
empno   ename
7369    SMITH
7499    ALLTE
7521    WAROS
7566    JOSSS
7654    SOCTD
7698    ADAMS
7782    JAMSK
7788    FOESS
7939    KINGS
Time taken: 0.123 seconds, Fetched: 9 row(s)
hive (default)> 
```

#### 6.1.2 列别名
> 在列名和别名之间加入关键字`AS`
```
hive (default)> select empno as no,ename as name from emp;
OK
no      name
7369    SMITH
7499    ALLTE
7521    WAROS
7566    JOSSS
7654    SOCTD
7698    ADAMS
7782    JAMSK
7788    FOESS
7939    KINGS
Time taken: 0.078 seconds, Fetched: 9 row(s)
hive (default)> 
```
#### 6.1.3 算术运算符

| 运算符      |     描述 |
| :--------: | :--------:|
| A + B    |   A和B 相加 |
| A - B   |   A减B |
| A * B    |   A和B 相乘 |
| A / B    |   A除以B |
| A % B    |   A对B取余 |
| A & B    |   A和B按位取与 |
| AB    |   A和B按位取或 |
| A+B    |   A和B按位取异或 |
| ~A    |   A按位取反 |

> 查询所员工薪水+1
```
hive (default)> select sal +1 as wage from emp;
OK
wage
801.0
1601.0
1251.18
2895.25
2853.3
25525.02
1101.0
951.0
3001.0
Time taken: 0.063 seconds, Fetched: 9 row(s)
hive (default)> 
```
#### 6.1.4 常用函数
#### 6.1.4.1 求总行数 (count)
```
hive (default)> select count(*) cnt from emp;
Query ID = root_20190328225729_5783bab3-92a5-4a6c-b830-c0f8e7127225
Total jobs = 1
Launching Job 1 out of 1
Number of reduce tasks determined at compile time: 1
In order to change the average load for a reducer (in bytes):
  set hive.exec.reducers.bytes.per.reducer=<number>
In order to limit the maximum number of reducers:
  set hive.exec.reducers.max=<number>
In order to set a constant number of reducers:
  set mapreduce.job.reduces=<number>
Starting Job = job_1553780256887_0006, Tracking URL = http://systemhub611:8088/proxy/application_1553780256887_0006/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553780256887_0006
Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 1
Stage-1 map = 0%,  reduce = 0%
Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 1.55 sec
Stage-1 map = 100%,  reduce = 100%, Cumulative CPU 3.43 sec
MapReduce Total cumulative CPU time: 3 seconds 430 msec
Ended Job = job_1553780256887_0006
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 1  Reduce: 1   Cumulative CPU: 3.43 sec   HDFS Read: 7647 HDFS Write: 2 SUCCESS
Total MapReduce CPU Time Spent: 3 seconds 430 msec
OK
cnt
9
Time taken: 42.734 seconds, Fetched: 1 row(s)
hive (default)> 
```
#### 6.1.4.2 求工资的最大值 (max)
```
hive (default)> select max(sal) max_wage from emp;
Query ID = root_20190328225946_778636eb-c34a-4a75-b8e5-68684633a0a3
Total jobs = 1
Launching Job 1 out of 1
Number of reduce tasks determined at compile time: 1
In order to change the average load for a reducer (in bytes):
  set hive.exec.reducers.bytes.per.reducer=<number>
In order to limit the maximum number of reducers:
  set hive.exec.reducers.max=<number>
In order to set a constant number of reducers:
  set mapreduce.job.reduces=<number>
Starting Job = job_1553780256887_0007, Tracking URL = http://systemhub611:8088/proxy/application_1553780256887_0007/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553780256887_0007
Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 1
Stage-1 map = 0%,  reduce = 0%
Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 1.33 sec
Stage-1 map = 100%,  reduce = 100%, Cumulative CPU 3.07 sec
MapReduce Total cumulative CPU time: 3 seconds 70 msec
Ended Job = job_1553780256887_0007
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 1  Reduce: 1   Cumulative CPU: 3.07 sec   HDFS Read: 7836 HDFS Write: 9 SUCCESS
Total MapReduce CPU Time Spent: 3 seconds 70 msec
OK
max_wage
25524.02
Time taken: 31.112 seconds, Fetched: 1 row(s)
hive (default)> 
```
#### 6.1.4.3 求工资的最小值 (min)
```
hive (default)> select min(sal) min_wage from emp;
Query ID = root_20190328230109_5dbce45f-9887-44cc-b6fb-5aa64ac11a50
Total jobs = 1
Launching Job 1 out of 1
Number of reduce tasks determined at compile time: 1
In order to change the average load for a reducer (in bytes):
  set hive.exec.reducers.bytes.per.reducer=<number>
In order to limit the maximum number of reducers:
  set hive.exec.reducers.max=<number>
In order to set a constant number of reducers:
  set mapreduce.job.reduces=<number>
Starting Job = job_1553780256887_0008, Tracking URL = http://systemhub611:8088/proxy/application_1553780256887_0008/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553780256887_0008
Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 1
Stage-1 map = 0%,  reduce = 0%
Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 1.52 sec
Stage-1 map = 100%,  reduce = 100%, Cumulative CPU 3.42 sec
MapReduce Total cumulative CPU time: 3 seconds 420 msec
Ended Job = job_1553780256887_0008
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 1  Reduce: 1   Cumulative CPU: 3.42 sec   HDFS Read: 7836 HDFS Write: 6 SUCCESS
Total MapReduce CPU Time Spent: 3 seconds 420 msec
OK
min_wage
800.0
Time taken: 30.23 seconds, Fetched: 1 row(s)
hive (default)>
```
#### 6.1.4.4 求工资的总和 (sum)
```
hive (default)> select sum(sal) sum_wage from emp;
Query ID = root_20190328230304_600ecafd-b2a6-4b53-8ba8-fb9938c9f0c9
Total jobs = 1
Launching Job 1 out of 1
Number of reduce tasks determined at compile time: 1
In order to change the average load for a reducer (in bytes):
  set hive.exec.reducers.bytes.per.reducer=<number>
In order to limit the maximum number of reducers:
  set hive.exec.reducers.max=<number>
In order to set a constant number of reducers:
  set mapreduce.job.reduces=<number>
Starting Job = job_1553780256887_0010, Tracking URL = http://systemhub611:8088/proxy/application_1553780256887_0010/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553780256887_0010
Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 1
Stage-1 map = 0%,  reduce = 0%
Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 1.36 sec
Stage-1 map = 100%,  reduce = 100%, Cumulative CPU 3.13 sec
MapReduce Total cumulative CPU time: 3 seconds 130 msec
Ended Job = job_1553780256887_0010
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 1  Reduce: 1   Cumulative CPU: 3.13 sec   HDFS Read: 7830 HDFS Write: 9 SUCCESS
Total MapReduce CPU Time Spent: 3 seconds 130 msec
OK
sum_wage
39970.75
Time taken: 33.111 seconds, Fetched: 1 row(s)
hive (default)> 
```
#### 6.1.4.5 求工资的平均值 (avg)
```
hive (default)> select avg(sal) avg_wage from emp;
Query ID = root_20190328230301_15ba0d3a-130a-42a5-9b9a-a313f187e814
Total jobs = 1
Launching Job 1 out of 1
Number of reduce tasks determined at compile time: 1
In order to change the average load for a reducer (in bytes):
  set hive.exec.reducers.bytes.per.reducer=<number>
In order to limit the maximum number of reducers:
  set hive.exec.reducers.max=<number>
In order to set a constant number of reducers:
  set mapreduce.job.reduces=<number>
Starting Job = job_1553780256887_0009, Tracking URL = http://systemhub611:8088/proxy/application_1553780256887_0009/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553780256887_0009
Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 1
Stage-1 map = 0%,  reduce = 0%
Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 1.21 sec
Stage-1 map = 100%,  reduce = 100%, Cumulative CPU 2.96 sec
MapReduce Total cumulative CPU time: 2 seconds 960 msec
Ended Job = job_1553780256887_0009
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 1  Reduce: 1   Cumulative CPU: 2.96 sec   HDFS Read: 8011 HDFS Write: 18 SUCCESS
Total MapReduce CPU Time Spent: 2 seconds 960 msec
OK
avg_wage
4441.194444444444
Time taken: 67.764 seconds, Fetched: 1 row(s)
hive (default)> 
```

#### 6.1.5 Limit语句
> 典型的查询会返回多行数据,LIMIT子句用于限制返回的行数.
```
hive (default)> select * from emp limit 5;
OK
emp.empno       emp.ename       emp.job emp.mgr emp.hiredate    emp.sal emp.comm        emp.deptno
7369    SMITH   CLERKSKLD       7902    1980-12-17      800.0   20.0    NULL
7499    ALLTE   SALESMANS       7689    1987-02-23      1600.0  300.0   30
7521    WAROS   SJDHHJDJX       7869    1984-06-12      1250.18 500.0   30
7566    JOSSS   JDHYHDSDS       4545    1874-05-15      2894.25 20.0    NULL
7654    SOCTD   MANSJUSSD       4855    1996-02-14      2852.3  30.0    NULL
Time taken: 0.135 seconds, Fetched: 5 row(s)
hive (default)> 
```

### 6.2 Where语句
> 1.使用`WHERE`子句,将不满足条件的行过滤掉.
> 2.`WHERE`子句紧随`FROM`子句.
> 3.案例实操
> 查询出薪水大于1000的所有员工.
```
hive (default)> select * from emp where sal > 1000;
OK
emp.empno       emp.ename       emp.job emp.mgr emp.hiredate    emp.sal emp.comm        emp.deptno
7499    ALLTE   SALESMANS       7689    1987-02-23      1600.0  300.0   30
7521    WAROS   SJDHHJDJX       7869    1984-06-12      1250.18 500.0   30
7566    JOSSS   JDHYHDSDS       4545    1874-05-15      2894.25 20.0    NULL
7654    SOCTD   MANSJUSSD       4855    1996-02-14      2852.3  30.0    NULL
7698    ADAMS   JUSHHWESD       4552    1985-05-16      25524.02        30.0    NULL
7782    JAMSK   KIHNGSEHN       7769    1991-06-23      1100.0  20.0    NULL
7939    KINGS   CLADDJHEW       7566    1993-07-12      3000.0  20.0    NULL
Time taken: 0.26 seconds, Fetched: 7 row(s)
hive (default)> 
```
#### 6.2.1 比较运算符 (Between / In / Is Null)
> 下面表中描述了谓词操作符,这些操作符同样可以用于JOIN...ON和HAVING语句中.
##### 6.2.1.1 比较运算符对照表
| 操作符      |     支持数据类型 |   描述   |
| :--------: | :--------:| :------: |
| A=B    |   基本数据类型 |  如果A等于B则返回TRUE,反之返回FALSE.  |
| A<=>B    |   基本数据类型 |  如果A和B都为NULL,则返回TRUE,其他的和等号(=)操作符的结果一致,如果任一为NULL则结果为NULL.  |
| A<>B, A!=B    |   基本数据类型 |  A或者B为NULL则返回NULL,如果A不等于B,则返回TRUE,反之返回FALSE.  |
| A<B    |   基本数据类型 |  A或者B为NULL,则返回NULL,如果A小于B,则返回TRUE,反之返回FALSE.  |
| A<=B    |   基本数据类型 |  A或者B为NULL,则返回NULL,如果A小于等于B,则返回TRUE,反之返回FALSE.  |
| A>B    |   基本数据类型 |  A或者B为NULL,则返回NULL,如果A大于B,则返回TRUE,反之返回FALSE.  |
| A>=B    |   基本数据类型 |  A或者B为NULL,则返回NULL,如果A大于等于B,则返回TRUE,反之返回FALSE.  |
| A [NOT] BETWEEN B AND C    |   基本数据类型 |  如果A,B或者C任一为NULL,则结果为NULL,如果A的值大于等于B而且小于或等于C,则结果为TRUE,反之为FALSE,如果使用NOT关键字则可达到相反的效果.  |
| A IS NULL    |   所有数据类型 |  如果A等于NULL,则返回TRUE,反之返回FALSE.  |
| A IS NOT NULL    |   所有数据类型 |  如果A不等于NULL,则返回TRUE,反之返回FALSE. |
| IN(Num1,Num2)    |   所有数据类型 |  使用IN运算显示列表中的值.  |
| A [NOT] LIKE B    |   STRING 类型 |  B是一个SQL下的简单正则表达式,如果A与其匹配的话,则返回TRUE,反之返回FALSE,B的表达式说明如下:‘x%’表示A必须以字母‘x’开头,‘%x’表示A必须以字母’x’结尾,而‘%x%’表示A包含有字母’x’,可以位于开头,结尾或者字符串中间,如果使用NOT,关键字则可达到相反的效果.  |
| A RLIKE B,A REGEXP B    |   STRING 类型 |  B是一个正则表达式,如果A与其匹配，则返回TRUE,反之返回FALSE,匹配使用的是JDK中的正则表达式接口实现的,因为正则也依据其中的规则,例如,正则表达式必须和整个字符串A相匹配,而不是只需与其字符串匹配.  |

##### 6.2.1.2 案例实操
###### 6.2.1.2.1 查询薪水等于3000的所有员工
```
hive (default)> select * from emp where sal = 3000;
OK
emp.empno       emp.ename       emp.job emp.mgr emp.hiredate    emp.sal emp.comm        emp.deptno
7939    KINGS   CLADDJHEW       7566    1993-07-12      3000.0  20.0    NULL
Time taken: 0.063 seconds, Fetched: 1 row(s)
hive (default)> 
```
###### 6.2.1.2.2 查询工资在500到1000的员工信息
```
hive (default)> select * from emp where sal between 500 and 1000;
OK
emp.empno       emp.ename       emp.job emp.mgr emp.hiredate    emp.sal emp.comm        emp.deptno
7369    SMITH   CLERKSKLD       7902    1980-12-17      800.0   20.0    NULL
7788    FOESS   CLAEDFDFD       7698    1994-09-17      950.0   30.0    NULL
Time taken: 0.086 seconds, Fetched: 2 row(s)
hive (default)> 
```
###### 6.2.1.2.3 查询comm为空的所有员工信息
```
hive (default)> select * from emp where comm is null;
OK
emp.empno       emp.ename       emp.job emp.mgr emp.hiredate    emp.sal emp.comm        emp.deptno
Time taken: 0.077 seconds
hive (default)> 
```
###### 6.2.1.2.4 查询工资是1500和3000的员工信息
```
hive (default)> select * from emp where sal IN(1500,3000);
OK
emp.empno       emp.ename       emp.job emp.mgr emp.hiredate    emp.sal emp.comm        emp.deptno
7939    KINGS   CLADDJHEW       7566    1993-07-12      3000.0  20.0    NULL
Time taken: 0.117 seconds, Fetched: 1 row(s)
hive (default)> 
```


#### 6.2.2 Like和RLike
> 1.使用`LIKE`运算选择类似的值.
> 
> 2.选择条件可以包含字符或数字:
> `%` 代表零个或多个字符(任意个字符)
> `_` 代表一个字符
> 
> 3.`RLIKE`子句是Hive中这个功能的一个扩展,其可以通过Java的正则表达式这个更强大的语言来指定匹配条件.
##### 6.2.2.1 案例实操
###### 6.2.2.1.1 查找以2开头薪水的员工信息
```
hive (default)> select * from emp where sal LIKE '2%';
OK
emp.empno       emp.ename       emp.job emp.mgr emp.hiredate    emp.sal emp.comm        emp.deptno
7566    JOSSS   JDHYHDSDS       4545    1874-05-15      2894.25 20.0    NULL
7654    SOCTD   MANSJUSSD       4855    1996-02-14      2852.3  30.0    NULL
7698    ADAMS   JUSHHWESD       4552    1985-05-16      25524.02        30.0    NULL
Time taken: 0.134 seconds, Fetched: 3 row(s)
hive (default)> 
```
###### 6.2.2.1.2 查找第二个数值为2薪水的员工信息
```
hive (default)> select * from emp where sal LIKE '_2%';
OK
emp.empno       emp.ename       emp.job emp.mgr emp.hiredate    emp.sal emp.comm        emp.deptno
7521    WAROS   SJDHHJDJX       7869    1984-06-12      1250.18 500.0   30
Time taken: 0.075 seconds, Fetched: 1 row(s)
hive (default)> 
```
###### 6.2.2.1.3 查找薪水中含有2的员工信息
```
hive (default)> select * from emp where sal RLIKE '[2]';
OK
emp.empno       emp.ename       emp.job emp.mgr emp.hiredate    emp.sal emp.comm        emp.deptno
7521    WAROS   SJDHHJDJX       7869    1984-06-12      1250.18 500.0   30
7566    JOSSS   JDHYHDSDS       4545    1874-05-15      2894.25 20.0    NULL
7654    SOCTD   MANSJUSSD       4855    1996-02-14      2852.3  30.0    NULL
7698    ADAMS   JUSHHWESD       4552    1985-05-16      25524.02        30.0    NULL
Time taken: 0.088 seconds, Fetched: 4 row(s)
hive (default)> 
```

#### 6.2.3 逻辑运算符 (And / Or / Not)

| 操作符      |     含义 |
| :--------: | :--------:|
| AND    |   逻辑并 |
| OR    |   逻辑或 |
| NOT    |   逻辑否 |
##### 6.2.3.1 案例实操
###### 6.2.3.1.1 查询薪水大于1000,部门是30
```
hive (default)> select * from emp where sal > 1000 AND deptno = 30;
OK
emp.empno       emp.ename       emp.job emp.mgr emp.hiredate    emp.sal emp.comm        emp.deptno
7499    ALLTE   SALESMANS       7689    1987-02-23      1600.0  300.0   30
7521    WAROS   SJDHHJDJX       7869    1984-06-12      1250.18 500.0   30
Time taken: 0.107 seconds, Fetched: 2 row(s)
hive (default)> 
```
###### 6.2.3.1.2 查询薪水大于1000,或者部门是30
```
hive (default)> select * from emp where sal > 1000 or deptno = 30;
OK
emp.empno       emp.ename       emp.job emp.mgr emp.hiredate    emp.sal emp.comm        emp.deptno
7499    ALLTE   SALESMANS       7689    1987-02-23      1600.0  300.0   30
7521    WAROS   SJDHHJDJX       7869    1984-06-12      1250.18 500.0   30
7566    JOSSS   JDHYHDSDS       4545    1874-05-15      2894.25 20.0    NULL
7654    SOCTD   MANSJUSSD       4855    1996-02-14      2852.3  30.0    NULL
7698    ADAMS   JUSHHWESD       4552    1985-05-16      25524.02        30.0    NULL
7782    JAMSK   KIHNGSEHN       7769    1991-06-23      1100.0  20.0    NULL
7939    KINGS   CLADDJHEW       7566    1993-07-12      3000.0  20.0    NULL
Time taken: 0.088 seconds, Fetched: 7 row(s)
hive (default)> 
```
###### 6.2.3.1.3 查询除了20部门和30部门以外的员工信息
```
hive (default)> select * from emp where deptno not IN(30,20);
OK
emp.empno       emp.ename       emp.job emp.mgr emp.hiredate    emp.sal emp.comm        emp.deptno
Time taken: 0.067 seconds
hive (default)> 
```

### 6.3 分组
#### 6.3.1 Group By 语句
> `GROUP  BY`语句通常会和聚合函数一起使用,按照一个或者多个列队结果进行分组,然后对每个组执行聚合操作.
> 
> 1.计算emp表每个部门的平均工资.
```
hive (default)> select avg(sal) avg_sal from emp
              > group by deptno;
Query ID = root_20190329100652_589ff409-e520-40bc-9cb4-4637d9775441
Total jobs = 1
Launching Job 1 out of 1
Number of reduce tasks not specified. Estimated from input data size: 1
In order to change the average load for a reducer (in bytes):
  set hive.exec.reducers.bytes.per.reducer=<number>
In order to limit the maximum number of reducers:
  set hive.exec.reducers.max=<number>
In order to set a constant number of reducers:
  set mapreduce.job.reduces=<number>
Starting Job = job_1553824894278_0001, Tracking URL = http://systemhub611:8088/proxy/application_1553824894278_0001/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553824894278_0001
Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 1
Stage-1 map = 0%,  reduce = 0%
Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 1.72 sec
Stage-1 map = 100%,  reduce = 100%, Cumulative CPU 3.55 sec
MapReduce Total cumulative CPU time: 3 seconds 550 msec
Ended Job = job_1553824894278_0001
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 1  Reduce: 1   Cumulative CPU: 3.55 sec   HDFS Read: 8446 HDFS Write: 37 SUCCESS
Total MapReduce CPU Time Spent: 3 seconds 550 msec
OK
avg_sal
5302.938571428572
1425.0900000000001
Time taken: 39.062 seconds, Fetched: 2 row(s)
hive (default)> 
```
> 2.计算emp每个部门中每个岗位的最高薪水.
```
hive (default)> select deptno,job,avg(sal) avg_sal from emp
              > group by deptno,job;
Query ID = root_20190329101147_338b3ac5-d29e-46eb-abae-d4d2a3bcc3ae
Total jobs = 1
Launching Job 1 out of 1
Number of reduce tasks not specified. Estimated from input data size: 1
In order to change the average load for a reducer (in bytes):
  set hive.exec.reducers.bytes.per.reducer=<number>
In order to limit the maximum number of reducers:
  set hive.exec.reducers.max=<number>
In order to set a constant number of reducers:
  set mapreduce.job.reduces=<number>
Starting Job = job_1553824894278_0002, Tracking URL = http://systemhub611:8088/proxy/application_1553824894278_0002/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553824894278_0002
Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 1
Stage-1 map = 0%,  reduce = 0%
Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 1.21 sec
Stage-1 map = 100%,  reduce = 100%, Cumulative CPU 2.97 sec
MapReduce Total cumulative CPU time: 2 seconds 970 msec
Ended Job = job_1553824894278_0002
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 1  Reduce: 1   Cumulative CPU: 2.97 sec   HDFS Read: 8904 HDFS Write: 182 SUCCESS
Total MapReduce CPU Time Spent: 2 seconds 970 msec
OK
deptno  job     avg_sal
NULL    CLADDJHEW       3000.0
NULL    CLAEDFDFD       950.0
NULL    CLERKSKLD       800.0
NULL    JDHYHDSDS       2894.25
NULL    JUSHHWESD       25524.02
NULL    KIHNGSEHN       1100.0
NULL    MANSJUSSD       2852.3
30      SALESMANS       1600.0
30      SJDHHJDJX       1250.18
Time taken: 28.517 seconds, Fetched: 9 row(s)
hive (default)> 
```

#### 6.3.2 Having 语句
> having与where不同点
> 
> where针对表中的列发挥作用,查询数据.
> having针对查询结果中的列发挥作用,筛选数据.
> where后面不能写分组函数,而having后面可以使用分组函数.
> having只用于group by分组统计语句.

> 求每个部门的平均薪水大于2000的部门
```
hive (default)> select deptno,avg(sal) avg_sal from emp
              > group by deptno
              > having avg_sal > 2000;
Query ID = root_20190329102456_d4f50a80-3441-421c-9e89-acf8665d98aa
Total jobs = 1
Launching Job 1 out of 1
Number of reduce tasks not specified. Estimated from input data size: 1
In order to change the average load for a reducer (in bytes):
  set hive.exec.reducers.bytes.per.reducer=<number>
In order to limit the maximum number of reducers:
  set hive.exec.reducers.max=<number>
In order to set a constant number of reducers:
  set mapreduce.job.reduces=<number>
Starting Job = job_1553824894278_0003, Tracking URL = http://systemhub611:8088/proxy/application_1553824894278_0003/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553824894278_0003
Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 1
Stage-1 map = 0%,  reduce = 0%
Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 1.2 sec
Stage-1 map = 100%,  reduce = 100%, Cumulative CPU 3.65 sec
MapReduce Total cumulative CPU time: 3 seconds 650 msec
Ended Job = job_1553824894278_0003
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 1  Reduce: 1   Cumulative CPU: 3.65 sec   HDFS Read: 8985 HDFS Write: 21 SUCCESS
Total MapReduce CPU Time Spent: 3 seconds 650 msec
OK
deptno  avg_sal
NULL    5302.938571428572
Time taken: 29.14 seconds, Fetched: 1 row(s)
hive (default)> 
```

### 6.4 Join语句
#### 6.4.1 等值Join
> Hive支持通常的`SQL JOIN`语句,但是只支持等值连接,不支持非等值连接.
```
hive (default)> select e.empno,e.ename,d.dname
              > from emp e join dept d
              > on e.deptno=d.deptid;
Query ID = root_d5dfa88a-b9a2-4377-aebe-1328cf0b6653
Total jobs = 1
WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Execution log at: /tmp/root/aebe-1328cf0b6653.log
Starting to launch local task to process map join;      maximum memory = 518979584
Dump the side-table for tag: 1 with group count: 4 into file: file:/tmp/root/c9582a8b-1e8f-446e-b899-f5114533b280/-local-10003/HashTable-Stage-3/MapJoin-mapfile01--.hashtable
Uploaded 1 File to: file:/tmp/root/c9582a8b-1e8f-446e-b899-f5114533b280/hive_2019-03-29_11-02-28_999_8089713357386975442-1/-local-10003/HashTable-Stage-3/MapJoin-mapfile01--.hashtable (373 bytes)
End of local task; Time Taken: 1.969 sec.
Execution completed successfully
MapredLocal task succeeded
Launching Job 1 out of 1
Number of reduce tasks is set to 0 since there's no reduce operator
Starting Job = job_1553824894278_0004, Tracking URL = http://systemhub611:8088/proxy/application_1553824894278_0004/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553824894278_0004
Hadoop job information for Stage-3: number of mappers: 1; number of reducers: 0
Stage-3 map = 0%,  reduce = 0%
Stage-3 map = 100%,  reduce = 0%, Cumulative CPU 1.81 sec
MapReduce Total cumulative CPU time: 1 seconds 810 msec
Ended Job = job_1553824894278_0004
MapReduce Jobs Launched: 
Stage-Stage-3: Map: 1   Cumulative CPU: 1.81 sec   HDFS Read: 7157 HDFS Write: 0 SUCCESS
Total MapReduce CPU Time Spent: 1 seconds 810 msec
OK
e.empno e.ename d.dname
Time taken: 29.819 seconds
hive (default)> 
```
#### 6.4.2 表别名
> 1.好处:
> 使用别名可以简化查询.
> 使用表名前缀可以提高执行效率.
> 
> 案例实操
```
hive (default)> select e.empno,e.ename,d.dname
              > from emp e join dept d
              > on e.deptno=d.deptid;
```
#### 6.4.3 内连接
> 内连接: 只有进行连接的两个表中都存在与连接条件相匹配的数据才会被保留下.
#### 6.4.4 左外连接
> 左外连接: JOIN操作符左边表中符合WHERE子句的所有记录将会被返回.
```
hive (default)> select e.empno,e.ename,d.dname
              > from emp e left join dept d
              > on e.deptno=d.deptid;
Query ID = root_20190329112652_1446145a-1749-4a6f-85ad-b4576ee31e0f
Total jobs = 1
WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Execution log at: /tmp/root/root_20190329112652_1446145a-1749-4a6f-85ad-b4576ee31e0f.log
Starting to launch local task to process map join;      maximum memory = 518979584
2019-03-29 11:26:59     Dump the side-table for tag: 1 with group count: 4 into file: file:/tmp/root/c9582a8b-1e8f-446e-b899-f5114533b280/hive_2019-03-29_11-26-52_365_8094669471916599336-1/-local-10003/HashTable-Stage-3/MapJoin-mapfile11--.hashtable
2019-03-29 11:26:59     Uploaded 1 File to: file:/tmp/root/c9582a8b-1e8f-446e-b899-f5114533b280/hive_2019-03-29_11-26-52_365_8094669471916599336-1/-local-10003/HashTable-Stage-3/MapJoin-mapfile11--.hashtable (373 bytes)
End of local task; Time Taken: 1.522 sec.
Execution completed successfully
MapredLocal task succeeded
Launching Job 1 out of 1
Number of reduce tasks is set to 0 since there's no reduce operator
Starting Job = job_1553824894278_0005, Tracking URL = http://systemhub611:8088/proxy/application_1553824894278_0005/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553824894278_0005
Hadoop job information for Stage-3: number of mappers: 1; number of reducers: 0
Stage-3 map = 0%,  reduce = 0%
Stage-3 map = 100%,  reduce = 0%, Cumulative CPU 1.44 sec
MapReduce Total cumulative CPU time: 1 seconds 440 msec
Ended Job = job_1553824894278_0005
MapReduce Jobs Launched: 
Stage-Stage-3: Map: 1   Cumulative CPU: 1.44 sec   HDFS Read: 7035 HDFS Write: 126 SUCCESS
Total MapReduce CPU Time Spent: 1 seconds 440 msec
OK
e.empno e.ename d.dname
7369    SMITH   NULL
7499    ALLTE   NULL
7521    WAROS   NULL
7566    JOSSS   NULL
7654    SOCTD   NULL
7698    ADAMS   NULL
7782    JAMSK   NULL
7788    FOESS   NULL
7939    KINGS   NULL
Time taken: 32.565 seconds, Fetched: 9 row(s)
hive (default)> 
```
#### 6.4.5 右外连接
> 右外连接: JOIN操作符右边表中符合WHERE子句的所有记录将会被返回.
```
hive (default)> select e.empno,e.ename,d.dname
              > from emp e right join dept d
              > on e.deptno=d.deptid;
Query ID = root_20190329115001_8d324711-c545-4ea3-bef5-28cc14a11989
Total jobs = 1
19/03/29 11:50:06 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Execution log at: /tmp/root/root_20190329115001_8d324711-c545-4ea3-bef5-28cc14a11989.log
Starting to launch local task to process map join;      maximum memory = 518979584
2019-03-29 11:50:08     Dump the side-table for tag: 0 with group count: 2 into file: file:/tmp/root/c9582a8b-1e8f-446e-b899-f5114533b280/hive_2019-03-29_11-50-01_720_5879451311571173295-1/-local-10003/HashTable-Stage-3/MapJoin-mapfile20--.hashtable
2019-03-29 11:50:09     Uploaded 1 File to: file:/tmp/root/c9582a8b-1e8f-446e-b899-f5114533b280/hive_2019-03-29_11-50-01_720_5879451311571173295-1/-local-10003/HashTable-Stage-3/MapJoin-mapfile20--.hashtable (413 bytes)
End of local task; Time Taken: 1.56 sec.
Execution completed successfully
MapredLocal task succeeded
Launching Job 1 out of 1
Number of reduce tasks is set to 0 since there's no reduce operator
Starting Job = job_1553824894278_0006, Tracking URL = http://systemhub611:8088/proxy/application_1553824894278_0006/
Kill Command = /opt/module/hadoop/bin/hadoop job  -kill job_1553824894278_0006
Hadoop job information for Stage-3: number of mappers: 1; number of reducers: 0
Stage-3 map = 0%,  reduce = 0%
Stage-3 map = 100%,  reduce = 0%, Cumulative CPU 1.42 sec
MapReduce Total cumulative CPU time: 1 seconds 420 msec
Ended Job = job_1553824894278_0006
MapReduce Jobs Launched: 
Stage-Stage-3: Map: 1   Cumulative CPU: 1.42 sec   HDFS Read: 6640 HDFS Write: 61 SUCCESS
Total MapReduce CPU Time Spent: 1 seconds 420 msec
OK
e.empno e.ename d.dname
NULL    NULL    ACCOUNTING
NULL    NULL    RESEARCH
NULL    NULL    SALES
NULL    NULL    OPERATIONS
Time taken: 29.374 seconds, Fetched: 4 row(s)
hive (default)> 
```

#### 6.4.6 满外连接
> 满外连接: 将会返回所有表中符合WHERE语句条件的所有记录,如果任一表的指定字段没有符合条件的值的话,那么就使用NULL值替代.
```
hive (default)> select e.empno,e.ename,d.dname
              > from emp e full join dept d
              > on e.deptno=d.deptid;
Stage-Stage-1: Map: 2  Reduce: 1   Cumulative CPU: 5.24 sec   HDFS Read: 13887 HDFS Write: 187 SUCCESS
Total MapReduce CPU Time Spent: 5 seconds 240 msec
OK
e.empno e.ename d.dname
7939    KINGS   NULL
7788    FOESS   NULL
7782    JAMSK   NULL
7698    ADAMS   NULL
7654    SOCTD   NULL
7566    JOSSS   NULL
7369    SMITH   NULL
7521    WAROS   NULL
7499    ALLTE   NULL
NULL    NULL    ACCOUNTING
NULL    NULL    RESEARCH
NULL    NULL    SALES
NULL    NULL    OPERATIONS
Time taken: 35.59 seconds, Fetched: 13 row(s)
hive (default)> 
```

#### 6.4.7 多表连接
> 注意: 连接n个表,至少需要n-1个连接条件.
> 例如: 连接三个表,至少需要两个连接条件.
> 0.数据准备
```
[root@systemhub711 ~]# cd /opt/module/datas/
[root@systemhub711 datas]# vim location.txt
```
```
1700    Beijing
1800    London
1900    Tokyo
```
> 1.创建位置表
```
hive (default)> create table if not exists default.location(loc int,loc_name string)row format delimited fields terminated by '\t';
OK
Time taken: 0.328 seconds
hive (default)> 
```
> 2.导入数据
```
hive (default)> load data local inpath '/opt/module/datas/location.txt' into table location;
Loading data to table default.location
Table default.location stats: [numFiles=1, totalSize=36]
OK
Time taken: 0.386 seconds
hive (default)> select * from location;
OK
location.loc    location.loc_name
1700    Beijing
1800    London
1900    Tokyo
Time taken: 0.077 seconds, Fetched: 3 row(s)
hive (default)> 
```
> 3.多表连接查询
```
hive (default)> select e.ename,d.dname,l.loc_name
              > from emp e join dept d
              > on e.deptno=d.deptid
              > join location l
              > on d.loc=l.loc;
```
> 大多数情况下,Hive会对每对JOIN连接对象启动一个MapReduce任务.
> 
> 本例中会首先启动一个MapReduce job对表e和表d进行连接操作,然后会再启动一个MapReduce job将第一个MapReduce job的输出和表l;进行连接操作.
> 
> 注意: 为什么不是表d和表l先进行连接操作呢? 这是因为Hive总是按照从左到右的顺序执行的.

#### 6.4.8 笛卡尔积
> 1.笛卡尔集会在下面条件下产生:
> 
> 省略连接条件.
> 
> 连接条件无效.
> 
> 所有表中的所有行互相连接.
> 
> 案例实操
```
hive (default)> select empno, deptno from emp, dept;
Warning: Map Join MAPJOIN[7][bigTable=emp] in task 'Stage-3:MAPRED' is a cross product
Query ID = root_20190329124854_dc330707-1941-4608-8244-1d5bd9214e38
Total jobs = 1
Total MapReduce CPU Time Spent: 1 seconds 470 msec
OK
empno   deptno
7369    NULL
7369    NULL
7369    NULL
7369    NULL
7499    30
7499    30
7499    30
7499    30
7521    30
```
#### 6.4.9 连接谓词中不支持or
> 错误示范
```
hive (default)> select e.empno,e.ename,d.deptno from emp e join dept d on e.deptno=d.deptno or e.ename=d.ename;

FAILED: SemanticException [Error 10019]: Line 1:58 OR not supported in JOIN currently 'ename'
hive (default)> 
```

### 6.5 排序
#### 6.5.1 全局排序 (Order By)
> Order By: 全局排序,一个MapReduce
##### 6.5.1.1 使用`ORDER BY` 子句排序
> ASC (ascend) 升序 (默认)
> DESC (descend) 降序
##### 6.5.1.2 `ORDER BY` 子句在`SELECT`语句结尾
##### 6.5.1.3 案例实操
###### 6.5.1.3.1 查询员工信息按工资升序排列
```
hive (default)> select * from emp order by sal;
Query ID = root_20190329130738_e22bdd23-0e80-43cb-8667-dde41851efa4
Total jobs = 1
Stage-Stage-1: Map: 1  Reduce: 1   Cumulative CPU: 3.13 sec   HDFS Read: 8460 HDFS Write: 472 SUCCESS
Total MapReduce CPU Time Spent: 3 seconds 130 msec
OK
emp.empno       emp.ename       emp.job emp.mgr emp.hiredate    emp.sal emp.comm        emp.deptno
7369    SMITH   CLERKSKLD       7902    1980-12-17      800.0   20.0    NULL
7788    FOESS   CLAEDFDFD       7698    1994-09-17      950.0   30.0    NULL
7782    JAMSK   KIHNGSEHN       7769    1991-06-23      1100.0  20.0    NULL
7521    WAROS   SJDHHJDJX       7869    1984-06-12      1250.18 500.0   30
7499    ALLTE   SALESMANS       7689    1987-02-23      1600.0  300.0   30
7654    SOCTD   MANSJUSSD       4855    1996-02-14      2852.3  30.0    NULL
7566    JOSSS   JDHYHDSDS       4545    1874-05-15      2894.25 20.0    NULL
7939    KINGS   CLADDJHEW       7566    1993-07-12      3000.0  20.0    NULL
7698    ADAMS   JUSHHWESD       4552    1985-05-16      25524.02        30.0    NULL
Time taken: 29.233 seconds, Fetched: 9 row(s)
hive (default)>
```
###### 6.5.1.3.2 查询员工信息按工资降序排列
```
hive (default)> select * from emp order by sal desc;
Query ID = root_20190329131750_d47ccdca-56fa-4b3f-aac1-e9d35e5e44e3
Total MapReduce CPU Time Spent: 3 seconds 450 msec
OK
emp.empno       emp.ename       emp.job emp.mgr emp.hiredate    emp.sal emp.comm        emp.deptno
7698    ADAMS   JUSHHWESD       4552    1985-05-16      25524.02        30.0    NULL
7939    KINGS   CLADDJHEW       7566    1993-07-12      3000.0  20.0    NULL
7566    JOSSS   JDHYHDSDS       4545    1874-05-15      2894.25 20.0    NULL
7654    SOCTD   MANSJUSSD       4855    1996-02-14      2852.3  30.0    NULL
7499    ALLTE   SALESMANS       7689    1987-02-23      1600.0  300.0   30
7521    WAROS   SJDHHJDJX       7869    1984-06-12      1250.18 500.0   30
7782    JAMSK   KIHNGSEHN       7769    1991-06-23      1100.0  20.0    NULL
7788    FOESS   CLAEDFDFD       7698    1994-09-17      950.0   30.0    NULL
7369    SMITH   CLERKSKLD       7902    1980-12-17      800.0   20.0    NULL
```

#### 6.5.2 按照别名排序
> 按照员工薪水的2倍排序
```
hive (default)> select ename,sal*2 twosal from emp order by twosal;
Query ID = root_20190329132035_8bf552a3-03b8-4e33-835b-56f26c8a5a12
Total MapReduce CPU Time Spent: 3 seconds 490 msec
OK
ename   twosal
SMITH   1600.0
FOESS   1900.0
JAMSK   2200.0
WAROS   2500.36
ALLTE   3200.0
SOCTD   5704.6
JOSSS   5788.5
KINGS   6000.0
ADAMS   51048.04
Time taken: 31.107 seconds, Fetched: 9 row(s)
hive (default)> 
```

#### 6.5.3 多列排序
> 按照部门和工资升序排序
```
hive (default)> select ename,deptno,sal from emp order by deptno,sal;
Query ID = root_20190329132255_7a5c8581-0c60-4a17-a726-5f8c1f8d8b36
Total MapReduce CPU Time Spent: 2 seconds 770 msec
OK
ename   deptno  sal
SMITH   NULL    800.0
FOESS   NULL    950.0
JAMSK   NULL    1100.0
SOCTD   NULL    2852.3
JOSSS   NULL    2894.25
KINGS   NULL    3000.0
ADAMS   NULL    25524.02
WAROS   30      1250.18
ALLTE   30      1600.0
Time taken: 28.476 seconds, Fetched: 9 row(s)
hive (default)> 
```
#### 6.5.4 MapReduce内部排序 (Sort By)
> Sort By: 每个MapReduce内部进行排序,对全局结果集来说不是排序.
> 
> 1.设置reduce个数.
```
hive (default)> set mapreduce.job.reduces=3;
```
> 
> 2.查看设置reduce个数.
```
hive (default)> set mapreduce.job.reduces;
mapreduce.job.reduces=3
hive (default)> 
```
> 
> 3.根据部门编号降序查看员工信息.
```
hive (default)> select * from emp sort by empno desc;
Query ID = root_20190329133608_60e6d25c-1197-4a09-8c96-df4fdbb35628
Stage-Stage-1: Map: 1  Reduce: 3   Cumulative CPU: 7.96 sec   HDFS Read: 16132 HDFS Write: 472 SUCCESS
Total MapReduce CPU Time Spent: 7 seconds 960 msec
OK
emp.empno       emp.ename       emp.job emp.mgr emp.hiredate    emp.sal emp.comm        emp.deptno
7939    KINGS   CLADDJHEW       7566    1993-07-12      3000.0  20.0    NULL
7788    FOESS   CLAEDFDFD       7698    1994-09-17      950.0   30.0    NULL
7782    JAMSK   KIHNGSEHN       7769    1991-06-23      1100.0  20.0    NULL
7698    ADAMS   JUSHHWESD       4552    1985-05-16      25524.02        30.0    NULL
7654    SOCTD   MANSJUSSD       4855    1996-02-14      2852.3  30.0    NULL
7566    JOSSS   JDHYHDSDS       4545    1874-05-15      2894.25 20.0    NULL
7521    WAROS   SJDHHJDJX       7869    1984-06-12      1250.18 500.0   30
7499    ALLTE   SALESMANS       7689    1987-02-23      1600.0  300.0   30
7369    SMITH   CLERKSKLD       7902    1980-12-17      800.0   20.0    NULL
Time taken: 32.412 seconds, Fetched: 9 row(s)
hive (default)> 
```

#### 6.5.5 分区排序 (Distribute By)
> Distribute By: 类似MR中partition,进行分区,结合`sort by`使用.
> 注意,Hive要求`DISTRIBUTE BY`语句要写在`SORT BY`语句之前.
> 对于`distribute by`进行测试,一定要分配多reduce进行处理,否则无法看到`distribute by`的效果.
> 

#### 6.5.6 Cluster By
> 当`distribute by`和`sorts by`字段相同时,可以使用`cluster by`方式.
> 
> `cluster by`除了具有`distribute by`的功能外还兼具`sort by`的功能,但是排序只能是倒序排序,不能指定排序规则为`ASC`或者`DESC`.
> 1.以下两种写法等价
```
hive (default)> select * from emp cluster by deptno;

hive (default)> select * from emp distribute by deptno sort by deptno;
```
> 注意: 按照部门编号分区,不一定就是固定死的数值,可以是20号和30号部门分到一个分区里面去.

### 6.6 分桶及抽样查询
#### 6.6.1 分桶表数据存储
> 分区针对的是数据的存储路径,分桶针对的是数据文件.
> 
> 分区提供一个隔离数据和优化查询的便利方式,不过并非所有的数据集都可形成合理的分区,特别是之前所提到过的要确定合适的划分大小这个疑虑.
> 
> 分桶是将数据集分解成更容易管理的若干部分的另一个技术.
> 
##### 6.6.1.1 先创建分桶表,通过直接导入数据文件的方式
###### 6.6.1.1.1 数据准备
```
[root@systemhub711 datas]# vim test_bucket.txt
```
```
1001    101
1002    102
1003    103
1004    104
1005    105
1006    106
1007    107
1008    108
1009    109
1010    110
1011    111
1012    112
1013    113
1014    114
1015    115
1016    116
```
###### 6.6.1.1.2 创建分桶表
```
hive (default)> create table test_bucket(id int,name string)
              > clustered by (id)
              > into 4 buckets
              > row format delimited fields terminated by '\t';
OK
Time taken: 0.138 seconds
hive (default)> 
```
###### 6.6.1.1.3 查看表结构
```
hive (default)> desc formatted test_bucket;
OK
col_name        data_type       comment
# col_name              data_type               comment             
                 
id                      int                                         
name                    string                                      
                 
# Detailed Table Information             
Database:               default                  
Owner:                  root                       
LastAccessTime:         UNKNOWN                  
Protect Mode:           None                     
Retention:              0                        
Location:               hdfs://systemhub511:9000/user/hive/warehouse/test_bucket         
Table Type:             MANAGED_TABLE            
Table Parameters:                
        transient_lastDdlTime   1553865393          
                 
# Storage Information            
SerDe Library:          org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe       
InputFormat:            org.apache.hadoop.mapred.TextInputFormat         
OutputFormat:           org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat       
Compressed:             No                       
Num Buckets:            4                        
Bucket Columns:         [id]                     
Sort Columns:           []                       
Storage Desc Params:             
        field.delim             \t                  
        serialization.format    \t                  
Time taken: 0.123 seconds, Fetched: 28 row(s)
hive (default)> 
```
###### 6.6.1.1.4 导入数据到分桶表中
```
hive (default)> load data local inpath '/opt/module/datas/test_bucket.txt' into table test_bucket;
Loading data to table default.test_bucket
Table default.test_bucket stats: [numFiles=1, totalSize=144]
OK
Time taken: 0.345 seconds
hive (default)> 
```
###### 6.6.1.1.5 查看创建的分桶表中是否分成4个桶
> 发现并没有分成4个桶,是什么原因呢
```
hive (default)> dfs -cat /user/hive/warehouse/test_bucket/*;
1001    101
1002    102
1003    103
1004    104
1005    105
1006    106
1007    107
1008    108
1009    109
1010    110
1011    111
1012    112
1013    113
1014    114
1015    115
1016    116
hive (default)> 
```

##### 6.6.1.2 创建分桶表时,数据通过子查询的方式导入
###### 6.6.1.2.1 新建一个普通test_buck表
```
hive (default)> create table test_buck(id int,name string)
              > row format delimited fields terminated by '\t';
OK
Time taken: 0.084 seconds
hive (default)> 
```
###### 6.6.1.2.2 向普通test_buck表中导入数据
```
hive (default)> load data local inpath '/opt/module/datas/test_bucket.txt' into table test_buck;
Loading data to table default.test_buck
Table default.test_buck stats: [numFiles=1, totalSize=144]
OK
Time taken: 0.239 seconds
hive (default)> 
```
###### 6.6.1.2.3 清空test_bucket表中数据
```
hive (default)> truncate table test_bucket;
OK
Time taken: 0.151 seconds
hive (default)> 
```
###### 6.6.1.2.4 通过子查询的方式,导入数据到分桶表
```
hive (default)> insert into table test_bucket
              > select * from test_buck;
Query ID = root_20190329213846_8d66d5f4-e16d-4725-9231-e9b9dd84c1de
Loading data to table default.test_bucket
Table default.test_bucket stats: [numFiles=1, numRows=16, totalSize=144, rawDataSize=128]
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 1   Cumulative CPU: 1.29 sec   HDFS Read: 3550 HDFS Write: 220 SUCCESS
Total MapReduce CPU Time Spent: 1 seconds 290 msec
OK
test_buck.id    test_buck.name
Time taken: 20.851 seconds
hive (default)> 
```
###### 6.6.1.2.5 发现还是只有一个分桶
```
hive (default)> dfs -cat /user/hive/warehouse/test_bucket/*;
1001    101
1002    102
1003    103
1004    104
1005    105
1006    106
1007    107
1008    108
1009    109
1010    110
1011    111
1012    112
1013    113
1014    114
1015    115
1016    116
hive (default)> 
```
###### 6.6.1.2.6 设置分桶属性
```
hive (default)> set hive.enforce.bucketing=true;
hive (default)> set mapreduce.job.reduces=-1;
hive (default)> insert into table test_bucket
              > select id,name from test_buck cluster by(id);
Loading data to table default.test_bucket
Table default.test_bucket stats: [numFiles=5, numRows=32, totalSize=288, rawDataSize=256]
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 1  Reduce: 4   Cumulative CPU: 9.76 sec   HDFS Read: 15857 HDFS Write: 444 SUCCESS
Total MapReduce CPU Time Spent: 9 seconds 760 msec
OK
id      name
Time taken: 37.969 seconds
hive (default)> 
```
###### 6.6.1.2.7 查询分桶数据
> 查看分桶文件
```
hive (default)> dfs -ls /user/hive/warehouse/test_bucket/*;
-rwxrwxrwx 3 root supergroup 14 /user/hive/warehouse/test_bucket/000000_0
-rwxrwxrwx 3 root supergroup 36 /user/hive/warehouse/test_bucket/000001_0
-rwxrwxrwx 3 root supergroup 36 /user/hive/warehouse/test_bucket/000002_0
-rwxrwxrwx 3 root supergroup 36 /user/hive/warehouse/test_bucket/000003_0
hive (default)> 
```
> 查看分桶数据
```
hive (default)> select * from test_bucket;
OK
test_bucket.id  test_bucket.name
1001    101
1002    102
1003    103
1004    104
1005    105
1006    106
1007    107
1008    108
1009    109
1010    110
1011    111
1012    112
1013    113
1014    114
1015    115
1016    116
1004    104
1008    108
1012    112
1016    116
1001    101
1005    105
1009    109
1013    113
1002    102
1006    106
1010    110
1014    114
1003    103
1007    107
1011    111
1015    115
Time taken: 0.081 seconds, Fetched: 32 row(s)
hive (default)> 
```


#### 6.6.2 分桶抽样查询
> 对于非常大的数据集,有时开发者需要使用的是一个具有代表性的查询结果而不是全部结果,Hive可以通过对表进行抽样来满足这个需求.
> 
#### 6.6.2.1 查询test_bucket表中的数据
```
hive (default)> select * from test_bucket tablesample(bucket 1 out of 4 on id);
OK
test_bucket.id  test_bucket.name
1004    104
1008    108
1012    112
1016    116
1004    104
1008    108
1012    112
1016    116
Time taken: 0.127 seconds, Fetched: 8 row(s)
hive (default)> 
```
> 注: `tablesample`是抽样语句,语法: `TABLESAMPLE(BUCKET x OUT OF y)`
> 
> `x`表示从哪个bucket开始抽取,例如,table总bucket数为4,tablesample(bucket 4 out of 4),表示总共抽取(4/4=)个bucket的数据,抽取第4个bucket数据.
> 
> `y`必须是table总bucket数的倍数或者因子,hive根据y的大小,决定抽样的比例,例如table总共分了4份,当y=2时,抽取(4/2=)2个bucket数据,当y=8时,抽取(4/8=)1/2个bucket数据.
> 
> 注意: x的值必须小于等于y的值,否则
```
FAILED:   SemanticException   [Error   10061]:   Numerator   should   not   be   bigger   than denominator in sample clause for table test_bucket
```

#### 6.6.3 数据块抽样
> Hive提供了另外一种按照百分比进行抽样的方式,这种是基于行数的,按照输入路径下的数据块百分比进行的抽样.
```
hive (default)> select * from test_buck tablesample(0.1 percent);
OK
test_buck.id    test_buck.name
1001    101
1002    102
1003    103
1004    104
1005    105
1006    106
1007    107
1008    108
1009    109
1010    110
1011    111
1012    112
1013    113
1014    114
1015    115
1016    116
Time taken: 0.115 seconds, Fetched: 16 row(s)
hive (default)> 
```
> 提示: 这种抽样方式不一定适用于所有的文件格式,另外这种抽样的最小抽样单元是一个HDFS数据块,因此,如果表的数据大小小于普通的块大小128M的话,那么将会返回所有行.

### 6.7 其他常用查询函数
#### 6.7.1 空字段赋值
##### 6.7.1.1 函数说明
> NVL:给值为NULL的数据赋值,格式是`NVL(string1,replace_with)`.
> 
> 它的功能是如果string1为NULL,则NVL函数返回replace_with的值,否则返回string1的值,如果两个参数为NULL,则返回NULL.
##### 6.7.1.2 数据准备 采用emp数据表
##### 6.7.1.3 查询deptno字段为NULL,则用-1代替
```
hive (default)> select empno,nvl(deptno,-1) from emp;
OK
empno   _c1
7369    -1
7499    30
7521    30
7566    -1
7654    -1
7698    -1
7782    -1
7788    -1
7939    -1
Time taken: 0.066 seconds, Fetched: 9 row(s)
hive (default)> 
```

#### 6.7.2 CASE WHEN
##### 6.7.2.1 数据准备
> user表示用户名, a&b表示部门,男女表示性别
```
user001 A Male
user002 A Male
user003 B Female
user004 A Female
user005 B Female
user006 B Female
```
##### 6.7.2.2 需求
> 计算出不同部分员工性别有多少

##### 6.7.2.3 创建本地文件并导入数据
```
[root@systemhub711 datas]# vim emp_sex.txt
```

##### 6.7.2.4 创建表并导入数据
```
hive (default)> create table emp_sex(name string,dept_id string,sex string) row format delimited fields terminated by ' ';
OK
Time taken: 0.11 seconds
hive (default)> load data local inpath '/opt/module/datas/emp_sex.txt' into table emp_sex;
Loading data to table default.emp_sex
Table default.emp_sex stats: [numFiles=1, totalSize=84]
OK
Time taken: 0.255 seconds
hive (default)> 
```
##### 6.7.2.5 按照需求查询数据
```
hive (default)>  select dept_id,
              > sum(case sex when 'Male' then 1 else 0 end) male_count,
              > sum(case sex when 'Female' then 1 else 0 end) female_count
              > from emp_sex
              > group by dept_id;
Query ID = root_20190329235632_478f9985-3a7f-4c56-8648-fc0c2a760985
Total MapReduce CPU Time Spent: 3 seconds 320 msec
OK
dept_id male_count female_count
A       2       	1
B       1       	2
```



## 🔒 尚未解锁 正在学习探索中... 尽情期待 Blog更新! 🔒


#### 6.7.3 行转列
#### 6.7.4 列转行
#### 6.7.5 窗口函数
#### 6.7.6 Rnak


## 7. 函数
### 7.1 系统函数
### 7.2 自定义函数
### 7.3 自定义UDF函数

## 8. 压缩 & 存储
### 8.1 Hadoop源码编译支持Snappy压缩
### 8.2 Hadoop压缩配置
### 8.3 开启Map输出阶段压缩
### 8.4 开启Reduce输出阶段压缩
### 8.5 文件存储格式
### 8.6 存储和压缩结合

## 9. 企业级调优
### 9.1 Fetch抓取
### 9.2 本地模式
### 9.3 表的优化
### 9.4 数据倾斜
### 9.5 并行执行
### 9.6 严格模式
### 9.7 JVM重用
### 9.8 推测执行
### 9.10 执行计划 (Explain)

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