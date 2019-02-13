# 大数据生态系统 修仙之道 Hadoop Blog

@(2019-01-22)[Docs Language:简体中文 & English|Programing Language:Hadoop|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)|![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg)|GeekDeveloper:[JEEP-711](https://github.com/jeep711)|Github:[github.com/geekparkhub](https://github.com/geekparkhub)|Gitee:[gitee.com/geekparkhub](https://gitee.com/geekparkhub)]

##  🐘 Hadoop Technology 修仙之道 炼精化气 🐘

![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/hadoop.jpg)

- **极客实验室是极客国际公园旗下为未来而构建的极客社区;**
- **我们正在构建一个活跃的小众社区,汇聚众多优秀开发者与设计师;**
- **关注极具创新精神的前沿技术&分享交流&项目合作机会等互联网行业服务;**
- **Open开放 `·` Creation创想 `|` OpenSource开放成就梦想 GeekParkHub共建前所未见!**
- **Future Vision : Establishment of the Geek Foundation;**
- **GeekParkHub GithubHome:**<https://github.com/geekparkhub>
- **GeekParkHub GiteeHome:**<https://gitee.com/geekparkhub>
- **欢迎贡献`各领域开源野生Blog`&`笔记`&`文章`&`片段`&`分享`&`创想`&`OpenSource Project`&`Code`&`Code Review`**
- 🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈 issues: [geekparkhub.github.io/issues](https://github.com/geekparkhub/geekparkhub.github.io/issues) 🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈


-------------------

[TOC]



## 1. 大数据 简介
> 大数据是指无法在一定时间内用常规软件工具对其内容进行抓取、管理和处理的数据集合。大数据技术,是指从各种各样类型的数据中,快速获得有价值信息的能力。适用于大数据的技术,包括大规模并行处理(MPP)据库,数据挖掘电网,分布式文件系统,分布式数据库,云计算平台,互联网,和可扩展的存储系统,大数据由巨型数据集组成,这些数据集大小常超出人类在可接受时间下的收集、庋用、管理和处理能力,大数据的大小经常改变,截至2012年,单一数据集的大小从数太字节(TB)十兆亿字节(PB)等.   —— [MBA智库百科](https://wiki.mbalib.com/wiki/%E5%A4%A7%E6%95%B0%E6%8D%AE)


## 2. 大数据 概论

### 大数据 概念
> **`大数据(BigData)`**是指**`无法在一定时间范围`**内用常规软件工具进行捕捉、管理和处理的数据集合,是需要新处理模式才能具有更强的决策力、洞察发现力和流程优化能力的海量、高增长率和多样化的信息资产.
> 
> 大数据主要解决:海量数据的**`存储`**和海量数据的**`分析计算`**问题.
> 
> 数据存储单位: **`bit`** / **`Byte`** / **`KB`** / **`MB`** / **`GB`** / **`TB`**  / **`PB`** / **`EB`** / **`ZB`** / **`YB`** / **`BB`** / **`NB`** / **`DB`**
> 
> **`1 Byte = 8bit`**
> **`1 KB = 1024Byte`**
> **`1 MB = 1024KB`**
> **`1 GB = 1024MB`**
> **`1 TB = 1024GB`**
> **`1 PB = 1024TB`**
> **`1 EB = 1024PB`**
> **`1 ZB = 1024EB`**
> **`1 YB = 1024ZB`**
> **`1 BB = 1024YB`**
> **`1 NB = 1024BB`**
> **`1 DB = 1024NB`**

### 大数据 特点(4V)
#### 1.Volume (大量)
> 截止目前,人类生产的所有印刷材料的数据量是200PB(1PB=1024TB),而历史上全人类总共说过的话的数量大约是5EB(1EB=1024PB),当前典型个人计算机硬盘的容量为TB量级,而一些大企业的数据量已经近EB量级.
> 
#### 2.Velocity (高速)
> 这是大数据区分于传统数据挖掘的最显著特征,根据IDC的"数字宇宙"报告,预计2020年,全球数据使用量将达到35.2ZB(1 ZB = 1024EB),在如此海量的数据面前,处理数据的效率就是企业的生命.

#### 3.Variety (多样)
> 这种类型的多样性也让数据被分为结构化数据和非结构化数据,相对于以往便于存储的以数据库&文本为主的结构化数据,非结构化数据越来越多,包括网络日志,音频,视频,图片,地理位置信息等,这些多类型的数据对数据的处理能力提出了更高要求.

#### 4.Value (低价值密度)
> 价值密度的高低与数据总量的大小成反比,如何快速对有价值数据"提纯",成为目前大数据背景下待解决的难题.

### 大数据 应用场景
> **`物流仓储`**:大数据分析系统助力商家精细化运营,提升销量,节约成本.
> 
> **`零售`**:分析用户消费习惯,为用户购买商品提供方便,从而提升商品售量,经典故事案例 -《纸尿布+啤酒》.
> 
> **`旅游`**:深度结合大数据能力与旅游行业需求,共建旅游产业智慧管理,智慧服务,智慧营销的未来.
> 
> **`商品广告推荐`**:为用户推荐可能喜欢的商品.
> 
> **`保险`**:海量数据挖掘及风险预测,助力保险行业精准营销,提升精细化定价能力.
> 
> **`金融`**:多维度体现用户特征,帮助金融机构推荐优质客户,防范欺诈风险.
> 
> **`房产`**:大数据全面助力房地产行业,打造精准投策与营销,挑选出更合适的地域.

### 大数据部门业务流程分析
``` sequence
产品人员->数据部门:提出需求(统计总用户数,日活跃用户数,回流用户数等)
数据部门-->数据可视化/报表展示/邮件发送/大屏幕展示等:搭建数据平台,分析数据指标
```
### 大数据部门组织结构(重点)
**大数据部门组织结构**
| 所在组    |  所在组工作职责 |
| :-------- | --------:|
| 平台组  | Hadoop,Flume,Kafka,Hbase,Spark等框架平台搭建,集群性能监控,集群性能调优 |
| 数据仓库组  | ETL工程师-数据清洗,Hive工程师-数据分析,数据仓库建模 |
| 数据挖掘组  | 算法工程师 推荐系统工程师 用户画像工程师 |
| 数据报表开发组  | JAVAEE工程师 |

## 3. 探讨Hadoop框架 大数据生态

### Hadoop 简介

> Apache Hadoop是一款支持数据密集型分布式应用程序并以Apache 2.0许可协议发布的开源软件框架,它支持在商品硬件构建的大型集群上运行的应用程序,Hadoop是根据谷歌公司发表的MapReduce和Google文件系统的论文自行实现而成。所有的Hadoop模块都有一个基本假设,即硬件故障是常见情况,应该由框架自动处理。
> 
> Hadoop框架透明地为应用提供可靠性和数据移动,它实现了名为MapReduce的编程范式:应用程序被分割成许多小部分,而每个部分都能在集群中的任意节点上运行或重新运行。此外,Hadoop还提供了分布式文件系统,用以存储所有计算节点的数据,这为整个集群带来了非常高的带宽。MapReduce和分布式文件系统的设计,使得整个框架能够自动处理节点故障,它使应用程序与成千上万的独立计算的计算机和PB级的数据连接起来,现在普遍认为整个Apache Hadoop"平台"包括Hadoop内核、MapReduce、Hadoop分布式文件系统(HDFS)以及一些相关项目,有Apache Hive和Apache HBase等等.   —— [维基百科](https://zh.wikipedia.org/wiki/Apache_Hadoop)

### Hadoop 是什么
> Hadoop是由Apache基金会所开发的分布式系统基础架构.
> 
> Hadoop主要解决:海量**`数据的存储`**和海量**`数据的分析计算`**问题
> 
> 广义上来讲,Hadoop通常是指一个更广泛的概念 --- Hadoop生态圈

### Hadoop 发展历史
> 1.Hadoop创始人:Doug Cutting
> 
> Lucene框架是Doug Cutting开创的开源软件,使用java编程语言开发,实现与Google类似的全文搜索功能,它提供了全文检索引擎的架构,包括完整的查询引擎和索引引擎.
> 
> 2.2001年年底Lucene成为Apache基金会的一个子项目.
> 
> 3.对于海量数据的场景,Lucene面对与Google同样的困难,存储数据困难,检索速度慢.
> 
> 4.学习和模仿Google解决这些问题的办法:(Lucene的升级版) Nutch.
> 
> 5.可以说Google是Hadoop的思想之源(Google在大数据方面的三篇论文)
> 
> GFS ---> HDFS
> Map-MapReduce ---> MR
> BigTable ---> Hbase
> 
> 6.2003至2004年,Google公开了部分GFS和MapReduce思想细节,以此为基础Doug Cutting等开发者用了2年业余时间实现了DFS和MapReduce机制,使Nutch性能飙升.
> 
> 7.2005年Hadoop作为Lucene的子项目,Nutch的一部分正式引入Apache基金会.
> 
> 8.2006年3月份,Map-Reduce和NDFS(Nutch Distributed File System),分别被纳入称为Hadoop的项目中.
> 
> 9.Hadoop名字来源于Doug Cutting孩子的玩具大象.
> 
> 10.Hadoop就此诞生并迅速发展,标志着大数据时代来临.

### Hadoop 三大发行版本
> Hadoop 三大发行版本 **`Apache`** | **`Cloudera`** | **`Hortonworks`**

#### Apache Hadoop
> Apache版本最最原始(最基础)版本,对于入门学习最佳.
> 
> 官网地址 : http://hadoop.apache.org/releases.html
> 
> 下载地址 : https://archive.apache.org/dist/hadoop/common/

#### Cloudera Hadoop
> Cloudera在大型互联网企业中应用场景较多.
> 
> 官网地址 : https://www.cloudera.com/downloads/cdh/5-10-0.html
> 
> 下载地址 : http://archive.cloudera.com/cdh5/cdh/5/
> 
> 2008年成立的Cloudera是最早将Hadoop商用公司,为合作伙伴提供Hadoop的商业解决方案,主要是包括支持,咨询服务,培训.
> 
> 2009年Hadoop创始人Doug Cutting也加盟了Cloudera公司,Cloudera产品主要为CDH,Cloudera Manager | Cloudera Support.
> 
> CDH是Cloudera的Hadoop发行版,完全开源,比Apache Hadoop在兼容性,安全性,稳定性上有所增强.
> 
> Cloudera Manager是集群的软件分发及管理监控平台,可以再几个小时内部部署好一个Hadoop集群,并对集群节点及服务
进行实时监控,Cloudera Support即是对Hadoop的技术支持.
> 
> Cloudera的标价为每年每个节点4000美元,Cloudera开发并贡献了可实时处理大数据的Impala项目.

#### Hortonworks Hadoop
> Hortonworks文档较好.
> 
> 官网地址 : https://hortonworks.com/products/data-center/hdp/
> 
> 下载地址 : https://hortonworks.com/downloads/#data-platform
> 
> 2011年成立的Hortonworks是雅虎与硅谷风投公司Benchmark Capital合资组建.
> 
> 公司成立之初就吸纳了大约25名至30名专门研究Hadoop的雅虎工程师,上述工程师均在2005年开始协助雅虎开发Hadoop,并贡献了80%的Hadoop代码.
> 
> 雅虎工程副总裁,雅虎Hadoop开发团队负责人Eric Baldeschwieler出任Hortonworks的首席执行官.
> 
> Hortonworks主打产品是Hortonworks Data Platform(HDP),也同样是100%开源产品,HDP除常见的项目外还包括Ambari,一款开源的安装和管理系统.
> 
> HCatalog 一个元数据管理系统,HCatalog现已集成到Facebook开源的Hive中,Hortonworks的Stinger开创性的极大的优化了Hive项目,Hortonworks为入门提供一个非常好的易于使用的沙盒.
> 
> Hortonworks开发了很多增强特性并提交至核心主干,这使得Apache Hadoop能够在包括Window Server和Windowns Azure在内的Microsoft Windows平台上本地运行,定价以集群为基础,每10个节点每年为12500美元.

### Hadoop 优势 (4高)
#### 1.高可靠性
> Hadoop底层维护多个数据副本,所以即使Haoop某个计算元素或存储出现故障,也不会导致数据的丢失.
#### 2.高扩展性
> 在集群间分配任务数据,可方便的扩展数以千计的节点.
#### 3.高效性
> 在MapReduce的思想下,Hadoop是并行工作,以加快任务处理速度.
#### 4.高容错性
> 能够自动将失败的任务重新分配.



### Hadoop 组成(面试重点)
#### Hadoop1.x与Hadoop2.x 区别
> Hadoop1.x组成 : **`MapReduce(计算+资源调度)`** | **`HDFS(数据存储)`** | **`Common(辅助工具)`**
> 
> Hadoop2.x组成 : **`MapReduce(计算)`** | **`Yarn(资源调度)`** | **`HDFS(数据存储)`** | **`Common(辅助工具)`**
> 
> 在Hadoop1.x时代,Hadoop中的MapReduce同时处理业务逻辑运算和资源的调度,所以耦合性较大.
> 
> 在Hadoop2.x时代,增加了Yarn,Yarn只负责资源的调度,MapReduce只负责运算.

#### HDFS 架构概述
HDFS (Hadoop Distributed File System) | **`三大组件 nn / dn / 2nn`**
> 1.NameNode(nn) : 存储文件的元数据,如文件名,文件目录结构,文件属性(生成时间,副本数,文件权限,),以及每个文件的块列表和块所在的DataNode等.
> 
> 2.DataNode(dn) : 在本地文件系统存储文件块数据,以及块数据的校验和.
> 
> 3.Secondary NameNode(2nn):用来监控HDFS状态的辅助后台程序,每隔一段时间获取HDFS元数据的快照.

#### YARN 架构概述
**`四大组件 | RM / NM / AM / Container`**
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_001.jpg)

#### MapReduce 架构概述
> **`两大阶段 | Map / Reduce`**
> 
> MapReduce将计算过程分为两个阶段:Map 和 Reduce
> 
> Map阶段并行处理输入数据 | Reduce阶段对Map结果进行汇总
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_002.jpg)

### 大数据技术 生态体系
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_003.jpg)

### 推荐 系统框架图
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_004.jpg)


## 4. Hadoop 运行环境搭建(开发重点)
### 虚拟机环境 准备
#### 1.克隆虚拟机
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_005.jpg)
#### 2.修改克隆虚拟机的静态IP
> 使用root用户登录
**`vim /etc/udev/rules.d/70-persistent-net.rules`**

源代码
``` bash
# This file was automatically generated by the /lib/udev/write_net_rules
# program, run by the persistent-net-generator.rules rules file.
#
# You can modify it, as long as you keep each rule on a single
# line, and change only the value of the NAME= key.

# PCI device 0x8086:0x100f (e1000)
SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="00:0c:29:a3:d8:a7", ATTR{type}=="1", KERNEL=="eth*", NAME="eth0"

# PCI device 0x8086:0x100f (e1000)
SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="00:0c:29:67:b3:77", ATTR{type}=="1", KERNEL=="eth*", NAME="eth1"
```

