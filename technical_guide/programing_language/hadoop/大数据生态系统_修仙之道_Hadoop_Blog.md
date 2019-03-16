
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
- **`Official Public Email`**
- Group Email：<geekparkhub@outlook.com> —— <hackerparkhub@outlook.com> —— <hackerpark@hotmail.com>
- User Email：<jeep711.home.@gmail.com> —— <jeep-711@outlook.com>
- System Email：<systemhub-711@outlook.com>
- Service Email：<servicehub-711@outlook.com>


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
> **大数据部门组织结构**
| 所在组    |  所在组工作职责 |
| :-------- | :--------:|
| 平台组  | Hadoop,Flume,Kafka,Hbase,Spark等框架平台搭建,集群性能监控,集群性能调优 |
| 数据仓库组  | ETL工程师-数据清洗,Hive工程师-数据分析,数据仓库建模 |
| 数据挖掘组  | 算法工程师 推荐系统工程师 用户画像工程师 |
| 数据报表开发组  | JAVAEE工程师 |

## 3. 探索Hadoop框架 大数据生态

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
> Cloudera Manager是集群的软件分发及管理监控平台,可以再几个小时内部部署好一个Hadoop集群,并对集群节点及服务进行实时监控,Cloudera Support即是对Hadoop的技术支持.
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
> Hadoop底层维护多个数据副本,所以即使Hadoop某个计算元素或存储出现故障,也不会导致数据的丢失.
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
> HDFS (Hadoop Distributed File System) | **`三大组件 nn / dn / 2nn`**
> 
> 1.NameNode(nn) : 存储文件的元数据,如文件名,文件目录结构,文件属性(生成时间,副本数,文件权限,),以及每个文件的块列表和块所在的DataNode等.
> 
> 2.DataNode(dn) : 在本地文件系统存储文件块数据,以及块数据的校验和.
> 
> 3.Secondary NameNode(2nn):用来监控HDFS状态的辅助后台程序,每隔一段时间获取HDFS元数据的快照.

#### YARN 架构概述
> **`四大组件 | RM / NM / AM / Container`**
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
> **`vim /etc/udev/rules.d/70-persistent-net.rules`**

> 源代码
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

> 将NAME="eth1"更改为NAME="eth0",并复制00:0c:29:67:b3:77地址
``` bash
# PCI device 0x8086:0x100f (e1000)
SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="00:0c:29:67:b3:77", ATTR{type}=="1", KERNEL=="eth*", NAME="eth0"
```
> 更改完毕,`:wq`保存退出

> 修改网络配置
> 粘贴上一步地址,修改HWADDR属性
> **`vim /etc/sysconfig/network-scripts/ifcfg-eth0`**
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
> 更改完毕,`:wq`保存退出

#### 3.修改主机名
`vim /etc/sysconfig/network`
``` bash
NETWORKING=yes
HOSTNAME=corehub-004
```
> 更改完毕,`:wq`保存退出

#### 4.关闭防火墙
> 暂时性关闭防火墙:`service iptables stop`

#### 5.创建用户
> `useradd username`

#### 6.配置用户具有root权限
`vim /etc/sudoers`
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_006.jpg)
> 更改完毕,`:wq!`保存退出

#### 7.在/opt目录下创建文件夹
> 1.创建software,module文件夹
> software 用于日后存储的程序安装包
> module 用于日后存储解析后的程序jar包
``` powershell
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
> 2.修改software,module文件夹的所有者
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
> 通过远程工具,将hadoop-2.7.2.tar.gz传输到/opt/software/目录下
> 

> 将hadoop-2.7.2.tar.gz解压/opt/module/目录下
``` powershell
tar -zxvf hadoop-2.7.2.tar.gz -C /opt/module
```
> 将解压完成hadoop-2.7.2重命名为hadoop
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
> 配置hadoop环境变量
``` powershell
[root@corehub-001 module]# cd hadoop/
[root@corehub-001 hadoop]# pwd
/opt/module/hadoop
[root@corehub-001 hadoop]#
```
``` powershell
[root@corehub-001 geek-developer]# vim /etc/profile
```
``` powershell
##HADOOP_HOME
export HADOOP_HOME=/opt/module/hadoop
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
```
> 完成环境变量,`:wq`保存退出
> `source /etc/profile` 更新配置文件指令
``` powershell
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
> By default, Hadoop is configured to run in a non-distributed mode, as a single Java process. This is useful for debugging.
> 
> The following example copies the unpacked conf directory to use as input and then finds and displays every match of the given regular expression. Output is written to the given output directory.
``` powershell
$ mkdir input
$ cp etc/hadoop/*.xml input
$ bin/hadoop jar s
```

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
``` powershell
[geek-developer@corehub-001 hadoop]$ sudo cp etc/hadoop/*.xml input/
[geek-developer@corehub-001 hadoop]$ ls input/
capacity-scheduler.xml  hadoop-policy.xml  httpfs-site.xml  kms-site.xml
core-site.xml           hdfs-site.xml      kms-acls.xml     yarn-site.xml
[geek-developer@corehub-001 hadoop]$ 
```

##### 3.执行share目录下的hadoop-mapreduce-examples-2.7.2.jar包,并指定输入和输出路径,以符合正则表达式并统计个数
> `dfs[a-z.]+` 以dfs开头,以a到z任意字符以.过滤掉 - - 字符
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
``` powershell
[root@corehub-001 hadoop]# cd wcinput/
[root@corehub-001 wcinput]# touch wc.input
[root@corehub-001 wcinput]# ll
total 0
-rw-r--r--. 1 root root 0 Jan 24 23:08 wc.input
[root@corehub-001 wcinput]# 
```
##### 3.编辑wc.input文件并在文件中输入内容,输入完毕按esc,输入:wq保存退出
``` powershell
[root@corehub-001 wcinput]# vim wc.input
```
``` powershell
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
``` powershell
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
> 获取并复制JAVA_HOME路径
``` powershell
[root@corehub-001 hadoop]# echo $JAVA_HOME
/opt/jdk1.8.0_162
```
> 配置hadoop-env.sh
``` powershell
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

``` powershell
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
> 输入完毕按esc,输入:wq保存退出

