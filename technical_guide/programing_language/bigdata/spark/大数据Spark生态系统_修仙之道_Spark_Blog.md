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

##### 1.3.2.3 Spark HA 高可用
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_008.jpg)

- 1.停止集群所有服务
- 2.配置spark-env.sh | vim `spark-env.sh`
```
# SPARK_MASTER_HOST=systemhub511
# SPARK_MASTER_PORT=7077
export SPARK_DAEMON_JAVA_OPTS="-Dspark.deploy.recoveryMode=ZOOKEEPER -Dspark.deploy.zookeeper.url=systemhub511,systemhub611,systemhub711 -Dspark.deploy.zookeeper.dir=/spark"
export SPARK_HISTORY_OPTS="-Dspark.history.ui.port=18080 -Dspark.history.retainedApplications=30 -Dspark.history.fs.logDirectory=hdfs://systemhub511:9000/directory"
```
- 3.分发至其他节点集群
```
[root@systemhub511 module]# scp -r spark/ root@systemhub611:/opt/module/
[root@systemhub511 module]# scp -r spark/ root@systemhub711:/opt/module/
```
- 4.启动Hadoop HDFS
```
[root@systemhub511 spark]# /opt/module/hadoop/sbin/start-dfs.sh
```
- 5.启动Zookeeper集群
```
[root@systemhub511 spark]# /opt/module/zookeeper/bin/zkServer.sh start
[root@systemhub611 ~]# /opt/module/zookeeper/bin/zkServer.sh start
[root@systemhub711 ~]# /opt/module/zookeeper/bin/zkServer.sh start
```
- 6.在systemhub511启动全部服务节点
```
[root@systemhub511 spark]# sbin/start-all.sh
```
- 7.在systemhub611单独启动master备份节点
```
[root@systemhub611 ~]# /opt/module/spark/sbin/start-master.sh
```
- 8.访问SparkHA集群
```
[root@systemhub511 spark]# bin/spark-shell --master spark://systemhub511:7077,systemhub611:7077
```
`http://systemhub511:8080` | systemhub511节点状态为`ALIVE`
`http://systemhub611:8080` | systemhub611节点状态为`STANDBY`
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_009.jpg)

- 9.故障转移测试
- 手动杀死systemhub511服务器Master进程,并查看systemhub511是否将任务转移给systemhub611备份节点作为主节点.
- 9.1 查看集群节点状态
```
[root@systemhub511 spark]# jps.sh
================        root@systemhub511 All Processes         ===========
32242 org.apache.hadoop.hdfs.server.namenode.NameNode
11206 org.apache.spark.deploy.master.Master
11368 org.apache.spark.deploy.worker.Worker
9705 org.apache.zookeeper.server.quorum.QuorumPeerMain
32444 org.apache.hadoop.hdfs.server.datanode.DataNode
5228 sun.tools.jps.Jps
================        root@systemhub611 All Processes         ===========
9157 org.apache.spark.deploy.master.Master
8901 org.apache.spark.deploy.worker.Worker
2822 sun.tools.jps.Jps
30214 org.apache.hadoop.hdfs.server.datanode.DataNode
7495 org.apache.zookeeper.server.quorum.QuorumPeerMain
================        root@systemhub711 All Processes         ===========
5312 org.apache.spark.deploy.worker.Worker
31568 sun.tools.jps.Jps
26869 org.apache.hadoop.hdfs.server.namenode.SecondaryNameNode
26647 org.apache.hadoop.hdfs.server.datanode.DataNode
4014 org.apache.zookeeper.server.quorum.QuorumPeerMain
[root@systemhub511 spark]# 
```

- 9.2 Kill systemhub511 Master主节点
```
[root@systemhub511 spark]# kill -9 11206
```
- 9.3 systemhub511节点已宕机 | systemhub611备份节点状态已转化为ALIVE主节点
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_010.jpg)


#### 💥 1.3.3 Yarn Mode 💥
##### 1.3.3.1 Yarn Mode 概述
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_011.jpg)
- Spark客户端直接连接Yarn,不需要额外构建Spark集群.
- 两种模式`yarn-client`和`yarn-cluster`,主要区别在于 : Driver程序运行节点
- `yarn-client` : Driver程序运行在客户端,适用于交互调试,立即看到app输出.
- `yarn-cluster` : Driver程序运行在由RM(ResourceManager)启动AP(APPMaster)适用于生产环境.

##### 1.3.3.2 YarnMode QuickStart

- 1.配置spark-env.sh | vim `spark-env.sh`
```
YARN_CONF_DIR=/opt/module/hadoop/etc/hadoop
```
- vim `spark-defaults.conf`
```
spark.master                     spark://systemhub511:7077
spark.eventLog.enabled           true
spark.eventLog.dir               hdfs://systemhub511:9000/directory
spark.yarn.historyServer.address=systemhub511:18080
spark.history.ui.port=18080
```
- vim `yarn-site.xml`
``` xml
<!--是否启动一个线程检查每个任务正使用的物理内存量,如果任务超出分配值,则直接将其杀掉,默认是true -->
<property>
  <name>yarn.nodemanager.pmem-check-enabled</name>
  <value>false</value>
</property>

<!--是否启动一个线程检查每个任务正使用的虚拟内存量,如果任务超出分配值,则直接将其杀掉,默认是true-->
<property>
  <name>yarn.nodemanager.vmem-check-enabled</name>
  <value>false</value>
</property>
```

- 2.分发至其他节点集群
```
[root@systemhub511 module]# scp -r spark/ root@systemhub611:/opt/module/
[root@systemhub511 module]# scp -r spark/ root@systemhub711:/opt/module/
```

- 3.提交任务到Yarn执行
```
bin/spark-submit \ 
--class org.apache.spark.examples.SparkPi \ 
--master yarn \ 
--deploy-mode client \ 
./examples/jars/spark-examples_2.11-2.1.1.jar\ 
100
```

#### 💥 1.3.4 Mesos Mode 💥
##### 1.3.4.1 Mesos Mode 概述
- Spark客户端直接连接Mesos,不需要额外构建Spark集群,国内应用比较少,更多是运用yarn调度.


#### 💥 1.3.5 运行模式对比 💥

| 模式      |     集群数量 |   集群进程   |   所属者   |
| :--------: | :--------:| :------: | :------: |
| Loacl Mode    |   1 |  无  |  Spark  |
| Standalone Mode    |   3 |  Master & Worker  |  Spark  |
| Yarn Mode    |   1 |  Yarn & HDFS  |  Hadoop  |

#### 💥 1.3.6 WordCount 实例 💥
- Spark Shell仅在测试和验证程序时使用的较多,在生产环境中通常会在IDE中编制程序,然后打成jar包提交到集群,最常用是创建Maven工程,利用Maven来管理jar包依赖.
- 1.JetBrains IntelliJ IDEA New Maven Project | 此过程省略
- 2.父工程配置信息 | pom.xml
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.geekparkhub.core.spark</groupId>
    <artifactId>spark_server</artifactId>
    <packaging>pom</packaging>
    <version>1.0-SNAPSHOT</version>

    <modules>
        <module>spark-common</module>
    </modules>

    <dependencies>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-core_2.11</artifactId>
            <version>2.1.1</version>
        </dependency>
    </dependencies>

</project>
```
- 3.创建子模块 spark-common | 子模块配置信息 pom.xml
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>spark_server</artifactId>
        <groupId>com.geekparkhub.core.spark</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>

    <artifactId>spark-common</artifactId>

    <build>
        <finalName>WordCount</finalName>
        <plugins>
            <plugin>
                <groupId>net.alchim31.maven</groupId>
                <artifactId>scala-maven-plugin</artifactId>
                <version>3.2.2</version>
                <executions>
                    <execution>
                        <goals>
                            <goal>compile</goal>
                            <goal>testCompile</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>

</project>
```

- 4.在`spark-common`子模块中创建scala源码目录 | Create `WordCount.scala`
``` scala
package com.geekparkhub.core.spark.application.wordcount

import org.apache.spark.rdd.RDD
import org.apache.spark.{SparkConf, SparkContext}

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园枢纽
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * WordCountApplication
  * <p>
  */

object WordCount {
  def main(args: Array[String]): Unit = {

    /**
      * Create SparkConf
      * 创建 SparkConf
      */
    val sparkConf = new SparkConf().setMaster(args(0)).setAppName("WordCountApplication")

    /**
      * Create SparkContext
      * 创建 SparkContext
      */
    val sc = new SparkContext()

    /**
      * Read file
      * 读取文件
      */
    val line: RDD[String] = sc.textFile(args(1))

    /**
      * To flatten
      * 压平
      */
    val word: RDD[String] = line.flatMap(_.split(" "))

    /**
      * Word conversion dual group
      * 单词转换二元组
      */
    val wordAndOne: RDD[(String, Int)] = word.map((_, 1))

    /**
      * Count the total number of words
      * 统计单词总数
      */
    val wordCount: RDD[(String, Int)] = wordAndOne.reduceByKey(_+_)

    /**
      * Write out the file
      * 写出文件
      */
    wordCount.saveAsTextFile(args(2))

    /**
      * Close resource
      * 关闭资源
      */
    sc.stop()
  }
}
```
- 5.将`spark-common`子模块打至成jar包上传至systemhub511服务器
- 6.启动HDFS | 在HDFS创建多级目录
```
[root@systemhub511 ~]# hadoop fs -mkdir -p /core_flow/spark/input/wordcount
```

- 7.将本地文件上传至HDFS目录
```
hadoop fs -put /opt/module/spark/input/wordcount/wordcount_001.txt /core_flow/spark/input/wordcount
```
- 8.Yarn执行提交任务至
```
bin/spark-submit \
--class com.geekparkhub.core.spark.application.wordcount.WordCount \
--master yarn \
./lib_jar/WordCount.jar yarn \
/core_flow/spark/input/wordcount/wordcount_001.txt \
/core_flow/spark/output/wordcount
```
- 9.查看任务汇总结果
- 9.1 `hadoop fs -ls -R`
```
[root@systemhub511 spark]# hadoop fs -ls -R /core_flow/spark/output/wordcount/
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
-rw-r--r--   3 root supergroup /core_flow/spark/output/wordcount/_SUCCESS
-rw-r--r--   3 root supergroup /core_flow/spark/output/wordcount/part-00000
-rw-r--r--   3 root supergroup /core_flow/spark/output/wordcount/part-00001
[root@systemhub511 spark]# 
```
- 9.2 part-00000
```
[root@systemhub511 spark]# hadoop fs -cat /core_flow/spark/output/wordcount/part-00000
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
(scala,1)
(hive,2)
(oozie,1)
(java,1)
[root@systemhub511 spark]# 
```
- 9.3 part-00001
```
[root@systemhub511 spark]# hadoop fs -cat /core_flow/spark/output/wordcount/part-00001
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
(spark,2)
(hadoop,3)
(flume,1)
(hbase,1)
[root@systemhub511 spark]# 
```


### 🔥 1.3 Spark Core 🔥
#### 1.3.1 RDD 概述
##### 1.3.1.1 什么是RDD
> `RDD` (`Resilient Distributed Dataset`)`弹性分布式数据集`是Spark中最基本数据抽象,代码中是一个抽象类,它代表一个弹性/不可变/可分区/里面的元素可并行计算的集合.

##### 1.3.1.2 RDD 属性
```
 * Internally, each RDD is characterized by five main properties:
 *
 *  - 1. A list of partitions
 *  - 2. A function for computing each split
 *  - 3. A list of dependencies on other RDDs
 *  - 4. Optionally, a Partitioner for key-value RDDs (e.g. to say that the RDD is hash-partitioned)
 *  - 5. Optionally, a list of preferred locations to compute each split on (e.g. block locations for an HDFS file)
```
> 1.一组分区(Partition),即数据集基本组成单位;
> 2.一个计算每个分区的函数;
> 3.RDD之间依赖关系;
> 4.一个Partitioner,即RDD分片函数;
> 5.一个列表,存储存取每个Partition的优先位置(preferred location)

##### 1.3.1.3 RDD 特点
> RDD表示只读分区数据集,对RDD进行改动,只能通过RDD转换操作,由一个RDD得到一个新的RDD,新的RDD包含了从其他RDD衍生所必需的信息,RDDs之间存在依赖,RDD执行是按照血缘关系延时计算,如果血缘关系较长,可以通过持久化RDD来切断血缘关系.

###### 1.3.1.3.1 弹性
- 存储弹性 : 内存与磁盘的自动切换.
- 容错弹性 : 数据丢失可以自动恢复.
- 计算弹性 : 计算出错重试机制.
- 分片弹性 : 可根据需要重新分片.


