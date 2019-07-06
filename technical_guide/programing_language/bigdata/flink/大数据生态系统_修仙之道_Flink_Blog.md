# 大数据Flink生态系统 修仙之道 Flink Blog

@(2019-06-01)[ Docs Language:简体中文 & English|Programing Flink|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)|![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg) | ![GitHub repo size in bytes](https://img.shields.io/github/repo-size/geekparkhub/geekparkhub.github.io.svg) | GeekDeveloper:[JEEP-711](https://github.com/jeep711)|Github:[github.com/geekparkhub](https://github.com/geekparkhub)|Gitee:[gitee.com/geekparkhub](https://gitee.com/geekparkhub) ]

## 🐘 Flink Technology 修仙之道 四禅八定 🐘

![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/flink.jpg)

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



## 🔥 0. 在学习Flink之前你需要了解 🔥
> 在继续学习本路线之前,你应该了解一些基本计算机编程术语.
> 
> Flink是新一代分布式流式处理计算引擎,是大数据重要内容.
> 
> 此学习路线将基于Scala编程语言对Flink核心环节进行详细操作.
> 
> 如果你学习过Java & Scala编程语言 & Spark计算框架,将有助于你更快了解掌握Flink核心技术.


## 🔥 1. 概述 🔥

### 1.1 流处理 技术演变
> 在开源世界里 , ApacheStorm项目是流处理的先锋.
> 
> Storm最早由NathanMarz和创业公司BackType团队开发,后来才被Apache基金会接纳.
> 
> Storm提供了低延迟流处理,但是它为实时性付出了一些代价 : 很难实现高吞吐,并且其正确性没能达到通常所需水平,换句话说它并不能保证exactly-once,即便是它能够保证正确性级别,其开销也相当大.
> 
> 在低延迟和高吞吐流处理系统中维持良好的容错性是非常困难,但是为了得到有保障的准确状态.
> 
> 开发者们想到了一种替代方法 : 将连续时间中的流数据分割成一系列微小的批量作业,如果分割得足够小(即所谓的微批处理作业),计算就几乎可以实现真正流处理.
> 
> 因为存在延迟,所以不可能做到完全实时,但是每个简单的应用程序都可以实现仅有几秒甚至几亚秒延迟,这就是在Spark批处理引擎上运行的Spark Streaming所使用的方法.
> 
> 更重要的是使用微批处理方法,可以实现exactly-once语义,从而保障状态一致性.
> 
> 如果一个微批处理失败,它可以重新运行,这比连续流处理方法更容易.
> 
> StormTrident是对Storm的延伸,它底层流处理引擎就是基于微批处理方法来进行计算,从而实现了exactly-once语义,但是在延迟性方面付出了很大的代价.
> 
> 对于StormTrident以及Spark Streaming等微批处理策略,只能根据批量作业时间倍数进行分割,无法根据实际情况分割事件数据,并且对于一些对延迟比较敏感作业,往往需要开发者在写业务代码时花费大量精力来提升性能,这些灵活性和表现力方面的缺陷,使得这些微批处理策略开发速度变慢,运维成本变高.
> 
> 于是Flink出现了,这一技术框架可以避免上述弊端,并且拥有所需的诸多功能,还能按照连续事件高效地处理数据,Flink部分特性如下图所示 : 
> 
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_001.jpg)

### 1.2 初识 Flink
> Flink起源于Stratosphere项目,Stratosphere是在2010~2014年由3所地处柏林的大学和欧洲一些其他的大学共同进行的研究项目.
> 
> 2014年4月Stratosphere的代码被复制并捐赠给了Apache软件基金会,参加这个孵化项目的初始成员是Stratosphere系统核心开发人员.
> 
> 2014年12月,Flink一跃成为Apache软件基金会顶级项目.
> 
> 在德语中,Flink一词表示快速和灵巧,项目采用一只松鼠彩色图案作为logo.
> 
> 这不仅是因为松鼠具有快速和灵巧的特点,还因为柏林松鼠有一种迷人的红棕色,而Flink松鼠logo拥有可爱的尾巴,尾巴的颜色与Apache软件基金会logo颜色相呼应,也就是说这是一只Apache风格的松鼠.
> 
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_002.jpg)
> 
> Flink官方主页在其顶部展示了该项目的理念 : Apache Flink是为分布式、高性能、随时可用以及准确的流处理应用程序打造的开源流处理框架.
> 
> Apache Flink是一个框架和分布式处理引擎,用于对无界和有界数据流进行有状态计算.


### 1.3 批处理 & 流处理
> 批处理特点 : 有界、持久、大量,批处理非常适合需要访问全真记录才能完成的计算工作,一般用于离线统计.
> 
> 流处理特点 : 无界、实时,流处理方式无需针对整个数据集执行操作,而是对通过系统传输的每个数据项执行操作,一般用于实时统.
> 
> 在 spark生态体系中,对于批处理和流处理采用了不同的技术框架 : 
> 批处理由sparkSQL实现,流处理sparkStreaming实现,这也是大部分框架采用的策略,使用独立的处理器实现批处理和流处理.
> 
> 而Flink可以同时实现批处理和流处理,Flink将批处理(既处理有限的静态数据)视作一种特殊流处理.


### 1.4 Flink 核心计算框架
> Flink核心计算架构是图中Flink Runtime执行引擎,它是一个分布式系统,能够接受数据流程序并在一台或多台机器上以容错方式执行.
> 
> FlinkRuntime执行引擎可以作为YARN(Yet Another Resource Negotiator)应用程序在集群上运行,也可以在Mesos集群上运行,还可以在单机上运行(这对于调试Flink应用程序来说非常有用)
> 
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_003.jpg)
> 
> Flink技术栈核心组成部分,Flink分别提供`面向流式处理接口(DataStream API)`和`面向批处理接口(DataSet API)`.
> 
> 因此Flink既可以完成流处理,也可以完成批处理.
> 
> Flink支持拓展库涉及机器学习(FlinkML) / 复杂事件处理(CEP) / 图计算(Gelly),还有分别针对流处理和批处理(Table API).
> 
> 能被FlinkRuntime执行引擎接受程序很强大,但是随着程序有着冗长的代码,编写起来也很费力,基于这个原因,Flink提供了封装在Runtime执行引擎之上的API,以帮助开发者方便地生成流式计算程序.
> 
> Flink提供了用于`流处理 DataStream API`和用于`批处理 DataSet API`,值得注意的是尽管FlinkRuntime执行引擎是基于流处理,但是DataSet API先于DataStream API被开发出来,这是因为工业界对无限流处理的需求在Flink诞生之初并不大.
> 
> DataStreamAPI可以流畅地分析无限数据流,并且可以用Java或者Scala来实现,开发人员需要基于一个叫DataStream数据结构来开发,这个数据结构用于表示永不停止的分布式数据流.
> 
> Flink分布式特点体现在它能够在成百上千台机器上运行,它将大型计算任务分成许多小的部分,每个机器执行一部分.
> 
> Flink能够自动地确保发生机器故障或者其他错误时计算能够持续进行,或者在修复bug或进行版本升级后有计划地再执行一次,这种能力使得开发人员不需要担心运行失败.
> 
> Flink本质上使用容错性数据流,这使得开发人员可以分析持续生成且永远不结束数据(即流处理).


## 🔥 2. Flink 基本架构 🔥
### 2.1 JobManager & TaskManager
> Flink运行时包含两种类型处理器 : 
> 
> 1.**JobManager处理器** : 
> 
> 也称之为Master,用于协调分布式执行,它用来调度task,协调检查点,协调失败时恢复等,Flink运行时至少存在一个master处理器,如果配置高可用模式则会存在多个master处理器,它们其中有一个是leader,而其他都是standby.
> 
> 2.**TaskManager处理器** : 
> 
> 也称之为Worker,用于执行一个dataflow的task(或者特殊的subtask)、数据缓冲和data stream的交换,Flink运行时至少会存在一个worker处理器.
> 
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_004.jpg)
> 
> Master和Worker处理器可以直接在物理机上启动,或者通过像YARN资源调度框架启动.
> 
> Worker连接到Master,告知自身可用性进而获得任务分配.

### 2.2 无界数据流 & 有界数据流
> Flink用于处理有界和无界数据 : 
> 
> **无界数据流** : 
> 无界数据流有一个开始但是没有结束,它们不会在生成时终止并提供数据,必须连续处理无界流,也就是说必须在获取后立即处理event,对于无界数据流无法等待所有数据都到达,因为输入是无界的,并且在任何时间点都不会完成,处理无界数据通常要求以特定顺序(例如事件发生顺序)获取event,以便能够推断结果完整性,无界流处理称为流处理.
> 
> **有界数据流** : 
> 有界数据流有明确定义开始和结束,可以在执行任何计算之前通过获取所有数据来处理有界流,处理有界流不需要有序获取,因为可以始终对有界数据集进行排序,有界流的处理也称为批处理.
> 
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_005.jpg)
> 
> Apache Flink是一个面向分布式数据流处理和批量数据处理的开源计算平台,它能够基于同一个Flink运行时(Flink  Runtime),提供支持流处理和批处理两种类型应用的功能.
> 
> 现有开源计算方案会把流处理和批处理作为两种不同的应用类型.
> 
> 因为它们要实现目标是完全不相同的 : 流处理一般需要支持低延迟、Exactly-once保证,而批处理需要支持高吞吐、高效处理,所以在实现时通常是分别给出两套实现方法.
> 
> 或者通过独立开源框架来实现其中每一种处理方案,例如实现批处理开源方案有MapReduce / Tez / Crunch / Spark,实现流处理开源方案有Samza / Storm等.
> 
> Flink在实现流处理和批处理时,与传统方案完全不同,它从另一个视角看待流处理和批处理,将二者统一起来 : Flink是完全支持流处理,也就是说作为流处理看待时输入数据流是无界的,批处理被作为一种特殊流处理,只是它的输入数据流被定义为有界,基于同一个Flink运行时(Flink Runtime),分别提供了流处理和批处理API,而这两种API也是实现上层面向流处理、批处理类型应用框架基础.

### 2.3 数据流 编程模型
> Flink提供了不同级别抽象,以开发流或批处理作业,如下图所示 : 
> 
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_006.jpg)
> 
> **1. Process Function**
> 
> 最底层级的抽象仅仅提供了有状态流,它将通过过程函数(Process Function)被嵌入到DataStream API中.
> 
> 底层过程函数(Process Function)与DataStream API 相集成,使其可以对某些特定操作进行底层抽象,它允许开发者可以自由地处理来自一个或多个数据流的事件,并使用一致容错的状态,除此之外开发者可以注册事件时间并处理时间回调,从而使程序可以处理复杂计算.
> 
> **2. Core APIs**
> 
> 实际上大多数应用并不需要上述底层抽象,而是针对核心API(Core APIs)进行编程,比如DataStream API(有界或无界流数据)以及DataSet API(有界数据集).
> 
> 这些API为数据处理提供了通用构建模块,比如由开发者定义多种形式转换(transformations),连接(joins),聚合(aggregations),窗口操作(windows)等等.
> 
> DataSet API为有界数据集提供了额外支持,例如循环与迭代,这些API处理数据类型以类(classes)形式由各自编程语言所表示.
> 
> **3. Table API**
> Table API以表为中心,其中表可能会动态变化(在表达流数据时).
> 
> Table API遵循(扩展)关系模型 : 表有二维数据结构(schema)(类似于关系数据库中的表),同时API提供可比较的操作,例如select / project / join / group-by / aggregate等.
> 
> Table API程序声明式地定义什么逻辑操作应该执行,而不是准确地确定这些操作代码的看上去如何,尽管Table API可以通过多种类型的开发者自定义函数(UDF)进行扩展,其仍不如核心API更具表达能力,但是使用起来却更加简洁(代码量更少),除此之外Table API程序在执行之前会经过内置优化器进行优化.
> 开发者可以在表与DataStream/DataSet之间无缝切换,以允许程序将Table API与DataStream以及DataSet 混合使用.
> 
> **4. SQL**
> 
> Flink提供最高层级的抽象是SQL,这一层抽象在语法与表达能力上与Table API类似,但是是以SQL查询表达式的形式表现程序,SQL抽象与Table API交互密切,同时SQL查询可以直接在Table API定义的表上执行.