###### 配置 **`hdfs.site.xml`**
> hdfs.site.xml 官方文档说明 : [hdfs-default.xml](http://hadoop.apache.org/docs/r2.7.2/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml)
``` powershell
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
> 输入完毕按esc,输入:wq保存退出

##### 启动集群
###### 格式化 NameNode
> (第一次初始化启动需要格式化,只需在首次启动前格式化)
``` powershell
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
``` powershell
[root@corehub-001 hadoop]# sbin/hadoop-daemon.sh start namenode
starting namenode, logging to /opt/module/hadoop/logs/hadoop-root-namenode-corehub-001.out
[root@corehub-001 hadoop]# jps
3153 Jps
3022 NameNode
```

###### 启动 DataNode
``` powershell
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

``` powershell
[root@corehub-001 hadoop]# bin/hdfs dfs -mkdir -p /user/geekparkhub/input
19/01/25 14:41:14 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
```
``` powershell
[root@corehub-001 hadoop]# bin/hdfs dfs -ls -R /
19/01/25 14:44:20 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
drwxr-xr-x   - root supergroup          0 2019-01-25 14:41 /user
drwxr-xr-x   - root supergroup          0 2019-01-25 14:41 /user/geekparkhub
drwxr-xr-x   - root supergroup          0 2019-01-25 14:41 /user/geekparkhub/input
[root@corehub-001 hadoop]# 
```
##### 在hadoop目录下,将wcinput目录及元数据文件上传到/user/geekparkhub/input目录中
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_009.jpg)
``` powershell
[root@corehub-001 hadoop]# bin/hdfs dfs -put wcinput/wc.input /user/geekparkhub/input
19/01/25 15:02:56 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
[root@corehub-001 hadoop]#
```

##### 执行并读取HDFS程序
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_010.jpg)
``` powershell
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
``` powershell
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
``` powershell
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
``` powershell
[root@corehub-001 hadoop]# mv etc/hadoop/mapred-site.xml.template etc/hadoop/mapred-site.xml
```
``` powershell
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
``` powershell
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
``` powershell
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
``` powershell
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
``` powershell
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
``` powershell
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
> 注意:开启日志聚集功能,需要`重新启NodeManager,ResourceManager,HistoryManager此三项服务`.

##### 分别停止HistoryManager服务,NodeManager服务,ResourceManager服务

###### 停止HistoryManager服务
``` powershell
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
``` powershell
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
``` powershell
[root@corehub-001 hadoop]# sbin/yarn-daemon.sh stop resourcemanager
stopping resourcemanager
[root@corehub-001 hadoop]# jps
98388 Jps
9353 DataNode
9066 NameNode
[root@corehub-001 hadoop]# 
```
##### 配置yarn-site.xml
``` prolog
[root@corehub-001 hadoop]# vim etc/hadoop/yarn-site.xml
```
```xml
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
``` powershell
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
``` powershell
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
``` powershell
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
``` powershell
[root@corehub-001 hadoop]# bin/hdfs dfs -rm -r /user/geekparkhub/output
19/01/27 22:26:57 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
19/01/27 22:26:58 INFO fs.TrashPolicyDefault: Namenode trash configuration: Deletion interval = 0 minutes, Emptier interval = 0 minutes.
Deleted /user/geekparkhub/output
[root@corehub-001 hadoop]# 
```
##### 执行WordCount程序
``` powershell
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

> 查看日志方式 也可以通过进入log文件夹进行查看
``` powershell
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
| :-------- | :--------:| :--------:|
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
> **`scp     -r      $pdir/$fname`**
> **`$user@corehub$host:$pdir/$fname`**
> 指令    递归    源数据文件路径/名称                   目的用户名@主机名称:目的路径/名称
> 
> 3.scp实操案例
> 在corehub-001上,将corehub-001中的/opt/module目录下的软件拷贝到corehub-002上
``` powershell
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
``` powershell
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
``` powershell
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
> 4.将corehub-001配置文件分发推送到corehub-002,corehub-003服务器上,推送完毕后更新配置即可生效
``` powershell
[root@corehub-001 ~]# scp -r /etc/profile root@corehub-002:/etc/profile
root@corehub-002's password: 
profile                                                                             100% 2073     2.0KB/s   00:00    
[root@corehub-001 ~]# 
```
``` powershell
[root@corehub-001 ~]# scp -r /etc/profile root@corehub-003:/etc/profile
The authenticity of host 'corehub-003 (192.168.152.136)' can't be established.
RSA key fingerprint is 63:9d:81:a7:3d:83:7f:04:19:32:8f:c8:97:9d:07:d8.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'corehub-003,192.168.152.136' (RSA) to the list of known hosts.
root@corehub-003's password: 
profile                                                                             100% 2073     2.0KB/s   00:00    
[root@corehub-001 ~]# 
```
``` powershell
source /etc/profile
```

##### rsync 远程同步工具
> rsync主要用于备份和镜像,具有速度快,避免复制相同内容和支持符号链接的优点.
> rsync与scp区别:用rsync做文件的复制要比scp速度快,rsync只对差异文件做更新,scp是把所有文件复制的过程.
> 
> 基本语法
> 
> **`rsync -rVl $pdir$fname $user@corehub$host:$pdir/$fname`**
> 指令    选项参数 源文件路径/名称  目的用户名@主机名称:目的路径/名称

| 选项      |     功能 |
| :-------- | :--------:|
| -r    |   递归 |
| -v    |   显示复制过程 |
| -l    |   拷贝符号连接 |

> rsync实操案例
> 将corehub-001服务器上的/opt/software目录同步到corehub-002服务器的root用户目录下
``` powershell
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

> 需求分析:
>rsync指令 原始拷贝
> rsync -rvl /opt/module root@corehub-002:/opt/
> 期望脚本:将sxync要要同步的文件名称
> 说明:在/home/geek-developer/bin/此目录下存放脚本,geek-developer用户可以在系统任何地方直接执行.

> 脚本实现
> 创建bin目录 mkdir bin
``` powershell
[root@corehub-001 ~]# mkdir bin
[root@corehub-001 ~]# ll
total 100
-rw-------. 1 root root  3362 Jan 18 04:54 anaconda-ks.cfg
drwxr-xr-x. 2 root root  4096 Jan 30 18:00 bin
drwxr-xr-x. 2 root root  4096 Jan 24 19:40 Desktop
drwxr-xr-x. 2 root root  4096 Jan 18 05:51 Documents
drwxr-xr-x. 2 root root  4096 Jan 18 05:51 Downloads
-rw-r--r--. 1 root root 41364 Jan 18 04:54 install.log
-rw-r--r--. 1 root root  9154 Jan 18 04:52 install.log.syslog
drwxr-xr-x. 2 root root  4096 Jan 18 05:51 Music
drwxr-xr-x. 2 root root  4096 Jan 18 05:51 Pictures
drwxr-xr-x. 2 root root  4096 Jan 18 05:51 Public
drwxr-xr-x. 2 root root  4096 Jan 18 05:51 Templates
drwxr-xr-x. 2 root root  4096 Jan 18 05:51 Videos
[root@corehub-001 ~]#
```

> 进入bin目录 cd bin/
``` powershell
[root@corehub-001 ~]# cd bin/
[root@corehub-001 bin]# ll
total 0
[root@corehub-001 bin]# 
```

> 创建xsync文件 touch xsync
``` powershell
[root@corehub-001 bin]# touch xsync
[root@corehub-001 bin]# ll
total 0
-rw-r--r--. 1 root root 0 Jan 30 18:05 xsync
[root@corehub-001 bin]# 
```

> 编辑xsync vim xsync
``` powershell
#!/bin/bash
# 1.获取输入参数个数,如果没有参数,直接退出
pcount=$#
if((pcount==0)); then
echo no args;
exit
fi
# 2.获取文件名称
p1=$1
fname=`basename $p1`
echo fname=$fname
# 3.获取上级目录到据对路径
pdri=`cd -P $(dirname $p1); pwd`
echo pdir=$pdri
# 4.获取当前用户名称
user=`whoami`
# 5.循环遍历
for((host=103;host<105;host++)); do
echo -------corehub$host-------
rsync -rvl $pdir/$fname $user@corehub$host:$pdri
done
```

#### 集群配置
> 1.集群部署规划
| linux服务器 | corehub-001 | corehub-002 | corehub-003 |
| :-------- | :--------:| :------: | :------: |
| HDFS    | NameNode,DataNode | DataNode | SecondaryNameNode,DataNode |
| YARN    | NodeManager |  ResourceManager,NodeManager  | NodeManager |

> 2.配置集群
> 配置core-site.xml
``` powershell
[root@corehub-001 hadoop]# vim etc/hadoop/core-site.xml
```
> 在该文件中编写如下配置
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
> HDFS配置文件
> 配置hadoop-env.sh
``` powershell
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
> 配置hdfs-site.xml
``` powershell
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
> YARN配置文件
> 配置yarn-env.sh
``` powershell
[root@corehub-001 hadoop]# vim etc/hadoop/yarn-env.sh
```
``` powershell
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
> 配置yarn-site.xml
> 在该文件中编写如下配置
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

> MapReduce配置文件
> 配置mapred-env.sh
``` powershell
[root@corehub-001 hadoop]# vim etc/hadoop/mapred-env.sh
```

``` powershell
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
> 配置mapred-site.xml
> 在该文件中编写如下配置
``` powershell
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
> 分别删除001,002,003号服务器上的 log,data文件
> 删除前提,先保证没有jps在运行中,否则会导致悲剧发生
> 删除001号服务器
``` powershell
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
> 删除002号服务器
``` powershell
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
> 删除003号服务器
``` powershell
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
> 最后 格式化 001服务器数据
``` powershell
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
> 启动001号服务
``` powershell
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
> 启动002号服务
``` powershell
[root@corehub-002 hadoop]# sbin/hadoop-daemon.sh start datanode
starting datanode, logging to /opt/module/hadoop/logs/hadoop-root-datanode-corehub-002.out
[root@corehub-002 hadoop]# jps
63289 DataNode
63405 Jps
[root@corehub-002 hadoop]# 
```
> 启动003号服务
``` powershell
[root@corehub-003 hadoop]# sbin/hadoop-daemon.sh start datanode
starting datanode, logging to /opt/module/hadoop/logs/hadoop-root-datanode-corehub-003.out
[root@corehub-003 hadoop]# jps
67184 DataNode
67332 Jps
[root@corehub-003 hadoop]# 
```

#### SSH无密码配置
> SSH有密码演示
``` powershell
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
> 免登录原理
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_014.jpg)

> ls -al指令 grep指令查找到.ssh文件
``` powershell
[root@corehub-001 ~]# ls -al | grep .ssh
drwx------.  2 root root  4096 Jan 31 13:24 .ssh
[root@corehub-001 ~]# 
```
> cd进入.ssh目录,创建公钥私钥,输入指令后连续输入三次回车即可完成创建
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
> 将001号服务器公钥拷贝到自身服务器
``` powershell
[root@corehub-001 ~]# ssh corehub-001
The authenticity of host 'corehub-001 (192.168.177.130)' can't be established.
RSA key fingerprint is 99:b3:c1:16:af:d9:de:79:5f:cf:53:25:63:f1:30:1d.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'corehub-001,192.168.177.130' (RSA) to the list of known hosts.
root@corehub-001's password: 
Last login: Thu Jan 31 14:22:12 2019 from 192.168.177.2
[root@corehub-001 ~]# 
```
> 将001号服务器公钥拷贝到002服务器
``` powershell
[root@corehub-001 .ssh]# ssh-copy-id corehub-002
root@corehub-002's password: 
Now try logging into the machine, with "ssh 'corehub-002'", and check in:
  .ssh/authorized_keys
to make sure we haven't added extra keys that you weren't expecting.
[root@corehub-001 .ssh]# 
```
> 将001号服务器公钥拷贝到003服务器
``` powershell
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
> 拷贝完毕,测试是否可以免登录
> 免登录002服务器
``` powershell
[root@corehub-001 ~]# ssh corehub-002
Last login: Thu Jan 31 14:22:33 2019 from corehub-001
[root@corehub-002 ~]# exit
logout
Connection to corehub-002 closed.
[root@corehub-001 ~]# 
```
> 免登录003服务器
``` powershell
[root@corehub-001 ~]# ssh corehub-003
Last login: Thu Jan 31 14:22:32 2019 from 192.168.177.2
[root@corehub-003 ~]# exit
logout
Connection to corehub-003 closed.
[root@corehub-001 ~]# 
```
> ssh文件功能说明
> `Known hosts`:记录ssh访问过计算机公钥(public key)
> `id rsa`:生成的私钥
> `id_rsa.pub`:生成的公钥
> `authorized_keys`:存放授权过得无密码登录服务器公钥

#### 群起集群
> 1.配置slaves
``` powershell
[root@corehub-001 hadoop]# vim etc/hadoop/slaves
```
> 在该文件中添加一下内容
> 注意:该文件添加的内容结尾不允许有空格,文件中部允许有空格
``` powershell
corehub-001
corehub-002
corehub-003
```
> 测试群起
``` powershell
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
> 对照 集群部署规划 查看001号进程 是否正常启动
``` powershell
[root@corehub-001 hadoop]# jps
39894 NameNode
47978 Jps
46235 DataNode
[root@corehub-001 hadoop]#
```
> 对照 集群部署规划 查看002号进程 是否正常启动
``` powershell
[root@corehub-002 hadoop]# jps
19375 Jps
9007 DataNode
[root@corehub-002 hadoop]# 
```
> 对照 集群部署规划 查看003号进程 是否正常启动
``` powershell
[root@corehub-003 hadoop]# jps
18212 SecondaryNameNode
23335 Jps
12654 DataNode
[root@corehub-003 hadoop]# 
```
> 在002服务器启动YARN ResourceManager
``` powershell
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
> 3.集群基本测试
> a.上传文件到集群
> 上传小文件
``` powershell
[root@corehub-001 hadoop]# bin/hdfs dfs -mkdir -p /user/geekparkhub/input
```
``` powershell
[root@corehub-001 hadoop]# bin/hdfs dfs -put wcinput/wc.input /user/geekparkhub/input
```
> 上传大文件
``` powershell
[root@corehub-001 hadoop]# bin/hdfs dfs -put /opt/software/hadoop-2.7.2.tar.gz /user/geekparkhub/input
```

> b.上传文件查看文件存放位置
> 查看HDFS文件存储路径
``` powershell
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
> 1.各个服务组件逐一启动和关闭
> 分别启动/关闭 HDFS组件
`hadoop-daemon.sh start/stop namenode/datanode/secondarynamenode`
> 启动/关闭 YARN
`yarn-daemon.sh start/stop resourcemanager/nodemanager`
> 
> 2.各个模块分开启动和关闭(前提是配置好ssh免登录)常用
> 1.整体启动关闭YARN
`start-dfs.sh / stop-dfs.sh`
> 2.整体启动关闭YARN
`start-yarn.sh / stop-yarn.sh`


#### 集群时间同步
> 时间同步方式:找一台机器作为时间服务器,所有机器与这台集群时间进行定时的同步,比如每隔十分钟,同步一次时间
> 配置时间同步实现步骤
> 1.时间服务配置(必须是root用户)
> 检查ntp是否安装
``` powershell
[root@corehub-002 ~]# rpm -qa|grep ntp
fontpackages-filesystem-1.41-1.1.el6.noarch
ntpdate-4.2.6p5-15.el6.centos.x86_64
ntp-4.2.6p5-15.el6.centos.x86_64
[root@corehub-002 ~]# 
```
> 修改ntp配置文件
`vim /etc/ntp.conf`
> 修改内容如下:
> 修改 (授权`192.168.177.2`-`192.168.177.255`网段上所有的机器可以从这台机器上查询和同步时间)
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

> 修改(集群在局域网中,不使用其他互联网上的时间)
``` powershell
# Use public servers from the pool.ntp.org project.
# Please consider joining the pool (http://www.pool.ntp.org/join.html).
# server 0.centos.pool.ntp.org iburst
# server 1.centos.pool.ntp.org iburst
# server 2.centos.pool.ntp.org iburst
# server 3.centos.pool.ntp.org iburst
```
> 添加(当该节点丢失网络连接,依然可以采用本地时间作为时间服务器为集群中的其他节点提供时间同步)
``` powershell
# 当该节点丢失网络连接,依然可以采用本地时间作为时间服务器为集群中的其他节点提供时间同步
server 127.127.1.0
fudge 127.127.1.0 stratum 10
```
> 修改/etc/sysconfig/ntpd文件
> 让硬件与系统时间同步
`vim /etc/sysconfig/ntpd`
``` powershell
SYNC_HWCLOCK=yes
```
> 重新启动ntpd服务
``` powershell
[root@corehub-002 geek-developer]# service ntpd start
Starting ntpd:                                             [  OK  ]
[root@corehub-002 geek-developer]# service ntpd status
ntpd (pid  2871) is running...
[root@corehub-002 geek-developer]# 
```
> 设置ntpd服务开机自启
``` powershell
[root@corehub-002 geek-developer]# chkconfig ntpd on
[root@corehub-002 geek-developer]# 
```
> 其他机器配置(必须root用户)
> 在其他机器配置10分钟与时间服务器同步一次
> 初步测试
``` powershell
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

> 编写定时任务如下:
``` powershell
[root@corehub-003 hadoop]# crontab -e
```
``` powershell
*/1 * * * * /usr/sbin/ntpdate corehub-002
~                                                                               
~                                                                      
~                                                                               
"/tmp/crontab.phnH6Y" 1L, 42C
```

> 修改任意机器时间
> date -s "2019-7-12 41:55:23"
> 一分钟后查看机器是否与时间度服务器同步
``` powershell
[root@corehub-003 ~]# date -s "2018-11-11 11:11:11"
[root@corehub-003 ~]# date
Sun Nov 11 11:11:12 CST 2018
[root@corehub-003 ~]# date
Sun Feb  3 13:04:23 CST 2019
```

## 6. Hadoop 编译源码
### 前期准备工作
#### 1.centos联网
> 配置centos能够连接外网,linux虚拟机 测试 `ping www.baidu.com` 是否畅通
> 
> 注意:采用root角色编译,减少文件权限出现的问题
#### 2.jar包准备
`hadoop-2.7.2-src.tar.gz` | [快速下载通道](https://archive.apache.org/dist/hadoop/common/hadoop-2.7.2/)
`jdk-8u144-linux-x64.tar.gz`  | [快速下载通道](https://www.oracle.com/technetwork/java/javase/documentation/8u-relnotes-2225394.html)
`apache-ant-1.9.10-bin.tar.gz` (build tool 打包工具)  | [快速下载通道](https://archive.apache.org/dist/ant/binaries/apache-ant-1.9.10-bin.tar.gz)
`apache-maven-3.0.5-bin.tar.gz`  | [快速下载通道](http://archive.apache.org/dist/maven/maven-3/3.0.5/binaries/)
`protobuf-2.5.0.tar.gz` (序列化框架)  | [快速下载通道](https://files.pythonhosted.org/packages/3f/ad/c8221a0778cc04197047f0f6ddee683ef1a0851976a4bd4ad17af19d22ec/protobuf-2.5.0.tar.gz)

### jar包安装
#### maven安装
> 解压tar包到指定目录
``` powershell
[root@corehub-001 software]# tar -zvxf apache-maven-3.0.5-bin.tar.gz -C /opt/module/
```
> 重命名
``` powershell
[root@corehub-001 module]# mv apache-maven-3.0.5 maven
[root@corehub-001 module]# ll
total 16
drwxr-xr-x.  6 root   root  4096 Feb  4  2018 ant
drwxr-xr-x. 15  10011 10011 4096 Jan 31 13:52 hadoop
drwxr-xr-x.  6 root   root  4096 Feb  3 14:54 maven
[root@corehub-001 module]# 
```
> 配置环境变量
``` powershell
[root@corehub-001 ~]# cd /opt/module/maven/
[root@corehub-001 maven]# pwd
/opt/module/maven
[root@corehub-001 maven]# vim /etc/profile
```
``` powershell
##MAVEN_HOME
export MAVEN_HOME=/opt/module/maven
export PATH=$PATH:$MAVEN_HOME/bin
```
``` powershell
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
> 解压tar包到指定目录
``` powershell
[root@corehub-001 software]# tar -zvxf apache-ant-1.9.10-bin.tar.gz -C /opt/module/
```
> 重命名
``` prolog
[root@corehub-001 module]# mv apache-ant-1.9.10 ant
[root@corehub-001 module]# ll
total 8
drwxr-xr-x.  6 root  root  4096 Feb  4  2018 ant
drwxr-xr-x. 15 10011 10011 4096 Jan 31 13:52 hadoop
[root@corehub-001 module]# 
```
> 配置环境变量
``` powershell
[root@corehub-001 ~]# cd /opt/module/ant/
[root@corehub-001 ant]# pwd
/opt/module/ant
[root@corehub-001 ant]# vim /etc/profile
```
``` powershell
##ANT_HOME
export ANT_HOME=/opt/module/ant
export PATH=$PATH:$ANT_HOME/bin
```
``` powershell
[root@corehub-001 ant]# source /etc/profile
[root@corehub-001 ant]# ant -version
Apache Ant(TM) version 1.9.10 compiled on February 3 2018
[root@corehub-001 ant]# 
```
#### 安装glibc-headers 与 g++
``` powershell
yum install glibc-headers
```
``` powershell
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
``` powershell
yum install make
```

``` powershell
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
> 解压tar包到指定目录
``` powershell
[root@corehub-001 software]# tar -zvxf protobuf-2.5.0.tar.gz -C /opt/module/
```
> 重命名
``` powershell
[root@corehub-001 module]# mv protobuf-2.5.0 protobuf
[root@corehub-001 module]# ll
total 16
drwxr-xr-x.  6 root   root  4096 Feb  4  2018 ant
drwxr-xr-x. 15  10011 10011 4096 Jan 31 13:52 hadoop
drwxr-xr-x.  6 root   root  4096 Feb  3 14:54 maven
drwxr-x---.  4 109965  5000 4096 Feb 28  2013 protobuf
[root@corehub-001 module]# 
```
> 配置环境变量
``` powershell
[root@corehub-001 ~]# cd /opt/module/protobuf/
[root@corehub-001 protobuf]# pwd
/opt/module/protobuf
[root@corehub-001 protobuf]# vim /etc/profile
```
``` powershell
##PROTOBUF_HOME
export PROTOBUF_HOME=/opt/module/protobuf
export PATH=$PATH:$PROTOBUF_HOME/bin
```
``` powershell
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
> 1.`高容错性`:数据自动保存多个副本,它通过增加副本的形式,提供容错性.某一个副本丢失以后,它可以自动恢复.
> 
> 2.`适合处理大数据`:
> `数据规模`:能够处理数据规模达到GB,TB,甚至PB级别数据.
> `文件规模`:能够处理百万规模以上的文件数量,数量相当之大.
> 
> 3.`可构建到廉价机器上`,通过多个副本机制,提高可靠性.

> **`缺点`**
> 1.`不适合低延时数据访问`,比如毫秒级的存储数据,是做不到的.
> 
> 2.`无法高效的对大量的小文件进行存储`:存储大量小文件的话,它会占用NameNode大量的内存来存储文件目录和块信息,这样是不可取的,因为NameNode的内存总是有限的.小文件存储的寻址时间会超过读取时间,它违反了HDFS设计目标.
> 
> 3.`不支持并发写入`,文件随机修改.
> 
> 4.`仅支持数据的追加`,不支持文件的随机修改.

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
``` powershell
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
> 1.启动Hadoop集群
> **`sbin/start-dfs.sh`**
> **`sbin/start-yarn.sh`**
> 
> 2.-help 帮助信息
> **`hadoop fs -help rm`**
> 
> 3.-ls 显示目录信息
> **`hadoop fs -ls /`**
> 
> 4.-mkdir 在HDFS上创建目录
> **`hadoop fs -mkdir -p /group/geekparkhub`**
> 
> 5.-moveFromLocal 从本地剪切粘贴到HDFS
> touch test.txt
> **`hadoop fs -moveFromLocal ./test.txt /group/geekparkhub`**
> 
> 6.-appendToFile 追加一个文件到已存在的文件末尾
> touch test001.txt
> vim test001.txt
> 输入 123
> **`hadoop fs -appendToFile ./test001.txt /group/geekparkhub/test.txt`**
> 
> 7.-cat 显示文件内容
> **`hadoop fs -cat /group/geekparkhub/test.txt`**
> 
> 8.-chgrp,-chmod,-chown,linux文件系统中用法一致,修改文件所属权限
> 
> 9.-copyFromLocal 从本地文件系统中拷贝到HDFS中
> **`hadoop fs -copyFromLocal test001.txt /group/geekparkhub/`**
> 
> 10.-copyToLocal 从HDFS上拷贝到本地
> **`hadoop fs -copyToLocal /group/geekparkhub/test.txt ./`**
> 
> 11.-cp 从HDFS路径拷贝到HDFS另一个路径
> **`hadoop fs -cp /group/geekparkhub/test.txt /user/geekparkhub/`**
> 
> 12.-mv 在HDFS目录中移动文件
> **`hadoop fs -mv /group/geekparkhub/test001.txt /user/geekparkhub/`**
> 
> 13.-get 等同于copyToLocal 从HDFS下载文件到本地
> **`hadoop fs -get /group/geekparkhub/test001.txt ./`**
> 
> 14.-getmerge 合并下载多个文件,比如HDFS目录 /log/下有多个文件日志文件,log1,log3,log3
> **`hadoop fs -getmerge /user/geekparkhub/* ./list.txt`**
> 
> 15.-put 等同于copyFromLocal
> **`hadoop fs -put ./list.txt /user/geekparkhub`**
> 
> 16.-tail 显示一个文件的末尾
> **`hadoop fs -tail /group/geekparkhub/test.txt`**
> 
> 17.-rm 删除文件或文件夹
> **`hadoop fs -rm /user/geekparkhub/list.txt`**
> 
> 18.-rmdir 删除空目录
> **`hadoop fs -rmdir /user/testfile/`**
> 
> 19.-du 统计文件夹的大小信息
> **`hadoop fs -du -s -h /`**
> 
> 20.-setrep 设置HDFS中文件的副本数量
> **`hadoop fs -setrep 10 /group/geekparkhub/test.txt`**


### 7.2 HDFS客户端操作(开发重点)
#### HDFS客户端环境准备 以Win版本 为例
##### 1.根据自身电脑操作系统拷贝对应编译后的hadoop jar包到英文路径
##### 2.Win版本 配置HADOOP_HOME环境变量
``` powershell
HADOOP_HOME = D:\J2EE\Hadoop\hadoop
```
##### 3.Win版本 配置Path环境变量
``` powershell
Path = %HADOOP_HOME%\bin
```
##### 4.JetBrains IntelliJ IDEA New Maven Project | 此过程省略

##### 5.创建HDFS客户端
``` java
package com.geekparkhub.hdfs;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.log4j.Logger;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * <p>
 * HDFS 客户端
 */
public class HdfsClient {

    /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(HdfsClient.class);

    public static void main(String[] args) throws IOException, URISyntaxException, InterruptedException {
        /**
         * 1.获取HDFS客户端实例
         *  Obtain an HDFS client instance
         */
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(new URI("hdfs://corehub-001:9000"), conf, "root");

        /**
         * 2.在HDFS中创建路径
         * Create a path in HDFS
         */
        fs.mkdirs(new Path("/hdfstest/files"));

        /**
         * 3.关闭HDFS资源
         * Turn off HDFS resources
         */
        fs.close();

        /**
         * 4.日志打印
         * Log printing
         */
        log.info("测试程序-执行结束!");
    }
}
```
##### 6.查看测试结果

#### HDFS API操作
> 参数优先级
> 参数优先级排序:
> 1.客户端代码中设置的值
> 2.ClassPath下用户自定义配置文件
> 3.服务器默认配置文件

##### HDFS文件上传(测试)
``` java
package com.geekparkhub.hdfs;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.log4j.Logger;
import org.junit.Test;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * <p>
 * HDFS 客户端
 */
public class HdfsClient {

    /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(HdfsClient.class);

    public static void main(String[] args) {
    }
    
	/**
    * 文件上传
    * File Upload
    * @throws URISyntaxException
    * @throws IOException
    * @throws InterruptedException
    */
    @Test
    public void testCopyFromLocalFile() throws URISyntaxException, IOException, InterruptedException {

        /**
         * 1.获取HDFS客户端实例
         *  Obtain an HDFS client instance
         */
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(new URI("hdfs://corehub-001:9000"), conf, "root");

        /**
         * 2.执行上传API
         * Execute the upload API
         */
        fs.copyFromLocalFile(new Path("D:/J2EE/md5/rfc1321.txt"), new Path("/hdfs/client/files/rfc1321.txt"));

        /**
         * 3.关闭数据资源
         * Close data resources
         */
        fs.close();

        /**
         * 4.日志打印
         * Log printing
         */
        log.info("测试程序-文件拷贝执行结束!");
    }
}
```
##### HDFS文件下载
``` java
package com.geekparkhub.hdfs;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.log4j.Logger;
import org.junit.Test;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * <p>
 * HDFS 客户端
 */
public class HdfsClient {

    /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(HdfsClient.class);

    public static void main(String[] args) {
    }

    /**
     * 文件下载
     * file download
     *
     * @throws URISyntaxException
     * @throws IOException
     * @throws InterruptedException
     */
    @Test
    public void testCopyToLocalFile() throws URISyntaxException, IOException, InterruptedException {

        /**
         * 1.获取HDFS客户端实例
         *  Obtain an HDFS client instance
         */
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(new URI("hdfs://corehub-001:9000"), conf, "root");

        /**
         * 2.执行下载API
         * Execute the download API
         */
        fs.copyToLocalFile(new Path("/group/geekparkhub/input/hadoop-2.7.2.tar.gz"), new Path("F:/Demo/hadoop-2.7.2.tar.gz"));

        /**
         * 3.关闭数据资源
         * Close data resources
         */
        fs.close();

        /**
         * 4.日志打印
         * Log printing
         */
        log.info("测试程序-文件下载成功-执行结束!");
    }
}
```
##### HDFS文件夹删除
``` java
package com.geekparkhub.hdfs;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.log4j.Logger;
import org.junit.Test;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * <p>
 * HDFS 客户端
 */
public class HdfsClient {

    /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(HdfsClient.class);

    public static void main(String[] args) {
    }

    @Test
    public void testDelete() throws URISyntaxException, IOException, InterruptedException {

        /**
         * 1.获取HDFS客户端实例
         *  Obtain an HDFS client instance
         */
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(new URI("hdfs://corehub-001:9000"),conf,"root");

        /**
         * 2.执行删除API
         * Execute the download API
         */
        fs.delete(new Path("/hdfs/client/files/001"),true);

        /**
         * 3.关闭数据资源
         * Close data resources
         */
        fs.close();

        /**
         * 4.日志打印
         * Log printing
         */
        log.info("测试程序-删除成功-执行结束!");
    }
}
```
##### HDFS文件名更改
``` java
package com.geekparkhub.hdfs;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;
import org.apache.log4j.Logger;
import org.junit.Test;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * <p>
 * HDFS 客户端
 */
public class HdfsClient {

    /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(HdfsClient.class);

    public static void main(String[] args) {
    }

    /**
     * 文件更名
     * File rename
     *
     * @throws IOException
     * @throws URISyntaxException
     * @throws InterruptedException
     */
    @Test
    public void testReName() throws IOException, URISyntaxException, InterruptedException {

        /**
         * 1.获取HDFS客户端实例
         *  Obtain an HDFS client instance
         */
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(new URI("hdfs://corehub-001:9000"), conf, "root");

        /**
         * 2.执行修改API
         * Execute the modification API
         */
        fs.rename(new Path("/hdfs/client/files/001/test/bootmgr.exe.mui"), new Path("/hdfs/client/files/001/test/hub.exe.mui"));

        /**
         * 3.关闭数据资源
         * Close data resources
         */
        fs.close();

        /**
         * 4.日志打印
         * Log printing
         */
        log.info("测试程序-修改成功-执行结束!");
    }
}
```
##### HDFS文件详情查看
> 查看文件名称,权限,长度,块信息
``` java
package com.geekparkhub.hdfs;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;
import org.apache.log4j.Logger;
import org.junit.Test;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * <p>
 * HDFS 客户端
 */
public class HdfsClient {

    /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(HdfsClient.class);

    public static void main(String[] args) {
    }

    /**
     * 查看文件详情
     * View file details
     *
     * @throws URISyntaxException
     * @throws IOException
     * @throws InterruptedException
     */
    @Test
    public void testListFile() throws URISyntaxException, IOException, InterruptedException {

        /**
         * 1.获取HDFS客户端实例
         *  Obtain an HDFS client instance
         */
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(new URI("hdfs://corehub-001:9000"), conf, "root");

        /**
         * 2.执行查看API
         * Execute view API
         */
        RemoteIterator<LocatedFileStatus> iterator = fs.listFiles(new Path("/"), true);

        while (iterator.hasNext()) {
            LocatedFileStatus fileStatus = iterator.next();
            /**
             * 查看文件名称,权限,长度,块信息
             */
            // 文件名称
            log.info("文件名称：" + fileStatus.getPath().getName());
            // 文件权限
            log.info("文件权限：" + fileStatus.getPermission());
            // 文件长度
            log.info("文件长度：" + fileStatus.getLen());
            // 文件块信息
            BlockLocation[] blockLocation = fileStatus.getBlockLocations();
            for (BlockLocation blockLocations : blockLocation) {
                String[] hosts = blockLocations.getHosts();
                for (String host : hosts) {
                    log.info("块信息：" + host);
                }
                log.info("-------------------------------");
            }
        }

        /**
         * 3.关闭数据资源
         * Close data resources
         */
        fs.close();

        /**
         * 4.日志打印
         * Log printing
         */
        log.info("测试程序-文件查看成功-执行结束!");
    }
}
```
##### HDFS文件和文件夹判断
``` java
package com.geekparkhub.hdfs;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;
import org.apache.log4j.Logger;
import org.junit.Test;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * <p>
 * HDFS 客户端
 */
public class HdfsClient {

    /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(HdfsClient.class);

    public static void main(String[] args) {
    }

    /**
     * 判断文件或文件夹
     *
     * @throws URISyntaxException
     * @throws IOException
     * @throws InterruptedException
     */
    @Test
    public void testListStatus() throws URISyntaxException, IOException, InterruptedException {

        /**
         * 1.获取HDFS客户端实例
         *  Obtain an HDFS client instance
         */
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(new URI("hdfs://corehub-001:9000"), conf, "root");

        /**
         * 2.执行判断API
         * Execution judgment API
         */
        FileStatus[] statuses = fs.listStatus(new Path("/"));
        for (FileStatus status : statuses) {
            if (status.isFile()) {
                // 文件
                log.info("File：" + status.getPath().getName());
            } else {
                // 文件夹
                log.info("File Directory：" + status.getPath().getName());
            }
        }

        /**
         * 3.关闭数据资源
         * Close data resources
         */
        fs.close();

        /**
         * 4.日志打印
         * Log printing
         */
        log.info("测试程序-文件判断成功-执行结束!");
    }
}
```
#### HDFS I/O流操作
> 如自行实现上述API操作,可以采用I/O流方式实现数据上传下载
##### HDFS文件上传
> 需求: 将C:\Windows\Web\4K\Wallpaper\Windows\img0_3840x2160.jpg文件上传到HDFS目录中
``` java
package com.geekparkhub.hdfs;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;
import org.apache.log4j.Logger;
import org.junit.Test;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * <p>
 * HDFS IO
 */
public class HDFSIO {

    /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(HDFSIO.class);

    /**
     * 将C:\Windows\Web\4K\Wallpaper\Windows\img0_3840x2160.jpg文件上传到HDFS目录中
     * Upload the C:\Windows\Web\4 K\Wallpaper\Windows\img 0_3840 x 2160.jpg file to the HDFS directory
     *
     * @throws URISyntaxException
     * @throws IOException
     * @throws InterruptedException
     */
    @Test
    public void putFileToHDFS() throws URISyntaxException, IOException, InterruptedException {

        /**
         * 1.获取HDFS客户端实例
         *  Obtain an HDFS client instance
         */
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(new URI("hdfs://corehub-001:9000"), conf, "root");

        /**
         * 2.获取输入流
         * Get the input stream
         */
        FileInputStream fileInputStream = new FileInputStream(new File("C:/Windows/Web/4K/Wallpaper/Windows/img0_3840x2160.jpg"));

        /**
         * 3.获取输出流
         * Get the output stream
         */
        FSDataOutputStream fsDataOutputStream = fs.create(new Path("/hdfs/client/files/img0_3840x2160.jpg"));

        /**
         * 4.流数据对拷
         * Stream data copy
         */
        IOUtils.copyBytes(fileInputStream, fsDataOutputStream, conf);

        /**
         * 5.关闭数据资源
         * Close data resources
         */
        IOUtils.closeStream(fsDataOutputStream);
        IOUtils.closeStream(fileInputStream);
        fs.close();

        /**
         * 5.日志打印
         * Log printing
         */
        log.info("文件上传成功-程序执行结束!");
    }
}
```
##### HDFS文件下载
> 需求: 从HDFS上下载文件到本地盘符下
``` java
package com.geekparkhub.hdfs;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;
import org.apache.log4j.Logger;
import org.junit.Test;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * <p>
 * HDFS IO
 */
public class HDFSIO {

    /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(HDFSIO.class);

    /**
     * 从HDFS上下载文件到本地盘符下
     * Download files from HDFS to local drive letter
     *
     * @throws URISyntaxException
     * @throws IOException
     * @throws InterruptedException
     */
    @Test
    public void getFileFromHDFS() throws URISyntaxException, IOException, InterruptedException {

        /**
         * 1.获取HDFS客户端实例
         *  Obtain an HDFS client instance
         */
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(new URI("hdfs://corehub-001:9000"), conf, "root");

        /**
         * 2.获取输入流
         * Get the input stream
         */
        FSDataInputStream fsDataInputStream = fs.open(new Path("/hdfs/client/files/img0_3840x2160.jpg"));

        /**
         * 3.获取输出流
         * Get the output stream
         */
        FileOutputStream fileInputStream = new FileOutputStream(new File("d:/Downloads/img0_3840x2160.jpg"));

        /**
         * 4.流数据对拷
         * Stream data copy
         */
        IOUtils.copyBytes(fsDataInputStream, fileInputStream, conf);

        /**
         * 5.关闭数据资源
         * Close data resources
         */
        IOUtils.closeStream(fsDataInputStream);
        IOUtils.closeStream(fileInputStream);
        fs.close();

        /**
         * 5.日志打印
         * Log printing
         */
        log.info("文件下载成功-程序执行结束!");
    }
}
```
##### 定位文件读取
> 需求: 分块读取HDFS上的大文件,比如HDFS目录下的hadoop-2.7.2.tar.gz
``` java
package com.geekparkhub.hdfs;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;
import org.apache.log4j.Logger;
import org.junit.Test;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * <p>
 * HDFS IO
 */
public class HDFSIO {

    /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(HDFSIO.class);

    /**
     * 第一块文件 下载
     * First file download
     *
     * @throws URISyntaxException
     * @throws IOException
     * @throws InterruptedException
     */
    @Test
    public void readFileSeek1() throws URISyntaxException, IOException, InterruptedException {

        /**
         * 1.获取HDFS客户端实例
         *  Obtain an HDFS client instance
         */
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(new URI("hdfs://corehub-001:9000"), conf, "root");

        /**
         * 2.获取输入流
         * Get the input stream
         */
        FSDataInputStream fsDataInputStream = fs.open(new Path("/user/geekparkhub/input/hadoop-2.7.2.tar.gz"));

        /**
         * 3.获取输出流
         * Get the output stream
         */
        FileOutputStream fileInputStream = new FileOutputStream(new File("d:/Downloads/hadoop-2.7.2.tar.gz.part1"));

        /**
         * 4.流数据对拷 只拷贝单块128M
         * Stream data copy Copy only a single block of 128 M
         */
        byte[] bytes = new byte[1024];
        for (int i = 0; i < 1024 * 128; i++) {
            fsDataInputStream.read(bytes);
            fileInputStream.write(bytes);
        }

        /**
         * 5.关闭数据资源
         * Close data resources
         */
        IOUtils.closeStream(fsDataInputStream);
        IOUtils.closeStream(fileInputStream);
        fs.close();

        /**
         * 5.日志打印
         * Log printing
         */
        log.info("第一块文件下载成功-程序执行结束!");
    }

    /**
     * 第二块文件 下载
     * Second file download
     * @throws URISyntaxException
     * @throws IOException
     * @throws InterruptedException
     */
    @Test
    public void readFileSeek2() throws URISyntaxException, IOException, InterruptedException {

        /**
         * 1.获取HDFS客户端实例
         *  Obtain an HDFS client instance
         */
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(new URI("hdfs://corehub-001:9000"), conf, "root");

        /**
         * 2.获取输入流
         * Get the input stream
         */
        FSDataInputStream fsDataInputStream = fs.open(new Path("/user/geekparkhub/input/hadoop-2.7.2.tar.gz"));

        /**
         * 3.设置指定读取起点
         * Set the specified reading start point
         */
        fsDataInputStream.seek(1024 * 1024 * 128);

        /**
         * 4.获取输出流
         * Get the output stream
         */
        FileOutputStream fileInputStream = new FileOutputStream(new File("d:/Downloads/hadoop-2.7.2.tar.gz.part2"));

        /**
         * 5.流数据对拷
         * Stream data copy
         */
        IOUtils.copyBytes(fsDataInputStream, fileInputStream, conf);

        /**
         * 6.关闭数据资源
         * Close data resources
         */
        IOUtils.closeStream(fsDataInputStream);
        IOUtils.closeStream(fileInputStream);
        fs.close();

        /**
         * 7.日志打印
         * Log printing
         */
        log.info("第二块文件下载成功-程序执行结束!");
    }
}
```
> 使用win指令,将part1+part2 数据拼接
``` powershell
D:\Downloads>type hadoop-2.7.2.tar.gz.part2 >> hadoop-2.7.2.tar.gz.part1
```
            
### 7.3 HDFS数据流(面试重点)
#### HDFS写数据流程
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_016.jpg)
##### 剖析文件写入
> 1.客户端通过Distributed File System模块向NameNode请求上传文件,NameNode检查目标文件是否存在,父目录是否存在.
> 2.NameNode返回是否可以上传.
> 3.客户端请求第一个block上传到哪个Datanode服务器.
> 4.NameNode返回3个DataNode节点,分别问dn1,dn2,dn3.
> 5.客户端通过FSDataOutputStream模块请求dh1上传数据,dn1收到请求会继续调用dn2,然后dn2调用dn3,将这个通信管道建立完成.
> 6.dn1,dn2,dn3逐级应答客户端.
> 7.客户端开始想dn1上传第一个block(先从磁盘读取数据放到一个本地内存缓存),以packet为单位,dn1收到一个packet就会传给dn2,dn2传给dn3,dn1每传一个packet会放入一个应答队列等待应答.
> 8.当一个block传输完成之后,客户端再次请求NameNode上传第二个block的服务器(重复执行3-7步骤).

#### HDFS读数据流程
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_018.jpg)
> 1.客户端通过Distributed File System向NameNode请求下载文件,NameNode通过查询元数据,找到文件块所在的DataNode地址.
> 2.挑选一台DataNode(就近原则,然后随机)服务器,请求读取数据.
> 3.DataNode开始传输数据给客户端(从磁盘里面读取数据输入流,以packet为单位来做校验).
> 4.客户端以packet为单位接收,先在本地缓存,然后写入目标文件.

##### 网络拓展-节点距离计算
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_017.jpg)
> 在HDFS写数据的过程中,NameNode会选择距离待上传数据最近距离的DataNode接收数据,那么这个最近距离怎么计算?
> 节点距离:两个节点到达最近的共同祖先的距离总和.

### 7.4 NameNode和SecondayNameNode工作机制(面试重点)
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_019.jpg)

> 第一阶段：NameNode启动
> (1) 第一次启动 NameNode格式化后,创建 fsimage 和 edits 文件,如果不是第一次启动,直接加载编辑日志和镜像文件到内存.
> (2) 客户端对元数据进行增删改的请求.
> (3) NameNode 记录操作日志，更新滚动日志.
> (4) NameNode 在内存中对数据进行增删改查.
> 
> 第二阶段：Secondary NameNode工作
> (1) Secondary NameNode询问NameNode 是否需要 checkpoint,直接带回 NameNode是否检查结果.
> (2) Secondary NameNode 请求执行 checkpoint.
> (3) NameNode 滚动正在写的 edits 日志.
> (4) 将滚动前的编辑日志和镜像文件拷贝到 Secondary NameNode.
> (5) Secondary NameNode 加载编辑日志和镜像文件到内存，并合并.
> (6) 生成新的镜像文件 fsimage.chkpoint.
> (7) 拷贝 fsimage.chkpoint 到 NameNode.
> (8) NameNode 将 fsimage.chkpoint 重新命名成 fsimage.

#### Fsimage和Edits解析
> 1. 概念
> namenode被格式化之后,将在/opt/module/hadoop/data/tmp/dfs/name/current目录中产生如下文件
``` powershell
[root@corehub-001 hadoop]# cd data/tmp/dfs/name/current/
[root@corehub-001 current]# ll
total 3120
-rw-r--r--. 1 root root 1048576 Feb 17 02:14 edits_0000000000000000001-0000000000000000040
-rw-r--r--. 1 root root    1335 Feb 17 19:40 edits_0000000000000000041-0000000000000000061
-rw-r--r--. 1 root root      42 Feb 17 20:40 edits_0000000000000000062-0000000000000000063
-rw-r--r--. 1 root root     280 Feb 17 21:40 edits_0000000000000000064-0000000000000000068
-rw-r--r--. 1 root root      42 Feb 17 22:40 edits_0000000000000000069-0000000000000000070
-rw-r--r--. 1 root root      42 Feb 17 23:40 edits_0000000000000000071-0000000000000000072
-rw-r--r--. 1 root root 1048576 Feb 17 23:40 edits_0000000000000000073-0000000000000000073
-rw-r--r--. 1 root root      42 Feb 19 19:19 edits_0000000000000000074-0000000000000000075
-rw-r--r--. 1 root root 1048576 Feb 19 19:19 edits_inprogress_0000000000000000076
-rw-r--r--. 1 root root    1361 Feb 19 19:18 fsimage_0000000000000000073
-rw-r--r--. 1 root root      62 Feb 19 19:18 fsimage_0000000000000000073.md5
-rw-r--r--. 1 root root    1361 Feb 19 19:19 fsimage_0000000000000000075
-rw-r--r--. 1 root root      62 Feb 19 19:19 fsimage_0000000000000000075.md5
-rw-r--r--. 1 root root       3 Feb 19 19:19 seen_txid
-rw-r--r--. 1 root root     207 Feb 19 19:18 VERSION
```
> 1.Fsimage 文件：HDFS文件系统元数据的一个永久性的检查点,其中包含HDFS文件系统的所有目录和文件idnode的序列化信息.
> 2.Edits 文件：存放HDFS文件系统的所有更新操作的路径,文件系统客户端执行的所有写操作首先会被记录到edits文件中.
> 3.`seen_txid`文件保存的是一个数字,就是最后一个 edits_的数字.
> 4.每次 NameNode启动的时候都会将 fsimage 文件读入内存,并从 00001 开始到seen_txid 中记录的数字依次执行每个 edits 里面的更新操作,保证内存中的元数据信息是最新的、同步的,可以看成 NameNode 启动的时候就将 fsimage 和 edits 文件进行了合并.
> 
> 2 oiv指令 查看 fsimage 文件
> 
> 1.查看 oiv 和 oev 命令
``` powershell
[root@corehub-001 current]$ hdfs
oiv apply the offline fsimage viewer to an fsimage
oev apply the offline edits viewer to an edits file
```
> 2.基本语法
> hdfs oiv -p 文件类型 -i 镜像文件 -o 转换后文件输出路径
> 
> 3.案例实操
``` powershell
[root@corehub-001 current]# ll
total 3120
-rw-r--r--. 1 root root 1048576 Feb 17 02:14 edits_0000000000000000001-0000000000000000040
-rw-r--r--. 1 root root    1335 Feb 17 19:40 edits_0000000000000000041-0000000000000000061
-rw-r--r--. 1 root root      42 Feb 17 20:40 edits_0000000000000000062-0000000000000000063
-rw-r--r--. 1 root root     280 Feb 17 21:40 edits_0000000000000000064-0000000000000000068
-rw-r--r--. 1 root root      42 Feb 17 22:40 edits_0000000000000000069-0000000000000000070
-rw-r--r--. 1 root root      42 Feb 17 23:40 edits_0000000000000000071-0000000000000000072
-rw-r--r--. 1 root root 1048576 Feb 17 23:40 edits_0000000000000000073-0000000000000000073
-rw-r--r--. 1 root root      42 Feb 19 19:19 edits_0000000000000000074-0000000000000000075
-rw-r--r--. 1 root root 1048576 Feb 19 19:19 edits_inprogress_0000000000000000076
-rw-r--r--. 1 root root    1361 Feb 19 19:18 fsimage_0000000000000000073
-rw-r--r--. 1 root root      62 Feb 19 19:18 fsimage_0000000000000000073.md5
-rw-r--r--. 1 root root    1361 Feb 19 19:19 fsimage_0000000000000000075
-rw-r--r--. 1 root root      62 Feb 19 19:19 fsimage_0000000000000000075.md5
-rw-r--r--. 1 root root       3 Feb 19 19:19 seen_txid
-rw-r--r--. 1 root root     207 Feb 19 19:18 VERSION
[root@corehub-001 current]# hdfs oiv -p XML -i fsimage_0000000000000000073 -o fs-073.xml
```
> 将显示的 xml 文件内容拷贝到 eclipse 中创建的 xml 文件中,并格式化。部分显示结果如下.
``` xml
<?xml version="1.0"?>
<fsimage>
    <NameSection>
        <genstampV1>1000</genstampV1>
        <genstampV2>1010</genstampV2>
        <genstampV1Limit>0</genstampV1Limit>
        <lastAllocatedBlockId>1073741834</lastAllocatedBlockId>
        <txid>73</txid>
    </NameSection>
    <INodeSection>
        <lastInodeId>16401</lastInodeId>
        <inode>
            <id>16385</id>
            <type>DIRECTORY</type>
            <name></name>
            <mtime>1550340875095</mtime>
            <permission>root:supergroup:rwxr-xr-x</permission>
            <nsquota>9223372036854775807</nsquota>
            <dsquota>-1</dsquota>
        </inode>
        <inode>
            <id>16386</id>
            <type>DIRECTORY</type>
            <name>user</name>
            <mtime>1550339935918</mtime>
            <permission>root:supergroup:rwxr-xr-x</permission>
            <nsquota>-1</nsquota>
            <dsquota>-1</dsquota>
        </inode>
        <inode>
            <id>16393</id>
            <type>FILE</type>
            <name>wc.input</name>
            <replication>3</replication>
            <mtime>1550340172723</mtime>
            <atime>1550340172398</atime>
            <perferredBlockSize>134217728</perferredBlockSize>
            <permission>root:supergroup:rw-r--r--</permission>
            <blocks>
                <block>
                    <id>1073741826</id>
                    <genstamp>1002</genstamp>
                    <numBytes>196</numBytes>
                </block>
            </blocks>
        </inode>
        <inode>
            <id>16396</id>
            <type>DIRECTORY</type>
            <name>hdfs</name>
            <mtime>1550340875095</mtime>
            <permission>root:supergroup:rwxr-xr-x</permission>
            <nsquota>-1</nsquota>
            <dsquota>-1</dsquota>
        </inode>
    </INodeSection>
    <INodeReferenceSection></INodeReferenceSection>
    <SnapshotSection>
        <snapshotCounter>0</snapshotCounter>
    </SnapshotSection>
    <INodeDirectorySection>
        <directory>
            <parent>16396</parent>
            <inode>16397</inode>
        </directory>
        <directory>
            <parent>16397</parent>
            <inode>16398</inode>
        </directory>
        <directory>
            <parent>16398</parent>
            <inode>16400</inode>
        </directory>
    </INodeDirectorySection>
    <FileUnderConstructionSection></FileUnderConstructionSection>
    <SnapshotDiffSection>
        <diff>
            <inodeid>16385</inodeid>
        </diff>
    </SnapshotDiffSection>
    <SecretManagerSection>
        <currentId>0</currentId>
        <tokenSequenceNumber>0</tokenSequenceNumber>
    </SecretManagerSection>
</fsimage>
```
> 3 oev 查看 edits 文件
> 
> 1.基本语法
> hdfs oev -p 文件类型 -i 编辑日志 -o 转换后文件输出路径
> 
> 2.案例实操
``` powershell
[root@corehub-001 current]# hdfs oev -p XML -i edits_0000000000000000073-0000000000000000073 -o edits-073.xml
```
> 将显示的 xml 文件内容拷贝到 eclipse 中创建的 xml 文件中,并格式化,显示结果如下.
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<EDITS>
  <EDITS_VERSION>-63</EDITS_VERSION>
  <RECORD>
    <OPCODE>OP_START_LOG_SEGMENT</OPCODE>
    <DATA>
      <TXID>73</TXID>
    </DATA>
  </RECORD>
</EDITS>
```
#### checkpoint 时间设置
> 1.通常情况下,SecondaryNameNode每隔一小时执行
> hdfs-default.xml
``` xml
<property>
<name>dfs.namenode.checkpoint.period</name>
<value>3600</value>
</property>
```
> 2.一分钟检查一次操作次数,当操作次数达到1百万时,SecondaryNameNode执行一次
``` xml
<property>
<name>dfs.namenode.checkpoint.txns</name>
<value>1000000</value>
<description>操作动作次数</description>
</property>
<property>
<name>dfs.namenode.checkpoint.check.period</name>
<value>60</value>
<description> 1 分钟检查一次操作次数</description>
</property>
```
#### NameNode 故障处理
> NameNode 故障后，可以采用如下两种方法恢复数据
> 
> 方法一：将 SecondaryNameNode中数据拷贝到NameNode存储数据的目录.
> 1.kill -9 namenode进程
> 
> 2.删除NameNode存储的数据(/opt/module/hadoop/data/tmp/dfs/name)
``` powershell
[root@corehub-001 hadoop]$ rm -rf 
/opt/module/hadoop-2.7.2/data/tmp/dfs/name/*
```
> 3.拷贝SecondaryNameNode中数据到原NameNode存储数据目录
``` powershell
[root@corehub-001 name]$ scp -r root@corehub-003:/opt/module/hadoop/data/tmp/dfs/namesecondary/* ./
```
> 4.重新启动namenode
``` powershell
[root@corehub-001 hadoop]$ sbin/hadoop-daemon.sh start namenode
```

> 方 法 二 ： 使 用 -importCheckpoint选项启动NameNode守护进程,从而将SecondaryNameNode中数据拷贝到 NameNode目录中
> 1.修改 hdfs-site.xml 中的配置信息
``` xml
<property>
 <name>dfs.namenode.checkpoint.period</name>
 <value>120</value>
</property>
<property>
 <name>dfs.namenode.name.dir</name>
 <value>/opt/module/hadoop-2.7.2/data/tmp/dfs/name</value>
</property>
```
> 2.kill -9 namenode 进程
> 3.删除 NameNode存储的数据(/opt/module/hadoop/data/tmp/dfs/name)
``` powershell
[root@corehub-001 hadoop]$ rm -rf /opt/module/hadoop/data/tmp/dfs/name/*
```
> 4.如果 SecondaryNameNode不和 NameNode在一个主机节点上,需要将SecondaryNameNode存储数据的目录拷贝到 NameNode存储数据的平级目录并删除in_use.lock 文件.
``` powershell
[root@corehub-001 dfs]$ scp -r root@corehub-003:/opt/module/hadoop/data/tmp/dfs/namesecondary ./
[root@corehub-001 namesecondary]$ rm -rf in_use.lock
[root@corehub-001 dfs]$ pwd
/opt/module/hadoop-2.7.2/data/tmp/dfs
[root@corehub-001 dfs]$ ls
data name namesecondary
```
> 5.导入检查点数据(等待一会 ctrl+c 结束)
``` powershell
 [root@corehub-001 hadoop]$ bin/hdfs namenode -importCheckpoint
```
> 6.启动 namenode
``` powershell
[root@corehub-001 hadoop]$ sbin/haddaemon.sh start namenode
```

#### 集群安全模式
> 1.概述
> 
> 1.NameNode启动时
> NameNode 启动时,首先将映像文件(fsimage)入内存,并执行编辑日志(edits)的各项操作,一旦在内存中成功建立文件系统元数据的映像,则创建一个新的(fsimage)文件和一个空的编辑日志,此时,NameNode开始监听DataNode请求,但是此刻,NameNode运行在安全模式,即NameNode的文件系统对于客户端来说是只读的.
> 
> 2.DataNode启动时
> 系统中的数据块的位置并不是由NameNode维护的,而是以块列表的形式存储在DataNode中,在系统的正常操作期间,NameNode会在内存中保留所有块位置的映射信息,在安全模式下,各个DataNode会向NameNode发送最新的块列表信息,NameNode了解到足够多的块位置信息之后,即可高效运行文件系统。
> 
> 3.安全模式退出判断
> 如果满足"最小副本条件",NameNode会在30秒钟之后就退出安全模式,所谓的最小副本条件指的是在整个文件系统中 99.9%的块满足最小副本级别(默认值 ：dfs.replication.min=1),在启动一个刚刚格式化的 HDFS集群时,因为系统中还没有任何块,所以NameNode不会进入安全模式.

> 2.基本语法
> 集群处于安全模式,不能执行重要操作(写操作),群启动完成后,自动退出安全模式。
> 查看安全模式状态
``` powershell
[root@corehub-001 hadoop]# bin/hdfs dfsadmin -safemode get
Safe mode is OFF
[root@corehub-001 hadoop]# 
```
> 进入安全模式状态
``` powershell
[root@corehub-001 hadoop]# bin/hdfs dfsadmin -safemode enter
Safe mode is ON
[root@corehub-001 hadoop]# 
```
> 离开安全模式状态
``` powershell
[root@corehub-001 hadoop]# bin/hdfs dfsadmin -safemode  leave
Safe mode is OFF
[root@corehub-001 hadoop]# 
```
> 等待安全模式状态
``` powershell
[root@corehub-001 hadoop]# bin/hdfs dfsadmin -safemode wait
```

#### NameNode 多目录配置
> 1.NameNode的本地目录可以配置成多个,且每个目录存放内容相同,增加了可靠性.
> 2.具体配置如下:
> 在hdfs-site.xml文件中增加如下内容
``` xml
<property>
 <name>dfs.namenode.name.dir</name>
 <value>file:///${hadoop.tmp.dir}/dfs/name1,file:///${hadoop.tmp.dir}/dfs/name2</value>
</property>
```
> 3.停止集群,删除 data 和 logs 中所有数据
``` powershell
[root@corehub-001 hadoop]$ rm -rf data/ logs/
[root@corehub-002 hadoop]$ rm -rf data/ logs/
[root@corehub-003 hadoop]$ rm -rf data/ logs/
```
> 4.格式化集群并启动.
``` powershell
[root@corehub-001 hadoop]$ bin/hdfs namenode –format
[root@corehub-001 hadoop]$ sbin/start-dfs.sh
```
> 5.查看结果
``` powershell
[root@corehub-001 dfs]$ ll
总用量 12
drwx------. 3 root root 4096 02 月 11 08:03 data
drwxrwxr-x. 3 root root 4096 02 月 11 08:03 name1
drwxrwxr-x. 3 root root 4096 02 月 11 08:03 nam
```

### 7.5 DataNode(面试开发重点)
#### DataNode工作机制
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_020.jpg)

> 1.一个数据块在DataNode上以文件形式存储在磁盘上,包括两个文件,一个是数据本身,一个是元数据包括数据块的长度,块数据的校验和,以及时间戳.
> 
> 2.DataNode启动后向NameNode注册,通过后,周期性(1 小时)向NameNode上报所有的块信息.
> 
> 3.心跳是每3秒一次,心跳返回结果带有NameNode给该DataNode的命令如复制块数据到另一台机器,或删除某个数据块。如果超过10分钟没有收到某个DataNode 的心跳,则认为该节点不可用.
> 
> 4.集群运行中可以安全加入和退出一些机器.

#### 服役新数据节点
> 随着公司业务的增长,数据量越来越大,原有的数据节点的容量已经不能满足存储数据的需求,需要在原有集群基础上动态添加新的数据节点.
> 
> 1.环境准备
> (1) 克隆一台虚拟机
> (2) 修改ip地址和主机名称
> (3) 修改xsync文件,增加新增节点的ssh无密登录配置
> (4) 删除原来 HDFS 文件系统留存的文件/opt/module/hadoop/data
> 
> 2.服役新节点具体步骤
> (1) 在namenode的/opt/module/hadoop/etc/hadoop目录下创建 dfs.hosts 文件
``` powershell
[root@corehub-004 hadoop]$ pwd
/opt/module/hadoop/etc/hadoop
[root@corehub-004 hadoop]$ touch dfs.hosts
[root@corehub-004 hadoop]$ vi dfs.hosts
```
> 添加如下主机名称（包含新服役的节点）
> corehub-001
> corehub-002
> corehub-003
> corehub-004

> (2) 在namenode的hdfs-site.xml配置文件中增加dfs.hosts属性
``` xml
<property>
<name>dfs.hosts</name>
 <value>/opt/module/hadoop/etc/hadoop/dfs.hosts</value>
</property>
```

> (3) 刷新 namenode
``` powershell
[root@corehub-001 hadoop]$ hdfs dfsadmin -refreshNodes Refresh nodes successful
```

> (4) 更新 resourcemanager 节点
``` powershell
[root@corehub-001 hadoop$ yarn rmadmin -refreshNodes
19/02/19 14:17:11 INFO client.RMProxy: Connecting to ResourceManager at corehub-003/192.168.1.103:8033
```

> (5) 在 NameNode 的 slaves 文件中增加新主机名称
> 增加 004
> corehub-001
> corehub-002
> corehub-003
> corehub-004

> (6) 单独命令启动新的数据节点和节点管理器
``` powershell
[root@corehub-004 hadoop]$ sbin/hadoop-daemon.sh start datanode
starting datanode, logging to 
/opt/module/hadoop/logs/hadoop-atguigu-datanode-corehub-004.out
[root@corehub-004 hadoop]$ sbin/yarn-daemon.sh start nodemanager
starting nodemanager, logging to 
/opt/module/hadoop/logs/yarn-atguigu-nodemanager-corehub-004.out
```
> (7) 在 web 浏览器上检查是否 ok
> 如果数据不均衡,可以用命令实现集群的再平衡
``` powershell
[root@corehub-001 sbin]$ ./start-balancer.sh
starting balancer, logging to 
/opt/module/hadoop/logs/hadoop-atguigu-balancer-corehub-001.out
Time Stamp Iteration# Bytes Already Moved Bytes Left To Move 
Bytes Being Moved
```

#### 退役旧数据节点
> 1.在 namenode 的/opt/module/hadoop/etc/hadoop 目录下创建 dfs.hosts.ex
``` powershell
[root@corehub-001 hadoop]$ pwd
/opt/module/hadoop/etc/hadoop
[root@corehub-001 hadoop]$ touch dfs.hosts.exclude
[root@corehub-001 hadoop]$ vi dfs.hosts.exclude
```
> 添加如下主机名称 (要退役的节点)
> corehub-004
> 2.在namenode的hdfs-site.xml 配置文件中增加 dfs.hosts.exclude 属性
``` xml
<property>
<name>dfs.hosts.exclude</name>
 <value>/opt/module/hadoop/etc/hadoop/dfs.hosts.exclude</value>
</property>
```
> 3.刷新namenode、刷新 resourcemanager
``` powershell
[root@corehub-001 hadoop]$ hdfs dfsadmin -refreshNodes Refresh nodes successful
[root@corehub-001 hadoop]$ yarn rmadmin -refreshNodes
19/02/19 14:55:56 INFO client.RMProxy: Connecting to ResourceManager at 
corehub-001/192.168.1.103:8033
```

> 4.检查 web 浏览器,退役节点的状态为 decommission in progress(退役中)说明数据节点正在复制块到其他节点.
> 
> 5.等待退役节点状态为 decommissioned(所有块已经复制完成)停止该节点及节点资源管理器。注意：如果副本数是3,服役的节点小于等于3,是不能退役成功的,需要修改副本数后才能退役
``` powershell
[root@corehub-004 hadoop]$ sbin/hadoop-daemon.sh stop datanode
stopping datanode
[root@corehub-004 hadoop]$ sbin/yarn-daemon.sh stop nodemanager
stopping nodemanager
```
> 6.从include文件中删除退役节点,再运行刷新节点的命令
> (1) 从namenode的dfs.hosts文件中删除退役节点corehub-004
> corehub-001
> corehub-002
> corehub-003
> 
> (2) 刷新 namenode,刷新 resourcemanager
``` powershell
[root@corehub-001 hadoop]$ hdfs dfsadmin -refreshNodes
Refresh nodes successful
[root@corehub-001 hadoop]$ yarn rmadmin -refreshNodes
19/02/19 14:55:56 INFO client.RMProxy: Connecting to ResourceManager at 
corehub-002/192.168.1.103:8033
```
> 7.从 namenode的slave文件中删除退役节点corehub-004
> corehub-001
> corehub-002
> corehub-003
> 
> 8.如果数据不均衡,可以用命令实现集群的再平衡
``` powershell
[root@corehub-001 hadoop]$ sbin/start-balancer.sh 
starting balancer, logging to 
/opt/module/hadoop/logs/hadoop-atguigu-balancer-corehub-001.out
Time Stamp Iteration# Bytes Already Moved Bytes Left To Move 
Bytes Being Moved
```

#### DataNode多目录配置
> 1.datanode也可以配置成多个目录,每个目录存储的数据不一样, 即:数据不是副本.
> 
> 2.具体配置如下：
> hdfs-site.xml
``` xml
<property>
<name>dfs.datanode.data.dir</name>
<value>file:///${hadoop.tmp.dir}/dfs/data1,file:///${hadoop.tmp.dir}/dfs/data2</value>
</property>
```


### 7.6 HDFS 2.X新特性
#### 集群间数据拷贝
> 1.scp实现两个远程主机之间文件复制
> 推 push
``` powershell
scp -r hello.txt root@corehub-002:/user/geekparkhub/hello.txt
```
> 拉取 pull
``` powershell
scp -r root@corehub-002:/user/geekparkhub/hello.txt /hello.txt
```
> 2.采用distcp指令 实现两个hadoop集群之间递归数据复制
``` powershell
bin/hadoop distcp hdfs://corehub-001:9000/user/geekparkhub/hello.txt hdfs://corehub-002:9000/user/geekparkhub/hello.txt
```
#### Hadoop存档
> 小文件存档
> 
> 1.HDFS存储小文件弊端
> 每个文件均按块储存,每个块的元数据在NameNode的内存中,因此HDFS存储小文件会非常低效,因为大量的小文件会耗尽NameNode中的大部分内存,但注意,储存小文件所需要的磁盘容量和数据块的大小无关,例如,一个1MB的文件设置为128MB的块存储,实际使用的是1MB的磁盘空间,而不是128MB.
> 
> 2.解决存储小文件办法之一
> HDFS存档文件或HAR文件,是一个更高效的文件存档工具,它将文件存入HDFS块,在减少NameNode内存使用的同时,允许对文件进行透明访问,具体说来,HDFS存档文件对内还是一个一个独立文件,对NameNode而言却是一个整体,减少了NameNode的内存.
> 
> 3.案例实操
> 归档文件
> 将/user/geekparkhub/input目录里面的所有文件归档成一个叫 myhar.har 的归档文件,并把归档后文件存储到/user/geekparkhub/output路径下
``` powershell
[root@corehub-001 hadoop]# hadoop archive -archiveName input.har -p /user/geekparkhub/input /user/geekparkhub/output
19/02/20 00:21:28 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
19/02/20 00:21:30 INFO client.RMProxy: Connecting to ResourceManager at corehub-002/192.168.152.135:8032
19/02/20 00:21:33 INFO client.RMProxy: Connecting to ResourceManager at corehub-002/192.168.152.135:8032
19/02/20 00:21:33 INFO client.RMProxy: Connecting to ResourceManager at corehub-002/192.168.152.135:8032
19/02/20 00:21:33 INFO mapreduce.JobSubmitter: number of splits:1
19/02/20 00:21:34 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1550666045505_0001
19/02/20 00:21:35 INFO impl.YarnClientImpl: Submitted application application_1550666045505_0001
19/02/20 00:21:35 INFO mapreduce.Job: The url to track the job: http://corehub-002:8088/proxy/application_1550666045505_0001/
19/02/20 00:21:35 INFO mapreduce.Job: Running job: job_1550666045505_0001
19/02/20 00:21:53 INFO mapreduce.Job: Job job_1550666045505_0001 running in uber mode : false
19/02/20 00:21:53 INFO mapreduce.Job:  map 0% reduce 0%
19/02/20 00:22:07 INFO mapreduce.Job:  map 32% reduce 0%
19/02/20 00:22:28 INFO mapreduce.Job:  map 43% reduce 0%
19/02/20 00:22:57 INFO mapreduce.Job:  map 55% reduce 0%
19/02/20 00:23:30 INFO mapreduce.Job:  map 100% reduce 0%
19/02/20 00:23:41 INFO mapreduce.Job:  map 100% reduce 100%
19/02/20 00:23:41 INFO mapreduce.Job: Job job_1550666045505_0001 completed successfully
19/02/20 00:23:41 INFO mapreduce.Job: Counters: 49
        File System Counters
                FILE: Number of bytes read=535
                FILE: Number of bytes written=238807
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=585985943
                HDFS: Number of bytes written=585985840
                HDFS: Number of read operations=21
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=7
        Job Counters 
                Launched map tasks=1
                Launched reduce tasks=1
                Other local map tasks=1
                Total time spent by all maps in occupied slots (ms)=94659
                Total time spent by all reduces in occupied slots (ms)=7959
                Total time spent by all map tasks (ms)=94659
                Total time spent by all reduce tasks (ms)=7959
                Total vcore-milliseconds taken by all map tasks=94659
                Total vcore-milliseconds taken by all reduce tasks=7959
                Total megabyte-milliseconds taken by all map tasks=96930816
                Total megabyte-milliseconds taken by all reduce tasks=8150016
        Map-Reduce Framework
                Map input records=5
                Map output records=5
                Map output bytes=518
                Map output materialized bytes=535
                Input split bytes=116
                Combine input records=0
                Combine output records=0
                Reduce input groups=5
                Reduce shuffle bytes=535
                Reduce input records=5
                Reduce output records=0
                Spilled Records=10
                Shuffled Maps =1
                Failed Shuffles=0
                Merged Map outputs=1
                GC time elapsed (ms)=1297
                CPU time spent (ms)=15680
                Physical memory (bytes) snapshot=414289920
                Virtual memory (bytes) snapshot=4127817728
                Total committed heap usage (bytes)=251527168
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters 
                Bytes Read=507
        File Output Format Counters 
                Bytes Written=0
[root@corehub-001 hadoop]# 
```
> 解析查看归档
``` powershell
[root@corehub-001 hadoop]# hadoop fs -ls -R har:///user/geekparkhub/output/input.har
19/02/20 00:28:03 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
-rw-r--r--   3 root supergroup  212046774 2019-02-14 17:33 har:///user/geekparkhub/output/input.har/hadoop-2.7.2.tar.gz
-rw-r--r--   3 root supergroup  189815615 2019-02-14 17:34 har:///user/geekparkhub/output/input.har/jdk-8u162-linux-x64.tar.gz
-rw-r--r--   3 root supergroup  184122460 2019-02-14 17:35 har:///user/geekparkhub/output/input.har/mysql-5.5.35-linux2.6-x86_64.tar.gz
-rw-r--r--   3 root supergroup        471 2019-02-14 17:32 har:///user/geekparkhub/output/input.har/wc.input
[root@corehub-001 hadoop]# 
```
#### 回收站
> 开启回收站功能,可以将删除的文件在不超时的情况下,恢复元数据,起到防止误删除,备份等作用.
> 
> 1.回收站参数设置及工作机制
> 开启回收站功能参数说明
> 1.默认值 fs.trash.interval=0    0 表示禁用回收站,可以设置删除文件的存活时间.
> 2.默认值 fs.trash.checkpoint.interval=0,检查回收站的间隔时间
> 如果该值为 0,则该值设置和 fs.trash.interval 的参数值相等,要求 fs.trash.checkpoint.interval<=fs.trash.interval
> 2.启用回收站
> 修改core-site.xml 配置垃圾回收时间为1分钟
``` xml
<property>
	<name>fs.trash.interval</name>
	<value>1</value>
</property>
```
> 3.查看回收站
> 回收站在集群中路径: /user/geekparkhub/.Trash/ .....
> 
> 4.修改访问垃圾回收站用户名称
> 进入垃圾回收站用户名称,默认是dr.who 修改为root用户
> 修改core-site.xml
``` xml
<property>
	<name>hadoop.http.staticuser.user</name>
	<value>root</value>
</property>
```
> 5.通过程序删除的文件不会经过回收站,需要调用moveToTrash()才进入回收站
``` java
Trash trash = New Trash(conf);
trash.moveToTrash(path);
```
> 6.恢复回收站数据
``` powershell
hadoop fs -mv /user/geekparkhub/.Trash/Current/user/geekparkhub/input /user/geekparkhub/input
```
> 7.清空回收站
``` powershell
hadoop fs -expunge
```

#### 快照管理
> 快照相当于对目录做一个备份,并不会立即复制所有文件,而是指向同一个文件,当写入发生时,才会产生新文件.
> 
> 1.基本语法
> (1) `hdfs dfsadmin -allowSnapshot 路径` (功能描述：开启指定目录的快照功能)
> (2) `hdfs dfsadmin -disallowSnapshot 路径` (功能描述：禁用指定目录的快照功能,默认是禁用)
> (3) `hdfs dfs -createSnapshot 路径` (功能描述：对目录创建快照)
> (4) `hdfs dfs -createSnapshot 路径 名称` (功能描述：指定名称创建快照)
> (5) `hdfs dfs -renameSnapshot 路径 旧名称 新名称` (功能描述：重命名快照)
> (6) `hdfs lsSnapshottableDir` (功能描述：列出当前用户所有可快照目录)
> (7) `hdfs snapshotDiff 路径 1 路径 2` (功能描述：比较两个快照目录的不同之处)
> (8) `hdfs dfs -deleteSnapshot <path> <snapshotName>` (功能描述：删除快照)

### 7.7 MapReduce 概述
#### MapReduce 定义
> MapReduce是一个分布式运算程序的编程框架,是用户开发''基于Hadoop的数据分析应用''的核心框架.
> 
> MapReduce核心功能是将用户编写的业务逻辑代码和自带默认组件整合成一个完整的分布式运算程序,并发运行在一个Hadoop集群上.
> 
#### MapReduce 优缺点
> `优点`
> 
> MapReduce 易于编程
> 它简单的实现一些接口,就可以完成一个分布式程序,这个分布式程序可以以分布到大量廉价的PC机器上运行,也就是说一个分布式程序,跟写一个简单的串行程序是一模一样的,就是因为这个特点使得MapReduce编程变得非常流行.
> 
> 良好的扩展性
> 当计算资源不能得到满足的时候,可以通过简单的增加机器来扩展它的计算能力.
> 
> 高容错性
> MapReduce设计的初衷就是使用程序能够部署在廉价的PC机器上,这就要求它具有很高的容错性,比如其中一台机器宕机了,它可以把上面的计算任务转移到另一个节点上运行,不至于这个任务运行失败,而且这个程序不需要人工参与,而完全是由Hadoop内部完成.
> 
> 适合PB级别以上海量数据的离线处理
> 可是实现上千台服务器集群并发工作,提升数据处理能力.
> 
> `缺点`
>  
> 不擅长 实时计算
> MapReduce无法向MYSQL一样,在毫秒或秒级别内返回结果.
> 
> 不擅长 流式计算
> 流式计算的输入数据是动态的,而MapReduce的输入数据集是静态的,不能动态变化,这是因为MapReduce自身的设计特点决定了数据源必须是静态的.
>  
> 不擅长 DAG (有向图计算)
> 多个应用程序存在依赖关系,后一个应用程序的输入为前一个的输出,在这种情况下,MapReduce并不是不能做,而是使用后,每个MaoReduce作业的输出结果都会写入到磁盘,会造成大量的磁盘I/O,导致性能非常的低.

#### MapReduce 核心编程思想
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_021.jpg)

> 1.分布式的运算程序往往需要分成至少2个阶段.
> 
> 2.第一个阶段的Maptask并发实例,完全并行运行,互不相干.
> 
> 3.第二个阶段的Reduce task并发实例互不相干,但是他们的数据依赖于上一个阶段的所有MapTask并发实例的输出.
> 
> 4.MapReduce编程模型只能包含一个Map阶段和一个Reduce阶段,如果用户的业务逻辑非常复杂,那就只能多个MapReduce程序,串行运行.

#### MapReduce 进程
> 一个完整的MapReduce程序在分布式运行时有三大实例进程
> MrAppMaster 负责整个程序的过程调度及状态协调.
> MapTask 负责Map阶段的整个数据处理流程.
> ReduceTask 负责Reduce阶段的整个数据处理流程.

#### WordCount 官方源码
> 采用反编译工具编译源码,发现WordCount案例有Map类,Reduce类和驱动类,且数据的类型是Hadoop自身封装的序列化类型.

#### 常用数据库 序列化类型
> 常用数据类型对应 Hadoop数据序列化类型
| Java数据类型 | Hadoop Writable |
| :--------: | :--------:| 
| boolean    |   BooleanWritable |
| byte    |   ByteWritable | 
| int    |   IntWritable | 
| float    |   FloatWritable | 
| long    |   LongWritable | 
| double    |   DoubleWritable | 
| `String`    |   `Text` | 
| map    |   MapWritable | 
| array    |   ArrayWritable | 

#### MapReduce 编程范式
> 开发者编写程序分成三个部分 : **`Mapper`** / **`Reduce`** / **`Driver`**
> 
> **`Mapper阶段`**
> 1.开发者自定义的Mapper要继承自己的父类.
> 2.Mapper的输入数据是K/V(键值对)的形式,(K/V的类型可以自定义).
> 3.Mapper中的业务逻辑写在map()方法中.
> 4.Mapper的输出数据是K/V(键值对)的形式,(K/V的类型可以自定义).
> 5.map()方法(MapTask进程)对每一个<K,V>调用一次.
> 
> **`Reduce阶段`**
> 1.开发者自定义的Reducer要继承自己的父类.
> 2.Reducer的输入数据类型对应Mapper的输出数据类型,也就是K/V.
> 3.Reducer的业务逻辑写在reduce()方法中.
> 4.ReduceTask进程对每一组相同的K的<K,V>组调用一次reduce()方法.
> 
> **`Driver阶段`**
> 相当于Yarn集群的客户端,用于提交开发者整个程序到Yarn集群,提交的是封装了MapReduce程序相关运行参数的job对象.

#### WordCount 案例实操
##### 1. 案例需求 : 在给定的文本文件中统计输出每一个单词出现的次数.
##### 2. 创建demo.txt 输入数据源文件
##### 3. 编写 期望输出数据,例如
> geek geek
> geekparkhub
> hackerparkhub hackerparkhub hackerparkhub hackerparkhub hackerparkhub
> hadoop hadoop hadoop
> test
> helloworld helloworld
> 
##### 4. 需求分析
> 按照MapReduce编程规范,分别编写Mapper,Reducer,Driver,如图所示
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_022.jpg)

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_023.jpg)

##### 5. JetBrains IntelliJ IDEA New Maven Project | 此过程省略
##### 6. 配置 maven pom.xml文件
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.geekparkhub.mapreduce</groupId>
    <artifactId>mapreduce</artifactId>
    <version>1.0-SNAPSHOT</version>

    <dependencies>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-core</artifactId>
            <version>2.8.2</version>
        </dependency>
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-common</artifactId>
            <version>2.7.2</version>
        </dependency>
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-client</artifactId>
            <version>2.7.2</version>
        </dependency>
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-hdfs</artifactId>
            <version>2.7.2</version>
        </dependency>
    </dependencies>
</project>
```
##### 7. 配置 log4j.properties文件
``` prolog
log4j.rootLogger=INFO, stdout
log4j.appender.stdout=org.apache.log4j.ConsoleAppender
log4j.appender.stdout.layout=org.apache.log4j.PatternLayout
log4j.appender.stdout.layout.ConversionPattern=%d %p [%c] - %m%n
log4j.appender.logfile=org.apache.log4j.FileAppender
log4j.appender.logfile.File=target/corehub.log
log4j.appender.logfile.layout=org.apache.log4j.PatternLayout
log4j.appender.logfile.layout.ConversionPattern=%d %p [%c] - %m%n
```
##### 8. 创建 Map阶段WordcountMapper.class
``` java
package com.geekparkhub.hadoop.mapreduce;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * <p>
 * Map 阶段
 * <p>
 * KEYIN 输入数据的key
 * VALUEIN 输入数据的value
 * KEYOUT 输出数据的key
 * VALUEOUT 输出数据的value
 * @author system
 */

public class WordcountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {

    Text k = new Text();
    IntWritable v = new IntWritable(1);

    /**
     * Rewrite the map() method
     * 重写map()方法
     *
     * @param key
     * @param value
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        /**
         * 1. Get the first row of data, assuming the data is: geek geek
         * 1. 获取第一行数据,假设数据是:geek geek
         */
        String line = value.toString();

        /**
         * 2. Cutting data
         * 2. 切割空格数据
         */
        String[] words = line.split(" ");

        /**
         * 3. Loop through the data
         * 3. 循环遍历数据
         */
        for (String word : words) {
            k.set(word);
            context.write(k, v);
        }
    }
}
```
##### 9. 创建 Reduce阶段WordcountReducer.class
``` java
package com.geekparkhub.hadoop.mapreduce;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * <p>
 * Reducer 阶段
 * <p>
 * KEYIN 既是map阶段输出的key
 * VALUEIN 既是map阶段输出的value
 * @author system
 */

public class WordcountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

    /**
     * Rewrite the reduce() method
     * 重写reduce()方法
     *
     * @param key
     * @param values
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
        IntWritable v = new IntWritable();
        /**
         * 1. Accumulate summation
         * 1. 累加求和
         */
        int sum = 0;
        for (IntWritable value : values) {
            sum += value.get();
        }
        v.set(sum);

        /**
         * 2. Output data
         * 2. 输出数据
         */
        context.write(key, v);
    }
}
```
##### 10. 创建 Driver阶段WordcountDriver.class
``` java
package com.geekparkhub.hadoop.mapreduce;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.log4j.Logger;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * <p>
 * Driver 阶段
 *
 * @author system
 */

