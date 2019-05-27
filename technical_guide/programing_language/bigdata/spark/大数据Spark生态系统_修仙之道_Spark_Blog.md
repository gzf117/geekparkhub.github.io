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
###### 1.3.2.3.1.1 `map(func)` 案例
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
###### 1.3.2.3.1.2 `mapPartitions(func)` 案例
- 作用 : 类似于map,但独立地在RDD每一个分片上运行,因此在类型为T的RDD上运行时,func函数类型必须是Iterator[T] => Iterator[U]
- 假设有N个元素,有M个分区,那么map函数将被调用N次,而mapPartitions被调用M次,一个函数一次处理所有分区.
```
scala> rdd.mapPartitions(_.map(_*2)).collect
res11: Array[Int] = Array(1022, 1222, 1422)
scala> 
```

###### 1.3.2.3.1.3 `mapPartitionsWithIndex(func)` 案例
- 作用 : 类似于mapPartitions,但func带有一个整数参数表示分片索引值,因此在类型为T的RDD上运行时,func的函数类型必须是(Int, Interator[T]) => Iterator[U];
```
scala> rdd.mapPartitionsWithIndex((index,items)=>(items.map((index,_)))).collect
res13: Array[(Int, Int)] = Array((1,511), (2,611), (3,711))
scala> 
```

###### 1.3.2.3.1.4 `flatMap(func)` 案例
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

###### 1.3.2.3.1.6 `glom` 案例
- 作用 : 将每一个分区形成一个数组,形成新的RDD类型时RDD[Array[T]]
```
scala> rdd.glom.collect
res17: Array[Array[Int]] = Array(Array(), Array(511), Array(611), Array(711))   
scala> 
```

###### 1.3.2.3.1.7 `groupBy(func)` 案例
- 作用 : 分组按照传入函数的返回值进行分组,将相同的key对应的值放入一个迭代器.
```
scala> rdd.groupBy(_ % 2).collect
res18: Array[(Int, Iterable[Int])] = Array((1,CompactBuffer(611, 711, 511)))    
scala> 
```

###### 1.3.2.3.1.8 `filter(func)` 案例
- 作用 : 过滤返回一个新的RDD,该RDD由经过func函数计算后返回值为true的输入元素组成.
```
scala> rdd.filter(_%3==0).collect
res20: Array[Int] = Array(711)
scala> 
```

###### 1.3.2.3.1.9 `sample(withReplacement,fraction,seed)` 案例
- 作用 : 以指定随机种子随机抽样出数量为fraction的数据,withReplacement表示是抽出的数据是否放回,true为有放回的抽样,false为无放回的抽样,seed用于指定随机数生成器种子.
```
scala> val rdd = sc.parallelize(1 to 100)
rdd: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[22] at parallelize at <console>:24
scala> rdd.sample(false,0.1,3).collect
res22: Array[Int] = Array(1, 33, 37, 50, 59, 69, 75, 78, 85, 98) 
scala> 
```

###### 1.3.2.3.1.10 `distinct([numTasks]))` 案例
- 作用 : 对源RDD进行去重后返回一个新的RDD,默认情况下,只有8个并行任务来操作,但是可以传入一个可选的numTasks参数改变它.
- 使用distinct()对其去重操作.
```
scala> rdd.distinct(4).collect
res23: Array[Int] = Array(84, 100, 96, 52, 56, 4, 76, 16, 28, 80, 48, 32, 36, 24, 64, 92, 40, 72, 8, 12, 20, 60, 44, 88, 68, 13, 41, 61, 81, 21, 77, 53, 97, 25, 29, 65, 73, 57, 93, 33, 37, 45, 1, 89, 17, 69, 9, 85, 49, 5, 34, 82, 66, 22, 54, 98, 46, 30, 14, 50, 62, 42, 74, 90, 6, 70, 18, 38, 86, 58, 78, 26, 94, 10, 2, 19, 39, 15, 47, 71, 55, 95, 79, 59, 11, 35, 27, 75, 51, 23, 63, 83, 67, 3, 7, 91, 31, 87, 43, 99)
scala> 
```
###### 1.3.2.3.1.11 `coalesce(numPartitions)` 案例
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
###### 1.3.2.3.1.12 `repartition(numPartitions)` 案例
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
###### 1.3.2.3.1.14 `sortBy(func,[ascending],[numTasks])` 案例
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

###### 1.3.2.3.1.15 `pipe(command,[envVars])` 案例
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

##### 1.3.2.3.2 双Value类型交互

##### 1.3.2.3.3 Key-Value 类型


##### 1.3.2.4 Action



#### 1.3.3 Key-Value RDD 数据分区
#### 1.3.4 数据读取保存
#### 1.3.5 RDD 编程进阶






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