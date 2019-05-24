# 大数据Spark生态系统 修仙之道 Spark Blog

@(2019-05-15)[ Docs Language:简体中文 & English|Programing Spark|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)|![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg) | ![GitHub repo size in bytes](https://img.shields.io/github/repo-size/geekparkhub/geekparkhub.github.io.svg) | GeekDeveloper:[JEEP-711](https://github.com/jeep711)|Github:[github.com/geekparkhub](https://github.com/geekparkhub)|Gitee:[gitee.com/geekparkhub](https://gitee.com/geekparkhub) ]

## 🐘 Spark Technology 修仙之道 金仙道果 🐘

![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/spark.jpg)

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


## 🔥 1. Spark 基础 🔥

### 1.1 Spark 概述
- Spark是一种基于内存快速 / 通用 / 可扩展大数据分析引擎.
- Spark在2009年诞生于(UC Berkeley AMP Lab)加州大学伯克利分校AMP实验室,Spark是使用内存计算的开源大数据并行计算框架,可以应对复杂的大数据处理场景,2013年Spark成为Apache基金会旗下顶级项目.
- Spark内核是由Scala编程语言开发,同时也提供了Java/Python/R语言等开发编程接口.


#### 1.1.1 Spark 模块
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_001.jpg)
- 1.`Spark Core` : 实现了Spark基本功能,包含任务调度 / 内存管理 / 错误恢复 / 与存储系统交互等模块,Spark Core中还包含了对弹性分布式数据集(Resilient Distributed DataSet,简称RDD)API定义.
- 2.`Spark SQL` : 是Spark用来操作结构化数据程序包,通过Spark SQL,可以使用SQL或者Apache Hive版本的SQL方言(HQL)来查询数据,Spark SQL支持多种数据源,比如Hive表、Parquet以及JSON等.
- 3.`Spark Streaming` : 是Spark提供对实时数据进行流式计算的组件,提供了用来操作数据流的API,并且与Spark Core中的RDD API高度对应.
- 4.`Spark MLlib` : 提供常见的机器学习(ML)功能程序库,包括分类、回归、聚类、协同过滤等,还提供了模型评估、数据导入等额外支持功能.
- 5.`集群管理器` : Spark设计为可以高效地在一个计算节点到数千个计算节点之间伸缩计算,为了实现这样要求,同时获得最大灵活性,Spark支持在各种集群管理器(Cluster Manager)上运行,包括Hadoop YARN、ApacheMesos,以及Spark自带简易调度器,叫作独立调度器.

#### 1.1.2 Spark 特点
- 1.`快速` : 与Hadoop MapReduce相比,Spark基于内存运算要快100倍以上,基于硬盘运算也要快10倍以上,Spark实现了高效DAG有向无环图执行引擎,可以通过基于内存来高效处理数据流,计算中间结果是存在于内存中.
- 2.`易用` : Spark支持Java、Python和Scala的API,还支持超过80种高级算法,使开发者可以快速构建不同应用,而且Spark支持交互式的Python和Scala的Shell,可以非常方便地在Shell中使用Spark集群来验证解决问题方法.
- 3.`通用性强` : Spark提供了统一解决方案,Spark可以用于批处理 / 交互式查询(SparkSQL) / 实时流处理(SparkStreaming) / 机器学习(SparkMLlib) / 图计算(GraphX),这些不同类型的处理都可以在同一个应用中无缝使用,减少了开发和维护的人力成本和部署平台的物力成本.
- 4.`兼容性` : Spark可以非常方便地与其他的开源产品进行融合,比如Spark可以使用Hadoop YARN和ApacheMesos作为资源管理和调度器,并且可以处理所有Hadoop支持的数据,包括HDFS、HBase等,这对于已经部署Hadoop集群的用户特别重要,因为不需要做任何数据迁移就可以使用Spark强大处理能力.