public class WordcountDriver {

    /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(WordcountDriver.class);

    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {

        /**
         * 1. Get the Job object
         * 1. 获取Job对象
         */
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf);

        /**
         * 2. Set the jar storage location
         * 2. 设置jar存储位置
         */
        job.setJarByClass(WordcountDriver.class);

        /**
         * 3. Associate Map and Reduce classes
         * 3. 关联Map和Reduce类
         */
        job.setMapperClass(WordcountMapper.class);
        job.setReducerClass(WordcountReducer.class);

        /**
         * 4. Set the key and value types of the output data in the Mapper stage.
         * 4. 设置Mapper阶段输出数据的key与value类型
         */
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(IntWritable.class);

        /**
         * 5. Set the key and value types for the final data output
         * 5. 设置最终数据输出的key与value类型
         */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        /**
         * 6. Set the input path and output path
         * 6. 设置输入路径和输出路径
         */
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         * 7. Submit the Job
         * 7. 提交Job
         */
        boolean result = job.waitForCompletion(true);

        /**
         * 8. Log printing
         * 8. 日志打印
         */
        System.exit(result ? 0 : 1);
    }
}
```

##### 11. 运行结果
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_024.jpg)

``` powershell
bogon:resources system$ ls -ll
total 48
drwxrwxrwx  1 system  staff  8192  3  2 17:00 input
-rwxrwxrwx  1 system  staff   436  1 21 22:15 log4j.properties
drwxrwxrwx  1 system  staff  8192  3  2 17:21 output
bogon:resources system$ cd output/
._SUCCESS.crc      _SUCCESS           
.part-r-00000.crc  part-r-00000       
bogon:resources system$ cat output/part-r-00000
geek	2
geekparkhub	1
hackerparkhub	5
hadoop	3
helloworld	2
test	1
bogon:resources system$ 
```

##### 12.集群测试 WordCount
###### 在中pom.xml添加依赖,使用maven install 将WordCount程序打包成jar包
``` xml
<build> 
  <plugins> 
    <plugin> 
      <artifactId>maven-compiler-plugin</artifactId>  
      <version>2.3.2</version>  
      <configuration> 
        <source>1.8</source>  
        <target>1.8</target> 
      </configuration> 
    </plugin>  
    <plugin> 
      <artifactId>maven-assembly-plugin</artifactId>  
      <configuration> 
        <descriptorRefs> 
          <descriptorRef>jar-with-dependencies</descriptorRef> 
        </descriptorRefs>  
        <archive> 
          <manifest> 
          <mainClass>com.geekparkhub.hadoop.mapreduce.WordcountDriver</mainClass> 
          </manifest> 
        </archive> 
      </configuration>  
      <executions> 
        <execution> 
          <id>make-assembly</id>  
          <phase>package</phase>  
          <goals> 
            <goal>single</goal> 
          </goals> 
        </execution> 
      </executions> 
    </plugin> 
  </plugins> 