将NAME="eth1"更改为NAME="eth0",并复制00:0c:29:67:b3:77地址
``` bash
# PCI device 0x8086:0x100f (e1000)
SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="00:0c:29:67:b3:77", ATTR{type}=="1", KERNEL=="eth*", NAME="eth0"
```
更改完毕,`:wq`保存退出

修改网络配置
粘贴上一步地址,修改HWADDR属性
**`vim /etc/sysconfig/network-scripts/ifcfg-eth0`**
```bash
DEVICE=eth0
HWADDR=00:0c:29:67:b3:77
TYPE=Ethernet
UUID=b75136b3-4a81-41b5-9ebd-bfc1831d0df7
ONBOOT=yes
NM_CONTROLLED=yes
BOOTPROTO=static

IPADDR=192.168.177.131
GATEWAY=192.168.177.2
DNS1=192.168.177.2
```
更改完毕,`:wq`保存退出

#### 3.修改主机名
`vim /etc/sysconfig/network`
``` bash
NETWORKING=yes
HOSTNAME=corehub-004
```
更改完毕,`:wq`保存退出

#### 4.关闭防火墙
暂时性关闭防火墙:`service iptables stop`

#### 5.创建用户
`useradd username`

#### 6.配置用户具有root权限
`vim /etc/sudoers`
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_006.jpg)
更改完毕,`:wq!`保存退出

#### 7.在/opt目录下创建文件夹
> 1.创建software,module文件夹
> software 用于日后存储的程序安装包
> module 用于日后存储解析后的程序jar包
```
sudo mkdir software
sudo mkdir module
```
``` powershell
[geek-developer@corehub-001 ~]$ cd /opt/
[geek-developer@corehub-001 opt]$ ll
total 8
drwxr-xr-x. 6 root root 4096 Jan 17 23:35 devtool
drwxr-xr-x. 2 root root 4096 Oct  4  2017 rh
[geek-developer@corehub-001 opt]$ sudo mkdir software
[sudo] password for geek-developer: 
[geek-developer@corehub-001 opt]$ sudo mkdir module
[geek-developer@corehub-001 opt]$ ll
total 16
drwxr-xr-x. 6 root root 4096 Jan 17 23:35 devtool
drwxr-xr-x. 2 root root 4096 Jan 24 20:12 module
drwxr-xr-x. 2 root root 4096 Oct  4  2017 rh
drwxr-xr-x. 2 root root 4096 Jan 24 20:11 software
[geek-developer@corehub-001 opt]$ 
```
2.修改software,module文件夹的所有者
``` powershell
[geek-developer@corehub-001 opt]# chown geek-developer:geek-developer software/ module/
[geek-developer@corehub-001 opt]# ll
total 16
drwxr-xr-x. 6 root           root           4096 Jan 17 23:35 devtool
drwxr-xr-x. 2 geek-developer geek-developer 4096 Jan 24 20:12 module
drwxr-xr-x. 2 root           root           4096 Oct  4  2017 rh
drwxr-xr-x. 2 geek-developer geek-developer 4096 Jan 24 20:11 software
[geek-developer@corehub-001 opt]# 
```

### 安装 Hadoop
> 在安装Hadoop前提是需要先安装JAVA并配置环境变量即可
> 
> Apache Hadoop官方地址 : https://archive.apache.org/dist/hadoop/common/hadoop-2.7.2/
> 
> 通过远程工具,将hadoop-2.7.2.tar.gz传输到/op/tsoftware/目录下
> 

将hadoop-2.7.2.tar.gz解压/opt/module/目录下
```
tar -zxvf hadoop-2.7.2.tar.gz -C /opt/module
```
将解压完成hadoop-2.7.2重命名为hadoop
``` powershell
[root@corehub-001 software]# cd ..
[root@corehub-001 opt]# cd module/
[root@corehub-001 module]# ll
total 4
drwxr-xr-x. 9 10011 10011 4096 Jan 26  2016 hadoop-2.7.2
[root@corehub-001 module]# mv hadoop-2.7.2 hadoop
[root@corehub-001 module]# ll
total 4
drwxr-xr-x. 9 10011 10011 4096 Jan 26  2016 hadoop
[root@corehub-001 module]# 
```
配置hadoop环境变量
```
[root@corehub-001 module]# cd hadoop/
[root@corehub-001 hadoop]# pwd
/opt/module/hadoop
[root@corehub-001 hadoop]#
```
```
[root@corehub-001 geek-developer]# vim /etc/profile
```
```
##HADOOP_HOME
export HADOOP_HOME=/opt/module/hadoop
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
```
完成环境变量,`:wq`保存退出
`source /etc/profile` 更新配置文件指令
```
[root@corehub-001 geek-developer]# source /etc/profile
[root@corehub-001 geek-developer]# hadoop
Usage: hadoop [--config confdir] [COMMAND | CLASSNAME]
  CLASSNAME            run the class named CLASSNAME
 or
  where COMMAND is one of:
  fs                   run a generic filesystem user client
  version              print the version
  jar <jar>            run a jar file
                       note: please use "yarn jar" to launch
                             YARN applications, not this command.
  checknative [-a|-h]  check native hadoop and compression libraries availability
  distcp <srcurl> <desturl> copy file or directories recursively
  archive -archiveName NAME -p <parent path> <src>* <dest> create a hadoop archive
  classpath            prints the class path needed to get the
  credential           interact with credential providers
                       Hadoop jar and the required libraries
  daemonlog            get/set the log level for each daemon
  trace                view and modify Hadoop tracing settings

Most commands print help when invoked w/o parameters.
[root@corehub-001 geek-developer]# 
```


### Hadoop 目录结构
> **`bin目录`** :  Hadoop服务脚本.
> 
> **`etc目录`** :  Hadoop的配置文件目录,存放Haoop配置文件.
> 
> **`lib目录`** : 存放Hadoop本地库,(对数据进行压缩解压功能).
> 
> **`sbin目录`** : 存放启动或停止Hadoop相关服务脚本.
> 
> **`share目录`** : 存放Hadoop依赖jar包,文档,官方案例.