#### 1.1.3 Spark 应用场景
- 1.Spark具有丰富组件,可适用于多种复杂应用场景,如SQL查询/机器学习/图形计算/流式计算等,同时Spark可以与Hadoop很好地集成在一起,目前已经有部分主流大数据厂商在发行版Hadoop版本中包含Spark/Cloudera/Hortonworks/MapReduce等.
- 2.Spark得到了众多大数据公司的支持,这些公司包括Hortonworks、IBM、Intel、Cloudera、MapR、Pivotal、百度、阿里、腾讯、京东、携程、优酷土豆,当前百度的Spark已应用于大搜索、直达号、百度大数据等业务,阿里利用GraphX构建了大规模图计算和图挖掘系统,实现了很多生产系统的推荐算法,腾讯Spark集群达到8000台规模,是当前已知世界上最大的Spark集群.


### 1.2 Spark 部署
- Spark官方地址 : [spark.apache.org](http://spark.apache.org)
- Spark官方下载 : [spark.apache.org/downloads.html](https://spark.apache.org/downloads.html)
- Spark官方文档 : [spark.apache.org/docs/2.1.1/](https://spark.apache.org/docs/2.1.1/)

解压`spark-2.1.1-bin-hadoop2.7.tgz`
```
[root@systemhub511 software]# tar -zxvf spark-2.1.1-bin-hadoop2.7.tgz -C /opt/module/
```
重命名`spark-2.1.1-bin-hadoop2.7`
```
[root@systemhub511 module]# mv spark-2.1.1-bin-hadoop2.7/ spark
```

### 1.3 Spark 运行模式
#### 💥 1.3.1 Loacl Mode 💥
##### 1.3.1.1 Loacl Mode 概述
- Local模式就是运行在单台本地计算机模式,通常就是用于在本地上练手或测试,它可以通过以下集中方式设置Master.
- 1.`local` : 所有计算都运行在一个线程当中,没有任何并行计算,通常在本机执行测试代码就用这种模式.
- 2.`local[K]` : 指定使用多少个线程来运行计算,比如`local[4]`就是运行4个Worker线程,通常Cpu有几个Core,就指定几个线程,最大化利用Cpu计算能力.
- 3.`local[*]` : 这种模式直接按照Cpu最多Cores来设置线程数量.

##### 1.3.1.2 (求π) & (WordCount) & (本地调试) 官方案例
- 1.基本语法
```
bin/spark-submit \
--class <main-class>
--master <master-url> \
--deploy-mode <deploy-mode> \
--conf <key>=<value> \
... # other options
<application-jar> \
[application-arguments]
```
- 2.参数说明
- `--master`: 指定Master地址,默认为Local.
- `--class`: 应用主启动类(如org.apache.spark.examples.SparkPi).
- `--deploy-mode` : 是否发布驱动到worker节点(cluster)或者作为一个本地客户端(client)(default: client)*
- `--conf` : 任意Spark配置属性,格式`key=value`,如果值包含空格,可以加引号`"key=value"`
- `application-jar` : 打包好应用jar,包含依赖,URL在集群中全局可见,比如`hdfs://`共享存储系统,如果是`file://path`,那么所有节点的path都包含同样的jar包.
- `application-arguments` : 传给main()方法的参数.
- `--executor-memory 1G` : 指定每个executor可用内存为1G
- `--total-executor-cores 2` : 指定每个executor使用cpu核数为2个

- 3.求π程序
- 3.1 求π执行语句
```
bin/spark-submit \
--class org.apache.spark.examples.SparkPi \
--executor-memory 1G \
--total-executor-cores 1 \
./examples/jars/spark-examples_2.11-2.1.1.jar \
100
```
- 3.2 开始执行任务
```
[root@systemhub511 spark]# bin/spark-submit \
> --class org.apache.spark.examples.SparkPi \
> --executor-memory 1G \
> --total-executor-cores 1 \
> ./examples/jars/spark-examples_2.11-2.1.1.jar \
> 100
```
- 3.3 查看执行结果 | 该算法是利用`蒙特·卡罗算法`求π
```
INFO DAGScheduler: Job 0 finished: reduce at SparkPi.scala:38, took 3.059446 s
Pi is roughly 3.1411463141146316
```
- 3.4 启动`spark-shell`
```
[root@systemhub511 spark]# bin/spark-shell
Spark context Web UI available at http://systemhub511:4040
Spark context available as 'sc' (master = local[*], app id = local-1558677071165).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 2.1.1
      /_/
         
Using Scala version 2.11.8 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_162)
Type in expressions to have them evaluated.
Type :help for more information.

scala> 
```
- 3.5 通过WebUI查看程序运行 | `http://hostname:4040`

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_002.jpg)

- 4.运行WordCount程序
- 4.1 在spark根目录创建wordcount目录
```
[root@systemhub511 spark]# mkdir -p input/wordcount
```
- 4.2 在wordcount目录创建数据文件 | vim `wordcount_001.txt`
```
[root@systemhub511 spark]# cd input/wordcount/
[root@systemhub511 wordcount]# vim wordcount_001.txt
```
```
hadoop spark hive
hadoop spark hadoop
hbase flume hive
scala java oozie
```
- 4.3 执行WordCount并查看打印结果
```
scala> sc.textFile("/opt/module/spark/input/wordcount/wordcount_001.txt").flatMap(_.split(" ")).map((_,1)).reduceByKey(_+_).collect
res0: Array[(String, Int)] = Array((scala,1), (spark,2), (hive,2), (hadoop,3), (oozie,1), (flume,1), (java,1), (hbase,1))

scala> 
```
- 4.4 将WordCount执行结果输出至本地文件
```
scala> sc.textFile("/opt/module/spark/input/wordcount/wordcount_001.txt").flatMap(_.split(" ")).map((_,1)).reduceByKey(_+_).saveAsTextFile("./output/wordcount/")
```
- 4.5 查看文件结果
```
[root@systemhub511 spark]# cd output/wordcount/
[root@systemhub511 wordcount]# ll
total 4
-rw-r--r--. 1 root root 79 May 24 14:48 part-00000
-rw-r--r--. 1 root root  0 May 24 14:48 _SUCCESS
[root@systemhub511 wordcount]# cat part-00000 
(scala,1)
(spark,2)
(hive,2)
(hadoop,3)
(oozie,1)
(flume,1)
(java,1)
(hbase,1)
[root@systemhub511 wordcount]# 
```

##### 1.3.1.3 提交流程
- 提交任务分析 | Spark通用运行简易流程
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_003.jpg)
- 提交任务角色 : Driver (驱动器) & Executor (执行器)
- `1. Driver (驱动器)`
- Spark驱动器是执行开发程序中main方法进程,它负责开发人员编写用来创建SparkContext / 创建RDD,以及进行RDD转化操作和行动操作代码的执行,如果使用spark shell,那么当启动Spark shell的时候,系统后台自启一个Spark驱动器程序,就是在Spark shell中预加载一个叫作sc的SparkContext对象,如果驱动器程序终止,那么Spark应用也就结束了.
- 1.1 Driver主要负责 : 1.将开发者程序转为任务. `->` 2.跟踪Executor运行状况. `->` 3.为执行器节点调度任务. `->` 4.WebUI展示应用运行状况.
- `2. Executor (执行器)`
- Spark Executor是一个工作进程,负责在Spark作业中运行任务,任务间相互独立,Spark应用启动时,Executor节点被同时启动,并且始终伴随着整个Spark应用的生命周期而存在,如果有Executor节点发生了故障或崩溃,Spark应用也可以继续执行,会将出错节点上任务调度到其他Executor节点上继续运行.
- 2.2 Executor主要负责 : 1.负责运行组成Spark应用任务,并将结果返回给驱动器进程. `->` 2.通过自身的块管理器(Block Manager)为开发者程序中要求缓存RDD提供内存式存储,RDD是直接缓存在Executor进程内,因此任务可以在运行时充分利用缓存数据加速运算.

##### 1.3.1.4 数据流程

| 参数列表      |     参数描述 |
| :--------: | :--------:|
| `textFile("input")`    |   读取本地文件input文件夹数据 |
| `flatMap(_.split(" "))` | 压平操作,按照空格分割符将一行数据映射成一个个单词 |
| `map((_,1))` | 对每一个元素操作,将单词映射为元组 |
| `reduceByKey(_+_)` | 按照key将值进行聚合相加 |
| `collect` | 将数据收集到Driver端展示 |

- WordCount 程序分析
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_004.jpg)