</build>
```

###### 运行WordCount jar包程序
``` powershell
[root@systemhub511 hadoop]# hadoop jar mapreduce.jar com.geekparkhub.hadoop.mapreduce.WordcountDriver /user/geekparkhub/input /user/geekparkhub/output
19/03/04 21:12:56 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
19/03/04 21:12:57 INFO client.RMProxy: Connecting to ResourceManager at systemhub611/172.16.168.131:8032
19/03/04 21:12:57 WARN mapreduce.JobResourceUploader: Hadoop command-line option parsing not performed. Implement the Tool interface and execute your application with ToolRunner to remedy this.
19/03/04 21:12:58 INFO input.FileInputFormat: Total input paths to process : 1
19/03/04 21:12:58 INFO mapreduce.JobSubmitter: number of splits:1
19/03/04 21:12:58 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1551704437826_0003
19/03/04 21:12:58 INFO impl.YarnClientImpl: Submitted application application_1551704437826_0003
19/03/04 21:12:58 INFO mapreduce.Job: The url to track the job: http://systemhub611:8088/proxy/application_1551704437826_0003/
19/03/04 21:12:58 INFO mapreduce.Job: Running job: job_1551704437826_0003
19/03/04 21:13:08 INFO mapreduce.Job: Job job_1551704437826_0003 running in uber mode : false
19/03/04 21:13:08 INFO mapreduce.Job:  map 0% reduce 0%
19/03/04 21:13:14 INFO mapreduce.Job:  map 100% reduce 0%
19/03/04 21:13:22 INFO mapreduce.Job:  map 100% reduce 100%
19/03/04 21:13:22 INFO mapreduce.Job: Job job_1551704437826_0003 completed successfully
19/03/04 21:13:22 INFO mapreduce.Job: Counters: 49
        File System Counters
                FILE: Number of bytes read=230
                FILE: Number of bytes written=235407
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=261
                HDFS: Number of bytes written=66
                HDFS: Number of read operations=6
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
        Job Counters 
                Launched map tasks=1
                Launched reduce tasks=1
                Data-local map tasks=1
                Total time spent by all maps in occupied slots (ms)=3817
                Total time spent by all reduces in occupied slots (ms)=4512
                Total time spent by all map tasks (ms)=3817
                Total time spent by all reduce tasks (ms)=4512
                Total vcore-milliseconds taken by all map tasks=3817
                Total vcore-milliseconds taken by all reduce tasks=4512
                Total megabyte-milliseconds taken by all map tasks=3908608
                Total megabyte-milliseconds taken by all reduce tasks=4620288
        Map-Reduce Framework
                Map input records=6
                Map output records=14
                Map output bytes=196
                Map output materialized bytes=230
                Input split bytes=121
                Combine input records=0
                Combine output records=0
                Reduce input groups=6
                Reduce shuffle bytes=230
                Reduce input records=14
                Reduce output records=6
                Spilled Records=28
                Shuffled Maps =1
                Failed Shuffles=0
                Merged Map outputs=1
                GC time elapsed (ms)=161
                CPU time spent (ms)=1130
                Physical memory (bytes) snapshot=289771520
                Virtual memory (bytes) snapshot=4118065152
                Total committed heap usage (bytes)=139399168
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters 
                Bytes Read=140
        File Output Format Counters 
                Bytes Written=66
[root@systemhub511 hadoop]# 
```
###### 使用hadoop fs -cat 指令查看 WordCount统计结果
``` powershell
[root@systemhub511 hadoop]# hadoop fs -cat /user/geekparkhub/output/part-r-00000
19/03/04 21:24:23 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
geek    2
geekparkhub     1
hackerparkhub   5
hadoop  3
helloworld      2
test    1
[root@systemhub511 hadoop]# 
```

### 7.7.1 Hadoop 序列化
#### 序列化 概述
##### 什么是序列化
> 序列化：就是把内存中的对象,转换成字节序列,(或其他数据传输协议)以便于存储到磁盘(持久化)和网络传输.
> 
> 反序列化：就是将收到字节序列,(或其他数据传输协议)或者是磁盘的持久化数据,转换成内存中的对象.
> 
##### 为什么要序列化
> 一般来讲,''存活''对象只能生存在内存里,关机断电就没有了,而且''存活''对象只能由本地的进程使用,不能被发送到网络上的另一台计算机,然而序列化可以存储''存活''对象,可以将''存活''对象发送到远程计算机.
> 
##### 为什么不使用java序列化
> java序列化是一个重量级序列化框架(Serializable),一个对象被序列化后,会附带很多额外的信息(各种校验信息,Header,继承体系等),不便于在网络上高效传输,所以Hadoop自己开发了一套序列化机制(Writable).
> 
##### Hadoop序列化特点
> 紧凑：高效使用存储空间.
> 快速：读写数据的额外开销小.
> 可扩展性：随着通讯协议的升级而升级.
> 互操作性：支持多语言交互.

#### 自定义bean对象 实现序列化接口
> 在企业开发中往往常用的基本序列化类型不能满足所有需求,比如在Hadoop框架内部传递一个bean对象,那么该对象就需要实现序列化接口.
> 
> 具体实现bean对象序列化 七步走
> 
> 1.必须实现Writable接口.
> 2.反序列化时,需要反射机制调用空构造函数,所以必须要有空构造函数.
``` java
    /**
     * When deserializing, you need to reflect the call to the null parameter constructor.
     * 反序列化时,需要反射调用空参构造函数
     */
    public FlowBean() {
        super();
    }
```
> 3.重写序列化方法.
``` java
    /**
     * Serialization method
     * 序列化方法
     *
     * @param out
     * @throws IOException
     */
    @Override
    public void write(DataOutput out) throws IOException {
        out.writeLong(upFlow);
        out.writeLong(downFlow);
        out.writeLong(sumFlow);
    }
```
> 4.重写反序列化方法
> 5.注意反序列化的顺序和序列化的顺序完全一致
``` java
    /**
     * Deserialization method, the deserialization method read order must be consistent with the write order of the write serialization method
     * 反序列化方法,反序列化方法读顺序必须和写序列化方法的写顺序必须一致
     *
     * @param in
     * @throws IOException
     */
    @Override
    public void readFields(DataInput in) throws IOException {
        this.upFlow = in.readLong();
        this.downFlow = in.readLong();
        this.sumFlow = in.readLong();
    }
```
> 6.要想把结果显示在文件中，需要重写toString()，可用”\t”分开，方便后续用.
``` java
    /**
     * Write a to String method to facilitate subsequent printing to text
     * 编写toString方法,方便后续打印到文本
     *
     * @return
     */
    @Override
    public String toString() {
        return upFlow + "\t" + downFlow + "\t" + sumFlow;
    }
```
> 7.如果需要将自定义的bean放在key中传输，则还需要实现comparable接口，因为mapreduce框中的shuffle过程一定会对key进行排序

#### 序列化 案例实操
##### 1.需求
> 统计每一个手机号耗费的总上行流量、下行流量、总流量.
##### 2.获取数据源:来自网络资源
##### 3.输入数据格式:
``` prolog
1   130001099990 111.186.104.167 www.baidu.com 28219 21031 200
2   15026889999 180.166.156.78 www.google.com 264 0 200
3   13601029999 212.64.111.89 www.github.com 132 1512 200
4   14512449999 117.135.178.67 www.qq.com 1929 180 200
5   15210039999 211.136.129.80 www.shouhu.com 132 15152 200
6   15510759999 112.65.214.26 www.qingha.com 2008 2779 200
7   15810579999 140.206.76.67 www.alibaba.com 9087 3673 200
8   13900999999 27.115.112.25 www.info.xcar.com.cn 46 177 200
9   13341098674 39.129.1.90 www.yq.aliyun.com 976 7661 200
10  14701159999 218.206.61.16 www.flaticon.com 5432 12 200
11  15116949999 219.159.60.26 www.translate.google.com 3 398 200
12  13261999999 36.111.136.126 www.blog.csdn.net 745 21 200 
13  15910419999 222.74.169.128 www.zhangshengrong.com 3890 496 200
14  18618689999 61.138.127.67 www.cn.bing.com 63 1498 200
15  18810599999 101.124.10.67 www.gitee.com 196 3360 200
16  18901009997 106.39.56.671 www.pai.com 16 289 200
17  13341099905 114.67.225.123 www.importnew.com 203 46 200
18  18221609878 116.196.121.45 www.booking.com 1732 698 200
19  01058484076 192.144.135.12 www.zhipin.com 80 1469 200
20  01082895409 221.176.7.23 www.bing.com 7596 264 200 
21  18674215555 139.219.14.124 www.facebook.com 92 738 200
22  15527194444 211.150.90.01 www.refinery29.com 5493 189 200 
23  31125344449 113.61.165.26 www.thenextweb.com 1892 25 200
24  15542102444 180.218.164.34 www.cinemablend.com 394 29 200
25  18674215555 60.245.45.34 www.oschina.net 4782 968 200
26  18476943333 61.139.47.27 www.tool.cn 3215 14 200
```
##### 4.输出数据格式:
``` prolog
    13560436666  1116  954  2070

    手机号码 上行流量 下行流量 总流量
```
##### 5.分析基本思路:
> Map阶段:
> 1.读取一行数据,切分字段
> 2.抽取手机号、上行流量、下行流量
> 3.以手机号为key,bean对象为value输出,即context.write(手机号,bean);
> 
> Reduce阶段:
> 1.累加上行流量和下行流量得到总流量.
> 2.实现自定义的bean来封装流量信息,并将bean作为map输出的key来传输
> 3.MR程序在处理数据的过程中会对数据排序(map输出的kv对传输到reduce之前,会排序),排序的依据是map输出的key,所以我们如果要实现自己需要的排序规则,则可以考虑将排序因素放到key中,让key实现接口:WritableComparable,然后重写key的compareTo方法
##### 6.编写MapReduce程序
> 编写流量统计 FlowBean
``` java
package com.geekparkhub.hadoop.flowsum;

import org.apache.hadoop.io.Writable;
import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 * @author system
 * <p>
 * FlowBean 序列化
 * <p>
 */

public class FlowBean implements Writable {

    /**
     * Upstream traffic
     * 上行流量
     */
    private long upFlow;

    /**
     * Downstream traffic
     * 下行流量
     */
    private long downFlow;

    /**
     * Total flow
     * 总流量
     */
    private long sumFlow;

    /**
     * When deserializing, you need to reflect the call to the null parameter constructor.
     * 反序列化时,需要反射调用空参构造器
     */
    public FlowBean() {
        super();
    }

    /**
     * Parametric constructor
     * 有参构造器
     *
     * @param upFlow
     * @param downFlow
     */
    public FlowBean(long upFlow, long downFlow) {
        super();
        upFlow = upFlow;
        downFlow = downFlow;
        sumFlow = upFlow + downFlow;
    }

    /**
     * Serialization method
     * 序列化方法
     *
     * @param out
     * @throws IOException
     */
    @Override
    public void write(DataOutput out) throws IOException {
        out.writeLong(upFlow);
        out.writeLong(downFlow);
        out.writeLong(sumFlow);
    }

    /**
     * Deserialization method, the deserialization method read order must be consistent with the write order of the write serialization method
     * 反序列化方法,反序列化方法读顺序必须和写序列化方法的写顺序必须一致
     *
     * @param in
     * @throws IOException
     */
    @Override
    public void readFields(DataInput in) throws IOException {
        upFlow = in.readLong();
        downFlow = in.readLong();
        sumFlow = in.readLong();
    }

    /**
     * Write a to String method to facilitate subsequent printing to text
     * 编写toString方法,方便后续打印到文本
     *
     * @return
     */
    @Override
    public String toString() {
        return upFlow + "\t" + downFlow + "\t" + sumFlow;
    }

    /**
     * Get&Set method
     * Get&Set方法
     *
     * @return
     */
    public long getUpFlow() {
        return upFlow;
    }

    public void setUpFlow(long upFlow) {
        this.upFlow = upFlow;
    }

    public long getDownFlow() {
        return downFlow;
    }

    public void setDownFlow(long downFlow) {
        this.downFlow = downFlow;
    }

    public long getSumFlow() {
        return sumFlow;
    }

    public void setSumFlow(long sumFlow) {
        this.sumFlow = sumFlow;
    }

    public void set(long upFlow2,long downFlow2){
        upFlow = upFlow2;
        downFlow = downFlow2;
        sumFlow = upFlow2 + downFlow2;
    }

}
```
> 编写流量统计 FlowCountMapper
``` java
package com.geekparkhub.hadoop.flowsum;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * FlowCountMapper 序列化
 * <p>
 */

public class FlowCountMapper extends Mapper<LongWritable, Text, Text, FlowBean> {

    /**
     * Extract k, v
     * 提取k,v
     */
    Text k = new Text();
    FlowBean v = new FlowBean();

    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {

        /**
         * Get the first row of data
         * 获取第一行数据
         */
        String line = value.toString();

        /**
         * Cutting data
         * 切割数据
         */
        String[] fields = line.split(" ");

        /**
         * Package object
         * 封装对象
         */

        // 封装手机号 | Package phone number
        k.set(fields[1]);

        long upFlow = Long.parseLong(fields[fields.length - 3]);
        long downFlow = Long.parseLong(fields[fields.length - 2]);

        v.setUpFlow(upFlow);
        v.setDownFlow(downFlow);

        /**
         * data input
         * 写入数据
         */
        context.write(k, v);
    }
}
```
> 编写流量统计 FlowCountReducer
``` java
package com.geekparkhub.hadoop.flowsum;

import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.io.Text;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * FlowCountReducer 序列化
 * <p>
 */

public class FlowCountReducer extends Reducer<Text,FlowBean,Text,FlowBean> {

    FlowBean v = new FlowBean();

    @Override
    protected void reduce(Text key, Iterable<FlowBean> values, Context context) throws IOException, InterruptedException {

        long sum_upFlow = 0;
        long sum_downFlow = 0;

        /**
         * Cumulative summation
         * 累加求和
         */
        for (FlowBean flowBean : values){
            sum_upFlow += flowBean.getUpFlow();
            sum_downFlow += flowBean.getDownFlow();
        }
        v.set(sum_upFlow,sum_downFlow);

        /**
         * data input
         * 写入数据
         */
        context.write(key,v);
    }
}
```
> 编写流量统计 FlowsumDriver
``` java
package com.geekparkhub.hadoop.flowsum;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.fs.Path;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * FlowsumDriver 序列化
 * <p>
 */

public class FlowsumDriver {

    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {

        /**
         * Preset data input and output path
         * 预设数据输入输出路径
         */
        args = new String[]{"/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_flow",
                "/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_flow"};

        /**
         * Get configuration information, or job object instance
         * 获取配置信息,或者job对象实例
         */
        Configuration configuration = new Configuration();
        Job job = Job.getInstance(configuration);

        /**
         * Specify the local path where the jar package of the program is located.
         * 指定本程序的jar包所在的本地路径
         */
        job.setJarByClass(FlowsumDriver.class);

        /**
         * Specify the mapper/Reducer business class to be used by this business job
         * 指定本业务job要使用的mapper/Reducer业务类
         */
        job.setMapperClass(FlowCountMapper.class);
        job.setReducerClass(FlowCountReducer.class);

        /**
         * Specify the kv type of the mapper output data
         * 指定mapper输出数据的kv类型
         */
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(FlowBean.class);

        /**
         * Specify the kv type of the final output data
         * 指定最终输出的数据的kv类型
         */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(FlowBean.class);

        /**
         * Specify the directory where the input input file of the job is located.
         * 指定job的输入原始文件所在目录
         */
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         * Submit the relevant parameters configured in the job, and the jar package where the java class used by the job is located, and submit it to the yarn to run.
         * 将job中配置的相关参数,以及job所用的java类所在的jar包,提交给yarn去运行
         */
        boolean results = job.waitForCompletion(true);
        System.exit(results ? 0 : 1);
    }
}
```

##### 输入运行结果
``` prolog
01058484076	890	1469	2359
01082895409	7596	264	7860
130001099990	28219	21031	49250
13261999999	745	231	976
13341098674	976	7661	8637
13341099905	203	466	669
13601029999	132	1512	1644
13900999999	456	177	633
14512449999	1929	180	2109
14701159999	5432	122	5554
15026889999	264	980	1244
15116949999	743	398	1141
15210039999	132	15152	15284
15510759999	2008	2779	4787
15527194444	5493	189	5682
15542102444	3394	329	3723
15810579999	9087	3673	12760
15910419999	3890	496	4386
18221609878	1732	698	2430
18344215555	3992	738	4730
18476943333	3215	164	3379
18618689999	663	1498	2161
18674215555	4782	968	5750
18810599999	196	3360	3556
18901009997	816	289	1105
31125344449	1892	255	2147
```

### 7.7.2 MapReduce 框架原理

### 7.7.3.1 InputFormat 数据输入
#### 切片与MapTask并行度决定机制
##### 1.问题引出
>  MapTask的并行度决定Map阶段的任务处理并发度,进而影响到整个Job的处理速度.
> Q&A 1G的数据,启动8个MapTask,可以提高集群的并发处理能力,那么1K的数据,也启动8个MapTask,也会提高集群性能吗?
> MapTask并行任务是否越多越好? 哪些因素影响到MapTask并行度?
##### 2.MapTask并行度决定机制
> 数据块:Block是HDFS物理上把数据分成一块一块.
> 数据切片:数据切片是指在逻辑上对输入进行分片,并不会在磁盘上将其切分片进行存储.
##### 数据切片与MapTask并行度决定机制
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_025.jpg)

#### Job提交流程源码 和 切片源码详解

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_028.jpg)

##### 提取 job提交流程 核心源码
``` java
waitForCompletion();
    submit();
        // 建立连接
        connect();
        // 创建提交job的代理
        new Cluster(getConfiguration());
            // 判断是本地yarn还是远程
            initialize(jobTrackAddr, conf); 
// 提交
sjobsubmitter.submitJobInternal(Job.this, cluster);
    // 创建给集群提交数据的Stag路径
    Path jobStagingArea = JobSubmissionFiles.getStagingDir(cluster, conf); 
    // 获取jobid,并创建job路径
    JobID jobId = submitClient.getNewJobID();
    // 拷贝jar包到集群
    copyAndConfigureFiles(job, submitJobDir);
        rUploader.uploadFiles(job, jobSubmitDir);
    // 计算切片,生成切片规划文件
    writeSplits(job, submitJobDir); 
        maps = writeNewSplits(job, jobSubmitDir); 
            input.getSplits(job); 
    // 向Stag路径写xml配置文件
    writeConf(conf, submitJobFile);
        conf.writeXml(out);
    // 提交job,返回提交状态
    status = submitClient.submitJob(jobId,submitJobDir.toString(),job.getCredentials());
```

#### FileInputFormat 切片
> FileInputFormat源码解析(input.getSplits(job))
> 找到数据存储的目录.
> 开始遍历处理(规划切片)下的每一个文件遍历第一个文件ss.txt.
> a）获取文件大小fs.sizeOf(ss.txt).
> b）计算切片大小computeSliteSize(Math.max(minSize,Math.min(maxSize,blocksize)))=blocksize=128M.
> c）默认情况下,切片大小=blocksized.
> 开始切,形成第1个切片:ss.txt—0:128M,第2个切片ss.txt—128:256M,第3个切片ss.txt—256M:300M,(每次切片时,都要判断切完剩下的部分是否大于块的1.1倍,不大于1.1倍就划分一块切片).
> e）将切片信息写到一个切片规划文件中.
> f）整个切片的核心过程在getSplit()方法中完成.
> g）数据切片只是在逻辑上对输入数据进行分片,并不会再磁盘上将其切分成分片进行存储,InputSplit只记录了分片的元数据信息,比如起始位置、长度以及所在的节点列表等.
> h）注意:block是HDFS物理上存储的数据,切片是对数据逻辑上的划分.
> 提交切片规划文件到yarn上,yarn上的MrAppMaster就可以根据切片规划文件计算开启maptask个数.

#### FileInputFormat 切片机制
##### 切片机制
> FileInputFormat中默认的切片机制:
> 1.简单地按照文件的内容长度进行切片.
> 2.切片大小,默认等于Block大小.
> 3.切片时不考虑数据集整体,而是逐个针对每一个文件单独切片.
> 4.在本地运行模式下Block块大小为32M,在集群运行模式下Block块大小为128M.
##### 案例分析
> 比如待处理数据有两个文件:
> 
> file1.txt 320M
> file2.txt 10M
> 
> 经过FileInputFormat的切片机制运算后，形成的切片信息如下:
> file1.txt.split1  --  0~128
> file1.txt.split2  --  128~256
> file1.txt.split3  --  256~320
> file2.txt.split1  --  0~10M
> 
> FileInputFormat切片大小的参数配置
> 
> 通过分析源码,在FileInputFormat中,计算切片大小的逻辑:
> 
> 切片主要由这几个值来运算决定.
``` java
Math.max(minSize,Math.min(maxSize,blockSize));
```
``` java
// 默认值为1
mapreduce.input.fileinputformat.split.minsize=1
```
``` java
// 默认值Long.MAXValue / Long类型的最大值
mapreduce.input.fileinputformat.split.maxsize= Long.MAXValue
```
> 因此,默认情况下,切片大小=blocksize
> 
> maxsize(切片最大值):参数如果调得比blocksize小,则会让切片变小,而且就等于配置的这个参数的值.
> 
> minsize(切片最小值):参数调的比blockSize大,则可以让切片变得比blocksize还大.
> 
> 获取切片信息API
``` java
// 根据文件类型获取切片信息
FileSplit inputSplit = (FileSplit) context.getInputSplit();
// 获取切片的文件名称
String name = inputSplit.getPath().getName();
```
#### CombineTexInputFormat 切片机制
> 框架默认的TexInputFormat切片机制是对任务按文件规划切片,不管文件多小,都会是一个单独的切片,都会交给一个MapTask,这样如果有大量的小文件,就会产生大量的MapTask,处理效率非常低.
##### 1.应用场景
> CombineTexInputFormat用于小文件过多的场景,它可以将多个小文件从逻辑上规划到一个切片中,这样多个小文件就可以交给一个MapTsak处理.
##### 2.虚拟存储切片最大值设置
``` java
 // 设置为4MB
 CombineTexInputFormat.setMaxInputSplitSize(job,4194304);
```
> 注意:虚拟存储切片最大设置最好要根据实际的小文件大小情况来设置具体参数.
##### 3.切片机制
> 生成切片过程为两部分:虚拟存储过程和切片过程.
> 
###### 虚拟存储过程:
> 将输入目录下所有文件大小,依次和设置的setMaxInputSplitSize值比较,如果不大于设置的最大值,逻辑上划分一个块,如果输入文件大小设置的最大值且大于两倍,那么以最大值切割一块,当剩余数据大小超过设置的最大值且不大于最大值2倍,此时将文件均分为2个虚拟存储块(防止出现太小切片).
> 
> 例如setMaxInputSplitSize值为4M,输入文件大小为8.02M,则逻辑上分成一个4M,剩余的大小为4.02M,如果按照4M逻辑划分,就会出现0.02M的小虚拟存储文件,所以将剩余的4.02M文件切分成(2.01M和2.01M)两个文件.
> 
###### 切片过程:
> 1.判断虚拟存储打文件大小是否大于setMaxInputSplitSize值,大于等于则单独形成一个切片.
> 
> 2.如果不大于则跟下一个虚拟存储文件进行合并,并同形成一个切片.
> 
> 3.测试例子:有4个小文件大小分别为,1.7M / 5.1M / 3.4M / 6.8M,这四个小文件,则虚拟存储之后形成6个文件块,大小分别为如图所示.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_029.jpg)

#### CombineTexInputFormat 案例实操
##### 1.需求
> 将输入的大量小文件合并形成一个切片统一处理.
##### 输入数据:准备四个小文件.
##### 期望:一个切片处理4个文件.
##### 2.实现过程
> 不做任何处理,运行WordCount程序,观察切片个数为4.

> Log printing
``` prolog
2019-03-07 00:25:34,640 INFO [org.apache.hadoop.mapreduce.JobSubmitter] - number of splits:4
```
> 在WordcountDriver中增加如下代码,运行程序,并观察运行的切片个数为3.
``` java
 /**
 * If you do not set the Input Format, it defaults to Text Input Format.class
 * 如果不设置InputFormat，它默认用的是TextInputFormat.class
 */
 job.setInputFormatClass(CombineTextInputFormat.class);
        
 /**
 * Set the virtual storage slice maximum to 4M
 * 设置虚拟存储切片最大值为 4M
 */
 CombineTextInputFormat.setMaxInputSplitSize(job, 4194304);
         
 /**
 * Set the virtual storage slice minimum to 2M
 * 设置虚拟存储切片最小值为 2M
 */
 CombineTextInputFormat.setMinInputSplitSize(job, 2097152);
```
> Log printing
``` prolog
2019-03-07 00:40:29,199 INFO [org.apache.hadoop.mapreduce.JobSubmitter] - number of splits:3
```
> 在WordcountDriver中增加如下代码,运行程序,并观察运行的切片个数为1.
``` java
	/**
	* If you do not set the Input Format, it defaults to Text Input Format.class
	* 如果不设置InputFormat，它默认用的是TextInputFormat.class
	*/
	job.setInputFormatClass(CombineTextInputFormat.class);

	/**
	* Set the virtual storage slice maximum to 20M
	* 设置虚拟存储切片最大值为 20M
	*/
	CombineTextInputFormat.setMaxInputSplitSize(job, 20971520);
```
> Log printing
``` prolog
2019-03-07 00:52:11,201 INFO [org.apache.hadoop.mapreduce.JobSubmitter] - number of splits:1
```

#### FileInputFormat 实现类
> Q&A:MapReduce任务的输入文件一般是存储在HDFS里面,输入的文件格式包括:基于行的日志文件/二进制格式文件等,这些文件一般会很大,达到数十GB,至更大,那么MapReduce是如何读取这些数据的呢?
> 
> InputFormat常见的 接口实现类包括：TextInputFormat / KeyValueTextInputFormat / NLineInputFormat / CombineTextInputFormat和自定义InputFormat等.
#### 1.TextInputFormat
> TextInputFormat是默认的FileInputFormat实现类,按行读取每条记录,键是存储该行在整个文件中的起始字节偏移量,LongWritable类型,值是这行的内容,不包括任何行终止符(换行符,回车符),Text类型.
> 
> 以下是一个示例,比如一个分片包含了如下4条文本记录:
``` prolog
 Rich learning form
 Intelligent learning engine
 Learning more convenient
 From the real demand for more close to the enterprise
```
> 每条记录表示为以下 键/值对 & K既是偏移量 V整行内容:
``` prolog
 (0,Rich learning form)
 (19,Intelligent learning engine)
 (47,Learning more convenient)
 (72,From the real demand for more close to the enterprise)
```
#### 2.KeyValueTexInputFormat
> 每一行均为一条记录,被分隔符分割为Key,Value,可以通过在驱动类中设置```conf.set(KeyValueLineRecordReader.KEY_VALUE_SEPERATOR,"\t");```来设定分隔符,默认分隔符是tab.
> 以下是一个示例,输入是一个包含4条记录的分片,其中——>表示一个(水平方向的)制表符:
``` prolog
 line1 ——>Rich learning form
 line2 ——>Intelligent learning engine
 line3 ——>Learning more convenient
 line4 ——>From the real demand for more close to the enterprise
```
> 每条记录表示为以下键/值对:
``` prolog
 (line1,Rich learning form)
 (line2,Intelligent learning engine)
 (line3,Learning more convenient)
 (line4,From the real demand for more close to the enterprise)
```
> 此时的键是每行排在制表符之前的Text序列.

#### KeyValueTexInputFormat 使用案例
##### 1.需求
> 统计输入文件中第一行的第一个单词相同的行数.
##### 2.输入数据
``` prolog
GeekParkHub
Geek International Park
HackerParkHub
Geek International Park
HackerParkHub
```
##### 3.期望结果数据
``` prolog
GeekParkHub 1
Geek International Park 2
HackerParkHub 2
```
##### 4.代码实现
###### Create KVTextMapper.class
``` java
package com.geekparkhub.hadoop.kv;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * KVTextMapper
 * <p>
 */

public class KVTextMapper extends Mapper<Text, Text, Text, IntWritable> {

    /**
     * Instantiated object
     * 实例化对象
     */
    IntWritable v = new IntWritable(1);

    @Override
    protected void map(Text key, Text value, Context context) throws IOException, InterruptedException {
        /**
         * Write data
         * 写出数据
         */
        context.write(key, v);
    }
}
```
###### Create KVTextReducer.class
``` java
package com.geekparkhub.hadoop.kv;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * KVTextReducer
 * <p>
 */

public class KVTextReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

    IntWritable v = new IntWritable();

    @Override
    protected void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {

        /**
         * Cumulative summation
         * 累计求和
         */
        int sum = 0;
        for (IntWritable value : values) {
            sum += value.get();
        }

        v.set(sum);

        /**
         * Write data
         * 写出数据
         */
        context.write(key, v);
    }
}
```
###### Create KVTextDriver.class
``` java
package com.geekparkhub.hadoop.kv;

import com.geekparkhub.hadoop.mapreduce.WordcountDriver;
import com.geekparkhub.hadoop.mapreduce.WordcountMapper;
import com.geekparkhub.hadoop.mapreduce.WordcountReducer;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.CombineTextInputFormat;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.KeyValueLineRecordReader;
import org.apache.hadoop.mapreduce.lib.input.KeyValueTextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * KVTextDriver
 * <p>
 */