###### 1.3.1.3.2 分区
> RDD逻辑上是分区的,每个分区数据是抽象存在的,计算时会通过一个compute函数得到每个分区数据,如果RDD是通过已有文件系统构建,则compute函数是读取指定文件系统中数据,如果RDD是通过其他RDD转换而来,则compute函数是执行转换逻辑将其他RDD数据进行转换.

###### 1.3.1.3.3 只读
> RDD是只读的,要想改变RDD中数据,只能在现有RDD基础上创建新的RDD.
> 
> 由一个RDD转换到另一个RDD,可以通过丰富的操作算子实现,不再像MapReduce那样只能写map和reduce.
> 
> RDD操作算子包括两类,一类是`transformations`,它是用来将RDD进行转化,构建RDD的血缘关系,另一类是`actions`,它是用来触发RDD计算得到RDD相关计算结果或者将RDD保存文件系统中.

###### 1.3.1.3.4 依赖
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_012.jpg)

> 如图所示,RDDs通过操作算子进行转换,转换得到新RDD包含了从其他RDDs衍生所必需的信息,RDDs之间维护着这种血缘关系,也称之为依赖.
> 
> 依赖包括两种,一种是窄依赖,RDDs之间分区是一一对应,另一种是宽依赖,下游RDD的每个分区与上游RDD(也称之为父RDD)的每个分区都有关,是多对多关系.

###### 1.3.1.3.5 缓存
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_013.jpg)

> 如果在应用程序中多次使用同一个RDD时,可以将该RDD缓存起来,该RDD只有在第一次计算时会根据血缘关系得到分区数据,在后续其他地方用到该RDD时,会直接从缓存处取而不用再根据血缘关系计算,这样就加速后期的重用.
> 
> 如图所示,RDD-1经过一系列转换后得到RDD-n并保存到HDFS,RDD-1在这一过程中会有个中间结果,如果将其缓存到内存,那么在随后RDD-1转换到RDD-m这一过程中,就不会计算其之前的RDD-0.

###### 1.3.1.3.6 CheckPoint
> 虽然RDD血缘关系天然地可以实现容错,当RDD某个分区数据失败或丢失,可以通过血缘关系重建,但是对于长时间迭代型应用来说随着迭代进行,RDDs之间血缘关系会越来越长,一旦在后续迭代过程中出错,则需要通过非常长的血缘关系去重建,势必影响性能.
> 
> 为此,RDD支持checkpoint将数据保存到持久化存储中,这样就可以切断之前血缘关系,因为checkpoint后的RDD不需要知道它的父RDDs,它可以从checkpoint处拿到数据.


#### 1.3.2 RDD 编程
##### 1.3.2.1 编程模型
> 在Spark中,RDD被表示为对象,通过对象方法调用RDD进行转换,经过一系列的`transformations`定义RDD之后,就可以调用`actions`触发RDD计算,`action`可以是向应用程序返回结果(count,collect等),或者是向存储系统保存数据(saveAsTextFile等).
> 在Spark中,只有遇到`action`才会执行RDD计算(即延迟计算),这样在运行时可以通过管道方式传输多个转换.
> 使用Spark开发者需要编写一个Driver程序,它被提交到集群以调度运行Worker,Driver中定义了一个或多个RDD.并调用RDD上的action.Worker则执行RDD分区计算任务.
##### 1.3.2.2 RDD 创建
- Spark创建RDD创建方式可以分为三种:
- 1.从集合中创建RDD
- 2.从外部存储创建RDD
- 3.从其他RDD创建
###### 1.3.2.1 集合创建RDD
- 从集合中创建RDD,Spark主要提供了两种函数 : `parallelize`和`makeRDD`
- 1.使用`parallelize()`从集合创建RDD
```
scala> val rdd = sc.parallelize(Array(511,611,711))
rdd: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[0] at parallelize at <console>:24
scala> rdd.collect
res0: Array[Int] = Array(511, 611, 711)
scala> 
```
- 2.使用`makeRDD()`从集合创建RDD
```
scala> val makerdd = sc.makeRDD(Array(511,611,711))
makerdd: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[1] at makeRDD at <console>:24
scala> makerdd.collect
res1: Array[Int] = Array(511, 611, 711)
scala> 
```
###### 1.3.2.2 外部存储系统数据集创建RDD
- 除了在本地文件系统,还有所有Hadoop支持数据集,比如HDFS/Cassandra/HBase等.
- 详见 1.3.4 数据读取保存
```
scala> sc.textFile("/opt/module/spark/input/wordcount/wordcount_001.txt")
res2: org.apache.spark.rdd.RDD[String] = /opt/module/spark/input/wordcount/wordcount_001.txt MapPartitionsRDD[3] at textFile at <console>:25
scala> 
```

###### 1.3.2.3 从其他创建RDD
- 详见1.3.2.3 RDD 转换


##### 1.3.2.3 RDD 转换
- RDD整体分为`Value`类型和`Key-Value`类型

##### 1.3.2.3.1 Value 类型
###### 1.3.2.3.1.1 `map(func)` Method
- 作用 : 返回一个新RDD,该RDD由每一个输入元素经过func函数转换后组成.
- 创建RDD
```
scala> val rdd = sc.parallelize(Array(511,611,711))
rdd: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[0] at parallelize at <console>:24
scala> rdd.collect
res0: Array[Int] = Array(511, 611, 711)
scala> 
```
- 打印RDD最终结果
```
scala> rdd.map((_,1)).collect
res4: Array[(Int, Int)] = Array((511,1), (611,1), (711,1))
scala> 
```
- 将所有元素RDD*2,最终结果
```
scala> rdd.map((_*2)).collect
res5: Array[Int] = Array(1022, 1222, 1422)
scala> 
```
###### 1.3.2.3.1.2 `mapPartitions(func)` Method
- 作用 : 类似于map,但独立地在RDD每一个分片上运行,因此在类型为T的RDD上运行时,func函数类型必须是Iterator[T] => Iterator[U]
- 假设有N个元素,有M个分区,那么map函数将被调用N次,而mapPartitions被调用M次,一个函数一次处理所有分区.
```
scala> rdd.mapPartitions(_.map(_*2)).collect
res11: Array[Int] = Array(1022, 1222, 1422)
scala> 
```

###### 1.3.2.3.1.3 `mapPartitionsWithIndex(func)` Method
- 作用 : 类似于mapPartitions,但func带有一个整数参数表示分片索引值,因此在类型为T的RDD上运行时,func的函数类型必须是(Int, Interator[T]) => Iterator[U];
```
scala> rdd.mapPartitionsWithIndex((index,items)=>(items.map((index,_)))).collect
res13: Array[(Int, Int)] = Array((1,511), (2,611), (3,711))
scala> 
```

###### 1.3.2.3.1.4 `flatMap(func)` Method
- 作用 : 类似于map,但是每一个输入元素可以被映射为0或多个输出元素(所以func应该返回一个序列,而不是单一元素)
```
scala> val text = sc.textFile("/core_flow/spark/input/wordcount/wordcount_001.txt")
text: org.apache.spark.rdd.RDD[String] = /core_flow/spark/input/wordcount/wordcount_001.txt MapPartitionsRDD[15] at textFile at <console>:24
scala> text.flatMap(_.split(" ")).collect
res16: Array[String] = Array(hadoop, spark, hive, hadoop, spark, hadoop, hbase, flume, hive, scala, java, oozie)
scala> 
```

###### 1.3.2.3.1.5 `map()`与`mapPartition()`区别
- 1.map() : 每次处理一条数据
- 2.mapPartition() : 每次处理一个分区的数据,这个分区的数据处理完后,原RDD中分区的数据才能释放,可能导致OOM.
- 3.开发指导 : 当内存空间较大的时候建议使用mapPartition(),以提高处理效率.

###### 1.3.2.3.1.6 `glom` Method
- 作用 : 将每一个分区形成一个数组,形成新的RDD类型时RDD[Array[T]]
```
scala> rdd.glom.collect
res17: Array[Array[Int]] = Array(Array(), Array(511), Array(611), Array(711))   
scala> 
```

###### 1.3.2.3.1.7 `groupBy(func)` Method
- 作用 : 分组按照传入函数的返回值进行分组,将相同的key对应的值放入一个迭代器.
```
scala> rdd.groupBy(_ % 2).collect
res18: Array[(Int, Iterable[Int])] = Array((1,CompactBuffer(611, 711, 511)))    
scala> 
```

###### 1.3.2.3.1.8 `filter(func)` Method
- 作用 : 过滤返回一个新的RDD,该RDD由经过func函数计算后返回值为true的输入元素组成.
```
scala> rdd.filter(_%3==0).collect
res20: Array[Int] = Array(711)
scala> 
```

###### 1.3.2.3.1.9 `sample(withReplacement,fraction,seed)` Method
- 作用 : 以指定随机种子随机抽样出数量为fraction的数据,withReplacement表示是抽出的数据是否放回,true为有放回的抽样,false为无放回的抽样,seed用于指定随机数生成器种子.
```
scala> val rdd = sc.parallelize(1 to 100)
rdd: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[22] at parallelize at <console>:24
scala> rdd.sample(false,0.1,3).collect
res22: Array[Int] = Array(1, 33, 37, 50, 59, 69, 75, 78, 85, 98) 
scala> 
```

###### 1.3.2.3.1.10 `distinct([numTasks]))` Method
- 作用 : 对源RDD进行去重后返回一个新的RDD,默认情况下,只有8个并行任务来操作,但是可以传入一个可选的numTasks参数改变它.
- 使用distinct()对其去重操作.
```
scala> rdd.distinct(4).collect
res23: Array[Int] = Array(84, 100, 96, 52, 56, 4, 76, 16, 28, 80, 48, 32, 36, 24, 64, 92, 40, 72, 8, 12, 20, 60, 44, 88, 68, 13, 41, 61, 81, 21, 77, 53, 97, 25, 29, 65, 73, 57, 93, 33, 37, 45, 1, 89, 17, 69, 9, 85, 49, 5, 34, 82, 66, 22, 54, 98, 46, 30, 14, 50, 62, 42, 74, 90, 6, 70, 18, 38, 86, 58, 78, 26, 94, 10, 2, 19, 39, 15, 47, 71, 55, 95, 79, 59, 11, 35, 27, 75, 51, 23, 63, 83, 67, 3, 7, 91, 31, 87, 43, 99)
scala> 
```
###### 1.3.2.3.1.11 `coalesce(numPartitions)` Method
- 作用 : 缩减分区数,用于大数据集过滤后,提高小数据集的执行效率.
- 创建4个分区RDD,对其缩减分区.
- 创建RDD/查看RDD分区数/对RDD重新分区/查看新RDD分区数
```
scala> val rdd = sc.parallelize(1 to 16,4)
rdd: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[27] at parallelize at <console>:24

scala> rdd.partitions.size
res24: Int = 4

scala> val coalesceRDD = rdd.coalesce(3)
coalesceRDD: org.apache.spark.rdd.RDD[Int] = CoalescedRDD[28] at coalesce at <console>:26

scala> coalesceRDD.partitions.size
res25: Int = 3
scala> 
```
###### 1.3.2.3.1.12 `repartition(numPartitions)` Method
- 作用 : 根据分区数,重新通过网络随机洗牌所有数据.
- 创建4个分区RDD,对其重新分区.
- 创建RDD/查看RDD分区数/对RDD重新分区/查看新RDD分区数
```
scala> val rdd = sc.parallelize(1 to 16,4)
rdd: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[29] at parallelize at <console>:24

scala> rdd.partitions.size
res26: Int = 4

scala> val rerdd = rdd.repartition(2)
rerdd: org.apache.spark.rdd.RDD[Int] = MapPartitionsRDD[33] at repartition at <console>:26

scala> rerdd.partitions.size
res27: Int = 2
scala> 
```

###### 1.3.2.3.1.13 `coalesce`与`repartition`区别
> 1.`coalesce`重新分区,可以选择是否进行shuffle过程,由参数`shuffle: Boolean = false/true`决定.
> 
> 2.`repartition`实际上是调用coalesce,进行shuffle过程,源码演示:
``` scala
def repartition(numpartitions: int)(implicit ord: ordering[t] = null): rdd[t] = withscope {
coalesce(numpartitions, shuffle = true)
}
```
###### 1.3.2.3.1.14 `sortBy(func,[ascending],[numTasks])` Method
- 作用 : 使用func先对数据进行处理,按照处理后的数据比较结果排序,默认为正序.
- 创建RDD,按照不同规则进行排序 | 按照自身大小排序 / 按照与3余数大小排序 / 按照倒序排序
```
scala>  val rdd = sc.parallelize(List(2,1,3,4))
rdd: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[34] at parallelize at <console>:24

scala> rdd.sortBy(x => x).collect()
res29: Array[Int] = Array(1, 2, 3, 4)

scala> rdd.sortBy(x => x%3).collect()
res30: Array[Int] = Array(3, 1, 4, 2)

scala> rdd.sortBy(x => x,false).collect()
res31: Array[Int] = Array(4, 3, 2, 1)

scala> 
```