#### 💥 1.3.2 Standalone Mode 💥
##### 1.3.2.1 Standalone Mode 概述
- 由`Master`+`Slave`构建而成的Spark集群,Spark运行在集群中.
- Standalone运行模式
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_005.jpg)

##### 1.3.2.2 StandaloneMode QuickStart
- 1.在spark根目录下进入conf目录
```
[root@systemhub511 spark]# cd conf/
```
- 2.修改配置文件名称 | `slaves` & `spark-env.sh`
```
[root@systemhub511 conf]# mv slaves.template slaves
[root@systemhub511 conf]# mv spark-env.sh.template spark-env.sh
```
- 3.修改slave文件,添加work节点 | vim `slaves`
```
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# A Spark Worker will be started on each of the machines listed below.
systemhub511
systemhub611
systemhub711
```
- 4.修改spark-env.sh文件 | vim `spark-env.sh`
```
# Options for the daemons used in the standalone deploy mode
SPARK_MASTER_HOST=systemhub511
SPARK_MASTER_PORT=7077
```

- 5.将spark分发至其他节点集群
```
[root@systemhub511 module]# scp -r spark/ root@systemhub611:/opt/module/
[root@systemhub511 module]# scp -r spark/ root@systemhub711:/opt/module/
```
- 6.启动spark集群 | `sbin/start-all.sh`
```
[root@systemhub511 spark]# sbin/start-all.sh
starting org.apache.spark.deploy.master.Master, logging to /opt/module/spark/logs/spark-root-org.apache.spark.deploy.master.Master-1-systemhub511.out
systemhub711: starting org.apache.spark.deploy.worker.Worker, logging to /opt/module/spark/logs/spark-root-org.apache.spark.deploy.worker.Worker-1-systemhub711.out
systemhub611: starting org.apache.spark.deploy.worker.Worker, logging to /opt/module/spark/logs/spark-root-org.apache.spark.deploy.worker.Worker-1-systemhub611.out
systemhub511: starting org.apache.spark.deploy.worker.Worker, logging to /opt/module/spark/logs/spark-root-org.apache.spark.deploy.worker.Worker-1-systemhub511.out
[root@systemhub511 spark]# 
```
- 7.查看集群节点状态
``` powershell
[root@systemhub511 spark]# jps.sh
================        root@systemhub511 All Processes         ===========
30651 org.apache.spark.deploy.worker.Worker
30443 org.apache.spark.deploy.master.Master
813 sun.tools.jps.Jps
================        root@systemhub611 All Processes         ===========
10369 org.apache.spark.deploy.worker.Worker
11777 sun.tools.jps.Jps
================        root@systemhub711 All Processes         ===========
8960 org.apache.spark.deploy.worker.Worker
10364 sun.tools.jps.Jps
[root@systemhub511 spark]# 
```