public class KVTextDriver {

    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {

        args = new String[]{"/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_kv",
                "/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_kv_001"};

        /**
         * 1. Get the Job object
         * 1. 获取Job对象
         */
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf);

        /**
         * Set the cutting method to KeyValueLineRecordReader
         * 设置切割方式为 KeyValueLineRecordReader
         */
        conf.set(KeyValueLineRecordReader.KEY_VALUE_SEPERATOR, " ");

        /**
         * 2. Set the jar storage location
         * 2. 设置jar存储位置
         */
        job.setJarByClass(KVTextDriver.class);

        /**
         * 3. Associate Map and Reduce classes
         * 3. 关联Map和Reduce类
         */
        job.setMapperClass(KVTextMapper.class);
        job.setReducerClass(KVTextReducer.class);

        /**
         * 4. Set the key and value types of the output data in the Mapper stage.
         * 4. 设置Mapper阶段输出数据的key与value类型
         */
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(IntWritable.class);

        /**
         * 5. Set the key and value types for the final data output
         * 5. 设置最终数据输出的key与value类型
         */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        /**
         * Set the Format mode to KeyValueTextInputFormat
         * 设置Format模式为KeyValueTextInputFormat
         * If you do not set the Input Format, it defaults to Text Input Format.class
         * 如果不设置InputFormat，它默认用的是TextInputFormat.class
         */
        job.setInputFormatClass(KeyValueTextInputFormat.class);

        /**
         * 6. Set the input path and output path
         * 6. 设置输入路径和输出路径
         */
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         * 7. Submit the Job
         * 7. 提交Job
         */
        boolean result = job.waitForCompletion(true);

        /**
         * 8. Log printing
         * 8. 日志打印
         */
        System.exit(result ? 0 : 1);
    }
}
```
##### 5.运行程序 查看part-r-00000结果
``` prolog
Geek International Park	2
GeekParkHub	1
HackerParkHub	2
```

#### 3.NLiveInputFormat
> 如果使用NLiveInputFormat,代表每个map进程处理的InputSplit不再按Block块去划分,而是按NLiveInputFormat指定的行数N来划分,既输入文件的总行数/N=切片数,如果不整除,切片数=商+1
> 以下是一个示例,仍然以下面的4行输入为例:
``` prolog
 Rich learning form
 Intelligent learning engine
 Learning more convenient
 From the real demand for more close to the enterprise
```
> 例如,如果N是2,则每个输入分片包括两行,开启2个MapTask.
``` prolog
 (0,Rich learning form)
 (19,Intelligent learning engine)
```
> 另一个mapper则收到后两行:
``` prolog
 (47,Learning more convenient)
 (72,From the real demand for more close to the enterprise)
```
> 这里的键和值与TextInputFormat生成的一样.

#### NLiveInputFormat 使用案例
##### 1.需求:
> 对每个单词进行统计,根据每个输入文件的行数来规定输出多少个切片,要求每三行放入一个切片中.
##### 2.输入数据:
``` prolog
GeekParkHub
Geek International Park
GeekParkHub
Geek International Park
GeekParkHub
Geek International Park
GeekParkHub
Geek International Park
GeekParkHub
Geek International Park Geek International Park
Geek International Park
```
##### 3.输出结果:
``` prolog
INFO [org.apache.hadoop.mapreduce.JobSubmitter] - number of splits:4
```
##### 4.代码实现:
###### Create NLineMapper.class
``` java
package com.geekparkhub.hadoop.nline;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * NLineMapper
 * <p>
 */

public class NLineMapper extends Mapper<LongWritable, Text, Text, IntWritable> {

    Text k = new Text();
    IntWritable v = new IntWritable(1);

    /**
     * Rewrite the map() method
     * 重写map()方法
     *
     * @param key
     * @param value
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {

        /**
         * 1. Get the first row of data
         * 1. 获取第一行数据
         */
        String line = value.toString();

        /**
         * 2. Cutting data
         * 2. 切割空格数据
         */
        String[] words = line.split(" ");

        /**
         * 3. Loop through the data
         * 3. 循环遍历数据
         */
        for (String word : words) {
            K.set(Long.parseLong(word));
            context.write(k, v);
        }
    }
}
```
###### Create NLineReducer.class
``` java
package com.geekparkhub.hadoop.nline;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * NLineReducer
 * <p>
 */

public class NLineReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

    IntWritable v = new IntWritable();
    
    /**
     * Rewrite the reduce() method
     * 重写reduce()方法
     *
     * @param key
     * @param values
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {

        /**
         * 1. Accumulate summation
         * 1. 累加求和
         */
        int sum = 0;
        for (IntWritable value : values) {
            sum += value.get();
        }
        v.set(sum);

        /**
         * 2. Output data
         * 2. 输出数据
         */
        context.write(key, v);

    }
}
```
###### Create NLineDriver.class
``` java
package com.geekparkhub.hadoop.nline;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.NLineInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * NLineDriver
 * <p>
 */

public class NLineDriver {
    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {

        args = new String[]{"/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_nl",
                "/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_nl_001"};

        /**
         * 1. Get the Job object
         * 1. 获取Job对象
         */
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf);

        /**
         * Set Input Split to perform a slice every three times
         * 设置InputSplit每三行为一个切片.
         */
        NLineInputFormat.setNumLinesPerSplit(job,3);

        /**
         * Processing the number of records using the NLine Input Format
         * 使用NLineInputFormat处理记录数.
         */
        job.setInputFormatClass(NLineInputFormat.class);

        /**
         * 2. Set the jar storage location
         * 2. 设置jar存储位置
         */
        job.setJarByClass(NLineDriver.class);

        /**
         * 3. Associate Map and Reduce classes
         * 3. 关联Map和Reduce类
         */
        job.setMapperClass(NLineMapper.class);
        job.setReducerClass(NLineReducer.class);

        /**
         * 4. Set the key and value types of the output data in the Mapper stage.
         * 4. 设置Mapper阶段输出数据的key与value类型
         */
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(IntWritable.class);

        /**
         * 5. Set the key and value types for the final data output
         * 5. 设置最终数据输出的key与value类型
         */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        /**
         * 6. Set the input path and output path
         * 6. 设置输入路径和输出路径
         */
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         * 7. Submit the Job
         * 7. 提交Job
         */
        boolean result = job.waitForCompletion(true);

        /**
         * 8. Log printing
         * 8. 日志打印
         */
        System.exit(result ? 0 : 1);
    }
}
```
##### 5.结果查看:
> part-r-00000
``` prolog
Geek	12
Hub	5
International	7
Park	12
```
 > Log printing
``` prolog
2019-03-07 22:27:28,044 INFO [org.apache.hadoop.mapreduce.JobSubmitter] - number of splits:4
```

#### 自定义InputFormat
> 在企业开发中,Hadoop框架自带的InputFormat类型不能满足于所有应用场景,需要自定义InputFormat来解决实际问题.
#### 自定义InputFormat步骤如下:
> 1.自定义一个类继承FileInputFormat.
> 2.改写RecordReader,实现一次读取一个完整文件封装为KV.
> 3.在输出时使用SequenceFileOutPutFormat输出合并文件.
> 
#### 自定义InputFormat 案例实操
##### 1.需求
> 无论hdfs还是mapreduce,对于小文件都有损效率,实践中,又难免面临处理大量小文件的场景,此时就需要有相应解决方案.
> 
> 将多个小文件合并成一个文件SequenceFile,SequenceFile里面存储着多个文件,存储的形式为文件路径+名称为key,文件内容为value.
##### 2.输入数据
> Create 1.txt / Create 2.txt / Create 3.txt
> 
> 最终预期文件格式：part-r-00000

##### 3.分析
> 小文件的优化无非以下几种方式:
> 在数据采集的时候,就将小文件或小批数据合成大文件再上传HDFS.
> 在业务处理之前,在HDFS上使用mapreduce程序对小文件进行合并.
> 在mapreduce处理时,可采用CombineTextInputFormat提高效率.

##### 4.具体实现
> 1.自定义一个类继承FileInputFormat
> 重写isSplitable()方法,返回fales不可切割.
> 重写createRecordReader(),创建自定义RecordReader对象,并初始化
> 2.改写RecordReader,实现一次读取一个完整文件封装为KV
> 采用IO流一次读取一个文件输出到value中,因为设置了不可切片,最终把所有文件都封装到了value中.
> 获取文件路径信息+名称,并设置key
> 3.设置Driver
```
 // 设置输出的inputFormat
 job.setInputFormatClass(WholeFileInputformat.class);
 // 设置输出的outputFormat
 job.setOutputFormatClass(SequenceFileOutputFormat.class);
```

##### 5.程序实现
###### Create WholeFileInputformat.class
``` java
package com.geekparkhub.hadoop.inputformat;

import org.apache.hadoop.io.BytesWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.InputSplit;
import org.apache.hadoop.mapreduce.RecordReader;
import org.apache.hadoop.mapreduce.TaskAttemptContext;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * WholeFileInputformat
 * <p>
 */

public class WholeFileInputformat extends FileInputFormat<Text, BytesWritable> {

    /**
     * Rewrite the Record Reader() method
     * 重写RecordReader()方法
     *
     * @param split
     * @param context
     * @return
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    public RecordReader<Text, BytesWritable> createRecordReader(InputSplit split, TaskAttemptContext context) throws IOException, InterruptedException {

        WholeRecordReader recordReader = new WholeRecordReader();

        /**
         * Call initialization method
         * 调用初始化方法
         */
        recordReader.initialize(split, context);
        return recordReader;
    }
}
```
###### Create WholeRecordReader.class
``` java
package com.geekparkhub.hadoop.inputformat;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.BytesWritable;
import org.apache.hadoop.io.IOUtils;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.InputSplit;
import org.apache.hadoop.mapreduce.RecordReader;
import org.apache.hadoop.mapreduce.TaskAttemptContext;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * WholeRecordReader
 * <p>
 */

public class WholeRecordReader extends RecordReader<Text, BytesWritable> {

    /**
     * Declaration file slice
     * 声明文件切片
     */
    FileSplit split;
    Configuration conf;
    Text k = new Text();
    BytesWritable v = new BytesWritable();

    /**
     * Marker bit
     * 标记位
     */
    boolean isProgress = true;

    @Override
    public void initialize(InputSplit split, TaskAttemptContext context) throws IOException, InterruptedException {
        /**
         * Initialization operation
         * 初始化操作
         */
        this.split = (FileSplit) split;

        /**
         * Get configuration information
         * 获取配置信息
         */
        conf = context.getConfiguration();
    }

    @Override
    public boolean nextKeyValue() throws IOException, InterruptedException {

        if (isProgress) {

            /**
             * Handling core business logic
             * 处理核心业务逻辑
             */
            byte[] buf = new byte[(int) split.getLength()];

            /**
             * Get fs object
             * 1.获取fs对象
             */
            Path path = split.getPath();
            FileSystem fs = path.getFileSystem(conf);

            /**
             * Get the input stream
             * 2.获取输入流
             */
            FSDataInputStream fis = fs.open(path);

            /**
             * File copy buffer
             * 3.将文件拷贝缓冲区
             */
            IOUtils.readFully(fis, buf, 0, buf.length);

            /**
             * Package V
             * 4.封装 V
             */
            v.set(buf, 0, buf.length);

            /**
             * Package K
             * 5.封装 K
             */
            k.set(path.toString());

            /**
             * Close resource
             * 6.关闭资源
             */
            IOUtils.closeStream(fis);

            /**
             * Clear flag
             * 清空标记位
             */
            isProgress = false;
            return true;
        }
        return false;
    }

    @Override
    public Text getCurrentKey() throws IOException, InterruptedException {

        return k;
    }

    @Override
    public BytesWritable getCurrentValue() throws IOException, InterruptedException {

        return v;
    }

    @Override
    public float getProgress() throws IOException, InterruptedException {
        return 0;
    }

    @Override
    public void close() throws IOException {

    }
}
```
###### Create SequenceFileMapper.class
``` java
package com.geekparkhub.hadoop.inputformat;

import org.apache.hadoop.io.BytesWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * SequenceFileMapper
 * <p>
 */

public class SequenceFileMapper extends Mapper<Text, BytesWritable, Text, BytesWritable> {

    @Override
    protected void map(Text key, BytesWritable value, Context context) throws IOException, InterruptedException {
        context.write(key, value);
    }
}
```
###### Create SequenceFileReducer.class
``` java
package com.geekparkhub.hadoop.inputformat;

import org.apache.hadoop.io.BytesWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * SequenceFileReducer
 * <p>
 */

public class SequenceFileReducer extends Reducer<Text, BytesWritable, Text, BytesWritable> {
    @Override
    protected void reduce(Text key, Iterable<BytesWritable> values, Context context) throws IOException, InterruptedException {

        /**
         * Loop out data
         * 循环写出数据
         */
        for (BytesWritable value : values) {
            context.write(key, value);
        }
    }
}
```
###### Create SequenceFileDriver.class
``` java
package com.geekparkhub.hadoop.inputformat;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.BytesWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormat;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * SequenceFileDriver
 * <p>
 */

public class SequenceFileDriver {

    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {

        args = new String[]{"/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_format",
                "/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_format_001"};

        /**
         * 1. Get the Job object
         * 1. 获取Job对象
         */
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf);

        /**
         * 2. Set the jar storage location
         * 2. 设置jar存储位置
         */
        job.setJarByClass(SequenceFileDriver.class);

        /**
         * Set the input inputformat
         * 设置输入的 inputformat
         */
        job.setInputFormatClass(WholeFileInputformat.class);

        /**
         * Set the output format of the output
         * 设置输出的 outputformat
         */
        job.setOutputFormatClass(SequenceFileOutputFormat.class);

        /**
         * 3. Associate Map and Reduce classes
         * 3. 关联Map和Reduce类
         */
        job.setMapperClass(SequenceFileMapper.class);
        job.setReducerClass(SequenceFileReducer.class);

        /**
         * 4. Set the key and value types of the output data in the Mapper stage.
         * 4. 设置Mapper阶段输出数据的key与value类型
         */
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(BytesWritable.class);

        /**
         * 5. Set the key and value types for the final data output
         * 5. 设置最终数据输出的key与value类型
         */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(BytesWritable.class);

        /**
         * 6. Set the input path and output path
         * 6. 设置输入路径和输出路径
         */
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         * 7. Submit the Job
         * 7. 提交Job
         */
        boolean result = job.waitForCompletion(true);

        /**
         * 8. Log printing
         * 8. 日志打印
         */
        System.exit(result ? 0 : 1);
    }
}
```
##### 6.运行查看 part-r-00000二进制结果
``` prolog
SEQorg.apache.hadoop.io.Text"org.apache.hadoop.io.BytesWritablepˮ��y5�3�Ζ���!nmfile:/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_format/1.txt� GeekParkHub | 极客实验室
 Website | https://www.geekparkhub.com/
 Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见nmfile:/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_format/2.txt�HackerParkHub | 黑客公园枢纽
Website | https://www.hackerparkhub.com/
Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜�nmfile:/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_format/3.txtEGeek International Park | 极客国际公园
GeekDeveloper : JEEP-711
```


#### 37.7.3.2 MapReduce 工作流程
##### Map 框架原理流程图(一)
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_026.jpg)

##### Reduce 框架原理流程图(二)
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_027.jpg)

>  流程详解上面的流程是整个mapreduce最全工作流程,但是shuffle过程只是从第7步开始 到第16步结束,具体shuffle过程详解,如下:
>  
> 1.maptask收集我们的map()方法输出的kv对,放到内存缓冲区中.
> 
> 2.从内存缓冲区不断溢出本地磁盘文件,可能会溢出多个文件.
> 
> 3.多个溢出文件会被合并成大的溢出文件.
> 
> 4.在溢出过程中,及合并的过程中,都要调用partitioner进行分区和针对key进行排序.
> 
> 5.reducetask根据自己的分区号,去各个maptask机器上取相应的结果分区数据.
> 
> 6.reducetask会取到同一个分区的来自不同maptask的结果文件,reducetask会将这些文件再进行合并(归并排序).
> 
> 7.合并成大文件后,shuffle的过程也就结束了,后面进入reducetask的逻辑运算过程,(从文件中取出一个一个的键值对group,调用用户自定义的reduce()方法).
> 
> 8.注意Shuffle中的缓冲区大小会影响到mapreduce程序的执行效率,原则上说,缓冲区越大,磁盘io的次数越少,执行速度就越快,缓冲区的大小可以通过参数调整,参数:io.sort.mb,默认100M.


#### 7.7.3.3 Shuffle 机制
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_031.jpg)
##### Shuffle 机制
> MapReduce确保每个Reducer的输入都是按键排序的,系统执行排序的过程(即将map输出作为输入传给reducer)称为shuffle.
> 
> 通俗易懂的讲,Map方法之后,Reduce方法之前的数据处理过程称之为Shuffle.
##### Partition 分区
###### 1.问题引出
> 要去将统计结果按照条件输出到不同文件中(分区),比如:将统计结果按照手机号归属地不同省份输出到不同文件中(分区).
###### 2.默认Partition分区
> 默认分区是根据key的hashCode对reduceTasks个数取模得到的.
> 开发者没法控制哪个key存储到哪个分区.
``` java
public class HashPartitioner<K, V> extends Partitioner<K, V> {
    public int getPartition(K key, V value, int numReduceTasks) {
        return (key.hashCode() & Integer.MAX_VALUE) % numReduceTasks;
    }
}
```
###### 3.自定义Partition分区 步骤
> 自定义类继承Partitioner,重写getPartition()方法.
``` java
public class ProvincePartitioner extends Partitioner<Text, FlowBean> {

    /**
     * Override the getPartition() method
     * 重写getPartition()方法
     */
    @Override
    publicint getPartition(Text key, FlowBean value, int numPartitions) {
        // 处理控制分区代码
        return partition;
    }
}
```
###### 4.在Job驱动中,设置自定义Partitioner.
``` java
job.setPartitionerClass(CustomPartitioner.class);
```
###### 5.自定义Partitio后,要根据自定义Partitioner的逻辑设置相应数量的ReduceTask.
``` java
job.setNumReduceTasks(5);
```

##### Partition分区 实操案例
###### 1.需求
> 将统计结果按手机归属地不同省份输出到不同文件中(分区).
> 
> 输出输入源 phone_datas.txt
``` prolog
1 13901129979 111.186.104.167 www.baidu.com 28219 21031 200
2 15026889999 180.166.156.78 www.google.com 264 980 200
3 13601029999 212.64.111.89 www.github.com 132 1512 400
4 13901129949 117.135.178.67 1929 180 200
5 13621399979 211.136.129.80 132 15152 200
6 15510759999 112.65.214.26 2008 2779 400
7 13716179966 140.206.76.67 www.alibaba.com 9087 3673 200
8 13900999999 27.115.112.25 www.info.xcar.com.cn 456 177 200
9 13621399732 39.129.1.90 www.yq.aliyun.com 976 7661 500
10 14701159999 218.206.61.16 www.flaticon.com 5432 122 200
11 15116949999 219.159.60.26 www.translate.google.com 743 398 200
12 13261999999 36.111.136.126 www.blog.csdn.net 745 231 200
13 15910419999 222.74.169.128 3890 496 200
14 13901129937 61.138.127.67 www.cn.bing.com 663 1498 200
15 13621399649 101.124.10.67 www.gitee.com 196 3360 500
16 18901009997 106.39.56.671 www.pai.com 816 289 200
17 13341099905 114.67.225.123 www.importnew.com 203 466 200
18 13800049725 116.196.121.45 www.booking.com 1732 698 200
19 01058484076 192.144.135.12 www.zhipin.com 890 1469 404
20 13716179787 221.176.7.23 www.bing.com 7596 264 200
21 13716179612 139.219.14.124 www.facebook.com 3992 738 200
22 15527194444 211.150.90.01 www.refinery29.com 5493 189 301
23 13800049962 113.61.165.26 www.thenextweb.com 1892 255 200
24 13800049915 180.218.164.34 www.cinemablend.com 3394 329 200
25 18674215555 60.245.45.34 4782 968 302
26 18476943333 61.139.47.27 www.tool.cn 3215 164 200
```
> 期望输出数据
> 手机号136/137/138/139位开头都分别存储到一个独立的4个文件中,其他首号开头存储到一个文件中.

###### 结合上一期(序列化 之 flowsum实操案例) 实现Partition分区
> flowsum 案例 快速阅读通道 [回顾案例](https://geekparkhub.github.io/technical_guide/programing_language/hadoop/hadoop.html#%E5%BA%8F%E5%88%97%E5%8C%96-%E6%A1%88%E4%BE%8B%E5%AE%9E%E6%93%8D) | [回顾案例项目](https://github.com/geekparkhub/geekparkhub.github.io/tree/master/technical_guide/programing_language/hadoop/hadoop_projects/mapreduce/src/main/java/com/geekparkhub/hadoop/flowsum)
###### 2.代码实现
###### Create ProvincePartitioner.class
``` java
package com.geekparkhub.hadoop.flowsum;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Partitioner;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * ProvincePartitioner
 * <p>
 */

public class ProvincePartitioner extends Partitioner<Text, FlowBean> {

    /**
     * Override the getPartition() method
     * 重写getPartition()方法
     * <p>
     * Key is the phone number, value is the traffic information
     * key是手机号,value是流量信息
     */

    @Override
    public int getPartition(Text key, FlowBean value, int numPartitions) {

        /**
         * Get the top three mobile phone numbers
         * 获取手机号前三位
         */
        String prePhoneNum = key.toString().substring(0, 3);

        /**
         * Partition status
         * 分区状态
         */
        int partition = 4;

        if ("136".equals(prePhoneNum)) {
            /**
             * If the first number is 136, the first data of 136 is written to the 0th partition.
             * 如果获得到首号为136,将136首号数据写入到第0分区.
             */
            partition = 0;
        } else if ("137".equals(prePhoneNum)) {
            /**
             * If the first number is 137, the first data of 137 is written to the first partition.
             * 如果获得到首号为137,将137首号数据写入到第1分区.
             */
            partition = 1;
        } else if ("138".equals(prePhoneNum)) {
            /**
             * If the first number is 138, the first data of 138 is written to the second partition.
             * 如果获得到首号为138,将138首号数据写入到第2分区.
             */
            partition = 2;
        } else if ("139".equals(prePhoneNum)) {
            /**
             * If the first number is 138, the first data of 138 is written to the third partition.
             * 如果获得到首号为138,将138首号数据写入到第3分区.
             */
            partition = 3;
        }
        /**
         * If the first number is obtained, write the other first data to the default 4th partition.
         * 如果获得到首号为其他,将其他首号数据写入到默认第4分区.
         */
        return partition;
    }
}
```
###### Update FlowsumDriver.class
``` java
package com.geekparkhub.hadoop.flowsum;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.fs.Path;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * FlowsumDriver 序列化
 * <p>
 */

public class FlowsumDriver {

    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {

        /**
         * Preset data input and output path
         * 预设数据输入输出路径
         */
        args = new String[]{"/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_flow",
                "/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_flow_002"};

        /**
         * Get configuration information, or job object instance
         * 获取配置信息,或者job对象实例
         */
        Configuration configuration = new Configuration();
        Job job = Job.getInstance(configuration);

        /**
         * Specify the local path where the jar package of the program is located.
         * 指定本程序的jar包所在的本地路径
         */
        job.setJarByClass(FlowsumDriver.class);

        /**
         * Set up a custom Partitioner
         * 设置自定义Partitioner
         */
        job.setPartitionerClass(ProvincePartitioner.class);

        /**
         * Set up Num Reduce Tasks
         * 设置NumReduceTasks
         */
        job.setNumReduceTasks(5);

        /**
         * Specify the mapper/Reducer business class to be used by this business job
         * 指定本业务job要使用的mapper/Reducer业务类
         */
        job.setMapperClass(FlowCountMapper.class);
        job.setReducerClass(FlowCountReducer.class);

        /**
         * Specify the kv type of the mapper output data
         * 指定mapper输出数据的kv类型
         */
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(FlowBean.class);

        /**
         * Specify the kv type of the final output data
         * 指定最终输出的数据的kv类型
         */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(FlowBean.class);

        /**
         * Specify the directory where the input input file of the job is located.
         * 指定job的输入原始文件所在目录
         */
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         * Submit the relevant parameters configured in the job, and the jar package where the java class used by the job is located, and submit it to the yarn to run.
         * 将job中配置的相关参数,以及job所用的java类所在的jar包,提交给yarn去运行
         */
        boolean results = job.waitForCompletion(true);
        System.exit(results ? 0 : 1);
    }
}
```
###### 3.运行查看结果
> 哇 结果 如此神奇 😄😄😄😄
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_032.jpg)
###### 4.分区案例小总结
> 1.如果ReduceTask的数量大于getPartition的结果数,则会多生产几个空的输出文件part-r-000xx;
> 
> 2.如果1小于ReduceTask的数量并且小于getPartition的结果数,则有一部分分区数据无处安放,导致抛出Exception异常.
> 
> 3.如果ReduceTask的数量等于1,则不管MapTask端输出多少个分区文件,最终结果都交给这一个ReduceTask,最终也就会只产生一个结果文件part-r-00000.
> 
> 4.分区号必须从零开始,逐一递增.
> Q&A 假设:自定义分区数为5,则
```
 // 1.会正常运行,只不过会产生一个输出文件.
 job.setNumReduceTask(1);
 
 // 2. 会抛出Exception异常
 job.setNumReduceTask(2);
 
 // 3. 大于5,程序会正常运行,会产生多余空文件.
  job.setNumReduceTask(6); 
```

##### WritableComparable 排序
###### 排序概述
> 排序是MapReduce框架中最重要的操作之一.
> 
> MapTask和ReduceTask均会对数据(按照key)进行排序,该操作属于Hadoop的默认行为,任何应用程序中的数据均会被排序,而不管逻辑上是否需要.
> 
> 默认排序是按照字典顺序排序,且实现该排序的方法是快速排序.
> 
> 对于MapTask,它会将处理的结果暂时放到一个缓冲区中,当缓冲区使用率达到一定阈值后,再对缓冲区中的数据进行一次排序,并将这些有序数据写到磁盘上,而当数据处理完毕后,它会对磁盘上所有文件进行一次归并排序.
> 
> 对于ReduceTask,它从每个MapTask上远程拷贝相应的数据文件,如果文件大小超过一定阈值,则放到磁盘上,否则放到内存中,如果磁盘上文件数目达到一定阈值,则进行一次合并以生成一个更大文件,如果内存中文件大小或者数目超过一定阈值,则进行一次合并后将数据写到磁盘上,当所有数据拷贝完毕后,ReduceTask统一对内存和磁盘上的所有数据进行归并排序.

###### 排序分类
> 部分排序:MapReduce根据输入记录的键对数据集排序,保证输出的每个文件内部排序.
> 
> 全排序:最终输出结果只有一个文件,且文件内部有序,实现方式是只设置一个ReduceTask,但该方法在处理大型文件是效率极低,因为一台机器处理所有文件,完全丧失了MapRecuce所提供的并行架构.
> 
> 辅助排序:(GroupingComparator分组) 在Reduce端对key进行分组,应用于:在接收的key为bean对象时,想让一个或几个字段相同(全部字段比较不相同)的key进入到同一个reduce方法时,可以采用分组排序.
> 
> 二次排序:在自定义排序过程中,如果compareTo中的判断条件为两个即为二次排序.

###### 自定义排序WritableComparable
> 1.原理分析
> 
> bean对象作为key传输,需要实现WritableComparable接口并重写compareTo方法,就可以实现排序.
``` java
 /**
 * Override the compareTo() method
 * 重写compareTo()方法
 */
 
 @Override
 public int compareTo(FlowBean o) {
	 int result;
	 // 按照总流量大小,倒序排序
	 if(sumFlow > bean.getSumFlow()){
		 result = -1;
	 }else if(sumFlow < bean.getSumFlow()){
		 result = 1;
	 }else{
		 result = 0;
	 }
	 return result;
 }
```

##### WritableComparable 排序 实操案例(全排序)
###### 1.需求
> 根据flowsum案例结果再次对总流量数据进行倒序排序.
###### 2.数据源
``` prolog
1 13901129979 111.186.104.167 www.baidu.com 28219 21031 200
2 15026889999 180.166.156.78 www.google.com 264 980 200
3 13601029999 212.64.111.89 www.github.com 132 1512 400
4 13901129949 117.135.178.67 1929 180 200
5 13621399979 211.136.129.80 132 15152 200
6 15510759999 112.65.214.26 2008 2779 400
7 13716179966 140.206.76.67 www.alibaba.com 9087 3673 200
8 13900999999 27.115.112.25 www.info.xcar.com.cn 456 177 200
9 13621399732 39.129.1.90 www.yq.aliyun.com 976 7661 500
10 14701159999 218.206.61.16 www.flaticon.com 5432 122 200
11 15116949999 219.159.60.26 www.translate.google.com 743 398 200
12 13261999999 36.111.136.126 www.blog.csdn.net 745 231 200
13 15910419999 222.74.169.128 3890 496 200
14 13901129937 61.138.127.67 www.cn.bing.com 663 1498 200
15 13621399649 101.124.10.67 www.gitee.com 196 3360 500
16 18901009997 106.39.56.671 www.pai.com 816 289 200
17 13341099905 114.67.225.123 www.importnew.com 203 466 200
18 13800049725 116.196.121.45 www.booking.com 1732 698 200
19 01058484076 192.144.135.12 www.zhipin.com 890 1469 404
20 13716179787 221.176.7.23 www.bing.com 7596 264 200
21 13716179612 139.219.14.124 www.facebook.com 3992 738 200
22 15527194444 211.150.90.01 www.refinery29.com 5493 189 301
23 13800049962 113.61.165.26 www.thenextweb.com 1892 255 200
24 13800049915 180.218.164.34 www.cinemablend.com 3394 329 200
25 18674215555 60.245.45.34 4782 968 302
26 18476943333 61.139.47.27 www.tool.cn 3215 164 200
```
###### 3.第一次处理后的数据 part-r-00000
``` prolog
01058484076	890	1469	2359
01082895409	7596	264	7860
130001099990	28219	21031	49250
13261999999	745	231	976
13341098674	976	7661	8637
13341099905	203	466	669
13601029999	132	1512	1644
13900999999	456	177	633
14512449999	1929	180	2109
14701159999	5432	122	5554
15026889999	264	980	1244
15116949999	743	398	1141
15210039999	132	15152	15284
15510759999	2008	2779	4787
15527194444	5493	189	5682
15542102444	3394	329	3723
15810579999	9087	3673	12760
15910419999	3890	496	4386
18221609878	1732	698	2430
18344215555	3992	738	4730
18476943333	3215	164	3379
18618689999	663	1498	2161
18674215555	4782	968	5750
18810599999	196	3360	3556
18901009997	816	289	1105
31125344449	1892	255	2147
```
###### 4.期望数据输出
``` prolog
15810579999		9087	3673	12760
13341098674		976	7661	8637
01082895409		7596	264	7860
```
###### 5.需求分析
> FlowBean实现WritableComparable接口重写compareTo方法
``` java
 /**
 * Override the compareTo() method
 * 重写compareTo()方法
 */
 
 @Override
 public int compareTo(FlowBean o) {
 // 倒序排列，从大到小 
 return (this.sumFlow > o.getSumFlow()) ? (-1) : 1;
 }