## 5. Hadoop 运行模式
> Hadoop运行模式包括 : **`本地运行`** / **`伪分布式运行`** / **`完全分布式运行`**
### 🎉🎉 本地运行模式 🎉🎉
#### 👨‍💻👨‍💻 Grep 官方案例 👨‍💻👨‍💻
> 官方案例地址 : [Standalone Operation](http://hadoop.apache.org/docs/r2.7.2/hadoop-project-dist/hadoop-common/SingleCluster.html)
> 
> By default, Hadoop is configured to run in a non-distributed mode, as a single Java process. This is useful for debugging.
> 
> The following example copies the unpacked conf directory to use as input and then finds and displays every match of the given regular expression. Output is written to the given output directory.
> ```
> $ mkdir input
> $ cp etc/hadoop/*.xml input
> $ bin/hadoop jar s
> ```

##### 1.快速开始,在hadoop目录下 创建input文件夹
``` powershell
[geek-developer@corehub-001 ~]$ cd /opt/module/hadoop/
[geek-developer@corehub-001 hadoop]$ ll
total 52
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 bin
drwxr-xr-x. 3 10011 10011  4096 Jan 26  2016 etc
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 include
drwxr-xr-x. 3 10011 10011  4096 Jan 26  2016 lib
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 libexec
-rw-r--r--. 1 10011 10011 15429 Jan 26  2016 LICENSE.txt
-rw-r--r--. 1 10011 10011   101 Jan 26  2016 NOTICE.txt
-rw-r--r--. 1 10011 10011  1366 Jan 26  2016 README.txt
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 sbin
drwxr-xr-x. 4 10011 10011  4096 Jan 26  2016 share
[geek-developer@corehub-001 hadoop]$ sudo mkdir input
[geek-developer@corehub-001 hadoop]$ ll
total 56
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 bin
drwxr-xr-x. 3 10011 10011  4096 Jan 26  2016 etc
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 include
drwxr-xr-x. 2 root  root   4096 Jan 24 22:23 input
drwxr-xr-x. 3 10011 10011  4096 Jan 26  2016 lib
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 libexec
-rw-r--r--. 1 10011 10011 15429 Jan 26  2016 LICENSE.txt
-rw-r--r--. 1 10011 10011   101 Jan 26  2016 NOTICE.txt
-rw-r--r--. 1 10011 10011  1366 Jan 26  2016 README.txt
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 sbin
drwxr-xr-x. 4 10011 10011  4096 Jan 26  2016 share
[geek-developer@corehub-001 hadoop]$ 
```
##### 2.在hadoop目录中,将etc文件夹内 以.xml为后缀的配置文件拷贝到input文件夹里
```
[geek-developer@corehub-001 hadoop]$ sudo cp etc/hadoop/*.xml input/
[geek-developer@corehub-001 hadoop]$ ls input/
capacity-scheduler.xml  hadoop-policy.xml  httpfs-site.xml  kms-site.xml
core-site.xml           hdfs-site.xml      kms-acls.xml     yarn-site.xml
[geek-developer@corehub-001 hadoop]$ 
```

##### 3.执行share目录下的hadoop-mapreduce-examples-2.7.2.jar包,并指定输入和输出路径,以符合正则表达式并统计个数
`dfs[a-z.]+` 以dfs开头,以a到z任意字符以.过滤掉 - - 字符
``` powershell
[root@corehub-001 geek-developer]# cd /opt/module/hadoop/
##########执行share目录下的hadoop-mapreduce-examples-2.7.2.jar包,并指定输入和输出路径#############
[root@corehub-001 hadoop]# hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.2.jar grep input/ output 'dfs[a-z.]+'
19/01/24 22:43:48 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
19/01/24 22:43:48 INFO Configuration.deprecation: session.id is deprecated. Instead, use dfs.metrics.session-id
19/01/24 22:43:48 INFO jvm.JvmMetrics: Initializing JVM Metrics with processName=JobTracker, sessionId=
19/01/24 22:43:50 INFO output.FileOutputCommitter: Saved output of task 'attempt_local1034400674_0001_r_000000_0' to file:/opt/module/hadoop/grep-temp-1632689888/_temporary/0/task_local1034400674_0001_r_000000
19/01/24 22:43:50 INFO mapred.LocalJobRunner: reduce > reduce
19/01/24 22:43:50 INFO mapred.Task: Task 'attempt_local1034400674_0001_r_000000_0' done.
19/01/24 22:43:50 INFO mapred.LocalJobRunner: Finishing task: attempt_local1034400674_0001_r_000000_0
19/01/24 22:43:50 INFO mapred.LocalJobRunner: reduce task executor complete.
19/01/24 22:43:50 INFO mapreduce.Job: Job job_local1034400674_0001 running in uber mode : false
19/01/24 22:43:50 INFO mapreduce.Job:  map 100% reduce 100%
19/01/24 22:43:50 INFO mapreduce.Job: Job job_local1034400674_0001 completed successfully
19/01/24 22:43:50 INFO mapreduce.Job: Counters: 30
	File System Counters
		FILE: Number of bytes read=2691317
		FILE: Number of bytes written=5002436
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
	Map-Reduce Framework
		Map input records=745
		Map output records=1
		Map output bytes=17
		Map output materialized bytes=67
		Input split bytes=877
		Combine input records=1
		Combine output records=1
		Reduce input groups=1
		Reduce shuffle bytes=67
		Reduce input records=1
		Reduce output records=1
		Spilled Records=2
		Shuffled Maps =8
		Failed Shuffles=0
		Merged Map outputs=8
		GC time elapsed (ms)=147
		Total committed heap usage (bytes)=2574778368
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
	File Input Format Counters 
		Bytes Read=26007
	File Output Format Counters 
		Bytes Written=123
[root@corehub-001 hadoop]# ll
total 60
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 bin
drwxr-xr-x. 3 10011 10011  4096 Jan 26  2016 etc
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 include
drwxr-xr-x. 2 root  root   4096 Jan 24 22:28 input
drwxr-xr-x. 3 10011 10011  4096 Jan 26  2016 lib
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 libexec
-rw-r--r--. 1 10011 10011 15429 Jan 26  2016 LICENSE.txt
-rw-r--r--. 1 10011 10011   101 Jan 26  2016 NOTICE.txt
drwxr-xr-x. 2 root  root   4096 Jan 24 22:43 output
-rw-r--r--. 1 10011 10011  1366 Jan 26  2016 README.txt
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 sbin
drwxr-xr-x. 4 10011 10011  4096 Jan 26  2016 share
[root@corehub-001 hadoop]# ll output/
total 4
-rw-r--r--. 1 root root 11 Jan 24 22:43 part-r-00000
-rw-r--r--. 1 root root  0 Jan 24 22:43 _SUCCESS
############cd 进入output目录下############
[root@corehub-001 hadoop]# cd output/
############最后查看符合正则表达式并统计个数############
[root@corehub-001 output]# cat part-r-00000 
1	dfsadmin
[root@corehub-001 output]#
```

#### 👨‍💻👨‍💻 WordCount 官方案例 👨‍💻👨‍💻
##### 1.在hadoop目录下,创建一个wcinput文件夹
``` powershell
[root@corehub-001 hadoop]# mkdir wcinput
[root@corehub-001 hadoop]# ll
total 64
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 bin
drwxr-xr-x. 3 10011 10011  4096 Jan 26  2016 etc
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 include
drwxr-xr-x. 2 root  root   4096 Jan 24 22:28 input
drwxr-xr-x. 3 10011 10011  4096 Jan 26  2016 lib
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 libexec
-rw-r--r--. 1 10011 10011 15429 Jan 26  2016 LICENSE.txt
-rw-r--r--. 1 10011 10011   101 Jan 26  2016 NOTICE.txt
drwxr-xr-x. 2 root  root   4096 Jan 24 22:43 output
-rw-r--r--. 1 10011 10011  1366 Jan 26  2016 README.txt
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 sbin
drwxr-xr-x. 4 10011 10011  4096 Jan 26  2016 share
drwxr-xr-x. 2 root  root   4096 Jan 24 23:07 wcinput
[root@corehub-001 hadoop]# 
```
##### 2.在wcinput文件下创建一个wc.input文件
```
[root@corehub-001 hadoop]# cd wcinput/
[root@corehub-001 wcinput]# touch wc.input
[root@corehub-001 wcinput]# ll
total 0
-rw-r--r--. 1 root root 0 Jan 24 23:08 wc.input
[root@corehub-001 wcinput]# 
```
##### 3.编辑wc.input文件并在文件中输入内容,输入完毕按esc,输入:wq保存退出
```
[root@corehub-001 wcinput]# vim wc.input
```
```
hello-world
hello-world
java
python
php
golang
hadoop yarn
hadoop mapreduce
hive
spark
java
springcloud
springboot
geek
geekpark
geekparkhub
geekparkhub
geek-developer
jeep-711
jeep-711
github
~                                           
~   
```
##### 4.返回hadoop目录
```
[root@corehub-001 wcinput]# cd ..
[root@corehub-001 hadoop]# 
```
##### 5.执行程序
``` powershell
[root@corehub-001 hadoop]# hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.2.jar wordcount wcinput wcoutput
19/01/24 23:20:50 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
19/01/24 23:20:50 INFO Configuration.deprecation: session.id is deprecated. Instead, use dfs.metrics.session-id
19/01/24 23:20:50 INFO jvm.JvmMetrics: Initializing JVM Metrics with processName=JobTracker, sessionId=
19/01/24 23:20:50 INFO input.FileInputFormat: Total input paths to process : 1
19/01/24 23:20:50 INFO mapreduce.JobSubmitter: number of splits:1
19/01/24 23:20:51 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_local450202257_0001
19/01/24 23:20:51 INFO mapreduce.Job: The url to track the job: http://localhost:8080/
19/01/24 23:20:51 INFO mapreduce.Job: Running job: job_local450202257_0001
19/01/24 23:20:51 INFO output.FileOutputCommitter: Saved output of task 'attempt_local450202257_0001_r_000000_0' to file:/opt/module/hadoop/wcoutput/_temporary/0/task_local450202257_0001_r_000000
19/01/24 23:20:51 INFO mapred.LocalJobRunner: reduce > reduce
19/01/24 23:20:51 INFO mapred.Task: Task 'attempt_local450202257_0001_r_000000_0' done.
19/01/24 23:20:51 INFO mapred.LocalJobRunner: Finishing task: attempt_local450202257_0001_r_000000_0
19/01/24 23:20:51 INFO mapred.LocalJobRunner: reduce task executor complete.
19/01/24 23:20:52 INFO mapreduce.Job: Job job_local450202257_0001 running in uber mode : false
19/01/24 23:20:52 INFO mapreduce.Job:  map 100% reduce 100%
19/01/24 23:20:52 INFO mapreduce.Job: Job job_local450202257_0001 completed successfully
19/01/24 23:20:52 INFO mapreduce.Job: Counters: 30
	File System Counters
		FILE: Number of bytes read=547482
		FILE: Number of bytes written=1105096
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
	Map-Reduce Framework
		Map input records=4
		Map output records=6
		Map output bytes=77
		Map output materialized bytes=77
		Input split bytes=105
		Combine input records=6
		Combine output records=5
		Reduce input groups=5
		Reduce shuffle bytes=77
		Reduce input records=5
		Reduce output records=5
		Spilled Records=10
		Shuffled Maps =1
		Failed Shuffles=0
		Merged Map outputs=1
		GC time elapsed (ms)=0
		Total committed heap usage (bytes)=397410304
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
	File Input Format Counters 
		Bytes Read=53
	File Output Format Counters 
		Bytes Written=63
[root@corehub-001 hadoop]# 
```
##### 6.查看统计单词的个数结果 | 😍😍 深深感受到大数据的魅力所在 😍😍
``` powershell
[root@corehub-001 hadoop]# ll
total 68
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 bin
drwxr-xr-x. 3 10011 10011  4096 Jan 26  2016 etc
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 include
drwxr-xr-x. 2 root  root   4096 Jan 24 22:28 input
drwxr-xr-x. 3 10011 10011  4096 Jan 26  2016 lib
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 libexec
-rw-r--r--. 1 10011 10011 15429 Jan 26  2016 LICENSE.txt
-rw-r--r--. 1 10011 10011   101 Jan 26  2016 NOTICE.txt
drwxr-xr-x. 2 root  root   4096 Jan 24 22:43 output
-rw-r--r--. 1 10011 10011  1366 Jan 26  2016 README.txt
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 sbin
drwxr-xr-x. 4 10011 10011  4096 Jan 26  2016 share
drwxr-xr-x. 2 root  root   4096 Jan 24 23:33 wcinput
drwxr-xr-x. 2 root  root   4096 Jan 24 23:34 wcoutput
[root@corehub-001 hadoop]# ll wcoutput/
total 4
-rw-r--r--. 1 root root 184 Jan 24 23:34 part-r-00000
-rw-r--r--. 1 root root   0 Jan 24 23:34 _SUCCESS
[root@corehub-001 hadoop]# cd wcoutput/
[root@corehub-001 wcoutput]# cat part-r-00000 
geek	1
geek-developer	1
geekpark	1
geekparkhub	2
github	1
golang	1
hadoop	2
hello-world	2
hive	1
java	2
jeep-711	2
mapreduce	1
php	1
python	1
spark	1
springboot	1
springcloud	1
yarn	1
[root@corehub-001 wcoutput]# 
```

###  🎉🎉 伪分布式 运行模式 🎉🎉
#### 启动HDFS并运行MapReduce程序
> 分析 : 配置集群,启动测试集群增删查,执行WordCount案例
##### 配置集群
###### 配置 hadoop-env.sh,获取jdk安装路径
获取并复制JAVA_HOME路径
```
[root@corehub-001 hadoop]# echo $JAVA_HOME
/opt/jdk1.8.0_162
```
配置hadoop-env.sh
```
[root@corehub-001 hadoop]# vim etc/hadoop/hadoop-env.sh
```
``` powershell
# The only required environment variable is JAVA_HOME.  All others are
# optional.  When running a distributed configuration it is best to
# set JAVA_HOME in this file, so that it is correctly defined on
# remote nodes.

# The java implementation to use.
export JAVA_HOME=/opt/jdk1.8.0_162
```

###### 配置 **`core-site.xml`**
> core-site.xml 官方文档说明 : [core-default.xml](http://hadoop.apache.org/docs/r2.7.2/hadoop-project-dist/hadoop-common/core-default.xml)

```
[root@corehub-001 hadoop]# vim etc/hadoop/core-site.xml
```
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->
<!-- Put site-specific property overrides in this file. -->

<configuration>
<!-- 指定HDFS中的NameNode地址 -->
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://corehub-001:9000</value>
  </property>
<!-- 指定Hadoop运行时产生文件的存储目录 -->
   <property>
     <name>hadoop.tmp.dir</name>
     <value>/opt/module/hadoop/data/tmp</value>
   </property>
</configuration>
```
输入完毕按esc,输入:wq保存退出

###### 配置 **`hdfs.site.xml`**
> hdfs.site.xml 官方文档说明 : [hdfs-default.xml](http://hadoop.apache.org/docs/r2.7.2/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml)
```
[root@corehub-001 hadoop]# vim etc/hadoop/hdfs-site.xml
```
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->

<!-- Put site-specific property overrides in this file. -->

<configuration>
<!-- 指定HDFS副本数量 -->
  <property>
   <name>dfs.replication</name>
     <value>1</value>
  </property>
</configuration>
```
输入完毕按esc,输入:wq保存退出

##### 启动集群
###### 格式化 NameNode
> (第一次初始化启动需要格式化,只需在首次启动前格式化)
```
[root@corehub-001 hadoop]# bin/hdfs namenode -format
19/01/25 12:59:38 INFO namenode.NameNode: STARTUP_MSG: 
/************************************************************
STARTUP_MSG: Starting NameNode
STARTUP_MSG:   host = corehub-001/192.168.152.130
STARTUP_MSG:   args = [-format]
STARTUP_MSG:   version = 2.7.2
STARTUP_MSG:   classpath = /opt/module/hadoop/etc/hadoop:/opt/module/hadoop/share/hadoop/common/lib/jsp-api-2.1.jar:/opt/module/hadoop/share/hadoop/common/lib/servlet-api-2.5.jar:/opt/module/hadoop/share/hadoop/common/lib/jsch-
STARTUP_MSG:   build = https://git-wip-us.apache.org/repos/asf/hadoop.git -r b165c4fe8a74265c792ce23f546c64604acf0e41; compiled by 'jenkins' on 2016-01-26T00:08Z
STARTUP_MSG:   java = 1.8.0_162
************************************************************/
19/01/25 12:59:38 INFO namenode.NameNode: registered UNIX signal handlers for [TERM, HUP, INT]
19/01/25 12:59:38 INFO namenode.NameNode: createNameNode [-format]
19/01/25 12:59:38 INFO blockmanagement.DatanodeManager: dfs.block.invalidate.limit=1000
19/01/25 12:59:38 INFO blockmanagement.DatanodeManager: dfs.namenode.datanode.registration.ip-hostname-check=true
19/01/25 12:59:38 INFO blockmanagement.BlockManager: dfs.namenode.startup.delay.block.deletion.sec is set to 000:00:00:00.000
19/01/25 12:59:38 INFO blockmanagement.BlockManager: The block deletion will start around 2019 Jan 25 12:59:38
19/01/25 12:59:39 INFO util.GSet: Computing capacity for map NameNodeRetryCache
19/01/25 12:59:39 INFO util.GSet: VM type       = 64-bit
19/01/25 12:59:39 INFO util.GSet: 0.029999999329447746% max memory 889 MB = 273.1 KB
19/01/25 12:59:39 INFO util.GSet: capacity      = 2^15 = 32768 entries
19/01/25 12:59:39 INFO namenode.FSImage: Allocated new BlockPoolId: BP-169105537-192.168.152.130-1548449979185
19/01/25 12:59:39 INFO common.Storage: Storage directory /opt/module/hadoop/data/tmp/dfs/name has been successfully formatted.
19/01/25 12:59:39 INFO namenode.NNStorageRetentionManager: Going to retain 1 images with txid >= 0
19/01/25 12:59:39 INFO util.ExitUtil: Exiting with status 0
19/01/25 12:59:39 INFO namenode.NameNode: SHUTDOWN_MSG: 
/************************************************************
SHUTDOWN_MSG: Shutting down NameNode at corehub-001/192.168.152.130
************************************************************/
[root@corehub-001 hadoop]# ll
total 72
drwxr-xr-x. 2 10011 10011  4096 Jan 25  2016 bin
drwxr-xr-x. 3 root  root   4096 Jan 25 12:59 data
drwxr-xr-x. 3 10011 10011  4096 Jan 25  2016 etc
drwxr-xr-x. 2 10011 10011  4096 Jan 25  2016 include
drwxr-xr-x. 2 root  root   4096 Jan 25 09:44 input
drwxr-xr-x. 3 10011 10011  4096 Jan 25  2016 lib
drwxr-xr-x. 2 10011 10011  4096 Jan 25  2016 libexec
-rw-r--r--. 1 10011 10011 15429 Jan 25  2016 LICENSE.txt
-rw-r--r--. 1 10011 10011   101 Jan 25  2016 NOTICE.txt
drwxr-xr-x. 2 root  root   4096 Jan 25 09:45 output
-rw-r--r--. 1 10011 10011  1366 Jan 25  2016 README.txt
drwxr-xr-x. 2 10011 10011  4096 Jan 25  2016 sbin
drwxr-xr-x. 4 10011 10011  4096 Jan 25  2016 share
drwxr-xr-x. 2 root  root   4096 Jan 25 09:47 wcinput
drwxr-xr-x. 2 root  root   4096 Jan 25 09:48 wcoutput
[root@corehub-001 hadoop]# 
```
###### 启动 NameNode
```
[root@corehub-001 hadoop]# sbin/hadoop-daemon.sh start namenode
starting namenode, logging to /opt/module/hadoop/logs/hadoop-root-namenode-corehub-001.out
[root@corehub-001 hadoop]# jps
3153 Jps
3022 NameNode
```

###### 启动 DataNode
```
[root@corehub-001 hadoop]# sbin/hadoop-daemon.sh start datanode
starting datanode, logging to /opt/module/hadoop/logs/hadoop-root-datanode-corehub-001.out
[root@corehub-001 hadoop]# jps
3696 DataNode
3858 Jps
3022 NameNode
[root@corehub-001 hadoop]# 
```

##### 查看是否启动成功
> 可通过hadoop提供website图形化界面 查看启动结果
> 
> 通过 LinuxHostName:50070端口号形式访问 或 通过 Linux IPaddr:50070端口号访问
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_007.jpg)
##### 以hdfs指令 创建多级目录
> 类似于Linux目录树结构一致,可见熟练掌握LInux命令尤为重要
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_008.jpg)

```
[root@corehub-001 hadoop]# bin/hdfs dfs -mkdir -p /user/geekparkhub/input
19/01/25 14:41:14 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
```
```
[root@corehub-001 hadoop]# bin/hdfs dfs -ls -R /
19/01/25 14:44:20 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
drwxr-xr-x   - root supergroup          0 2019-01-25 14:41 /user
drwxr-xr-x   - root supergroup          0 2019-01-25 14:41 /user/geekparkhub
drwxr-xr-x   - root supergroup          0 2019-01-25 14:41 /user/geekparkhub/input
[root@corehub-001 hadoop]# 
```
##### 在hadoop目录下,将wcinput目录及元数据文件上传到/user/geekparkhub/input目录中
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_009.jpg)
```
[root@corehub-001 hadoop]# bin/hdfs dfs -put wcinput/wc.input /user/geekparkhub/input
19/01/25 15:02:56 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
[root@corehub-001 hadoop]#
```

##### 执行并读取HDFS程序
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_010.jpg)
```
[root@corehub-001 hadoop]# hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.2.jar wordcount /user/geekparkhub/input /user/geekparkhub/output
19/01/25 15:16:04 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
19/01/25 15:16:05 INFO Configuration.deprecation: session.id is deprecated. Instead, use dfs.metrics.session-id
19/01/25 15:16:05 INFO jvm.JvmMetrics: Initializing JVM Metrics with processName=JobTracker, sessionId=
19/01/25 15:16:05 INFO input.FileInputFormat: Total input paths to process : 1
19/01/25 15:16:08 INFO mapreduce.Job:  map 100% reduce 100%
19/01/25 15:16:08 INFO mapreduce.Job: Job job_local169102714_0001 completed successfully
19/01/25 15:16:08 INFO mapreduce.Job: Counters: 35
        File System Counters
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters 
                Bytes Read=471
        File Output Format Counters 
                Bytes Written=503
[root@corehub-001 hadoop]#
```