- 8.(求π)官方案例
- 8.1 执行语句 | 指定 spark master
```
bin/spark-submit \
--class org.apache.spark.examples.SparkPi \
--master spark://systemhub511:7077 \
--executor-memory 1G \
--total-executor-cores 1 \
./examples/jars/spark-examples_2.11-2.1.1.jar \
100
```
- 8.2 执行并查看结果
```
[root@systemhub511 spark]# bin/spark-submit \
> --class org.apache.spark.examples.SparkPi \
> --master spark://systemhub511:7077 \
> --executor-memory 1G \
> --total-executor-cores 1 \
> ./examples/jars/spark-examples_2.11-2.1.1.jar \
> 100
INFO DAGScheduler: Job 0 finished: reduce at SparkPi.scala:38, took 6.478381 s
Pi is roughly 3.1405883140588315
```

- 8.3 启动`sparkshell`,并执行WordCount程序查看结果
- 参数：`--master spark://systemhub511:7077` 指定要连接集群master
```
[root@systemhub511 spark]# bin/spark-shell --master spark://systemhub511:7077

Spark context Web UI available at http://systemhub511:4040
Spark context available as 'sc' (master = spark://systemhub511:7077, app id = app-20190524174512-0001).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 2.1.1
      /_/
         
Using Scala version 2.11.8 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_162)
Type in expressions to have them evaluated.
Type :help for more information.

scala> sc.textFile("/opt/module/spark/input/wordcount/wordcount_001.txt").flatMap(_.split(" ")).map((_,1)).reduceByKey(_+_).collect
res0: Array[(String, Int)] = Array((scala,1), (hive,2), (oozie,1), (java,1), (spark,2), (hadoop,3), (flume,1), (hbase,1))

scala> 
```