```
> Mapper类,key为bean,value为手机号
> Reduceer类 循环输出,避免总流量相同情况

###### 6.代码实现
###### Create FlowBean.class
``` java
package com.geekparkhub.hadoop.sort;

import org.apache.hadoop.io.WritableComparable;
import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * FlowBean
 * <p>
 */

public class FlowBean implements WritableComparable<FlowBean> {

    /**
     * Upstream traffic
     * 上行流量
     */
    private long upFlow;

    /**
     * Downstream traffic
     * 下行流量
     */
    private long downFlow;

    /**
     * Total flow
     * 总流量
     */
    private long sumFlow;

    /**
     * When deserializing, you need to reflect the call to the null parameter constructor.
     * 反序列化时,需要反射调用空参构造器
     */
    public FlowBean() {
    }

    /**
     * Parametric constructor
     * 有参构造器
     *
     * @param upFlow
     * @param downFlow
     */
    public FlowBean(long upFlow, long downFlow) {
        super();
        this.upFlow = upFlow;
        this.downFlow = downFlow;
        sumFlow = upFlow + downFlow;
    }

    /**
     * Rewrite the compare To() method
     * 重写compareTo()方法
     *
     * @param bean
     * @return
     */
    @Override
    public int compareTo(FlowBean bean) {
        /**
         * 处理排序核心CODE
         */
        int result;
        if (sumFlow > bean.getSumFlow()) {
            result = -1;
        } else if (sumFlow < bean.getSumFlow()) {
            result = 1;
        } else {
            result = 0;
        }
        return result;
    }

    /**
     * Rewrite serialization method
     * 重写 序列化方法
     *
     * @param out
     * @throws IOException
     */
    @Override
    public void write(DataOutput out) throws IOException {
        out.writeLong(upFlow);
        out.writeLong(downFlow);
        out.writeLong(sumFlow);
    }

    /**
     * Overwrite deserialization method
     * 重写 反序列化方法
     *
     * @param in
     * @throws IOException
     */
    @Override
    public void readFields(DataInput in) throws IOException {
        upFlow = in.readLong();
        downFlow = in.readLong();
        sumFlow = in.readLong();
    }

    /**
     * Get&Set method
     * Get&Set方法
     *
     * @return
     */
    public long getUpFlow() {
        return upFlow;
    }

    public void setUpFlow(long upFlow) {
        this.upFlow = upFlow;
    }

    public long getDownFlow() {
        return downFlow;
    }

    public void setDownFlow(long downFlow) {
        this.downFlow = downFlow;
    }

    public long getSumFlow() {
        return sumFlow;
    }

    public void setSumFlow(long sumFlow) {
        this.sumFlow = sumFlow;
    }

    @Override
    public String toString() {
        return "\t" + upFlow + "\t" + downFlow + "\t" + sumFlow;
    }
}
```
###### Create FlowCountSortMapper.class
``` java
package com.geekparkhub.hadoop.sort;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * FlowCountSortMapper
 * <p>
 */

public class FlowCountSortMapper extends Mapper<LongWritable, Text, FlowBean, Text> {

    /**
     * Extract k, v
     * 提取k,v
     */
    FlowBean k = new FlowBean();
    Text v = new Text();

    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {

        /**
         * Get the first row of data
         * 获取第一行数据
         */
        String line = value.toString();

        /**
         * Cutting data
         * 切割数据
         */
        String[] split = line.split("\t");

        /**
         * Package object
         * 封装对象
         */
        String phoneNum = split[0];
        long upFlow = Long.parseLong(split[1]);
        long downFlow = Long.parseLong(split[2]);
        long sumFlow = Long.parseLong(split[3]);

        k.setUpFlow(upFlow);
        k.setDownFlow(downFlow);
        k.setSumFlow(sumFlow);
        v.set(phoneNum);

        /**
         * data input
         * 写入数据
         */
        context.write(k, v);
    }
}
```
###### Create FlowCountSortReducer.class
``` java
package com.geekparkhub.hadoop.sort;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * FlowCountSortReducer
 * <p>
 */

public class FlowCountSortReducer extends Reducer<FlowBean, Text, Text, FlowBean> {

    @Override
    protected void reduce(FlowBean key, Iterable<Text> values, Context context) throws IOException, InterruptedException {

        /**
         * Loop output, write data
         * 循环输出,写出数据
         */
        for (Text value : values) {
            context.write(value, key);
        }
    }
}
```
###### Create FlowCountSortDriver.class
``` java
package com.geekparkhub.hadoop.sort;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * FlowCountSortDriver
 * <p>
 */

public class FlowCountSortDriver {
    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {

        /**
         * Preset data input and output path
         * 预设数据输入输出路径
         */
        args = new String[]{"/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_flow_count_sort",
                "/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_flow_count_sort_001"};

        /**
         * 1. Get the Job object
         * 1. 获取Job对象
         */
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf);

        /**
         * 2. Set the jar storage location
         * 2. 设置jar存储位置
         */
        job.setJarByClass(FlowCountSortDriver.class);

        /**
         * 3. Associate Map and Reduce classes
         * 3. 关联Map和Reduce类
         */
        job.setMapperClass(FlowCountSortMapper.class);
        job.setReducerClass(FlowCountSortReducer.class);

        /**
         * 4. Set the key and value types of the output data in the Mapper stage.
         * 4. 设置Mapper阶段输出数据的key与value类型
         */
        job.setMapOutputKeyClass(FlowBean.class);
        job.setMapOutputValueClass(Text.class);

        /**
         * 5. Set the key and value types for the final data output
         * 5. 设置最终数据输出的key与value类型
         */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(FlowBean.class);

        /**
         * 6. Set the input path and output path
         * 6. 设置输入路径和输出路径
         */
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         * 7. Submit the Job
         * 7. 提交Job
         */
        boolean result = job.waitForCompletion(true);

        /**
         * 8. Log printing
         * 8. 日志打印
         */
        System.exit(result ? 0 : 1);
    }
}
```
###### 7.运行查看 总流量倒序排序结果
``` prolog
130001099990		28219	21031	 49250
15210039999		132	15152	 15284
15810579999		9087	3673	12760
13341098674		976	7661	8637
01082895409		7596	264	7860
18674215555		4782	968	5750
15527194444		5493	189	5682
14701159999		5432	122	5554
15510759999		2008	2779	4787
18344215555		3992	738	4730
15910419999		3890	496	4386
15542102444		3394	329	3723
18810599999		196	3360	3556
18476943333		3215	164	3379
18221609878		1732	698	2430
01058484076		890	1469	2359
18618689999		663	1498	2161
31125344449		1892	255	2147
14512449999		1929	180	2109
13601029999		132	1512	1644
15026889999		264	980	1244
15116949999		743	398	1141
18901009997		816	289	1105
13261999999		745	231	976
13341099905		203	466	669
13900999999		456	177	633
```

##### WritableComparable 排序 实操案例(区内排序)
###### 1.需求
> 要求每个省份手机号输出的文件中按照总流量内部排序.
> 分析:基于前一个需求,增加自定义分区类即可.
###### 2.代码实现
###### Create ProvincePartitioner.class
``` java
package com.geekparkhub.hadoop.sort;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Partitioner;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * ProvincePartitioner
 * <p>
 */

public class ProvincePartitioner extends Partitioner<FlowBean, Text> {

    /**
     * Override the getPartition() method
     * 重写getPartition()方法
     * <p>
     * value is the phone number, key is the traffic information
     * value是手机号,key是流量信息
     */
    @Override
    public int getPartition(FlowBean key, Text value, int numPartitions) {

        /**
         * Get the top three mobile phone numbers
         * 获取手机号前三位
         */
        String prePhoneNum = value.toString().substring(0, 3);

        /**
         * Partition status
         * 分区状态
         */
        int partition = 4;
        if ("136".equals(prePhoneNum)) {
            /**
             * If the first number is 136, the first data of 136 is written to the 0th partition.
             * 如果获得到首号为136,将136首号数据写入到第0分区.
             */
            partition = 0;
        } else if ("137".equals(prePhoneNum)) {
            /**
             * If the first number is 137, the first data of 137 is written to the first partition.
             * 如果获得到首号为137,将137首号数据写入到第1分区.
             */
            partition = 1;
        } else if ("138".equals(prePhoneNum)) {
            /**
             * If the first number is 138, the first data of 138 is written to the second partition.
             * 如果获得到首号为138,将138首号数据写入到第2分区.
             */
            partition = 2;
        } else if ("139".equals(prePhoneNum)) {
            /**
             * If the first number is 138, the first data of 138 is written to the third partition.
             * 如果获得到首号为138,将138首号数据写入到第3分区.
             */
            partition = 3;
        }
        /**
         * If the first number is obtained, write the other first data to the default 4th partition.
         * 如果获得到首号为其他,将其他首号数据写入到默认第4分区.
         */
        return partition;
    }
}
```
###### Update FlowCountSortDriver.class
```
 /**
 * Set up a custom Partitioner
 * 设置自定义Partitioner
 */
 job.setPartitionerClass(ProvincePartitioner.class);

 /**
 * Set up Num Reduce Tasks
 * 设置NumReduceTasks
 */
 job.setNumReduceTasks(5);
```
###### 3.运行查看分区后倒序排序结果
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_033.jpg)


##### Combine 合并
> Combine是MR程序中Mapper和Reduce之外的一种组件.
> 
> Combine组件的父类就是Reducer.
> 
> Combine和Reducer的区别在于运行的位置:
> Combine是在每一个MapTask所在的节点运行.
> Reducer是接收全局所以的Mapper的输出结果.
> 
> Combine的意义就是对每一个MapTask的输出进行局部汇总,以减小网络传输量.
> 
> Combine能够应用的前提是不能影响最终的业务逻辑,而且Combiner的输出kv应该跟Reducer的输入kv类型要对应起来.

###### 自定义Combiner实现步骤
> 自定义一个combiner继承Reducer,,重写reduce方法
``` java
public class WordcountCombiner extends Reducer<Text, IntWritable, Text, IntWritable> {
    @Override
    protected void reduce(Text key, Iterable<IntWritable> values,
        Context context) throws IOException, InterruptedException {
        // 1 汇总操作
        int count = 0;
        for (IntWritable v : values) {
            count = v.get();
        }
        // 2 写出
        context.write(key, new IntWritable(count));
    }
}
```
> 在job驱动类中设置
``` java
job.setCombinerClass(WordcountCombiner.class);
``` 
##### Combine 合并案例实操
###### 1.需求:
> 统计过程中对每一个maptask的输出进行局部汇总，以减小网络传输量即采用Combiner功能.
###### 2.数据输入
###### 3.期望输出数据
> Combine输入数据多,输出时经过合并,输出数据降低.
###### 4.代码实现
> Create WordcountCombiner.class
``` java
package com.geekparkhub.hadoop.wordcount;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * WordcountCombiner
 * <p>
 */

public class WordcountCombiner extends Reducer<Text, IntWritable, Text, IntWritable> {

    IntWritable v = new IntWritable();

    @Override
    protected void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {

        /**
         * 1. Accumulate summation
         * 1. 累加求和
         */
        int sum = 0;

        for (IntWritable value : values) {
            sum += value.get();
        }
        v.set(sum);

        /**
         * 2. Output data
         * 2. 输出数据
         */
        context.write(key, v);
    }
}
```
> Update WordcountDriver.class
``` java
 /**
 * Set set Combiner Class
 *设置setCombinerClass
 */
 job.setCombinerClass(WordcountCombiner.class);
```
###### 5.第二种实现方案
> 只需要在WordcountDriver.class中添加以下配置即可.
``` java
 /**
 * Set set Combiner Class
 *设置setCombinerClass
 */
 job.setCombinerClass(WordcountReducer.class);
```
###### 6.运行并查看日志信息
> 在Combine input没合并之前是1048848,在合并之后是9123,这样就减小网络传输量.
``` prolog
	Map-Reduce Framework
		Map input records=177089
		Map output records=1048848
		Map output bytes=10947197
		Map output materialized bytes=263385
		Input split bytes=768
		Combine input records=1048848
		Combine output records=9123
		Reduce input groups=4576
		Reduce shuffle bytes=263385
		Reduce input records=9123
		Reduce output records=4576
		Spilled Records=18246
```

##### GroupingComparator分组(辅助排序)
> 对Reduce阶段的数据根据某一个或几个字段进行分组.
> 
> 分组排序步骤:
> 1.自定义类继承WritableComparator.
> 2.重写compare()方法.
> 3.创建一个构造器将比较对象的类传给父类.

##### GroupingComparator分组 案例实操
###### 1.需求
> 有如下订单数据,求每一个订单中最贵的商品.

| 订单ID | 商品ID |   商品金额   |
| :-------- | :--------:| :------: |
| 0000001 |   Pdt_06 |  50.0   |
|     	  |   Pdt_04 |  310.0  |
| 0000002 |   Pdt_25 |  520.0  |
|     	  |   Pdt_01 |  299.9  |
|     	  |   Pdt_11 |  1086.3 |
| 0000003 |   Pdt_34 |  124.6  |
|		  |   Pdt_12 |  496.0  |

###### 2.数据源
``` prolog
0000001 Pdt_06 50.0
0000001 Pdt_04 310.0
0000002 Pdt_25 520.0
0000002 Pdt_01 299.9
0000002 Pdt_11 1086.3
0000003 Pdt_34 124.6
0000003 Pdt_12 496.0
```
###### 3.期望输出数据
``` prolog
1	310.0
2	1086.3
3	496.0
```
###### 4.需求分析
> 利用订单ID和商品金额作为key,可以将Map阶段读取到的所有订单数据按照ID来升序排序,如果ID相同再按照金额降序排序,发送到Reduce.
> 
> 在Reduce端利用GroupingComparator将订单ID相同的kv聚合成组,然后取得第一个既是该订单中最贵商品.

###### 5.代码实现
###### Create OrderBean.class
``` java
package com.geekparkhub.hadoop.order;

import org.apache.hadoop.io.WritableComparable;
import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * OrderBean
 * <p>
 */

public class OrderBean implements WritableComparable<OrderBean> {

    /**
     * OrderBean attribute Product ID
     * OrderBean属性 商品ID
     */
    private int order_id;

    /**
     * OrderBean attribute
     * OrderBean属性 商品金额
     */
    private double order_money;

    /**
     * OrderBean no-argument constructor
     * OrderBean 无参构造器
     */
    public OrderBean() {
        super();
    }

    /**
     * OrderBean parameter constructor
     * OrderBean 参数构造器
     *
     * @param order_id
     * @param order_money
     */
    public OrderBean(int order_id, double order_money) {
        super();
        this.order_id = order_id;
        this.order_money = order_money;
    }

    /**
     * Rewrite the compare To() method
     * 重写compareTo()方法
     * <p>
     * Handling core business logic
     * 处理核心业务逻辑
     *
     * @param bean
     * @return
     */

    @Override
    public int compareTo(OrderBean bean) {

        /**
         * Sort by order ID in ascending order, if the same will be sorted by item amount in descending order
         * 先按照订单ID升序排序,如果相同将按照商品金额降序排序.
         */

        /**
         * Sort status
         * 排序状态
         *
         * State 1 : Indicates positive order sort
         * State -1 : Indicates descending sort
         * State 0 : Indicates equal
         *
         * 状态 1  : 表示 正序排序
         * 状态 -1 : 表示降序排序
         * 状态 0 : 表示相等
         */
        int result;

        if (order_id > bean.getOrder_id()) {
            result = 1;
        } else if (order_id < bean.getOrder_id()) {
            result = -1;
        } else {
            if (order_money > bean.getOrder_money()) {
                result = -1;
            } else if (order_money < bean.getOrder_money()) {
                result = 1;
            } else {
                result = 0;
            }
        }
        return result;
    }

    /**
     * Rewrite serialization method
     * 重写 序列化方法
     *
     * @param out
     * @throws IOException
     */
    @Override
    public void write(DataOutput out) throws IOException {
        out.writeInt(order_id);
        out.writeDouble(order_money);
    }

    /**
     * Overwrite deserialization method
     * 重写 反序列化方法
     *
     * @param in
     * @throws IOException
     */
    @Override
    public void readFields(DataInput in) throws IOException {
        order_id = in.readInt();
        order_money = in.readDouble();
    }

    /**
     * Get & Set method
     * Get & Set方法
     *
     * @return
     */
    public int getOrder_id() {
        return order_id;
    }

    public void setOrder_id(int order_id) {
        this.order_id = order_id;
    }

    public double getOrder_money() {
        return order_money;
    }

    public void setOrder_money(double order_money) {
        this.order_money = order_money;
    }

    /**
     * To String method
     * toString方法
     *
     * @return
     */
    @Override
    public String toString() {
        return order_id + "\t" + order_money;
    }
}
```
###### Create OrderSortMapper.class
``` java
package com.geekparkhub.hadoop.order;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * OrderSortMapper
 * <p>
 */

public class OrderSortMapper extends Mapper<LongWritable, Text, OrderBean, NullWritable> {

    /**
     * Instantiated object
     * 实例化对象
     */
    OrderBean k = new OrderBean();

    /**
     * Rewrite the map() method
     * 重写map()方法
     *
     * @param key
     * @param value
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {

        /**
         * Get a row of data
         * 获取一行数据
         */
        String line = value.toString();

        /**
         * Cutting data
         * 切割数据
         */
        String[] fields = line.split(" ");

        /**
         * Package object
         * 封装对象
         */
        k.setOrder_id(Integer.parseInt(fields[0]));
        k.setOrder_money(Double.parseDouble(fields[2]));

        /**
         * Write data
         * 写出数据
         */
        context.write(k, NullWritable.get());
    }
}
```
###### Create OrderSortReducer.class
``` java
package com.geekparkhub.hadoop.order;

import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.mapreduce.Reducer;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * OrderSortReducer
 * <p>
 */

public class OrderSortReducer extends Reducer<OrderBean, NullWritable, OrderBean, NullWritable> {

    /**
     * Rewrite the reduce() method
     * 重写reduce()方法
     *
     * @param key
     * @param values
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void reduce(OrderBean key, Iterable<NullWritable> values, Context context) throws IOException, InterruptedException {

        /**
         * Write data
         * 写出数据
         */
        context.write(key, NullWritable.get());
    }
}
```
###### Create OrderSortDriver.class
``` java
package com.geekparkhub.hadoop.order;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * OrderSortDriver
 * <p>
 */

public class OrderSortDriver {
    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {

        /**
         * Preset data input and output path
         * 预设数据输入输出路径
         */
        args = new String[]{"/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_order",
                "/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_order_001"};

        /**
         * 1. Get the Job object
         * 1. 获取Job对象
         */
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf);

        /**
         * 2. Set the jar storage location
         * 2. 设置jar存储位置
         */
        job.setJarByClass(OrderSortDriver.class);

        /**
         * 3. Associate Map and Reduce classes
         * 3. 关联Map和Reduce类
         */
        job.setMapperClass(OrderSortMapper.class);
        job.setReducerClass(OrderSortReducer.class);

        /**
         * 4. Set the key and value types of the output data in the Mapper stage.
         * 4. 设置Mapper阶段输出数据的key与value类型
         */
        job.setMapOutputKeyClass(OrderBean.class);
        job.setMapOutputValueClass(NullWritable.class);

        /**
         * 5. Set the key and value types for the final data output
         * 5. 设置最终数据输出的key与value类型
         */
        job.setOutputKeyClass(OrderBean.class);
        job.setOutputValueClass(NullWritable.class);

        /**
         * 6. Set the input path and output path
         * 6. 设置输入路径和输出路径
         */
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         * Set partition
         * 设置分区
         */
        job.setPartitionerClass(OrderSortPartitioner.class);

        /**
         * Set the number of Reduce
         * 设置Reduce个数
         */
        job.setNumReduceTasks(3);

        /**
         * Set the Reduce side grouping
         * 设置Reduce端分组
         */
        job.setGroupingComparatorClass(OrderSortGroupingComparator.class);

        /**
         * 7. Submit the Job
         * 7. 提交Job
         */
        boolean result = job.waitForCompletion(true);

        /**
         * 8. Log printing
         * 8. 日志打印
         */
        System.exit(result ? 0 : 1);
    }
}
```
###### Create OrderSortGroupingComparator.class
``` java
package com.geekparkhub.hadoop.order;

import org.apache.hadoop.io.WritableComparable;
import org.apache.hadoop.io.WritableComparator;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * OrderSortGroupingComparator
 * <p>
 */

public class OrderSortGroupingComparator extends WritableComparator {

    protected OrderSortGroupingComparator() {
        super(OrderBean.class, true);
    }

    @Override
    public int compare(WritableComparable a, WritableComparable b) {
        /**
         * As long as the order ID is the same, it is considered to be the same key
         * 只要订单ID相同,就认为是相同的key
         */

        OrderBean aBean = (OrderBean) a;
        OrderBean bBean = (OrderBean) b;

        int result;
        if (aBean.getOrder_id() > bBean.getOrder_id()) {
            result = 1;
        } else if (aBean.getOrder_id() < bBean.getOrder_id()) {
            result = -1;
        } else {
            result = 0;
        }
        return result;
    }
}
```
###### Create OrderSortPartitioner.class
``` java
package com.geekparkhub.hadoop.order;

import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.mapreduce.Partitioner;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 * @author system
 * <p>
 * OrderSortPartitioner
 * </p>
 */

public class OrderSortPartitioner extends Partitioner<OrderBean, NullWritable> {
    @Override
    public int getPartition(OrderBean key, NullWritable  value, int numReduceTasks) {
        return (key.getOrder_id() & Integer.MAX_VALUE) % numReduceTasks;
    }
}
```
###### 6.运行 查看结果
``` prolog
1	310.0
2	1086.3
3	496.0
```

#### 7.7.3.4 Map Task 工作机制
##### MapTask 工作机制
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_030.jpg)
> 1.Read阶段:MapTask通过用户编写的RecordReader,从输入InputSplit中解析出一个个key/value.
> 
> 2.Map阶段:该节点主要是将解析出的key/value交给用户编写map()函数处理,并产生一系列新的key/value.
> 
> 3.Collect收集阶段:在用户编写map()函数中,当数据处理完成后,一般会调用OutputCollector.collect()输出结果,在该函数内部,它会将生成的key/value分区(调用Partitioner)并写入一个环形内存缓冲区中.
> 
> 4.Spill阶段：即"溢写"当环形缓冲区满后,MapReduce会将数据写到本地磁盘上,生成一个临时文件,需要注意的是,将数据写入本地磁盘之前,先要对数据进行一次本地排序,并在必要时对数据进行合并、压缩等操作.
> 
> 5.溢写阶段详情: 
> 步骤1: 利用快速排序算法对缓存区内的数据进行排序,排序方式是,先按照分区编号partition进行排序,然后按照key进行排序,这样,经过排序后,数据以分区为单位聚集在一起,同一分区内所有数据按照key有序.
> 
> 步骤2: 按照分区编号由小到大依次将每个分区中的数据写入任务工作目录下的临时文件output/spillN.out(N表示当前溢写次数),如果用户设置了Combiner,则写入文件之前,对每个分区中的数据进行一次聚集操作.
> 
> 步骤3: 将分区数据的元信息写到内存索引数据结构SpillRecord中,其中每个分区的元信息包括在临时文件中的偏移量、压缩前数据大小和压缩后数据大小,如果当前内存索引大小超过1MB,则将内存索引写到文件output/spillN.out.index中.
> 
> 5.Combine阶段:当所有数据处理完成后,MapTask对所有临时文件进行一次合并,以确保最终只会生成一个数据文件.
> 
> 当所有数据处理完后,MapTask会将所有临时文件合并成一个大文件,并保存到文件output/file.out中,同时生成相应的索引文件output/file.out.index
> 
> 在进行文件合并过程中,MapTask以分区为单位进行合并,对于某个分区,它将采用多轮递归合并的方式,每轮合并io.sort.factor(默认100)文件,并将产生的文件重新加入待合并列表中,对文件排序后,重复以上过程,直到最终得到一个大文件.
> 
> 让每个MapTask最终只生成一个数据文件,可避免同时打开大量文件和同时读取大量小文件产生的随机读取带来的开销.


#### 7.7.3.5 Reduce Task 工作机制
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_034.jpg)
> 1.Copy阶段:ReduceTask从各个MapTask上远程拷贝一片数据,并针对某一片数据,如果其大小超过一定阈值,则写到磁盘上,否则直接放到内存中.
> 
> 2.Merge阶段:在远程拷贝数据的同时,ReduceTask启动了两个后台线程对内存和磁盘上的文件进行合并,以防止内存使用过多或磁盘上文件过多.
> 
> 3.Sort阶段:按照MapReduce语义,用户编写reduce()函数输入数据是按key进行聚集的一组数据,为了将key相同的数据聚在一起,Hadoop采用了基于排序的策略,由于各个MapTask已经实现对自己的处理结果进行了局部排序,因此ReduceTask只需对所有数据进行一次归并排序即可.
> 
> 4.Reduce阶段:reduce()函数将计算结果写到HDFS上.

#### 设置ReduceTask并行度(个数)
> reducetask的并行度同样影响整个job的执行并发度和执行效率,但与maptask的并发数由切片数决定不同,Reducetask数量的决定是可以直接手动设置:
> 
> 注意事项:
> 
> 1.ReduceTask=0,表示没有Reduce阶段,输出文件个数和Map个数一致.
> 
> 2.ReduceTask默认值就是1,所以输出文件个数为一个.
> 
> 3.如果数据分布不均匀,就有可能在Reduce阶段产生数据倾斜.
> 
> 4.ReduceTask数量并不是任意设置,还要考虑业务逻辑需求,有些情况下,需要计算全局汇总结果,就只能有1个Reducetask.
> 
> 5.具体多少个ReduceTask,需要根据集群性能而定.
> 
> 6.如果分区数不是1,但是ReduceTask为1,是否执行分区过程.
> 
> 答案是:不执行分区过程,因为在MapTask的源码中,执行分区的前提是先判断ReduceNum个数是否大于1,不大于1肯定不执行.


#### 7.7.3.6 OutputFromat 数据输出
##### OutputFormat接口实现类
> OutputFormat是MapReduce输出的基类,所有实现MapReduce输出都实现了OutputFormat接口.
##### 常见的OutputFormat实现类
###### 文本输出 TextOutputFormat
> 默认的输出格式是TextOutputFormat,它把每条记录写为文本行,它的键和值可以是任意类型,因为TextOutputFormat调用toString()方法把它们转换为字符串.
###### SequenceFileOutputFormat
> SequenceFileOutputFormat将它的输出写为一个顺序文件,如果输出需要作为后续MapReduce任务的输入,这便是一种好的输出格式,因为它的格式紧凑,很容易被压缩.
###### 自定义OutputFormat
> 根据开发者需求,自定义实现输出.

##### 自定义OutputFormat
> 为了实现控制最终文件的输出路径,可以自定义OutputFormat,要在一个MapReduce程序中根据数据的不同输出两类结果到不同目录,这类灵活的输出需求可以通过自定义OutputFormat来实现.

##### 自定义OutputFormat步骤
> 1.自定义一个类继承FileOutputFormat.
> 2.改写recordwriter,具体改写输出数据的方法write().

##### 自定义OutputFormat案例实操
###### 1.需求
> 过滤输入的log日志中是否包含geekparkhub
> 
> a.包含geekparkhub的网站输出到geekparkhub.log
> 
> b.不包含geekparkhub的网站输出到other.log
###### 2.输入数据
``` prolog
https://www.google.com/
https://github.com/
https://www.youtube.com/
https://twitter.com/
https://www.facebook.com
https://www.geekparkhub.com/
https://www.flaticon.com
https://baidu.com/
https://gitee.com/
http://info.xcar.com.cn/
http://tool.oschina.net/
https://www.instagram.com
https://emojipedia.org/
```
###### 3.具体实现
> 创建一个FilterRecordWriter类继承RecordWriter
> 创建两个文件输出流:geekparkhubOut,otherOut
> 如过输入数据包含geekparkhub则输出geekparkhubOut流,如不包含geekparkhub,则输出到otherOut流.

###### Create FilterMapper.class
``` java
package com.geekparkhub.hadoop.outputformat;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * FilterMapper
 * <p>
 */

public class FilterMapper extends Mapper<LongWritable, Text, Text, NullWritable> {

    /**
     * Rewrite the map() method
     * 重写map()方法
     *
     * @param key
     * @param value
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */

    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {

        /**
         * Write data
         * 写出数据
         */
        context.write(value, NullWritable.get());
    }
}
```
###### Create FilterReducer.class
``` java
package com.geekparkhub.hadoop.outputformat;

import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * FilterReducer
 * <p>
 */

public class FilterReducer extends Reducer<Text, NullWritable, Text, NullWritable> {

    Text k = new Text();

    /**
     * Rewrite the reduce() method
     * 重写reduce()方法
     *
     * @param key
     * @param values
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */

    @Override
    protected void reduce(Text key, Iterable<NullWritable> values, Context context) throws IOException, InterruptedException {

        /**
         * Manually format the data source
         * 手动格式化数据源
         */
        String line = key.toString();
        line = line + "\r\t";
        k.set(line);

        /**
         * Loop out data
         * 循环写出数据
         */
        for (NullWritable value : values) {
            context.write(k, NullWritable.get());
        }

    }
}
```

###### Create FilterOutputFormat.class
``` java
package com.geekparkhub.hadoop.outputformat;

import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * FilterOutputFormat
 * <p>
 */

public class FilterOutputFormat extends FileOutputFormat<Text, NullWritable> {