#### 启动YARN上运行MapReduce程序
> 分析 : 配置集群在Yarn上运行MR,启动测试集群增删查,在Yarn上执行Wordcount案例
##### 配置集群
###### 配置yarn-env.sh
`vim etc/hadoop/yarn-env.sh`
``` powershell
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# User for YARN daemons
export HADOOP_YARN_USER=${HADOOP_YARN_USER:-yarn}

# resolve links - $0 may be a softlink
export YARN_CONF_DIR="${YARN_CONF_DIR:-$HADOOP_YARN_HOME/conf}"

# some Java parameters
export JAVA_HOME=/opt/jdk1.8.0_162
if [ "$JAVA_HOME" != "" ]; then
  #echo "run java in $JAVA_HOME"
  JAVA_HOME=$JAVA_HOME
fi

if [ "$JAVA_HOME" = "" ]; then
  echo "Error: JAVA_HOME is not set."
  exit 1
fi

JAVA=$JAVA_HOME/bin/java
JAVA_HEAP_MAX=-Xmx1000m
```
###### 配置yarn-site.xml
> yarn-site.xml 官方文档说明 : [yarn-default.xml](http://hadoop.apache.org/docs/r2.7.2/hadoop-yarn/hadoop-yarn-common/yarn-default.xml)
```
[root@corehub-001 hadoop]# vim etc/hadoop/yarn-site.xml
```
``` xml
<?xml version="1.0"?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->
<configuration>
<!-- Site specific YARN configuration properties -->
<!-- Reducer获取数据方式 -->
    <property>
      <name>yarn.nodemanager.aux-services</name>
      <value>mapreduce_shuffle</value>
    </property>
<!-- 指定Yarn的ResourceManager地址-->
    <property>
      <name>yarn.resourcemanager.hostname</name>
      <value>corehub-001</value>
    </property>
</configuration>
```

###### 配置mapred-env.sh
`vim etc/hadoop/mapred-env.sh`
```
[root@corehub-001 hadoop]# vim etc/hadoop/mapred-env.sh
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

export JAVA_HOME=/opt/jdk1.8.0_162

export HADOOP_JOB_HISTORYSERVER_HEAPSIZE=1000

export HADOOP_MAPRED_ROOT_LOGGER=INFO,RFA

#export HADOOP_JOB_HISTORYSERVER_OPTS=
#export HADOOP_MAPRED_LOG_DIR="" # Where log files are stored.  $HADOOP_MAPRED_HOME/logs by default.
#export HADOOP_JHS_LOGGER=INFO,RFA # Hadoop JobSummary logger.
#export HADOOP_MAPRED_PID_DIR= # The pid files are stored. /tmp by default.
#export HADOOP_MAPRED_IDENT_STRING= #A string representing this instance of hadoop. $USER by default
#export HADOOP_MAPRED_NICENESS= #The scheduling priority for daemons. Defaults to 0.
```

###### 配置mapred-site.xml
> mapred-site.xml.template 重命名为mapred-site.xml
```
[root@corehub-001 hadoop]# mv etc/hadoop/mapred-site.xml.template etc/hadoop/mapred-site.xml
```
```
[root@corehub-001 hadoop]# vim etc/hadoop/mapred-site.xml
```
``` xml
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->
<!-- Put site-specific property overrides in this file. -->
<configuration>
<!-- 指定MR运行在Yarn上 -->
    <property>
      <name>mapreduce.framework.name</name>
      <value>yarn</value>
    </property>
</configuration>
```
##### 启动集群
> 启动前必须保证NameNode和DataNode已经启动
###### 启动ResourceManager
```
[root@corehub-001 hadoop]# sbin/yarn-daemon.sh start resourcemanager
starting resourcemanager, logging to /opt/module/hadoop/logs/yarn-root-resourcemanager-corehub-001.out
[root@corehub-001 hadoop]# jps
39653 ResourceManager
9353 DataNode
9066 NameNode
40171 Jps
[root@corehub-001 hadoop]# 
```
###### 启动NodeManager
```
[root@corehub-001 hadoop]# sbin/yarn-daemon.sh start nodemanager
starting nodemanager, logging to /opt/module/hadoop/logs/yarn-root-nodemanager-corehub-001.out
[root@corehub-001 hadoop]# jps
40880 Jps
40769 NodeManager
39653 ResourceManager
9353 DataNode
9066 NameNode
[root@corehub-001 hadoop]# 
```
###### 执行wordcount程序并查看运行结果
> 可通过hadoop提供website图形化界面 查看启动结果
> 
> 通过 LinuxHostName:8088端口号形式访问 或 通过 Linux IPaddr:8088端口号访问
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_011.jpg)
```
[root@corehub-001 hadoop]# hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.2.jar wordcount /user/geekparkhub/input /user/geekparkhub/output
^H19/01/27 19:37:36 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
19/01/27 19:37:37 INFO client.RMProxy: Connecting to ResourceManager at corehub-001/192.168.177.130:8032
19/01/27 19:37:38 INFO input.FileInputFormat: Total input paths to process : 1
19/01/27 19:37:38 INFO mapreduce.JobSubmitter: number of splits:1
19/01/27 19:37:38 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1548588180141_0001
19/01/27 19:37:39 INFO impl.YarnClientImpl: Submitted application application_1548588180141_0001
19/01/27 19:37:39 INFO mapreduce.Job: The url to track the job: http://corehub-001:8088/proxy/application_1548588180141_0001/
19/01/27 19:37:39 INFO mapreduce.Job: Running job: job_1548588180141_0001
19/01/27 19:37:53 INFO mapreduce.Job: Job job_1548588180141_0001 running in uber mode : false
19/01/27 19:37:53 INFO mapreduce.Job:  map 0% reduce 0%
19/01/27 19:38:01 INFO mapreduce.Job:  map 100% reduce 0%
19/01/27 19:38:08 INFO mapreduce.Job:  map 100% reduce 100%
19/01/27 19:38:08 INFO mapreduce.Job: Job job_1548588180141_0001 completed successfully
19/01/27 19:38:08 INFO mapreduce.Job: Counters: 49
        Job Counters 
                Launched map tasks=1
                Launched reduce tasks=1
                Data-local map tasks=1
                Total time spent by all maps in occupied slots (ms)=5298
                Total time spent by all reduces in occupied slots (ms)=4839
                Total time spent by all map tasks (ms)=5298
                Total time spent by all reduce tasks (ms)=4839
                Total vcore-milliseconds taken by all map tasks=5298
                Total vcore-milliseconds taken by all reduce tasks=4839
                Total megabyte-milliseconds taken by all map tasks=5425152
                Total megabyte-milliseconds taken by all reduce tasks=4955136
        Map-Reduce Framework
                Map input records=24
                Map output records=23
                Map output bytes=285
                Map output materialized bytes=262
                Input split bytes=120
                Combine input records=23
                Combine output records=18
                Reduce input groups=18
                Reduce shuffle bytes=262
                Reduce input records=18
                Reduce output records=18
                Spilled Records=36
                Shuffled Maps =1
                Failed Shuffles=0
                Merged Map outputs=1
                GC time elapsed (ms)=164
                CPU time spent (ms)=1830
                Physical memory (bytes) snapshot=416026624
                Virtual memory (bytes) snapshot=4163923968
                Total committed heap usage (bytes)=275775488
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters 
                Bytes Read=196
        File Output Format Counters 
                Bytes Written=184
```


#### 配置历史服务器
> 为了查看程序历史运行情况,需要配置一下历史服务器
##### 配置mapred-site.xml
```
[root@corehub-001 hadoop]# vim etc/hadoop/mapred-site.xml
```
``` xml
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->

<!-- Put site-specific property overrides in this file. -->

<configuration>
<!-- 指定MR运行在Yarn上 -->
    <property>
      <name>mapreduce.framework.name</name>
      <value>yarn</value>
    </property>
<!-- 历史服务器地址 -->
    <property>
       <name>mapreduce.jobhistory.address</name>
       <value>corehub-001:10020</value>
    </property>
<!-- 历史服务器WEB地址 -->
    <property>
       <name>mapreduce.jobhistory.webapp.address</name>
       <value>corehub-001:19888</value>
    </property>
</configuration>
```
##### 启动历史服务器并查看查看历史服务器是否启动以及JobHistory运行状态
```
[root@corehub-001 hadoop]# sbin/mr-jobhistory-daemon.sh start historyserver
starting historyserver, logging to /opt/module/hadoop/logs/mapred-root-historyserver-corehub-001.out
[root@corehub-001 hadoop]# jps
40769 NodeManager
66818 JobHistoryServer
39653 ResourceManager
66948 Jps
9353 DataNode
9066 NameNode
[root@corehub-001 hadoop]# 
```
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_012.jpg)



#### 配置日志聚集
> 日志聚集概念:应用运行完成以后,将程序运行日志信息上传到HDFS系统上.
> 日志聚集功能优势:可以方便查看程序运行详情,方便开发调试.
> 注意:开启日志聚集功能,需要**`重新启动NodeManager,ResourceManager,HistoryManager此三项服务`**.

##### 分别停止HistoryManager服务,NodeManager服务,ResourceManager服务

###### 停止HistoryManager服务
```
[root@corehub-001 hadoop]# sbin/mr-jobhistory-daemon.sh stop historyserver
stopping historyserver
[root@corehub-001 hadoop]# jps
40769 NodeManager
39653 ResourceManager
94488 Jps
9353 DataNode
9066 NameNode
[root@corehub-001 hadoop]# 
```
###### 停止NodeManager服务
```
[root@corehub-001 hadoop]# sbin/yarn-daemon.sh stop nodemanager
stopping nodemanager
[root@corehub-001 hadoop]# jps
39653 ResourceManager
9353 DataNode
9066 NameNode
96078 Jps
[root@corehub-001 hadoop]# 
```
###### 停止ResourceManager服务
```
[root@corehub-001 hadoop]# sbin/yarn-daemon.sh stop resourcemanager
stopping resourcemanager
[root@corehub-001 hadoop]# jps
98388 Jps
9353 DataNode
9066 NameNode
[root@corehub-001 hadoop]# 
```
##### 配置yarn-site.xml
```
[root@corehub-001 hadoop]# vim etc/hadoop/yarn-site.xml
```
```
<?xml version="1.0"?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->
<configuration>
<!-- Site specific YARN configuration properties -->
<!-- Reducer获取数据方式 -->
    <property>
      <name>yarn.nodemanager.aux-services</name>
      <value>mapreduce_shuffle</value>
    </property>
<!-- 指定Yarn的ResourceManager地址-->
    <property>
      <name>yarn.resourcemanager.hostname</name>
      <value>corehub-001</value>
    </property>
<!-- 日志聚集功能使用 -->
    <property>
      <name>yarn.log-aggregation-enable</name>
      <value>true</value>
    </property>
<!-- 日志保留时间设置为7天 根据开发情况,时间可自定义-->
<!-- 一天=3600秒 3600*24*7=604800 -->
    <property>
      <name>yarn.log-aggregation.retain-seconds</name>
      <value>604800</value>
    </property>
</configuration>
```
##### 分别开启HistoryManager服务,NodeManager服务,ResourceManager服务
###### 开启ResourceManager服务
```
[root@corehub-001 hadoop]# sbin/yarn-daemon.sh start resourcemanager
starting resourcemanager, logging to /opt/module/hadoop/logs/yarn-root-resourcemanager-corehub-001.out
[root@corehub-001 hadoop]# jps
113380 ResourceManager
113463 Jps
9353 DataNode
9066 NameNode
[root@corehub-001 hadoop]#
```
###### 开启NodeManager服务
```
[root@corehub-001 hadoop]# sbin/yarn-daemon.sh start nodemanager
starting nodemanager, logging to /opt/module/hadoop/logs/yarn-root-nodemanager-corehub-001.out
[root@corehub-001 hadoop]# jps
114081 NodeManager
113380 ResourceManager
9353 DataNode
9066 NameNode
114159 Jps
[root@corehub-001 hadoop]# 
```
###### 开启HistoryManager服务
```
[root@corehub-001 hadoop]# sbin/mr-jobhistory-daemon.sh start historyserver
starting historyserver, logging to /opt/module/hadoop/logs/mapred-root-historyserver-corehub-001.out
[root@corehub-001 hadoop]# jps
114081 NodeManager
115184 JobHistoryServer
113380 ResourceManager
9353 DataNode
9066 NameNode
115263 Jps
[root@corehub-001 hadoop]# 
```
##### 删除HDFS上已经存在的输出目录
```
[root@corehub-001 hadoop]# bin/hdfs dfs -rm -r /user/geekparkhub/output
19/01/27 22:26:57 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
19/01/27 22:26:58 INFO fs.TrashPolicyDefault: Namenode trash configuration: Deletion interval = 0 minutes, Emptier interval = 0 minutes.
Deleted /user/geekparkhub/output
[root@corehub-001 hadoop]# 
```
##### 执行WordCount程序
```
[root@corehub-001 hadoop]# hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.2.jar wordcount /user/geekparkhub/input /user/geekparkhub/output
19/01/27 22:32:29 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
19/01/27 22:32:30 INFO client.RMProxy: Connecting to ResourceManager at corehub-001/192.168.177.130:8032
19/01/27 22:32:33 INFO input.FileInputFormat: Total input paths to process : 1
19/01/27 22:32:33 INFO mapreduce.JobSubmitter: number of splits:1
19/01/27 22:32:34 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1548598949012_0001
19/01/27 22:32:35 INFO impl.YarnClientImpl: Submitted application application_1548598949012_0001
19/01/27 22:32:35 INFO mapreduce.Job: The url to track the job: http://corehub-001:8088/proxy/application_1548598949012_0001/
19/01/27 22:32:35 INFO mapreduce.Job: Running job: job_1548598949012_0001
19/01/27 22:33:14 INFO mapreduce.Job: Job job_1548598949012_0001 running in uber mode : false
19/01/27 22:33:14 INFO mapreduce.Job:  map 0% reduce 0%
19/01/27 22:33:23 INFO mapreduce.Job:  map 100% reduce 0%
19/01/27 22:33:32 INFO mapreduce.Job:  map 100% reduce 100%
19/01/27 22:33:33 INFO mapreduce.Job: Job job_1548598949012_0001 completed successfully
19/01/27 22:33:34 INFO mapreduce.Job: Counters: 49
        File System Counters
                FILE: Number of bytes read=262
                FILE: Number of bytes written=235459
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=316
                HDFS: Number of bytes written=184
                HDFS: Number of read operations=6
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
        Job Counters 
                Map-Reduce Framework
                Map input records=24
                Map output records=23
                Map output bytes=285
                Map output materialized bytes=262
                Input split bytes=120
                Combine input records=23
                Combine output records=18
                Reduce input groups=18
                Reduce shuffle bytes=262
                Reduce input records=18
                Reduce output records=18
                Spilled Records=36
                Shuffled Maps =1
                Failed Shuffles=0
                Merged Map outputs=1
                GC time elapsed (ms)=220
                CPU time spent (ms)=2130
                Physical memory (bytes) snapshot=399134720
                Virtual memory (bytes) snapshot=4166119424
                Total committed heap usage (bytes)=276824064
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters 
                Bytes Read=196
        File Output Format Counters 
                Bytes Written=184
```
##### 查看日志
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_013.jpg)