## 🔥 3. Flink 集群部署 🔥

### 3.1 Flink for Linux 部署
> Flink可以选择部署方式有 : 
> 
> Local / Standalone(资源利用率低) / Yarn / Mesos / Docker / Kubernetes / AWS
> 
> 现有主要对Standalone模式和Yarn模式下进行Flink集群部署.

- Flink 官方地址 : [flink.apache.org/zh/](https://flink.apache.org/zh/)
- Flink 官方下载 : [archive.apache.org/dist/flink/flink-1.6.1/](https://archive.apache.org/dist/flink/flink-1.6.1/)
- Flink 官方文档 : [ci.apache.org/projects/flink/flink-docs-release-1.6/](https://ci.apache.org/projects/flink/flink-docs-release-1.6/)

1.解压`flink-1.6.1-bin-hadoop2.7-scala_2.11.tgz`
```
[root@systemhub511 ~]# cd /opt/software/
[root@systemhub511 software]# tar -zxvf flink-1.6.1-bin-hadoop2.7-scala_2.11.tgz -C /opt/module/
```
2.重命名`flink-1.6.1`
```
[root@systemhub511 software]# cd ..
[root@systemhub511 opt]# cd module/
[root@systemhub511 module]# mv flink-1.6.1 flink
```

### 3.2 Standalone 模式
3. vim `flink-conf.yaml` | 在conf目录下修改flink-conf.yaml文件,指定JobManager
``` powershell
[root@systemhub511 module]# cd flink/conf/
[root@systemhub511 conf]# vim flink-conf.yaml
```
```
jobmanager.rpc.address: systemhub611

# The RPC port where the JobManager is reachable.
```
 
4. vim `slaves` | 在conf目录下修改slave文件,指定TaskManager
```
[root@systemhub511 conf]# vim slaves
```
```
systemhub511
systemhub711
```
5.配置完毕 将flink集群分发
```
[root@systemhub511 module]# scp -r ./flink/ root@systemhub611:/opt/module/flink/
[root@systemhub511 module]# scp -r ./flink/ root@systemhub711:/opt/module/flink/
```
6.在systemhub611节点启动flink集群
```
[root@systemhub511 module]# cd flink/
[root@systemhub611 flink]# ./bin/start-cluster.sh
Starting cluster.
Starting standalonesession daemon on host systemhub511.
Starting taskexecutor daemon on host systemhub611.
Starting taskexecutor daemon on host systemhub711.
[root@systemhub611 flink]# 
```
7.查看flink集群进程
```
[root@systemhub611 flink]# jps.sh
                                                               
                                                           
                            
 ██████╗ ███████╗███████╗██╗  ██╗██████╗  █████╗ ██████╗ ██╗  ██╗██╗  ██╗██╗   ██╗██████╗ 
██╔════╝ ██╔════╝██╔════╝██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██║  ██║██║   ██║██╔══██╗
██║  ███╗█████╗  █████╗  █████╔╝ ██████╔╝███████║██████╔╝█████╔╝ ███████║██║   ██║██████╔╝
██║   ██║██╔══╝  ██╔══╝  ██╔═██╗ ██╔═══╝ ██╔══██║██╔══██╗██╔═██╗ ██╔══██║██║   ██║██╔══██╗
╚██████╔╝███████╗███████╗██║  ██╗██║     ██║  ██║██║  ██║██║  ██╗██║  ██║╚██████╔╝██████╔╝
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 

                Open · Creation | Website | https://www.geekparkhub.com/
    
Open Source Open Achievement Dream , GeekParkHub Co-construction has never been seen before. 


===========     root@systemhub511 All Processes         ===========
9384 sun.tools.jps.Jps
9306 org.apache.flink.runtime.entrypoint.StandaloneSessionClusterEntrypoint
===========     root@systemhub611 All Processes         ===========
9686 sun.tools.jps.Jps
9622 org.apache.flink.runtime.taskexecutor.TaskManagerRunner
===========     root@systemhub711 All Processes         ===========
9426 org.apache.flink.runtime.taskexecutor.TaskManagerRunner
9470 sun.tools.jps.Jps
[root@systemhub511 flink]# 
```
8.可通过WebUI访问flink | http://hostname:8081/#/overview
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_007.jpg)
> 
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_008.jpg)


### 3.3 Yarn 模式
> 1.确保已经设置HADOOP_HOME环境变量
> 
> 2.启动Hadoop集群 (HDFS和Yarn)
```
[root@systemhub611 ~]# start-cluster.sh
                                                        
 ██████╗ ███████╗███████╗██╗  ██╗██████╗  █████╗ ██████╗ ██╗  ██╗██╗  ██╗██╗   ██╗██████╗ 
██╔════╝ ██╔════╝██╔════╝██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██║  ██║██║   ██║██╔══██╗
██║  ███╗█████╗  █████╗  █████╔╝ ██████╔╝███████║██████╔╝█████╔╝ ███████║██║   ██║██████╔╝
██║   ██║██╔══╝  ██╔══╝  ██╔═██╗ ██╔═══╝ ██╔══██║██╔══██╗██╔═██╗ ██╔══██║██║   ██║██╔══██╗
╚██████╔╝███████╗███████╗██║  ██╗██║     ██║  ██║██║  ██║██║  ██╗██║  ██║╚██████╔╝██████╔╝
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 

                Open · Creation | Website | https://www.geekparkhub.com/
    
Open Source Open Achievement Dream , GeekParkHub Co-construction has never been seen before. 


================                Start All Node Services         ===========
================================================================
================                Starting Zookeeper              ===========
================================================================
Starting zookeeper ... ZooKeeper JMX enabled by default
Using config: /opt/module/zookeeper/bin/../conf/zoo.cfg
STARTED
ZooKeeper JMX enabled by default
Using config: /opt/module/zookeeper/bin/../conf/zoo.cfg
Starting zookeeper ... STARTED
ZooKeeper JMX enabled by default
Using config: /opt/module/zookeeper/bin/../conf/zoo.cfg
Starting zookeeper ... STARTED
================                Starting HDFS           ===========
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/opt/module/hadoop/share/hadoop/common/lib/slf4j-log4j12-1.7.10.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/opt/module/hbase/lib/slf4j-log4j12-1.7.5.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
Starting namenodes on [systemhub511]
systemhub511: starting namenode, logging to /opt/module/hadoop/logs/hadoop-root-namenode-systemhub511.out
systemhub511: SLF4J: Class path contains multiple SLF4J bindings.
systemhub511: SLF4J: Found binding in [jar:file:/opt/module/hadoop/share/hadoop/common/lib/slf4j-log4j12-1.7.10.jar!/org/slf4j/impl/StaticLoggerBinder.class]
systemhub511: SLF4J: Found binding in [jar:file:/opt/module/hbase/lib/slf4j-log4j12-1.7.5.jar!/org/slf4j/impl/StaticLoggerBinder.class]
systemhub511: SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
systemhub511: SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
systemhub711: starting datanode, logging to /opt/module/hadoop/logs/hadoop-root-datanode-systemhub711.out
systemhub511: starting datanode, logging to /opt/module/hadoop/logs/hadoop-root-datanode-systemhub511.out
systemhub611: starting datanode, logging to /opt/module/hadoop/logs/hadoop-root-datanode-systemhub611.out
Starting secondary namenodes [systemhub711]
systemhub711: starting secondarynamenode, logging to /opt/module/hadoop/logs/hadoop-root-secondarynamenode-systemhub711.out
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/opt/module/hadoop/share/hadoop/common/lib/slf4j-log4j12-1.7.10.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/opt/module/hbase/lib/slf4j-log4j12-1.7.5.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
================                Starting YARN           ===========
starting yarn daemons
starting resourcemanager, logging to /opt/module/hadoop/logs/yarn-root-resourcemanager-systemhub611.out
systemhub711: starting nodemanager, logging to /opt/module/hadoop/logs/yarn-root-nodemanager-systemhub711.out
systemhub511: starting nodemanager, logging to /opt/module/hadoop/logs/yarn-root-nodemanager-systemhub511.out
systemhub611: starting nodemanager, logging to /opt/module/hadoop/logs/yarn-root-nodemanager-systemhub611.out
================                Starting JobHistoryServer       ===========
starting historyserver, logging to /opt/module/hadoop/logs/mapred-root-historyserver-systemhub511.out
[root@systemhub511 ~]#
```
> 3.在systemhub611节点提交Yarn-Session,使用yarn-session.sh脚本进行提交.
> 
> 参数说明 : 
> 
> `-n` (--container) : TaskManager数量
> 
> `-s` (--slots) : 每个TaskManager的slot数量,默认一个slot一个core,默认每个taskmanager的slot的个数为1,有时可以多一些taskmanager,做冗余.
> 
> `-jm` : JobManager内存 (单位MB)
> 
> `-tm` : 每个taskmanager内存 (单位MB)
> 
> `-nm` : yarn 的appName (即表示yarn应用名称)
> 
> `-d` : 后台执行
> 
```
[root@systemhub611 ~]# cd /opt/module/flink/
[root@systemhub611 flink]# ./bin/yarn-session.sh -n 2 -s 6 -jm 1024 -tm 1024 -nm test -d
```
> 4.启动后查看HadoopWebUi,可以查看任务提交
> 
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_009.jpg)
> 
> 5.查看进程 提交Session节点
```
[root@systemhub611 conf]# jps -l
5540 org.apache.zookeeper.server.quorum.QuorumPeerMain
5781 org.apache.hadoop.yarn.server.resourcemanager.ResourceManager
8277 sun.tools.jps.Jps
8089 org.apache.flink.yarn.entrypoint.YarnSessionClusterEntrypoint
5609 org.apache.hadoop.hdfs.server.datanode.DataNode
5886 org.apache.hadoop.yarn.server.nodemanager.NodeManager
[root@systemhub611 conf]# 
```
> 6.提交Jar到集群运行
```
[root@systemhub611 flink]# ./bin/flink run -m yarn-cluster ./examples/batch/WordCount.jar
```
> 7.提交后在YarnWebUI查看任务运行情况
> 
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_010.jpg)
> 
> 8.任务结束 查看运行结果
```
Use --input to specify file input.
Printing result to stdout. Use --output to specify output path.
(a,5)
(action,1)
(after,1)
(against,1)
(all,2)
(for,2)
(fortune,1)
(would,2)
(wrong,1)
(you,1)
Program execution finished
Job with JobID c2f9e1af0aaf6005895fa362f2ae5d5b has finished.
Job Runtime: 41972 ms
Accumulator Results: 
- 8835528805a89471c138d1cd86fd473b (java.util.ArrayList) [170 elements]
[root@systemhub611 flink]#
```