    /**
     * Rewrite the getRecordWriter() method
     * 重写getRecordWriter()方法
     * @param job
     * @return
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    public RecordWriter<Text, NullWritable> getRecordWriter(TaskAttemptContext job) throws IOException, InterruptedException {
        return new FRecordWriter(job);
    }
}
```
###### Create FRecordWriter.class
``` java
package com.geekparkhub.hadoop.outputformat;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.RecordWriter;
import org.apache.hadoop.mapreduce.TaskAttemptContext;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * FRecordWriter
 * <p>
 */

public class FRecordWriter extends RecordWriter<Text, NullWritable> {

    /**
     * Extract FS Data Output Stream
     * 提取FSDataOutputStream
     */
    FSDataOutputStream geekparkhubOut;
    FSDataOutputStream otherOut;

    /**
     * FRecordWriter 写数据核心构造器
     *
     * @param job
     */

    public FRecordWriter(TaskAttemptContext job) {

        try {

            /**
             * Get the file system and pass the current job object to the file system
             *获取文件系统,将当前job对象传递给文件系统
             */
            FileSystem fs = FileSystem.get(job.getConfiguration());

            /**
             * Create an output stream geekparkhub.log
             * 创建输出流 geekparkhub.log
             */
            geekparkhubOut = fs.create(new Path("/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_format_001/geekparkhub.log"));

            /**
             * Create an output stream other.log
             * 创建输出流 other.log
             */
            otherOut = fs.create(new Path("/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_format_001/other.log"));

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Override write() method
     * 复写 write()方法
     *
     * @param key
     * @param value
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    public void write(Text key, NullWritable value) throws IOException, InterruptedException {

        /**
         * Determine if the key contains geekparkhub
         * If yes, write to geekparkhub.log
         * If not, write to other.log
         *
         * 判断key中是否含有geekparkhub
         * 如果有则写入到geekparkhub.log
         * 如法没有则写入到other.log
         */

        if (key.toString().contains("geekparkhub")) {
            geekparkhubOut.write(key.toString().getBytes());
        } else {
            otherOut.write(key.toString().getBytes());
        }

    }

    /**
     * Override the close() method
     * 复写 close()方法
     *
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    public void close(TaskAttemptContext context) throws IOException, InterruptedException {
        if (geekparkhubOut != null) {
            geekparkhubOut.close();
        }
        if (otherOut != null) {
            otherOut.close();
        }
    }
}
```
###### Create FilterDriver.class
``` java
package com.geekparkhub.hadoop.outputformat;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * FilterDriver
 * <p>
 */

public class FilterDriver {
    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {

        /**
         * Preset data input and output path
         * 预设数据输入输出路径
         */
        args = new String[]{"/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_outputformat",
                "/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_format_001"};

        /**
         * 1. Get the Job object
         * 1. 获取Job对象
         */
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf);

        /**
         * 2. Set the jar storage location
         * 2. 设置jar存储位置
         */
        job.setJarByClass(FilterDriver.class);

        /**
         * 3. Associate Map and Reduce classes
         * 3. 关联Map和Reduce类
         */
        job.setMapperClass(FilterMapper.class);
        job.setReducerClass(FilterReducer.class);

        /**
         * 4. Set the key and value types of the output data in the Mapper stage.
         * 4. 设置Mapper阶段输出数据的key与value类型
         */
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(NullWritable.class);

        /**
         * 5. Set the key and value types for the final data output
         * 5. 设置最终数据输出的key与value类型
         */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(NullWritable.class);

        /**
         * Set custom output format components to the job object
         * 设置自定义输出格式组件到job对象中
         */
        job.setOutputFormatClass(FilterOutputFormat.class);

        /**
         * 6. Set the input path and output path
         * 6. 设置输入路径和输出路径
         */
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         * 7. Submit the Job
         * 7. 提交Job
         */
        boolean result = job.waitForCompletion(true);

        /**
         * 8. Log printing
         * 8. 日志打印
         */
        System.exit(result ? 0 : 1);
    }
}
```
###### 4.运行并查看结果
> geekparkhub.log
``` prolog
https://www.geekparkhub.com/
```
> other.log
``` prolog
	http://info.xcar.com.cn/
	http://tool.oschina.net/
	https://baidu.com/
	https://emojipedia.org/
	https://gitee.com/
	https://github.com/
	https://twitter.com/
	https://www.facebook.com
	https://www.flaticon.com
	https://www.google.com/
	https://www.instagram.com
	https://www.youtube.com/
```

#### 7.7.3.7 Join 多种应用
##### Reduce join    
###### Reduce join工作原理
> Map端的主要工作:为来自不同表(文件)的key/value对打标签以区别不同来源的记录,然后用连接字段作为key,其余部分和新加的标志作为value,最后进行输出.
> 
> Reduce端的主要工作:在reduce端以连接字段作为key的分组已经完成,我们只需要在每一个分组当中将那些来源于不同文件的记录(在map阶段已经打标志)分开,最后进行合并就ok了.
##### Reduce join案例实操
###### 1.需求
> 订单数据表t_order = order
| id      |     pid |   amount   |
| :-------- | --------:| :------: |
| 1001    |   01 |  1  |
| 1002    |   02 |  2  |
| 1003    |   03 |  3  |
| 1004    |   04 |  4  |
| 1005    |   05 |  5  |
| 1006    |   06 |  6  |

> 商品信息表t_product = pd
| pid      |     pname | 
| :-------- | :--------:|
| 01    |   小米 |
| 02    |   华为 |
| 03    |   锤子 |

> 将商品信息表中数据根据商品pid合并到订单数据表中.
| id      |     pname |   amount   |
| :-------- | :--------:| :------: |
| 1001    |   小米 |  1  |
| 1002    |   华为 |  2  |
| 1003    |   锤子 |  3  |
| 1004    |   小米 |  4  |
| 1005    |   华为 |  5  |
| 1006    |   锤子 |  6  |

###### 2.需求分析
> 通过将关联条件作为map输出的key,将两表满足join条件的数据并携带数据所来源的文件信息,发往同一个ReduceTask,在Reduce中进行数据的串联.
> Map阶段处理
> 获取输入文件类型,获取输入数据,对不同文件分别处理,封装Bean对象输出.
> MapTask阶段处理,默认对产品ID排序.
> ReduceTask阶段处理,Reduce方法缓存订单表和产品表数据集合,然后合并.


###### 3.代码实现
###### Create TableBean.class
``` java
package com.geekparkhub.hadoop.table;

import org.apache.hadoop.io.Writable;
import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * TableBean
 * <p>
 */

public class TableBean implements Writable {

    /**
     * Order ID
     * 订单ID
     */
    private String order_id;

    /**
     * Product ID
     * 产品ID
     */
    private String p_id;

    /**
     * Merchandise Quantity
     * 产品数量
     */
    private int amount;

    /**
     * Product Name
     * 产品名称
     */
    private String pname;

    /**
     * Table Mark
     * 表标记
     */
    private String flag;

    /**
     * Empty reference constructor
     * 空参构造器
     */
    public TableBean() {
        super();
    }

    /**
     * Parameter constructor
     * 参数构造器
     * @param order_id
     * @param p_id
     * @param amount
     * @param pname
     * @param flag
     */
    public TableBean(String order_id, String p_id, int amount, String pname, String flag) {
        this.order_id = order_id;
        this.p_id = p_id;
        this.amount = amount;
        this.pname = pname;
        this.flag = flag;
    }

    /**
     * Copy serialization method
     * 复写 序列化方法
     * @param out
     * @throws IOException
     */
    @Override
    public void write(DataOutput out) throws IOException {
        out.writeUTF(order_id);
        out.writeUTF(p_id);
        out.writeInt(amount);
        out.writeUTF(pname);
        out.writeUTF(flag);
    }

    /**
     * Overwrite deserialization method
     * 复写 反序列化方法
     * @param in
     * @throws IOException
     */
    @Override
    public void readFields(DataInput in) throws IOException {
        this.order_id = in.readUTF();
        this.p_id = in.readUTF();
        this.amount = in.readInt();
        this.pname = in.readUTF();
        this.flag = in.readUTF();
    }

    /**
     * Get&Set method
     * Get&Set方法
     */
    public String getOrder_id() {
        return order_id;
    }

    public void setOrder_id(String order_id) {
        this.order_id = order_id;
    }

    public String getP_id() {
        return p_id;
    }

    public void setP_id(String p_id) {
        this.p_id = p_id;
    }

    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public String getPname() {
        return pname;
    }

    public void setPname(String pname) {
        this.pname = pname;
    }

    public String getFlag() {
        return flag;
    }

    public void setFlag(String flag) {
        this.flag = flag;
    }

    /**
     * Override toString() method
     * 复写 toString()方法
     * @return
     */
    @Override
    public String toString() {
        return order_id + "\t" + pname + "\t" + amount + "\t" ;
    }
}
```
###### Create TableMapper.class
``` java
package com.geekparkhub.hadoop.table;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * TableMapper
 * <p>
 */

public class TableMapper extends Mapper<LongWritable, Text, Text, TableBean> {

    /**
     * file name
     * 文件名称
     */
    String name;

    TableBean tableBean = new TableBean();
    Text k = new Text();

    /**
     * Override initialization method
     * 复写 初始化方法
     *
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void setup(Mapper<LongWritable, Text, Text, TableBean>.Context context) throws IOException, InterruptedException {
        /**
         * Get the file name
         * 获取文件名称
         */
        FileSplit inputSplit = (FileSplit) context.getInputSplit();
        name = inputSplit.getPath().getName();
    }

    /**
     * Rewrite the map() method
     * 复写 map()方法
     *
     * @param key
     * @param value
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {

        /**
         * Get the first row of data
         * 获取第一行数据
         */
        String line = value.toString();

        /**
         * If it starts with order, it proves to be the order form, otherwise it is the product list.
         * 如果以order开头,则证明是订单表,否则是产品表
         */
        if (name.startsWith("order")) {

            /**
             * Cutting data
             * 切割数据
             */
            String[] flelds = line.split(" ");

            /**
             * Encapsulate key&value object
             * 封装key&value对象
             */
            tableBean.setOrder_id(flelds[0]);
            tableBean.setP_id(flelds[1]);
            tableBean.setAmount(Integer.parseInt(flelds[2]));
            tableBean.setPname("");
            tableBean.setFlag("order");

            /**
             * Set OID
             * 设置OID
             */
            k.set(flelds[1]);
        } else {

            /**
             * Cutting data
             * 切割数据
             */
            String[] flelds = line.split(" ");

            /**
             * Encapsulate key&value object
             * 封装key&value对象
             */
            tableBean.setOrder_id("");
            tableBean.setP_id(flelds[0]);
            tableBean.setAmount(0);
            tableBean.setPname(flelds[1]);
            tableBean.setFlag("pd");

            /**
             * Set the PID
             * 设置PID
             */
            k.set(flelds[0]);
        }

        /**
         * Write data
         * 写出数据
         */
        context.write(k, tableBean);
    }
}
```

###### Create TableReducer.class
``` java
package com.geekparkhub.hadoop.table;

import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;

import static org.apache.commons.beanutils.BeanUtils.*;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * TableReducer
 * <p>
 */

public class TableReducer extends Reducer<Text, TableBean, TableBean, NullWritable> {
    /**
     * @param key
     * @param values
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void reduce(Text key, Iterable<TableBean> values, Context context) throws IOException, InterruptedException {

        /**
         * Store all order collections
         * 存放所有订单集合
         */
        ArrayList<TableBean> orderBeans = new ArrayList<>();

        /**
         * Store all product collections
         * 存放所有产品集合
         */
        TableBean pdBean = new TableBean();

        /**
         * Loop traversal
         * 循环遍历
         */
        for (TableBean tableBean : values) {
            if ("order".equals(tableBean.getFlag())) {
                TableBean tmp = new TableBean();
                try {
                    copyProperties(tmp, tableBean);
                    orderBeans.add(tableBean);
                } catch (IllegalAccessException e) {
                    e.printStackTrace();
                } catch (InvocationTargetException e) {
                    e.printStackTrace();
                }
            } else {
                try {
                    copyProperties(pdBean, tableBean);
                } catch (IllegalAccessException e) {
                    e.printStackTrace();
                } catch (InvocationTargetException e) {
                    e.printStackTrace();
                }
            }
        }

        /**
         * Loop through the orderBeans
         * 循环遍历 orderBeans
         */
        for (TableBean tableBean : orderBeans) {
            tableBean.setPname(pdBean.getPname());
            context.write(tableBean, NullWritable.get());
        }

    }
}	
```

###### Create TableDriver.class
``` java
package com.geekparkhub.hadoop.table;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * TableDriver
 * <p>
 */

public class TableDriver {

    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {
        /**
         * Preset data input and output path
         * 预设数据输入输出路径
         */
        args = new String[]{"/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_table",
                "/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_table_001"};

        /**
         * 1. Get the Job object
         * 1. 获取Job对象
         */
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf);

        /**
         * 2. Set the jar storage location
         * 2. 设置jar存储位置
         */
        job.setJarByClass(TableDriver.class);

        /**
         * 3. Associate Map and Reduce classes
         * 3. 关联Map和Reduce类
         */
        job.setMapperClass(TableMapper.class);
        job.setReducerClass(TableReducer.class);

        /**
         * 4. Set the key and value types of the output data in the Mapper stage.
         * 4. 设置Mapper阶段输出数据的key与value类型
         */
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(TableBean.class);

        /**
         * 5. Set the key and value types for the final data output
         * 5. 设置最终数据输出的key与value类型
         */
        job.setOutputKeyClass(TableBean.class);
        job.setOutputValueClass(NullWritable.class);

        /**
         * 6. Set the input path and output path
         * 6. 设置输入路径和输出路径
         */
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         * 7. Submit the Job
         * 7. 提交Job
         */
        boolean result = job.waitForCompletion(true);

        /**
         * 8. Log printing
         * 8. 日志打印
         */
        System.exit(result ? 0 : 1);
    }
}
```
> 缺点：这种方式中,合并的操作是在reduce阶段完成,reduce端的处理压力太大,map节点的运算负载则很低,资源利用率不高,且在reduce阶段极易产生数据倾斜.
> 
> 解决方案: map端实现数据合并.
> 解决方案: 在map端缓存多张表,提前处理业务逻辑,这样增加map端业务,减少reduce端数据的压力,尽可能的减少数据倾斜.

##### Map join
> 使用场景: 一张表十分小、一张表很大.

##### Map join案例实操
> 分析:适用于关联表中有小表的情形
> 可以将小表分发到所有的map节点,这样,map节点就可以在本地对自己所读到的大表数据进行合并并输出最终结果,可以大大提高合并操作的并发度,加快处理速度.
##### 代码实现
##### Create DistributedCacheDriver.class
``` java
package com.geekparkhub.hadoop.cache;

import com.geekparkhub.hadoop.table.TableBean;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * DistributedCacheDriver
 * <p>
 */

public class DistributedCacheDriver {
    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException, URISyntaxException {
        /**
         * Preset data input and output path
         * 预设数据输入输出路径
         */
        args = new String[]{"/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_table",
                "/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_table_001"};

        /**
         * 1. Get the Job object
         * 1. 获取Job对象
         */
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf);

        /**
         * 2. Set the jar storage location
         * 2. 设置jar存储位置
         */
        job.setJarByClass(DistributedCacheDriver.class);

        /**
         * 3. Associate Map classes
         * 3. 关联Map类
         */
        job.setMapperClass(DistributedCacheMapper.class);

        /**
         * 4. Set the key and value types for the final data output
         * 4. 设置最终数据输出的key与value类型
         */
        job.setOutputKeyClass(TableBean.class);
        job.setOutputValueClass(NullWritable.class);

        /**
         * 5. Set the input path and output path
         * 5. 设置输入路径和输出路径
         */
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         * 6.Loading cached data
         * 6.加载缓存数据
         */
        job.addCacheFile(new URI("/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_table/pd.txt"));

        /**
         * 7.The logic of the Join on the Map does not require the Reduce phase. Set the number of Reduce Tasks to 0.
         * 7.Map端Join的逻辑不需要Reduce阶段,设置ReduceTask数量为0
         */
        job.setNumReduceTasks(0);

        /**
         * 8. Submit the Job
         * 8. 提交Job
         */
        boolean result = job.waitForCompletion(true);

        /**
         * 9. Log printing
         * 9. 日志打印
         */
        System.exit(result ? 0 : 1);
    }
}
```
##### Create DistributedCacheMapper.class
``` java
package com.geekparkhub.hadoop.cache;

import org.apache.commons.lang.StringUtils;
import org.apache.hadoop.io.IOUtils;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URI;
import java.util.HashMap;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * DistributedCacheMapper
 * <p>
 */

public class DistributedCacheMapper extends Mapper<LongWritable, Text,Text, NullWritable> {

    HashMap<String, String> pdMap = new HashMap<>();
    Text k = new Text();

    /**
     * Override initialization method
     * 复写 初始化方法
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void setup(Mapper<LongWritable,Text,Text,NullWritable>.Context context) throws IOException, InterruptedException {

        /**
         * Get the cache path of the file
         * 获取文件缓存路径
         */
        URI[] cacheFiles = context.getCacheFiles();
        String path = cacheFiles[0].getPath().toString();

        /**
         * Cache smaller data tables
         * 缓存较小的数据表
         */
        BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(path), "UTF-8"));

        /**
         * Loop traversal
         * 循环遍历
         */
        String line;
        while (StringUtils.isNotEmpty(line = reader.readLine())){
            /**
             * Cutting data
             * 切割数据
             */
            String[] fileds = line.split(" ");
            pdMap.put(fileds[0],fileds[1]);
        }
        /**
         * Close resource
         * 关闭资源
         */
        IOUtils.closeStream(reader);
    }

    /**
     * Override map method
     * 复写 map方法
     * @param key
     * @param value
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {

        /**
         * Get a row of data
         * 获取一行数据
         */
        String line = value.toString();

        /**
         * Cutting data
         * 切割数据
         */
        String[] fileds = line.split(" ");

        /**
         * Get pid field attribute
         * 获取pid字段属性
         */
        String pid = fileds[1];

        /**
         * Get pname field attribute
         * 获取pname字段属性
         */
        String pname = pdMap.get(pid);

        /**
         * Data stitching
         * 数据拼接
         */
        line = line +"\t"+ pname;
        k.set(line);

        /**
         * Write data
         * 写出数据
         */
        context.write(k,NullWritable.get());
    }
}
```

#### 7.7.3.8 计数器应用
> Hadoop为每个作业维护若干内置计数器,以描述多项指标.
> 
> 例如,某些计数器记录已处理的字节数和记录数,使用户可监控已处理的输入数据量和已产生的输出数据量.

#### 计数器API
##### 1.采用枚举的方式统计计数
```
enum MyCounter{MALFORORMED,NORMAL}
// 对枚举定义的自定义计数器加1 context.getCounter(MyCounter.MALFORORMED).increment(1);
```
##### 2.采用计数器组/计数器名称的方式统计
```
context.getCounter("counterGroup", "countera").increment(1);
```
##### 3.计数结果在程序运行后的控制台上查看

#### 7.7.3.9 数据清洗(ETL)
> 在运行核心业务Mapreduce程序之前,往往要先对数据进行清洗,清理掉不符合用户要求的数据.
> 
> 清理的过程往往只需要运行mapper程序,不需要运行reduce程序.

##### 数据清洗案例实操-快速清洗版
###### 1.需求
> 去除日志中长度小于等于11的日志.
> web.log 元数据 - 数据行数为14619
> 注意:为了方便演示,已省略一万行日志数据信息
``` accesslog
194.237.142.21 - - [18/Sep/2013:06:49:18 +0000] "GET /wp-content/uploads/2013/07/rstudio-git3.png HTTP/1.1" 304 0 "-" "Mozilla/4.0 (compatible;)"
183.49.46.228 - - [18/Sep/2013:06:49:23 +0000] "-" 400 0 "-" "-"
163.177.71.12 - - [18/Sep/2013:06:49:33 +0000] "HEAD / HTTP/1.1" 200 20 "-" "DNSPod-Monitor/1.0"
163.177.71.12 - - [18/Sep/2013:06:49:36 +0000] "HEAD / HTTP/1.1" 200 20 "-" "DNSPod-Monitor/1.0"
101.226.68.137 - - [18/Sep/2013:06:49:42 +0000] "HEAD / HTTP/1.1" 200 20 "-" "DNSPod-Monitor/1.0"
101.226.68.137 - - [18/Sep/2013:06:49:45 +0000] "HEAD / HTTP/1.1" 200 20 "-" "DNSPod-Monitor/1.0"
60.208.6.156 - - [18/Sep/2013:06:49:48 +0000] "GET /wp-content/uploads/2013/07/rcassandra.png HTTP/1.0" 200 185524 "http://cos.name/category/software/packages/" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36"
222.68.172.190 - - [18/Sep/2013:06:49:57 +0000] "GET /images/my.jpg HTTP/1.1" 200 19939 "http://www.angularjs.cn/A00n" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36"
222.68.172.190 - - [18/Sep/2013:06:50:08 +0000] "-" 400 0 "-" "-"
183.195.232.138 - - [18/Sep/2013:06:50:16 +0000] "HEAD / HTTP/1.1" 200 20 "-" "DNSPod-Monitor/1.0"
183.195.232.138 - - [18/Sep/2013:06:50:16 +0000] "HEAD / HTTP/1.1" 200 20 "-" "DNSPod-Monitor/1.0"
```

``` prolog
194.237.142.21 - - [18/Sep/2013:06:49:18 +0000] "GET /wp-content/uploads/2013/07/rstudio-git3.png HTTP/1.1" 304 0 "-" "Mozilla/4.0 (compatible;)"
```

``` prolog
 194.237.142.21 | (表示记录客户端的ip地址)
 - - | (表示记录客户端用户名称,忽略属性)
 [18/Sep/2013:06:49:18 +0000] | (表示记录访问时间与时区)
 "GET /wp-content/uploads/2013/07/rstudio-git3.png HTTP/1.1" | (表示记录请求的url与http协议)
 304 | (表示记录请求状态,成功是200)
 0 | (表示记录发送给客户端文件主体内容大小)
 "-" | (表示用来记录用户访问页面链接途径)
 "Mozilla/4.0 (compatible;)" | (表示记录客户浏览器的相关信息)
```

> 期望输出数据 每行字段长度大于11
###### 2.需求分析
> 需要在Map阶段对输入的数据根据规则进行过滤清洗.
###### 3.代码实现
###### Create LogMapper.class
``` java
package com.geekparkhub.hadoop.weblog;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * LogMapper
 * <p>
 */

public class LogMapper extends Mapper<LongWritable, Text, Text, NullWritable> {

    /**
     * Rewrite the map() method
     * 复写 map()方法
     *
     * @param key
     * @param value
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */

    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {

        /**
         * Get a row of data
         * 获取一行数据
         */
        String line = value.toString();

        /**
         * Analytical data
         * 解析数据
         */
        boolean result = parseLog(line, context);

        /**
         * If the parsing fails, skip the return directly.
         * 如果解析失败,则直接跳过返回
         */
        if (!result) {
            return;
        }
        /**
         * If the parsing is successful, write out the data.
         * 如果解析成功,写出数据
         */
        context.write(value, NullWritable.get());
    }

    /**
     * Parsing log method
     * 解析日志方法
     *
     * @param line
     * @param context
     * @return
     */
    private boolean parseLog(String line, Context context) {

        /**
         * Cutting data
         * 切割数据
         */
        String[] flelds = line.split(" ");

        /**
         * Return true if the log length is greater than 11.
         * 如果日志长度大于11,则返回true
         */
        if (flelds.length > 11) {
            /**
             * Introduce a counter, in the Map phase, the number that is judged to be true.
             * 引入计数器,在Map阶段,判断为true的个数
             */
            context.getCounter("map", "true").increment(1);
            return true;
        } else {
            /**
             * Introduce a counter, in the Map phase, the number that is judged to be false.
             * 引入计数器,在Map阶段,判断为false的个数
             */
            context.getCounter("map", "false").increment(1);
            return false;
        }
    }
}
```
###### Create LogDriver.class
``` java
package com.geekparkhub.hadoop.weblog;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import java.io.IOException;


/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * LogDriver
 * <p>
 */

public class LogDriver {
    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {

        /**
         * Preset data input and output path
         * 预设数据输入输出路径
         */
        args = new String[]{"/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_log",
                "/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_log_001"};

        /**
         * 1. Get the Job object
         * 1. 获取Job对象
         */
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf);

        /**
         * 2. Set the jar storage location
         * 2. 设置jar存储位置
         */
        job.setJarByClass(LogDriver.class);

        /**
         * 3. Associate Map classes
         * 3. 关联Map类
         */
        job.setMapperClass(LogMapper.class);

        /**
         * 4. Set the key and value types for the final data output
         * 4. 设置最终数据输出的key与value类型
         */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(NullWritable.class);

        /**
         * 6.Set the number of Reduce Tasks to 0.
         * 6.设置ReduceTask数量为0
         */
        job.setNumReduceTasks(0);

        /**
         * 5. Set the input path and output path
         * 5. 设置输入路径和输出路径
         */
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         * 7. Submit the Job
         * 7. 提交Job
         */
        boolean result = job.waitForCompletion(true);

        /**
         * 8. Log printing
         * 8. 日志打印
         */
        System.exit(result ? 0 : 1);
    }
}
```
###### 4.运行查看结果
> 14619为总行数,在map阶段已通过13770,已过滤掉849行数据
``` prolog
Map-Reduce Framework
		Map input records=14619
		Map output records=13770
		Input split bytes=173
		Spilled Records=0
		Failed Shuffles=0
		Merged Map outputs=0
		GC time elapsed (ms)=9
		Total committed heap usage (bytes)=324534272
	map
		false=849
		true=13770
	File Input Format Counters 
		Bytes Read=3040376
	File Output Format Counters 
		Bytes Written=2993323
```

##### 数据清洗案例实操-复杂清洗版
###### 1.需求:
> 对web访问日志中的各字段识别切分,去除日志中不合法的记录,根据统计需求生成各类访问请求过滤数据.
###### 2.数据源同上
``` prolog
194.237.142.21 - - [18/Sep/2013:06:49:18 +0000] "GET /wp-content/uploads/2013/07/rstudio-git3.png HTTP/1.1" 304 0 "-" "Mozilla/4.0 (compatible;)"
```
``` prolog
 194.237.142.21 | (表示记录客户端的ip地址)
 - - | (表示记录客户端用户名称,忽略属性)
 [18/Sep/2013:06:49:18 +0000] | (表示记录访问时间与时区)
 "GET /wp-content/uploads/2013/07/rstudio-git3.png HTTP/1.1" | (表示记录请求的url与http协议)
 304 | (表示记录请求状态,成功是200)
 0 | (表示记录发送给客户端文件主体内容大小)
 "-" | (表示用来记录用户访问页面链接途径)
 "Mozilla/4.0 (compatible;)" | (表示记录客户浏览器的相关信息)
```
###### 3.代码实现
###### Create LogBean.class
``` java
package com.geekparkhub.hadoop.logclean;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * LogBean
 * <p>
 */

public class LogBean {

    /**
     *
     * 194.237.142.21 | (Indicating the ip address of the recording client.)
     * - - | (Indicating the record client user name, ignoring attributes.)
     * [18/Sep/2013:06:49:18 +0000] | (Indicating record access time With the time zone.)
     * "GET /wp-content/uploads/2013/07/rstudio-git3.png HTTP/1.1" | (indicating the url of the request request and the http protocol.)
     * 304 | (indicating the status of the record request, the success is 200.)
     * 0 | (Indicating the size of the content of the file sent to the client file.)
     * "-" | (indicating the path used to record the user's access to the page.)
     * "Mozilla/4.0 (compatible;)" | (Indicates information about the client's browser.)
     *
     *  194.237.142.21 | (表示记录客户端的ip地址)
     *  - - | (表示记录客户端用户名称,忽略属性)
     *  [18/Sep/2013:06:49:18 +0000] | (表示记录访问时间与时区)
     *  "GET /wp-content/uploads/2013/07/rstudio-git3.png HTTP/1.1" | (表示记录请求的url与http协议)
     *  304 | (表示记录请求状态,成功是200)
     *  0 | (表示记录发送给客户端文件主体内容大小)
     *  "-" | (表示用来记录用户访问页面链接途径)
     *  "Mozilla/4.0 (compatible;)" | (表示记录客户浏览器的相关信息)
     *
     */

    /**
     * Indicates the ip address of the recording client.
     * 表示记录客户端的ip地址.
     */
    private String remote_addr;

    /**
     * Indicates the record client user name, ignoring attributes.
     * 表示记录客户端用户名称,忽略属性.
     */
    private String remote_user;

    /**
     * Indicates the record access time and time zone.
     * 表示记录访问时间与时区.
     */
    private String time_local;

    /**
     * Indicates the url of the record request and the http protocol.
     * 表示记录请求的url与http协议.
     */
    private String request;

    /**
     * Indicates the status of the record request. The success is 200.
     * 表示记录请求状态,成功是200.
     */
    private String status;

    /**
     * Indicates the size of the body of the file sent to the client.
     * 表示记录发送给客户端文件主体内容大小.
     */
    private String body_bytes_sent;

    /**
     * Indicates the path used to record the user's access to the page.
     * 表示用来记录用户访问页面链接途径.
     */
    private String http_referer;

    /**
     * Indicates information about the client's browser.
     * 表示记录客户浏览器的相关信息.
     */
    private String http_user_agent;

    /**
     * Determine if the data is legal.
     * 判断数据是否合法.
     */
    private boolean valid = true;

    /**
     * Get & Set method
     * Get & Set 方法
     *
     * @return
     */
    public String getRemote_addr() {
        return remote_addr;
    }

    public void setRemote_addr(String remote_addr) {
        this.remote_addr = remote_addr;
    }

    public String getRemote_user() {
        return remote_user;
    }

    public void setRemote_user(String remote_user) {
        this.remote_user = remote_user;
    }

    public String getTime_local() {
        return time_local;
    }

    public void setTime_local(String time_local) {
        this.time_local = time_local;
    }

    public String getRequest() {
        return request;
    }