查看日志方式 也可以通过进入log文件夹进行查看
```
[root@corehub-001 hadoop]# ll
total 76
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 bin
drwxr-xr-x. 3 root  root   4096 Jan 27 18:47 data
drwxr-xr-x. 3 10011 10011  4096 Jan 26  2016 etc
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 include
drwxr-xr-x. 2 root  root   4096 Jan 24 22:28 input
drwxr-xr-x. 3 10011 10011  4096 Jan 26  2016 lib
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 libexec
-rw-r--r--. 1 10011 10011 15429 Jan 26  2016 LICENSE.txt
drwxr-xr-x. 3 root  root   4096 Jan 27 22:23 logs
-rw-r--r--. 1 10011 10011   101 Jan 26  2016 NOTICE.txt
drwxr-xr-x. 2 root  root   4096 Jan 24 22:43 output
-rw-r--r--. 1 10011 10011  1366 Jan 26  2016 README.txt
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 sbin
drwxr-xr-x. 4 10011 10011  4096 Jan 26  2016 share
drwxr-xr-x. 2 root  root   4096 Jan 24 23:48 wcinput
drwxr-xr-x. 2 root  root   4096 Jan 24 23:34 wcoutput
[root@corehub-001 hadoop]# ll logs/
total 472
-rw-r--r--. 1 root root  51669 Jan 27 22:36 hadoop-root-datanode-corehub-001.log
-rw-r--r--. 1 root root    715 Jan 27 18:48 hadoop-root-datanode-corehub-001.out
-rw-r--r--. 1 root root  59522 Jan 27 22:36 hadoop-root-namenode-corehub-001.log
-rw-r--r--. 1 root root   4960 Jan 27 18:55 hadoop-root-namenode-corehub-001.out
-rw-r--r--. 1 root root  53574 Jan 27 22:42 mapred-root-historyserver-corehub-001.log
-rw-r--r--. 1 root root   1484 Jan 27 22:24 mapred-root-historyserver-corehub-001.out
-rw-r--r--. 1 root root   1477 Jan 27 20:53 mapred-root-historyserver-corehub-001.out.1
-rw-r--r--. 1 root root      0 Jan 27 18:47 SecurityAuth-root.audit
drwxr-xr-x. 3 root root   4096 Jan 27 22:42 userlogs
-rw-r--r--. 1 root root 126215 Jan 27 22:33 yarn-root-nodemanager-corehub-001.log
-rw-r--r--. 1 root root   1515 Jan 27 22:23 yarn-root-nodemanager-corehub-001.out
-rw-r--r--. 1 root root   1508 Jan 27 19:24 yarn-root-nodemanager-corehub-001.out.1
-rw-r--r--. 1 root root 125846 Jan 27 22:38 yarn-root-resourcemanager-corehub-001.log
-rw-r--r--. 1 root root   1531 Jan 27 22:22 yarn-root-resourcemanager-corehub-001.out
-rw-r--r--. 1 root root   1524 Jan 27 19:23 yarn-root-resourcemanager-corehub-001.out.1
[root@corehub-001 hadoop]# 
```

#### 配置文件说明
> Hadoop 配置文件分为两类:默认配置文件和自定义配置文件,只有开发者想修改某一默认配置时,才需要修改自定义配置文件,更改相应属性值.
##### 1.默认配置文件
  

| 要获取的默认文件 | 文件存放在Hadoop的jar包中的位置 | 常用配置信息
| :-------- | --------:| --------:|
| [core-default.xml]    | hadoop-common-2.7.2.jar/core-default.xml | NameNode属性和端口号,数据存储路径 |
| [hdfs-default.xml]    | hadoop-hdfs-2.7.2.jar/hdfs-default.xml | 副本数 |
| [yarn-default.xml]    | hadoop-yarn-common-2.7.2.jar/yarn-default.xml | ResourceManager&NodeManager属性 |
| [mapred-default.xml]    | hadoop-mapred-client-core-2.7.2.jar/mapred-default.xml | 在Yarn运行程序,默认是在本机运行 |

##### 2.自定义配置文
> 四个配置文件存放在**`$HADOOP_HOME/etc/hadoop`**路径中,开发者可以根据项目需求重新进行修改配置
> 
> **`core-site.xml`** | **`hdfs-site.xml`**
> **`yarn-site.xml`** | **`mapred-site.xml`**


###  🎉🎉 完全分布式 运行模式 (开发重点) 🎉🎉
> 分析:准备三台服务器 (关闭防火墙,设置静态IP地址,主机名称)
> 安装JavaJDK | 配置Java环境变量
> 安装Hadoop | 配置hadoop环境变量
> 配置集群 | 单点启动
> 配置SSH | 群起并测试集群

#### 虚拟机准备
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_005.jpg)

##### scp(secure copy)安全拷贝
> 1.scp定义
> scp可以实现服务器与服务器之间的数据拷贝,(from server1 to server2)
> 
> 2.scp基本语法
> **`scp     -r      $pdir/$fname`**            **`$user@corehub$host:$pdir/$fname`**
> 指令    递归    源数据文件路径/名称                   目的用户名@主机名称:目的路径/名称
> 
> 3.scp实操案例
> 在corehub-001上,将corehub-001中的/opt/module目录下的软件拷贝到corehub-002上
```
[root@corehub-001 ~]# cd /opt/
[root@corehub-001 opt]# ll
total 408824
-rwxrw-rw-.  1 root root   9621331 Jan 13 17:36 apache-tomcat-8.5.33.tar.gz
drwxr-xr-x.  8 uucp  143      4096 Dec 19  2017 jdk1.8.0_162
-rwxrw-rw-.  1 root root 189815615 Jan 13 18:22 jdk-8u162-linux-x64.tar.gz
drwxr-xr-x.  3 root root      4096 Jan 25 09:23 module
drwxr-xr-x. 13 root root      4096 Jan 13 23:07 mysql
-rwxrw-rw-.  1 root root 184122460 Jan 13 18:21 mysql-5.5.35-linux2.6-x86_64.tar.gz
drwxr-xr-x.  2 root root      4096 Nov 22  2013 rh
drwxr-xr-x.  2 root root      4096 Jan 25 09:20 software
drwxr-xr-x.  9 root root      4096 Jan 13 23:06 tomcat
drwxr-xr-x. 11 1001 1001      4096 Jan 17 22:48 zookeeper
-rw-r--r--.  1 root root  35042811 Jan 17 17:11 zookeeper-3.4.10.tar.gz
[root@corehub-001 opt]# scp -r module/ root@corehub-002:/opt/module/
The authenticity of host 'corehub-002 (192.168.152.135)' can't be established.
RSA key fingerprint is 63:9d:81:a7:3d:83:7f:04:19:32:8f:c8:97:9d:07:d8.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'corehub-002,192.168.152.135' (RSA) to the list of known hosts.
root@corehub-002's password:
hdfs-config.sh                                                                      100% 1427     1.4KB/s   00:00    
mapred-config.sh                                                                    100% 2223     2.2KB/s   00:00    
httpfs-config.sh                                                                    100% 5749     5.6KB/s   00:00    
mapred-config.cmd                                                                   100% 1640     1.6KB/s   00:00    
yarn-config.cmd                                                                     100% 2131     2.1KB/s   00:00    
kms-config.sh                                                                       100% 5431     5.3KB/s   00:00    
yarn-config.sh                                                                      100% 2134     2.1KB/s   00:00    
hadoop-config.cmd                                                                   100% 8270     8.1KB/s   00:00    
[root@corehub-001 opt]#
```
> 数据已从corehub-001服务器同步推送到corehub-002服务器
```
[root@corehub-002 ~]# cd /opt/
[root@corehub-002 opt]# ll
total 408824
-rwxrw-rw-.  1 root root   9621331 Jan 13 17:36 apache-tomcat-8.5.33.tar.gz
drwxr-xr-x.  8 uucp  143      4096 Dec 19  2017 jdk1.8.0_162
-rwxrw-rw-.  1 root root 189815615 Jan 13 18:22 jdk-8u162-linux-x64.tar.gz
drwxr-xr-x.  4 root root      4096 Jan 29 06:08 module
drwxr-xr-x. 13 root root      4096 Jan 13 23:07 mysql
-rwxrw-rw-.  1 root root 184122460 Jan 13 18:21 mysql-5.5.35-linux2.6-x86_64.tar.gz
drwxr-xr-x.  2 root root      4096 Nov 22  2013 rh
drwxr-xr-x.  2 root root      4096 Jan 25 10:20 software
drwxr-xr-x.  9 root root      4096 Jan 13 23:06 tomcat
drwxr-xr-x. 11 1001 1001      4096 Jan 19 18:51 zookeeper
-rw-r--r--.  1 root root  35042811 Jan 17 17:11 zookeeper-3.4.10.tar.gz
[root@corehub-002 opt]# cd module/
[root@corehub-002 module]# ll
total 4
drwxr-xr-x. 15 root root 4096 Jan 29 06:09 hadoop
[root@corehub-002 module]# 
```

> 在corehub-003服务器上,拉取corehub-001服务器上数据
```
[root@corehub-003 ~]# scp -r root@corehub-001:/opt/module /opt
root@corehub-001's password: 
hadoop-policy.xml                                                                   100% 9683     9.5KB/s   00:00    
yarn-site.xml                                                                       100%  690     0.7KB/s   00:00    
hdfs-site.xml                                                                       100%  775     0.8KB/s   00:00    
core-site.xml                                                                       100%  774     0.8KB/s   00:00    
httpfs-site.xml                                                                     100%  620     0.6KB/s   00:00    
capacity-scheduler.xml
mapred-config.cmd                                                                   100% 1640     1.6KB/s   00:00    
yarn-config.cmd                                                                     100% 2131     2.1KB/s   00:00    
kms-config.sh                                                                       100% 5431     5.3KB/s   00:00    
yarn-config.sh                                                                      100% 2134     2.1KB/s   00:00    
hadoop-config.cmd                                                                   100% 8270     8.1KB/s   00:00    
[root@corehub-003 ~]# 
```
> 4. 将corehub-001配置文件分发推送到corehub-002,corehub-003服务器上,推送完毕后更新配置即可生效
```
[root@corehub-001 ~]# scp -r /etc/profile root@corehub-002:/etc/profile
root@corehub-002's password: 
profile                                                                             100% 2073     2.0KB/s   00:00    
[root@corehub-001 ~]# 
```
```
[root@corehub-001 ~]# scp -r /etc/profile root@corehub-003:/etc/profile
The authenticity of host 'corehub-003 (192.168.152.136)' can't be established.
RSA key fingerprint is 63:9d:81:a7:3d:83:7f:04:19:32:8f:c8:97:9d:07:d8.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'corehub-003,192.168.152.136' (RSA) to the list of known hosts.
root@corehub-003's password: 
profile                                                                             100% 2073     2.0KB/s   00:00    
[root@corehub-001 ~]# 
```
```
source /etc/profile
```

##### rsync 远程同步工具
> rsync主要用于备份和镜像,具有速度快,避免复制相同内容和支持符号链接的优点.
> rsync与scp区别:用rsync做文件的复制要比scp速度快,rsync只对差异文件做更新,scp是把所有文件复制的过程.
> 


基本语法
**`rsync -rVl $pdir$fname $user@corehub$host:$pdir/$fname`**
指令    选项参数 源文件路径/名称  目的用户名@主机名称:目的路径/名称

| 选项      |     功能 |
| :-------- | --------:|
| -r    |   递归 |
| -v    |   显示复制过程 |
| -l    |   拷贝符号连接 |

rsync实操案例
> 将corehub-001服务器上的/opt/software目录同步到corehub-002服务器的root用户目录下
```
[root@corehub-001 ~]# rsync -rvl /opt/software/ root@corehub-002:/opt/software/
root@corehub-002's password: 
sending incremental file list
created directory /opt/software
./
hadoop-2.7.2.tar.gz
sent 212072761 bytes  received 34 bytes  12852896.67 bytes/sec
total size is 212046774  speedup is 1.00
[root@corehub-001 ~]# 
```

#### 编写集群分发脚本xsync
> 需求:循环复制文件到所有节点的相同目录下

需求分析:
rsync指令 原始拷贝
rsync -rvl /opt/module root@corehub-002:/opt/
期望脚本:将sxync要要同步的文件名称
说明:在/home/geek-developer/bin/此目录下存放脚本,geek-developer用户可以在系统任何地方直接执行

脚本实现
> 创建bin目录 mkdir bin
> ```
> [root@corehub-001 ~]# mkdir bin
> [root@corehub-001 ~]# ll
> total 100
> -rw-------. 1 root root  3362 Jan 18 04:54 anaconda-ks.cfg
> drwxr-xr-x. 2 root root  4096 Jan 30 18:00 bin
> drwxr-xr-x. 2 root root  4096 Jan 24 19:40 Desktop
> drwxr-xr-x. 2 root root  4096 Jan 18 05:51 Documents
> drwxr-xr-x. 2 root root  4096 Jan 18 05:51 Downloads
> -rw-r--r--. 1 root root 41364 Jan 18 04:54 install.log
> -rw-r--r--. 1 root root  9154 Jan 18 04:52 install.log.syslog
> drwxr-xr-x. 2 root root  4096 Jan 18 05:51 Music
> drwxr-xr-x. 2 root root  4096 Jan 18 05:51 Pictures
> drwxr-xr-x. 2 root root  4096 Jan 18 05:51 Public
> drwxr-xr-x. 2 root root  4096 Jan 18 05:51 Templates
> drwxr-xr-x. 2 root root  4096 Jan 18 05:51 Videos
> [root@corehub-001 ~]#
> ```

> 进入bin目录 cd bin/
> ```
> [root@corehub-001 ~]# cd bin/
> [root@corehub-001 bin]# ll
> total 0
> [root@corehub-001 bin]# 
> ```

> 创建xsync文件 touch xsync
> ```
> [root@corehub-001 bin]# touch xsync
> [root@corehub-001 bin]# ll
> total 0
> -rw-r--r--. 1 root root 0 Jan 30 18:05 xsync
> [root@corehub-001 bin]# 
> ```

> 编辑xsync vim xsync
> ```
> #!/bin/bash
> # 1.获取输入参数个数,如果没有参数,直接退出
> pcount=$#
> if((pcount==0)); then
> echo no args;
> exit
> fi
> 
> # 2.获取文件名称
> p1=$1
> fname=`basename $p1`
> echo fname=$fname
> 
> # 3.获取上级目录到据对路径
> pdri=`cd -P $(dirname $p1); pwd`
> echo pdir=$pdri
> 
> # 4.获取当前用户名称
> user=`whoami`
> 
> # 5.循环遍历
> for((host=103;host<105;host++)); do
> echo -------corehub$host-------
> rsync -rvl $pdir/$fname $user@corehub$host:$pdri
> done
> ```





#### 集群配置
1.集群部署规划

| linux服务器 | corehub-001 | corehub-002 | corehub-003 |
| :-------- | --------:| :------: | :------: |
| HDFS    | NameNode,DataNode | DataNode | SecondaryNameNode,DataNode |
| YARN    | NodeManager |  ResourceManager,NodeManager  | NodeManager |