- 8.4 通过WebUI查看程序运行 | `http://hostname:8088`
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_006.jpg)

- 8.5 配置历史服务器(JobHistoryServer)
- 重命名`spark-default.conf.template`
```
[root@systemhub511 conf]# mv spark-defaults.conf.template spark-defaults.conf
```
- 8.5.1 配置`spark-default.conf` | vim `spark-default.conf`
```
spark.master                     spark://systemhub511:7077
spark.eventLog.enabled           true
spark.eventLog.dir               hdfs://systemhub511:9000/directory
```
- 8.5.2 配置spark-env.sh | vim `spark-env.sh`
```
export SPARK_HISTORY_OPTS="-Dspark.history.ui.port=18080 -Dspark.history.retainedApplications=30 -Dspark.history.fs.logDirectory=hdfs://systemhub511:9000/directory"
```
- 参数描述 : 
```
spark.eventLog.dir：Application在运行过程中所有信息均记录在该属性指定的路径下.

spark.history.ui.port=18080 WEBUI访问端口号为18080

spark.history.fs.logDirectory=hdfs://systemhub511:9000/directory 配置了该属性后,在start-history-server.sh时就无需再显示指定路径,Spark History Server只展示该指定路径下信息.

spark.history.retainedApplications=30 指定保存Application历史记录个数,如果超过这个值,旧应用程序信息将被删除,这个是内存中应用数,而不是页面上显示应用数.
```
- 8.5.3 分发至其他节点集群
```
[root@systemhub511 module]# scp -r spark/ root@systemhub611:/opt/module/
[root@systemhub511 module]# scp -r spark/ root@systemhub711:/opt/module/
```
- 8.5.4 启动Hadoop HDFS
```
[root@systemhub511 hadoop]# sbin/start-dfs.sh
```
- 8.5.5 手动创建HDFS /directory目录
```
[root@systemhub511 spark]# hadoop fs -mkdir /directory
``` 
- 8.5.6 启动Spark集群
```
[root@systemhub511 spark]# sbin/start-all.sh
```
- 8.5.6 启动Spark历史服务
```
[root@systemhub511 spark]# sbin/start-history-server.sh
```
- 8.5.7 启动`sparkshell`
```
[root@systemhub511 spark]# bin/spark-shell --master spark://systemhub511:7077
sc.textFile("/opt/module/spark/input/wordcount/wordcount_001.txt").flatMap(_.split(" ")).map((_,1)).reduceByKey(_+_).collect
```
- 8.5.8 查看历史服务 | `http://hostname:18080`
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_007.jpg)

#### 💥 1.3.3 Yarn Mode 💥
##### 1.3.3.1 Yarn Mode 概述





#### 💥 1.3.4 Mesos Mode 💥
##### 1.3.4.1 Mesos Mode 概述



### 🔥 1.3 Spark Core 🔥
#### 1.3.1 RDD 概述
#### 1.3.2 RDD 编程
#### 1.3.3 RDD 持久化
#### 1.3.4 RDD 依赖关系
#### 1.3.5 键值对操作
#### 1.3.6 数据读取保存
#### 1.3.7 Spark 进阶
#### 1.3.8 Spark Core 实例


### 🔥 1.4 Spark SQL 🔥
#### 1.4.1 Spark SQL 概述
#### 1.4.2 Spark SQL 查询
#### 1.4.3 DataFrame
#### 1.4.4 DataSet
#### 1.4.5 聚合函数
#### 1.4.6 Spark SQL 数据源
#### 1.4.7 OLAP Server
#### 1.4.8 Spark SQL 实例


### 🔥 1.5 Spark Streaming 🔥
#### 1.5.1 Spark Streaming 概述
#### 1.5.2 Spark Streaming Program
#### 1.5.3 DataStream 概述
#### 1.5.4 DataStream 输入
#### 1.5.5 DataStream 转换
#### 1.5.6 DataStream 输出
#### 1.5.7 7*24hour运行
#### 1.5.8 Spark Streaming 实例



## 🔥 2. Spark 高阶 🔥
### 2.1 内核机制
### 2.1 性能调优







## 3. 修仙之道 技术架构迭代 登峰造极之势
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