###### 1.3.2.3.1.15 `pipe(command,[envVars])` Method
- 作用 : 管道针对每个分区,都执行一个shell脚本,返回输出RDD.
- 创建脚本,使用管道将脚本作用于RDD上
```
[root@systemhub511 ~]# vim /opt/module/spark/input/pipe.sh
[root@systemhub511 ~]# chmod 777 /opt/module/spark/input/pipe.sh
```
- vim `pipe.sh`
``` powershell
#!/bin/
shecho"Start"
while read LINE;do
	echo ">>>" ${LINE}
done
```
```
scala> rdd.pipe("/opt/module/spark/pipe.sh").collect
res18: Array[String] = Array(Start, >>>hi, >>>Hello, >>>how, >>>are, >>>you)
scala> 
```



##### 1.3.2.3.2 双Value类型交互

###### 1.3.2.3.2.1 `union(otherDataset)` Method
- 作用 : 对源RDD和参数RDD求并集后返回一个新RDD | 创建两个RDD进行并集计算
```
scala> var rdd1 = sc.parallelize(1 to 5)
rdd1: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[0] at parallelize at <console>:24

scala> var rdd2 = sc.parallelize(5 to 10)
rdd2: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[1] at parallelize at <console>:24

scala> rdd1.union(rdd2).collect
res0: Array[Int] = Array(1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10)
scala> 
```

###### 1.3.2.3.2.2 `subtract(otherDataset)` Method
- 作用 : 计算差的一种函数,去除两个RDD中相同元素,不同的RDD将保留下来
```
scala> rdd1.subtract(rdd2).collect
res0: Array[Int] = Array(2, 4, 1, 3)
scala> 
```

###### 1.3.2.3.2.3 `intersection(otherDataset)` Method
- 作用 : 对源RDD和参数RDD求交集后,返回一个新的RDD
```
scala> rdd1.intersection(rdd2).collect
res1: Array[Int] = Array(5)
scala> 
```
###### 1.3.2.3.2.4 `cartesian(otherDataset)` Method
- 作用 : 笛卡尔积 `(尽量避免使用)`
```
scala> rdd1.cartesian(rdd2).collect
res2: Array[(Int, Int)] = Array((1,5), (1,6), (1,7), (2,5), (2,6), (2,7), (1,8), (1,9), (1,10), (2,8), (2,9), (2,10), (3,5), (3,6), (3,7), (4,5), (4,6), (4,7), (5,5), (5,6), (5,7), (3,8), (3,9), (3,10), (4,8), (4,9), (4,10), (5,8), (5,9), (5,10))
scala> 
```

###### 1.3.2.3.2.5 `zip(otherDataset)` Method
- 作用 : 将两个RDD组合成Key/Value形式RDD,默认两个RDD的partition数量以及元素数量都相同,否则会抛出异常.
```
scala> rdd1.zip(rdd2).collect
res4: Array[(Int, Int)] = Array((1,6), (2,7), (3,8), (4,9), (5,10))
scala> 
```

##### 1.3.2.3.3 Key-Value 类型

###### 1.3.2.3.3.1 `partitionBy` Method
- 作用 : 对pairRDD进行分区操作,如果原有的partionRDD和现有的partionRDD是一致的话就不进行分区,否则会生成ShuffleRDD,即会产生shuffle过程.
```
scala> val rdd1 = sc.parallelize(Array((1,"A"),(2,"B"),(3,"C"),(4,"D")),4)
rdd1: org.apache.spark.rdd.RDD[(Int, String)] = ParallelCollectionRDD[0] at parallelize at <console>:24

scala> rdd1.mapPartitionsWithIndex((i,t)=>t.map((i,_))).collect
res3: Array[(Int, (Int, String))] = Array((0,(1,A)), (1,(2,B)), (2,(3,C)), (3,(4,D)))

scala> rdd1.partitionBy(new org.apache.spark.HashPartitioner(2))
res5: org.apache.spark.rdd.RDD[(Int, String)] = ShuffledRDD[3] at partitionBy at <console>:27

scala> res5.partitions.size
res6: Int = 2
scala> 
```

###### 1.3.2.3.3.2 `reduceByKey(func,[numTasks])` Method
- 在一个(K,V)的RDD上调用,返回一个(K,V)的RDD,使用指定reduce函数,将相同key值聚合到一起,reduce任务个数可以通过第二个可选参数来设置.
```
scala> val rdd = sc.parallelize(List(("female",1),("male",5),("female",5),("male",2)))
rdd: org.apache.spark.rdd.RDD[(String, Int)] = ParallelCollectionRDD[4] at parallelize at <console>:24

scala> rdd.reduceByKey((x,y)=>x+y).collect
res7: Array[(String, Int)] = Array((female,6), (male,7))
scala> 
```

###### 1.3.2.3.3.3 `groupByKey` Method
- 作用 : groupByKey也是对每个key进行操作,但只生成一个seq.
```
scala> rdd.groupByKey(2).collect
res8: Array[(String, Iterable[Int])] = Array((female,CompactBuffer(5, 1)), (male,CompactBuffer(5, 2)))

scala> 
```

###### 1.3.2.3.3.4 `reduceByKey`与`groupByKey` 区别
> 1.reduceByKey : 按照key进行聚合,在shuffle之前有combine(预聚合)操作,返回结果是RDD[k,v]
> 
> 2.groupByKey : 按照key进行分组,直接进行shuffle
> 
> 3.开发指导 : reduceByKey比groupByKey,建议使用reduceByKey,但是需要注意是否会影响业务逻辑.

###### 1.3.2.3.3.5 `aggregateByKey` Method
> 参数 : `(zeroValue:U,[partitioner:Partitioner])(seqOp: (U, V) => U,combOp: (U, U) => U)`
> 
> 1.作用 : 在kv对的RDD中,按key将value进行分组合并,合并时将每个value和初始值作为seq函数参数进行计算,返回结果作为一个新的kv对,然后再将结果按照key进行合并,最后将每个分组的value传递给combine函数进行计算(先将前两个value进行计算,将返回结果和下一个value传给combine函数,以此类推),将key与计算结果作为一个新的kv对输出.
> 
> 2.参数描述 : 
> `zeroValue` : 给每一个分区中的每一个key一个初始值.
> `seqOp` : 函数用于在每一个分区中用初始值逐步迭代value
> `combOp` : 函数用于合并每个分区中的结果

- 创建一个pairRDD,取出每个分区相同key对应值的最大值然后相加.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_014.jpg)

```
scala> val rdd = sc.parallelize(List(("a",3),("a",2),("c",4),("b",3),("c",6),("c",8)),2)
rdd: org.apache.spark.rdd.RDD[(String, Int)] = ParallelCollectionRDD[7] at parallelize at <console>:24

scala> rdd.aggregateByKey(0)(math.max(_,_),_+_).collect
res9: Array[(String, Int)] = Array((b,3), (a,3), (c,12))
scala> 
```
```
scala> rdd.aggregateByKey(0)(_+_,_+_).collect
res10: Array[(String, Int)] = Array((b,3), (a,5), (c,18))

scala> rdd.reduceByKey(_+_).collect
res11: Array[(String, Int)] = Array((b,3), (a,5), (c,18))
scala> 
```

###### 1.3.2.3.3.6 `foldByKey` Method
- 参数 : `(zeroValue: V)(func: (V, V) => V): RDD[(K, V)]`
- 作用 : `aggregateByKey`的简化操作,seqop和combop相同
```
scala> rdd.foldByKey(0)(_+_).collect
res12: Array[(String, Int)] = Array((b,3), (a,5), (c,18))
scala> 
```

###### 1.3.2.3.3.7 `combineByKey[C]` Method
- 参数 : `(createCombiner:V=>C,mergeValue:(C,V)=>C,mergeCombiners:(C,C)=>C) `
- 作用 : 针对相同K,将V合并成一个集合.

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_015.jpg)

- 参数描述 : 
> 1.`createCombiner:combineByKey()`会遍历分区中的所有元素,因此每个元素的键要么还没有遇到过,要么就和之前的某个元素的键相同。如果这是一个新的元素,combineByKey()会使用一个叫作createCombiner()函数来创建那个键对应的累加器初始值.
> 
> 2.`mergeValue` : 如果这是一个在处理当前分区之前已经遇到的键,它会使用mergeValue()方法将该键的累加器对应的当前值与这个新的值进行合并.
> 
> 3.`mergeCombiners` : 由于每个分区都是独立处理,因此对于同一个键可以有多个累加器,如果有两个或者更多的分区都有对应同一个键的累加器,就需要使用用户提供的mergeCombiners()方法将各个分区的结果进行合并.
```
scala> rdd.combineByKey((_,1),(acc:(Int,Int),v)=>(acc._1+v,acc._2+1),(acc1:(Int,Int),acc2:(Int,Int))=>(acc1._1+acc2._1,acc1._2+acc2._2)).collect
res15: Array[(String, (Int, Int))] = Array((b,(3,1)), (a,(5,2)), (c,(18,3)))    
scala> 
```

###### 1.3.2.3.3.8 `sortByKey([ascending],[numTasks])` Method
- 作用 : 在一个(K,V)的RDD上调用,K必须实现Ordered接口,返回一个按照key进行排序的(K,V)的RDD
```
scala>  rdd.sortByKey().collect
res17: Array[(String, Int)] = Array((a,3), (a,2), (b,3), (c,6), (c,8), (c,4))

scala> rdd.sortByKey(false).collect
res19: Array[(String, Int)] = Array((c,4), (c,6), (c,8), (b,3), (a,3), (a,2))
scala> 
```

###### 1.3.2.3.3.9 `mapValues` Method
- 针对于(K,V)形式的类型只对V进行操作
```
scala> rdd.mapValues(_*2).collect
res20: Array[(String, Int)] = Array((a,6), (a,4), (c,8), (b,6), (c,12), (c,16))
scala>
```

###### 1.3.2.3.3.10 `join(otherDataset,[numTasks])` Method
- 作用 : 在类型为(K,V)和(K,W)的RDD上调用,返回一个相同key对应的所有元素对在一起的(K,(V,W))的RDD
```
scala> val rdd = sc.parallelize(Array((1,"a"),(2,"b"),(3,"c")))
rdd: org.apache.spark.rdd.RDD[(Int, String)] = ParallelCollectionRDD[20] at parallelize at <console>:24

scala> val rdd1 = sc.parallelize(Array((1,4),(2,5),(3,6)))
rdd1: org.apache.spark.rdd.RDD[(Int, Int)] = ParallelCollectionRDD[21] at parallelize at <console>:24

scala> rdd.join(rdd1).collect
res21: Array[(Int, (String, Int))] = Array((1,(a,4)), (2,(b,5)), (3,(c,6))) 

scala> rdd.leftOuterJoin(rdd1).collect
res22: Array[(Int, (String, Option[Int]))] = Array((1,(a,Some(4))), (2,(b,Some(5))), (3,(c,Some(6))))

scala> rdd.rightOuterJoin(rdd1).collect
res23: Array[(Int, (Option[String], Int))] = Array((1,(Some(a),4)), (2,(Some(b),5)), (3,(Some(c),6)))
scala> 
```

###### 1.3.2.3.3.11 `cogroup(otherDataset,[numTasks])` Method
- 作用 : 在类型为(K,V)和(K,W)的RDD上调用,返回一个`(K,(Iterable<V>,Iterable<W>))`类型的RDD
```
scala> rdd.cogroup(rdd1).collect
res24: Array[(Int, (Iterable[String], Iterable[Int]))] = Array((1,(CompactBuffer(a),CompactBuffer(4))), (2,(CompactBuffer(b),CompactBuffer(5))), (3,(CompactBuffer(c),CompactBuffer(6))))

scala>
```

##### 1.3.2.4 Action
###### 1.3.2.4.1 `reduce(func)` Method
- 作用 : 通过func函数聚集RDD中的所有元素,先聚合分区内数据,再聚合分区间数据
```
scala> val rdd = sc.parallelize(1 to 10)
rdd: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[33] at parallelize at <console>:24

scala> rdd.reduce(_+_)
res25: Int = 55
scala>
```