2.配置集群
配置core-site.xml
```
[root@corehub-001 hadoop]# vim etc/hadoop/core-site.xml
```
在该文件中编写如下配置
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->
<!-- Put site-specific property overrides in this file. -->
<configuration>
<!-- 指定HDFS中的NameNode地址 -->
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://corehub-001:9000</value>
  </property>
<!-- 指定Hadoop运行时产生文件的存储目录 -->
   <property>
     <name>hadoop.tmp.dir</name>
     <value>/opt/module/hadoop/data/tmp</value>
   </property>
</configuration>
```
HDFS配置文件
配置hadoop-env.sh
```
[root@corehub-001 hadoop]# vim etc/hadoop/hadoop-env.sh
```
``` bash
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

# Set Hadoop-specific environment variables here.

# The only required environment variable is JAVA_HOME.  All others are
# optional.  When running a distributed configuration it is best to
# set JAVA_HOME in this file, so that it is correctly defined on
# remote nodes.
# The java implementation to use.
export JAVA_HOME=/opt/devtool/jdk1.8.0_162
```
配置hdfs-site.xml
```
[root@corehub-001 hadoop]# vim etc/hadoop/hdfs-site.xml
```
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->
<!-- Put site-specific property overrides in this file. -->
<configuration>
<!-- 指定HDFS副本数量 -->
  <property>
   <name>dfs.replication</name>
     <value>3</value>
  </property>
  <!-- 指定Hadoop辅助名称节点主机配置 -->
  <property>
   <name>dfs.namenode.secondary.http-address</name>
     <value>corehub-003:50090</value>
  </property>
</configuration>
```
YARN配置文件
配置yarn-env.sh
```
[root@corehub-001 hadoop]# vim etc/hadoop/yarn-env.sh
```
```
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# User for YARN daemons
export HADOOP_YARN_USER=${HADOOP_YARN_USER:-yarn}

# resolve links - $0 may be a softlink
export YARN_CONF_DIR="${YARN_CONF_DIR:-$HADOOP_YARN_HOME/conf}"

# some Java parameters
export JAVA_HOME=/opt/devtool/jdk1.8.0_162
```
配置yarn-site.xml
在该文件中编写如下配置
``` xml
<?xml version="1.0"?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->
<configuration>
<!-- Site specific YARN configuration properties -->
<!-- Reducer获取数据方式 -->
    <property>
      <name>yarn.nodemanager.aux-services</name>
      <value>mapreduce_shuffle</value>
    </property>
<!-- 指定Yarn的ResourceManager地址-->
    <property>
      <name>yarn.resourcemanager.hostname</name>
      <value>corehub-002</value>
    </property>
</configuration>
```

MapReduce配置文件
配置mapred-env.sh
```
[root@corehub-001 hadoop]# vim etc/hadoop/mapred-env.sh
```

```
[root@corehub-001 hadoop]# vim etc/hadoop/yarn-site.xml
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
export JAVA_HOME=/opt/devtool/jdk1.8.0_16
```
配置mapred-site.xml
在该文件中编写如下配置
```
[root@corehub-001 hadoop]# vim etc/hadoop/mapred-site.xml
```
``` xml
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->
<!-- Put site-specific property overrides in this file. -->
<configuration>
<!-- 指定MR运行在Yarn上 -->
    <property>
      <name>mapreduce.framework.name</name>
      <value>yarn</value>
    </property>
</configuration>
```
分别删除001,002,003号服务器上的 log,data文件
删除前提,先保证没有jps在运行中,否则会导致悲剧发生
删除001号服务器
```
[root@corehub-001 hadoop]# rm -rf data/ logs/
[root@corehub-001 hadoop]# ll
total 68
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 bin
drwxr-xr-x. 3 10011 10011  4096 Jan 26  2016 etc
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 include
drwxr-xr-x. 2 root  root   4096 Jan 24 22:28 input
drwxr-xr-x. 3 10011 10011  4096 Jan 26  2016 lib
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 libexec
-rw-r--r--. 1 10011 10011 15429 Jan 26  2016 LICENSE.txt
-rw-r--r--. 1 10011 10011   101 Jan 26  2016 NOTICE.txt
drwxr-xr-x. 2 root  root   4096 Jan 24 22:43 output
-rw-r--r--. 1 10011 10011  1366 Jan 26  2016 README.txt
drwxr-xr-x. 2 10011 10011  4096 Jan 26  2016 sbin
drwxr-xr-x. 4 10011 10011  4096 Jan 26  2016 share
drwxr-xr-x. 2 root  root   4096 Jan 24 23:48 wcinput
drwxr-xr-x. 2 root  root   4096 Jan 24 23:34 wcoutput
[root@corehub-001 hadoop]#
```
删除002号服务器
```
[root@corehub-002 hadoop]# rm -rf data/ logs/
[root@corehub-002 hadoop]# ll
total 68
drwxr-xr-x. 2 root root  4096 Jan 31 13:34 bin
drwxr-xr-x. 3 root root  4096 Jan 31 13:33 etc
drwxr-xr-x. 2 root root  4096 Jan 31 13:34 include
drwxr-xr-x. 2 root root  4096 Jan 31 13:34 input
drwxr-xr-x. 3 root root  4096 Jan 31 13:34 lib
drwxr-xr-x. 2 root root  4096 Jan 31 13:33 libexec
-rw-r--r--. 1 root root 15429 Jan 31 13:33 LICENSE.txt
-rw-r--r--. 1 root root   101 Jan 31 13:34 NOTICE.txt
drwxr-xr-x. 2 root root  4096 Jan 31 13:34 output
-rw-r--r--. 1 root root  1366 Jan 31 13:33 README.txt
drwxr-xr-x. 2 root root  4096 Jan 31 13:33 sbin
drwxr-xr-x. 4 root root  4096 Jan 31 13:34 share
drwxr-xr-x. 2 root root  4096 Jan 31 13:34 wcinput
drwxr-xr-x. 2 root root  4096 Jan 31 13:34 wcoutput
[root@corehub-002 hadoop]# 

```
删除003号服务器
```
[root@corehub-003 hadoop]# rm -rf data/ logs/
[root@corehub-003 hadoop]# ll
total 68
drwxr-xr-x. 2 root root  4096 Jan 31 13:37 bin
drwxr-xr-x. 3 root root  4096 Jan 31 13:37 etc
drwxr-xr-x. 2 root root  4096 Jan 31 13:37 include
drwxr-xr-x. 2 root root  4096 Jan 31 13:37 input
drwxr-xr-x. 3 root root  4096 Jan 31 13:37 lib
drwxr-xr-x. 2 root root  4096 Jan 31 13:37 libexec
-rw-r--r--. 1 root root 15429 Jan 31 13:37 LICENSE.txt
-rw-r--r--. 1 root root   101 Jan 31 13:37 NOTICE.txt
drwxr-xr-x. 2 root root  4096 Jan 31 13:37 output
-rw-r--r--. 1 root root  1366 Jan 31 13:37 README.txt
drwxr-xr-x. 2 root root  4096 Jan 31 13:37 sbin
drwxr-xr-x. 4 root root  4096 Jan 31 13:37 share
drwxr-xr-x. 2 root root  4096 Jan 31 13:37 wcinput
drwxr-xr-x. 2 root root  4096 Jan 31 13:37 wcoutput
[root@corehub-003 hadoop]# 
```
最后 格式化 001服务器数据
```
[root@corehub-001 hadoop]# bin/hdfs namenode -format
/************************************************************
STARTUP_MSG: Starting NameNode
STARTUP_MSG:   host = corehub-001/192.168.177.130
STARTUP_MSG:   args = [-format]
STARTUP_MSG:   version = 2.7.2
STARTUP_MSG:   classpath = /opt/module/hadoop/etc/hadoop:/opt/module/hadoop/share/hadoop/common/lib/jersey-server-1.9.jar:/opt/module/hadoop/share/hadoop/common/lib/servlet-api-2.5.jar:/opt/module/hadoop/share/hadoop/common/lib/commons-lang-2.6.jar:/opt/module/hadoop/share/hadoop/common/lib/commons-math3-3.1.1.jar:/opt/module/hadoop/share/hadoop/common/lib/java-xmlbuilder-0.4.jar:/opt/module/hadoop/share/hadoop/common/lib/xmlenc-0.52.jar:/opt/module/hadoop/share/hadoop/common/lib/commons-compress-1.4.1.jar:/opt/module/hadoop/share/hadoop/common/lib/jackson-mapper-asl-1.9.13.jar
19/01/31 13:49:10 INFO common.Storage: Storage directory /opt/module/hadoop/data/tmp/dfs/name has been successfully formatted.
19/01/31 13:49:10 INFO namenode.NNStorageRetentionManager: Going to retain 1 images with txid >= 0
19/01/31 13:49:10 INFO util.ExitUtil: Exiting with status 0
19/01/31 13:49:10 INFO namenode.NameNode: SHUTDOWN_MSG: 
/************************************************************
SHUTDOWN_MSG: Shutting down NameNode at corehub-001/192.168.177.130
************************************************************/
```



#### 集群单点启动
启动001号服务
```
[root@corehub-001 hadoop]# sbin/hadoop-daemon.sh start namenode
starting namenode, logging to /opt/module/hadoop/logs/hadoop-root-namenode-corehub-001.out
[root@corehub-001 hadoop]# jps
94401 NameNode
94539 Jps
[root@corehub-001 hadoop]# sbin/hadoop-daemon.sh start datanode
starting datanode, logging to /opt/module/hadoop/logs/hadoop-root-datanode-corehub-001.out
[root@corehub-001 hadoop]# jps
94401 NameNode
94789 DataNode
95017 Jps
[root@corehub-001 hadoop]# 
```
启动002号服务
```
[root@corehub-002 hadoop]# sbin/hadoop-daemon.sh start datanode
starting datanode, logging to /opt/module/hadoop/logs/hadoop-root-datanode-corehub-002.out
[root@corehub-002 hadoop]# jps
63289 DataNode
63405 Jps
[root@corehub-002 hadoop]# 
```
启动003号服务
```
[root@corehub-003 hadoop]# sbin/hadoop-daemon.sh start datanode
starting datanode, logging to /opt/module/hadoop/logs/hadoop-root-datanode-corehub-003.out
[root@corehub-003 hadoop]# jps
67184 DataNode
67332 Jps
[root@corehub-003 hadoop]# 
```

#### SSH无密码配置
SSH有密码演示
```
[root@corehub-001 ~]# ssh corehub-002
root@corehub-002's password: 
Last login: Thu Jan 31 14:22:32 2019 from 192.168.177.2
[root@corehub-002 ~]# hostname
corehub-002
[root@corehub-002 ~]# exit
logout
Connection to corehub-002 closed.
[root@corehub-001 ~]# 
```
免登录原理
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_014.jpg)

ls -al指令 grep指令查找到.ssh文件
```
[root@corehub-001 ~]# ls -al | grep .ssh
drwx------.  2 root root  4096 Jan 31 13:24 .ssh
[root@corehub-001 ~]# 
```
cd进入.ssh目录,创建公钥私钥,输入指令后连续输入三次回车即可完成创建
``` bash
[root@corehub-001 .ssh]# ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
42:52:6e:8d:a2:3b:55:fb:d8:bf:dd:d1:de:d4:c3:21 root@corehub-001
The key's randomart image is:
+--[ RSA 2048]----+
|      .          |
|     o o         |
|    o * .        |
|   . * .         |
|  . . o S    E . |
|   o   =      o.o|
|  o   . o     .o+|
|   .     . . . +o|
|          o.. . o|
+-----------------+
[root@corehub-001 .ssh]# ll
total 12
-rw-------. 1 root root 1675 Jan 31 14:42 id_rsa
-rw-r--r--. 1 root root  398 Jan 31 14:42 id_rsa.pub
-rw-r--r--. 1 root root  409 Jan 31 13:24 known_hosts
[root@corehub-001 .ssh]# 
```
将001号服务器公钥拷贝到自身服务器
```
[root@corehub-001 ~]# ssh corehub-001
The authenticity of host 'corehub-001 (192.168.177.130)' can't be established.
RSA key fingerprint is 99:b3:c1:16:af:d9:de:79:5f:cf:53:25:63:f1:30:1d.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'corehub-001,192.168.177.130' (RSA) to the list of known hosts.
root@corehub-001's password: 
Last login: Thu Jan 31 14:22:12 2019 from 192.168.177.2
[root@corehub-001 ~]# 
```
将001号服务器公钥拷贝到002服务器
```
[root@corehub-001 .ssh]# ssh-copy-id corehub-002
root@corehub-002's password: 
Now try logging into the machine, with "ssh 'corehub-002'", and check in:
  .ssh/authorized_keys
to make sure we haven't added extra keys that you weren't expecting.
[root@corehub-001 .ssh]# 
```
将001号服务器公钥拷贝到003服务器
```
[root@corehub-001 .ssh]# ssh-copy-id corehub-003
The authenticity of host 'corehub-003 (192.168.177.132)' can't be established.
RSA key fingerprint is 99:b3:c1:16:af:d9:de:79:5f:cf:53:25:63:f1:30:1d.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'corehub-003,192.168.177.132' (RSA) to the list of known hosts.
root@corehub-003's password: 
Now try logging into the machine, with "ssh 'corehub-003'", and check in:
  .ssh/authorized_keys
to make sure we haven't added extra keys that you weren't expecting.
[root@corehub-001 .ssh]# 
```
拷贝完毕,测试是否可以免登录
免登录002服务器
```
[root@corehub-001 ~]# ssh corehub-002
Last login: Thu Jan 31 14:22:33 2019 from corehub-001
[root@corehub-002 ~]# exit
logout
Connection to corehub-002 closed.
[root@corehub-001 ~]# 
```
免登录003服务器
```
[root@corehub-001 ~]# ssh corehub-003
Last login: Thu Jan 31 14:22:32 2019 from 192.168.177.2
[root@corehub-003 ~]# exit
logout
Connection to corehub-003 closed.
[root@corehub-001 ~]# 
```
ssh文件功能说明
**`Known hosts`**:记录ssh访问过计算机公钥(public key)
**`id rsa`**:生成的私钥
**`id_rsa.pub`**:生成的公钥
**`authorized_keys`**:存放授权过得无密码登录服务器公钥