## 🔥 4. Flink 运行架构 🔥
### 4.1 任务提交流程

> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_011.jpg)
> 
> Flink任务提交后,Client向HDFS上传Flink的Jar包和配置.
> 
> 之后向YarnResourceManager提交任务,ResourceManager分配Container资源并通知对应的NodeManager启动ApplicationMaster.
> 
> ApplicationMaster启动后加载Flink的Jar包和配置构建环境,然后启动JobManager.
> 
> 之后ApplicationMaster向ResourceManager申请资源启动TaskManager,ResourceManager分配Container资源后,由ApplicationMaster通知资源所在节点的NodeManager启动TaskManager.
> 
> NodeManager加载Flink的Jar包和配置构建环境并启动TaskManager,TaskManager启动后向JobManager发送心跳包,并等待JobManager向其分配任务.
> 

### 4.2 任务调度流程
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_012.jpg)
> 
> 客户端不是运行时和程序执行的一部分,但它用于准备并发送dataflow给Master,然后客户端断开连接或者维持连接以等待接收计算结果,客户端可以以两种方式运行 : 要么作为Java/Scala程序的一部分被程序触发执行,要么以命令行./bin/flink run方式执行.

### 4.3 Worker & Slots
> 每一个worker(TaskManager)是一个JVM进程,它可能会在独立的线程上执行一个或多个subtask.
> 
> 为了控制一个worker能接收多少个task,worker通过task slot来进行控制(一个worker至少有一个task slot).
> 
> 每个task slot表示TaskManager拥有资源的一个固定大小的子集.
> 
> 假如一个TaskManager有三个slot.那么它会将其管理的内存分成三份给各个slot.
> 
> 资源slot化意味着一个subtask将不需要跟来自其他job的subtask竞争被管理的内存.取而代之的是它将拥有一定数量的内存储备.
> 
> 需要注意的是这里不会涉及到CPU隔离,slot目前仅仅用来隔离task的受管理的内存.
> 
> 通过调整task slot的数量,允许开发者定义subtask之间如何互相隔离.
> 
> 如果一个TaskManager一个slot,那将意味着每个task group运行在独立的JVM中(该JVM可能是通过一个特定的容器启动),而一个TaskManager多个slot意味着更多的subtask可以共享同一个JVM,而在同一个JVM进程中的task将共享TCP连接(基于多路复用)和心跳消息,它们也可能共享数据集和数据结构,因此这减少了每个task的负载.
> 
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_013.jpg)
> 
> TaskSlot是静态概念,是指TaskManager具有的并发执行能力,可以通过参数`taskmanager.numberOfTaskSlots`进行配置.
> 
> 而并行度parallelism是动态概念,即TaskManager运行程序时实际使用的并发能力,可以通过参数`parallelism.default`进行配置.
> 
> 也就是说,假设一共有3个TaskManager,每一个TaskManager中的分配3个TaskSlot,也就是每个TaskManager可以接收3个task,一共9个TaskSlot.
> 
> 如果设置`parallelism.default=1`,即运行程序默认的并行度为1,9个TaskSlot只用了1个,有8个空闲,因此设置合适的并行度才能提高效率.
> 

### 4.4 程序与数据流
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_014.jpg)
> 
> Flink程序的基础构建模块是流(streams)与转换(transformations),需要注意的是Flink的DataSet API所使用的DataSets其内部也是stream.
> 
> 一个stream可以看成一个中间结果,而一个transformations是以一个或多个stream作为输入的某种operation,该operation利用这些stream进行计算从而产生一个或多个result stream.
> 
> 在运行时Flink上运行程序会被映射成streaming dataflows,它包含了streams和transformationsoperators.
> 
> 每一个dataflow以一个或多个sources开始以一个或多个sinks结束.
> 
> dataflow类似于任意的有向无环图(DAG),当然特定形式的环可以通过iteration构建.
> 
> 在大部分情况下,程序中的transformations跟dataflow中的operator是一一对应关系,但有时候,一个transformation可能对应多个operator.

### 4.5 并行数据流
> Flink程序执行具有并行、分布式的特性.
> 
> 在执行过程中一个stream包含一个或多个stream partition,而每一个operator包含一个或多个operator subtask,这些operator subtasks在不同的线程、不同的物理机或不同的容器中彼此互不依赖得执行.
> 
> 一个特定operator的subtask的个数被称之为其parallelism(并行度).
> 
> 一个stream的并行度总是等同于其producing operator的并行度.
> 
> 一个程序中不同的operator可能具有不同的并行度.
> 
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_015.jpg)
> 
> Stream在operator之间传输数据的形式可以是one-to-one(forwarding)的模式也可以是redistributing的模式,具体是哪一种形式取决于operator的种类.
> 
> `One-to-one` : stream(比如在source和map operator之间)维护着分区以及元素的顺序,那意味着map operator的subtask看到的元素的个数以及顺序跟source operator的subtask生产的元素的个数、顺序相同,map、fliter、flatMap等算子都是one-to-one的对应关系.
> 
> `Redistributing` : stream(map()跟keyBy/window之间或者keyBy/window跟sink之间)的分区会发生改变.
> 
> 每一个operator subtask依据所选择的transformation发送数据到不同的目标subtask.
> 
> 例如keyBy()基于hashCode重分区、broadcast和rebalance会随机重新分区,这些算子都会引起redistribute过程,而redistribute过程就类似于Spark中的shuffle过程.

### 4.6 task & operatorchains
> 出于分布式执行的目的,Flink将operator的subtask链接在一起形成task,每个task在一个线程中执行.
> 
> 将operators链接成task是非常有效的优化 : 它能减少线程之间的切换和基于缓存区的数据交换,在减少时延的同时提升吞吐量,链接的行为可以在编程API中进行指定.
> 
> 以下展示5个subtask以5个并行线程执行
> 
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_016.jpg)


## 🔥 5. Flink DataStream API 🔥
### 5.1 Flink 运行模型
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_017.jpg)
> 
> 以上为Flink的运行模型,Flink的程序主要由三部分构成 : 
> 
> 分别为`Source` -> `Transformation` -> `Sink`
> 
> **DataSource** : 主要负责数据的读取.
> 
> **Transformation** : 主要负责对属于的转换操作.
> 
> **Sink** : 负责最终数据的输出.


### 5.2 Flink程序 运行流程
- 每个Flink程序都包含以下若干流程 : 
- 1.获得执行环境 : (Execution Environment)
- 2.加载/创建初始数据 : (Source)
- 3.指定转换数据 : (Transformation)
- 4.指定放置计算结果位置 : (Sink)
- 5.触发程序执行

### 5.3 Environment
> 执行环境`Stream Execution Environment`是所有Flink程序的基础.
> 
> 创建执行环境有三种方式分别为 : 
> ```
> StreamExecutionEnvironment.getExecutionEnvironment
> StreamExecutionEnvironment.createLocalEnvironment
> StreamExecutionEnvironment.createRemoteEnvironment
> ```

#### 5.3.1 StreamExecutionEnvironment.getExecutionEnvironment
> ```
> val env = StreamExecutionEnvironment.getExecutionEnvironment
> ```
> 说明 : 创建一个执行环境,表示当前执行程序的上下文.
> 
> 如果程序是独立调用,则此方法返回本地执行环境.
> 如果从命令行客户端调用程序以提交到集群,则此方法返回此集群的执行环境,也就是说getExecutionEnvironment会根据查询运行方式决定返回什么样的运行环境,是最常用的一种创建执行环境方式.

#### 5.3.2 StreamExecutionEnvironment.createLocalEnvironment
> ```
> val env = StreamExecutionEnvironment.createLocalEnvironment(1)
> ```
> 
> 说明 : 返回本地执行环境,需要在调用时指定默认的并行度.


#### 5.3.3 StreamExecutionEnvironment.createRemoteEnvironment
> ```
> val env = StreamExecutionEnvironment.createRemoteEnvironment(1)
> ```
> 
> 说明 : 返回集群执行环境,将Jar提交到远程服务器,需要在调用时指定JobManager的IP和端口号,并指定要在集群中运行的Jar包.

### 5.4 Source
> **0. 基于Scala编程语言完成对Source/Transformation/Sink等环节进行操作**
> 
> **1. JetBrains IntelliJ IDEA New Maven Project | 此过程省略**
> 
> **2. pom配置信息 | pom.xml**
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>flink_server</artifactId>
        <groupId>com.geekparkhub.core.flink</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>

    <artifactId>flink-common</artifactId>

    <dependencies>
        <dependency>
            <groupId>org.scala-lang</groupId>
            <artifactId>scala-library</artifactId>
            <version>2.11.8</version>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-core</artifactId>
            <version>1.6.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-clients_2.11</artifactId>
            <version>1.6.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-scala_2.11</artifactId>
            <version>1.6.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-streaming-scala_2.11</artifactId>
            <version>1.6.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.cassandra</groupId>
            <artifactId>cassandra-all</artifactId>
            <version>0.8.1</version>
            <exclusions>
                <exclusion>
                    <groupId>org.slf4j</groupId>
                    <artifactId>slf4j-log4j12</artifactId>
                </exclusion>
                <exclusion>
                    <groupId>log4j</groupId>
                    <artifactId>log4j</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
    </dependencies>
</project>
```

#### 5.4.1 基于File创建输入数据源
> **1. readTextFile(path)**
> 
> 说明 : 一列一列的读取遵循TextInputFormat规范的文本文件,并将结果作为String返回.
> 
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.api.java.io.TextInputFormat
import org.apache.flink.core.fs.Path
import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * FlinkSourceFlow
  * <p>
  */

object FlinkSourceFlow extends App {

  // 调用readTextFileFlow方法
  readTextFileFlow()

  /**
    * 定义 readTextFile方法
    * 读取文本文件
    */
  def readTextFileFlow(): Unit = {
    // 创建执行环境
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    // 加载初始数据 -> (Source)
    val filePaths = "../flink_server/flink-coreflow/src/main/resources/input_01/test01.txt"
    val stream = env.readTextFile(filePaths)
    // 打印数据 -> (Sink)
    stream.print()
    // 触发程序执行
    env.execute("readTextFileFlow")
  }
}
```
- 运行查看结果
```
1> svm lr softmax gbdt
5> cnn rnn lstm gbdt
2> cnn rnn lstm gan
7> svm lr softmax adam
4> sgd adam relu rss
```

> **2. readFile(fileInputFormat, path)**
> 
> 说明 : 按照指定的文件格式读取文件
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.api.java.io.TextInputFormat
import org.apache.flink.core.fs.Path
import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * FlinkSourceFlow
  * <p>
  */

object FlinkSourceFlow extends App {

  // 调用readFileFlow方法
  readFileFlow()