###### 1.3.2.4.2 `collect()` Method
- 作用 : 在驱动程序中,以数组的形式返回数据集的所有元素
```
scala> rdd.collect
res26: Array[Int] = Array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
scala>
```

###### 1.3.2.4.3 `count()` Method
- 作用 : 返回RDD中元素的个数
```
scala> rdd.count
res27: Long = 10
scala> 
```

###### 1.3.2.4.4 `first()` Method
- 作用 : 返回RDD中第一个元素
```
scala> rdd.first
res28: Int = 1
scala> 
```

###### 1.3.2.4.5 `take(n)` Method
- 作用 : 返回一个由RDD前n个元素组成的数组
```
scala> rdd.take(2)
res30: Array[Int] = Array(1, 2)
scala> 
```

###### 1.3.2.4.6 `takeOrdered(n)` Method
- 作用 : 返回该RDD排序后的前n个元素组成的数组
```
scala> rdd.takeOrdered(3)
res31: Array[Int] = Array(1, 2, 3) 
scala> 
```

###### 1.3.2.4.7 `aggregate` Method
> 参数 : `(zeroValue: U)(seqOp: (U, T) ⇒U, combOp: (U, U) ⇒U)`
> 
> 作用 : aggregate函数将每个分区里面的元素通过seqOp和初始值进行聚合,然后用combine函数将每个分区的结果和初始值(zeroValue)进行combine操作,这个函数最终返回的类型不需要和RDD中元素类型一致.
```
scala> rdd.aggregate(0)(_+_,_+_)
res32: Int = 55
scala>
```

###### 1.3.2.4.8 `fold(num)(func)` Method
- 作用 : 折叠操作,aggregate的简化操作,seqop和combop一样
```
scala> rdd.fold(0)(_+_)
res34: Int = 55
scala> 
```

###### 1.3.2.4.9 `saveAsTextFile(path)` Method
- 作用 : 将数据集元素以textfile的形式保存到HDFS文件系统或者其他支持的文件系统,对于每个元素,Spark将会调用toString方法,将它装换为文件中的文本.

###### 1.3.2.4.10 `saveAsSequenceFile(path)` Method
- 作用 : 将数据集中的元素以Hadoop sequencefile格式保存到指定目录下,可以使HDFS或者其他Hadoop支持的文件系统.

###### 1.3.2.4.11 `saveAsObjectFile(path)` Method
- 作用 : 用于将RDD中元素序列化成对象,存储到文件中.

###### 1.3.2.4.12 `countByKey()` Method
- 作用 : 针对(K,V)类型RDD,返回一个(K,Int)的map,表示每一个key对应的元素个数.
```
scala> val rdd = sc.parallelize(List((1,3),(1,2),(1,4),(2,3),(3,6),(3,8)),3)
rdd: org.apache.spark.rdd.RDD[(Int, Int)] = ParallelCollectionRDD[35] at parallelize at <console>:24

scala> rdd.countByKey
res35: scala.collection.Map[Int,Long] = Map(3 -> 2, 1 -> 3, 2 -> 1)
scala> 
```

###### 1.3.2.4.13 `foreach(func)` Method
- 作用 : 在数据集的每一个元素上,运行函数func进行更新
```
scala> rdd.foreach(print)
```


##### 1.3.2.5 RDD 函数传递
> 在实际开发中往往需要开发者定义一些对于RDD操作,那么此时需要主要的是,初始化工作是在Driver端进行,而实际运行程序是在Executor端进行,这就涉及到了跨进程通信,跨进程通信是需要序列化操作.

###### 1.3.2.5.1 传递方法
> 在这个方法中所调用的方法`isMatch()`是定义在Search这个类中,实际上调用的是`this.isMatch()`,`this`表示Search这个类的对象,程序在运行过程中需要将Search对象序列化以后传递到Executor端.
###### 1.3.2.5.2 传递属性
> 在这个方法中所调用的方法`query`是定义在Search这个类中的字段,实际上调用的是`this.query`,this表示Search这个类的对象,程序在运行过程中需要将Search对象序列化以后传递到Executor端.

- Create `Search.scala`
``` scala
package com.geekparkhub.core.spark.application.methods
import org.apache.spark.rdd.RDD

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园枢纽
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * Search
  * <p>
  */

class Search(query: String) extends Serializable {

  // 过滤出包含字符串数据
  def isMatch(s: String): Boolean = {
    s.contains(query)
  }

  // 过滤出包含字符串RDD
  def getMatch1(rdd: RDD[String]): RDD[String] = {
    rdd.filter(isMatch)
  }

  // 过滤出包含字符串RDD
  def getMatche2(rdd: RDD[String]): RDD[String] = {
    rdd.filter(x => x.contains(query))
  }
}
```

- Create `TransFormAction.scala`
``` scala
package com.geekparkhub.core.spark.application.methods
import org.apache.spark.rdd.RDD
import org.apache.spark.{SparkConf, SparkContext}

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园枢纽
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * TransFormAction
  * <p>
  */

object TransFormAction {
  def main(args: Array[String]): Unit = {

    // 创建SpakConf
    val sparkConf: SparkConf = new SparkConf().setMaster("local[*]").setAppName("TransFormAction")

    // 创建SC
    val sc = new SparkContext(sparkConf)

    // 创建RDD
    val word: RDD[String] = sc.parallelize(Array("abc", "dcd"))

    // 创建Search对象
    val search = new Search("a")

    // 调用方法
    val searched: RDD[String] = search.getMatch1(word)

    // 循环输出
    searched.collect().foreach(println)

    // 关闭资源
    sc.stop()
  }
}
```

##### 1.3.2.6 RDD 依赖关系
###### 1.3.2.6.1 Lineage
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_016.jpg)

> RDD只支持粗粒度转换,即在大量记录上执行的单个操作,将创建RDD的一系列Lineage(血统)记录下来,以便恢复丢失的分区,RDD的Lineage会记录RDD的元数据信息和转换行为,当该RDD的部分分区数据丢失时,它可以根据这些信息来重新运算和恢复丢失的数据分区.

- 创建RDD依赖关系
```
scala> sc.textFile("/core_flow/spark/input/wordcount/wordcount_001.txt")
res0: org.apache.spark.rdd.RDD[String] = /core_flow/spark/input/wordcount/wordcount_001.txt MapPartitionsRDD[1] at textFile at <console>:25

scala> res0.flatMap(_.split(" "))
res2: org.apache.spark.rdd.RDD[String] = MapPartitionsRDD[2] at flatMap at <console>:27

scala> res2.map((_,1))
res3: org.apache.spark.rdd.RDD[(String, Int)] = MapPartitionsRDD[3] at map at <console>:29

scala> res3.reduceByKey(_+_)
res4: org.apache.spark.rdd.RDD[(String, Int)] = ShuffledRDD[4] at reduceByKey at <console>:31

scala>
```
- 分别查看四个RDD依赖关系
- res0.toDebugString
```
scala> res0.toDebugString
res5: String =
(2) /core_flow/spark/input/wordcount/wordcount_001.txt MapPartitionsRDD[1] at textFile at <console>:25 []
 |  /core_flow/spark/input/wordcount/wordcount_001.txt HadoopRDD[0] at textFile at <console>:25 []
scala> 
```
- res2.toDebugString
```
scala> res2.toDebugString
res6: String =
(2) MapPartitionsRDD[2] at flatMap at <console>:27 []
 |  /core_flow/spark/input/wordcount/wordcount_001.txt MapPartitionsRDD[1] at textFile at <console>:25 []
 |  /core_flow/spark/input/wordcount/wordcount_001.txt HadoopRDD[0] at textFile at <console>:25 []
scala> 
```
- res3.toDebugString
```
scala> res3.toDebugString
res7: String =
(2) MapPartitionsRDD[3] at map at <console>:29 []
 |  MapPartitionsRDD[2] at flatMap at <console>:27 []
 |  /core_flow/spark/input/wordcount/wordcount_001.txt MapPartitionsRDD[1] at textFile at <console>:25 []
 |  /core_flow/spark/input/wordcount/wordcount_001.txt HadoopRDD[0] at textFile at <console>:25 []
scala> 
```
- res4.toDebugString
```
scala> res4.toDebugString
res8: String =
(2) ShuffledRDD[4] at reduceByKey at <console>:31 []
 +-(2) MapPartitionsRDD[3] at map at <console>:29 []
    |  MapPartitionsRDD[2] at flatMap at <console>:27 []
    |  /core_flow/spark/input/wordcount/wordcount_001.txt MapPartitionsRDD[1] at textFile at <console>:25 []
    |  /core_flow/spark/input/wordcount/wordcount_001.txt HadoopRDD[0] at textFile at <console>:25 []
scala> 
```
###### 1.3.2.6.2 窄依赖
- 窄依赖指的是每一个父RDD的Partition最多被子RDD的一个Partition使用.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_017.jpg)


###### 1.3.2.6.3 宽依赖
- 宽依赖指的是多个子RDD的Partition会依赖同一个父RDD的Partition,会引起shuffle过程.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_018.jpg)

###### 1.3.2.6.4 DAG
- DAG(Directed Acyclic Graph)叫做有向无环图,原始的RDD通过一系列的转换就就形成了DAG,根据RDD之间的依赖关系的不同将DAG划分成不同的Stage.
- 对于窄依赖,partition的转换处理在Stage中完成计算,对于宽依赖,由于有Shuffle的存在,只能在parent RDD处理完成后,才能开始接下来的计算,因此宽依赖是划分Stage依据.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_019.jpg)


###### 1.3.2.6.5 任务划分(重点)
- RDD任务切分中间分为 : `Application` / `Job` / `Stage` /  `Task`
- Application : 初始化一个SparkContext即生成一个Application.
- Job : 一个Action算子就会生成一个Job.
- Stage : 根据RDD之间的依赖关系的不同将Job划分成不同的Stage,遇到一个宽依赖则划分一个Stage.
- Task : Stage是一个TaskSet,将Stage划分的结果发送到不同的Executor执行即为一个Task.
- Application`->`Job`->`Stage`->`Task 每一层都是1对n的关系

##### 1.3.2.6.7 RDD缓存
- RDD通过persist方法或cache方法可以将前面的计算结果缓存,默认情况下`persist()`会把数据以序列化形式缓存在JVM 的堆空间中.
- 但是并不是这两个方法被调用时立即缓存,而是触发后面的action时,该RDD将会被缓存在计算节点的内存中,并供后面重用
- 缓存有可能丢失或者存储存储于内存的数据由于内存不足而被删除,RDD的缓存容错机制保证了即使缓存丢失也能保证计算的正确执行,通过基于RDD的一系列转换,丢失的数据会被重算,由于RDD的各个Partition是相对独立,因此只需要计算丢失的部分即可,并不需要重算全部Partition.

##### 1.3.2.6.8 RDDCheckPoint
- Spark中对于数据的保存除了持久化操作之外,还提供了一种检查点的机制,检查点(本质是通过将RDD写入Disk做检查点)是为了通过lineage做容错的辅助,lineage过长会造成容错成本过高,这样就不如在中间阶段做检查点容错,如果之后有节点出现问题而丢失分区,从做检查点的RDD开始重做Lineage,就会减少开销,检查点通过将数据写入到HDFS文件系统实现了RDD的检查点功能.
- 为当前RDD设置检查点,该函数将会创建一个二进制的文件,并存储到checkpoint目录中,该目录是用SparkContext.setCheckpointDir()设置的,在checkpoint的过程中,该RDD所有依赖于父RDD中的信息将全部被移除,对RDD进行checkpoint操作并不会马上被执行,必须执行Action操作才能触发.
- 设置检查点
```
scala> sc.setCheckpointDir("hdfs://systemhub511:9000/core_flow/spark/checkpoint")
```
- 创建RDD
```
scala>  val rdd = sc.parallelize(Array("systemhub511"))
rdd: org.apache.spark.rdd.RDD[String] = ParallelCollectionRDD[5] at parallelize at <console>:24
```
- 将RDD转换为携带当前时间戳并做checkpoint
```
scala> val check = rdd.map(_+System.currentTimeMillis)
check: org.apache.spark.rdd.RDD[String] = MapPartitionsRDD[6] at map at <console>:26
scala> 
```
- 多次打印结果
```
scala> check.collect
res10: Array[String] = Array(systemhub5111559138263898)

scala> check.collect
res11: Array[String] = Array(systemhub5111559138266443)

scala> check.collect
res12: Array[String] = Array(systemhub5111559138267862)

scala> 
```