#### 群起集群
1.配置slaves
```
[root@corehub-001 hadoop]# vim etc/hadoop/slaves
```
在该文件中添加一下内容
注意:该文件添加的内容结尾不允许有空格,文件中部允许有空格
```
corehub-001
corehub-002
corehub-003
```
测试群起
```
[root@corehub-001 hadoop]# sbin/start-dfs.sh
Starting namenodes on [corehub-001]
root@corehub-001's password: 
corehub-001: namenode running as process 39894. Stop it first.
root@corehub-001's password: corehub-002: datanode running as process 9007. Stop it first.
corehub-003: datanode running as process 12654. Stop it first.
root@corehub-001's password: corehub-001: Permission denied, please try again.
corehub-001: Permission denied, please try again.
root@corehub-001's password: 
corehub-001: Permission denied (publickey,gssapi-keyex,gssapi-with-mic,password).
Starting secondary namenodes [corehub-003]
corehub-003: secondarynamenode running as process 18212. Stop it first.
```
对照 集群部署规划 查看001号进程 是否正常启动
```
[root@corehub-001 hadoop]# jps
39894 NameNode
47978 Jps
46235 DataNode
[root@corehub-001 hadoop]#
```
对照 集群部署规划 查看002号进程 是否正常启动
```
[root@corehub-002 hadoop]# jps
19375 Jps
9007 DataNode
[root@corehub-002 hadoop]# 
```
对照 集群部署规划 查看003号进程 是否正常启动
```
[root@corehub-003 hadoop]# jps
18212 SecondaryNameNode
23335 Jps
12654 DataNode
[root@corehub-003 hadoop]# 
```
在002服务器启动YARN ResourceManager
```
[root@corehub-002 hadoop]# sbin/start-yarn.sh
starting yarn daemons
starting resourcemanager, logging to /opt/module/hadoop/logs/yarn-root-resourcemanager-corehub-002.out
corehub-001: starting nodemanager, logging to /opt/module/hadoop/logs/yarn-root-nodemanager-corehub-001.out
corehub-003: starting nodemanager, logging to /opt/module/hadoop/logs/yarn-root-nodemanager-corehub-003.out
corehub-002: starting nodemanager, logging to /opt/module/hadoop/logs/yarn-root-nodemanager-corehub-002.out
[root@corehub-002 hadoop]# jps
22144 Jps
22052 NodeManager
9007 DataNode
21935 ResourceManager
[root@corehub-002 hadoop]# 
```
3.集群基本测试
a.上传文件到集群
上传小文件
```
[root@corehub-001 hadoop]# bin/hdfs dfs -mkdir -p /user/geekparkhub/input
```
```
[root@corehub-001 hadoop]# bin/hdfs dfs -put wcinput/wc.input /user/geekparkhub/input
```
上传大文件
```
[root@corehub-001 hadoop]# bin/hdfs dfs -put /opt/software/hadoop-2.7.2.tar.gz /user/geekparkhub/input
```

b.上传文件查看文件存放位置
查看HDFS文件存储路径
```
[root@corehub-001 subdir0]# pwd
/opt/module/hadoop/data/tmp/dfs/data/current/BP-1162876294-192.168.177.130-1548913750188/current/finalized/subdir0/subdir0
[root@corehub-001 subdir0]# ll
total 405008
-rw-r--r--. 1 root root       196 Jan 31 16:16 blk_1073741827
-rw-r--r--. 1 root root        11 Jan 31 16:16 blk_1073741827_1003.meta
-rw-r--r--. 1 root root 134217728 Jan 31 16:21 blk_1073741830
-rw-r--r--. 1 root root   1048583 Jan 31 16:21 blk_1073741830_1006.meta
-rw-r--r--. 1 root root  77829046 Jan 31 16:22 blk_1073741831
-rw-r--r--. 1 root root    608047 Jan 31 16:22 blk_1073741831_1007.meta
-rw-r--r--. 1 root root   9621331 Jan 31 16:31 blk_1073741832
-rw-r--r--. 1 root root     75175 Jan 31 16:31 blk_1073741832_1008.meta
-rw-r--r--. 1 root root 134217728 Jan 31 16:32 blk_1073741833
-rw-r--r--. 1 root root   1048583 Jan 31 16:32 blk_1073741833_1009.meta
-rw-r--r--. 1 root root  55597887 Jan 31 16:32 blk_1073741834
-rw-r--r--. 1 root root    434367 Jan 31 16:32 blk_1073741834_1010.meta
[root@corehub-001 subdir0]# 
```

#### 集群启动/关闭方式总结
1.各个服务组件逐一启动和关闭
分别启动/关闭 HDFS组件
`hadoop-daemon.sh start/stop namenode/datanode/secondarynamenode`
启动/关闭 YARN
`yarn-daemon.sh start/stop resourcemanager/nodemanager`

2.各个模块分开启动和关闭(前提是配置好ssh免登录)常用
1.整体启动关闭YARN
`start-dfs.sh / stop-dfs.sh`
2.整体启动关闭YARN
`start-yarn.sh / stop-yarn.sh`


#### 集群时间同步
> 时间同步方式:找一台机器作为时间服务器,所有机器与这台集群时间进行定时的同步,比如每隔十分钟,同步一次时间

配置时间同步实现步骤
1.时间服务配置(必须是root用户)
检查ntp是否安装
```
[root@corehub-002 ~]# rpm -qa|grep ntp
fontpackages-filesystem-1.41-1.1.el6.noarch
ntpdate-4.2.6p5-15.el6.centos.x86_64
ntp-4.2.6p5-15.el6.centos.x86_64
[root@corehub-002 ~]# 
```
修改ntp配置文件
`vim /etc/ntp.conf`
修改内容如下:
修改 (授权`192.168.177.2`-`192.168.177.255`网段上所有的机器可以从这台机器上查询和同步时间)
``` bash
[root@corehub-002 ~]# vim /etc/ntp.conf
# For more information about this file, see the man pages
# ntp.conf(5), ntp_acc(5), ntp_auth(5), ntp_clock(5), ntp_misc(5), ntp_mon(5).

driftfile /var/lib/ntp/drift

# Permit time synchronization with our time source, but do not
# permit the source to query or modify the service on this system.
restrict default kod nomodify notrap nopeer noquery
restrict -6 default kod nomodify notrap nopeer noquery

# Permit all access over the loopback interface.  This could
# be tightened as well, but to do so would effect some of
# the administrative functions.
restrict 127.0.0.1
restrict -6 ::1

# Hosts on local network are less restricted.
restrict 192.168.1.0 mask 255.255.255.0 nomodify notrap
```

修改(集群在局域网中,不使用其他互联网上的时间)
```
# Use public servers from the pool.ntp.org project.
# Please consider joining the pool (http://www.pool.ntp.org/join.html).
# server 0.centos.pool.ntp.org iburst
# server 1.centos.pool.ntp.org iburst
# server 2.centos.pool.ntp.org iburst
# server 3.centos.pool.ntp.org iburst
```
添加(当该节点丢失网络连接,依然可以采用本地时间作为时间服务器为集群中的其他节点提供时间同步)
```
# 当该节点丢失网络连接,依然可以采用本地时间作为时间服务器为集群中的其他节点提供时间同步
server 127.127.1.0
fudge 127.127.1.0 stratum 10
```
修改/etc/sysconfig/ntpd文件
让硬件与系统时间同步
`vim /etc/sysconfig/ntpd`
```
SYNC_HWCLOCK=yes
```
重新启动ntpd服务
```
[root@corehub-002 geek-developer]# service ntpd start
Starting ntpd:                                             [  OK  ]
[root@corehub-002 geek-developer]# service ntpd status
ntpd (pid  2871) is running...
[root@corehub-002 geek-developer]# 
```
设置ntpd服务开机自启
```
[root@corehub-002 geek-developer]# chkconfig ntpd on
[root@corehub-002 geek-developer]# 
```
其他机器配置(必须root用户)
在其他机器配置10分钟与时间服务器同步一次
初步测试
```
[root@corehub-001 ~]# date -s "2018-11-11 11:11:11"
Sun Nov 11 11:11:11 CST 2018
[root@corehub-001 ~]# date
Sun Nov 11 11:11:12 CST 2018
[root@corehub-001 ~]# /usr/sbin/ntpdate corehub-002
 3 Feb 12:58:56 ntpdate[6473]: step time server 192.168.177.131 offset 7264060.505383 sec
[root@corehub-001 ~]# date
Sun Feb  3 12:59:43 CST 2019
[root@corehub-001 ~]# 
```

编写定时任务如下:
```
[root@corehub-003 hadoop]# crontab -e
```
```
*/1 * * * * /usr/sbin/ntpdate corehub-002
~                                                                               
~                                                                      
~                                                                               
"/tmp/crontab.phnH6Y" 1L, 42C
```

修改任意机器时间
date -s "2019-7-12 41:55:23"
一分钟后查看机器是否与时间度服务器同步
```
[root@corehub-003 ~]# date -s "2018-11-11 11:11:11"
[root@corehub-003 ~]# date
Sun Nov 11 11:11:12 CST 2018
[root@corehub-003 ~]# date
Sun Feb  3 13:04:23 CST 2019
```