    public void setRequest(String request) {
        this.request = request;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getBody_bytes_sent() {
        return body_bytes_sent;
    }

    public void setBody_bytes_sent(String body_bytes_sent) {
        this.body_bytes_sent = body_bytes_sent;
    }

    public String getHttp_referer() {
        return http_referer;
    }

    public void setHttp_referer(String http_referer) {
        this.http_referer = http_referer;
    }

    public String getHttp_user_agent() {
        return http_user_agent;
    }

    public void setHttp_user_agent(String http_user_agent) {
        this.http_user_agent = http_user_agent;
    }

    public boolean isValid() {
        return valid;
    }

    public void setValid(boolean valid) {
        this.valid = valid;
    }

    /**
     * To String method
     * toString方法
     */
    @Override
    public String toString() {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append(this.valid);
        stringBuilder.append("\001").append(this.remote_addr);
        stringBuilder.append("\001").append(this.remote_user);
        stringBuilder.append("\001").append(this.time_local);
        stringBuilder.append("\001").append(this.request);
        stringBuilder.append("\001").append(this.status);
        stringBuilder.append("\001").append(this.body_bytes_sent);
        stringBuilder.append("\001").append(this.http_referer);
        stringBuilder.append("\001").append(this.http_user_agent);
        return stringBuilder.toString();
    }
}
```
###### Create LogMappers.class
``` java
package com.geekparkhub.hadoop.logclean;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * LogMappers
 * <p>
 */

public class LogMappers extends Mapper<LongWritable, Text, Text, NullWritable> {

    Text k = new Text();

    /**
     * Copy map method
     * 复写 map方法
     *
     * @param key
     * @param value
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {

        /**
         * Get a row of data
         * 获取一行数据
         */
        String line = value.toString();

        /**
         * Is the parsing log legal?
         * 解析日志是否合法
         */
        LogBean logBean = pressLog(line);

        /**
         * If the data is not legal, return directly
         * 如果数据不合法,则直接返回
         */
        if (!logBean.isValid()) {
            return;
        }

        /**
         * Package object
         * 封装对象
         */
        k.set(logBean.toString());

        /**
         * Write data
         * 写出数据
         */
        context.write(k, NullWritable.get());
    }

    /**
     * Parsing log method
     * 解析日志方法
     *
     * @param line
     * @return
     */
    private LogBean pressLog(String line) {
        LogBean logBean = new LogBean();

        /**
         * Cutting data
         * 切割数据
         */
        String[] fields = line.split(" ");

        /**
         * Encapsulate data if the log length is greater than 11.
         * 如果日志长度大于11,则封装数据
         */
        if (fields.length > 11) {
            logBean.setRemote_addr(fields[0]);
            logBean.setRemote_user(fields[1]);
            logBean.setTime_local(fields[3].substring(1));
            logBean.setRequest(fields[6]);
            logBean.setStatus(fields[8]);
            logBean.setBody_bytes_sent(fields[9]);
            logBean.setHttp_referer(fields[10]);

            /**
             * Splice data if the client browser's information is greater than 12.
             * 如果客户浏览器的信息大于12,则拼接数据
             */
            if (fields.length > 12) {
                logBean.setHttp_user_agent(fields[11] + " " + fields[12]);
            } else {
                logBean.setHttp_user_agent(fields[11]);
            }

            /**
             * Clean the data if the network status is greater than 400=HTTPERROR
             * 如果网络状态大于400=HTTPERROR,则清洗该数据
             */
            if (Integer.parseInt(logBean.getStatus()) >= 400) {
                logBean.setValid(false);
            }
        } else {
            logBean.setValid(false);
        }
        return logBean;
    }
}
```
###### Create LogDrivers.class
``` java
package com.geekparkhub.hadoop.logclean;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * LogDrivers
 * <p>
 */

public class LogDrivers {
    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {

        /**
         * Preset data input and output path
         * 预设数据输入输出路径
         */
        args = new String[]{"/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_log",
                "/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_log_001"};

        /**
         * 1. Get the Job object
         * 1. 获取Job对象
         */
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf);

        /**
         * 2. Set the jar storage location
         * 2. 设置jar存储位置
         */
        job.setJarByClass(LogDrivers.class);

        /**
         * 3. Associate Map classes
         * 3. 关联Map类
         */
        job.setMapperClass(LogMappers.class);

        /**
         * 4. Set the key and value types for the final data output
         * 4. 设置最终数据输出的key与value类型
         */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(NullWritable.class);

        /**
         * 6.Set the number of Reduce Tasks to 0.
         * 6.设置ReduceTask数量为0
         */
        job.setNumReduceTasks(0);

        /**
         * 5. Set the input path and output path
         * 5. 设置输入路径和输出路径
         */
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         * 7. Submit the Job
         * 7. 提交Job
         */
        boolean result = job.waitForCompletion(true);

        /**
         * 8. Log printing
         * 8. 日志打印
         */
        System.exit(result ? 0 : 1);
    }
}
```
###### 4.运行并查看结果
``` prolog
true194.237.142.21-18/Sep/2013:06:49:18/wp-content/uploads/2013/07/rstudio-git3.png3040"-""Mozilla/4.0 (compatible;)"
true163.177.71.12-18/Sep/2013:06:49:33/20020"-""DNSPod-Monitor/1.0"
true163.177.71.12-18/Sep/2013:06:49:36/20020"-""DNSPod-Monitor/1.0"
true101.226.68.137-18/Sep/2013:06:49:42/20020"-""DNSPod-Monitor/1.0"
true101.226.68.137-18/Sep/2013:06:49:45/20020"-""DNSPod-Monitor/1.0"
```


#### 7.7.3.10 MapReduce 开发总结
##### 1.输入数据接口:
> InputFormat默认使用的实现类是:TextInputFormat
> 
> TextInputFormat的功能逻辑是:一次读一行文本,然后将该行的起始偏移量作为key,行内容作为value返回.
> 
> KeyValueTextInputFormat每一行均为一条记录,被分隔符分割为key,value.默认分隔符是tab(\t).
> 
> NlineInputFormat按照指定的行数N来划分切片.
> 
> CombineTextInputFormat可以把多个小文件合并成一个切片处理,提高处理效率.
> 
> 开发者还可以自定义InputFormat.

##### 2.逻辑处理接口:Mapper
> 开发者根据业务需求实现其中三个方法: map() | setup() | cleanup () 
##### 3.Partitioner分区
> Partitioner分区有默认实现HashPartitioner,逻辑是根据key的哈希值和numReduces来返回一个分区号.
``` java
key.hashCode()&Integer.MAXVALUE % numReduces
```
> 如果业务上有特别的需求,可以自定义分区.
##### 4.Comparable排序
> 当自定义的对象作为key来输出时,就必须要实现WritableComparable接口,重写其中的compareTo()方法.
> 
> 部分排序:对最终输出的每一个文件进行内部排序.
> 
> 全排序:对所有数据进行排序，通常只有一个Reduce.
> 
> 二次排序:排序的条件有两个.
##### 5.Combiner合并
> Combiner合并可以提高程序执行效率,减少IO传输,但是使用时必须不能影响原有的业务处理结果.
##### 6.reduce端分组:Groupingcomparator
> 在Reduce端对key进行分组,应用于:在接收的key为bean对象时,想让一个或几个字段相同(全部字段比较不相同)的key进入到一个reduce方法时,可以采用分组排序.
> 
##### 7.逻辑处理接口:Reducer
> 用户根据业务需求实现其中三个方法：reduce()  | setup() | cleanup()
##### 8.输出数据接口:
> OutputFormat默认实现类是TextOutputFormat.
> 
> 功能逻辑是:将每一个KV对向目标文本文件中输出为一行.
> 
> SequenceFileOutputFormat将它的输出写为一个顺序文件.如果输出需要作为后续MapReduce任务的输入,这便是一种好的输出格式,因为它的格式紧凑,很容易被压缩.
> 用户还可以自定义OutputFormat.


### 7.7.4 Hadoop 数据压缩
#### 数据压缩 概述
> 压缩技术能够有效减少底层存储系统(HDFS)读写字节数,压缩提高了网络带宽和磁盘空间的效率.
> 在Hadoop下,尤其是数据规模很大和工作负载密集的情况下,使用数据压缩显得非常重要,在这种情况下,I/O操作和网络数据传输要花大量的时间,还有Shuffle与Merge过程同样也面临着巨大的I/O压力.
> 
> 鉴于磁盘I/O和网络带宽是Hadoop的宝贵资源,数据压缩对于节省资源、最小化磁盘I/O和网络传输非常有帮助。
> 不过,尽管压缩与解压操作的CPU开销不高,其性能的提升和资源的节省并非没有代价.
> 
> 如果磁盘I/O和网络带宽影响了MapReduce作业性能,在任意MapReduce阶段启用压缩都可以改善端到端处理时间并减少I/O和网络流量.

##### 压缩策略和原则
> 压缩是提高Hadoop运行效率的一种优化策略.
> 
> 通过压缩编码对Mapper或者Reducer的输出进行压缩,以减少磁盘IO,提高MR程序运行速度.
> 
> 注意:采用压缩技术减少了磁盘IO,但是同时也增加了cpu运算负担,所以压缩特性运用得当能提高性能,但运用不当也可能降低性能.

##### 压缩基本原则
> 1.运算密集型job,少用压缩.
> 2.IO密集型job,多用压缩.

#### MapReduce 支持压缩编码

| 压缩格式 | hadoop自带 | 算法 | 文件扩展名 | 是否可切分 | 换成压缩格式后,原来的程序是否需要修改 |
| :-------- | --------:| :------: | :------: | :------: | :------: |
| DEFAULT  | 是,直接使用 | DEFAULT | .default | 否 | 和文本处理一样,不需要修改 |
| Gzip  | 是,直接使用 | DEFAULT | .gz | 否 | 和文本处理一样,不需要修改 |
| bzip2  | 是,直接使用 | bzip2 | .bz2 | 是 | 和文本处理一样,不需要修改 |
| LZO  | 否,需要安装 | LZO | .lzo | 是 | 需要建索引,还需要指定输入格式 |
| Snappy  | 否,需要安装 | Snappy | .snappy | 否 | 和文本处理一样,不需要修改 |

> 为了支持多种压缩/解压缩算法,Hadoop引入了编码/解码器
| 压缩格式 | 对应的编码/解码器 |
| :-------- | --------:|
| DEFLATE | org.apache.hadoop.io.compress.DefaultCodec |
| gzip    | org.apache.hadoop.io.compress.BZip2Codec |
| bzip2    |org.apache.hadoop.io.compress.BZip2Codec|
| LZO    | com.hadoop.compression.lzo.LzopCodec |
| Snappy    | org.apache.hadoop.io.compress.SnappyCodec |

> 压缩性能的比较
| 压缩算法 | 原始文件大小| 压缩文件大小| 压缩速度 | 解压速度 |
| :-------- | --------:| ------: | :------: | :------: |
| gzip   |   8.3GB |  1.8GB  | 17.5MB/s | 58MB/s   |
| bzip2  |   8.3GB |  1.1GB  | 2.4MB/s  | 9.5MB/s  |
| LZO    |   8.3GB |  2.9GB  | 49.3MB/s | 74.6MB/s |
| snappy |   8.3GB |  1.5GB  | 250MB/s | 500MB/s |


#### 压缩方式选择
##### Gzip压缩
> 优点: 压缩率比较高,而且压缩/解压速度也比较快,hadoop本身支持,在应用中处理gzip格式的文件就和直接处理文本一样,大部分linux系统都自带gzip命令,使用方便.
> 
> 缺点: 不支持split.
> 
> 应用场景: 当每个文件压缩之后在130M以内的(1个块大小内),都可以考虑用gzip压缩格式.
> 
> 例如说一天或者一个小时的日志压缩成一个gzip文件,运行mapreduce程序的时候通过多个gzip文件达到并发,hive程序,streaming程序,和java写的mapreduce程序完全和文本处理一样,压缩之后原来的程序不需要做任何修改.

##### Bzip压缩
> 优点: 支持split,具有很高的压缩率,比gzip压缩率都高,hadoop本身支持,但不支持native,在linux系统下自带bzip2命令,使用方便.
> 
> 缺点: 压缩/解压速度慢,不支持native.
> 
> 应用场景: 适合对速度要求不高,但需要较高的压缩率的时候,可以作为mapreduce作业的输出格式,或者输出之后的数据比较大,处理之后的数据需要压缩存档减少磁盘空间并且以后数据用得比较少的情况,或者对单个很大的文本文件想压缩减少存储空间,同时又需要支持split,而且兼容之前的应用程序(即应用程序不需要修改)的情况.

##### Lzo压缩
> 优点: 压缩/解压速度也比较快,合理的压缩率,支持split,是hadoop中最流行的压缩格式,可以在linux系统下安装lzop命令,使用方便.
> 
> 缺点: 压缩率比gzip要低一些,hadoop本身不支持,需要安装,在应用中对lzo格式的文件需要做一些特殊处理(为了支持split需要建索引,还需要指定inputformat为lzo格式).
> 
> 应用场景: 一个很大的文本文件,压缩之后还大于200M以上的可以考虑,而且单个文件越大,lzo优点越越明显.

##### Snappy 压缩
> 优点: 高速压缩速度和合理的压缩率.
> 
> 缺点: 不支持split,压缩率比gzip要低,hadoop本身不支持,需要安装.
> 
> 应用场景: 当Mapreduce作业的Map输出的数据比较大的时候,作为Map到Reduce的中间数据的压缩格式,或者作为一个Mapreduce作业的输出和另外一个Mapreduce作业的输入.

#### 压缩位置选择
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_035.jpg)

#### 压缩参数配置
> 要在Hadoop中启用压缩,可以配置如下参数：
| 参数      |     默认值 |   阶段   |   建议   |
| :-------- | --------:| :------: | :------: |
| io.compression.codecs (在core-site.xml中配置) | org.apache.hadoop.io.compress.DefaultCodec, org.apache.hadoop.io.compress.GzipCodec,org.apache.hadoop.io.compress.BZip2Codec  | 输入压缩 | Hadoop使用文件扩展名判断是否支持某种编解码器 |
| mapreduce.map.output.compress (在mapred-site.xml中配置) | false  | mapper输出 |  这个参数设为true启用压缩 |
| mapreduce.map.output.compress.codec (在core-site.xml中配置) | field2 | field3 |  field3 |
| io.compression.codecs (在mapred-site.xml中配置) | org.apache.hadoop.io.compress.DefaultCodec | mapper输出 | 使用LZO或snappy编解码器在此阶段压缩数据 |
| mapreduce.output.fileoutputformat.compress (在mapred-site.xml中配置) | false | reducer输出 |  这个参数设为true启用压缩 |
| mapreduce.output.fileoutputformat.compress.codec(在mapred-site.xml中配置) | org.apache.hadoop.io.compress. DefaultCodec | reducer输出 |  使用标准工具或者编解码器,如gzip和bzip2 |
| mapreduce.output.fileoutputformat.compress.type (在mapred-site.xml中配置) | RECORD | reducer输出 |  SequenceFile输出使用的压缩类型:NONE和BLOCK  |


#### 压缩实操案例
##### 数据流的压缩和解压缩
> CompressionCodec有两个方法可以用于轻松地压缩或解压缩数据,要想对正在被写入一个输出流的数据进行压缩,我们可以使用`createOutputStream(OutputStreamout)`方法创建一个`CompressionOutputStream`,将其以压缩格式写入底层的流.
> 
> 相反,要想对从输入流读取而来的数据进行解压缩,则调用`createInputStream(InputStreamin)`函数,从而获得一个`CompressionInputStream`,从而从底层的流读取未压缩的数据.
###### Create TestCompress.class
> 使用BZip2格式 进行压缩
``` java
package com.geekparkhub.hadoop.compress;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.IOUtils;
import org.apache.hadoop.io.compress.CompressionCodec;
import org.apache.hadoop.io.compress.CompressionOutputStream;
import org.apache.hadoop.util.ReflectionUtils;
import java.io.*;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * TestCompress
 * <p>
 */

public class TestCompress {
    public static void main(String[] args) throws IOException, ClassNotFoundException {

        /**
         * Get the specified compressed file and set it to compress using B Zip 2 format.
         * 获取指定压缩文件,并设置使用BZip2格式进行压缩
         */
        compress("/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_combine_textInput_format/b.txt"
                , "org.apache.hadoop.io.compress.BZip2Codec");
    }

    /**
     * Compression method
     * 压缩方法
     *
     * @param fileName
     * @param method
     */
    private static void compress(String fileName, String method) throws IOException, ClassNotFoundException {

        /**
         * 获取输入流
         */
        FileInputStream fis = new FileInputStream(new File(fileName));

        /**
         * Pass the method parameter to the compression mode tool class through the reflection mechanism,
         * and set the encoding mode to obtain the compression extension.
         * 通过反射机制,将method参数传递给压缩方式工具类,并设置编码方式,获取压缩扩展名
         */
        Class classCodec = Class.forName(method);
        CompressionCodec codec = (CompressionCodec) ReflectionUtils.newInstance(classCodec, new Configuration());

        /**
         * Get the output stream
         * 获取输出流
         */
        FileOutputStream fos = new FileOutputStream(fileName + codec.getDefaultExtension());

        /**
         * Set the obtained normal output stream to the compressed output stream
         * 将获取到的普通输出流,设置为压缩输出流
         */
        CompressionOutputStream cos = codec.createOutputStream(fos);

        /**
         * Copy between streams
         * 流之间对拷
         */
        IOUtils.copyBytes(fis, cos, 1024 * 1024, false);

        /**
         * Close resource
         * 关闭资源
         */
        IOUtils.closeStream(cos);
        IOUtils.closeStream(fos);
        IOUtils.closeStream(fis);
    }
}
```
> 使用Gzip格式 进行压缩
``` java
package com.geekparkhub.hadoop.compress;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.IOUtils;
import org.apache.hadoop.io.compress.CompressionCodec;
import org.apache.hadoop.io.compress.CompressionOutputStream;
import org.apache.hadoop.util.ReflectionUtils;
import java.io.*;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * TestCompress
 * <p>
 */

public class TestCompress {
    public static void main(String[] args) throws IOException, ClassNotFoundException {

        /**
         * Get the specified compressed file and set it to compress using Gzip format.
         * 获取指定压缩文件,并设置使用Gzip格式进行压缩
         */
        compress("/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_combine_textInput_format/b.txt"
                , "org.apache.hadoop.io.compress.GzipCodec");
    }

    /**
     * Compression method
     * 压缩方法
     *
     * @param fileName
     * @param method
     */
    private static void compress(String fileName, String method) throws IOException, ClassNotFoundException {

        /**
         * 获取输入流
         */
        FileInputStream fis = new FileInputStream(new File(fileName));

        /**
         * Pass the method parameter to the compression mode tool class through the reflection mechanism,
         * and set the encoding mode to obtain the compression extension.
         * 通过反射机制,将method参数传递给压缩方式工具类,并设置编码方式,获取压缩扩展名
         */
        Class classCodec = Class.forName(method);
        CompressionCodec codec = (CompressionCodec) ReflectionUtils.newInstance(classCodec, new Configuration());

        /**
         * Get the output stream
         * 获取输出流
         */
        FileOutputStream fos = new FileOutputStream(fileName + codec.getDefaultExtension());

        /**
         * Set the obtained normal output stream to the compressed output stream
         * 将获取到的普通输出流,设置为压缩输出流
         */
        CompressionOutputStream cos = codec.createOutputStream(fos);

        /**
         * Copy between streams
         * 流之间对拷
         */
        IOUtils.copyBytes(fis, cos, 1024 * 1024, false);

        /**
         * Close resource
         * 关闭资源
         */
        IOUtils.closeStream(cos);
        IOUtils.closeStream(fos);
        IOUtils.closeStream(fis);
    }
}
```
> 使用DefaultCodec格式 进行压缩
``` java
package com.geekparkhub.hadoop.compress;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.IOUtils;
import org.apache.hadoop.io.compress.CompressionCodec;
import org.apache.hadoop.io.compress.CompressionOutputStream;
import org.apache.hadoop.util.ReflectionUtils;
import java.io.*;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * TestCompress
 * <p>
 */

public class TestCompress {
    public static void main(String[] args) throws IOException, ClassNotFoundException {

        /**
         * Get the specified compressed file and set it to compress using DefaultCodec Codec format.
         * 获取指定压缩文件,并设置使用DefaultCodec格式进行压缩
         */
        compress("/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_combine_textInput_format/b.txt"
                , "org.apache.hadoop.io.compress.DefaultCodec");
    }

    /**
     * Compression method
     * 压缩方法
     *
     * @param fileName
     * @param method
     */
    private static void compress(String fileName, String method) throws IOException, ClassNotFoundException {

        /**
         * 获取输入流
         */
        FileInputStream fis = new FileInputStream(new File(fileName));

        /**
         * Pass the method parameter to the compression mode tool class through the reflection mechanism,
         * and set the encoding mode to obtain the compression extension.
         * 通过反射机制,将method参数传递给压缩方式工具类,并设置编码方式,获取压缩扩展名
         */
        Class classCodec = Class.forName(method);
        CompressionCodec codec = (CompressionCodec) ReflectionUtils.newInstance(classCodec, new Configuration());

        /**
         * Get the output stream
         * 获取输出流
         */
        FileOutputStream fos = new FileOutputStream(fileName + codec.getDefaultExtension());

        /**
         * Set the obtained normal output stream to the compressed output stream
         * 将获取到的普通输出流,设置为压缩输出流
         */
        CompressionOutputStream cos = codec.createOutputStream(fos);

        /**
         * Copy between streams
         * 流之间对拷
         */
        IOUtils.copyBytes(fis, cos, 1024 * 1024, false);

        /**
         * Close resource
         * 关闭资源
         */
        IOUtils.closeStream(cos);
        IOUtils.closeStream(fos);
        IOUtils.closeStream(fis);
    }
}
```
###### 运行并查看结果
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_036.jpg)

###### Create TestDecompression.class
> 解压文件
``` java
package com.geekparkhub.hadoop.compress;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;
import org.apache.hadoop.io.compress.CompressionCodec;
import org.apache.hadoop.io.compress.CompressionCodecFactory;
import org.apache.hadoop.io.compress.CompressionInputStream;
import java.io.*;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * TestDecompression
 * <p>
 */

public class TestDecompression {

    public static void main(String[] args) throws IOException {

        /**
         * Get compressed file.
         * 获取压缩文件
         */
        decompress("/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_combine_textInput_format/b.txt.bz2");
    }

    /**
     * Decompression method
     * 解压方法
     *
     * @param fileName
     */
    private static void decompress(String fileName) throws IOException {

        /**
         * Check compression method
         * 检查压缩方式
         */
        CompressionCodecFactory factory = new CompressionCodecFactory(new Configuration());
        CompressionCodec codec = factory.getCodec(new Path(fileName));

        /**
         * Determine if the compressed file is empty
         * 判断压缩文件是否为空
         */
        if (codec == null) {
            System.out.println("当前格式,不支持解压! & Current format, does not support decompression!");
            return;
        }

        /**
         * Get the input stream
         * 获取输入流
         */
        FileInputStream fis = new FileInputStream(new File(fileName));
        CompressionInputStream cis = codec.createInputStream(fis);


        /**
         * Get the output stream
         * 获取输出流
         */
        FileOutputStream fos = new FileOutputStream(new File(fileName + ".decode"));

        /**
         * Stream copy
         * 流对拷
         */
        IOUtils.copyBytes(cis, fos, 1024 * 1024, false);

        /**
         * Close resource
         * 关闭资源
         */
        IOUtils.closeStream(fos);
        IOUtils.closeStream(cis);
        IOUtils.closeStream(fis);
    }
}
```
##### Map输出端采用压缩
> 即使MapReduce的输入输出文件都是未压缩的文件,但仍然可以对map任务的中间结果输出做压缩,因为它要写在硬盘并且通过网络传输到reduce节点,对其压缩可以提高很多性能,这些工作只要设置两个属性即可.
> 
> 1.hadoop源码支持提供的压缩格式有: BZip2Codec 、DefaultCodec
> 基于万能的WorkCount案例来实操一下吧
> 只需要在WordcountDriver中设置属性即可
``` java
package com.geekparkhub.hadoop.wordcount;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.compress.BZip2Codec;
import org.apache.hadoop.io.compress.CompressionCodec;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.log4j.Logger;

import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * WordcountDriver
 * <p>
 */

public class WordcountDriver {

    /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(WordcountDriver.class);

    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {

        args = new String[]{"/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_combine_textInput_format",
                "/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_combine_textInput_format_004"};

        Configuration configuration = new Configuration();
        
        /**
         * Enable map output compression
         * 开启map端输出压缩
         */
        configuration.setBoolean("mapreduce.map.output.compress", true);

        /**
         * Set the map side output compression method
         * 设置map端输出压缩方式
         */
        configuration.setClass("mapreduce.map.output.compress.codec",  BZip2Codec.class, CompressionCodec.class);

        /**
         * 1. Get the Job object
         * 1. 获取Job对象
         */
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf);

        /**
         * 2. Set the jar storage location
         * 2. 设置jar存储位置
         */
        job.setJarByClass(WordcountDriver.class);

        /**
         * Set set Combiner Class
         *设置setCombinerClass
         */
        job.setCombinerClass(WordcountCombiner.class);

        /**
         * 3. Associate Map and Reduce classes
         * 3. 关联Map和Reduce类
         */
        job.setMapperClass(WordcountMapper.class);
        job.setReducerClass(WordcountReducer.class);

        /**
         * 4. Set the key and value types of the output data in the Mapper stage.
         * 4. 设置Mapper阶段输出数据的key与value类型
         */
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(IntWritable.class);

        /**
         * 5. Set the key and value types for the final data output
         * 5. 设置最终数据输出的key与value类型
         */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        /**
         * 6. Set the input path and output path
         * 6. 设置输入路径和输出路径
         */
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         * 7. Submit the Job
         * 7. 提交Job
         */
        boolean result = job.waitForCompletion(true);

        /**
         * 8. Log printing
         * 8. 日志打印
         */
        System.exit(result ? 0 : 1);
    }
}
```

##### Reduce输出端采用压缩
> 基于万能的WorkCount案例来实操一下吧
> 只需要在WordcountDriver中设置属性即可
``` java
package com.geekparkhub.hadoop.wordcount;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.compress.BZip2Codec;
import org.apache.hadoop.io.compress.CompressionCodec;
import org.apache.hadoop.io.compress.DefaultCodec;
import org.apache.hadoop.io.compress.GzipCodec;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.log4j.Logger;
import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * WordcountDriver
 * <p>
 */

public class WordcountDriver {

    /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(WordcountDriver.class);

    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {

        args = new String[]{"/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_combine_textInput_format",
                "/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_combine_textInput_format_004"};

        Configuration configuration = new Configuration();

        /**
         * Enable map output compression
         * 开启map端输出压缩
         */
        configuration.setBoolean("mapreduce.map.output.compress", true);

        /**
         * Set the map side output compression method
         * 设置map端输出压缩方式
         */
        configuration.setClass("mapreduce.map.output.compress.codec", BZip2Codec.class, CompressionCodec.class);

        /**
         * 1. Get the Job object
         * 1. 获取Job对象
         */
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf);

        /**
         * 2. Set the jar storage location
         * 2. 设置jar存储位置
         */
        job.setJarByClass(WordcountDriver.class);

        /**
         * Set set Combiner Class
         *设置setCombinerClass
         */
        job.setCombinerClass(WordcountCombiner.class);

        /**
         * 3. Associate Map and Reduce classes
         * 3. 关联Map和Reduce类
         */
        job.setMapperClass(WordcountMapper.class);
        job.setReducerClass(WordcountReducer.class);

        /**
         * 4. Set the key and value types of the output data in the Mapper stage.
         * 4. 设置Mapper阶段输出数据的key与value类型
         */
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(IntWritable.class);

        /**
         * 5. Set the key and value types for the final data output
         * 5. 设置最终数据输出的key与value类型
         */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

//        job.setNumReduceTasks(2);

        /**
         * Set the Format mode to Combine Text Input Format
         * 设置Format模式为Combine Text Input Format
         * If you do not set the Input Format, it defaults to Text Input Format.class
         * 如果不设置InputFormat，它默认用的是TextInputFormat.class
         */
//        job.setInputFormatClass(CombineTextInputFormat.class);

        /**
         * Set the virtual storage slice maximum to 20M
         * 设置虚拟存储切片最大值为 20M
         */
//        CombineTextInputFormat.setMaxInputSplitSize(job, 20971520);

        /**
         * Set the virtual storage slice maximum to 4M
         * 设置虚拟存储切片最大值为 4M
         */
//         CombineTextInputFormat.setMaxInputSplitSize(job, 4194304);

        /**
         * Set the virtual storage slice minimum to 2M
         * 设置虚拟存储切片最小值为 2M
         */
//         CombineTextInputFormat.setMinInputSplitSize(job, 2097152);

        /**
         * 6. Set the input path and output path
         * 6. 设置输入路径和输出路径
         */
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         * Set reduce output compression on
         * 设置reduce端输出压缩开启
         */
        FileOutputFormat.setCompressOutput(job, true);

        /**
         * Set compression mode
         * 设置压缩方式
         */
        FileOutputFormat.setOutputCompressorClass(job, BZip2Codec.class);
//        FileOutputFormat.setOutputCompressorClass(job, GzipCodec.class);
//        FileOutputFormat.setOutputCompressorClass(job, DefaultCodec.class)

        /**
         * 7. Submit the Job
         * 7. 提交Job
         */
        boolean result = job.waitForCompletion(true);

        /**
         * 8. Log printing
         * 8. 日志打印
         */
        System.exit(result ? 0 : 1);
    }
}
```

### 7.7.5 Yarn资源调度器 (面试重点)
> Yarn是一个资源调度平台,负责为运算程序提供服务器运算资源,相当于一个分布式的操作系统平台,而Map Reduce等运算程序则相当于运行于操作系统之上的应用程序.
#### Yarn 基本架构
> YARN主要由ResourceManager、NodeManager、ApplicationMaster和Container等组件构成.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_037.jpg)

#### Yarn 工作机制
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hadoop/start_038.jpg)

## 🔒 尚未解锁 正在学习探索中... 尽情期待 Blog更新! 🔒

#### 作业提交全过程
#### 资源调度器

### 7.7.6 Hadoop 企业优化
#### MapReduce 运行缓慢的原因
#### MapReduce 优化方案
##### 数据输入
##### Map阶段
##### Reduce阶段
##### I/O传输
##### 数据倾斜问题
##### 常用调优参数

#### HDFS小文件优化方法
##### HDFS小文件弊端
##### HDFS小文件解决方案

### 7.7.7 MapReduce 扩展案例
#### 倒排索引案例(多job串联)
#### TopN案例
#### 找博客共同好友案例


### 8. HDFS HA高可用


## 9. 常见错误(各种坑)及解决方案


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