#### 1.3.3 Key-Value RDD 数据分区
- Spark目前支持Hash分区和Range分区,开发者也可以自定义分区,Hash分区为当前默认分区,Spark中分区器直接决定了RDD中分区的个数、RDD中每条数据经过Shuffle过程属于哪个分区和Reduce的个数.

##### 1.3.3.1 获取RDD 分区
- 查看RDD分区器
```
scala> rdd.partitioner
res14: Option[org.apache.spark.Partitioner] = None
```
##### 1.3.3.2 Hash 分区
- HashPartitioner分区的原理 : 对于给定的key,计算其hashCode,并除以分区个数取余,如果余数小于0,则用余数+分区的个数,否则加0,最后返回的值就是这个key所属的分区ID.
- Hash分区实操
```
scala> val nopar = sc.parallelize(List((1,3),(1,2),(2,4),(2,3),(3,6),(3,8)),8)
nopar: org.apache.spark.rdd.RDD[(Int, Int)] = ParallelCollectionRDD[7] at parallelize at <console>:25

scala> nopar.mapPartitionsWithIndex((index,iter)=>{Iterator(index.toString+":"+iter.mkString("|"))}).collect
res15: Array[String] = Array(0:, 1:(1,3), 2:(1,2), 3:(2,4), 4:, 5:(2,3), 6:(3,6), 7:(3,8))

scala> val hashpar = nopar.partitionBy(new org.apache.spark.HashPartitioner(7))
hashpar: org.apache.spark.rdd.RDD[(Int, Int)] = ShuffledRDD[9] at partitionBy at <console>:27

scala> hashpar.count
res20: Long = 6

scala> hashpar.partitioner
res21: Option[org.apache.spark.Partitioner] = Some(org.apache.spark.HashPartitioner@7)

scala> hashpar.mapPartitions(iter => Iterator(iter.length)).collect()
res22: Array[Int] = Array(0, 2, 2, 2, 0, 0, 0)
scala> 
```

##### 1.3.3.3 Ranger 分区
- HashPartitioner分区`弊端` : 可能导致每个分区中数据量不均匀,极端情况下会导致某些分区拥有RDD全部数据.
- RangePartitioner作用 : 将一定范围内数映射到某一个分区内,尽量保证每个分区中数据量均匀,而且分区与分区之间是有序,一个分区中元素肯定都是比另一个分区内元素小或者大,但是分区内元素是不能保证顺序,简单的说就是将一定范围内的数映射到某一个分区内.
- 实现过程 : 
- 1.先从整个RDD中抽取出样本数据,将样本数据排序,计算出每个分区最大key值,形成一个`Array[KEY]`类型的数组变量`rangeBounds`.
- 2.判断key在`rangeBounds`中所处的范围,给出该key值在下一个RDD中分区id下标,该分区器要求RDD中KEY类型必须是可排序.


##### 1.3.3.4 自定义 分区
- 要实现自定义分区器,需要继承`org.apache.spark.Partitioner`类并实现下面三个方法
- 1.`numPartitions: Int` : 返回创建出来的分区数
- 2.`getPartition(key: Any): Int` :  返回给定键的分区编号(0到numPartitions-1)
- 3.`equals()` : Java 判断相等性的标准方法,这个方法的实现非常重要,Spark需要用这个方法来检查分区器对象是否和其他分区器实例相同,这样Spark才可以判断两个RDD的分区方式是否相同.
- 4.定义自定义分区类 | Create `CustomerPartitioner.scala`
``` scala
package com.geekparkhub.core.spark.application.partitioner

import org.apache.spark.Partitioner

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园枢纽
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * CustomerPartitioner
  * <p>
  */

class CustomerPartitioner(partitions: Int) extends Partitioner {
  override def numPartitions: Int = partitions
  override def getPartition(key: Any): Int = {
    0
  }
}
```
- Create `PartitionerAction.scala`
```
package com.geekparkhub.core.spark.application.partitioner

import org.apache.spark.rdd.RDD
import org.apache.spark.{SparkConf, SparkContext}

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园枢纽
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * PartitionerAction
  * <p>
  */

object PartitionerAction {

  def main(args: Array[String]): Unit = {
    // 创建SpakConf
    val sparkConf: SparkConf = new SparkConf().setMaster("local[*]").setAppName("TransFormAction")

    // 创建SC
    val sc = new SparkContext(sparkConf)

    // 创建RDD
    val word: RDD[String] = sc.parallelize(Array("abc", "dcd"))

    // 将元素转换为元祖
    val wordAndOne: RDD[(String, Int)] = word.map((_, 1))

    // 自定义分区
    val partitioned: RDD[(String, Int)] = wordAndOne.partitionBy(new CustomerPartitioner(2))

    // 查看分区后分区结果
    val indexAndData: RDD[(Int, (String, Int))] = partitioned.mapPartitionsWithIndex((i,t)=>t.map((i,_)))

    // 打印数据
    indexAndData.collect().foreach(println)

    // 关闭资源
    sc.stop()
  }
}
```
- Log Println
```
(0,(abc,1))
(0,(dcd,1))
```

#### 1.3.4 数据读取&保存
- Spark数据读取及数据保存可以从两个维度来作区分 : 文件格式以及文件系统
- 文件格式分为 : Text文件 / Json文件 / Csv文件 / Sequence文件以及Object文件
- 文件系统分为 : 本地文件系统 / HDFS / HBASE以及数据库

##### 1.3.4.1 文件类数据读取&保存
###### 1.3.4.1 Text File
- 1.数据读取 : `textFile(String)` 
```
scala> sc.textFile("hdfs://systemhub511:9000/core_flow/spark/input/wordcount/wordcount_001.txt")
res23: org.apache.spark.rdd.RDD[String] = hdfs://systemhub511:9000/core_flow/spark/input/wordcount/wordcount_001.txt MapPartitionsRDD[12] at textFile at <console>:26

scala> res23.toDebugString
res25: String =
(2) hdfs://systemhub511:9000/core_flow/spark/input/wordcount/wordcount_001.txt MapPartitionsRDD[12] at textFile at <console>:26 []
 |  hdfs://systemhub511:9000/core_flow/spark/input/wordcount/wordcount_001.txt HadoopRDD[11] at textFile at <console>:26 []
scala> 
```
- 2.数据保存 : `saveAsTextFile(String)`
```
scala> hdfsFile.saveAsTextFile("/core_flow/spark/output/wordcount/")
```

###### 1.3.4.2 Json File
- 如果JSON文件中每一行就是一个JSON记录,那么可以通过将JSON文件当做文本文件来读取,然后利用相关的JSON库对每一条数据进行JSON解析.
- 使用RDD读取JSON文件处理很复杂,同时SparkSQL集成了很好的处理JSON文件方式,所以应用中多是采用SparkSQL处理JSON文件.
- 1.导入解析json所需包名
```
scala> import scala.util.parsing.json.JSON
import scala.util.parsing.json.JSON
scala> 
```
- 2.在HDFS创建存放JSON目录
```
[root@systemhub511 ~]# hadoop fs -mkdir -p /core_flow/spark/json/001
```
- 3.上传json文件到HDFS
```
[root@systemhub511 ~]# hadoop fs -put /opt/module/spark/examples/src/main/resources/people.json /core_flow/spark/json/001/
```
- 4.读取文件
```
scala> val json = sc.textFile("hdfs://systemhub511:9000/core_flow/spark/json/001/people.json")
json: org.apache.spark.rdd.RDD[String] = hdfs://systemhub511:9000/core_flow/spark/json/001/people.json MapPartitionsRDD[14] at textFile at <console>:26
scala>
```
- 5.解析json数据
```
scala> val result = json.map(JSON.parseFull)
result: org.apache.spark.rdd.RDD[Option[Any]] = MapPartitionsRDD[15] at map at <console>:28
scala>
```
- 6.打印解析结果
```
scala> result.collect
res26: Array[Option[Any]] = Array(Some(Map(name -> Michael)), Some(Map(name -> Andy, age -> 30.0)), Some(Map(name -> Justin, age -> 19.0)))
scala> 
```

###### 1.3.4.3 Sequence File
- SequenceFile文件是Hadoop用来存储二进制形式的key-value对而设计一种平面文件(FlatFile).
- Spark有专门用来读取SequenceFile接口,在SparkContext中,可以调用`sequenceFile[keyClass, valueClass](path)` | SequenceFile文件只针对`PairRDD`
- 1.创建RDD
```
scala>  val rdd = sc.parallelize(Array((1,2),(3,4),(5,6)))
rdd: org.apache.spark.rdd.RDD[(Int, Int)] = ParallelCollectionRDD[16] at parallelize at <console>:26
scala> 
```
- 2.将RDD保存为Sequence文件
```
scala> rdd.saveAsSequenceFile("file:///opt/module/spark/seqFile")
```
- 3.查看该文件
```
[root@systemhub511 ~]# cd /opt/module/spark/seqFile/
[root@systemhub511 seqFile]# ll -a
总用量 28
drwxr-xr-x.  2 root          root          4096 5月  29 23:57 .
drwxr-xr-x. 21 geekdeveloper geekdeveloper 4096 5月  30 00:05 ..
-rw-r--r--.  1 root          root            92 5月  29 23:57 part-00000
-rw-r--r--.  1 root          root            12 5月  29 23:57 .part-00000.crc
-rw-r--r--.  1 root          root           108 5月  29 23:57 part-00003
-rw-r--r--.  1 root          root            12 5月  29 23:57 .part-00003.crc
-rw-r--r--.  1 root          root             0 5月  29 23:57 _SUCCESS
-rw-r--r--.  1 root          root             8 5月  29 23:57 ._SUCCESS.crc
[root@systemhub511 seqFile]# cat part-00000
SEQ org.apache.hadoop.io.IntWritable org.apache.hadoop.io.IntWritabler[-o���]h�~u���
[root@systemhub511 seqFile]#
```
- 4.读取Sequence文件
```
scala>  val seq = sc.sequenceFile[Int,Int]("file:///opt/module/spark/seqFile")
seq: org.apache.spark.rdd.RDD[(Int, Int)] = MapPartitionsRDD[19] at sequenceFile at <console>:26
scala>
```
- 5.打印读取后的Sequence文件
```
scala> seq.collect
res14: Array[(Int, Int)] = Array((1,2), (3,4), (5,6))
```

###### 1.3.4.4 ObjectFile
- 对象文件是将对象序列化后保存文件,采用Java序列化机制,可以通过`objectFile[k,v](path)`函数接收一个路径,读取对象文件,返回对应RDD,也可以通过调用`saveAsObjectFile()`实现对对象文件输出,因为是序列化所以要指定类型.
- 1.创建RDD
```
scala> val rdd = sc.parallelize(Array(1,2,3,4))
rdd: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[20] at parallelize at <console>:26
scala> 
```
- 2.将RDD保存为Object文件
```
scala> rdd.saveAsObjectFile("file:///opt/module/spark/objectFile")
```
- 3.查看该文件
```
[root@systemhub511 ~]# cd /opt/module/spark/objectFile/
[root@systemhub511 objectFile]# ll
总用量 8
-rw-r--r--. 1 root root 138 5月  30 00:05 part-00000
-rw-r--r--. 1 root root 138 5月  30 00:05 part-00003
-rw-r--r--. 1 root root   0 5月  30 00:05 _SUCCESS
[root@systemhub511 objectFile]# cat part-00000
SEQ!org.apache.hadoop.io.NullWritable"org.apache.hadoop.io.BytesWritable� �L�h�l:T���#��ur[IM�`&v겥xp
[root@systemhub511 objectFile]#
```
- 4.读取Object文件
```
scala> val objFile = sc.objectFile[(Int)]("file:///opt/module/spark/objectFile")
objFile: org.apache.spark.rdd.RDD[Int] = MapPartitionsRDD[24] at objectFile at <console>:26
scala>
```
- 5.打印读取后的Sequence文件
```
objFile.collect
res19: Array[Int] = Array(1, 2, 3, 4)
```

##### 1.3.4.2 文件系统数据读取&保存

###### 1.3.4.1 HDFS
> Spark整个生态系统与Hadoop是完全兼容,所以对于Hadoop所支持的文件类型或者数据库类型,Spark也同样支持.
> 另外由于Hadoop的API有新旧两个版本,所以Spark为了能够兼容Hadoop所有版本,也提供了两套创建操作接口.
> 对于外部存储创建操作而言,hadoopRDD和newHadoopRDD是最为抽象的两个函数接口,主要包含以下四个参数  : 
> 
> 1.`输入格式(InputFormat)` : 制定数据输入类型,如TextInputFormat等,新旧两个版本所引用版本分别是`org.apache.hadoop.mapred.InputFormat`和`org.apache.hadoop.mapreduce.InputFormat(NewInputFormat)`
> 2.键类型 : 指定[K,V]键值对中K类型
> 3.值类型: 指定[K,V]键值对中V类型
> 4.分区值 : 指定由外部存储生成RDD的partition数量最小值,如果没有指定系统会使用默认值`defaultMinSplits`.
> 
> 其他创建操作API接口都是为了方便最终Spark程序开发者而设置的,是这两个接口高效实现版本,例如对于textFile而言,只有path这个指定文件路径参数,其他参数在系统内部指定了默认值.
> 1.在Hadoop中以压缩形式存储数据,不需要指定解压方式就能够进行读取,因为Hadoop本身有一个解压器会根据压缩文件后缀推断解压算法进行解压.
> 2.如果用Spark从Hadoop中读取某种类型数据不知道怎么读取的时候,上网查找一个使用map-reduce时候是怎么读取这种这种数据,然后再将对应的读取方式改写成上面的hadoopRDD和newAPIHadoopRDD两个类即可.


###### 1.3.4.2 MySQL数据库 连接
- 支持通过JavaJDBC访问关系型数据库,需要通过JdbcRDD进行
- 0.添加mysql依赖
``` xml
<dependencies>
 <dependency>
  <groupId>mysql</groupId>
  <artifactId>mysql-connector-java</artifactId>
  <version>8.0.15</version>
 </dependency>