  /**
    * 定义 readFileFlow方法
    * 指定文件格式读取文件
    */
  def readFileFlow(): Unit = {
    // 创建执行环境
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    // 创建文件路径
    val paths = "../flink_server/flink-coreflow/src/main/resources/input_01/test02.txt"
    val path = new Path(paths)
    // 加载初始数据 -> (Source)
    val filePath = "../flink_server/flink-coreflow/src/main/resources/input_01/test02.txt"
    val stream = env.readFile(new TextInputFormat(path), filePath)
    // 打印数据 -> (Sink)
    stream.print()
    // 触发程序执行
    env.execute("readFileFlow")
  }
}
```
- 运行查看结果
```
6> kafka 1
8> sqoop 1
4> kafka 2
5> apache 5
3> apache 3
2> kafka 1
1> apache 2
```

#### 5.4.2 基于Socket创建输入数据源
- 1.创建socketTextFlow方法
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.api.java.io.TextInputFormat
import org.apache.flink.core.fs.Path
import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * FlinkSourceFlow
  * <p>
  */

object FlinkSourceFlow extends App {

  // 调用socketTextFlow方法
  socketTextFlow()

  /**
    * 定义 socketTextFlow方法
    * 从Socket中读取信息,元素可以用分隔符分开
    */
  def socketTextFlow(): Unit ={
    // 创建执行环境
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    // 监听端口并加载初始数据 -> (Source)
    val stream = env.socketTextStream("systemhub",9999)
    // 打印数据 -> (Sink)
    stream.print()
    // 触发程序执行
    env.execute("socketTextFlow")
  }
}
```
- 2.在本地监听服务端口
```
systemhub:~ system$ nc -l 9999
```
- 3.运行程序
- 4.在本地服务端输入数据源
```
systemhub:~ system$ nc -l 9999
hello
flink
flink
socketTextFlow
socketTextFlow
socketTextFlow
socketTextFlow
socketTextFlow
socketTextFlow
socketTextFlow
```
- 5.查看运行结果
```
1> hello
2> flink
3> flink
4> socketTextFlow
5> socketTextFlow
6> socketTextFlow
7> socketTextFlow
8> socketTextFlow
1> socketTextFlow
2> socketTextFlow
```

#### 5.4.3 基于(集合 Collection)创建输入数据源
> **1. fromCollection(seq)**
> 
> 说明 : 从集合中创建一个数据流,集合中所有元素类型是一致的.
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.api.java.io.TextInputFormat
import org.apache.flink.core.fs.Path
import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * FlinkSourceFlow
  * <p>
  */

object FlinkSourceFlow extends App {

  // 调用fromCollectionFlow方法
  fromCollectionFlow()

  /**
    * 定义 fromCollectionFlow 方法
    * 从集合中创建一个数据流
    */
  def fromCollectionFlow(): Unit = {
    // 创建执行环境
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    // 创建集合,集合中所有元素类型需一致
    val list = List(1, 2, 3, 4)
    // 加载初始数据 -> (Source)
    val stream = env.fromCollection(list)
    // 打印数据 -> (Sink)
    stream.print()
    // 触发程序执行
    env.execute("fromCollectionFlow")
  }
}
```

> **2. fromCollection(Iterator)**
> 
> 说明 : 从迭代(Iterator)中创建一个数据流,指定元素数据类型的类由iterator返回.
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.api.java.io.TextInputFormat
import org.apache.flink.core.fs.Path
import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * FlinkSourceFlow
  * <p>
  */

object FlinkSourceFlow extends App {

  // 调用fromCollectionIteratorFlow方法
  fromCollectionIteratorFlow()

  /**
    * 定义 fromCollectionIteratorFlow 方法
    * 从集合中创建一个数据流
    */
  def fromCollectionIteratorFlow(): Unit = {
    // 创建执行环境
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    // 创建集合,集合中所有元素类型需一致
    val iterator = Iterator(1, 2, 3, 4)
    // 加载初始数据 -> (Source)
    val stream = env.fromCollection(iterator)
    // 打印数据 -> (Sink)
    stream.print()
    // 触发程序执行
    env.execute("fromCollectionIteratorFlow")
  }
}
```

> **3. fromElements(elements:_*)**
> 
> 从一个给定的对象序列中创建一个数据流,所有的对象必须是相同类型.
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.api.java.io.TextInputFormat
import org.apache.flink.core.fs.Path
import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * FlinkSourceFlow
  * <p>
  */

object FlinkSourceFlow extends App {

  // 调用fromElementsFlow方法
  fromElementsFlow()

  /**
    * 定义 fromElementsFlow 方法
    * 从一个给定的对象序列中创建一个数据流,所有的对象必须是相同类型
    */
  def fromElementsFlow(): Unit = {
    // 创建执行环境
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    // 创建集合,集合中所有元素类型需一致
    val list = List(1, 2, 3, 4)
    // 加载初始数据 -> (Source)
    val stream = env.fromElements(list)
    // 打印数据 -> (Sink)
    stream.print()
    // 触发程序执行
    env.execute("fromElementsFlow")
  }
}
```

> **4. generateSequence(from, to)**
> 
> 从给定的间隔中并行地产生一个数字序列.
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.api.java.io.TextInputFormat
import org.apache.flink.core.fs.Path
import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * FlinkSourceFlow
  * <p>
  */

object FlinkSourceFlow extends App {

  // 调用generateSequenceFlow方法
  generateSequenceFlow()

  /**
    * 定义 generateSequenceFlow 方法
    */
  def generateSequenceFlow(): Unit ={
    // 创建执行环境
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    // 创建初始数据 -> (Source)
    val stream = env.generateSequence(1,20)
    // 打印数据 -> (Sink)
    stream.print()
    // 触发程序执行
    env.execute("generateSequenceFlow")
  }
}
```

### 5.5 Sink
> Data Sink消费DataStream中的数据,并将它们转发到文件/套接字/外部系统或者打印出.
> 
> Flink有许多封装在DataStream操作里的内置输出格式.

#### 5.5.1 writeAsText
> 将元素以字符串形式逐行写入(TextOutputFormat),这些字符串通过调用每个元素的toString()方法来获取.

#### 5.5.2 WriteAsCsv
> 将元组以逗号分隔写入文件中(CsvOutputFormat),行及字段之间的分隔是可配置,每个字段的值来自对象的toString()方法.

#### 5.5.3 print/printToErr
> 打印每个元素的toString()方法的值到标准输出或者标准错误输出流中,或者也可以在输出流中添加一个前缀,这个可以帮助区分不同的打印调用,如果并行度大于1,那么输出也会有一个标识由哪个任务产生的标志.

#### 5.5.4 writeUsingOutputFormat
> 自定义文件输出的方法和基类(FileOutputFormat),支持自定义对象到字节的转换.

#### 5.5.5 writeToSocket
> 根据SerializationSchema将元素写入到socket中.

### 5.6 Transformation

#### 5.6.1 Map
> DataStream → DataStream : 输入一个参数产生一个参数.
> 
> stream.print() = 输出结果 4> 4 | 当前4是代表第4个并行线程输出的结果.
> 
> 即表示每一行前面的数字代表当前行是哪一个并行线程输出的结果
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * TransformationFlow
  * <p>
  */

object TransformationFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用mapFlow方法
  mapFlow()

  /**
    * 定义map方法
    * DataStream → DataStream : 输入一个参数产生一个参数.
    */
  def mapFlow(): Unit = {
    // 创建初始数据 -> (Source)
    val stream = env.generateSequence(1, 20)
    // 调用map函数
    val streamMap = stream.map(x => x * 2)
    // 打印数据 -> (Sink)
    streamMap.print()
    // 触发程序执行
    env.execute("mapFlow")
  }
}
```

#### 5.6.2 FlatMap
> DataStream → DataStream：输入一个参数,产生0个、1个或者多个输出.
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * TransformationFlow
  * <p>
  */

object TransformationFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用FlatMapFlow方法
  FlatMapFlow()

  /**
    * 定义FlatMapFlow方法
    * DataStream → DataStream：输入一个参数,产生0个、1个或者多个输出.
    */
  def FlatMapFlow(): Unit = {
    // 加载初始数据 -> (Source)
    val filePaths = "../flink_server/flink-coreflow/src/main/resources/input_01/test01.txt"
    val stream = env.readTextFile(filePaths)
    // 调用flatMap函数对数据以空格进行数据切分
    val streamFlatMap = stream.flatMap(x => x.split(" "))
    // 打印数据 -> (Sink)
    streamFlatMap.print()
    // 触发程序执行
    env.execute("FlatMapFlow")
  }
}
```

#### 5.6.3 Filter
> DataStream → DataStream : 计算每个元素的布尔值,并返回布尔值为true的元素.
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * TransformationFlow
  * <p>
  */

object TransformationFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用FilterFlow方法
  FilterFlow()

  /**
    * 定义FilterFlow方法
    * DataStream → DataStream : 计算每个元素的布尔值,并返回布尔值为true的元素.
    */
  def FilterFlow(): Unit = {
    // 创建初始数据 -> (Source)
    val stream = env.generateSequence(1, 20)
    // 调用filter函数,去除不等于1的元素的值
    val streamFilter = stream.filter(x => x == 1)
    // 打印数据 -> (Sink)
    streamFilter.print()
    // 触发程序执行
    env.execute("FilterFlow")
  }
}
```

#### 5.6.4 Connect
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_018.jpg)
> 
> DataStream , DataStream → ConnectedStreams : 连接两个保持它们类型的数据流,两个数据流被Connect之后,只是被放在ConnectedStreams同一个流中,内部依然保持各自的数据和形式不发生任何变化,两个流相互独立.
> 
> 通常Connect会与CoMap&CoFlatMap配合使用.
> 
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * TransformationFlow
  * <p>
  */

object TransformationFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用ConnectFlow方法
  ConnectFlow()

  /**
    * 定义ConnectFlow方法
    * DataStream , DataStream → ConnectedStreams
    */
  def ConnectFlow(): Unit = {
    // 加载与创建初始数据 -> (Source)
    val filePaths = "../flink_server/flink-coreflow/src/main/resources/input_01/test03.txt"
    val stream01 = env.generateSequence(1, 20)
    val stream02 = env.readTextFile(filePaths).flatMap(x => x.split(" "))
    // stream01将与stream02连接并形成ConnectedStreams连接流
    var streamConnect = stream01.connect(stream02)
    /**
      * 当ConnectedStreams在调用map函数的过程就称之为CoMap操作
      * x 即代表stream01在调用flatMap函数的过程就称之为CoFlatMap操作
      * y 即代表stream02在调用flatMap函数时的过程就称之为CoFlatMap操作
      *
      * 说明 : 对ConnectedStreams流进行CoMap操作
      * 说明 : `x` 即代表对stream01进行CoFlatMap操作
      * 说明 : `y` 即代表对stream02进行CoFlatMap操作
      *
      */
    val streamRes = streamConnect.map(x => x * 2, y => (y, 1L))
    // 打印数据 -> (Sink)
    streamRes.print()
    // 触发程序执行
    env.execute("ConnectFlow")
  }
}
```

#### 5.6.5 CoMap & CoFlatMap
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_019.jpg)
> 
> ConnectedStreams  →  DataStream : 作用于ConnectedStreams上,功能与map和flatMap一样,对ConnectedStreams中的每一个Stream分别进行map和flatMap处理.
> 
> 通常Connect会与CoMap&CoFlatMap配合使用.
> 
> **1. CoMap**
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * TransformationFlow
  * <p>
  */

object TransformationFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用CoMapFlow方法
  CoMapFlow()

  /**
    * 定义CoMapFlow方法
    * ConnectedStreams → DataStream
    */
  def CoMapFlow(): Unit = {
    // 加载与创建初始数据 -> (Source)
    val filePaths = "../flink_server/flink-coreflow/src/main/resources/input_01/test03.txt"
    val stream01 = env.generateSequence(1, 20)
    val stream02 = env.readTextFile(filePaths).flatMap(x => x.split(" "))
    // stream01将与stream02连接并形成ConnectedStreams连接流
    var streamConnect = stream01.connect(stream02)
    // 当streamConnect调用map函数的过程就称之为CoMap操作
    val streamCoMap = streamConnect.map((x) => x + 100, (y) => y + " connect")
    // 打印数据 -> (Sink)
    streamCoMap.print()
    // 触发程序执行
    env.execute("CoMapFlow")
  }
}
```
> **2. CoFlatMap**
```
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * TransformationFlow
  * <p>
  */

object TransformationFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用CoFlatMapFlow方法
  CoFlatMapFlow()

  /**
    * 定义CoFlatMapFlow方法
    * ConnectedStreams → DataStream
    */
  def CoFlatMapFlow(): Unit = {
    // 加载初始数据 -> (Source)
    val filePaths = "../flink_server/flink-coreflow/src/main/resources/input_01/test03.txt"
    val stream01 = env.readTextFile(filePaths)
    val stream02 = env.readTextFile(filePaths)
    // stream01将与stream02连接并形成ConnectedStreams连接流
    var streamConnect = stream01.connect(stream02)
    // 当streamConnect调用flatMap函数的过程就称之为CoFlatMap操作
    val streamCoFlatMap = streamConnect.flatMap((x) => x.split(" "), (y) => y.split(" "))
    // 打印数据 -> (Sink)
    streamCoFlatMap.print()
    // 触发程序执行
    env.execute("CoFlatMapFlow")
  }
}
```

#### 5.6.6 Split
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_020.jpg)
> 
> DataStream → SplitStream : 根据某些特征将DataStream拆分成两个或者多个DataStream.
> 
> 通常split()函数会与select()函数配合使用.
> 
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * TransformationFlow
  * <p>
  */

object TransformationFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用SplitFlow方法
  SplitFlow()

  /**
    * 定义SplitFlow方法
    * DataStream → SplitStream
    * 通常split()函数会与select()函数配合使用
    */
  def SplitFlow(): Unit = {
    // 加载初始数据 -> (Source)
    val filePaths = "../flink_server/flink-coreflow/src/main/resources/input_01/test03.txt"
    val stream = env.readTextFile(filePaths).flatMap(x => x.split(" "))
    // 调用split函数
    var streamSplit = stream.split(
      // 遍历每行数据,并校验values值与hadoop值相等,则表示条件成立
      values => ("hadoop".equals(values))
        // 将values值进行match模式匹配
      match {
        // 如果values条件为true,则将hadoop追加List集合中
        case true => List("hadoop")
        // 如果values条件为false,则将other追加List集合中
        case false => List("other")
      }
    )
    // 打印数据 -> (Sink)
    streamSplit.print()
    // 触发程序执行
    env.execute("SplitFlow")
  }
}
```

#### 5.6.7 Select
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_021.jpg)
> 
> SplitStream → DataStream : 从一个SplitStream中获取一个或者多个DataStream.
> 
> 通常select()函数会与split()函数配合使用.
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * TransformationFlow
  * <p>
  */

object TransformationFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用SplitAndSelectFlow方法
  SplitAndSelectFlow()

  /**
    * 定义SplitAndSelectFlow方法
    * SplitStream → DataStream
    * 通常select()函数会与split()函数配合使用
    */
  def SplitAndSelectFlow(): Unit = {
    // 加载初始数据 -> (Source)
    val filePaths = "../flink_server/flink-coreflow/src/main/resources/input_01/test03.txt"
    val stream = env.readTextFile(filePaths).flatMap(x => x.split(" "))
    // 调用split函数
    var streamSplit = stream.split(
      // 遍历每行数据,并校验values值与hadoop值相等,则表示条件成立
      values => ("hadoop".equals(values))
        // 将values值进行match模式匹配
      match {
        // 如果values条件为true,则将hadoop追加List集合中
        case true => List("hadoop")
        // 如果values条件为false,则将other追加List集合中
        case false => List("other")
      }
    )
    // 调用select函数
    val streamSelectHadoop = streamSplit.select("hadoop")
    val streamSelectOther = streamSplit.select("other")
    // 打印数据 -> (Sink)
    streamSelectHadoop.print()
    streamSelectOther.print()
    // 触发程序执行
    env.execute("SplitAndSelectFlow")
  }
}
```

#### 5.6.8 Union
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_022.jpg)
> 
> DataStream → DataStream : 对两个或者两个以上DataStream进行union操作.产生一个包含所有DataStream元素的新DataStream.
> 
> 注意:如果将一个DataStream跟它自身做union操作,在新的DataStream中,将看到每一个元素都出现两次.
> 
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * TransformationFlow
  * <p>
  */

object TransformationFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用UnionFlow方法
  UnionFlow()

  /**
    * 定义UnionFlow方法
    * DataStream → DataStream
    */
  def UnionFlow(): Unit = {
    // 加载初始数据 -> (Source)
    val filePath01 = "../flink_server/flink-coreflow/src/main/resources/input_01/test01.txt"
    val filePath02 = "../flink_server/flink-coreflow/src/main/resources/input_01/test03.txt"
    val stream01 = env.readTextFile(filePath01).flatMap(x => x.split(" "))
    val stream02 = env.readTextFile(filePath02).flatMap(x => x.split(" "))
    // 调用union函数
    val streamUnion = stream01.union(stream02)
    // 打印数据 -> (Sink)
    streamUnion.print()
    // 触发程序执行
    env.execute("UnionFlow")
  }
}
```

#### 5.6.9 KeyBy
> DataStream → KeyedStream : 输入必须是Tuple(元祖)类型,逻辑的将一个流拆分成不相交的分区,每个分区包含具有相同key的元素,在内部以hash形式实现.
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * TransformationFlow
  * <p>
  */

object TransformationFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用KeyByFlow方法
  KeyByFlow()

  /**
    * 定义KeyByFlow方法
    * DataStream → KeyedStream
    */
  def KeyByFlow(): Unit = {
    // 加载初始数据 -> (Source)
    val filePath = "../flink_server/flink-coreflow/src/main/resources/input_01/test03.txt"
    val stream = env.readTextFile(filePath).flatMap(x => x.split(" ")).map(x => (x, 1L))
    // 调用keyBy函数
    val streamkeyBy = stream.keyBy(0)
    // 打印数据 -> (Sink)
    streamkeyBy.print()
    // 触发程序执行
    env.execute("KeyByFlow")
  }
}
```

#### 5.6.10 Reduce
> KeyedStream → DataStream : 一个分组数据流的聚合操作,合并当前的元素和上次聚合的结果,产生一个新的值,返回的流中包含每一次聚合的结果,而不是只返回最后一次聚合的最终结果.
> 
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * WindowsFlow
  * <p>
  */

object TransformationFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用ReduceFlow方法
  ReduceFlow()

  /**
    * 定义ReduceFlow方法
    * KeyedStream → DataStream
    */
  def ReduceFlow(): Unit = {
    // 加载初始数据 -> (Source)
    val filePath = "../flink_server/flink-coreflow/src/main/resources/input_01/test03.txt"
    val stream = env.readTextFile(filePath).flatMap(x => x.split(" ")).map(x => (x, 1L))
    // 调用keyBy函数
    val streamkeyBy = stream.keyBy(0)
    // 调用reduce函数
    val streamReduce = streamkeyBy.reduce((item1, item2) => (item1._1, item1._2 + item2._2))
    // 打印数据 -> (Sink)
    streamReduce.print()
    // 触发程序执行
    env.execute("ReduceFlow")
  }
}
```


#### 5.6.11 Fold
> KeyedStream → DataStream : 一个有初始值的分组数据流的滚动折叠操作,合并当前元素和前一次折叠操作的结果,并产生一个新的值,返回的流中包含每一次折叠的结果,而不是只返回最后一次折叠的最终结果.

``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * WindowsFlow
  * <p>
  */

object TransformationFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用FoldFlow方法
  FoldFlow()

  /**
    * 定义FoldFlow方法
    * KeyedStream → DataStream
    */
  def FoldFlow(): Unit = {
    // 加载初始数据 -> (Source)
    val filePath = "../flink_server/flink-coreflow/src/main/resources/input_01/test03.txt"
    // 依次调用flatMap函数 -> map函数 -> keyBy函数
    val streamkeyBy = env.readTextFile(filePath).flatMap(x => x.split(" ")).map(x => (x, 1)).keyBy(0)
    // 调用fold函数
    val streamReduceFold = streamkeyBy.fold(100)((x, y) => (x + y._2))
    // 打印数据 -> (Sink)
    streamReduceFold.print()
    // 触发程序执行
    env.execute("FoldFlow")
  }
}
```

#### 5.6.12 Aggregations
> KeyedStream → DataStream : 分组数据流上的滚动聚合操作.
> 
> min和minBy的区别是min返回的是一个最小值,而minBy返回的是其字段中包含最小值的元素(同样原理适用于max和maxBy),返回的流中包含每一次聚合的结果,而不是只返回最后一次聚合的最终结果.
> ```
> keyedStream.sum(0)
> keyedStream.sum("key")
> keyedStream.min(0)
> keyedStream.min("key")
> keyedStream.max(0)
> keyedStream.max("key")
> keyedStream.minBy(0)
> keyedStream.minBy("key")
> keyedStream.maxBy(0)
> keyedStream.maxBy("key")
> ```
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * WindowsFlow
  * <p>
  */

object TransformationFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment
  
  // 调用AggregationsFlow方法
  AggregationsFlow()
  
  /**
    * 定义AggregationsFlow方法
    * KeyedStream → DataStream
    */
  def AggregationsFlow(): Unit = {
    // 加载初始数据 -> (Source)
    val filePath = "../flink_server/flink-coreflow/src/main/resources/input_01/test02.txt"
    // 依次调用map函数 ->  keyBy函数
    val streamkeyBy = env.readTextFile(filePath).map(item => (item.split(" ")(0), item.split(" ")(1).toLong)).keyBy(0)
    // 调用sum函数
    val streamReduceAggregations = streamkeyBy.sum(1)
    // 打印数据 -> (Sink)
    streamReduceAggregations.print()
    // 触发程序执行
    env.execute("AggregationsFlow")
  }
}
```

> 在5.6.10 Reduce之前的算子,都是可以直接作用在Stream上,因为它们不是聚合类型操作,但是5.6.10 Reduc之后你会发现,虽然可以对一个无边界的流数据直接应用聚合算子,但是它会记录下每一次的聚合结果,这每一次的聚合结果往往不是我们想要.
> 
> 其实reduce、fold、aggregation这些聚合算子都是需要与Window配合使用,只有配合Window使用,才能得到想要的结果.

