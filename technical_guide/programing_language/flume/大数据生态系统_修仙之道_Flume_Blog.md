# 大数据生态系统 修仙之道 Flume Blog

@(2019-03-25)[ Docs Language:简体中文 & English|Programing Language:Flume|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)|![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg) | ![GitHub repo size in bytes](https://img.shields.io/github/repo-size/geekparkhub/geekparkhub.github.io.svg) | GeekDeveloper:[JEEP-711](https://github.com/jeep711)|Github:[github.com/geekparkhub](https://github.com/geekparkhub)|Gitee:[gitee.com/geekparkhub](https://gitee.com/geekparkhub) ]

##  🐘 Flume Technology 修仙之道 炼神返虚 🐘

![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/fiume_cover.jpg)

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


## 1. Flume 概述
> Flume是Cloudera公司提供的一个`高可用`/`高可靠`/`分布式海量日志采集`/`聚合`/`传输`系统.
> 
> Flume作为Hadoop平台日志收集的核心组件,提供了强大可扩展性的设计架构和丰富的插件,能够将来自不同数据源的海量日志数据高效的收集/聚合/移动/存储到统一的数据存储系统中.
### 1.0 Flume 功能&特性
#### 1.0.1 Flume 功能
Flume功能强大,可以灵活调整架构/自定义插件/为开发者提供一下功能.
- 从固定目录下采集日志信息到目的地(HDFS/HBaes/Kafka).
- 实时采集日志信息到目的地(HDFS/HBaes/Kafka).
- 支持级联(多个Agent对接工作).
- 支持按照开发者定制实现数据采集,可以使用Flume来对接多种类型数据源,包括但不限于网络流量数据/社交媒体生成数据/电子邮件消息以及其他数据源.

#### 1.0.2 Flume 特性
- 压缩加密 : Flume级联节点之间的数据传输支持压缩和加密,提升数据传输效率和安全性.
- 复杂流 : Flume支持(fan-in)扇入流&(fan-out)扇出流,扇入流既Source可以接受多个输入,扇出流既Sink可以将Event分流输出到多个目标位置.
- 传输可靠性 : Flume在传输过程中,支持Channel缓存/数据发送/故障转移,保证传输过程中数据不会丢失,增强了数据传输的可靠性.
- 数据过滤 : Flume在传输数据过程中,可以对数据简单过滤/清洗,去除不关心的数据,如需对复杂数据过滤,需要开发者根据自身数据特殊性,开发过滤插件,Flume支持第三方过滤插件使用.

#### 1.0.3 Flume与其他日志收集系统 区别
> 目前常用的开源日志收集系统除了Flume之外还有Facebook的Scribe,Apache的Chukwa & Kafka(最早由Linkedin开发).
> 
> Scribe是Facebook开发的分布式日志收集系统,它为日志的"分布式收集和统一处理",提供了一个可扩展/高容错性方案.
> 
> Chukwa是用于监控大型分布式系统的开源数据收集系统,集成了Hadoop一些组件,将HDFS作为存储系统,使用MapReduce框架处理数据,并提供灵活且功能强大的工具包,用于显示/监控/分析结果.
> 
> Kafka是一个高吞吐量的分布式订阅消息系统,可用于分布式系统的日志收集,它最初是由LinkedIn公司开发,之后成为了Apache项目的一部分.
> 
> 对比体现表
| 日志收集产品 | Flume |   Scribe   |   Chukwa   |   Kafka   |
| :--------: | --------:| :------: |:------: |:------: |
| 开发语言    |   Java |  C/C++  |  Java  |  Scala  |
| 容错性    | Agent与存储之间有容错性机制,提供End-to-end/Store on failure/Best effort 三种级别可靠性保障. | Agent与存储之间有容错性机制,Agent与收集器之间的容错性需要开发者自行实现. |  Agent与存储之间有容错性机制.  |  Agent和收集器、存储之间都有容错性机制.  |
| 负载均衡   | Zookeeper |  不适用  |  不适用  | Zookeeper  |
| Agent    |   Flume提供丰富Agent,可直接使用,支持对Agent中的Source/Channel/Sink进行自定义开发. |  Scribe内部定义了ThriftAPI,开发者需要开发实现ThriftAgent.  |  提供一些自带Agent  |  开发者需根据Kafka提供的API自行开发实现Agent.  |
| 收集器(用于收集汇总数据)    |   不适用 |  使用ThriftServer  |  不适用  |  使用sendfile/zore-copy等技术提高收集效率.  |
| 存储    |   可使用HDFS |  可使用HDFS  |  可使用HDFS  |  可使用HDFS  |


### 1.1 Flume 定义
> Flume基于流式架构,灵活简单.
> 
> Flume支持从多种数据源收集数据,对数据进行处理后,将数据写入到数据接收方.
> 
> Flume提供从`本地文件`/`实时日志`/`REST消息`/`Thrift`/`Avro`/`Syslog`/`Kafka`等数据源收集数据的能力.
> 
> Flume具有可靠性机制和许多故障转移和恢复机制强大和容错能力,它使用一个简单可扩展数据模型,允许在线分析应用程序.
> 
> Flume用于实时收集服务器(Apache/Ngnix等)数据框架,Flume很多时候与Storm以及Spark Streaming等流式处理框架结合使用.

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/start_001.jpg)
> Flume主要作用是实时读取服务器本地磁盘数据,将数据写入到HDFS.

### 1.2 Flume 组成架构 ♨️

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/start_002.jpg)
> Flume 基础架构
> 
> Flume架构非常简单,只需要部署Agent代理一个角色,通过Agent获取外部日志数据再传输到目标存储HDFS中,上图中是使用单Agent架构直接采集数据集,主要用于采集集群内数据.

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/start_006.jpg)
> Flume 多Agent架构
> 
> Flume也支持多Agent架构,可以将多个Agent级联工作,Flume从最初的数据源收集数据,经过两个Agent传输,最终将数据存储到HDFS中,多Agent架构可以起到复制/分流等作用,主要用于将集群外数据导入到集群内.

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/start_005.jpg)
> Flume 组成架构详解


#### 1.2.1 Agent
> Agent主要由三大模块组成：`Source`/ `Channel` / `Sink`, 一个Agent内可以有多个Channel & Sink , Agent是一个JVM进程.
> 
> Agent具有字节有效载荷和可选的一组字符串属性的数据流的单元.
> 
> Flume代理(Agent)是一个(JVM)程,它承载事件从外部源传递到下一个目标(跳)组件,是Flume数据传输的基本单元,以事件的形式将数据从源头送至目的地.

#### 1.2.2 Source
> Source用于采集数据,Source是产生数据流的地方,同时Source会将产生的数据流传输到Channel,这有点类似于Java IO部分的Channel.
> 
> Source分为驱动型和轮询行,可以对接多种数据源.
> 
> 驱动型Source工作模式是数据源主动发送数据给Flume,驱动Flume接收数据,如Exec Source / Avro Source / Thrift Source / HTTP Source.
> 
> 轮询型Source工作模式是Flume周期性主动从数据源获取数据,如Syslog Source / Spooling Directory Source / Jms Source / Kafka Source.
> 
> 开发者可以对Source进行自定义开发.
> 
> Source 类型表
| Source类型 | 	 说明   |
| :--------: | :--------:|
| Exec Source    |   执行某个命令或脚本,并将其执行结果的输出作为数据源. |
| Avro Source    |   提供一个基于Avro协议的Server,将其绑定到某个端口上,等待Avro协议客户端发送数据. |
| Thrift Source    |   提供一个基于Thrift协议的Server,将其绑定到某个端口上,等待Thrift协议客户端发送数据. |
| HTTP Source    |   支持HTTP的post发送数据. |
| Syslog Source    |   采集系统Syslog日志. |
| Spooling Directory Source    |   采集本地静态文件. |
| Jms Source    |   从消息队列获取数据. |
| Kafka Source    |   从Kafka获取数据. |

#### 1.2.3 Channel
> Channel位于Source & Sink之间,Channel作用是类似于队列,用于临时缓存Agent中间的Event.
> 
> 开发者可以对Channel自定义开发,不同的Channel类型提供的数据持久化水平是不一样的,缓存位置也不同,Channel可以将Event存放到内存/文系统/数据库中.
> 
> Channel 类型表
| Channel类型  |     说明 |
| :--------: | :--------:|
| Memory Channel  |   Event存放在内存中,提供高吞吐,但不提供可靠性,可能丢失数据. |
| File Channel    |   Event存放在文件中,对数据进行持久化,但配置比较繁琐,需要配置数据目录和Checkpoint目录,不同的FileChannel需要配置一个Checkpoint目录. |
| JDBC Channel    |   Event存放在Flume内置的Derby数据库中,并对Event进行持久化,提供高可靠型. |


