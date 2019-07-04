# 大数据生态系统 修仙之道 Flink Blog

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


## 🔥 3. Flink集群部署 🔥

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


## 🔒 尚未解锁 正在探索中... 尽情期待 Blog更新! 🔒

## 🔥 5. Flink DataStream API 🔥
### 5.1 Flink 运行模型
### 5.2 Flink 程序架构
### 5.3 Environment
### 5.4 Source
### 5.5 Sink
### 5.6 Transformation

## 🔥 6. Time & Window 🔥
### 6.1 Time
### 6.2 Window
### 6.3 Window API


## 🔥 7. EventTime & Window 🔥
### 7.1 EventTime 引入
### 7.2 Watermark
### 7.3 EvnetTimeWindow API



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