</dependencies>
```
- 1.Mysql读取 | Create `JDBCConnection.scala`
``` scala
package com.geekparkhub.core.spark.application.dataconnections

import java.sql.DriverManager

import org.apache.spark.deploy.worker.DriverWrapper
import org.apache.spark.rdd.JdbcRDD
import org.apache.spark.{SparkConf, SparkContext}

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园枢纽
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * JDBCConnection
  * <p>
  */

object JDBCConnection {

  def main(args: Array[String]): Unit = {

    // 创建SpakConf
    val sparkConf: SparkConf = new SparkConf().setMaster("local[*]").setAppName("JDBCConnection")

    // 创建SC
    val sc = new SparkContext(sparkConf)

    // 定义JDBC连接属性信息
    val driver = "com.mysql.jdbc.Driver"
    val url = "jdbc:mysql://systemhub711:3306/company"
    val userName = "root"
    val passWd = "ax04854"

    // 创建JDBC RDD
    val JdbcRDD = new JdbcRDD[(Int, String)](sc, () => {
      Class.forName(driver)
      DriverManager.getConnection(url, userName, passWd)
    }, "select id,name from staff where ? <= id and id <= ?",
      1,
      10,
      1,
      x => {
        (x.getInt(1), x.getString(2))
      }
    )

    // 打印JdbcRDD结果
    JdbcRDD.collect().foreach(println)

    // 关闭资源
    sc.stop()
  }
}
```
- 2.Mysql写入 | Create `JBDCinsertData.scala`
``` scala
package com.geekparkhub.core.spark.application.dataconnections

import org.apache.spark.{SparkConf, SparkContext}

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园枢纽
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * JBDCinsertData
  * <p>
  */

object JBDCinsertData {
  def main(args: Array[String]): Unit = {

    // 创建SpakConf
    val sparkConf: SparkConf = new SparkConf().setMaster("local[*]").setAppName("JBDCRead")

    // 创建SC
    val sc = new SparkContext(sparkConf)

    // 创建数据
    val data = sc.parallelize(List("Female", "Male", "Female"))

    // 调用添加数据方法
    data.foreachPartition(insertData)
  }

  // 添加数据方法
  def insertData(iterator: Iterator[String]): Unit = {
    Class.forName("com.mysql.jdbc.Driver").newInstance()
    val conn = java.sql.DriverManager.getConnection("jdbc:mysql://systemhub711:3306/company", "root", "000000")
    iterator.foreach(data => {
      val ps = conn.prepareStatement("insert into staff(name) values(?)")
      ps.setString(1, data)
      ps.executeUpdate()
    })
  }
}
```


###### 1.3.4.3 HBase 数据库
- 由于`org.apache.hadoop.hbase.mapreduce.TableInputFormat`类的实现,Spark可以通过Hadoop输入格式访问HBase,这个输入格式会返回键值对数据,其中键的类型为`org. apache.hadoop.hbase.io.ImmutableBytesWritable`,而值的类型为`org.apache.hadoop.hbase.client.Result`.
- 0.添加HBASE依赖
```xml
<dependency>
  <groupId>org.apache.hbase</groupId>
  <artifactId>hbase-server</artifactId>
  <version>1.3.1</version>
</dependency>
<dependency>
  <groupId>org.apache.hbase</groupId>
  <artifactId>hbase-client</artifactId>
  <version>1.3.1</version>
</dependency>
```
- 1.HBase读取数据
``` scala
package com.geekparkhub.core.spark.application.dataconnections

import org.apache.hadoop.conf.Configuration
import org.apache.hadoop.hbase.HBaseConfiguration
import org.apache.hadoop.hbase.client.Result
import org.apache.hadoop.hbase.io.ImmutableBytesWritable
import org.apache.hadoop.hbase.mapreduce.TableInputFormat
import org.apache.hadoop.hbase.util.Bytes
import org.apache.spark.rdd.{NewHadoopRDD, RDD}
import org.apache.spark.{SparkConf, SparkContext}

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园枢纽
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * HbaseConnection
  * <p>
  */

object HbaseConnection {
  def main(args: Array[String]): Unit = {

    // 创建SpakConf
    val sparkConf: SparkConf = new SparkConf().setMaster("local[*]").setAppName("HbaseConnection")

    // 创建SC
    val sc = new SparkContext(sparkConf)

    //构建HBase配置信息
    val conf: Configuration = HBaseConfiguration.create()
    conf.set("hbase.zookeeper.quorum", "systemhub511,systemhub611,systemhub711")
    conf.set(TableInputFormat.INPUT_TABLE, "test")

    // 读取HBASE数据
    val hbaseRDD = new NewHadoopRDD(sc, classOf[TableInputFormat], classOf[ImmutableBytesWritable], classOf[Result], conf)

    // 获取RowKey
    val value: RDD[String] = hbaseRDD.map(x => Bytes.toString(x._2.getRow))

    // 输出数据
    value.collect().foreach(println)

    // 关闭资源
    sc.stop()
  }
}
```

- 2.HBase写入数据
``` scala
package com.geekparkhub.core.spark.application.dataconnections

import org.apache.hadoop.hbase.client.Put
import org.apache.hadoop.hbase.io.ImmutableBytesWritable
import org.apache.hadoop.hbase.mapred.TableOutputFormat
import org.apache.hadoop.hbase.util.Bytes
import org.apache.hadoop.mapred.JobConf
import org.apache.spark.rdd.RDD
import org.apache.spark.{SparkConf, SparkContext}

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园枢纽
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * HbaseWrite
  * <p>
  */