#### 1.2.4 Sink
> Sink负责将Event传输到下一个条跳或最终目的存储,Event写入成功后,会从Channel中被移除,Sink必须作用于一个确切的Channel.
> 
> 开发者可以使用不同类型的Sink将数据传输到不同目标储存(HDFS/HBase/Kafka/Sorr/本地文件系统),同样开发者也可以对Sink进行自定义开发.
> 
> Sink 类型表
| Sink类型   |     说明 |
| :--------:| :--------:|
| HDFS     |   将数据写入到HDFS |
| Avro Sink    |   使用Avro协议将数据发送给下一个跳的Flume. |
| Thrift Sink    |   使用Thrift协议将数据发送给另下一个跳的Flume. |
| File Rool Sink    |   将数据保存在本地文件系统中. |
| HBase Sink    |   将数据写入到HBase中. |
| Kafka Sink    |   将数据写入到Kafka中. |
| MorphlineSolr Sink    |   将数据写入到Solr中. |


#### 1.2.5 Event
> Event是Flume数据传输的基本单元,Event代表着一个数据流的最小完整单元,来自外部数据源,流向最终目的存储.
> 
> Event由`Header(报头)`&`Body(主体)`组成,Event以事件的形式将数据从源头送至目的地.

### 1.3 Flume 拓扑结构
#### 1.3.1 串行模式
![enter image description here](https://img2018.cnblogs.com/blog/395849/201901/395849-20190102181057205-502969424.png)
> 这种模式是将多个Flume给顺序连接起来了,从最初的Source开始到最终Sink传送到目的存储系统,此模式不建议桥接过多的Flume数量,Flume数量过多不仅会影响传输速率,而且一旦传输过程中某个节点Flume宕机,会影响整个传输系统.

#### 1.3.2 单Source多Channel,Sink模式 (复制模式)
![enter image description here](https://img2018.cnblogs.com/blog/395849/201901/395849-20190102181152096-873758554.png)
> Flume支持将事件流向一个或者多个目的地,这种模式将数据源复制到多个Channel中,每个Channel都有相同的数据,Sink可以选择传送的不同的目的地.

#### 1.3.3 单Source,Channel多Sink模式 (负载均衡)
![enter image description here](https://img2018.cnblogs.com/blog/395849/201901/395849-20190102181333336-493046725.png)
> Flume支持使用将多个sink逻辑上分到一个Sink组,Flume将数据发送到不同的Sink,主要解决负载均衡和故障转移问题.

#### 1.3.4 聚合模式
![enter image description here](https://img2018.cnblogs.com/blog/395849/201901/395849-20190102181409507-1332137680.png)
> 这种模式是最常见的,也非常实用,日常Web应用通常分布在上百个服务器,大者甚至上千上万个服务器产生的日志处理起来也非常麻烦.
> 
> 而这种Flume组合方式能很好的解决这一问题,每台服务器部署一个Flume采集日志,传送到一个集中收集日志的Flume,再由此Flume上传至HDFS/Hive/HBase/Jms等进行日志分析.

### 1.4 Flume Agent内部原理 🤔
![enter image description here](https://img2018.cnblogs.com/blog/395849/201901/395849-20190102181726224-1004855716.png)

## 2. 👨🏻‍💻 Flume Quick Start 👨🏻‍💻

### 2.1 Flume 安装地址
> Apache Flume官网 : [flume.apache.org](http://flume.apache.org/)
> 
> Apache Flume官方文档 : [flume.apache.org/FlumeUserGuide.html](http://flume.apache.org/FlumeUserGuide.html)
> 
> Apache Flume Download : [archive.apache.org/dist/flume](http://archive.apache.org/dist/flume/)

### 2.2 安装部署
> 1.将apache-flume-1.7.0-bin.tar.gz上传到linux /opt/software目录下.
``` powershell
[root@systemhub711 ~]# cd /opt/software/
[root@systemhub711 software]# ll
total 657128
-rw-r--r--. 1 root root  55711670 Apr  9 21:35 apache-flume-1.7.0-bin.tar.gz
-rw-r--r--. 1 root root  92834839 Mar 24 23:51 apache-hive-1.2.1-bin.tar.gz
-rwxrwxrwx. 1 root root   9621331 Jan 14 09:36 apache-tomcat-8.5.33.tar.gz
-rwxrwxrwx. 1 root root 212046774 Jan 24 20:37 hadoop-2.7.2.tar.gz
-rwxrwxrwx. 1 root root 189815615 Jan 14 10:22 jdk-8u162-linux-x64.tar.gz
-rwxrwxrwx. 1 root root  35042811 Jan 17 19:18 zookeeper-3.4.10.tar.gz
[root@systemhub711 software]# 
```
> 2.解压apache-flume-1.7.0-bin.tar.gz到/opt/module/目录下.
``` powershell
[root@systemhub711 software]# tar -zxvf apache-flume-1.7.0-bin.tar.gz -C /opt/module/
apache-flume-1.7.0-bin/lib/flume-ng-configuration-1.7.0.jar
apache-flume-1.7.0-bin/lib/slf4j-api-1.6.1.jar
apache-flume-1.7.0-bin/lib/slf4j-log4j12-1.6.1.jar
apache-flume-1.7.0-bin/lib/log4j-1.2.17.jar
apache-flume-1.7.0-bin/lib/guava-11.0.2.jar
apache-flume-1.7.0-bin/docs/searchindex.js
apache-flume-1.7.0-bin/docs/team-list.html
[root@systemhub711 software]# 
```
> 3.修改apache-flume-1.7.0-bin名称为flume
``` powershell
[root@systemhub711 software]# cd /opt/module/
[root@systemhub711 module]# mv apache-flume-1.7.0-bin flume
[root@systemhub711 module]# ll
total 28
drwxr-xr-x.  9 root root 4096 Feb 24 21:55 apache-tomcat
drwxr-xr-x.  6 root root 4096 Apr  3 22:36 datas
drwxr-xr-x.  7 root root 4096 Apr  9 21:37 flume
drwxr-xr-x. 12 root root 4096 Feb 27 14:24 hadoop
drwxr-xr-x. 10 root root 4096 Mar 25 23:32 hive
drwxr-xr-x.  8 uucp  143 4096 Dec 20  2017 jdk1.8.0_162
drwxr-xr-x. 10 1001 1001 4096 Mar 23  2017 zookeeper
[root@systemhub711 module]# 
```

> 4.将flume/conf下的flume-env.sh.template文件修改为flume-env.sh,并配置flume-env.sh脚本.
```
[root@systemhub711 module]# cd flume/conf/
[root@systemhub711 conf]# mv flume-env.sh.template flume-env.sh
[root@systemhub711 conf]# echo $JAVA_HOME
/opt/module/jdk1.8.0_162
[root@systemhub711 conf]# vim flume-env.sh
```
> 配置JAVA_HOME环境变量
```
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
# Enviroment variables can be set here.

export JAVA_HOME=/opt/module/jdk1.8.0_162
```


## 3. 🏢 企业开发案例 🏢
### 3.1 监控端口数据
> 首先Flume监控本机44444端口,然后通过telnet工具向systemhub711主机44444端口发送消息,最后Flume将监听数据实时在控制台显示.
#### 1.分析过程
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/start_007.jpg)

#### 2.实现步骤
##### 2.1 安装telnet工具
> 将rpm软件包拷贝(`xinetd-2.3.14-40.el6.x86_64.rpm` / `telnet-0.17-48.el6.x86_64.rpm` / `telnet-server-0.17-48.el6.x86_64.rpm`)到Linux系统,并执行RPM软件包安装命令.
> 
> 在software目录下创建flume_flow文件夹,并上传至此目录.
``` powershell
[root@systemhub711 conf]# cd /opt/software/
[root@systemhub711 software]# mkdir flume_flow
[root@systemhub711 software]# cd flume_flow/
[root@systemhub711 flume_flow]# ll
total 224
-rw-r--r--. 1 root root  59332 Apr  9 21:48 telnet-0.17-48.el6.x86_64.rpm
-rw-r--r--. 1 root root  37912 Apr  9 21:48 telnet-server-0.17-48.el6.x86_64.rpm
-rw-r--r--. 1 root root 124812 Apr  9 21:48 xinetd-2.3.14-40.el6.x86_64.rpm
[root@systemhub711 flume_flow]# 
```
> rpm -ivh指令安装
``` powershell
[root@systemhub711 flume_flow]# rpm -ivh xinetd-2.3.14-40.el6.x86_64.rpm
Preparing...                ########################################### [100%]
   1:xinetd                 ########################################### [100%]
[root@systemhub711 flume_flow]# rpm -ivh telnet-0.17-48.el6.x86_64.rpm
Preparing...                ########################################### [100%]
   1:telnet                 ########################################### [100%]
[root@systemhub711 flume_flow]# rpm -ivh telnet-server-0.17-48.el6.x86_64.rpm
Preparing...                ########################################### [100%]
   1:telnet-server          ########################################### [100%]
[root@systemhub711 flume_flow]# 
```
##### 2.2 判断44444端口是否被占用
> 功能描述 : `netstat`指令是一个监控TCP/IP网络非常有用的工具,它可以显示路由表,实际网络连接以及每一个网络接口设备状态信息.
> 
> 基本语法 : `netstat`[`选项`] / 选项参数 : 
> 
> `-t` 或 `--tcp` 表示显示TCP传输协议连接状况.
> `-u` 或 `--udp` 表示显示UDPP传输协议连接状况.
> `-n` 或 `--numeric` 表示直接使用IP地址,而不通过域名服务器.
> `-l` 或 `--listening` 表示显示监控中的服务器Socket.
> `-p` 或 `--programs` 表示正在使用Socket程序识别码和程序名称.
```
[root@systemhub711 flume_flow]# netstat -tunlp | grep 44444
[root@systemhub711 flume_flow]# 
```
##### 2.3 创建Flume Agent配置文件flume_telnet_logger.conf
> 在flume目录下创建job文件夹.
```
[root@systemhub711 flume_flow]# cd /opt/module/flume/
[root@systemhub711 flume]# mkdir job
[root@systemhub711 flume]# cd job/
[root@systemhub711 job]# 
```
> 在job文件夹下创建FlumeAgent配置文件`flume_telnet_logger.conf`
```
[root@systemhub711 job]# touch flume_telnet_logger.conf
[root@systemhub711 job]# ll
total 0
-rw-r--r--. 1 root root 0 Apr  9 22:31 flume_telnet_logger.conf
[root@systemhub711 job]# vim flume_telnet_logger.conf
```
> 配置`flume_telnet_logger.conf`文件.
> 
> ‼️ 注 ‼️ : 配置文件来源于官方文档 : [flume.apache.org/FlumeUserGuide.html](http://flume.apache.org/FlumeUserGuide.html)
> 
> 配置文件解析.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/start_008.jpg)
``` dsconfig
# example.conf: A single-node Flume configuration

# Name the components on this agent
a1.sources = r1
a1.sinks = k1
a1.channels = c1

# Describe/configure the source
a1.sources.r1.type = netcat
a1.sources.r1.bind = localhost
a1.sources.r1.port = 44444

# Describe the sink
a1.sinks.k1.type = logger

# Use a channel which buffers events in memory
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100

# Bind the source and sink to the channel
a1.sources.r1.channels = c1
a1.sinks.k1.channel = c1
```
> 添加内容如下.
``` dsconfig
# example.conf: A single-node Flume configuration

# Name the components on this agent
a1.sources = r1
a1.sinks = k1
a1.channels = c1

# Describe/configure the source
a1.sources.r1.type = netcat
a1.sources.r1.bind = systemhub711
a1.sources.r1.port = 44444

# Describe the sink
a1.sinks.k1.type = logger

# Use a channel which buffers events in memory
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100

# Bind the source and sink to the channel
a1.sources.r1.channels = c1
a1.sinks.k1.channel = c1
```

##### 2.4 开启Flume监听端口
> 参数说明 : 
> 
> `--conf conf/` 表示配置文件存储在conf/目录.
> 
> `--name a1` 表示为agent起别名为a1.
> 
> `--conf-file job/flume_telnet_logger.conf`  表示flume本次启动读取配置文件是在job目录下的flume_telnet_logger.conf文件.
> 
> `-Dflume.root.logger==INFO,console` 表示flume运行时动态修改flume.root.logger参数属性值,并将控制台日志打印级别设置为INFO级别.
> 
> 日志级别包括 : `log` / `info` / `warn` / `error`

``` powershell
[root@systemhub711 flume]# bin/flume-ng agent --conf conf/ --name a1 --conf-file job/flume_telnet_logger.conf -Dflume.root.logger==INFO,console
Info: Sourcing environment configuration script /opt/module/flume/conf/flume-env.sh
Info: Including Hadoop libraries found via (/opt/module/hadoop/bin/hadoop) for HDFS access
Info: Including Hive libraries found via (/opt/module/hive) for Hive access
+ exec /opt/module/jdk1.8.0_162/bin/java -Xmx20m -Dflume.root.logger==INFO,console -cp '/opt/module/flume/conf:/opt/module/flume/lib/*:/opt/module/hadoop/etc/hadoop:/opt/module/hadoop/share/hadoop/common/lib/*:/opt/module/hadoop/share/hadoop/common/*:/opt/module/hadoop/share/hadoop/hdfs:/opt/module/hadoop/share/hadoop/hdfs/lib/*:/opt/module/hadoop/share/hadoop/hdfs/*:/opt/module/hadoop/share/hadoop/yarn/lib/*:/opt/module/hadoop/share/hadoop/yarn/*:/opt/module/hadoop/share/hadoop/mapreduce/lib/*:/opt/module/hadoop/share/hadoop/mapreduce/*:/contrib/capacity-scheduler/*.jar:/opt/module/hive/lib/*' -Djava.library.path=:/opt/module/hadoop/lib/native org.apache.flume.node.Application --name a1 --conf-file job/flume_telnet_logger.conf
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/opt/module/flume/lib/slf4j-log4j12-1.6.1.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/opt/module/hadoop/share/hadoop/common/lib/slf4j-log4j12-1.7.10.jar!/org/slf4j/impl/StaticLoggerBinder.class]
```

##### 2.5 使用telnet工具向systemhub711主机44444端口发送消息
``` powershell
[root@systemhub711 ~]# telnet systemhub711 44444
Trying ...
Connected to systemhub711.
Escape character is '^]'.
hello_world
OK
are you ready?
OK
```
##### 2.6 查看Flume监听窗口接收数据情况
``` dsconfig
(SinkRunner-PollingRunner-DefaultSinkProcessor) [INFO - org.apache.flume.sink.LoggerSink.process(LoggerSink.java:95)] Event: { headers:{} body: 68 65 6C 6C 6F 5F 77 6F 72 6C 64 0D             hello_world. }

(SinkRunner-PollingRunner-DefaultSinkProcessor) [INFO - org.apache.flume.sink.LoggerSink.process(LoggerSink.java:95)] Event: { headers:{} body: 61 72 65 20 79 6F 75 20 72 65 61 64 79 3F 0D    are you ready?. }
```


### 3.2 实时读取本地文件到HDFS
> 实时监控hive日志并上传到HDFS.
> 
#### 1.步骤分析.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/start_009.jpg)
#### 2.实现步骤.
##### 1.拷贝Hadoop相关jar包到/flume/lib/指定目录下.
> `commons-configuration-1.6.jar` / `commons-io-2.4.jar`
> `hadoop-auth-2.7.2.jar` / `hadoop-common-2.7.2.jar`
> `hadoop-hdfs-2.7.2.jar` / `htrace-core-3.1.0-incubating.jar`
> 注意 : 根据自身版本查找jar包
``` powershell
[root@systemhub711 ~]# cd /opt/module/flume/lib/
[root@systemhub711 lib]# ll
total 64452
-rw-r--r--. 1 root root  298829 Apr 10 10:10 commons-configuration-1.6.jar
-rw-r--r--. 1 root root  185140 Apr 10 10:10 commons-io-2.4.jar
-rw-r--r--. 1 root root   70571 Apr 10 10:10 hadoop-auth-2.7.2.jar
-rw-r--r--. 1 root root 3440968 Apr 10 10:10 hadoop-common-2.7.2.jar
-rw-r--r--. 1 root root 8248640 Apr 10 10:10 hadoop-hdfs-2.7.2.jar
-rw-r--r--. 1 root root 1475955 Apr 10 10:10 htrace-core-3.1.0-incubating.jar
[root@systemhub711 lib]# 
```
##### 2.创建`flume_file_hdfs.conf`配置文件.
``` powershell
[root@systemhub711 lib]# cd ..
[root@systemhub711 flume]# cd job/
[root@systemhub711 job]# touch flume_file_hdfs.conf
[root@systemhub711 job]# vim flume_file_hdfs.conf
```
> 配置信息详情.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/start_010.jpg)
> 配置信息.
``` dsconfig
    #Name the components on this agent
    a2.sources = r2
    a2.sinks = k2
    a2.channels = c2
    
    #Describe/configure the source
    a2.sources.r2.type = exec
    a2.sources.r2.command = tail -f /opt/module/hive/logs/hive.log
    a2.sources.r2.shell = /bin/bash -c
    
    #Describe the sink
    a2.sinks.k2.type = hdfs
    a2.sinks.k2.hdfs.path = hdfs://systemhub511:9000/flume/%Y%m%d/%H
    
    #上传文件前缀
    a2.sinks.k2.hdfs.filePrefix = hive_logs
    #是否按照时间滚动文件夹
    a2.sinks.k2.hdfs.round = true
    #多少时间单位创建一个新的文件夹
    a2.sinks.k2.hdfs.roundValue = 1
    #重新定义时间单位
    a2.sinks.k2.hdfs.roundUnit = hour
    #是否使用本地时间戳
    a2.sinks.k2.hdfs.useLocalTimeStamp = true
    #积攒多少个Event才flush到HDFS一次
    a2.sinks.k2.hdfs.batchSize = 1000
    #设置文件类型,可支持压缩
    a2.sinks.k2.hdfs.fileType = DataStream
    #多久生成一个新文件
    a2.sinks.k2.hdfs.rollInterval = 600
    #设置每个文件滚动大小
    a2.sinks.k2.hdfs.rollSize = 134217700
    #文件的滚动与Event数量无关
    a2.sinks.k2.hdfs.rollCount = 0
    #最小冗余数
    a2.sinks.k2.hdfs.minBlockReplicas = 1

    #Use a channel which buffers events in memory
    a2.channels.c2.type = memory
    a2.channels.c2.capacity = 1000
    a2.channels.c2.transactionCapacity = 100

    #Bind the source and sink to the channel
    a2.sources.r2.channels = c2
    a2.sinks.k2.channel = c2
```
##### 3.执行监控配置
> 分别启动hadoop/flume/hive服务.
> 
> 启动Flume监控.
```
[root@systemhub711 flume]# bin/flume-ng agent --conf conf/ --name a2 --conf-file job/flume_file_hdfs.conf
Info: Sourcing environment configuration script /opt/module/flume/conf/flume-env.sh
Info: Including Hadoop libraries found via (/opt/module/hadoop/bin/hadoop) for HDFS access
Info: Including Hive libraries found via (/opt/module/hive) for Hive access
```
> 启动Hive
```
[root@systemhub711 module]# cd hive/
[root@systemhub711 hive]# bin/hive
Logging initialized using configuration in file:/opt/module/hive/conf/hive-log4j.properties
hive (default)> 
```
##### 4.查看Flume监听窗口数据
```
[root@systemhub511 hadoop]# hadoop fs -ls /flume/*
Found 1 items
drwxr-xr-x   - root supergroup 0 /flume/20500610/10
[root@systemhub511 hadoop]# hadoop fs -cat /flume/20500610/10/hive_logs.1554864629108.tmp
INFO  [main]: metastore.HiveMetaStore (HiveMetaStore.java:logInfo(746)) - 0: get_functions: db=default pat=*
INFO  [main]: HiveMetaStore.audit (HiveMetaStore.java:logAuditEvent(371)) - ugi=root    ip=unknown-ip-addr      cmd=get_functions: db=default pat=*       
INFO  [main]: metastore.HiveMetaStore (HiveMetaStore.java:logInfo(746)) - 0: get_functions: db=hive_db pat=*
INFO  [main]: HiveMetaStore.audit (HiveMetaStore.java:logAuditEvent(371)) - ugi=root    ip=unknown-ip-addr      cmd=get_functions: db=hive_db pat=*       
```


### 3.3 实时读取目录文件到HDFS
> 使用flume监听整个目录的文件.
> 
#### 1.步骤分析.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/start_011.jpg)
#### 2.实现步骤.
> 创建`flume_dir_hdfs.conf`配置文件.
```
[root@systemhub711 flume]# cd job/
[root@systemhub711 job]# touch flume_dir_hdfs.conf
[root@systemhub711 job]# vim flume_dir_hdfs.conf
```
> 配置信息详情.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/start_012.jpg)
> 配置信息.
```
    a3.sources = r3
    a3.sinks = k3
    a3.channels = c3

    #Describe/configure the source
    a3.sources.r3.type = spooldir
    a3.sources.r3.spoolDir = /opt/module/flume/upload
    a3.sources.r3.fileSuffix = .COMPLETED
    a3.sources.r3.fileHeader = true
    #忽略所有以.tmp结尾的文件,不上传
    a3.sources.r3.ignorePattern = ([^]*\.tmp)

    #Describe the sink
    a3.sinks.k3.type = hdfs
    a3.sinks.k3.hdfs.path = hdfs://systemhub511:8020/flume/upload/%Y%m%d/%H
    #上传文件前缀
    a3.sinks.k3.hdfs.filePrefix = upload-
    #是否按照时间滚动文件夹
    a3.sinks.k3.hdfs.round = true
    #多少时间单位创建一个新文件夹
    a3.sinks.k3.hdfs.roundValue = 1
    #重新定义时间单位
    a3.sinks.k3.hdfs.roundUnit = hour
    #是否使用本地时间戳
    a3.sinks.k3.hdfs.useLocalTimeStamp = true
    #积攒多少个Event才flush到HDFS一次
    a3.sinks.k3.hdfs.batchSize = 1000
    #设置文件类型,可支持压缩
    a3.sinks.k3.hdfs.fileType = DataStream
    #多久生成一个新文件
    a3.sinks.k3.hdfs.rollInterval = 600
    #设置每个文件的滚动大小
    a3.sinks.k3.hdfs.rollSize = 134217700
    #文件滚动与Event数量无关
    a3.sinks.k3.hdfs.rollCount = 0
    #最小冗余数
    a3.sinks.k3.hdfs.minBlockReplicas = 1

    #Use a channel which buffers events in memory
    a3.channels.c3.type = memory
    a3.channels.c3.capacity = 1000
    a3.channels.c3.transactionCapacity = 100
    
    #Bind the source and sink to the channel
    a3.sources.r3.channels = c3
    a3.sinks.k3.channel = c3
```
> 在Flume集群中创建upload目录.
```
[root@systemhub711 flume]# mkdir upload
[root@systemhub711 flume]# cd upload/
[root@systemhub711 upload]# 
```
> 创建log文件
```
[root@systemhub711 module]# cd flume/upload/
[root@systemhub711 upload]# touch test.log
[root@systemhub711 upload]# ll
total 0
-rw-r--r--. 1 root root 0 Apr 10 13:41 test.log
[root@systemhub711 upload]#
```
> 开启监听服务
```
[root@systemhub711 flume]# bin/flume-ng agent --conf conf/ --name a3 --conf-file job/flume_dir_hdfs.conf
Info: Sourcing environment configuration script /opt/module/flume/conf/flume-env.sh
Info: Including Hadoop libraries found via (/opt/module/hadoop/bin/hadoop) for HDFS access
```
> 查看log文件
> 上传完成的文件会以.COMPLETED结尾
```
[root@systemhub711 upload]# ll
total 0
-rw-r--r--. 1 root root 0 Apr 10 13:41 test.log.COMPLETED
[root@systemhub711 upload]#
```


### 3.4 单Flume多Channel/Sink
> 使用flume-1监控文件变动,flume-1将变动内容传递给flume-2,flume-2负责存储到HDFS,同时flume-1将变动内容传递给flume-3,flume-3负责输出到LocalFileSystem.
#### 1.步骤分析.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/start_013.jpg)

#### 2.实现步骤.
> 准备工作
> 1.在/opt/module/flume/job目录下创建group_001文件夹.
``` powershell
[root@systemhub711 flume]# cd job/
[root@systemhub711 job]# mkdir group_001
[root@systemhub711 job]# ll
total 16
-rw-r--r--. 1 root root 1582 Apr 10 16:28 flume_dir_hdfs.conf
-rw-r--r--. 1 root root 1519 Apr 10 10:49 flume_file_hdfs.conf
-rw-r--r--. 1 root root  548 Apr  9 22:46 flume_telnet_logger.conf
drwxr-xr-x. 2 root root 4096 Apr 10 17:24 group_001
[root@systemhub711 job]# 
```
> 2.在/opt/module/datas/core_flow/develop/project目录下创建flume3文件夹.
``` powershell
[root@systemhub711 project]# pwd
/opt/module/datas/core_flow/develop/project
[root@systemhub711 project]# mkdir flume3
[root@systemhub711 project]# ll
total 8
drwxr-xr-x. 3 root root 4096 Apr  3 22:36 analysis
drwxr-xr-x. 2 root root 4096 Apr 10 17:24 flume3
[root@systemhub711 project]# 
```
> 3.在group_001目录下创建`flume_file_flume.conf`配置文件.
> 用于监控hive.log文件的变动,同时产生两个channel和两个sink分别输送给flume-2和flume3
```
[root@systemhub711 job]# cd group_001/
[root@systemhub711 group_001]# touch flume_file_flume.conf
[root@systemhub711 group_001]# vim flume_file_flume.conf
```
> 添加配置信息
```
# Name the components on this agen
a1.sources = r1
a1.sinks = k1 k2
a1.channels = c1 c2
# 将数据流复制给多个channel
a1.sources.r1.selector.type = replicating

# Describe/configure the source
a1.sources.r1.type = exec
a1.sources.r1.command = tail -F /opt/module/hive/logs/hive.log
a1.sources.r1.shell = /bin/bash -c

# Describe the sink
a1.sinks.k1.type = avro
a1.sinks.k1.hostname = systemhub511
a1.sinks.k1.port = 5151

a1.sinks.k2.type = avro
a1.sinks.k2.hostname = systemhub511
a1.sinks.k2.port = 5152

# Describe the channel
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100

a1.channels.c2.type = memory
a1.channels.c2.capacity = 1000
a1.channels.c2.transactionCapacity = 100

# Bind the source andsink to the channe
a1.sources.r1.channels = c1 c2
a1.sinks.k1.channel = c1
a1.sinks.k2.channel = c2
```

> 4.在group_001目录下创建`flume_flume_hdfs.conf`配置文件.
> 用于接收flume-1的event,同时产生1个channel和1个sink,将数据输送给hdfs
```
[root@systemhub711 group_001]# touch flume_flume_hdfs.conf
[root@systemhub711 group_001]# vim flume_flume_hdfs.conf
```
> 添加配置信息.
```
# Name the components on this agent
a2.sources = r1
a2.sinks = k1
a2.channels = c1

# Describe/configure the source
a2.sources.r1.type = avro
a2.sources.r1.bind = systemhub511
a2.sources.r1.port = 5151

# Describe the sink
a2.sinks.k1.type = hdfs
a2.sinks.k1.hdfs.path = hdfs://systemhub511:9000/flume2/%Y%m%d/%H
#上传文件前缀
a2.sinks.k1.hdfs.filePrefix = flume2-
#是否按照时间滚动文件夹
a2.sinks.k1.hdfs.round = true
#多少时间单位创建一个新文件夹
a2.sinks.k1.hdfs.roundValue = 1
#重新定义时间单位
a2.sinks.k1.hdfs.roundUnit = hour
#是否使用本地时间戳
a2.sinks.k1.hdfs.useLocalTimeStamp = true
#积攒多少个Event才flush到HDFS一次
a2.sinks.k1.hdfs.batchSize =100
#设置文件类型,可支持压缩
a2.sinks.k1.hdfs.fileType = DataStream
#多久生成一个新文件
a2.sinks.k1.hdfs.rollInterval = 600
#设置每个文件的滚动大小大概是128M
a2.sinks.k1.hdfs.rollSize = 134217700
#文件的滚动与Event数量无关
a2.sinks.k1.hdfs.rollCount = 0
#最小冗余数
a2.sinks.k1.hdfs.minBlockReplicas = 1

# Describe the channel
a2.channels.c1.type = memory
a2.channels.c1.capacity = 1000
a2.channels.c1.transactionCapacity = 100

# Bind the source and sink to the channel
a2.sources.r1.channels = c1
a2.sinks.k1.channel = c1
```
> 5.在group_001目录下创建`flume_flume_dir.conf`配置文件.
> 用于接收flume-1的event,同时产生1个channel和1个sink,将数据传输到指定目录
```
[root@systemhub711 group_001]# touch flume_flume_dir.conf
[root@systemhub711 group_001]# vim flume_flume_dir.conf
```
> 添加配置信息.
```
# Name the components on this agent
a3.sources = r1
a3.sinks = k1
a3.channels = c1

# Describe/configure the source
a3.sources.r1.type = avro
a3.sources.r1.bind = systemhub511
a3.sources.r1.port = 5152

# Describe the sink
a3.sinks.k1.type = file_roll
a3.sinks.k1.sink.directory = /opt/module/datas/core_flow/develop/project/flume3

# Describe the channel
a3.channels.c1.type = memory
a3.channels.c1.capacity = 1000
a3.channels.c1.transactionCapacity = 100

# Bind the source and sink to the channel
a3.sources.r1.channels = c1
a3.sinks.k1.channel = c1
```
> 6.执行配置文件
> 
> `执行flume_flume_dir.conf`
```
[root@systemhub711 flume]# bin/flume-ng agent --conf conf/ --name a3 --conf-file job/group_001/flume_flume_dir.conf
Info: Sourcing environment configuration script /opt/module/flume/conf/flume-env.sh
Info: Including Hadoop libraries found via (/opt/module/hadoop/bin/hadoop) for HDFS access
Info: Including Hive libraries found via (/opt/module/hive) for Hive access
```
> `执行flume_flume_hdfs.conf`
```
[root@systemhub711 flume]# bin/flume-ng agent --conf conf/ --name a2 --conf-file job/group_001/flume_flume_hdfs.conf
Info: Sourcing environment configuration script /opt/module/flume/conf/flume-env.sh
Info: Including Hadoop libraries found via (/opt/module/hadoop/bin/hadoop) for HDFS access
Info: Including Hive libraries found via (/opt/module/hive) for Hive access
```
> `执行flume_file_flume.conf`
```
[root@systemhub711 flume]#  bin/flume-ng agent --conf conf/ --name a1 --conf-file job/group_001/flume_file_flume.conf
Info: Sourcing environment configuration script /opt/module/flume/conf/flume-env.sh
Info: Including Hadoop libraries found via (/opt/module/hadoop/bin/hadoop) for HDFS access
Info: Including Hive libraries found via (/opt/module/hive) for Hive access
```
> `执行hive`
```
[root@systemhub711 hive]# bin/hive
Logging initialized using configuration in file:/opt/module/hive/conf/hive-log4j.properties
hive (default)> 
```
> 7.查看Flume监听窗口数据
```
[root@systemhub711 flume3]# ll
total 0
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-1
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-10
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-11
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-12
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-13
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-14
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-15
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-16
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-17
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-18
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-19
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-2
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-20
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-21
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-22
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-23
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-3
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-4
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-5
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-6
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-7
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-8
-rw-r--r--. 1 root root 0 Apr 10 1554891473772-9
```

### 3.5 单Source,Channel多Sink
> 使用Flume1监控文件变动,Flume1将变动内容传输给Flume2,Flume2负责将信息传输到控制台,同时Flume1将变动内容传输给Flume3,Flume3负责存储到HDFS.

#### 1.步骤分析.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/start_014.jpg)

#### 2.实现步骤.
> 准备工作
> 1.在/opt/module/flume/job目录下创建group_002文件夹.
```
[root@systemhub711 project]# cd /opt/module/flume/job/
[root@systemhub711 job]# mkdir group_002
[root@systemhub711 job]# ll
total 20
-rw-r--r--. 1 root root 1582 Apr 10 16:28 flume_dir_hdfs.conf
-rw-r--r--. 1 root root 1519 Apr 10 10:49 flume_file_hdfs.conf
-rw-r--r--. 1 root root  548 Apr  9 22:46 flume_telnet_logger.conf
drwxr-xr-x. 2 root root 4096 Apr 10 21:30 group_001
drwxr-xr-x. 2 root root 4096 Apr 10 21:33 group_002
[root@systemhub711 job]# 
```
> 3.在group_002目录下创建`flume_telnet_flume.conf`配置文件.
```
[root@systemhub711 job]# cd group_002
[root@systemhub711 group_002]# touch flume_telnet_flume.conf
[root@systemhub711 group_002]# vim flume_telnet_flume.conf
```

> 添加配置信息.
```
# Name the components on this agent
a1.sources = r1
a1.channels = c1
a.sinkgroups = g1
a1.sinks = k1 k2

# Describe/configure the source
a1.sources.r1.type = netcat
a1.sources.r1.bind = systemhub711
a1.sources.r1.port = 44444
a1.sinkgroups.g1.processor.type = load balance
a1.sinkgroups.g1.processor.backoff = true
a1.sinkgroups.g1.processor.selector = round robin
a1.sinkgroups.g1.processor.selector.maxTimeOut = 10000

# Describe the sink
a1.sinks.k1.type = avro
a1.sinks.k1.hostname = systemhub711
a1.sinks.k1.port = 4141

a1.sinks.k2.type = avro
a1.sinks.k2.hostname = systemhub711
a1.sinks.k2.port = 4142

# Describe the channel
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100

# Bind the source and sink to the channel
a1.sources.r1.channels = c1
a1.sinkgroups.g1.sinks = k1 k2
a1.sinks.k1.channel = c1
a1.sinks.k2.channel = c1
```

> 在group_002目录下创建`flume_flume_console1.conf`配置文件.
> 配置上级Flume输出源,输出位置到本地控制台.
```
[root@systemhub711 group_002]# touch flume_flume_console1.conf
[root@systemhub711 group_002]# vim flume_flume_console1.conf
```
> 添加配置信息.
```
# Name the components on this agent
a2.sources = r1
a2.sinks = k1
a2.channels = c1

# Describe/configure the source
a2.sources.r1.type = avro
a2.sources.r1.bind = systemhub711
a2.sources.r1.port = 4141

# Describe the sink
a2.sinks = k1.type = logger

# Describe/configure the source
a2.channels.c1.type = memory
a2.channels.c1.capacity = 1000
a2.channels.c1.transactionCapacity = 100

# Bind the source and sink to the channel
a2.sources.r1.channels = c1
a2.sinks.k1.channel = c1
```
> 在group_002目录下创建`flume_flume_console2.conf`配置文件.
```
[root@systemhub711 group_002]# touch flume_flume_console2.conf
[root@systemhub711 group_002]# vim flume_flume_console2.conf
```
> 添加配置信息.
```
# Name the components on this agent
a3.sources = r1
a3.sinks = k1
a3.channels = c2

# Describe/configure the source
a3.sources.r1.type = avro
a3.sources.r1.bind = systemhub711
a3.sources.r1.port = 4142

# Describe the sink
a3.sinks = k1.type= logger

# Describe/configure the source
a3.channels.c2.type = memory
a3.channels.c2.capacity = 1000
a3.channels.c2.transactionCapacity = 100

# Bind the source and sink to the channel
a3.sources.r1.channels = c2
a3.sinks.k1.channel = c2
```

> 6.执行配置文件
> 
> 启动`flume_flume_console2.conf`
```
[root@systemhub711 flume]# bin/flume-ng agent --conf conf/ --name a3 --conf-file job/group_002/flume_flume_console2.conf -Dflume.root.logger==INFO,console
Info: Sourcing environment configuration script /opt/module/flume/conf/flume-env.sh
```
> 启动`flume_flume_console1.conf`
```
[root@systemhub711 flume]# bin/flume-ng agent --conf conf/ --name a2 --conf-file job/group_002/flume_flume_console1.conf -Dflume.root.logger==INFO,console
Info: Sourcing environment configuration script /opt/module/flume/conf/flume-env.sh
```
> 启动`flume_telnet_flume.conf`
```
[root@systemhub711 flume]# bin/flume-ng agent --conf conf/ --name a1 --conf-file job/group_002/flume_telnet_flume.conf
Info: Sourcing environment configuration script /opt/module/flume/conf/flume-env.sh

```

> 启动telnet工具向systemhub711主机44444端口发送消息
```
[root@systemhub711 flume]# telnet systemhub711 44444
Trying ...
Connected to systemhub711.
Escape character is '^]'.
hey.
OK
```

> 7.查看Flume监听窗口数据
```
(SinkRunner-PollingRunner-DefaultSinkProcessor) [INFO - org.apache.flume.sink.LoggerSink.process(LoggerSink.java:95)] Event: { headers:{} body: 68 65 6C 6C 6F 5F 77 6F 72 6C 64 0D    hey. }
```

### 3.6 多数据源汇总
> 服务器1上的Flume1监控文件/opt/module/group.log.
> 服务器2上的Flume2监控某个端口的数据流.
> 服务器1与服务器2将数据发送给服务器3上的Flume3,Flume3将最终数据打印到控制台.

#### 1.步骤分析.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/start_015.jpg)

#### 2.实现步骤.
> 准备工作
> 
> 1.在/opt/module/flume/job目录下创建group_003文件夹.
```
[root@systemhub711 job]# mkdir group_003
[root@systemhub711 job]# ll
total 24
-rw-r--r--. 1 root root 1582 Apr 10 16:28 flume_dir_hdfs.conf
-rw-r--r--. 1 root root 1519 Apr 10 10:49 flume_file_hdfs.conf
-rw-r--r--. 1 root root  548 Apr  9 22:46 flume_telnet_logger.conf
drwxr-xr-x. 2 root root 4096 Apr 10 21:30 group_001
drwxr-xr-x. 2 root root 4096 Apr 11 01:33 group_002
drwxr-xr-x. 2 root root 4096 Apr 11 16:53 group_003
```
> 2.分发Flume.
> 
> 向systemhub611服务器分发Flume.
```
[root@systemhub711 module]# rsync -rvl flume/ root@systemhub611:/opt/module/flume/
```
> 向systemhub511服务器分发Flume.
```
[root@systemhub711 module]# rsync -rvl flume/ root@systemhub511:/opt/module/flume/
```
> 3.分发完成,查看结果.
```
[root@systemhub511 module]# ll
total 20
drwxr-xr-x.  9 root  root  4096 Feb 24 21:55 apache-tomcat
drwxr-xr-x. 10 root  root  4096 Apr 11 17:02 flume
drwxr-xr-x. 12 10011 10011 4096 Mar  3 00:42 hadoop
drwxr-xr-x.  8 uucp    143 4096 Dec 20  2017 jdk1.8.0_162
drwxr-xr-x. 10  1001  1001 4096 Mar 23  2017 zookeeper
[root@systemhub511 module]#
```
```
[root@systemhub611 module]# ll
total 32
drwxr-xr-x.  9 root   root 4096 Feb 24 21:55 apache-tomcat
drwxr-xr-x. 10 root   root 4096 Apr 11 17:01 flume
drwxr-xr-x. 12 root   root 4096 Feb 27 14:24 hadoop
drwxr-xr-x.  8 uucp    143 4096 Dec 20  2017 jdk1.8.0_162
drwxr-xr-x.  6 root   root 4096 Apr  1 14:50 maven
drwxr-xr-x. 10 109965 5000 4096 Apr  1 18:15 protobuf
drwxr-xr-x.  6  60692 5000 4096 Apr  1 16:45 snappy
drwxr-xr-x. 10   1001 1001 4096 Mar 23  2017 zookeeper
[root@systemhub611 module]#
```
> 4.在systemhub711服务器上创建并配置`flume1_logger_flume.conf`配置文件.
> 配置Source用于监控hive.log文件,配置Sink输出数据到下一级Flume.
```
[root@systemhub711 //]# cd /opt/module/flume/
[root@systemhub711 flume]# cd job/group_003
[root@systemhub711 group_003]# touch flume1_logger_flume.conf
[root@systemhub711 group_003]# vim flume1_logger_flume.conf
```
> 添加配置信息.
```
# Name the components on this agent
a1.sources = r1
a1.sinks = k1
a1.channels = c1

# Describe/configure the source
a1.sources.r1.type = exec
a1.sources.r1.command = tail -F /opt/module/hive/logs/hive.log
a1.sources.r1.shell = /bin/bash -c

# Describe the sink
a1.sinks.k1.type = avro
a1.sinks.k1.hostname = systemhub511
a1.sinks.k1.port = 4141

# Describe the channel
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100

# Bind the source and sink to the channel
a1.sources.r1.channels = c1
a1.sinks.k1.channel = c1
```
> 5.在systemhub611服务器上创建并配置`flume2_netcat_flume.conf`配置文件.
> 配置Source监控端口44444数据流,配置Sink数据到下一级Flume.
```
[root@systemhub611 module]# cd flume/job/group_003
[root@systemhub611 group_003]# touch flume2_netcat_flume.conf
[root@systemhub611 group_003]# vim flume2_netcat_flume.conf
```
> 添加配置信息.
```
# Name the components on this agent
a2.sources = r1
a2.sinks = k1
a2.channels = c1

# Describe/configure the source
a2.sources.r1.type = netcat
a2.sources.r1.bind = systemhub611
a2.sources.r1.port = 44444

# Describe the sin
a2.sinks.k1.type = avro
a2.sinks.k1.hostname = systemhub511
a2.sinks.k1.port = 4141

# Use a channel which buffers events in memory
a2.channels.c1.type = memory
a2.channels.c1.capacity = 1000
a2.channels.c1.transactionCapacity = 100

# Bind the source and sink to the channel
a2.sources.r1.channels = c1
a2.sinks.k1.channel = c1
```

> 6.在systemhub511服务器上创建并配置`flume3_flume_logger.conf`配置文件.
> 配置Source用于接收Flume1与Flume1发送的数据,最终合并到Sink到控制台.
```
[root@systemhub511 opt]# cd module/flume/job/group_003
[root@systemhub511 group_003]# touch flume3_flume_logger.conf
[root@systemhub511 group_003]# vim flume3_flume_logger.conf
```
> 添加配置信息.
```
# Name the components on this agent
a3.sources = r1
a3.sinks = k1
a3.channels = c1

# Describe/configure the source
a3.sources.r1.type = avro
a3.sources.r1.bind = systemhub511
a3.sources.r1.port = 4141
a3.sinks = k1.type= logger

# Describe the channel
a3.channels.c1.type = memory
a3.channels.c1.capacity = 1000
a3.channels.c1.transactionCapacity = 100

# Bind the source and sink to the channel
a3.sources.r1.channels = c1
a3.sinks.k1.channel = c1
```
> 6.执行配置文件
> 启动systemhub511服务
```
[root@systemhub511 flume]# bin/flume-ng agent --conf conf/ --name a3 --conf-file job/group_003/flume3_flume_logger.conf -Dflume.root.logger==INFO,console
Info: Sourcing environment configuration script //opt/module/flume/conf/flume-env.sh
```
> 启动systemhub611服务
```
[root@systemhub611 flume]# bin/flume-ng agent --conf conf/ --name a2 --conf-file job/group_003/flume2_netcat_flume.conf
Info: Sourcing environment configuration script /opt/module/flume/conf/flume-env.sh
```
> 启动systemhub711服务
```
[root@systemhub711 flume]# bin/flume-ng agent --conf conf/ --name a1 --conf-file job/group_003/flume1_logger_flume.conf
Info: Sourcing environment configuration script /opt/module/flume/conf/flume-env.sh
```
> 7.启动telnet工具向systemhub611主机44444端口发送消息
```
[root@systemhub611 ~]# telnet systemhub611 44444
Trying ...
Connected to systemhub611.
Escape character is '^]'.
het^Hy.
OK
```
> 8.在systemhub511服务器查看Flume监听窗口数据
```
(SinkRunner-PollingRunner-DefaultSinkProcessor) [INFO - org.apache.flume.sink.LoggerSink.process(LoggerSink.java:95)] Event: { headers:{} body: 68 65 6C 6C 6F 5F 77 6F 72 6C 64 0D    het^Hy }
```



## 4. Flume监控Ganglia
### 4.1 Ganglia的安装与部署
#### 4.1.1 安装httpd服务与php
> install httpd php
```
[root@systemhub711 flume]# yum -y install httpd php
Loaded plugins: fastestmirror, refresh-packagekit, security
Determining fastest mirrors
 * base: mirrors.neusoft.edu.cn
 * extras: mirrors.huaweicloud.com
 * updates: mirrors.huaweicloud.com
 Installed:
  php.x86_64 0:5.3.3-49.el6
Dependency Installed:
  php-cli.x86_64 0:5.3.3-49.el6
  php-common.x86_64 0:5.3.3-49.el6
  httpd.x86_64 0:2.2.15-69.el6.centos
Dependency Updated:
  httpd-tools.x86_64 0:2.2.15-69.el6.centos                    
Complete!
```
#### 4.1.2 安装其他依赖
> install rrdtool perl-rrdtool rrdtool-devel
```
[root@systemhub711 flume]# yum -y install rrdtool perl-rrdtool rrdtool-devel
Loaded plugins: fastestmirror, refresh-packagekit, security
Loading mirror speeds from cached hostfile
 * base: mirrors.neusoft.edu.cn
 * extras: mirrors.huaweicloud.com
 * updates: mirrors.huaweicloud.com
Installed:
  rrdtool.x86_64 0:1.3.8-10.el6 rrdtool-devel.x86_64 0:1.3.8-10.el6 rrdtool-perl.x86_64 0:1.3.8-10.el6
Dependency Installed:
  dejavu-lgc-sans-mono-fonts.noarch 0:2.33-1.el6
  dejavu-fonts-common.noarch 0:2.33-1.el6   dejavu-sans-fonts.noarch 0:2.33-1.el6   dejavu-sans-mono-fonts.noarch 0:2.33-1.el6   dejavu-serif-fonts.noarch 0:2.33-1.el6  
Complete!
```
> install apr-devel
```
[root@systemhub711 flume]# yum -y install apr-devel
Loaded plugins: fastestmirror, refresh-packagekit, security
Loading mirror speeds from cached hostfile
 * base: mirrors.neusoft.edu.cn
 * extras: mirrors.huaweicloud.com
 * updates: mirrors.huaweicloud.com
Installed:
  apr-devel.x86_64 0:1.3.9-5.el6_9.1  
Dependency Updated:
  apr.x86_64 0:1.3.9-5.el6_9.1 
Complete!
```
#### 4.1.3 安装ganglia
```
[root@systemhub711 flume]# rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
Retrieving http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
warning: /var/tmp/rpm-tmp.p3Rjmd: Header V3 RSA/SHA256 Signature, key ID 0608b895: NOKEY
Preparing...                ########################################### [100%]
   1:epel-release           ########################################### [100%]
[root@systemhub711 flume]# 
```
> install ganglia-gmetad
```
[root@systemhub711 flume]# yum -y install ganglia-gmetad
Loaded plugins: fastestmirror, refresh-packagekit, security
Loading mirror speeds from cached hostfile
 * base: mirrors.neusoft.edu.cn
 * extras: mirrors.huaweicloud.com
 * updates: mirrors.huaweicloud.com
Installed:
  ganglia-gmetad.x86_64 0:3.7.2-2.el6
  ganglia.x86_64 0:3.7.2-2.el6
[root@systemhub711 flume]#
```
> install ganglia-web
```
[root@systemhub711 flume]# yum -y install ganglia-web
Loaded plugins: fastestmirror, refresh-packagekit, security
Loading mirror speeds from cached hostfile
 * base: mirrors.neusoft.edu.cn
 * extras: mirrors.huaweicloud.com
 * updates: mirrors.huaweicloud.com
Installed:
  ganglia-web.x86_64 0:3.7.1-2.el6
Dependency Installed
  libXpm.x86_64 0:3.5.10-2.el6  php-ZendFramework.noarch 0:1.12.20-1.el6 php-bcmath.x86_64 0:5.3.3-49.el6 php-gd.x86_64 0:5.3.3-49.el6 php-process.x86_64 0:5.3.3-49.el6
  php-xml.x86_64 0:5.3.3-49.el6
[root@systemhub711 flume]# 
```
> install -y ganglia-gmond
```
[root@systemhub711 flume]# yum install -y ganglia-gmond
Loaded plugins: fastestmirror, refresh-packagekit, security
Loading mirror speeds from cached hostfile
 * base: mirrors.neusoft.edu.cn
 * extras: mirrors.huaweicloud.com
 * updates: mirrors.huaweicloud.com
Setting up Install Process
Running Transaction
  Installing : ganglia-gmond-3.7.2-2.el6.x86_64
  1/1 
  Verifying  : ganglia-gmond-3.7.2-2.el6.x86_64
  1/1 
Installed:
  ganglia-gmond.x86_64 0:3.7.2-2.el6
[root@systemhub711 flume]# 
```
#### 4.1.4 修改配置文件
> `/etc/httpd/conf.d/ganglia.conf`
```
[root@systemhub711 flume]# vim /etc/httpd/conf.d/ganglia.conf
```
```
#
# Ganglia monitoring system php web frontend
#
Alias /ganglia /usr/share/ganglia\
<Location /ganglia>
  Order deny,allow
  Deny from all
  Allow from all
  # Allow from 127.0.0.1
  # Allow from ::1
  # Allow from .example.com
</Location>
```
> `/etc/ganglia/gmetad.conf`
```
[root@systemhub711 flume]# vim /etc/ganglia/gmetad.conf
```
```
data_source "systemhub711" 122.16.178.132
```
> `/etc/ganglia/gmond.conf`
```
[root@systemhub711 flume]# vim /etc/ganglia/gmond.conf
```
```
/*
 * The cluster attributes specified will be used as part of the <CLUSTER>
 * tag that will wrap all hosts collected by this instance.
 */
cluster {
  name = "systemhub711"
  owner = "unspecified"
  latlong = "unspecified"
  url = "unspecified"
}

/* Feel free to specify as many udp_send_channels as you like.  Gmond
   used to only support having a single channel */
udp_send_channel {
  #bind_hostname = yes # Highly recommended, soon to be default.
                       # This option tells gmond to use a source address
                       # that resolves to the machine's hostname.  Without
                       # this, the metrics may appear to come from any
                       # interface and the DNS names associated with
                       # those IPs will be used to create the RRDs.
  #mcast_join = 239.2.11.71
  host = 122.16.178.132
  port = 8649
  ttl = 1
}

/* You can specify as many udp_recv_channels as you like as well. */
udp_recv_channel {
  #mcast_join = 239.2.11.71
  port = 8649
  bind = 122.16.178.132
  retry_bind = true
  # Size of the UDP buffer. If you are handling lots of metrics you really
  # should bump it up to e.g. 10MB or even higher.
  # buffer = 10485760
}
```
> `/etc/selinux/config`
```
[root@systemhub711 flume]# vim /etc/selinux/config
```
``` dsconfig
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - No SELinux policy is loaded.
#     SELINUX=enforcing
SELINUX=disabled
# SELINUXTYPE= can take one of these two values:
#     targeted - Targeted processes are protected,
#     mls - Multi Level Security protection.
SELINUXTYPE=targeted
```
> selinux本次生效关闭必须重启,如果此时不想重启,可以临时生效
```
[root@systemhub711 flume]# sudo setenforce 0
```

#### 4.1.5 启动ganglia
##### 4.1.5.1 启动服务
```
[root@systemhub711 flume]# service httpd start
正在启动 httpd：
[root@systemhub711 flume]# service gmetad start
Starting GANGLIA gmetad:  [确定]
[root@systemhub711 flume]# service gmond start
Starting GANGLIA gmond:  [确定]
[root@systemhub711 flume]# 
```
##### 4.1.5.2 Browser access
> http://systemhub711/ganglia
> 
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/start_016.jpg)


### 4.2 操作Flume测试监控
#### 4.2.1 修改flume-env.sh配置
```
[root@systemhub711 conf]# vim flume-env.sh
```
```
export JAVA_OPTS="-Dflume.monitoring.type=ganglia -Dflume.monitoring.hosts=122.16.178.132:8649 -Xms100m -Xmx200m"
```
#### 4.2.2 启动flume任务
```
[root@systemhub711 flume]# bin/flume-ng agent 
--conf conf/ 
--name a1 
--conf-file job/flume_telnet_logger.conf 
-Dflume.root.logger==INFO,console 
-Dflume.monitoring.type=ganglia 
-Dflume.monitoring.hosts=122.16.178.132:8649

Info: Sourcing environment configuration script /opt/module/flume/conf/flume-env.sh
Info: Including Hadoop libraries found via (/opt/module/hadoop/bin/hadoop) for HDFS access
Info: Including Hive libraries found via (/opt/module/hive) for Hive access
```
#### 4.2.3 发送数据查看Ganglia监测图
```
[root@systemhub711 ~]# telnet systemhub711 44444
Trying ...
Connected to systemhub711.
Escape character is '^]'.
01010101
OK
```
```
(SinkRunner-PollingRunner-DefaultSinkProcessor) [INFO - org.apache.flume.sink.LoggerSink.process(LoggerSink.java:95)] Event: { headers:{} body: 30 31 30 31 30 31 30 31 0D                      01010101. }
```
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/start_018.jpg)

> 监测说明
| 字段 (图表名称) | 字段含义 |
| :--------: | :--------:|
| EventPutAttemptCount    |   Source尝试写入Channel事件总数量. |
| EventPutSuccessCount    |   成功写入Channel且提交事件总数量. |
| EventTakeAttemptCount    |   Sink尝试从Channel拉取事件总数量,这不意味着每次事件都被返回,因为Sink拉取时候Channel可能没有任何数据. |
| EventTakeSuccessCount    |   Sink成功读取事件总数量. |
| StartTime    |   Channel启动时间 (毫秒) |
| StopTime    |   Channel停止时间 (毫秒) |
| ChannelSize    |   目前Channel中事件总数量. |
| ChannelFillPercentage    |   Channel占用百分比. |
| ChannelCapacity    |   Channel容量. |




## 5. 企业面试题(重点)
### 5.1 如何实现Flume数据传输监控
> 使用第三方框架Ganglia实时监控Flume.

### 5.2 Flume中Source/Sink/Channel的作用
> 作用 : 
> 
> `Source组件`是专门用于收集数据,可以处理各种类型,各种格式日志数据,包括Avro / Thrift / Exec / Jms / Spooling Directory / Netcat / Sequence Generator / Syslog / Http / Legacy
> 
> `Channel组件`对采集到的数据进行缓存,可以存放在Memory或File中.
> 
> `Sink组件`是用于把数据发送发送到目的地的组件,目的地包括HDFS / Looger / Avro / Thrift / Ipc / File / HBase / Solr / 自定义.
> 
> `Source类型为` : 
> 监控后后台日志 : exec
> 监控后台产生日志端口 : netcat

### 5.3 Flume Channel Selectors
> Channel Selectors可以让不同的项目日志通过不同的Channel到不同的Sink中.
> 
> Channel Selectors (选择器)有两种类型 : 
> Replicating Channel Selector (Flume默认选择器)
> Multiplexing Channel Selector
> 
> 这两种Selector区别是Replicating会将Source的Events发往所有的Channel,类似于广播式传输,而Multiplexing可以选择Channel发送数据.

### 5.4 Flume 参数调优
> `Source`
> 可以增加Source个数,可以增大Source读取数据的能力.
> 目录产生文件过多时,需要将这个文件目录拆分成多个文件目录,同时配置好多个Source以保证Source有足够能力获取新产生的数据.
> 
> batchSize参数决定Source一次批量传输到Channel的Enent条数,适当将阈值调大,可以提高Source搬运Enent到Channel时的性能.
> 
> `Channel`
> type选择Memory是Channel性能最好,但是如果Flume进程意外宕机可能会丢失数据,type选择File时Channel容量性更好,但是性能上会比Memory Channel差.
> 使用File Channel时dataDirs配置多个不同磁盘下的目录可以提高性能.
> 
> `Sink`
> 增加Sink个数,也可以增加Sink消费Event的能力,Sink并不是增加的越多越好,过多Sink会占用系统资源,造成系统资源不必要的浪费.
> 
> batchSize参数决定Sink一次批量从Channel读取Event条数,适当将阈值调大可以提高Sink从Channel搬出Event性能.

### 5.5 Flume 事务机制
> Flume数据机制(类似于数据库事务机制) : Flume使用两个独立的事物分别负责从Source到Channel,以及从Channel到Sink的事物传递.
> 
> 比如Spooling Directory Source为文件的每一行创建一个事物,一旦事物中所有事件全部传递到Channel且提交成功,那么Source就会将该文件标记为已完成任务.
> 
> 同理,事物以类似的方式处理从Channel到Sink的传递过程,如果因为某种原因使得事件无法记录,那么事物将会数据回滚,且所有事件都会保存到Channel中,等待重新传递.
### 5.6 Flume 采集数据会丢失吗
> Channel有两种存储方式
> Memory Channel / File Channel
> 
> 当Channel存储方式采用File Channel,不会丢失数据,因为数据存储在磁盘中,且自身有事物机制.
> 
> 当Channel存储方式采用Memory Channel,会丢失数据,因为数据存储在内存中,数据传输可靠性差.


## 6. 修仙之道 技术架构迭代 登峰造极之势
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