## 🔥 6. Time & Window 🔥
### 6.1 Time
> 在Flink流式处理中,会涉及到时间的不同概念,如下Flink时间概念图所示 : 
> 
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_023.jpg)
> 
> **1. `Event Time`** : 是事件创建的时间,它通常由事件中的时间戳描述,例如采集的日志数据中,每一条日志都会记录自己的生成时间,Flink通过时间戳分配器访问事件时间戳.
> 
> **2. `Ingestion Time`** : 是数据进入Flink的时间.
> 
> **3. `Processing Time`** : 是每一个执行基于时间操作的算子的本地系统时间,与机器相关,默认的时间属性就是ProcessingTime.
> 
> 例如,一条日志进入Flink的时间为(2017-11-12 10:00:00.123) -> 即表示 Ingestion Time
> 
> 到达Window的系统时间为(2017-11-12 10:00:01.234) -> 即表示 Processing Time
> 
> 日志内容如下 : `2017-11-02 18:37:15.624 INFO Fail over to rm2` -> 即表示 Event Time
> 
> 对于业务来说,要统计1min内故障日志个数,哪个时间是最有意义？—— eventTime,因为要根据日志的生成时间进行统计.


### 6.2 Window
#### 6.2.1 Window 概述
> streaming流式计算是一种被设计用于处理无限数据集的数据处理引擎.
> 而无限数据集是指一种不断增长,本质上无限的数据集.
> 而window是一种切割无限数据为有限块,进行处理的手段.
> 
> Window是无限数据流处理的核心,Window将一个无限stream拆分成有限大小的buckets桶,开发者可以在这些桶上做计算操作.


#### 6.2.2 Window 类型
> Window可以分成两类 : 
> 
> CountWindow : 按照指定的数据条数生成一个Window,与时间无关.
> 
> TimeWindow : 按照时间生成Window.
> 
> 对于TimeWindow和CountWindow,可以根据窗口实现原理的不同分成三类 : 
> 滚动窗口(Tumbling Window)、滑动窗口(Sliding Window)和会话窗口(Session Window)
> 
> **1.滚动窗口 (Tumbling Windows)**
> 
> 将数据依据固定的窗口长度对数据进行切片.
> 
> 特点 : 时间对齐,窗口长度固定,没有重叠.
> 
> 滚动窗口分配器将每个元素分配到一个指定窗口大小的窗口中,滚动窗口有一个固定的大小,并且不会出现重叠.
> 
> 例如 : 如果指定一个5分钟大小的滚动窗口,窗口创建如下滚动窗口图所示 : 
> 适用场景 : 适合做BI统计等 (做每个时间段的聚合计算)
> 
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_024.jpg)
> 
> **2.滑动窗口 (Sliding Windows)**
> 滑动窗口是固定窗口的更广义的一种形式,滑动窗口由固定的窗口长度和滑动间隔组成.
> 
> 特点 : 时间对齐,窗口长度固定,有重叠.
> 
> 滑动窗口分配器将元素分配到固定长度的窗口中与滚动窗口类似,窗口的大小由窗口大小参数来配置,另一个窗口滑动参数控制滑动窗口开始的频率.
> 
> 因此滑动窗口如果滑动参数小于窗口大小的话,窗口是可以重叠的,在这种情况下元素会被分配到多个窗口中.
> 
> 例如 : 有10分钟的窗口和5分钟的滑动,那么每个窗口中5分钟的窗口里包含着上个10分钟产生的数据,如下滑动窗口图所示 : 
> 适用场景 : 对最近一个时间段内的统计(求某接口最近5min的失败率来决定是否要报警)
> 
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_025.jpg)

> **3.会话窗口 (Session Windows)**
> 
> 由一系列事件组合一个指定时间长度的timeout间隙组成,类似于web应用的session,也就是一段时间没有接收到新数据就会生成新的窗口.
> 
> 特点 : 时间无对齐.
> 
> session窗口分配器通过session活动来对元素进行分组,session窗口跟滚动窗口和滑动窗口相比,不会有重叠和固定的开始时间和结束时间的情况.
> 
> 相反,当它在一个固定的时间周期内不再收到元素,即非活动间隔产生,那个这个窗口就会关闭,一个session窗口通过一个session间隔来配置,这个session间隔定义了非活跃周期的长度,当这个非活跃周期产生,那么当前的session将关闭并且后续的元素将被分配到新的session窗口中去.
> 
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_026.jpg)


### 6.3 Window API
#### 6.3.1 Count Window
> CountWindow根据窗口中相同key元素的数量来触发执行,执行时只计算元素数量达到窗口大小的key对应的结果.
> 
> 注意 : CountWindow的window_size指的是相同Key的元素的个数,不是输入的所有元素的总数.
> 
> **1. 滚动窗口**
> 默认CountWindow是一个滚动窗口,只需要指定窗口大小即可,当元素key值数量达到窗口大小时,就会触发窗口的执行.
- 1.创建countWindowFlow方法
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * WindowsFlow
  * <p>
  */

object WindowsFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用countWindowFlow方法
  countWindowFlow()

  /**
    * 定义countWindowFlow方法
    */
  def countWindowFlow(): Unit = {
    // 监听端口并加载初始数据 -> (Source)
    val stream = env.socketTextStream("systemhub", 9999)
    // 对stream进行处理并按key聚合
    val streamKeyBy = stream.map(x => (x, 1L)).keyBy(0)
    /**
      * 引入滚动窗口
      * 参数5即表示5个相同key的元素计算一次
      * 注意 : CountWindow的window_size指的是相同Key的元素的个数,不是输入的所有元素的总数.
      */
    val streamWindow = streamKeyBy.countWindow(5)
    // 将聚合数据写入文件
    val streamReduce = streamWindow.reduce((x, y) => (x._1, x._2 + y._2))
    // 打印数据 -> (Sink)
    streamReduce.print()
    // 触发程序执行
    env.execute("countWindowFlow")
  }
}
```
- 2.在本地监听服务端口
```
systemhub:~ system$ nc -l 9999
```
- 3.运行程序
- 4.在本地服务端输入数据源
```
systemhub:~ system$ nc -l 9999
streamWindow
streamWindow
streamWindow
streamWindow
streamWindow
streamKeyBy
streamKeyBy
streamKeyBy
streamKeyBy
streamKeyBy
```
- 5.查看运行结果
```
1> (streamWindow,5)
5> (streamKeyBy,5)
```


> **2. 滑动窗口**
> 滑动窗口和滚动窗口的函数名是完全一致的,只是在传参数时需要传入两个参数,一个是`window_size`,一个是`sliding_size`.
> 
> 下面实例中sliding_size设置为2,也就是说每收到两个相同key的数据就计算一次,每一次计算的window范围是5个元素.
- 1.创建countWindowsFlow方法
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * WindowsFlow
  * <p>
  */

object WindowsFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用countWindowsFlow方法
  countWindowsFlow()

  /**
    * 定义countWindowsFlow方法
    */
  def countWindowsFlow(): Unit = {
    // 监听端口并加载初始数据 -> (Source)
    val stream = env.socketTextStream("systemhub", 9999)
    // 对stream进行处理并按key聚合
    val streamKeyBy = stream.map(x => (x, 1L)).keyBy(0)

    /**
      * 引入滑动窗口
      * 每收到两个相同key的数据就计算一次,每一次计算的window范围是5个元素
      */
    val streamWindow = streamKeyBy.countWindow(5, 2)
    // 将聚合数据写入文件
    val streamReduce = streamWindow.reduce((x, y) => (x._1, x._2 + y._2))
    // 打印数据 -> (Sink)
    streamReduce.print()
    // 触发程序执行
    env.execute("countWindowsFlow")
  }
}
```
- 2.在本地监听服务端口
```
systemhub:~ system$ nc -l 9999
```
- 3.运行程序
- 4.在本地服务端输入数据源
```
systemhub:~ system$ nc -l 9999
streamWindow
streamWindow
streamKeyBy
streamKeyBy
streamWindow
streamWindow
streamWindow
streamWindow
```
- 5.查看运行结果
```
1> (streamWindow,2)
5> (streamKeyBy,2)
1> (streamWindow,4)
1> (streamWindow,5)
```

#### 6.3.2 Time Window
> TimeWindow是将指定时间范围内的所有数据组成一个window,一次对一个window内的所有数据进行计算.
> 
> 时间间隔可以通过`Time.milliseconds(x)`,`Time.seconds(x)`,`Time.minutes(x)`等其中一个来指定.
> 
> **1. 滚动窗口**
> 
> Flink默认时间窗口根据ProcessingTime进行窗口的划分,将Flink获取到的数据根据进入Flink的时间划分到不同的窗口中.
- 1.创建TimeWindowFlow方法
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.api.windowing.time.Time

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * WindowsFlow
  * <p>
  */

object WindowsFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用TimeWindowFlow方法
  TimeWindowFlow()

  /**
    * 定义TimeWindowFlow方法
    */
  def TimeWindowFlow(): Unit = {
    // 监听端口并加载初始数据 -> (Source)
    val stream = env.socketTextStream("systemhub", 9999)
    // 对stream进行处理并按key聚合
    val streamKeyBy = stream.map(x => (x, 1L)).keyBy(0)
    /**
      * 引入滚动时间窗口
      * 时间间隔,可以通过`Time.milliseconds(x)`,`Time.seconds(x)`,`Time.minutes(x)`等其中一个来指定.
      */
    val streamTimeWindow = streamKeyBy.timeWindow(Time.seconds(5))
    // 将聚合数据写入文件
    val streamReduce = streamTimeWindow.reduce((x, y) => (x._1, x._2 + y._2))
    // 打印数据 -> (Sink)
    streamReduce.print()
    // 触发程序执行
    env.execute("TimeWindowFlow")
  }
}
```
- 2.在本地监听服务端口
```
systemhub:~ system$ nc -l 9999
```
- 3.运行程序
- 4.在本地服务端输入数据源
```
systemhub:~ system$ nc -l 9999
TimeWindowFlow
TimeWindowFlow
TimeWindowFlow
TimeWindowFlow
TimeWindowFlow
TimeWindowFlowTimeWindowFlow^[[B
TimeWindowFlow^[[A
TimeWindowFlow
TimeWindowFlow
systemhub:~ system$
```
- 5.查看运行结果
```
8> (TimeWindowFlow,3)
8> (TimeWindowFlow,2)
8> (TimeWindowFlowTimeWindowFlow,1)
4> (TimeWindowFlow,1)
8> (TimeWindowFlow,2)
```

> **2. 滑动窗口 (SlidingEventTimeWindows)**
> 
> 滑动窗口和滚动窗口的函数名是完全一致,只是在传参数时需要传入两个参数,一个是`window_size`,一个是`sliding_size`.
> 
> 下面实例中sliding_size设置为了2s,也就是说窗口每2s就计算一次，每一次计算的window范围是5s内的所有元素.
- 1.创建SlidingEventTimeWindowsFlow方法
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.api.windowing.time.Time

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * WindowsFlow
  * <p>
  */

object WindowsFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用SlidingEventTimeWindowsFlow方法
  SlidingEventTimeWindowsFlow()

  /**
    * 定义SlidingEventTimeWindowsFlow方法
    */
  def SlidingEventTimeWindowsFlow(): Unit = {
    // 监听端口并加载初始数据 -> (Source)
    val stream = env.socketTextStream("systemhub", 9999)
    // 对stream进行处理并按key聚合
    val streamKeyBy = stream.map(x => (x, 1L)).keyBy(0)
    /**
      * 引入滑动时间窗口
      * 窗口每2s就计算一次,每一次计算的window范围是10s内的所有元素.
      * 时间间隔,可以通过`Time.milliseconds(x)`,`Time.seconds(x)`,`Time.minutes(x)`等其中一个来指定.
      */
    val streamWindows = streamKeyBy.timeWindow(Time.seconds(10), Time.seconds(2))
    // 将聚合数据写入文件
    val streamReduce = streamWindows.reduce((x, y) => (x._1, x._2 + y._2))
    // 打印数据 -> (Sink)
    streamReduce.print()
    // 触发程序执行
    env.execute("SlidingEventTimeWindowsFlow")
  }
}
```
- 2.在本地监听服务端口
```
systemhub:~ system$ nc -l 9999
```
- 3.运行程序
- 4.在本地服务端输入数据源
```
systemhub:~ system$ nc -l 9999
SlidingEventTimeWindowsFlow
SlidingEventTimeWindowsFlow
SlidingEventTimeWindowsFlow
SlidingEventTimeWindowsFlow
systemhub:~ system$ 
```
- 5.查看运行结果
```
7> (SlidingEventTimeWindowsFlow,3)
7> (SlidingEventTimeWindowsFlow,3)
7> (SlidingEventTimeWindowsFlow,3)
7> (SlidingEventTimeWindowsFlow,3)
7> (SlidingEventTimeWindowsFlow,3)
7> (SlidingEventTimeWindowsFlow,1)
7> (SlidingEventTimeWindowsFlow,1)
7> (SlidingEventTimeWindowsFlow,1)
7> (SlidingEventTimeWindowsFlow,1)
7> (SlidingEventTimeWindowsFlow,1)
```

#### 6.3.3 Window Reduce
> WindowedStream → DataStream : 给window赋一个reduce功能的函数,并返回一个聚合的结果.
> 
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.api.windowing.time.Time

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * WindowsFlow
  * <p>
  */

object WindowsFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用WindowReduceFlow方法
  WindowReduceFlow()

  /**
    * 定义WindowReduceFlow方法
    */
  def WindowReduceFlow(): Unit = {
    // 监听端口并加载初始数据 -> (Source)
    val stream = env.socketTextStream("systemhub", 9999)
    // 对stream进行处理并按key聚合
    val streamKeyBy = stream.map(x => (x, 1L)).keyBy(0)
    /**
      * 引入滑动时间窗口
      * 窗口每2s就计算一次,每一次计算的window范围是10s内的所有元素.
      * 时间间隔,可以通过`Time.milliseconds(x)`,`Time.seconds(x)`,`Time.minutes(x)`等其中一个来指定.
      */
    val streamWindows = streamKeyBy.timeWindow(Time.seconds(10), Time.seconds(2))
    // 将聚合数据写入文件
    val streamReduce = streamWindows.reduce((x, y) => (x._1, x._2 + y._2))
    // 打印数据 -> (Sink)
    streamReduce.print()
    // 触发程序执行
    env.execute("WindowReduceFlow")
  }
}
```

#### 6.3.4 Window Fold
> WindowedStream → DataStream : 给窗口赋一个fold功能的函数,并返回一个fold后的结果.
- 1.创建WindowFoldFlow方法
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.api.windowing.time.Time

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * WindowsFlow
  * <p>
  */

object WindowsFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用WindowFoldFlow方法
  WindowFoldFlow()

  /**
    * 定义WindowFoldFlow方法
    */
  def WindowFoldFlow(): Unit = {
    // 监听端口并加载初始数据 -> (Source)
    val stream = env.socketTextStream("systemhub", 9999, '\n', 3)
    // 对stream进行处理并按key聚合
    val streamKeyBy = stream.map(x => (x, 1)).keyBy(0)
    /**
      * 引入滚动时间窗口
      * 时间间隔,可以通过`Time.milliseconds(x)`,`Time.seconds(x)`,`Time.minutes(x)`等其中一个来指定.
      */
    val streamTimeWindow = streamKeyBy.timeWindow(Time.seconds(5))
    // 调用fold函数操作
    val streamFold = streamTimeWindow.fold(100) {
      (x, y) => x + y._2
    }
    // 打印数据 -> (Sink)
    streamFold.print()
    // 触发程序执行
    env.execute("WindowFoldFlow")
  }
}
```
- 2.在本地监听服务端口
```
systemhub:~ system$ nc -l 9999
```
- 3.运行程序
- 4.在本地服务端输入数据源
```
systemhub:~ system$ nc -l 9999
WindowFoldFlow
WindowFoldFlow
WindowFoldFlow
WindowFoldFlow
WindowFoldFlow
WindowFoldFlow
WindowFoldFlow
WindowFoldFlow
WindowFoldFlow
WindowFoldFlow
systemhub:~ system$
```
- 5.查看运行结果
```
4> 103
4> 103
4> 101
4> 101
4> 102
```

#### 6.3.5 Aggregation on Window
> WindowedStream → DataStream : 对一个window内的所有元素做聚合操作.
> 
> min和minBy的区别是min返回的是最小值,而minBy返回的是包含最小值字段的元素(同样的原理适用于max和maxBy).
- 1.创建aggregationOnWindowFlow方法
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.api.windowing.time.Time

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * WindowsFlow
  * <p>
  */

object WindowsFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用aggregationOnWindowFlow方法
  aggregationOnWindowFlow()

  /**
    * 定义aggregationOnWindowFlow方法
    */
  def aggregationOnWindowFlow(): Unit = {
    // 监听端口并加载初始数据 -> (Source)
    val stream = env.socketTextStream("systemhub", 9999)
    // 对stream进行处理并按key聚合
    val streamKeyBy = stream.map(item => (item.split(" ")(0), item.split(" ")(1))).keyBy(0)
    // 引入滚动窗口
    val streamWindow = streamKeyBy.timeWindow(Time.seconds(5))
    // 执行聚合操作
    val streamMax = streamWindow.max(1)
    // 打印数据 -> (Sink)
    streamMax.print()
    // 触发程序执行
    env.execute("aggregationOnWindowFlow")
  }
}
```


## 🔥 7. EventTime & Window 🔥
### 7.1 EventTime 引入
> 在Flink流式处理中,绝大部分的业务都会使用eventTime,一般只在eventTime无法使用时,才会被迫使用ProcessingTime或者IngestionTime.
> 
> 如果要使用EventTime,那么需要引入EventTime时间属性,引入方式如下所示 : 
> ```
> val env = StreamExecutionEnvironment.getExecutionEnvironment
> 
> // 从调用时刻开始给env创建的每一个stream追加时间特征
> env.setStreamTimeCharacteristic(TimeCharacteristic.EventTime)
> ```

### 7.2 Watermark
#### 7.2.1 基本概念
> 流处理从事件产生到流经过source,再到operator,中间是有一个过程和时间.
> 
> 虽然大部分情况下,流到operator的数据都是按照事件产生的时间顺序来排列,但是也不排除由于网络、背压等原因,导致数据乱序的产生.
> 
> 所谓数据乱序就是指Flink接收到事件的先后顺序不是严格按照事件EventTime顺序排列的.
> 
> 数据乱序图如下 : 
> 
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_027.jpg)
> 
> 那么此时出现一个问题,一旦出现乱序,如果只根据eventTime决定window的运行,是不能明确数据是否全部到位,但又不能无限期的等待,此时必须要有个机制来保证一个特定时间后必须触发window进行计算,这个特别的机制就是Watermark.
> 
> Watermark是一种衡量EventTime进展机制,它是数据自身的隐藏属性,数据自身携带着对应的Watermark.
> 
> Watermark是用于处理乱序事件,而正确处理乱序事件,通常用Watermark机制结合window来实现.
> 
> 数据流中的Watermark用于表示EventTime小于Watermark的数据都已经到达,因此window的执行也是由Watermark来触发.
> 
> Watermark可以理解成一个延迟触发机制,可以设置Watermark的延时时长.
> 
> 每次系统会校验已经到达的数据中最大的maxEventTime,然后认定eventTime小于maxEventTime减去延时时长的所有数据都已经到达.
> 
> 如果有窗口停止时间等于maxEventTime减去延时时长,那么这个窗口就会被触发执行.
> 
> 有序流Watermarker 如下图所示 : (Watermark设置为0)
> 
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_028.jpg)
> 
> 无序数据 处理流程原理 : 
> 
> `已知条件` : 设置允许最大延时时长为2s , 以5秒为时间单位划分窗口,每个隔5秒就会划分一个窗口.
> 
> 在一条数据流中,将以1到5,5到10,10到15进行划分窗口,当窗口划分之后,在触发窗口执行之前,将会不断的接收外来数据进入窗口,当1进入时,将1存放至窗口1,当4进入时,4会先判断自身Watermark是多少,`计算公式:maxEventTime - 延时时长 = 自身Watermark`,既是`4-2=2`,计算完毕后得知4自身Watermark是2,此时4会判断当前窗口结束时间有没有小于等于2的值,此时发现并没有,则5进入窗口,此时5的自身Watermark就是3,5此时再次比较当前窗口结束时间有没有小于等于3的值,如没有则2进入,直到7进入窗口时,发现当前窗口结束时间小于等于5的条件成立,此时证明窗口1的数据已经全部到位,可以进行窗口执行,那么所剩下还没有进入到窗口的数据,则全部被抛弃,其他窗口流程如上述所示,这就是无序数据 处理流程原理.
> 
> 当Flink接收到每一条数据时,都会产生一条Watermark,当maxEventTime减去延时时长即表示这条Watermark就等于当前所有到达数据中的时间.
> 
> 也就是说Watermark是由数据自身携带,一旦数据携带的Watermark比当前未触发的窗口停止时间要晚,那么就会被触发相应窗口执行.
> 
> 由于Watermark是由数据携带,因此如果运行过程中无法获取新的数据,那么没有被触发的窗口将永远都不被触发.
> 
> 上图中所设置的允许最大延迟到达时间为2s.
> 
> 所以,时间戳为7s的事件既对应的Watermark时间是5s.
> ``` 
> 计算公式模型 : maxEventTime - 延时时长 = Watermark
> 套用计算模型 : 7s - 2s = 5s
> ```
> 时间戳为12s的事件既对应的Watermark时间是10s.
> ``` 
> 计算公式模型 : maxEventTime - 延时时长 = Watermark
> 套用计算模型 : 12s - 2s = 10s
> ```
> 如图所示 : 图中以5秒为时间单位划分窗口,每个隔5秒就会划分一个窗口.
> 
> 窗口1即表示是1s ~ 5s , 窗口2即表示是6s ~ 10s , 窗口3,窗口4,划分窗口以此类推
> 
> 那么时间戳为7s的事件到达时的Watermarker恰好触发窗口1.
> ``` 
> 计算公式模型 : maxEventTime - 延时时长 = Watermark
> 套用计算模型 : 7s - 2s = 5s
> 
> 判断公式模型 : Watermark = 窗口1 && Watermark = 窗口2
> 套用判断模型 : 5s = (窗口1 - 1s~5s) && 5s != (窗口2 - 6s~10s)
> ```
> 时间戳为12s的事件到达时的Watermark恰好触发窗口2.
> ``` 
> 计算公式模型 : maxEventTime - 延时时长 = Watermark
> 套用计算模型 : 12s - 2s = 10s
> 
> 判断公式模型 : Watermark = 窗口1 && Watermark = 窗口2
> 套用判断模型 : 10s != (窗口1 - 1s~5s) && 10s = (窗口2 - 6s~10s)
> ```

#### 7.2.2 Watermark 引入
``` scala
package com.geekparkhub.core.flink.workflow


import org.apache.flink.streaming.api.TimeCharacteristic
import org.apache.flink.streaming.api.functions.timestamps.BoundedOutOfOrdernessTimestampExtractor
import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.api.windowing.time.Time

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * EvnetTimeWindowFlow
  * <p>
  */
object EvnetTimeWindowFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用watermarkFlow方法
  watermarkFlow()
  
  /**
    * 定义watermarkFlow方法
    * 分配时间戳与Watermarks
    */
  def watermarkFlow(): Unit = {
    // 设置时间特征为EventTime,即表示从调用时开始赋予env创建的每个stream追加时间特征
    env.setStreamTimeCharacteristic(TimeCharacteristic.EventTime)
    // 设置时间戳
    val stream = env.socketTextStream("systemhub", 9999)
      .assignTimestampsAndWatermarks(new BoundedOutOfOrdernessTimestampExtractor[String](Time.milliseconds(0)) {
        override def extractTimestamp(time: String): Long = {
          // / EventTime是日志生成时间,从日志中解析EventTime
          val eventTime = time.split(" ")(0).toLong
          println("eventTime = " + eventTime)
          eventTime
        }
      })
  }
}
```
### 7.3 EvnetTimeWindow API
> 当使用EventTimeWindow时,所有的Window在EventTime的时间轴上进行划分,也就是说,在Window启动后,会根据初始的EventTime时间每隔一段时间划分一个窗口,如果Window大小是3秒,那么1分钟内会把Window划分为如下的形式 : 
> ```
> [00:00:00,00:00:03)
> [00:00:03,00:00:06)
> ...
> [00:00:57,00:01:00)
> ```
> 
> 如果Window大小是10秒,则Window会被分为如下形式 : 
> ```
> [00:00:00,00:00:10)
> [00:00:10,00:00:20)
> ...
> [00:00:50,00:01:00)
> ```
> 
> 注意,窗口是左闭右开,形式为 : 
> 
> `[window_start_time,window_end_time)`
> 
> Window的设定无关数据本身,而是系统实现定义好的,也就是说Window会一直按照指定的时间间隔进行划分,不论这个Window中有没有数据,EventTime在这个Window期间的数据会进入这个Window.
> 
> Window会不断产生,属于这个Window范围的数据会被不断加入到Window中,所有未被触发的Window都会等待触发,只要Window还没触发,属于这个Window范围的数据就会一直被加入到Window中,直到Window被触发才会停止数据的追加,而当Window触发之后才接受到的属于被触发Window的数据会被丢弃.
> 
> - Window会在以下的条件满足时被触发执行 : 
> - watermark时间 >= window_end_time
> - 在[window_start_time,window_end_time)中有数据存在
> 
> 通过下图来说明Watermark、EventTime和Window的关系
> 
> ![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flink/start_029.jpg)


#### 7.3.1 滚动窗口 (TumblingEventTimeWindows)
> 按照EventTime的时间窗口计算出结果,而无关系统的时间(包括输入的快慢)
- 1.创建TumblingEventTimeWindowsFlow方法
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.TimeCharacteristic
import org.apache.flink.streaming.api.functions.timestamps.BoundedOutOfOrdernessTimestampExtractor
import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.api.windowing.assigners.TumblingEventTimeWindows
import org.apache.flink.streaming.api.windowing.time.Time

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * EvnetTimeWindowFlow
  * <p>
  */
object EvnetTimeWindowFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用TumblingEventTimeWindowsFlow方法
  TumblingEventTimeWindowsFlow()

  /**
    * 定义TumblingEventTimeWindowsFlow方法
    * 定义 滚动窗口 方法
    */
  def TumblingEventTimeWindowsFlow(): Unit = {
    // 设置时间特征为EventTime,即表示从调用时开始赋予env创建的每个stream追加时间特征
    env.setStreamTimeCharacteristic(TimeCharacteristic.EventTime)
    // 设置时间戳,对stream进行处理并按key聚合
    val stream = env.socketTextStream("systemhub", 9999)
      .assignTimestampsAndWatermarks(new BoundedOutOfOrdernessTimestampExtractor[String](Time.milliseconds(3000)) {
        override def extractTimestamp(time: String): Long = {
          // / EventTime是日志生成时间,从日志中解析EventTime
          val eventTime = time.split(" ")(0).toLong
          println("eventTime = " + eventTime)
          eventTime
        }
      }).map(x => (x.split(" ")(1), (1L))).keyBy(0)
    // 引入滚动窗口,设置每5秒开启一个窗口
    val streamWindow = stream.window(TumblingEventTimeWindows.of(Time.seconds(5)))
    // 执行聚合操作
    val streamReduce = streamWindow.reduce((x, y) => (x._1, x._2 + y._2))
    // 打印数据 -> (Sink)
    streamReduce.print()
    // 触发程序执行
    env.execute("TumblingEventTimeWindowsFlow")
  }
}
```
- 2.在本地监听服务端口
```
systemhub:~ system$ nc -l 9999
```
- 3.运行程序
- 4.在本地服务端输入数据源
```
systemhub:~ system$ nc -l 9999
10000 TumblingEventTimeWindowsFlow
11000 TumblingEventTimeWindowsFlow
15000 TumblingEventTimeWindowsFlow
18000 TumblingEventTimeWindowsFlow
23000 TumblingEventTimeWindowsFlow
27999 TumblingEventTimeWindowsFlow
```
- 5.查看运行结果
```
eventTime = 10000
eventTime = 11000
eventTime = 15000
eventTime = 18000
2> (TumblingEventTimeWindowsFlow,2)
eventTime = 23000
2> (TumblingEventTimeWindowsFlow,2)
eventTime = 27999
2> (TumblingEventTimeWindowsFlow,1)
```

#### 7.3.2 滑动窗口 (SlidingEventTimeWindows)
- 1.创建SlidingEventTimeWindowsFlow方法
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.TimeCharacteristic
import org.apache.flink.streaming.api.functions.timestamps.BoundedOutOfOrdernessTimestampExtractor
import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.api.windowing.assigners.{SlidingEventTimeWindows, TumblingEventTimeWindows}
import org.apache.flink.streaming.api.windowing.time.Time

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * EvnetTimeWindowFlow
  * <p>
  */
object EvnetTimeWindowFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用SlidingEventTimeWindowsFlow方法
    SlidingEventTimeWindowsFlow()

  /**
    * 定义SlidingEventTimeWindowsFlow方法
    * 定义 滑动窗口 方法
    */
  def SlidingEventTimeWindowsFlow(): Unit = {
    // 设置时间特征为EventTime,即表示从调用时开始赋予env创建的每个stream追加时间特征
    env.setStreamTimeCharacteristic(TimeCharacteristic.EventTime)
    // 设置时间戳,对stream进行处理并按key聚合
    val stream = env.socketTextStream("systemhub", 9999)
      .assignTimestampsAndWatermarks(new BoundedOutOfOrdernessTimestampExtractor[String](Time.milliseconds(3000)) {
        override def extractTimestamp(time: String): Long = {
          // / EventTime是日志生成时间,从日志中解析EventTime
          val eventTime = time.split(" ")(0).toLong
          println("eventTime = " + eventTime)
          eventTime
        }
      }).map(x => (x.split(" ")(1), (1L))).keyBy(0)
    /**
      * 引入滑动窗口,设置窗口大小为10秒,并设置窗口滑动过程为5秒
      * 即表示5秒触发一次窗口执行,计算范围为10秒
      */
    val streamWindow = stream.window(SlidingEventTimeWindows.of(Time.seconds(10), Time.seconds(5)))
    // 执行聚合操作
    val streamReduce = streamWindow.reduce((x, y) => (x._1, x._2 + y._2))
    // 打印数据 -> (Sink)
    streamReduce.print()
    // 触发程序执行
    env.execute("SlidingEventTimeWindowsFlow")
  }
}
```
- 2.在本地监听服务端口
```
systemhub:~ system$ nc -l 9999
```
- 3.运行程序
- 4.在本地服务端输入数据源
```
10000 SlidingEventTimeWindowsFlow
11000 SlidingEventTimeWindowsFlow
15000 SlidingEventTimeWindowsFlow
18000 SlidingEventTimeWindowsFlow
```
- 5.查看运行结果
```
eventTime = 10000
eventTime = 11000
eventTime = 15000
eventTime = 18000
7> (SlidingEventTimeWindowsFlow,2)
```

#### 7.3.3 会话窗口 (EventTimeSessionWindows)
> 相邻两次数据的EventTime的时间差超过指定的时间间隔就会触发执行.
> 如果加入Watermark.那么当触发执行时.所有满足时间间隔而还没有触发的Window会同时触发执行.
- 1.创建EventTimeSessionWindowsFlow方法
``` scala
package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.TimeCharacteristic
import org.apache.flink.streaming.api.functions.timestamps.BoundedOutOfOrdernessTimestampExtractor
import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.api.windowing.assigners.{EventTimeSessionWindows, SlidingEventTimeWindows, TumblingEventTimeWindows}
import org.apache.flink.streaming.api.windowing.time.Time

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * EvnetTimeWindowFlow
  * <p>
  */
object EvnetTimeWindowFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用EventTimeSessionWindowsFlow方法
  EventTimeSessionWindowsFlow()

  /**
    * 定义EventTimeSessionWindowsFlow方法
    * 定义 会话窗口 方法
    */
  def EventTimeSessionWindowsFlow(): Unit = {
    // 设置时间特征为EventTime,即表示从调用时开始赋予env创建的每个stream追加时间特征
    env.setStreamTimeCharacteristic(TimeCharacteristic.EventTime)
    // 设置时间戳,对stream进行处理并按key聚合
    val stream = env.socketTextStream("systemhub", 9999)
      .assignTimestampsAndWatermarks(new BoundedOutOfOrdernessTimestampExtractor[String](Time.milliseconds(3000)) {
        override def extractTimestamp(time: String): Long = {
          // / EventTime是日志生成时间,从日志中解析EventTime
          val eventTime = time.split(" ")(0).toLong
          println("eventTime = " + eventTime)
          eventTime
        }
      }).map(x => (x.split(" ")(1), (1L))).keyBy(0)
    /**
      * 引入会话窗口
      * 设置5秒触发一次窗口执行,准确的说当前5秒加上3秒等于8秒,既每8秒才触发对应的窗口执行
      */
    val streamWindow = stream.window(EventTimeSessionWindows.withGap(Time.seconds(5)))
    // 执行聚合操作
    val streamReduce = streamWindow.reduce((x, y) => (x._1, x._2 + y._2))
    // 打印数据 -> (Sink)
    streamReduce.print()
    // 触发程序执行
    env.execute("EventTimeSessionWindowsFlow")
  }
}
```
- 2.在本地监听服务端口
```
systemhub:~ system$ nc -l 9999
```
- 3.运行程序
- 4.在本地服务端输入数据源
```
systemhub:~ system$ nc -l 9999
10000 EventTimeSessionWindowsFlow
11000 EventTimeSessionWindowsFlow
20000 EventTimeSessionWindowsFlow
29000 EventTimeSessionWindowsFlow
30000 EventTimeSessionWindowsFlow
39000 EventTimeSessionWindowsFlow
```
- 5.查看运行结果
```
eventTime = 10000
eventTime = 11000
eventTime = 20000
7> (EventTimeSessionWindowsFlow,2)
eventTime = 29000
7> (EventTimeSessionWindowsFlow,1)
eventTime = 30000
eventTime = 39000
7> (EventTimeSessionWindowsFlow,2)
eventTime = 40000
```


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