## 6. Hadoop 编译源码
### 前期准备工作
#### 1.centos联网
配置centos能够连接外网,linux虚拟机 测试 `ping www.baidu.com` 是否畅通
注意:采用root角色编译,减少文件权限出现的问题
#### 2.jar包准备
`hadoop-2.7.2-src.tar.gz` | [快速下载通道](https://archive.apache.org/dist/hadoop/common/hadoop-2.7.2/)
`jdk-8u144-linux-x64.tar.gz`  | [快速下载通道](https://www.oracle.com/technetwork/java/javase/documentation/8u-relnotes-2225394.html)
`apache-ant-1.9.10-bin.tar.gz` (build tool 打包工具)  | [快速下载通道](https://archive.apache.org/dist/ant/binaries/apache-ant-1.9.10-bin.tar.gz)
`apache-maven-3.0.5-bin.tar.gz`  | [快速下载通道](http://archive.apache.org/dist/maven/maven-3/3.0.5/binaries/)
`protobuf-2.5.0.tar.gz` (序列化框架)  | [快速下载通道](https://files.pythonhosted.org/packages/3f/ad/c8221a0778cc04197047f0f6ddee683ef1a0851976a4bd4ad17af19d22ec/protobuf-2.5.0.tar.gz)

### jar包安装
#### maven安装
解压tar包到指定目录
```
[root@corehub-001 software]# tar -zvxf apache-maven-3.0.5-bin.tar.gz -C /opt/module/
```
重命名
```
[root@corehub-001 module]# mv apache-maven-3.0.5 maven
[root@corehub-001 module]# ll
total 16
drwxr-xr-x.  6 root   root  4096 Feb  4  2018 ant
drwxr-xr-x. 15  10011 10011 4096 Jan 31 13:52 hadoop
drwxr-xr-x.  6 root   root  4096 Feb  3 14:54 maven
[root@corehub-001 module]# 
```
配置环境变量
```
[root@corehub-001 ~]# cd /opt/module/maven/
[root@corehub-001 maven]# pwd
/opt/module/maven
[root@corehub-001 maven]# vim /etc/profile
```
```
##MAVEN_HOME
export MAVEN_HOME=/opt/module/maven
export PATH=$PATH:$MAVEN_HOME/bin
```
```
[root@corehub-001 maven]# source /etc/profile
[root@corehub-001 maven]# mvn -version
Apache Maven 3.0.5 (r01de14724cdef164cd33c7c8c2fe155faf9602da; 2013-02-19 21:51:28+0800)
Maven home: /opt/module/maven
Java version: 1.8.0_162, vendor: Oracle Corporation
Java home: /opt/devtool/jdk1.8.0_162/jre
Default locale: en_US, platform encoding: UTF-8
OS name: "linux", version: "2.6.32-754.10.1.el6.x86_64", arch: "amd64", family: "unix"
[root@corehub-001 maven]# 
```


#### ant安装
解压tar包到指定目录
```
[root@corehub-001 software]# tar -zvxf apache-ant-1.9.10-bin.tar.gz -C /opt/module/
```
重命名
```
[root@corehub-001 module]# mv apache-ant-1.9.10 ant
[root@corehub-001 module]# ll
total 8
drwxr-xr-x.  6 root  root  4096 Feb  4  2018 ant
drwxr-xr-x. 15 10011 10011 4096 Jan 31 13:52 hadoop
[root@corehub-001 module]# 
```
配置环境变量
```
[root@corehub-001 ~]# cd /opt/module/ant/
[root@corehub-001 ant]# pwd
/opt/module/ant
[root@corehub-001 ant]# vim /etc/profile
```
```
##ANT_HOME
export ANT_HOME=/opt/module/ant
export PATH=$PATH:$ANT_HOME/bin
```
```
[root@corehub-001 ant]# source /etc/profile
[root@corehub-001 ant]# ant -version
Apache Ant(TM) version 1.9.10 compiled on February 3 2018
[root@corehub-001 ant]# 
```
#### 安装glibc-headers 与 g++
```
yum install glibc-headers
```
```
[root@corehub-001 geek-developer]# yum install gcc-c++
Loaded plugins: fastestmirror, refresh-packagekit, security
Setting up Install Process
Loading mirror speeds from cached hostfile
 * base: ftp.sjtu.edu.cn
 * extras: centos.ustc.edu.cn
 * updates: mirror.bit.edu.cn
Resolving Dependencies
--> Running transaction check
---> Package gcc-c++.x86_64 0:4.4.7-23.el6 will be installed
--> Processing Dependency: libstdc++-devel = 4.4.7-23.el6 for package: gcc-c++-4.4.7-23.el6.x86_64
--> Running transaction check
---> Package libstdc++-devel.x86_64 0:4.4.7-23.el6 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package                 Arch           Version              Repository    Size
================================================================================
Installing:
 gcc-c++                 x86_64         4.4.7-23.el6         base         4.7 M
Installing for dependencies:
 libstdc++-devel         x86_64         4.4.7-23.el6         base         1.6 M

Transaction Summary
================================================================================
Install       2 Package(s)

Total size: 6.3 M
Total download size: 4.7 M
Installed size: 20 M
Is this ok [y/N]: y
Downloading Packages:
gcc-c++-4.4.7-23.el6.x86_64.rpm                          | 4.7 MB     00:03     
Running rpm_check_debug
Running Transaction Test
Transaction Test Succeeded
Running Transaction
  Installing : libstdc++-devel-4.4.7-23.el6.x86_64                          1/2 
  Installing : gcc-c++-4.4.7-23.el6.x86_64                                  2/2 
  Verifying  : libstdc++-devel-4.4.7-23.el6.x86_64                          1/2 
  Verifying  : gcc-c++-4.4.7-23.el6.x86_64                                  2/2 

Installed:
  gcc-c++.x86_64 0:4.4.7-23.el6                                                 

Dependency Installed:
  libstdc++-devel.x86_64 0:4.4.7-23.el6                                         

Complete!
[root@corehub-001 geek-developer]#
```

#### 安装make与cmake
```
yum install make
```

```
[root@corehub-001 geek-developer]# yum install cmake
Loaded plugins: fastestmirror, refresh-packagekit, security
Setting up Install Process
Loading mirror speeds from cached hostfile
 * base: ftp.sjtu.edu.cn
 * extras: centos.ustc.edu.cn
 * updates: mirror.bit.edu.cn
Resolving Dependencies
--> Running transaction check
---> Package cmake.x86_64 0:2.8.12.2-4.el6 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package         Arch             Version                  Repository      Size
================================================================================
Installing:
 cmake           x86_64           2.8.12.2-4.el6           base           8.0 M

Transaction Summary
================================================================================
Install       1 Package(s)

Total download size: 8.0 M
Installed size: 28 M
Is this ok [y/N]: y
Downloading Packages:
cmake-2.8.12.2-4.el6.x86_64.rpm                          | 8.0 MB     00:05     
Running rpm_check_debug
Running Transaction Test
Transaction Test Succeeded
Running Transaction
  Installing : cmake-2.8.12.2-4.el6.x86_64                                  1/1 
  Verifying  : cmake-2.8.12.2-4.el6.x86_64                                  1/1 

Installed:
  cmake.x86_64 0:2.8.12.2-4.el6                                                 

Complete!
[root@corehub-001 geek-developer]# 
```


#### protobuf安装
解压tar包到指定目录
```
[root@corehub-001 software]# tar -zvxf protobuf-2.5.0.tar.gz -C /opt/module/
```
重命名
```
[root@corehub-001 module]# mv protobuf-2.5.0 protobuf
[root@corehub-001 module]# ll
total 16
drwxr-xr-x.  6 root   root  4096 Feb  4  2018 ant
drwxr-xr-x. 15  10011 10011 4096 Jan 31 13:52 hadoop
drwxr-xr-x.  6 root   root  4096 Feb  3 14:54 maven
drwxr-x---.  4 109965  5000 4096 Feb 28  2013 protobuf
[root@corehub-001 module]# 
```
配置环境变量
```
[root@corehub-001 ~]# cd /opt/module/protobuf/
[root@corehub-001 protobuf]# pwd
/opt/module/protobuf
[root@corehub-001 protobuf]# vim /etc/profile
```
```
##PROTOBUF_HOME
export PROTOBUF_HOME=/opt/module/protobuf
export PATH=$PATH:$PROTOBUF_HOME/bin
```
```
[root@corehub-001 protobuf]# source /etc/profile
```

### 编译源码

## 7. HDFS 概述
### HDFS产生背景以及定义
#### HDFS产生背景
> 随着数据量越来越大,在一个操作系统存不下所有的数据,那么就分配到更多的操作系统管理的磁盘中,但是不方便管理和维护,迫切需要一种系统来管理多台机器上的文件,这就是分布式文件管理系统,HDFS只是分布式文件管理系统中的一种.

#### HDFS定义
> HDFS(Hadoop Distributed File System) 它是一个文件系统,用于存储文件,通过目录树来定位文件,其次,它是分布式的,由很多服务器联合起来实现其功能,集群中的服务器有各自的角色.
> 
> HDFS使用场景: 适合一次写入,多次读取的场景,且不支持文件的修改,适合用来做数据分析,并不适合用来做网盘应用.

#### HDFS优点缺点 | 技术选型知识点
> **`优点`**
1.`高容错性`:数据自动保存多个副本,它通过增加副本的形式,提供容错性.某一个副本丢失以后,它可以自动恢复.
2.`适合处理大数据`:
`数据规模`:能够处理数据规模达到GB,TB,甚至PB级别数据.
`文件规模`:能够处理百万规模以上的文件数量,数量相当之大.
3.`可构建到廉价机器上`,通过多个副本机制,提高可靠性.

> **`缺点`**
1.`不适合低延时数据访问`,比如毫秒级的存储数据,是做不到的.
2.`无法高效的对大量的小文件进行存储`:存储大量小文件的话,它会占用NameNode大量的内存来存储文件目录和块信息,这样是不可取的,因为NameNode的内存总是有限的.小文件存储的寻址时间会超过读取时间,它违反了HDFS设计目标
3.`不支持并发写入`,文件随机修改.
4.`仅支持数据的追加`,不支持文件的随机修改.

#### HDFS架构组成
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_015.jpg)

##### 1.NameNode(nn):
> Masert,它是一个主管,管理者.
> 管理HDFS名称空间,配置副本策略,管理数据块(Block)映射信息,处理客户端读写请求.

##### 2.DataNode(dn):
> Slave,NameNode下达命令,DataNode执行实际操作.
> 存储实际数据块,执行数据块的读写操作.

##### 3.Client客户端:
> 文件切分,文件上传HDFS时,Client将文件切分成一个一个的Block,然后在进行上传.
> 与NameNode交互,获取文件的位置信息.
> 与DataNode交互,读取或写入数据.
> Client提供一些命令来管理HDFS,比如NameNode格式化.
> Client可以提供一些命令来访问HDFS,比如对HDFS增删改查(CURD)操作.

##### 4.SecondaryNameNode:
> 并非NameNode的热备,当NameNode挂掉时,它并不能马上替换NameNode并提供服务.
> 辅助NameNode,分担其工作量,比如定期合并Fsimage和Edis,并推送给NameNode.
> 在紧急情况下,可辅助恢复NameNode.


#### HDFS文件块大小(面试重点)
> HDFS中的文件在物理上是分块存储(Block),块的大小可以通过配置(dfs.blocksize)参数来规定,默认大小在Hadoop2.x版本中是128M,老版本1.x中是64M.
> 
> Q&A
> 为什么块的大小不能设置太小?也不能设置太大?
> 
> HDFS的块设置太小,会增加寻址时间,程序一直在找块的开始位置.
> 
>如果块设置的太大,从磁盘传输数据的时间会明显大于定位这个块开始位置所需的时间,导致程序在处理块数据时会非常慢.
> 
> **`HDFS块的大小设置主要取决于磁盘传输速率.`**

### 7.1 HDFS Shell操作(开发重点)

#### 1.基本语法
> **`bin/hadoop fs 具有指令`** OR **`bin/hdfs dfs 具体指令`**
> dfs是fs的实现类,dfs相当于子类

#### 2.启动集群
> 启动001号服务器(启动dfs服务)并查看进程
``` powershell
[root@corehub-001 hadoop]# sbin/start-dfs.sh
19/02/13 22:58:33 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Starting namenodes on [corehub-001]
root@corehub-001's password: 
corehub-001: namenode running as process 84816. Stop it first.
root@corehub-001's password: corehub-003: datanode running as process 85244. Stop it first.
corehub-002: datanode running as process 86146. Stop it first
corehub-003: secondarynamenode running as process 101469. Stop it first.
19/02/13 22:58:47 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
[root@corehub-001 hadoop]# jps
84816 NameNode
102134 Jps
101695 DataNode
[root@corehub-001 hadoop]# 
```
> 启动002号服务器(启动yarn服务)并查看进程
``` powershell
[root@corehub-002 hadoop]# sbin/start-yarn.sh
starting yarn daemons
starting resourcemanager, logging to /opt/module/hadoop/logs/yarn-root-resourcemanager-corehub-002.out
corehub-001: starting nodemanager, logging to /opt/module/hadoop/logs/yarn-root-nodemanager-corehub-001.out
corehub-003: starting nodemanager, logging to /opt/module/hadoop/logs/yarn-root-nodemanager-corehub-003.out
corehub-002: starting nodemanager, logging to /opt/module/hadoop/logs/yarn-root-nodemanager-corehub-002.out
[root@corehub-002 hadoop]# jps
105555 Jps
86146 DataNode
105307 ResourceManager
105421 NodeManager
[root@corehub-002 hadoop]# 
```
> 查看003号服务器进程
``` powershell
[root@corehub-003 hadoop]# jps
104626 NodeManager
107159 Jps
101469 SecondaryNameNode
85244 DataNode
You have new mail in /var/spool/mail/root
[root@corehub-003 hadoop]# 
```

#### 3.hadoop fs命令大全
```
[root@corehub-001 hadoop]# hadoop fs
Usage: hadoop fs [generic options]
        [-appendToFile <localsrc> ... <dst>]
        [-cat [-ignoreCrc] <src> ...]
        [-checksum <src> ...]
        [-chgrp [-R] GROUP PATH...]
        [-chmod [-R] <MODE[,MODE]... | OCTALMODE> PATH...]
        [-chown [-R] [OWNER][:[GROUP]] PATH...]
        [-copyFromLocal [-f] [-p] [-l] <localsrc> ... <dst>]
        [-copyToLocal [-p] [-ignoreCrc] [-crc] <src> ... <localdst>]
        [-count [-q] [-h] <path> ...]
        [-cp [-f] [-p | -p[topax]] <src> ... <dst>]
        [-createSnapshot <snapshotDir> [<snapshotName>]]
        [-deleteSnapshot <snapshotDir> <snapshotName>]
        [-df [-h] [<path> ...]]
        [-du [-s] [-h] <path> ...]
        [-expunge]
        [-find <path> ... <expression> ...]
        [-get [-p] [-ignoreCrc] [-crc] <src> ... <localdst>]
        [-getfacl [-R] <path>]
        [-getfattr [-R] {-n name | -d} [-e en] <path>]
        [-getmerge [-nl] <src> <localdst>]
        [-help [cmd ...]]
        [-ls [-d] [-h] [-R] [<path> ...]]
        [-mkdir [-p] <path> ...]
        [-moveFromLocal <localsrc> ... <dst>]
        [-moveToLocal <src> <localdst>]
        [-mv <src> ... <dst>]
        [-put [-f] [-p] [-l] <localsrc> ... <dst>]
        [-renameSnapshot <snapshotDir> <oldName> <newName>]
        [-rm [-f] [-r|-R] [-skipTrash] <src> ...]
        [-rmdir [--ignore-fail-on-non-empty] <dir> ...]
        [-setfacl [-R] [{-b|-k} {-m|-x <acl_spec>} <path>]|[--set <acl_spec> <path>]]
        [-setfattr {-n name [-v value] | -x name} <path>]
        [-setrep [-R] [-w] <rep> <path> ...]
        [-stat [format] <path> ...]
        [-tail [-f] <file>]
        [-test -[defsz] <path>]
        [-text [-ignoreCrc] <src> ...]
        [-touchz <path> ...]
        [-truncate [-w] <length> <path> ...]
        [-usage [cmd ...]]

Generic options supported are
-conf <configuration file>     specify an application configuration file
-D <property=value>            use value for given property
-fs <local|namenode:port>      specify a namenode
-jt <local|resourcemanager:port>    specify a ResourceManager
-files <comma separated list of files>    specify comma separated files to be copied to the map reduce cluster
-libjars <comma separated list of jars>    specify comma separated jar files to include in the classpath.
-archives <comma separated list of archives>    specify comma separated archives to be unarchived on the compute machines.

The general command line syntax is
bin/hadoop command [genericOptions] [commandOptions]

[root@corehub-001 hadoop]# 
```
#### 4.常用命令实操
> 1. 启动Hadoop集群
> **`sbin/start-dfs.sh`**
> **`sbin/start-yarn.sh`**
> 
> 2. -help 帮助信息
> **`hadoop fs -help rm`**
> 
> 3. -ls 显示目录信息
> **`hadoop fs -ls /`**
> 
> 4. -mkdir 在HDFS上创建目录
> **`hadoop fs -mkdir -p /group/geekparkhub`**
> 
> 5. -moveFromLocal 从本地剪切粘贴到HDFS
> touch test.txt
> **`hadoop fs -moveFromLocal ./test.txt /group/geekparkhub`**
> 
> 6. -appendToFile 追加一个文件到已存在的文件末尾
> touch test001.txt
> vim test001.txt
> 输入 123
> **`hadoop fs -appendToFile ./test001.txt /group/geekparkhub/test.txt`**
> 
> 7. -cat 显示文件内容
> **`hadoop fs -cat /group/geekparkhub/test.txt`**
> 
> 8. -chgrp,-chmod,-chown,linux文件系统中用法一致,修改文件所属权限
> 
> 9. -copyFromLocal 从本地文件系统中拷贝到HDFS中
> **`hadoop fs -copyFromLocal test001.txt /group/geekparkhub/`**
> 
> 10. -copyToLocal 从HDFS上拷贝到本地
> **`hadoop fs -copyToLocal /group/geekparkhub/test.txt ./`**
> 
> 11. -cp 从HDFS路径拷贝到HDFS另一个路径
> **`hadoop fs -cp /group/geekparkhub/test.txt /user/geekparkhub/`**
> 
> 12. -mv 在HDFS目录中移动文件
> **`hadoop fs -mv /group/geekparkhub/test001.txt /user/geekparkhub/`**
> 
> 13. -get 等同于copyToLocal 从HDFS下载文件到本地
> **`hadoop fs -get /group/geekparkhub/test001.txt ./`**
> 
> 14. -getmerge 合并下载多个文件,比如HDFS目录 /log/下有多个文件日志文件,log1,log3,log3
> **`hadoop fs -getmerge /user/geekparkhub/* ./list.txt`**
> 
> 15. -put 等同于copyFromLocal
> **`hadoop fs -put ./list.txt /user/geekparkhub`**
> 
> 16. -tail 显示一个文件的末尾
> **`hadoop fs -tail /group/geekparkhub/test.txt`**
> 
> 17. -rm 删除文件或文件夹
> **`hadoop fs -rm /user/geekparkhub/list.txt`**
> 
> 18. -rmdir 删除空目录
> **`hadoop fs -rmdir /user/testfile/`**
> 
> 19. -du 统计文件夹的大小信息
> **`hadoop fs -du -s -h /`**
> 
> 20. -setrep 设置HDFS中文件的副本数量
> **`hadoop fs -setrep 10 /group/geekparkhub/test.txt`**


## 🔒 尚未解锁 正在学习探索中... 尽情期待 Blog更新! 🔒
### 7.2 HDFS客户端操作(开发重点)
#### HDFS客户端环境准备
#### HDFS API操作
##### HDFS文件上传(测试)
##### HDFS文件下载
##### HDFS文件夹删除
##### HDFS文件名更改
##### HDFS文件详情查看
##### HDFS文件和文件夹判断
#### HDFS I/O流操作
##### HDFS文件上传
##### HDFS文件下载
##### 定位文件读取
            
### 7.3 HDFS数据流(面试重点)
#### HDFS写数据流程
##### 剖析文件写入
##### 网络拓展-节点距离计算
##### 机架感知(副本储存节点)

### 7.4 NameNode和SecondayNameNode工作机制(面试重点)

### 7..5 DataNode(面试开发重点)

### 7.6 HDFS 2.X新特性
#### 集群间数据拷贝
#### Hadoop存档
#### 快照管理
#### 回收站

### 7.7 HDFS HA高可用






## 7. 常见错误(各种坑)及解决方案


## 8. 修仙之道 技术架构迭代 登峰造极之势
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
- Email：<jeep711.home.@gmail.com>—— <jeep-711@outlook.com> —— <geekparkhub@outlook.com>



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

------