object HbaseWrite {
  def main(args: Array[String]): Unit = {

    // 创建SpakConf
    val sparkConf: SparkConf = new SparkConf().setMaster("local[*]").setAppName("HbaseWrite")

    // 创建SC
    val sc = new SparkContext(sparkConf)

    // 创建RDD
    val initialRDD: RDD[(Int, String, Int)] = sc.parallelize(List((1, "apple", 11), (2, "banana", 12), (3, "pear", 13)))

    // 创建JobConf
    val conf = new JobConf()
    conf.set("hbase.zookeeper.quorum", "systemhub511,systemhub611,systemhub711")
    conf.setOutputFormat(classOf[TableOutputFormat[ImmutableBytesWritable]])
    conf.set(TableOutputFormat.OUTPUT_TABLE, "test")

    // 定义 Hbase 添加数据方法
    def convert(triple: (Int, String, Int)): (ImmutableBytesWritable, Put) = {
      val put = new Put(Bytes.toBytes(triple._1))
      put.addImmutable(Bytes.toBytes("info"), Bytes.toBytes("name"), Bytes.toBytes(triple._2))
      put.addImmutable(Bytes.toBytes("info"), Bytes.toBytes("price"), Bytes.toBytes(triple._3))(new ImmutableBytesWritable, put)
    }

    // 转换RDD
    val writRDD: RDD[(ImmutableBytesWritable, Put)] = initialRDD.map(convert)

    // 写入HBASE
    writRDD.saveAsHadoopDataset(conf)

    // 关闭资源
    sc.stop()
  }
}
```

#### 1.3.5 RDD 编程进阶
##### 1.3.5.1 累加器
> 累加器用来对信息进行聚合,通常在向Spark传递函数时,比如使用`map()`函数或者用`filter()`传条件时,可以使用驱动器程序中定义变量,但是集群中运行每个任务都会得到这些变量的一份新副本,更新这些副本的值也不会影响驱动器中的对应变量,如果想实现所有分片处理时更新共享变量的功能,那么累加器可以实现想要的效果.

###### 1.3.5.1.1 系统累加器
> 通过在驱动器中调用S`parkContext.accumulator(initialValue`)方法,创建出存有初始值的累加器,返回值为`org.apache.spark.Accumulator[T]`对象,其中T是初始值initialValue的类型,Spark闭包里的执行器代码可以使用累加器的`+=`方法(在Java中是add)增加累加器的值,驱动器程序可以调用累加器的value属性(在Java中使用value()或setValue())来访问累加器的值.
> 
> 工作节点上任务不能访问累加器值,从这些任务的角度来看,累加器是一个只写变量.
> 
> 对于要在行动操作中使用累加器,Spark只会把每个任务对各累加器的修改应用一次,因此,如果想要一个无论在失败还是重复计算时都绝对可靠的累加器,必须把它放在foreach()这样的行动操作中,转化操作中累加器可能会发生不止一次更新.
``` scala
package com.geekparkhub.core.spark.application.methods

import org.apache.spark.rdd.RDD
import org.apache.spark.util.LongAccumulator
import org.apache.spark.{SparkConf, SparkContext}

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园枢纽
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * AccuAction
  * <p>
  */

object AccuAction {
  def main(args: Array[String]): Unit = {

    // 创建SpakConf
    val sparkConf: SparkConf = new SparkConf().setMaster("local[*]").setAppName("AccuAction")

    // 创建SC
    val sc = new SparkContext(sparkConf)

    // 累加器
    val sum: LongAccumulator = sc.longAccumulator("sum")

    // 创建RDD
    val value: RDD[Int] = sc.parallelize(Array(1, 2, 3, 4))

    val word: RDD[(Int, Int)] = value.map(x => {
      // 添加累加
      sum.add(x)
      (x, 1)
    })

    word.collect().foreach(println)

    println(sum.value)

    // 关闭资源
    sc.stop()
  }
}
```
###### 1.3.5.1.2 自定义累加器
> 自定义累加器类型功能在1.X版本中就已经提供,但是使用起来比较麻烦,在2.0版本后,累加器的易用性有了较大改进,而且官方还提供了一个新抽象类 : `AccumulatorV2`来提供更加友好自定义类型累加器的实现方式,实现自定义类型累加器需要继承`AccumulatorV2`并至少覆写下例中出现的方法,
``` scala
package com.geekparkhub.core.spark.application.methods

import org.apache.spark.util.AccumulatorV2

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园枢纽
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * AccumulatorAction
  * <p>
  */

class AccumulatorAction extends AccumulatorV2[Int,Int]{

  var sum  = 0

  // 判断是否为空
  override def isZero: Boolean = sum == 0

  // 复制方法
  override def copy(): AccumulatorV2[Int, Int] = {
    val accumulatorAction = new AccumulatorAction
    accumulatorAction.sum = this.sum
    accumulatorAction
  }

  // 重置方法
  override def reset(): Unit = 0

  // 累加方法
  override def add(v: Int): Unit = sum += v

  // 合并方法
  override def merge(other: AccumulatorV2[Int, Int]): Unit = sum += other.value

  // 返回值
  override def value: Int = sum
}
```

##### 1.3.5.2 广播变量 (调优策略)
> 广播变量用来高效分发较大对象,向所有工作节点发送一个较大的只读值,以供一个或多个Spark操作使用.
> 
> 比如,如果应用需要向所有节点发送一个较大的只读查询表,甚至是机器学习算法中的一个很大的特征向量,广播变量用起来都很顺手,在多个并行操作中使用同一个变量,但是Spark会为每个任务分别发送.
> 
> 使用广播变量过程 : 
> 1.通过对一个类型T的对象调用`SparkContext.broadcast`创建出`Broadcast[T]`对象,任何可序列化类型都可以这么实现.
> 2.通过value属性访问该对象值(在Java中为`value()`方法).
> 3.变量只会被发到各个节点一次,应作为只读值处理(修改这个值不会影响到别的节点).
```
scala> val broadcastVar = sc.broadcast(Array(1, 2, 3))
broadcastVar: org.apache.spark.broadcast.Broadcast[Array[Int]] = Broadcast(0)

scala> broadcastVar.value
res0: Array[Int] = Array(1, 2, 3)

scala> 
```


### 🔥 1.4 Spark SQL 🔥
#### 1.4.1 Spark SQL 概述
##### 1.4.1.1 什么是 Spark SQL
> Spark SQL是Spark用来处理结构化数据模块,它提供了2个编程抽象 : `DataFrame`和`DataSet`,并且作为分布式SQL查询引擎作用.
> 
> 已经学习了Hive,它是将Hive SQL转换成MapReduce然后提交到集群上执行,大大简化了编写MapReduc程序复杂性,由于MapReduce计算模型执行效率比较慢,所以Spark SQL应运而生,它是将Spark SQL转换成RDD,然后提交到集群执行,执行效率非常快.

##### 1.4.1.2 Spark SQL 特点
- 易整合
- 统一数据访问方式
- 兼容Hive
- 标准数据连接

##### 1.4.1.3 什么是 DataFrame
> 与RDD类似,DataFrame也是一个分布式数据容器,然而DataFrame更像传统数据库的二维表格,除了数据以外,还记录数据的结构信息,即schema,同时与Hive类似,DataFrame也支持嵌套数据类型(struct / array / map).
> 
> 从API易用性角度上看,DataFrame API提供是一套高层的关系操作,比函数式RDD API要更加友好,门槛更低.

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_020.jpg)
> 上图直观地体现了DataFrame和RDD区别,左侧RDD[Person]虽然以Person为类型参数,但Spark框架本身不了解Person类内部结构,而右侧DataFrame却提供了详细的结构信息,使得Spark SQL可以清楚地知道该数据集中包含哪些列,每列名称和类型各是什么,DataFrame是为数据提供了Schema视图,可以把它当做数据库中一张数据表.
> 
> DataFrame也是懒执行,性能上比RDD要高要原因 : 优化执行计划,查询计划通过Spark `catalyst optimiser`进行优化.

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_021.jpg)
> 为了说明查询优化,上图展示的人口数据分析示例,图中构造了两个DataFrame,将它们join之后又做了一次filter操作,如果原封不动地执行这个执行计划,最终的执行效率是不高的,因为join是一个代价较大操作,也可能会产生一个较大数据集,如果能将filter下推到join下方,先对DataFrame进行过滤,再join过滤后的较小的结果集,便可以有效缩短执行时间.
> 而Spark SQL的查询优化器正是这样做的,简而言之逻辑查询计划优化就是一个利用基于关系代数的等价变换,将高成本的操作替换为低成本操作的过程.

##### 1.4.1.4 什么是 DataSet
> 1.DataSet是DataframeAPI扩展,是SparkSQL最新数据抽象.
> 
> 2.友好API风格,既具有类型安全检查也具有Dataframe的查询优化特性.
> 
> 3.Dataset支持编解码器,当需要访问非堆上的数据时可以避免反序列化整个对象,提高了效率.
> 
> 4.样例类被用来在Dataset中定义数据结构信息,样例类中每个属性的名称直接映射到DataSet中的字段名称.
> 
> 5.Dataframe是Dataset的特列,`DataFrame=Dataset[Row]`,所以可以通过as方法将Dataframe转换为Dataset,Row是一个类型,跟Car / Person这些类型一样,所有表结构信息都用Row来表示.
> 
> 6.DataSet是强类型,比如可以有`Dataset[Car]`,`Dataset[Person]`.
> 
> 7.DataFrame只是知道字段,但是不知道字段类型,所以在执行这些操作时是没办法在编译的时候检查是否类型失败,比如可以对一个String进行减法操作,在执行时才报错,而DataSet不仅仅知道字段,而且知道字段类型,所以有更严格的错误检查,就跟JSON对象和类对象之间的类比.



#### 1.4.2 Spark SQL 编程
##### 1.4.2.1 SparkSession 新起始点
> 在老版本中,SparkSQL提供两种SQL查询起始点 : 
> SQLContext : 用于Spark提供SQL查询.
> HiveContext : 用于连接Hive查询.
> 
> SparkSession是Spark最新SQL查询起始点,实质上是SQLContext和HiveContext组合,所以在SQLContext和HiveContext上可用API在SparkSession上同样是可以使用,SparkSession内部封装了`sparkContext`,所以计算实际上是由sparkContext完成.

##### 1.4.2.2 DataFrame
###### 1.4.2.2.1 创建
> 在SparkSQL中`SparkSession`是创建DataFrame和执行SQL入口.
> 创建DataFrame有三种方式 : 
> 1.通过Spark数据源进行创建.
> 2.从已存在的RDD进行转换.
> 3.从Hive Table进行查询返回.

- 1.从Spark数据源进行创建
- 查看Spark数据源进行创建文件格式
```
scala> spark.read.
csv      jdbc   load     options   parquet   table   textFile      
format   json   option   orc       schema    text 
scala> spark.read.
```
- 2.读取json文件创建DataFrame展示结果
```
scala> val jsonflow = spark.read.json("hdfs://systemhub511:9000/core_flow/spark/json/001/people.json")
jsonflow: org.apache.spark.sql.DataFrame = [age: bigint, name: string]=

scala> jsonflow.show
+----+-------+
| age|   name|
+----+-------+
|null|Michael|
|  30|   Andy|
|  19| Justin|
+----+-------+

scala> 
```
- 3.RDD进行转换 | 轻轻1.4.2.5
- 4.Hive Table进行查询返回 | 

###### 1.4.2.2.2 SQL风格语法(主要)
- 对DataFrame创建临时表
- 临时表是Session范围内,Session退出后,表就会失效,如果想应用范围内有效,可以使用全局表,注意使用全局表时需要全路径访问,如 : `global_temp.people`
```
scala> jsonflow.createTempView("people")
```
- 通过SQL语句实现查询全表结果展示
```
scala> val sqlDF = spark.sql("SELECT * FROM people")
sqlDF: org.apache.spark.sql.DataFrame = [age: bigint, name: string]

scala> sqlDF.show
+----+-------+
| age|   name|
+----+-------+
|null|Michael|
|  30|   Andy|
|  19| Justin|
+----+-------+

scala> 
```
- 对于DataFrame创建全局表
```
scala> jsonflow.createGlobalTempView("peoples")
```
- 通过SQL语句实现查询全表结果展示
```
scala> spark.sql("SELECT * FROM global_temp.peoples").show()
+----+-------+
| age|   name|
+----+-------+
|null|Michael|
|  30|   Andy|
|  19| Justin|
+----+-------+

scala> spark.newSession().sql("SELECT * FROM global_temp.peoples").show()
+----+-------+
| age|   name|
+----+-------+
|null|Michael|
|  30|   Andy|
|  19| Justin|
+----+-------+

scala>
```
###### 1.4.2.2.3 DSL风格语法(次要)
- 查看DataFrame Schema信息
```
scala> jsonflow.printSchema
root
 |-- age: long (nullable = true)
 |-- name: string (nullable = true)

scala> 
```
- 只查看name列数据
```
scala> jsonflow.select("name").show
+-------+
|   name|
+-------+
|Michael|
|   Andy|
| Justin|
+-------+

scala> 
```
- 查看name列数据以及age+1数据
```
scala> jsonflow.select($"name",$"age" + 1).show()
+-------+---------+
|   name|(age + 1)|
+-------+---------+
|Michael|     null|
|   Andy|       31|
| Justin|       20|
+-------+---------+

scala>
```
- 查看age大于21数据
```
scala> jsonflow.filter($"age" > 21).show()
+---+----+
|age|name|
+---+----+
| 30|Andy|
+---+----+

scala> 
```
- 按照age分组,查看数据条数
```
scala> jsonflow.groupBy("age").count().show()
+----+-----+
| age|count|
+----+-----+
|  19|    1|
|null|    1|
|  30|    1|
+----+-----+

scala> 
```
###### 1.4.2.2.4 RDD转换为DateFrame
> 如果需要RDD与DF或者DS之间操作,需要引入`import spark.implicits._`
> spark并不是包名,而是sparkSession对象名称.

- 导入隐式转换并创建RDD
```
scala> import spark.implicits._
import spark.implicits._

scala> val peopleRDD = sc.textFile("hdfs://systemhub511:9000/core_flow/spark/input/wordcount/wordcount_001.txt")
peopleRDD: org.apache.spark.rdd.RDD[String] = hdfs://systemhub511:9000/core_flow/spark/input/wordcount/wordcount_001.txt MapPartitionsRDD[30] at textFile at <console>:27

scala>
```
- 1.通过手动转换
```
scala> peopleRDD.map{x=>{val split = x.split(",");(split(0),split(1).trim)}}.toDF("name","age")
res11: org.apache.spark.sql.DataFrame = [name: string, age: string]
scala> 
```
- 2.通过反射转换 (需要用到样例类) 
- 创建样例类,根据样例类将RDD转换为DataFrame
```
scala> case class People(name:String, age:Int)
defined class People

scala> peopleRDD.map{x=>{val split = x.split(",");People(split(0),split(1).trim.toInt)}}.toDF
res17: org.apache.spark.sql.DataFrame = [name: string, age: int]

scala> res17.toDF
res18: org.apache.spark.sql.DataFrame = [name: string, age: int]
scala> 
```
- 3.通过编程方式转换
- 导入所需类型
```
scala> import org.apache.spark.sql.types._
import org.apache.spark.sql.types._
scala> 
```
- 创建Schema
```
scala> val structType: StructType = StructType(StructField("name",StringType) :: StructField("age",IntegerType) :: Nil)
structType: org.apache.spark.sql.types.StructType = StructType(StructField(name,StringType,true), StructField(age,IntegerType,true))
scala> 
```
- 导入所需类型
```
scala> import org.apache.spark.sql.Row
import org.apache.spark.sql.Row
scala> 
```
- 根据指定类型创建二元组RDD
```
scala> val data = peopleRDD.map{x => val para = x.split(",");Row(para(0),para(1).trim.toInt)}
scala> 
```
- 根据数据及指定schema创建DataFrame
``` 
scala> val dataFrame = spark.createDataFrame(data, structType)
```
- Create SqlAction.scala
``` scala
package com.geekparkhub.core.spark.application.sparksql

import org.apache.spark.rdd.RDD
import org.apache.spark.sql.types.{IntegerType, StructField, StructType}
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.sql.{DataFrame, Row, SparkSession}

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园枢纽
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * SqlAction
  * <p>
  */

object SqlAction {
  def main(args: Array[String]): Unit = {

    // 创建SparkSession
    val sparkSession: SparkSession = SparkSession
      .builder().master("local[*]").appName("SqlAction").getOrCreate()

    // 创建SC
    val sc: SparkContext = sparkSession.sparkContext

    // 创建 RDD
    val rdd: RDD[Int] = sc.parallelize(Array(1,2,3,4,5))

    // 将Int类型RDD转换为Row类型RDD
    val rowRDD: RDD[Row] = rdd.map(x => {Row(x)})

    // 数据输出
    rowRDD.collect().foreach(println)

    // 创建元数据信息
    val structType = new StructType
    val structTypes: StructType = structType.add(StructField("id", IntegerType))
    val dataFrame: DataFrame = sparkSession.createDataFrame(rowRDD,structTypes)

    // 导入隐式转换
    import sparkSession.implicits._

    // DSL风格 数据查询
    dataFrame.select("id").show()
    
    // 关闭资源
    sparkSession.stop()
  }
}
```
###### 1.4.2.2.5 DateFrame转换为RDD
- 直接调用rdd即可.
- 创建DataFrame
```
scala> val df = spark.read.json("/core_flow/spark/json/001/people.json")df: org.apache.spark.sql.DataFrame = [age: bigint, name: string]                
scala> 
```
- 将DataFrame转换为RDD
```
scala> val dfToRDD = df.rdd
dfToRDD: org.apache.spark.rdd.RDD[org.apache.spark.sql.Row] = MapPartitionsRDD[6] at rdd at <console>:29
scala>
```
- 打印RDD
```
scala> dfToRDD.collect
res0: Array[org.apache.spark.sql.Row] = Array([null,Michael], [30,Andy], [19,Justin])
scala>
```

##### 1.4.2.3 DataSet
- Dataset是具有强类型的数据集合,需要提供对应类型信息.
###### 1.4.2.3.1 创建
- 创建样例类
```
scala> case class Person(name: String, age: Long)
defined class Person
scala> 
```
- 创建DataSet
```
scala> val caseClassDS = Seq(Person("Andy", 32)).toDS()
caseClassDS: org.apache.spark.sql.Dataset[Person] = [name: string, age: bigint]
scala> 
```
- 查看结果
```
scala> caseClassDS.show
+----+---+
|name|age|
+----+---+
|Andy| 32|
+----+---+

scala> 
```

###### 1.4.2.3.2 RDD转换为DataSet
- SparkSQL能够自动将包含有case类RDD转换成DataFrame,case类定义了table结构,case类属性通过反射变成了表列名,Case类可以包含诸如Seqs或者Array等复杂结构.
- 创建RDD
```
scala> val peopleRDD = sc.textFile("examples/src/main/resources/people.txt")
peopleRDD: org.apache.spark.rdd.RDD[String] = examples/src/main/resources/people.txt MapPartitionsRDD[8] at textFile at <console>:28

scala>
```
- 创建样例类
```
scala> case class Person(name: String, age: Long)
defined class Person
scala> 
```
- 将RDD转化为DataSet
```
scala> peopleRDD.map(line => {val para = line.split(",");Person(para(0),para(1).trim.toInt)}).toDS
res2: org.apache.spark.sql.Dataset[Person] = [name: string, age: bigint]
scala> 
```

###### 1.4.2.3.3 DataSet转换为RDD
- 调用rdd方法即可.
- 创建一个DataSet
```
scala> val DS= Seq(Person("Andy", 32)).toDS()
DS: org.apache.spark.sql.Dataset[Person] = [name: string, age: bigint]
scala> 
```
- 将DataSet转换为RDD
```
scala> DS.rdd
res3: org.apache.spark.rdd.RDD[Person] = MapPartitionsRDD[12] at rdd at <console>:28

scala> res3.collect
res4: Array[Person] = Array(Person(Andy,32))
scala> 
```

##### 1.4.2.4 DataFrame与DataSet相互操作
###### 1.4.2.4.1 DataFrame转Dataset
- 此方法就是在给出每一列类型后,使用as方法转成Dataset,这在数据类型是DataFrame又需要针对各个字段处理时极为方便,在使用一些特殊的操作时,一定要加上`import spark.implicits._`不然toDF、toDS无法使用.
- 创建DateFrame
```
scala> val df = spark.read.json("./examples/src/main/resources/people.json")
```
- 创建样例类
```
scala> case class Person(name: String, age: Long)
defined class Person
scala> 
```
- 将DateFrame转化为DataSet
```
scala> df.as[Person]
res14:  org.apache.spark.sql.Dataset[Person]  =  [age:  bigint,  name: string]
scala> 
```

###### 1.4.2.4.2 Dataset转DataFrame
- 创建样例类
```
scala> case class Person(name: String, age: Long)
defined class Person
scala>
```
- 创建DataSet
```
scala> val ds = Seq(Person("Andy", 32)).toDS()
ds: org.apache.spark.sql.Dataset[Person] = [name: string, age: bigint]
scala> 
```
- 将DataSet转化为DataFrame并展示结果
```
scala> val df = ds.toDF
df: org.apache.spark.sql.DataFrame = [name: string, age: bigint]

scala> df.show
+----+---+
|name|age|
+----+---+
|Andy| 32|
+----+---+
scala> 
```


##### 1.4.2.5 RDD / DataFrame / DataSet
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_023.jpg)
> 在SparkSQL中Spark为提供了两个新抽象,分别是`DataFrame`和`DataSet`.
> 他们和RDD有什么区别? 首先从版本的产生上来看 : 
```
RDD (Spark1.0) —> Dataframe(Spark1.3) —> Dataset(Spark1.6)
```
> 如果同样数据都给到这三个数据结构,他们分别计算之后,都会给出相同结果,不同是执行效率和执行方式.
> 在后期Spark版本中,DataSet会逐步取代RDD和DataFrame成为唯一的API接口.

###### 1.4.2.5.1 三者共性
- 1.RDD / DataFrame / Dataset全都是spark平台下分布式弹性数据集,为处理超大型数据提供便利.
- 2.三者都有惰性机制,在进行创建 / 转换,如map方法时不会立即执行,只有在遇到Action如foreach时,三者才会开始遍历运算.
- 3.三者都会根据spark内存情况自动缓存运算,这样即使数据量很大,也不用担心会内存溢出.
- 4.三者都有partition概念.
- 5.三者有许多共同函数,如filter,排序等.
- 6.在对DataFrame和Dataset进行操作许多操作都需要这个包进行支持`importspark.implicits._`
- 7.DataFrame和Dataset均可使用模式匹配获取各个字段值和类型.
- DataFrame : 
```
DF.map{
 caseRow(col1:String,col2:Int)=>
  println(col1);println(col2)
   col1
    case_=> ""
}
```
- Dataset : 
```
// 定义字段名和类型
caseclassColtest(col1:String,col2:Int)extendsSerializable
DS.map{
 caseColtest(col1:String,col2:Int)=>
  println(col1);println(col2)
   col1
    case_=> ""
}
```

###### 1.4.2.5.2 三者区别
- `1. RDD` :
- RDD一般和spark mlib同时使用
- RDD不支持sparksql操作
- `2. DataFrame`
- 与RDD和Dataset不同,DataFrame每一行类型固定为Row,每一列的值没法直接访问,只有通过解析才能获取各个字段值.
```
DF.foreach{
 line=>
  valcol1=line.getAs[String]("col1")
  valcol2=line.getAs[String]("col2")
}
```
- DataFrame与Dataset一般不与spark mlib同时使用
- DataFrame与Dataset均支持sparksql操作,比如select,groupby,还能注册临时表/视窗,进行sql语句操作.
- DataFrame与Dataset支持一些特别方便保存方式,比如保存成csv,可以带上表头,这样每一列字段名一目了然.
- `3.`Dataset`
- Dataset和DataFrame拥有完全相同的成员函数,区别只是每一行数据类型不同.
- DataFrame也可以叫`Dataset[Row]`,每一行的类型是Row,不解析每一行究竟有哪些字段,各个字段又是什么类型都无从得知,只能用上面提到`getAS`方法或者共性中的第七条提到的模式匹配拿出特定字段,而Dataset中,每一行是什么类型是不一定,在自定义了case class之后可以很自由获得每一行信息.
- Dataset在需要访问列中某个字段时是非常方便,然而如果要写一些适配性很强函数时,如果使用Dataset,行类型又不确定,可能是各种case class,无法实现适配,这时候用DataFrame即Dataset[Row]就能比较好解决问题.

##### 1.4.2.6 SparkSQL Application
- SQL & DSL风格数据查询
``` scala
package com.geekparkhub.core.spark.application.sparksql

import org.apache.spark.sql.{DataFrame, SparkSession}

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园枢纽
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * SqlAction
  * <p>
  */

object SqlAction {
  def main(args: Array[String]): Unit = {
    // 创建SparkSession
    val sparkSession: SparkSession = SparkSession
      .builder().master("local[*]").appName("SqlAction").getOrCreate()

    // 导入隐式转换
    import sparkSession.implicits._

    // 创建DF
    val df: DataFrame = sparkSession.read.json("/Volumes/GEEK-SYSTEM/Technical_Framework/spark/projects/spark_server/spark-sql/data/people.json")

    // SQL风格 数据查询 | 创建临时表
    df.createTempView("PEOPLE")
    sparkSession.sql("SELECT * FROM PEOPLE").show()

    // DSL风格 数据查询
    df.select("name").show()

    // 关闭资源
    sparkSession.stop()
  }
}
```

##### 1.4.2.7 自定义函数
- 在Shell窗口中可通过`spark.udf`功能自定义函数.

###### 1.4.2.7.1 自定义UDF函数
- 创建DF
```
scala> val df = spark.read.json("hdfs://systemhub511:9000/core_flow/spark/json/001/people.json")
df: org.apache.spark.sql.DataFrame = [age: bigint, name: string]

scala> df.show()
+----+-------+
| age|   name|
+----+-------+
|null|Michael|
|  30|   Andy|
|  19| Justin|
+----+-------+

scala>
```
- 注册UDF
```
scala> spark.udf.register("addName",(x:String) => "Name:" + x)
res1: org.apache.spark.sql.expressions.UserDefinedFunction = UserDefinedFunction(<function1>,StringType,Some(List(StringType)))

scala>
```
- 创建数据表
```
scala> df.createOrReplaceTempView("people")
```
- 查询数据表
```
scala> spark.sql("Select addName(name),age from people").show()
+-----------------+----+
|UDF:addName(name)| age|
+-----------------+----+
|     Name:Michael|null|
|        Name:Andy|  30|
|      Name:Justin|  19|
+-----------------+----+
scala>
```
###### 1.4.2.7.2 自定义聚合函数
- 强类型Dataset和弱类型DataFrame都提供了相关聚合函数,如count(),countDistinct(),avg(),max(),min(),除此之外还可以设定自定义聚合函数.
- 弱类型自定义聚合函数 : 通过继承`UserDefinedAggregateFunction`来实现自定义聚合函数.
- 下面展示 求平均工资自定义聚合函数
- Create `AvgAction.scala`
``` scala
package com.geekparkhub.core.spark.application.aggregation

import org.apache.spark.sql.Row
import org.apache.spark.sql.expressions.{MutableAggregationBuffer, UserDefinedAggregateFunction}
import org.apache.spark.sql.types.{DataType, DoubleType, LongType, StructField, StructType}

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园枢纽
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * AvgAction
  * <p>
  */

object AvgAction extends UserDefinedAggregateFunction {

  // 定义输入数据类型
  override def inputSchema: StructType = StructType(StructField("input", LongType) :: Nil)

  // 缓存中间值类型
  override def bufferSchema: StructType = StructType(StructField("sum", LongType) :: StructField("count", LongType) :: Nil)

  // 定义输出数据类型
  override def dataType: DataType = DoubleType

  // 函数稳定参数
  override def deterministic: Boolean = true

  // 初始化缓存数据
  override def initialize(buffer: MutableAggregationBuffer): Unit = {
    buffer(0) = 0L
    buffer(1) = 0L
  }

  // 在执行器之内更新
  override def update(buffer: MutableAggregationBuffer, input: Row): Unit = {
    buffer(0) = buffer.getLong(0) + input.getLong(0)
    buffer(1) = buffer.getLong(1) + 1L
  }

  // 在执行器之外合并
  override def merge(buffer1: MutableAggregationBuffer, buffer2: Row): Unit = {
    buffer1(0) = buffer1.getLong(0) + buffer2.getLong(0)
    buffer1(1) = buffer1.getLong(1) + buffer2.getLong(1)

  }

  // 执行数据计算
  override def evaluate(buffer: Row): Any = buffer.getLong(0).toDouble / buffer.getLong(1)
}
```
- Create `UdafAction.scala`
```
package com.geekparkhub.core.spark.application.aggregation

import org.apache.spark.sql.{DataFrame, SparkSession}

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园枢纽
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * UdafAction
  * <p>
  */

object UdafAction {
  def main(args: Array[String]): Unit = {

    // 创建SparkSession
    val sparkSession: SparkSession = SparkSession
      .builder().master("local[*]").appName("UdafAction").getOrCreate()

    // 创建DF
    val df: DataFrame = sparkSession.read.json("/Volumes/GEEK-SYSTEM/Technical_Framework/spark/projects/spark_server/spark-sql/data/people.json")

    // SQL风格 数据查询 | 创建临时表
    df.createTempView("PEOPLE")

    // 注册自定义函数
    sparkSession.udf.register("AvgAction", AvgAction)

    // 使用自定义函数
    sparkSession.sql("SELECT AvgAction(age) FROM PEOPLE").show()

    // 关闭资源
    sparkSession.stop()
  }
}
```

## 🔒 尚未解锁 正在探索中... 尽情期待 Blog更新! 🔒
- 强类型自定义聚合函数 : 通过继承`Aggregator`来实现强类型自定义聚合函数,同样是求平均工资.


#### 1.4.3 Spark SQL 数据源
#####1.4.3.1 通用加载 / 保存方法
#####1.4.3.2 JSON文件
#####1.4.3.3 Parquet文件
#####1.4.3.4 JDBC
#####1.4.3.5 Hive DataBase


#### 1.4.4 Spark SQL 实例



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