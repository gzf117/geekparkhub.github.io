,# 大数据Spark生态系统 修仙之道 Spark Blog

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
###### 1.4.2.7.2 自定义UDAF聚合函数
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


- 强类型自定义聚合函数 : 通过继承`Aggregator`来实现强类型自定义聚合函数,同样是求平均工资.

#### 1.4.3 Spark SQL 数据源
##### 1.4.3.1 通用加载 / 保存方法
###### 1.4.3.1.1 手动指定选项
- Spark SQL DataFrame接口支持多种数据源操作,一个DataFrame可以进行RDDs方式操作,也可以被注册为临时表,把DataFrame注册为临时表之后,就可以对该DataFrame执行SQL查询.
- Spark SQL默认数据源为Parquet格式,数据源为Parquet文件时,Spark SQL可以方便执行所有操作,修改配置项`spark.sql.sources.default`,可修改默认数据源格式 : 
```
scala> val df = spark.read.load("examples/src/main/resources/users.parquet") df.select("name","favorite_color").write.save("namesAndFavColors.parquet")
scala> 
```
- 当数据源格式不是parquet格式文件时,需要手动指定数据源格式,数据源格式需要指定全名（例如：`org.apache.spark.sql.parquet`）,如果数据源格式为内置格式,则只需要指定简称定`json`,`parquet`,`jdbc`,`orc`,`libsvm`,`csv`,`text`来指定数据格式
- 可以通过SparkSession提供的read.load方法用于通用加载数据，使用`write`和`save`保存数据.
```
scala> val peopleDF = spark.read.format("json").load("examples/src/main/resources/people.json")
scala> peopleDF.write.format("parquet").save("hdfs://hadoop102:9000/namesAndAges.parquet")
scala> 
```
- 除此之外,可以直接运行SQL在文件上.
```
scala> val sqlDF = spark.sql("SELECT * FROM parquet.`hdfs://systemhub511:9000/namesAndAges.parquet`")

scala> sqlDF.show()

scala> val peopleDF = spark.read.format("json").load("examples/src/main/resources/people.json")peopleDF: org.apache.spark.sql.DataFrame = [age: bigint, name: string]

scala> peopleDF.write.format("parquet").save("hdfs://hadoop102:9000/namesAndAges.parquet")

scala> peopleDF.show()
+----+-------+
| age|   name|
+----+-------+
|null|Michael|
|  30|   Andy|
|  19| Justin|
+----+-------+

scala> val sqlDF = spark.sql("SELECT * FROM  parquet.`hdfs://systemhub511:9000/namesAndAges.parquet`")
sqlDF: org.apache.spark.sql.DataFrame = [age: bigint, name: string]

scala> sqlDF.show()
+----+-------+
| age|   name|
+----+-------+
|null|Michael|
|  30|   Andy|
|  19| Justin|
+----+-------+
```


###### 1.4.3.1.2 文件保存选项
- 可以采用SaveMode执行存储操作,SaveMode定义了对数据处理模式,需要注意的是,这些保存模式不使用任何锁定,不是原子操作,此外当使用Overwrite方式执行时,在输出新数据之前原数据就已经被删除,SaveMode详细介绍如下表 : 

| Scala / Java      |     Any Language |   Meaning   |
| :--------: | :--------:| :------: |
| SaveMode.ErrorIfExists(default)    |   "error"(default) |  如果文件存在,则报错  |
| SaveMode.Append    |   "append" |  追加  |
| SaveMode.Overwrite    |   "overwrite" |  覆写  |
| SaveMode.Ignore    |   "ignore" |  数据存在,则忽略  |
-  源码出处
- `org.apache.spark.sql.DataFrameWriter` & `org.apache.spark.sql.SaveMode` 
```
/** 
 * Specifies the behavior when data or table already exists. Options include:
 *   - `overwrite`: overwrite the existing data.
 *   - `append`: append the data.
 *   - `ignore`: ignore the operation (i.e. no-op).
 *   - `error`: default option, throw an exception at runtime.
 *   
 * @since 1.4.0
 */ 
def mode(saveMode: String): DataFrameWriter[T] = {
  this.mode = saveMode.toLowerCase match {
    case "overwrite" => SaveMode.Overwrite
    case "append" => SaveMode.Append
    case "ignore" => SaveMode.Ignore
    case "error" | "default" => SaveMode.ErrorIfExists
    case _ => throw new IllegalArgumentException(s"Unknown save mode: $saveMode. " + "Accepted save modes are 'overwrite', 'append', 'ignore', 'error'.")
 }         
 this
}
```

#####1.4.3.2 JSON文件
- Spark SQL能够自动推测JSON数据集结构,并将它加载为`Dataset[Row]`,可以通过`SparkSession.read.json()`加载JSON 文件.
- JSON文件不是一个传统JSON文件,而是每一行都得是一个JSON串.
```
scala> import spark.implicits._

scala> val path = "examples/src/main/resources/people.json"

scala> val peopleDF = spark.read.json(path)

scala> peopleDF.createOrReplaceTempView("people")

scala> val teenagerNamesDF = spark.sql("SELECT name FROM people WHERE  age BETWEEN 13 AND 19")

scala> teenagerNamesDF.show()
+------+
|  name|
+------+
|Justin|
+------+

scala> val otherPeopleDataset = spark.createDataset("""{"name":"Yin","address":{"city":"Columbus","state":"Ohio"}}""" :: Nil)

scala> val otherPeople = spark.read.json(otherPeopleDataset)

scala> otherPeople.show()
+---------------+----+
| address 	|  name  |
+---------------+----+
|[Columbus,Ohio]| Yin|
```

#####1.4.3.3 Parquet文件
- Parquet是一种流行列式存储格式,可以高效地存储具有嵌套字段记录,Parquet格式经常在Hadoop生态圈中被使用,它也支持Spark SQL全部数据类型,Spark SQL提供了直接读取和存储Parquet格式文件的方法.
```
scala> importing spark.implicits._

scala> import spark.implicits._	

scala> val peopleDF = spark.read.json("examples/src/main/resources/people.json")

scala> peopleDF.write.parquet("hdfs://systemhub511:9000/people.parquet")

scala> val parquetFileDF =         spark.read.parquet("hdfs://systemhub511:9000/people.parquet")

scala> parquetFileDF.createOrReplaceTempView("parquetFile")

scala> val namesDF = spark.sql("SELECT name FROM parquetFile WHERE age BETWEEN 13 AND 19")

scala> namesDF.map(attributes => "Name: " + attributes(0)).show()

+------------+
|       value|
+------------+
|Name: Justin|
+------------+
```

#####1.4.3.4 JDBC
- Spark SQL可以通过JDBC从关系型数据库中读取数据方式创建DataFrame,通过对DataFrame一系列的计算后,还可以将数据再写回关系型数据库中.
- 注意,需要将相关数据库驱动放到spark类路径下.
```
[root@systemhub711 ~]# cp /opt/software/mysql-libs/mysql-connector-java-5.1.27/mysql-connector-java-5.1.27-bin.jar /opt/module/spark/jars/
```
```
scala> val jdbcDF = spark.read.format("jdbc").option("url","jdbc:mysql://systemhub711:3306/company").option("dbtable","staff").option("user","root").option("password","ax01465").load()
jdbcDF: org.apache.spark.sql.DataFrame = [id: int, name: string ... 1 more field]

scala> jdbcDF.show

+---+-------+------+
| id|   name|   sex|
+---+-------+------+
|  1|test001|  male|
|  2|test002|female|
|  3|test003|female|
|  4|test004|  male|
|  5|test005|female|
|  6|test006|  male|
|  7|test007|female|
|  8|test008|female|
|  9|test009|female|
| 10|test010|female|
| 11|test011|female|
| 12|test012|  male|
| 13| Female|  null|
| 14|   Male|  null|
| 15| Female|  null|
+---+-------+------+
scala> 
```
```
scala> jdbcDF.write.format("jdbc").option("url", "jdbc:mysql://systemhub711:3306/company").option("dbtable","rddtable2").option("user","root").option("password","ax01465").save()
```
#####1.4.3.5 Hive DataBase
> Apache Hive是Hadoop上SQL引擎,Spark SQL编译时可以包含Hive支持,也可以不包含,包含Hive支持的Spark SQL可以支持Hive表访问、UDF(用户自定义函数)以及Hive查询语言(HiveQL/HQL)等,需要强调的一点是,如果要在Spark SQL中包含Hive库,并不需要事先安装Hive,一般来说,最好还是在编译Spark SQL时引入Hive支持,这样就可以使用这些特性了,如果下载的是二进制版本Spark,它应该已经在编译时添加了Hive支持.
> 
> 若要把Spark SQL连接到一个部署好Hive上,你必须把hive-site.xml复制到Spark配置文件目录中`($SPARK_HOME/conf)`,即使没有部署好Hive,Spark SQL也可以运行,需要注意的是,如果没有部署好Hive,Spark SQL会在当前工作目录中创建出Hive元数据仓库,叫作`metastore_db`,此外如果尝试使用HiveQL中的`CREATE TABLE (并非CREATE EXTERNAL TABLE)`语句来创建表,这些表会被放在默认的文件系统中的`/user/hive/warehouse`目录中(如果classpath中有配好的hdfs-site.xml,默认文件系统就是HDFS,否则就是本地文件系统).

###### 1.4.3.5.1 内嵌Hive应用
- 如果要使用内嵌Hive,什么都不用做,直接用就可以了,`--conf:spark.sql.warehouse.dir=`
- 如果使用是内部的Hive,在Spark2.0之后,`spark.sql.warehouse.dir`用于指定数据仓库地址,如果需要是用HDFS作为路径,那么需要将`core-site.xml`和`hdfs-site.xml`加入到Spark conf目录,否则只会创建master节点上warehouse目录,查询时会出现文件找不到的问题,这是需要向使用HDFS,则需要将metastore删除,重启集群.
```
scala> spark.sql("show tables").show
+--------+---------+-----------+
|database|tableName|isTemporary|
+--------+---------+-----------+
+--------+---------+-----------+

scala> spark.sql("create table hivetest(id int)")
19/06/03 02:03:17 WARN metastore.HiveMetaStore: Location: file:/opt/module/spark/spark-warehouse/hivetest specified for non-external table:hivetest
res5: org.apache.spark.sql.DataFrame = []

scala> spark.sql("show tables").show
+--------+---------+-----------+
|database|tableName|isTemporary|
+--------+---------+-----------+
| default| hivetest|      false|
+--------+---------+-----------+

scala> spark.sql("select * from hivetest").show()
+---+
| id|
+---+
+---+
scala> 
```

###### 1.4.3.5.2 外部Hive应用
- 如果想连接外部已经部署好的Hive,需要通过以下几个步骤 : 
- 1.启动Hive服务
```
[root@systemhub711 spark]# /opt/module/hive/bin/hive
```
- 2.将Hive中的`hive-site.xml`拷贝或者软连接到Spark安装目录下conf目录下
```
[root@systemhub711 spark]# cp /opt/module/hive/conf/hive-site.xml ./conf/
```
- 3.开启spark shell终端 | 显示所有数据表并查看某张数据表数据
```
scala> spark.sql("show tables").show
+--------+--------------------+-----------+
|database|           tableName|isTemporary|
+--------+--------------------+-----------+
| default|            business|      false|
| default|                dept|      false|
| default|      dept_partition|      false|
| default|                 emp|      false|
| default|             emp_sex|      false|
| default|hive_hbase_emp_table|      false|
| default|       hive_workflow|      false|
| default|            location|      false|
| default|          movie_info|      false|
| default|multitasking_hive...|      false|
| default|         person_info|      false|
| default| relevance_hbase_emp|      false|
| default|               score|      false|
| default|          staff_hive|      false|
| default|                test|      false|
| default|             test001|      false|
| default|             test002|      false|
| default|             test003|      false|
| default|             test004|      false|
| default|             test005|      false|
+--------+--------------------+-----------+
only showing top 20 rows

scala> spark.sql("select * from emp").show
+-----+-----+---------+----+----------+--------+-----+------+
|empno|ename|      job| mgr|  hiredate|     sal| comm|deptno|
+-----+-----+---------+----+----------+--------+-----+------+
| 7369|SMITH|CLERKSKLD|7902|1980-12-17|   800.0| 20.0|  null|
| 7499|ALLTE|SALESMANS|7689|1987-02-23|  1600.0|300.0|    30|
| 7521|WAROS|SJDHHJDJX|7869|1984-06-12| 1250.18|500.0|    30|
| 7566|JOSSS|JDHYHDSDS|4545|1874-05-15| 2894.25| 20.0|  null|
| 7654|SOCTD|MANSJUSSD|4855|1996-02-14|  2852.3| 30.0|  null|
| 7698|ADAMS|JUSHHWESD|4552|1985-05-16|25524.02| 30.0|  null|
| 7782|JAMSK|KIHNGSEHN|7769|1991-06-23|  1100.0| 20.0|  null|
| 7788|FOESS|CLAEDFDFD|7698|1994-09-17|   950.0| 30.0|  null|
| 7939|KINGS|CLADDJHEW|7566|1993-07-12|  3000.0| 20.0|  null|
+-----+-----+---------+----+----------+--------+-----+------+
scala> 
```

###### 1.4.3.5.3 运行Spark SQL CLI
- Spark SQL CLI可以很方便在本地运行Hive元数据服务以及从命令行执行查询任务.
- 在Spark目录下执行如下命令启动Spark SQL CLI
```
[root@systemhub711 spark]# bin/spark-sql
spark-sql (default)> show tables;
database        tableName       isTemporary
default business        false
default dept    false
default dept_partition  false
default emp     false
default emp_sex false
default hive_hbase_emp_table    false
default hive_workflow   false
default location        false
default movie_info      false
default multitasking_hive_workflow      false
default person_info     false
default relevance_hbase_emp     false
default score   false
default staff_hive      false
default test    false
default test001 false
default test002 false
default test003 false
default test004 false
default test005 false
default test006 false
default test007 false
default test008 false
default test_buck       false
default test_bucket     false
Time taken: 6.2 seconds, Fetched 25 row(s)
19/06/03 02:17:58 INFO CliDriver: Time taken: 6.2 seconds, Fetched 25 row(s)
spark-sql (default)> 
```
###### 1.4.3.5.4 使用IDEA连接SparkSQL for Hive 
- pom.xml 公共依赖信息
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
        <module>spark-core</module>
        <module>spark-sql</module>
    </modules>

    <dependencies>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-core_2.11</artifactId>
            <version>2.1.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-sql_2.11</artifactId>
            <version>2.1.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive_2.11</artifactId>
            <version>2.1.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.hive</groupId>
            <artifactId>hive-exec</artifactId>
            <version>1.2.1</version>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.15</version>
        </dependency>
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
    </dependencies>
</project>
```
- Create `SparkHiveAction.scala`
``` scala
package com.geekparkhub.core.spark.application.sparksql

import org.apache.spark.sql.SparkSession

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
  * SparkHiveAction
  * <p>
  */

object SparkHiveAction {
  def main(args: Array[String]): Unit = {
    // 创建SparkSession
    val sparkSession: SparkSession = SparkSession
      .builder()
      .enableHiveSupport()
      .master("local[*]")
      .appName("SparkHiveAction")
      .getOrCreate()

    // 展示数据表信息
    sparkSession.sql("show tables").show()

    // 关闭资源
    sparkSession.stop()
  }
}
```
- 运行查看结果
```
+--------+--------------------+-----------+
|database|           tableName|isTemporary|
+--------+--------------------+-----------+
| default|            business|      false|
| default|                dept|      false|
| default|      dept_partition|      false|
| default|                 emp|      false|
| default|             emp_sex|      false|
| default|hive_hbase_emp_table|      false|
| default|       hive_workflow|      false|
| default|            location|      false|
| default|          movie_info|      false|
| default|multitasking_hive...|      false|
| default|         person_info|      false|
| default| relevance_hbase_emp|      false|
| default|               score|      false|
| default|          staff_hive|      false|
| default|                test|      false|
| default|             test001|      false|
| default|             test002|      false|
| default|             test003|      false|
| default|             test004|      false|
| default|             test005|      false|
+--------+--------------------+-----------+
only showing top 20 rows
```

#### 1.4.4 Spark SQL 实例

### 🔥 1.5 Spark Streaming 🔥
#### 1.5.1 Spark Streaming 概述
##### 1.5.1.1 Spark Streaming 是什么
> Spark Streaming用于流式数据处理,Spark Streaming支持数据输入源很多,例如 : Kafka / Flume / Twitter / ZeroMQ和简单TCP套接字等等,数据输入后可以用Spark高度抽象原语如 : map / reduce / join / window等进行运算,而结果也能保存在很多地方,如HDFS,数据库等,另外Spark Streaming也能和MLlib(机器学习)以及Graphx完美融合.

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_024.jpg)

> Spark Streaming和Spark基于RDD概念很相似,Spark Streaming使用`离散化流`(`discretized stream`)作为抽象表示,叫作`DStream`,DStream是随时间推移而收到的数据序列,在内部每个时间区间收到数据都作为RDD存在,而DStream是由这些RDD所组成的序列(因此得名“`离散化`”).
> 
> DStream可以从各种输入源创建,比如Flume / Kafka或者HDFS,创建出来DStream支持两种操作,一种是转化操作(`transformation`),会生成一个新的DStream,另一种是输出操作(`output operation`),可以把数据写入外部系统中,DStream提供了许多与RDD所支持的操作相类似操作支持,还增加了与时间相关新操作,比如滑动窗口.

##### 1.5.1.2 Spark Streaming 特点
- 1.易用
- 2.容错
- 3.易整合到Spark体系

##### 1.5.1.3 Spark Streaming 架构

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_025.jpg)

#### 1.5.2 DataStream 入门
##### 1.5.2.1 WordCount 案例
- 1.需求 : 使用`netcat`工具向9999端口不断发送数据,通过SparkStreaming读取端口数据并统计不同单词出现次数.
- 2.追加依赖信息
``` xml
<dependency>
 <groupId>org.apache.spark</groupId>
 <artifactId>spark-streaming_2.11</artifactId>
 <version>2.1.1</version>
</dependency>
```
- 3. Create `StreamWordCounAction.scala`
``` scala
package com.geekparkhub.core.spark.application.example

import org.apache.spark.SparkConf
import org.apache.spark.streaming.dstream.{DStream, ReceiverInputDStream}
import org.apache.spark.streaming.{Seconds, StreamingContext}

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
  * StreamWordCounAction
  * <p>
  */

object StreamWordCounAction {
  def main(args: Array[String]): Unit = {

    // 创建 SparkConf
    val sc: SparkConf = new SparkConf().setMaster("loacl[*]").setAppName("StreamWordCounAction")

    //创建 StreamingContext
    val ssc = new StreamingContext(sc, Seconds(3))

    // 创建 DStream
    val lineDStream: ReceiverInputDStream[String] = ssc.socketTextStream("systemhub511", 9999)

    // 将行数据转换为单词
    val wordDStream: DStream[String] = lineDStream.flatMap(_.split(" "))

    // 将单词住转换为元祖
    val wordAndOneDStream: DStream[(String, Int)] = wordDStream.map((_, 1))

    // 统计单词出现个数
    val DStreamResult: DStream[(String, Int)] = wordAndOneDStream.reduceByKey(_ + _)

    // 输出日志信息
    DStreamResult.print()

    // 启动流式任务
    ssc.start()
    ssc.awaitTermination()
  }
}
```

- 4.启动Hadoop集群服务(包括Spark服务)
```
[root@systemhub511 ~]# start-cluster.sh
[root@systemhub511 spark]# sbin/start-all.sh
[root@systemhub511 spark]# sbin/start-history-server.sh
```

- 5.启动程序并通过NetCat发送数据
```
[root@systemhub511 spark]# nc -lk 9999
hello
spark
io
io
io
```
- 6.查看日志信息
```
-------------------------------------------
Time: 1559563323000 ms
-------------------------------------------
(hello,1)

-------------------------------------------
Time: 1559563326000 ms
-------------------------------------------
(spark,1)

-------------------------------------------
Time: 1559563329000 ms
-------------------------------------------

Time: 1559563341000 ms
-------------------------------------------
(io,1)

-------------------------------------------
Time: 1559563344000 ms
-------------------------------------------
(io,2)
```
##### 1.5.2.2 WordCount 解析
> `Discretized Stream`是Spark Streaming基础抽象,代表持续性数据流和经过各种Spark原语操作后的结果数据流,在内部实现上`DStream`是一系列连续的RDD来表示,每个RDD含有一段时间间隔内的数据.

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_026.jpg)

> 对数据操作也是按照RDD为单位来进行
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_027.jpg)

> 计算过程由Spark engine来完成
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_028.jpg)

#### 1.5.3 DataStream 创建
> Spark  Streaming原生支持一些不同数据源,一些核心数据源已经被打包到Spark Streaming的Maven工件中,而其他一些则可以通过spark-streaming-kafka等附加工件获取,每个接收器都以Spark执行器程序中一个长期运行的任务形式运行,因此会占据分配给应用CPU核心.
> 
> 此外还需要有可用的CPU核心来处理数据,这意味着如果要运行多个接收器,就必须至少有和接收器数目相同的核心数,还要加上用来完成计算所需要的核心数,例如如果想要在流计算应用中运行10个接收器,那么至少需要为应用分配11个CPU核心,所以如果在本地模式运行,不要使用`local`或者`local[1]`

##### 1.5.3.1 文件数据源
> 文件数据流 : 能够读取所有HDFS API兼容文件系统文件,通过`fileStream`方法进行读取,Spark Streaming将会监控`dataDirectory`目录并不断处理移动进来的文件,但是目前不支持嵌套目录.

###### 1.5.3.1.1 用法及说明
- 注意事项 : 
- 1.文件需要有相同数据格式
- 2.文件进入dataDirectory方式需要通过移动或者重命名来实现
- 3.一旦文件移动进目录,则不能再修改,即便修改也不会读取新数据
```
streamingContext.textFileStream(dataDirectory)
```

###### 1.5.3.1.2 案例实操
- 1.在HDFS上创建用于被监听目录
```
[root@systemhub511 spark]# hadoop fs -mkdir /core_flow/spark/filestream
```
- 2.创建三个文件
```
[root@systemhub511 filestream]# vim a.txt
[root@systemhub511 filestream]# vim b.txt
[root@systemhub511 filestream]# vim c.txt
```
- 3.Create `FileStreamAction.scala`
``` scala
package com.geekparkhub.core.spark.application.datastream

import org.apache.spark.SparkConf
import org.apache.spark.streaming.dstream.DStream
import org.apache.spark.streaming.{Seconds, StreamingContext}

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
  * FileStreamAction
  * <p>
  */

object FileStreamAction {
  def main(args: Array[String]): Unit = {

    // 创建 SparkConf
    val sc: SparkConf = new SparkConf().setMaster("local[*]").setAppName("FileStreamAction")

    //创建 StreamingContext
    val ssc = new StreamingContext(sc, Seconds(3))

    // 监控文件夹 DStream
    val fileDStream: DStream[String] = ssc.textFileStream("hdfs://systemhub511:9000/core_flow/spark/filestream/")

    // 输出日志信息
    fileDStream.print()

    // 启动流式任务
    ssc.start()
    ssc.awaitTermination()
  }
}
```
- 4.启动程序
```
-------------------------------------------
Time: 1559566113000 ms
-------------------------------------------

-------------------------------------------
Time: 1559566116000 ms
-------------------------------------------

-------------------------------------------
Time: 1559566119000 ms
-------------------------------------------
```

- 5.上传文件
```
[root@systemhub511 spark]# hadoop fs -put /opt/module/datas/spark_flow/filestream/a.txt /core_flow/spark/filestream/

[root@systemhub511 spark]# hadoop fs -put /opt/module/datas/spark_flow/filestream/b.txt /core_flow/spark/filestream/

[root@systemhub511 spark]# hadoop fs -put /opt/module/datas/spark_flow/filestream/c.txt /core_flow/spark/filestream/
```
- 6.查看日志信息
```
-------------------------------------------
Time: 1559566146000 ms
-------------------------------------------
SparkStreaming
SparkStreaming
SparkStream
DStream

-------------------------------------------
Time: 1559566155000 ms
-------------------------------------------
textFileStream
textFileStream
StreamingContext

-------------------------------------------
Time: 1559566164000 ms
-------------------------------------------
awaitTermination
hadoop
```

##### 1.5.3.2 RDD 队列
###### 1.5.3.2.1 用法及说明
> 测试过程中,可以通过使用`ssc.queueStream(queueOfRDDs)`来创建DStream,每一个推送到这个队列中的RDD,都会作为一个DStream处理.
###### 1.5.3.2.2 案例实操
- 1.需求 : 循环创建RDD,将RDD放入队列,通过SparkStream创建Dstream计算WordCoun.
- 2.Create `QueuStreamAction.scala`
``` scala
package com.geekparkhub.core.spark.application.datastream

import org.apache.spark.SparkConf
import org.apache.spark.rdd.RDD
import org.apache.spark.streaming.dstream.{DStream, InputDStream}
import org.apache.spark.streaming.{Seconds, StreamingContext}

import scala.collection.mutable

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
  * QueuStreamAction
  * <p>
  */

object QueuStreamAction {
  def main(args: Array[String]): Unit = {
    // 创建 SparkConf
    val sc: SparkConf = new SparkConf().setMaster("local[*]").setAppName("QueuStreamAction")

    //创建 StreamingContext
    val ssc = new StreamingContext(sc, Seconds(3))

    // 创建RDD队列
    val rddQueue = new mutable.Queue[RDD[Int]]()

    // 创建 rddDStream
    val rddDStream: InputDStream[Int] = ssc.queueStream(rddQueue,false)

    // 统计计算
    val result: DStream[Int] = rddDStream.reduce(_ + _)

    // 输出日志信息
    result.print()

    // 启动流式任务
    ssc.start()

    // 循环创建RDD
    for (i <- 1 to 5) {
      rddQueue += ssc.sparkContext.makeRDD(1 to 100, 10)
      Thread.sleep(2000)
    }
    ssc.awaitTermination()
  }
}
```
 - 3.启动程序 查看日志信息
```
 -------------------------------------------
Time: 1559567436000 ms
-------------------------------------------
5050

-------------------------------------------
Time: 1559567439000 ms
-------------------------------------------
10100

-------------------------------------------
Time: 1559567442000 ms
-------------------------------------------
5050

-------------------------------------------
Time: 1559567445000 ms
-------------------------------------------
5050
```

##### 1.5.3.3 自定义数据源
###### 1.5.3.3.1 用法及说明
- 需要继承`Receiver`,并实现`onStart` & `onStop`方法来自定义数据源采集.
###### 1.5.3.3.2 案例实操	
- 需求 : 自定义数据源,实现监控某个端口号,获取该端口号内容.
- 1.Create `CustomizeReceiver.scala`
``` scala
package com.geekparkhub.core.spark.application.datastream

import java.io.{BufferedReader, InputStreamReader}
import java.net.Socket
import java.nio.charset.StandardCharsets

import org.apache.spark.storage.StorageLevel
import org.apache.spark.streaming.receiver.Receiver

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
  * CustomizeReceiver
  * <p>
  */

class CustomizeReceiver(hostName: String, port: Int) extends Receiver[String](StorageLevel.MEMORY_ONLY) {

  // 开始读取数据
  override def onStart(): Unit = {
    new Thread("receiver") {
      override def run(): Unit = {
        receiver()
      }
    }.start()
  }

  // 读取数据
  def receiver(): Unit = {
    try {
      // 创建 Socket
      val socket = new Socket(hostName, port)
      // 定义变量,用来接收端口传过来的数据
      var input: String = null
      // 创建BufferedReader用于读取端口传来的数据
      val reader = new BufferedReader(new InputStreamReader(socket.getInputStream, StandardCharsets.UTF_8))
      // 赋值
      input = reader.readLine()
      while (input != null) {
        store(input)
        input = reader.readLine()
      }
      // 跳出循环则关闭资源
      reader.close()
      socket.close()

      // 重启流式任务
      restart("restart")
    } catch {
      case e: Exception => restart("restart")
    }
  }

  // 结束读取数据
  override def onStop(): Unit = {}
}
```
- 2.Create `CustomizeReceiverAction.scala`
``` scala
package com.geekparkhub.core.spark.application.datastream

import org.apache.spark.SparkConf
import org.apache.spark.streaming.dstream.{DStream, ReceiverInputDStream}
import org.apache.spark.streaming.{Seconds, StreamingContext}

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
  * CustomizeReceiverAction
  * <p>
  */

object CustomizeReceiverAction {
  def main(args: Array[String]): Unit = {
    // 创建 SparkConf
    val sc: SparkConf = new SparkConf().setMaster("local[*]").setAppName("CustomizeReceiverAction")

    //创建 StreamingContext
    val ssc = new StreamingContext(sc, Seconds(3))

    val lineDStream: ReceiverInputDStream[String] = ssc.receiverStream(new CustomizeReceiver("systemhub511", 9999))

    // 将行数据转换为单词
    val wordDStream: DStream[String] = lineDStream.flatMap(_.split(" "))

    // 将单词住转换为元祖
    val wordAndOneDStream: DStream[(String, Int)] = wordDStream.map((_, 1))

    // 统计单词出现个数
    val DStreamResult: DStream[(String, Int)] = wordAndOneDStream.reduceByKey(_ + _)

    // 输出日志信息
    DStreamResult.print()

    // 启动流式任务
    ssc.start()
    ssc.awaitTermination()
  }
}
```
- 3.启动程序并通过NetCat发送数据
```
[root@systemhub511 spark]# nc -lk 9999CustomizeReceiverAction
CustomizeReceiverAction
CustomizeReceiver      
CustomizeReceiver      
CustomizeReceiv
```
- 4.查看日志信息
```
-------------------------------------------
Time: 1559570220000 ms
-------------------------------------------

Time: 1559570226000 ms
-------------------------------------------
(CustomizeReceiverAction,1)

-------------------------------------------
Time: 1559570229000 ms
-------------------------------------------
(CustomizeReceiverAction,1)
(CustomizeReceiver,1)

-------------------------------------------
Time: 1559570232000 ms
-------------------------------------------
(CustomizeReceiver,1)

-------------------------------------------
Time: 1559570238000 ms
-------------------------------------------
(CustomizeReceiv,1)
```



##### 1.5.3.4 Kafka数据源
###### 1.5.3.4.1 用法及说明
- 在工程中需要引入Maven工件`spark-streaming-kafka_2.10`来使用它,包内提供的KafkaUtils对象可以在StreamingContext和JavaStreamingContext中以Kafka消息创建出DStream.
- 
- 由于KafkaUtils可以订阅多个主题,因此它创建出的DStream由成对的主题和消息组成,要创建出一个流数据,需要使用StreamingContext实例、一个由逗号隔开的ZooKeeper主机列表字符串、消费者组的名字(唯一名字),以及一个从主题到针对这个主题的接收器线程数的映射表来调用createStream()方法.

###### 1.5.3.4.2 案例实操
- 需求 : 通过SparkStreaming从Kafka读取数据,并将读取过来数据做简单计算(WordCount),最终将信息打印至控制台.
- 1.追加依赖信息
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
        <module>spark-core</module>
        <module>spark-sql</module>
        <module>spark-streaming</module>
    </modules>

    <dependencies>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-core_2.11</artifactId>
            <version>2.1.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-sql_2.11</artifactId>
            <version>2.1.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive_2.11</artifactId>
            <version>2.1.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.hive</groupId>
            <artifactId>hive-exec</artifactId>
            <version>1.2.1</version>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.15</version>
        </dependency>
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
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-streaming_2.11</artifactId>
            <version>2.1.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-streaming-kafka_2.11</artifactId>
            <version>1.6.3</version>
        </dependency>
    </dependencies>
</project>
```
- 2.Create `KafkaSparkStreamingAction.scala`
```
package com.geekparkhub.core.spark.application.datastream

import kafka.serializer.StringDecoder
import org.apache.kafka.clients.consumer.ConsumerConfig
import org.apache.spark.SparkConf
import org.apache.spark.storage.StorageLevel
import org.apache.spark.streaming.dstream.ReceiverInputDStream
import org.apache.spark.streaming.kafka.KafkaUtils
import org.apache.spark.streaming.{Seconds, StreamingContext}

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
  * KafkaSparkStreamingAction
  * <p>
  */

object KafkaSparkStreamingAction {
  def main(args: Array[String]): Unit = {
    // 创建 SparkConf
    val sc: SparkConf = new SparkConf().setMaster("local[*]").setAppName("KafkaSparkStreamingAction")

    //创建 StreamingContext
    val ssc = new StreamingContext(sc, Seconds(3))

    // 声明 Kafka参数
    val zookeeper = "systemhub511:2181,systemhub611:2181,systemhub711:2181"
    val topic = "topic001"
    val consumerGroup = "spark"

    // 定义 Kafka参数
    val kafkaPara: Map[String, String] = Map[String, String](
      ConsumerConfig.GROUP_ID_CONFIG -> consumerGroup,
      "zookeeper.connect" -> zookeeper,
      ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG -> "org.apache.kafka.common.serialization.StringDeserializer",
      ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG -> "org.apache.kafka.common.serialization.StringDeserializer"
    )

    // 创建 KafkaDStream
    val KafkaDStream: ReceiverInputDStream[(String, String)] = KafkaUtils.createStream[String, String, StringDecoder, StringDecoder](ssc, kafkaPara, Map(topic -> 1), StorageLevel.MEMORY_ONLY)

    // 输出日志信息
    KafkaDStream.print()

    // 启动流式任务
    ssc.start()
    ssc.awaitTermination()
  }
}
```

- 3.检索所有 kafka topic
```
[root@systemhub511 kafka]# bin/kafka-topics.sh --list --zookeeper systemhub511:2181
__consumer_offsets
ct
topic001
topic002
topic003
topic004
```
- 4.开启数据生产者服务
```
[root@systemhub511 kafka]# bin/kafka-console-producer.sh --broker-list systemhub511:9092 --topic topic001
>
```
- 5.初次启动程序 | 运行时出现异常
```
Exception in thread "main" java.lang.NoClassDefFoundError: org/apache/spark/Logging
```
- 5.1 解决方案 : 在项目中创建`org.apache.spark`包,并创建`Logging`实体即可
```
package org.apache.spark

import org.apache.log4j.{LogManager, PropertyConfigurator}
import org.slf4j.{Logger, LoggerFactory}
import org.slf4j.impl.StaticLoggerBinder
import org.apache.spark.annotation.DeveloperApi
import org.apache.spark.util.Utils

/** :: DeveloperApi ::
  * Utility trait for classes that want to log data. Creates a SLF4J logger for the class and allows
  * logging messages at different levels using methods that only evaluate parameters lazily if the
  * log level is enabled.
  *
  * NOTE: DO NOT USE this class outside of Spark. It is intended as an internal utility.
  * This will likely be changed or removed in future releases.
  */
@DeveloperApi
trait Logging {
  // Make the log field transient so that objects with Logging can
  // be serialized and used on another machine
  @transient private var log_ : Logger = null

  // Method to get the logger name for this object
  protected def logName = {
    // Ignore trailing $'s in the class names for Scala objects
    this.getClass.getName.stripSuffix("$")
  }

  // Method to get or create the logger for this object
  protected def log: Logger = {
    if (log_ == null) {
      initializeIfNecessary()
      log_ = LoggerFactory.getLogger(logName)
    }
    log_
  }

  // Log methods that take only a String
  protected def logInfo(msg: => String) {
    if (log.isInfoEnabled) log.info(msg)
  }

  protected def logDebug(msg: => String) {
    if (log.isDebugEnabled) log.debug(msg)
  }

  protected def logTrace(msg: => String) {
    if (log.isTraceEnabled) log.trace(msg)
  }

  protected def logWarning(msg: => String) {
    if (log.isWarnEnabled) log.warn(msg)
  }

  protected def logError(msg: => String) {
    if (log.isErrorEnabled) log.error(msg)
  }

  // Log methods that take Throwables (Exceptions/Errors) too
  protected def logInfo(msg: => String, throwable: Throwable) {
    if (log.isInfoEnabled) log.info(msg, throwable)
  }

  protected def logDebug(msg: => String, throwable: Throwable) {
    if (log.isDebugEnabled) log.debug(msg, throwable)
  }

  protected def logTrace(msg: => String, throwable: Throwable) {
    if (log.isTraceEnabled) log.trace(msg, throwable)
  }

  protected def logWarning(msg: => String, throwable: Throwable) {
    if (log.isWarnEnabled) log.warn(msg, throwable)
  }

  protected def logError(msg: => String, throwable: Throwable) {
    if (log.isErrorEnabled) log.error(msg, throwable)
  }

  protected def isTraceEnabled(): Boolean = {
    log.isTraceEnabled
  }

  private def initializeIfNecessary() {
    if (!Logging.initialized) {
      Logging.initLock.synchronized {
        if (!Logging.initialized) {
          initializeLogging()
        }
      }
    }
  }

  private def initializeLogging() {
    // Don't use a logger in here, as this is itself occurring during initialization of a logger
    // If Log4j 1.2 is being used, but is not initialized, load a default properties file
    val binderClass = StaticLoggerBinder.getSingleton.getLoggerFactoryClassStr
    // This distinguishes the log4j 1.2 binding, currently
    // org.slf4j.impl.Log4jLoggerFactory, from the log4j 2.0 binding, currently
    // org.apache.logging.slf4j.Log4jLoggerFactory
    val usingLog4j12 = "org.slf4j.impl.Log4jLoggerFactory".equals(binderClass)

    lazy val isInInterpreter: Boolean = {
      try {
        val interpClass = classForName("org.apache.spark.repl.Main")
        interpClass.getMethod("interp").invoke(null) != null
      } catch {
        case _: ClassNotFoundException => false
      }
    }

    def classForName(className: String): Class[_] = {
      Class.forName(className, true, getContextOrSparkClassLoader)
      // scalastyle:on classforname
    }

    def getContextOrSparkClassLoader: ClassLoader =
      Option(Thread.currentThread().getContextClassLoader).getOrElse(getSparkClassLoader)

    def getSparkClassLoader: ClassLoader = getClass.getClassLoader

    if (usingLog4j12) {
      val log4j12Initialized = LogManager.getRootLogger.getAllAppenders.hasMoreElements
      if (!log4j12Initialized) {
        // scalastyle:off println
        if (isInInterpreter) {
          val replDefaultLogProps = "org/apache/spark/log4j-defaults-repl.properties"
          Option(Utils.getSparkClassLoader.getResource(replDefaultLogProps)) match {
            case Some(url) =>
              PropertyConfigurator.configure(url)
              System.err.println(s"Using Spark's repl log4j profile: $replDefaultLogProps")
              System.err.println("To adjust logging level use sc.setLogLevel(\"INFO\")")
            case None =>
              System.err.println(s"Spark was unable to load $replDefaultLogProps")
          }
        } else {
          val defaultLogProps = "org/apache/spark/log4j-defaults.properties"
          Option(Utils.getSparkClassLoader.getResource(defaultLogProps)) match {
            case Some(url) =>
              PropertyConfigurator.configure(url)
              System.err.println(s"Using Spark's default log4j profile: $defaultLogProps")
            case None =>
              System.err.println(s"Spark was unable to load $defaultLogProps")
          }
        }
        // scalastyle:on println
      }
    }
    Logging.initialized = true

    // Force a call into slf4j to initialize it. Avoids this happening from multiple threads
    // and triggering this: http://mailman.qos.ch/pipermail/slf4j-dev/2010-April/002956.html
    log
  }
}

private object Logging {
  @volatile private var initialized = false
  val initLock = new Object()
  try {
    // We use reflection here to handle the case where users remove the
    // slf4j-to-jul bridge order to route their logs to JUL.
    val bridgeClass = Utils.classForName("org.slf4j.bridge.SLF4JBridgeHandler")
    bridgeClass.getMethod("removeHandlersForRootLogger").invoke(null)
    val installed = bridgeClass.getMethod("isInstalled").invoke(null).asInstanceOf[Boolean]
    if (!installed) {
      bridgeClass.getMethod("install").invoke(null)
    }
  } catch {
    case e: ClassNotFoundException => // can't log anything yet so just fail silently
  }
}
```
- 6.再次启动程序
```
-------------------------------------------
Time: 1559624490000 ms
-------------------------------------------
```
- 7.向Kafka数据生产者写入数据
```
[root@systemhub511 kafka]# bin/kafka-console-producer.sh --broker-list systemhub511:9092 --topic topic001
>top001
>top002
>top003
>top004
>top005
>top006
```
- 8.查看日志信息
```
-------------------------------------------
Time: 1559624499000 ms
-------------------------------------------
(null,top001)

-------------------------------------------
Time: 1559624502000 ms
-------------------------------------------
(null,top002)

-------------------------------------------
Time: 1559624505000 ms
-------------------------------------------
(null,top003)

-------------------------------------------
Time: 1559624508000 ms
-------------------------------------------
(null,top004)

-------------------------------------------
Time: 1559624511000 ms
-------------------------------------------
(null,top005)

-------------------------------------------
Time: 1559624514000 ms
-------------------------------------------
(null,top006)
```

#### 1.5.4  DataStream 转换
- DStream上的原语与RDD类似,分为`Transformations(转换)`和`Output Operations()输出)`两种,此外转换操作中还有一些比较特殊原语,如 : `updateStateByKey()`、`transform()`以及各种Window相关原语.

##### 1.5.4.1 无状态转化操作
> 无状态转化操作就是把简单的RDD转化操作应用到每个批次上,也就是转化DStream中的每一个RDD,部分无状态转化操作列在了下表中,注意针对键值对的DStream转化操作(比如`reduceByKey()`)要添加`import StreamingContext._`才能在Scala中使用.

| 函数名称 |   作用 |   Scala实例 | 用来操作DStream[T]用户自定义函数 函数签名 |
| :--------: | :--------:| :------: | :------: |
| map()    |   对DStream中的每个元素应用到给定函数,返回由各个元素输出的元素的DStream. |  ds.map(x => x + 1)  |  f:(T) -> U  |
| flatMap()    |   对DStream中的每个元素应用给定函数,返回有各个元素输出迭代器组成的DStream. |  ds.flatMap(x => x.split(" "))  |  f: T -> Iterable[U] |
| filter()    |   返回由给定DStream中通过筛选的元素组成的DStream. |  ds.filter(x => x != 1)  |  f: T -> Boolean  |
| repartition()    |   改变DStream分区数 |  ds.repartition(10)  |  N/A  |
| reduceByKey()    |   将每个批次中间相同的记录规约 |  ds.reduceByKey((x,y) => x + y)  |  f:T , T -> T  |
| groupByKey()    | 将每个批次中的记录根据键分组   | ds.groupByKey()  |  N/A  |

> 需要记住的是,尽管这些函数看起来像作用在整个流上一样,但事实上每个DStream在内部是由许多RDD(批次)组成,且无状态转化操作是分别应用到每个RDD上的,例如`reduceByKey()`会归约每个时间区间中数据,但不会归约不同区间之间数据.
> 
> 举个例子,在之前的wordcount程序中,只会统计1秒内接收到的数据单词个数,而不会累加.
> 
> 无状态转化操作也能在多个DStream间整合数据,不过也是在各个时间区间内,例如键值对DStream拥有和RDD一样的与连接相关的转化操作,也就是`cogroup()` / `join()` / `leftOuterJoin()`等,可以在DStream上使用这些操作,这样就对每个批次分别执行了对应的RDD操作.
> 还可以像在常规的Spark中一样使用DStream的`union()`操作将它和另一个DStream 的内容合并起来,也可以使用StreamingContext.union()来合并多个流.

##### 1.5.4.2 有状态转化操作
###### 1.5.4.2.1 UpdateStateByKey
> UpdateStateByKey原语用于记录历史记录,有时需要在DStream中跨批次维护状态(例如流计算中累加wordcount),针对这种情况,`updateStateByKey()`提供了对一个状态变量的访问,用于键值对形式DStream,给定一个由(键,事件)对构成DStream,并传递一个指定如何根据新的事件更新每个键对应状态的函数,它可以构建出一个新的DStream,其内部数据为(键,状态) 对.
> 
> `updateStateByKey()`结果会是一个新的DStream,其内部的RDD序列是由每个时间区间对应的(键,状态)对组成.
> 
> `updateStateByKey`操作可以在用新信息进行更新时保持任意状态,为使用这个功能，只需要做下面两步 : 
> 1. 定义状态,状态可以是一个任意数据类型.
> 2.定义状态更新函数,用此函数阐明如何使用之前状态和来自输入流新值对状态进行更新.
> 使用`updateStateByKey`需要对检查点目录进行配置,会使用检查点来保存状态.
> 更新版的wordcount

- 1.定义有状态转化操作 | Create `UpdateStateByKeyWordCounAction.scala`
``` scala
package com.geekparkhub.core.spark.application.example

import org.apache.spark.SparkConf
import org.apache.spark.streaming.{Seconds, StreamingContext}
import org.apache.spark.streaming.dstream.{DStream, ReceiverInputDStream}

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
  * UpdateStateByKeyWordCounAction
  * <p>
  */

object UpdateStateByKeyWordCounAction {
  def main(args: Array[String]): Unit = {

    // 创建 SparkConf
    val sc: SparkConf = new SparkConf().setMaster("local[*]").setAppName("UpdateStateByKeyWordCounAction")

    //创建 StreamingContext
    val ssc = new StreamingContext(sc, Seconds(3))

    // 创建缓存目录检查站
    ssc.checkpoint("./ck")

    // 创建 DStream
    val lineDStream: ReceiverInputDStream[String] = ssc.socketTextStream("systemhub511", 9999)

    // 将行数据转换为单词
    val wordDStream: DStream[String] = lineDStream.flatMap(_.split(" "))

    // 将单词住转换为元祖
    val wordAndOneDStream: DStream[(String, Int)] = wordDStream.map((_, 1))

    /**
      * 定义更新状态方法
      * 参数 values为当前批次单词频度
      * 参数 state为以往批次单词频度
      */
    val updateFunc = (values: Seq[Int], state: Option[Int]) => {
      val count: Int = values.sum
      val perCount: Int = state.getOrElse(0)
      Some(count + perCount)
    }

    // 统计单词出现个数
    val DStreamResult: DStream[(String, Int)] = wordAndOneDStream.updateStateByKey(updateFunc)

    // 输出日志信息
    DStreamResult.print()

    // 启动流式任务
    ssc.start()
    ssc.awaitTermination()
  }
}
```
- 2.启动程序并通过NetCat发送数据
```
[root@systemhub511 spark]# nc -kl 9999
hello
hello
hello
geek
geek
hello
hey
hey
test
test
hello
```
- 3.查看日志信息
```
-------------------------------------------
Time: 1559643684000 ms
-------------------------------------------
(hello,1)

-------------------------------------------
Time: 1559643687000 ms
-------------------------------------------
(hello,1)

-------------------------------------------
Time: 1559643690000 ms
-------------------------------------------
(hello,3)

-------------------------------------------
Time: 1559643693000 ms
-------------------------------------------
(hello,3)
(geek,1)

-------------------------------------------
Time: 1559643696000 ms
-------------------------------------------
(hello,3)
(geek,2)

-------------------------------------------
Time: 1559643699000 ms
-------------------------------------------
(hello,4)
(geek,2)

-------------------------------------------
Time: 1559643702000 ms
-------------------------------------------
(hello,4)
(geek,2)
(hey,1)

-------------------------------------------
Time: 1559643705000 ms
-------------------------------------------
(hello,4)
(geek,2)
(hey,2)

-------------------------------------------
Time: 1559643708000 ms
-------------------------------------------
(hello,4)
(test,2)
(geek,2)
(hey,2)

-------------------------------------------
Time: 1559643711000 ms
-------------------------------------------
(hello,5)
(test,2)
(geek,2)
(hey,2)
```

###### 1.5.4.2.2 Window Operations
> `Window Operations`有点类似于Storm中`State`,可以设置窗口大小和滑动窗口间隔来动态获取当前Steaming允许状态.
> 
> 基于窗口操作会在一个比`StreamingContext`的批次间隔更长时间范围内,通过整合多个批次结果,计算出整个窗口的结果.

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_029.jpg)

> 所有基于窗口操作都需要两个参数,分别为窗口时长以及滑动步长,两者都必须是`StreamContext` 批次间隔整数倍,窗口时长控制每次计算最近多少个批次数据,其实就是最近的windowDuration/batchInterval个批次.
> 
> 如果有一个以10秒为批次间隔源DStream,要创建一个最近30秒时间窗口(即最近3个批次),就应当把windowDuration设为30秒,而滑动步长默认值与批次间隔相等,用来控制对新的DStream进行计算间隔,如果源DStream批次间隔为10秒,并且只希望每两个批次计算一次窗口结果,就应该把滑动步长设置为20秒.
> 
> 假设每隔十秒对持续30秒数据生成wordcount,为做到这个需要在持续30秒数据的(word,1)对DStream上应用reduceByKey,使用操作`reduceByKeyAndWindow`
```
reduce last 30 seconds of data, every 10 secondwindowedWordCounts = pairs.reduceByKeyAndWindow(lambda x, y: x + y, lambda x, y: x -y, 30, 20)
```
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_030.jpg)

> 关于Window操作有如下原语 : 
> 1.`window(windowLength,slideInterval)` : 基于对源DStream窗化批次进行计算返回一个新的Dstream.
> 
> 2.`countByWindow(windowLength,slideInterval)` ：返回滑动窗口计数流中的元素.
> 
> 3.`reduceByWindow(func,windowLength,slideInterval)` ：通过使用自定义函数整合滑动区间流元素来创建一个新的单元素流.
> 
> 4.`reduceByKeyAndWindow(func,windowLength,slideInterval, [numTasks])` ：当(K,V)对的DStream上调用此函数,会返回一个新(K,V)对的DStream,此处通过对滑动窗口中批次数据使用reduce函数来整合每个key的value值,`Note`:默认情况下,这个操作使用Spark默认数量并行任务(本地是2),在集群模式中依据配置属性(`spark.default.parallelism`)来做grouping,可以通过设置可选参数`numTasks`来设置不同数量tasks.
> 
> 5.`reduceByKeyAndWindow(func,invFunc,windowLength,slideInterval, [numTasks])` ：这个函数是上述函数更高效版本,每个窗口reduce值都是通过用前一个窗的reduce值来递增计算,通过reduce进入到滑动窗口数据并”反向reduce”离开窗口的旧数据来实现这个操作,一个例子是随着窗口滑动对keys的“加”“减”计数,这个函数只适用于”可逆的reduce函数”,也就是这些reduce函数有相应的”反reduce”函数(以参数`invFunc`形式传入),如前述函数reduce任务数量通过可选参数来配置,注意为了使用这个操作,检查点必须可用.
> 
> 6.`countByValueAndWindow(windowLength,slideInterval, [numTasks])` ：对(K,V)对的DStream调用,返回(K,Long)对的新DStream,其中每个key值是其在滑动窗口中频率,如上可配置reduce任务数量.
> 
> `reduceByWindow()`和`reduceByKeyAndWindow()`可以对每个窗口更高效地进行归约操作,它们接收一个归约函数,在整个窗口上执行,比如+除此以外,它们还有一种特殊形式,通过只考虑新进入窗口数据和离开窗口数据,让Spark增量计算归约结果,这种特殊形式需要提供归约函数的一个逆函数,比如+对应的逆函数为-,对于较大的窗口,提供逆函数可以大大提高执行效率.
> 
> `countByWindow()`和`countByValueAndWindow()`作为对数据进行计数操作的简写,`countByWindow()`返回一个表示每个窗口中元素个数的DStream,而`countByValueAndWindow()`返回的DStream则包含窗口中每个值的个数.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_031.jpg)

- 1.Create `WindowOperationsWordCountAction.scala`
``` scala
package com.geekparkhub.core.spark.application.example

import org.apache.spark.SparkConf
import org.apache.spark.streaming.{Seconds, StreamingContext}
import org.apache.spark.streaming.dstream.{DStream, ReceiverInputDStream}


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
  * WindowOperationsWordCountAction
  * <p>
  */

object WindowOperationsWordCountAction {
  def main(args: Array[String]): Unit = {
    // 创建 SparkConf
    val sc: SparkConf = new SparkConf().setMaster("local[*]").setAppName("WindowOperationsWordCountAction")

    //创建 StreamingContext
    val ssc = new StreamingContext(sc, Seconds(3))

    // 创建缓存目录检查站
    ssc.checkpoint("./ck")

    // 创建 DStream
    val lineDStream: ReceiverInputDStream[String] = ssc.socketTextStream("systemhub511", 9999)

    // 将行数据转换为单词
    val wordDStream: DStream[String] = lineDStream.flatMap(_.split(" "))

    // 将单词住转换为元祖
    val wordAndOneDStream: DStream[(String, Int)] = wordDStream.map((_, 1))

    // 统计单词出现个数
    val DStreamResult: DStream[(String, Int)] = wordAndOneDStream.reduceByKeyAndWindow((x: Int, y: Int) => x + y, Seconds(6), Seconds(3))

    // 输出日志信息
    DStreamResult.print()

    // 启动流式任务
    ssc.start()
    ssc.awaitTermination()
  }
}
```

- 2.启动程序并通过NetCat发送数据
```
[root@systemhub511 spark]# nc -kl 9999
sparkstreaming sparkcore sparksql spark
sparkstreaming sparkcore sparksql spark
sparkstreaming sparkcore sparksql spark
sparkstreaming sparkcore sparksql spark
sparkstreaming sparkcore sparksql spark
sparkstreaming sparkcore sparksql spark
sparkstreaming sparkcore sparksql spark
sparkstreaming sparkcore sparksql spark
sparkstreaming sparkcore sparksql spark
sparkstreaming sparkcore sparksql spark
sparkstreaming sparkcore sparksql spark
sparkstreaming sparkcore sparksql spark
```

- 3.查看日志信息
```
-------------------------------------------
Time: 1559652894000 ms
-------------------------------------------

-------------------------------------------
Time: 1559652897000 ms
-------------------------------------------
(sparksql,1)
(sparkcore,1)
(spark,1)
(sparkstreaming,1)

-------------------------------------------
Time: 1559652900000 ms
-------------------------------------------
(sparksql,3)
(sparkcore,3)
(spark,3)
(sparkstreaming,3)

-------------------------------------------
Time: 1559652903000 ms
-------------------------------------------
(sparksql,7)
(sparkcore,7)
(spark,7)
(sparkstreaming,7)

-------------------------------------------
Time: 1559652906000 ms
-------------------------------------------
(sparksql,8)
(sparkcore,8)
(spark,8)
(sparkstreaming,8)

-------------------------------------------
Time: 1559652909000 ms
-------------------------------------------
(sparksql,3)
(sparkcore,3)
(spark,3)
(sparkstreaming,3)

-------------------------------------------
Time: 1559652912000 ms
-------------------------------------------

-------------------------------------------
```

##### 1.5.4.3 其他重要操作
###### 1.5.4.3.1 Transform
> Transform原语允许DStream上执行任意`RDD-to-RDD`函数,即使这些函数并没有在DStreamAPI中暴露出来,通过该函数可以方便的扩展Spark API,该函数每一批次调度一次,其实也就是对DStream中的RDD应用转换.

###### 1.5.4.3.2 Join
> 连接操作(`leftOuterJoin` / `rightOuterJoin` / `fullOuterJoin`)也可以连接`Stream-Stream`,`windows-stream to windows-stream` / `stream-dataset`


#### 1.5.5 DataStream 输出
> 输出操作指定对流数据经转化操作得到的数据所要执行的操作(例如把结果推入外部数据库或输出到屏幕上),与RDD中惰性求值类似,如果一个DStream及其派生DStream都没有被执行输出操作,那么这些DStream就都不会被求值,如果StreamingContext中没有设定输出操作,整个context就都不会启动.
> 
> 输出操作如下 : 
> 1.`print()` ：在运行流程序驱动结点上打印DStream中每一批次数据最开始10个元素,这用于开发和调试,在Python API中,同样的操作叫print().
> 
> 2.`saveAsTextFiles(prefix, [suffix])` ：以text文件形式存储这个DStream的内容,每一批次存储文件名基于参数中的prefix和suffix,`prefix-Time_IN_MS[.suffix]`
> 
> 3.`saveAsObjectFiles(prefix, [suffix])` ：以Java对象序列化方式将Stream中的数据保存为SequenceFiles,每一批次存储文件名基于参数中的为`prefix-TIME_IN_MS[.suffix]`,Python中目前不可用.
> 
> 4.`saveAsHadoopFiles(prefix, [suffix])` ：将Stream中数据保存为Hadoopfiles, 每一批次存储文件名基于参数中的为`prefix-TIME_IN_MS[.suffix]`,Python APIPython中目前不可用.
> 
> 5.`foreachRDD(func)` ：这是最通用的输出操作,即将函数func用于产生于stream每一个RDD,其中参数传入函数func应该实现将每一个RDD中数据推送到外部系统,如将RDD存入文件或者通过网络将其写入数据库,注意函数func在运行流应用驱动中被执行,同时其中一般函数RDD操作从而强制其对于流RDD的运算.
> 
> 通用输出操作`foreachRDD()`,它用来对DStream中的RDD运行任意计算,这和`transform()`有些类似,都可以访问任意RDD,在foreachRDD()中,可以重用Spark中实现的所有行动操作,比如常见的用例之一是把数据写到诸如MySQL的外部数据库中.
> 
> `注意`: 
> 1.连接不能写在driver层面
> 2.如果写在foreach则每个RDD都创建,得不偿失
> 3.增加foreachPartition,在分区创建


#### 1.5.5 DataStream Program
##### 1.5.5.1 累加器和广播变量
> `累加器(Accumulators)`和`广播变量(Broadcast variables)`不能从Spark Streaming的检查点中恢复,如果启用检查并也使用了累加器和广播变量,那么必须创建累加器和广播变量的延迟单实例从而在驱动因失效重启后可以被重新实例化.

##### 1.5.5.2 DataFrame ans SQL Operations
> 可以很容易地在流数据上使用DataFrames和SQL,必须使用SparkContext来创建StreamingContext要用的SQLContext,此外这一过程可以在驱动失效后重启,通过创建一个实例化SQLContext单实例来实现这个工作,每个RDD被转换为DataFrame,以临时表格配置并用SQL进行查询.

##### 1.5.5.3 Caching / Persistence
> 和RDDs类似,DStreams同样允许开发者将流数据保存在内存中,也就是说在DStream上使用`persist()`方法将会DStreams中的每个RDD保存在内存中,当DStream中数据要被多次计算时,这个非常有用(如在同样数据上的多次操作),对于像`reduceByWindow`和`reduceByKeyAndWindow`以及基于状态的(updateStateByKey)这种操作,保存是隐含默认的,因此即使开发者没有调用persist(),由基于窗操作产生的DStreams会自动保存在内存中.


## 🔥 2. Spark 高阶 🔥
### 2.1 Spark 内核解析

#### 2.1.1 Spark 内核概述	
> Spark内核泛指Spark核心运行机制,包括Spark核心组件的运行机制、Spark任务调度机制、Spark内存管理机制、Spark核心功能的运行原理等,熟练掌握Spark内核原理,能够帮助我们更好地完成Spark代码设计,并能够帮助我们准确锁定项目运行过程中出现的问题的症结所在.
##### 2.1.1.1 Spark核心组件回顾
###### 2.1.1.1.1 Driver
> Spark驱动器节点,用于执行Spark任务中的main方法,负责实际代码的执行工作.
> 
> Driver在Spark作业执行时主要负责 : 
> 
> 1.将用户程序转化为任务(job).
> 2.在Executor之间调度任务(task).
> 3.跟踪Executor的执行情况.
> 4.通过UI展示查询运行情况.

###### 2.1.1.1.2 Executor
> Spark Executor节点是一个JVM进程,负责在Spark作业中运行具体任务,任务彼此之间相互独立,Spark应用启动时,Executor节点被同时启动,并且始终伴随着整个Spark应用生命周期而存在,如果有Executor节点发生了故障或崩溃,Spark应用也可以继续执行,会将出错节点上的任务调度到其他Executor节点上继续运行.
> 
> Executor有两个核心功能 : 
> 
> 1.负责运行组成Spark应用任务,并将结果返回给Driver进程.
> 2.它们通过自身的块管理器(Block Manager)为用户程序中要求缓存的RDD提供内存式存储,RDD是直接缓存在Executor进程内,因此任务可以在运行时充分利用缓存数据加速运算.

##### 2.1.1.2 Spark 通用运行流程概述
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_032.jpg)

> Spark通用运行流程,不论Spark以何种模式进行部署,任务提交后,都会先启动Driver进程,随后Driver进程向集群管理器注册应用程序,之后集群管理器根据此任务的配置文件分配Executor并启动,当Driver所需的资源全部满足后,Driver开始执行main函数,Spark查询为懒执行,当执行到action算子时开始反向推算,根据宽依赖进行stage划分,随后每一个stage对应一个taskset,taskset中有多个task,根据本地化原则,task会被分发到指定的Executor去执行,在任务执行的过程中,Executor也会不断与Driver进行通信,报告任务运行情况.

#### 2.1.2 Spark 部署模式
> Spark支持`3`种集群管理器 (ClusterManager),分别为 : 
> 
> 1.`Standalone` :` 独立模式`,Spark原生简单集群管理器,自带完整服务,可单独部署到一个集群中,无需依赖任何其他资源管理系统,使用Standalone可以很方便地搭建一个集群.
> 
> 2.`Apache Mesos` ：一个强大分布式资源管理框架,它允许多种不同的框架部署在其上,包括yarn.
> 
> 3.`HadoopYARN` ：统一资源管理机制,可以运行多套计算框架,如MapReduce/Storm等,根据driver在集群中的位置不同,分为YarnClient和YarnCluster.
> 
> 4.实际上除了上述这些通用的集群管理器外,Spark内部也提供了一些方便用户测试和学习的简单集群部署模式,由于在实际工厂环境下使用的绝大多数的集群管理器是HadoopYARN,因此我们关注的重点是HadoopYARN模式下的Spark集群部署.
> 
> 5.Spark运行模式取决于传递给SparkContext的MASTER环境变量的值,个别模式还需要辅助的程序接口来配合使用,目前支持的Master字符串及URL.
> 
> 6.Spark运行模式配置表
> | Master URL |  Meaning |
> | :--------: | :--------:|
> | `local`    |   在本地运行,只有一个工作进程,无并行计算能力. |
> | `local[K]`    |   在本地运行,有K个工作进程,通常设置K为机器CPU核心数量. |
> | `local[*]`    |   在本地运行,工作进程数量等于机器CPU核心数量. |
> | `spark://HOST:PORT`    |   以Standalone模式运行,这是Spark自身提供集群运行模式,默认端口号:7077,详细文档见:`Spark standalone cluster` |
> | `mesos://HOST:PORT`    |   在Mesos集群上运行,Driver进程和Worker进程运行在Mesos集群上,部署模式必须使用固定值:`--deploy-mode cluster`,详细文档见:`MesosClusterDispatcher` |
> | `yarn-client`    |   在Yarn集群上运行,Driver进程在本地,Work进程在Yarn集群上,部署模式必须使用固定值:`--deploy-modeclient`,Yarn集群地址必须在`HADOOP_CONF_DIRorYARN_CONF_DIR`变量里定义. |
> | `yarn-cluster`    |   在Yarn集群上运行,Driver进程在Yarn集群上,Work进程也在Yarn集群上,部署模式必须使用固定值:`--deploy-mode cluster`,Yarn集群地址必须在`HADOOP_CONF_DIRorYARN_CONF_DIR`变量里定义. |
> 
> 用户在提交任务给Spark处理时,以下两个参数共同决定了Spark运行方式.
> 
> 1.`–master MASTER_URL` ：决定了Spark任务提交给哪种集群处理.
> 
> 2.`–deploy-mode DEPLOY_MODE` ：决定了Driver的运行方式,可选值为Client或者Cluster

##### 2.1.2.1 Standalone 模式运行机制
> Standalone集群有四个重要组成部分,分别是 : 
> 
> 1.`Driver` ：是一个进程,编写Spark应用程序就运行在Driver上,由Driver进程执行.
> 
> 2.`Master` ：是一个进程,主要负责资源调度和分配,并进行集群监控等职责.
> 
> 3.`Worker` ：是一个进程,一个Worker运行在集群中的一台服务器上,主要负责两个职责,一个是用自己内存存储RDD某个或某些partition,另一个是启动其他进程和线程(Executor),对RDD上的partition进行并行的处理和计算.
> 
> 4.`Executor` ：是一个进程,一个Worker上可以运行多个Executor,Executor通过启动多个线程(task)来执行对RDD的partition进行并行计算,也就是执行RDD定义,例如map、flatMap、reduce等算子操作.

###### 2.1.2.1.1 Standalone Client 模式

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_033.jpg)
> 在Standalone Client模式下,Driver在任务提交的本地机器上运行,Driver启动后向Master注册应用程序,Master根据submit脚本资源需求找到内部资源至少可以启动一个Executor的所有Worker,然后在这些Worker之间分配Executor,Worker上Executor启动后会向Driver反向注册,所有Executor注册完成后,Driver开始执行main函数,之后执行到Action算子时,开始划分stage,每个stage生成对应的taskSet,之后将task分发到各个Executor上执行.
###### 2.1.2.1.2 Standalone Cluster 模式

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_034.jpg)

> 在Standalone Cluster模式下,任务提交后,Master会找到一个Worker启动Driver进程,Driver启动后向Master注册应用程序,Master根据submit脚本资源需求找到内部资源至少可以启动一个Executor的所有Worker,然后在这些Worker之间分配Executor,Worker上的Executor启动后会向Driver反向注册,所有Executor注册完成后,Driver开始执行main函数,之后执行到Action算子时,开始划分stage,每个stage生成对应的taskSet,之后将task分发到各个Executor上执行.
> 
> 注意 : Standalone两种模式下(`Client` / `Cluster`),Master在接到Driver注册Spark应用程序请求后,会获取其所管理的剩余资源能够启动一个Executor的所有Worker,然后在这些Worker之间分发Executor,此时分发只考虑Worker上资源是否足够使用,直到当前应用程序所需所有Executor都分配完毕,Executor反向注册完毕后,Driver开始执行main程序.

##### 2.1.2.2 YARN模式 运行机制 

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_035.jpg)
> 在YARNClient模式下,Driver在任务提交本地机器上运行,Driver启动后会和ResourceManager通讯申请启动ApplicationMaster,随后ResourceManager分配container,在合适的NodeManager上启动ApplicationMaster,此时的ApplicationMaster的功能相当于一个ExecutorLaucher,只负责向ResourceManager申请Executor内存.
> 
> ResourceManager接到ApplicationMaster资源申请后会分配container,然后ApplicationMaster在资源分配指定NodeManager上启动Executor进程,Executor进程启动后会向Driver反向注册,Executor全部注册完成后Driver开始执行main函数,之后执行到Action算子时,触发一个job,并根据宽依赖开始划分stage,每个stage生成对应的taskSet,之后将task分发到各个Executor上执行.

###### 2.1.2.2.1 YARN Cluster 模式

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_036.jpg)

> 在YARNCluster模式下,任务提交后会和ResourceManager通讯申请启动ApplicationMaster,随后ResourceManager分配container,在合适的NodeManager上启动ApplicationMaster,此时的ApplicationMaster就是Driver.
> 
> Driver启动后向ResourceManager申请Executor内存,ResourceManager接到ApplicationMaster的资源申请后会分配container,然后在合适的NodeManager上启动Executor进程,Executor进程启动后会向Driver反向注册,Executor全部注册完成后Driver开始执行main函数,之后执行到Action算子时,触发一个job,并根据宽依赖开始划分stage,每个stage生成对应的taskSet,之后将task分发到各个Executor上执行.

#### 2.1.3 Spark 通讯架构
##### 2.1.3.1 Spark 通信架构 概述
> Spark2.x版本使用Netty通讯框架作为内部通讯组件,spark基于Netty新rpc框架借鉴了Akka中的设计,它是基于Actor模型,如下图所示.
> 
> Actor模型
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_037.jpg)
> Spark通讯框架中各个组件(Client/Master/Worker)可以认为是一个个独立的实体,各个实体之间通过消息来进行通信,具体各个组件之间的关系图如下 : 
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_038.jpg)
> Endpoint(Client/Master/Worker)有1个InBox和N个OutBox(N>=1,N取决于当前Endpoint与多少其他的Endpoint进行通信,一个与其通讯的其他Endpoint对应一个OutBox),Endpoint接收到的消息被写入InBox,发送出去的消息写入OutBox并被发送到其他Endpoint的InBox中.

##### 2.1.3.2 Spark 通讯架构 解析
- Spark通信架构如下图所示 : 
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_039.jpg)
> 1.`RpcEndpoint` ：RPC端点,Spark针对每个节点(Client/Master/Worker)都称之为一个Rpc端点,且都实现RpcEndpoint接口,内部根据不同端点的需求,设计不同的消息和不同的业务处理,如果需要发送(询问)则调用Dispatcher.
> 
> 2.`RpcEnv` ：RPC上下文环境,每个RPC端点运行时依赖的上下文环境称为RpcEnv.
> 
> 3.`Dispatcher` ：消息分发器,针对于RPC端点需要发送消息或者从远程RPC接收到的消息,分发至对应的指令收件箱/发件箱,如果指令接收方是自己则存入收件箱,如果指令接收方不是自己,则放入发件箱.
> 
> 4.`Inbox` ：指令消息收件箱,一个本地RpcEndpoint对应一个收件箱,Dispatcher在每次向Inbox存入消息时,都将对应EndpointData加入内部ReceiverQueue中,另外Dispatcher创建时会启动一个单独线程进行轮询ReceiverQueue,进行收件箱消息消费.
> 
> 5.`RpcEndpointRef` ：RpcEndpointRef是对远程RpcEndpoint的一个引用,当需要向一个具体RpcEndpoint发送消息时,一般需要获取到该RpcEndpoint的引用然后通过该应用发送消息.
> 
> 6.`OutBox` ：指令消息发件箱,对于当前RpcEndpoint来说,一个目标RpcEndpoint对应一个发件箱,如果向多个目标RpcEndpoint发送信息,则有多个OutBox,当消息放入Outbox后,紧接着通过TransportClient将消息发送出去,消息放入发件箱以及发送过程是在同一个线程中进行.
> 
> 7.`RpcAddress` ：表示远程RpcEndpointRef地址,Host + Port
> 
> 8.`TransportClient` ：Netty通信客户端,一个OutBox对应一个TransportClient,TransportClient不断轮询OutBox,根据OutBox消息的receiver信息,请求对应的远程TransportServer.
> 
> 9.`TransportServer` ：Netty通信服务端,一个RpcEndpoint对应一个TransportServer,接受远程消息后调用Dispatcher分发消息至对应收发件箱.
> 
> 根据上面的分析,Spark通信架构的高层视图如下图所示 : 

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_040.jpg)

#### 2.1.4 Spark Context 解析
> 在Spark中由SparkContext负责与集群进行通讯、资源的申请以及任务的分配和监控等,当Worker节点中的Executor运行完毕Task后,Driver同时负责将SparkContext关闭,通常也可以使用SparkContext来代表驱动程序(Driver).
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_041.jpg)
> SparkContext是=通往Spark集群的唯一入口,可以用来在Spark集群中创建RDD、累加器和广播变量,SparkContext也是整个Spark应用程序中至关重要的一个对象,可以说是整个Application运行调度的核心(不包括资源调度).
> 
> SparkContext的核心作用是初始化Spark应用程序运行所需的核心组件,包括高层调度器(DAGScheduler)、底层调度器(TaskScheduler)和调度器的通信终端,(SchedulerBackend),同时还会负责Spark程序向ClusterManager的注册等.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_042.jpg)
> SparkContext初始化组件
> 在实际编码过程中,会先创建SparkConf实例,并对SparkConf的属性进行自定义设置,随后将SparkConf作为SparkContext类的唯一构造参数传入来完成SparkContext实例对象的创建.
> SparkContext在实例化过程中会初始化DAGScheduler、TaskScheduler和SchedulerBackend,当RDD的action算子触发了作业(Job)后,SparkContext会调用DAGScheduler根据宽窄依赖将Job划分成几个小的阶段(Stage),TaskScheduler会调度每个Stage任务(Task),另外SchedulerBackend负责申请和管理集群为当前Application分配的计算资源(即Executor).
> 
> 如果将SparkApplication比作汽车,那么SparkContext就是汽车引擎,而SparkConf就是引擎配置参数.
> 
> 下图描述Spark-On-Yarn模式下在任务调度期间,ApplicationMaster、Driver以及Executor内部模块的交互过程 :  Spark组件交互过程
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_043.jpg)
> Driver初始化SparkContext过程中,会分别初始化DAGScheduler / TaskScheduler / SchedulerBackend以及HeartbeatReceiver,并启动SchedulerBackend以及HeartbeatReceiver,SchedulerBackend通过ApplicationMaster申请资源,并不断从TaskScheduler中拿到合适的Task分发到Executor执行,HeartbeatReceiver负责接收Executor心跳信息,监控Executor的存活状况,并通知到TaskScheduler.


#### 2.1.5 Spark 任务调度机制
- 在工厂环境下,Spark集群的部署方式一般为YARN-Cluster模式,之后内核分析内容中默认集群部署方式为YARN-Cluster模式.

##### 2.1.5.1 Spark 任务提交 流程
- SparkYARN-Cluster模式下的任务提交流程
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_044.jpg)
- 时序图清晰地说明Spark应用程序从提交到运行的完整流程
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_045.jpg)
> 提交Spark应用程序,首先通过Client向ResourceManager请求启动一个Application,同时检查是否有足够的资源满足Application需求,如果资源条件满足,则准备ApplicationMaster的启动上下文,交给ResourceManager,并循环监控Application状态.
> 
> 当提交的资源队列中有资源时,ResourceManager会在某个NodeManager上启动ApplicationMaster进程,ApplicationMaster会单独启动Driver后台线程,当Driver启动后,ApplicationMaster会通过本地的RPC连接Driver,并开始向ResourceManager申请Container资源运行Executor进程(一个Executor对应与一个Container),当ResourceManager返回Container资源,ApplicationMaster则在对应的Container上启动Executor.
> 
> Driver线程主要是初始化SparkContext对象,准备运行所需的上下文,然后一方面保持与ApplicationMaster的RPC连接,通过ApplicationMaster申请资源,另一方面根据用户业务逻辑开始调度任务,将任务下发到已有的空闲Executor上.
> 
> 当ResourceManager向ApplicationMaster返回Container资源时,ApplicationMaster就尝试在对应的Container上启动Executor进程,Executor进程起来后,会向Driver反向注册,注册成功后保持与Driver的心跳,同时等待Driver分发任务,当分发的任务执行完毕后,将任务状态上报给Driver.
> 
> 从上述时序图可知,Client只负责提交Application并监控Application的状态,对于Spark的任务调度主要是集中在两个方面: 资源申请和任务分发,其主要是通过ApplicationMaster、Driver以及Executor之间来完成.

##### 2.1.5.2 Spark 任务调度 概述
> 当Driver起来后,Driver则会根据用户程序逻辑准备任务,并根据Executor资源情况逐步分发任务,在详细阐述任务调度前,首先说明下Spark里的几个概念,一个Spark应用程序包括Job、Stage以及Task三个概念.
> 1.Job是以Action方法为界,遇到一个Action方法则触发一个Job.
> 2.Stage是Job的子集,以RDD宽依赖(即Shuffle)为界,遇到Shuffle做一次划分.
> 3.Task是Stage的子集,以并行度(分区数)来衡量,分区数是多少,则有多少个task.
> 
> Spark任务调度总体来说分两路进行,一路是Stage级调度,一路是Task级调度,总体调度流程如下图所示 : Spark任务调度概览
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_046.jpg)
> Spark RDD通过其Transactions操作,形成了RDD血缘关系图,即DAG,最后通过Action的调用,触发Job并调度执行.
> DAGScheduler负责Stage级的调度,主要是将job切分成若干Stages,并将每个Stage打包成TaskSet交给TaskScheduler调度.
> TaskScheduler负责Task级的调度,将DAGScheduler给过来的TaskSet按照指定的调度策略分发到Executor上执行,调度过程中SchedulerBackend负责提供可用资源,其中SchedulerBackend有多种实现,分别对接不同的资源管理系统.

##### 2.1.5.3 Spark Stage级 调度
> Spark的任务调度是从DAG切割开始，主要是由DAGScheduler来完成。当遇到一个Action操作后就会触发一个Job的计算，并交给DAGScheduler来提交，下图是涉及到Job提交的相关方法调用流程图 : Job提交调用栈
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_047.jpg)
> Job由最终RDD和Action方法封装而成,SparkContext将Job交给DAGScheduler提交,它会根据RDD血缘关系构成的DAG进行切分,将一个Job划分为若干Stages,具体划分策略是，由最终RDD不断通过依赖回溯判断父依赖是否是宽依赖,即以Shuffle为界,划分Stage,窄依赖的RDD之间被划分到同一个Stage中,可以进行pipeline式计算,如上图紫色流程部分,划分的Stages分两类,一类叫做ResultStage,为DAG最下游的Stage,由Action方法决定,另一类叫做ShuffleMapStage,为下游Stage准备数据,下面看一个简单例子WordCount.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_048.jpg)
> Job由saveAsTextFile触发,该Job由RDD-3和saveAsTextFile方法组成,根据RDD之间的依赖关系从RDD-3开始回溯搜索,直到没有依赖的RDD-0,在回溯搜索过程中,RDD-3依赖RDD-2,并且是宽依赖,所以在RDD-2和RDD-3之间划分Stage,RDD-3被划到最后一个Stage,即ResultStage中,RDD-2依赖RDD-1,RDD-1依赖RDD-0,这些依赖都是窄依赖,所以将RDD-0、RDD-1和RDD-2划分到同一个Stage,即ShuffleMapStage中,实际执行的时候,数据记录会一气呵成地执行RDD-0到RDD-2的转化,不难看出其本质上是一个深度优先搜索算法.
> 
> 一个Stage是否被提交,需要判断它的父Stage是否执行,只有在父Stage执行完毕才能提交当前Stage,如果一个Stage没有父Stage,那么从该Stage开始提交,Stage提交时会将Task信息(分区信息以及方法等)序列化并被打包成TaskSet交给TaskScheduler,一个Partition对应一个Task,另一方面TaskScheduler会监控Stage的运行状态,只有Executor丢失或者Task由于Fetch失败才需要重新提交失败的Stage以调度运行失败任务,其他类型的Task失败会在TaskScheduler的调度过程中重试.
> 
> 相对来说DAGScheduler做事情较为简单,仅仅是在Stage层面上划分DAG,提交Stage并监控相关状态信息,TaskScheduler则相对较为复杂,下面详细阐述其细节.

##### 2.1.5.4 Spark Task级 调度
> SparkTask调度是由TaskScheduler来完成,由前文可知,DAGScheduler将Stage打包到TaskSet交给TaskScheduler,TaskScheduler会将TaskSet封装为TaskSetManager加入到调度队列中,TaskSetManager结构如下图所示 : TaskManager结构

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_049.jpg)
> TaskSetManager负责监控管理同一个Stage中的Tasks,TaskScheduler就是以TaskSetManager为单元来调度任务.
> 
> TaskScheduler初始化后会启动SchedulerBackend,它负责跟外界打交道,接收Executor的注册信息,并维护Executor的状态,所以说SchedulerBackend是管“粮食”的,同时它在启动后会定期地去“询问”TaskScheduler有没有任务要运行,也就是说它会定期地“问”TaskScheduler“我有这么余量,你要不要啊”,TaskScheduler在SchedulerBackend“问”它的时候,会从调度队列中按照指定的调度策略选择TaskSetManager去调度运行,大致方法调用流程如下图所示 : task调度流程
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_050.jpg)
> 将TaskSetManager加入rootPool调度池中之后,调用SchedulerBackend的riviveOffers方法给driverEndpoint发送ReviveOffer消息,driverEndpoint收到ReviveOffer消息后调用makeOffers方法,过滤出活跃状态的Executor(这些Executor都是任务启动时反向注册到Driver的Executor),然后将Executor封装成WorkerOffer对象,准备好计算资源(WorkerOffer)后,taskScheduler基于这些资源调用resourceOffer在Executor上分配task.

###### 2.1.5.4.1 调度策略
> TaskScheduler会先把DAGScheduler给过来的TaskSet封装成TaskSetManager扔到任务队列里,然后再从任务队列里按照一定的规则把它们取出来在SchedulerBackend给过来的Executor上运行m这个调度过程实际上还是比较粗粒度,是面向TaskSetManager.
> 
> 调度队列层次结构如下图所示 : FIFO调度策略内存结构
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_051.jpg)
> TaskScheduler是以树的方式来管理任务队列,树中的节点类型为Schdulable,叶子节点为TaskSetManager,非叶子节点为Pool,下图是它们之间的继承关系 : 任务队列继承关系
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_052.jpg)
> TaskScheduler支持两种调度策略,一种是FIFO,也是默认的调度策略,另一种是FAIR,在TaskScheduler初始化过程中会实例化rootPool,表示树的根节点,是Pool类型.
> 
> 1.`FIFO调度策略` | FIFO调度策略执行步骤如下
> 对s1和s2两个Schedulable的优先级(Schedulable类一个属性,记为priority,值越小,优先级越高).
> 如果两个Schedulable的优先级相同,则对s1,s2所属的Stage身份进行标识进行比较(Schedulable类的一个属性,记为priority,值越小,优先级越高)
> 如果比较的结果小于0,则优先调度s1,否则优先调度s2.
> FIFO调度策略内存结构
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_053.jpg)
> 2.`FAIR`调度策略 | FAIR调度策略的树结构如下图所示
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_054.jpg)
> FAIR模式中有一个rootPool和多个子Pool,各个子Pool中存储着所有待分配的TaskSetMagager.
> 
> 可以通过在Properties中指定`spark.scheduler.pool`属性,指定调度池中的某个调度池作为TaskSetManager的父调度池,如果根调度池不存在此属性值对应的调度池,会创建以此属性值为名称的调度池作为TaskSetManager的父调度池,并将此调度池作为根调度池的子调度池.
> 
> 在FAIR模式中,需要先对子Pool进行排序,再对子Pool里面的TaskSetMagager进行排序,因为Pool和TaskSetMagager都继承了Schedulable特质,因此使用相同的排序算法.
> 
> 排序过程的比较是基于Fair-share来比较的,每个要排序的对象包含三个属性 : runningTasks值(正在运行的Task数)、minShare值、weight值,比较时会综合考量runningTasks值,minShare值以及weight值.
> 
> 注意minShare、weight的值均在公平调度配置文件`fairscheduler.xml`中被指定,调度池在构建阶段会读取此文件的相关配置.
> 1.如果A对象的runningTasks大于它的minShare,B对象的runningTasks小于它的minShare,那么B排在A前面(runningTasks比minShare小的先执行).
> 
> 2.如果A、B对象的runningTasks都小于它们的minShare,那么就比较runningTasks与minShare的比值(minShare使用率),谁小谁排前面(minShare使用率低的先执行).
> 
> 3.如果A、B对象的runningTasks都大于它们的minShare,那么就比较runningTasks与weight的比值(权重使用率),谁小谁排前面(权重使用率低的先执行).
> 
> 4.如果上述比较均相等，则比较名字.
> 整体上来说就是通过minShare和weight这两个参数控制比较过程,可以做到让minShare使用率和权重使用率少(实际运行task比例较少)的先运行.
> FAIR模式排序完成后,所有的TaskSetManager被放入一个ArrayBuffer里,之后依次被取出并发送给Executor执行.
> 从调度队列中拿到TaskSetManager后,由于TaskSetManager封装了一个Stage的所有Task,并负责管理调度这些Task,那么接下来的工作就是TaskSetManager按照一定的规则一个个取出Task给TaskScheduler,TaskScheduler再交给SchedulerBackend去发到Executor上执行.

###### 2.1.5.4.2 本地化调度
> DAGScheduler切割Job,划分Stage,通过调用submitStage来提交一个Stage对应的tasks,submitStage会调用submitMissingTasks,submitMissingTasks确定每个需要计算的task的preferredLocations,通过调用`getPreferrdeLocations()`得到partition的优先位置,由于一个partition对应一个task,此partition的优先位置就是task的优先位置,对于要提交到TaskScheduler的TaskSet中的每一个task,该task优先位置与其对应的partition对应的优先位置一致.
> 
> 从调度队列中拿到TaskSetManager后,那么接下来的工作就是TaskSetManager按照一定的规则一个个取出task给TaskScheduler,TaskScheduler再交给SchedulerBackend去发到Executor上执行,TaskSetManager封装了一个Stage的所有task,并负责管理调度这些task.
> 
> 根据每个task的优先位置，确定task的Locality级别，Locality一共有五种，优先级由高到低顺序 : Spark本地化等级

> | 名称      |     解析 |
> | :--------: | :--------:|
> | `PROCESS_LOCAL`    |   进程本地化,task和数据在同一个Executor中,性能最好. |
> | `NODE_LOCAL`    |   节点本地化,task和数据在同一个节点中,但是task和数据不在同一个Executor中,数据需要在进程间进行传输. |
> | `RACK_LOCAL`    |   机架本地化,task和数据在同一个机架的两个节点上,数据需要通过网络在节点之间进行传输. |
> | `NO_PREF`    |   对于task来说,从哪里获取都一样,没有好坏之分 |
> | `ANY`    |   task和数据可以在集群的任何地方,而且不在一个机架中,性能最差 |
> 
> 在调度执行时,Spark调度总是会尽量让每个task以最高的本地性级别来启动,当一个task以X本地性级别启动,但是该本地性级别对应的所有节点都没有空闲资源而启动失败,此时并不会马上降低本地性级别启动而是在某个时间长度内再次以X本地性级别来启动该task,若超过限时时间则降级启动,去尝试下一个本地性级别,依次类推.
> 
> 可以通过调大每个类别的最大容忍延迟时间,在等待阶段对应的Executor可能就会有相应的资源去执行此task,这就在一定程度上提到了运行性能.

###### 2.1.5.4.3 失败重试与黑名单机制
> 除了选择合适的Task调度运行外,还需要监控Task的执行状态,与外部打交道的是SchedulerBackend,Task被提交到Executor启动执行后,Executor会将执行状态上报给SchedulerBackend,SchedulerBackend则告诉TaskScheduler,TaskScheduler找到该Task对应的TaskSetManager,并通知到该TaskSetManager,这样TaskSetManager就知道Task的失败与成功状态,对于失败的Task,会记录它失败的次数,如果失败次数还没有超过最大重试次数,那么就把它放回待调度的Task池子中,否则整个Application失败.
> 
> 在记录Task失败次数过程中,会记录它上一次失败所在的Executor Id和Host,这样下次再调度这个Task时,会使用黑名单机制,避免它被调度到上一次失败的节点上,起到一定的容错作用,黑名单记录Task上一次失败所在的Executor Id和Host,以及其对应的“拉黑”时间,“拉黑”时间是指这段时间内不要再往这个节点上调度这个Task了.

#### 2.1.6 Spark Shuffle 解析
##### 2.1.6.1 Shuffle 核心要点
###### 2.1.6.1.1 ShuffleMapStage与FinalStage
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_055.jpg)
> 在划分stage时,最后一个stage称为FinalStage,它本质上是一个ResultStage对象,前面的所有stage被称为ShuffleMapStage.
> 
> ShuffleMapStage的结束伴随着shuffle文件的写磁盘.
> ResultStage基本上对应代码中的action算子,即将一个函数应用在RDD的各个partition的数据集上,意味着一个job的运行结束.

###### 2.1.6.1.2 Shuffle 任务个数
> 1.map端task个数确定
> Shuffle过程中的task个数由RDD分区数决定，而RDD的分区个数与参数spark.default.parallelism有密切关系
> 在YarnCluster模式下，如果没有手动设置`spark.default.parallelism`
> ```
park.default.parallelism=  max(所有executor使用的core总数，2)
> ```
> 2. reduce端task个数确定
> Reduce端进行数据的聚合,一部分聚合算子可以手动指定reducetask的并行度,如果没有指定,则以map端的最后一个RDD的分区数作为其分区数,那么分区数就决定了reduce端的task的个数.

###### 2.1.6.1.3 reduce端数据读取
> 根据stage的划分,map端task和reduce端task不在相同的stage中,maptask位于ShuffleMapStage,reducetask位于ResultStage,maptask会先执行.
> 
> reduce端的数据拉取过程如下 : 
> 1.map task执行完毕后会将计算状态以及磁盘小文件位置等信息封装到mapStatue对象中,然后由本进程中的MapOutPutTrackerWorker对象将mapStatus对象发送给Driver进程的MapOutPutTrackerMaster对象.
> 2.在reduce task开始执行之前会先让本进程中的MapOutputTrackerWorker向Driver进程中的MapoutPutTrakcerMaster发动请求,请求磁盘小文件位置信息.
> 3.当所有的Map task执行完毕后,Driver进程中的MapOutPutTrackerMaster就掌握了所有的磁盘小文件的位置信息,此时MapOutPutTrackerMaster会告诉MapOutPutTrackerWorker磁盘小文件的位置信息.
> 4.完成之前的操作之后,由BlockTransforService去Executor所在的节点拉数据,默认会启动五个子线程,每次拉取的数据量不能超过48M(reduce task每次最多拉取48M数据,将拉来的数据存储到Executor内存的20%内存中).

##### 2.1.6.2 Hash Shuffle 解析
> 1.未经优化HashShuffleManager
> shuffle write阶段,主要就是在一个stage结束计算之后,为了下一个stage可以执行shuffle类的算子(比如reduceByKey),而将每个task处理的数据按key进行“划分”,所谓“划分”就是对相同的key执行hash算法,从而将相同key都写入同一个磁盘文件中,而每一个磁盘文件都只属于下游stage的一个task,在将数据写入磁盘之前,会先将数据写入内存缓冲中,当内存缓冲填满之后才会溢写到磁盘文件中去.
> 
> 下一个stage的task有多少个,当前stage的每个task就要创建多少份磁盘文件,比如下一个stage总共有100个task,那么当前stage的每个task都要创建100份磁盘文件,如果当前stage有50个task,总共有10个Executor,每个Executor执行5个task,那么每个Executor上总共就要创建500个磁盘文件,所有Executor上会创建5000个磁盘文件,由此可见,未经优化的shuffle write操作所产生的磁盘文件的数量是极其惊人.
> 
> shuffle read阶段,通常就是一个stage刚开始时要做的事情,此时该stage的每一个task就需要将上一个stage的计算结果中的所有相同key,从各个节点上通过网络都拉取到自己所在的节点上,然后进行key的聚合或连接等操作,由于shuffle write的过程中,maptask给下游stage的每个reducetask都创建了一个磁盘文件,因此shuffle read的过程中,每个reducetask只要从上游stage的所有maptask所在节点上,拉取属于自己的那一个磁盘文件即可.
> shuffle read的拉取过程是一边拉取一边进行聚合,每个shuffle read task都会有一个自己的buffer缓冲,每次都只能拉取与buffer缓冲相同大小的数据,然后通过内存中的一个Map进行聚合等操作,聚合完一批数据后,再拉取下一批数据,并放到buffer缓冲中进行聚合操作,以此类推,直到最后将所有数据到拉取完,并得到最终的结果.
> 未优化HashShuffleManager工作原理图 : 
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_056.jpg)

> 2.优化后 HashShuffleManager
> 为了优化HashShuffleManager可以设置一个参数,`spark.shuffle.consolidateFiles`,该参数默认值为false,将其设置为true即可开启优化机制,通常来说,如果使用HashShuffleManager,那么都建议开启这个选项.
> 
> 开启consolidate机制之后,在shuffle write过程中,task就不是为下游stage的每个task创建一个磁盘文件了,此时会出现shuffleFileGroup的概念,每个shuffleFileGroup会对应一批磁盘文件,磁盘文件的数量与下游stage的task数量是相同的,一个Executor上有多少个CPU core,就可以并行执行多少个task,而第一批并行执行的每个task都会创建一个shuffleFileGroup,并将数据写入对应的磁盘文件内.
> 
> 当Executor的CPU core执行完一批task,接着执行下一批task时,下一批task就会复用之前已有的shuffleFileGroup,包括其中的磁盘文件,也就是说此时task会将数据写入已有的磁盘文件中,而不会写入新的磁盘文件中,因此consolidate机制允许不同的task复用同一批磁盘文件,这样就可以有效将多个task的磁盘文件进行一定程度上的合并,从而大幅度减少磁盘文件的数量,进而提升shuffle write的性能.
> 
> 假设第二个stage有100个task,第一个stage有50个task,总共还是有10个Executor(ExecutorCPU个数为1),每个Executor执行5个task,那么原本使用未经优化HashShuffleManager时,每个Executor会产生500个磁盘文件,所有Executor会产生5000个磁盘文件的,但是此时经过优化之后,每个Executor创建的磁盘文件的数量的计算公式为：`CPU core的数量*下一个stage的task数量`,也就是说,每个Executor此时只会创建100个磁盘文件,所有Executor只会创建1000个磁盘文件.
> 
> 优化后HashShuffleManager工作原理图
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_057.jpg)



##### 2.1.6.3 Sort Shuffle 解析
> SortShuffleManager的运行机制主要分成两种,一种是普通运行机制,另一种是bypass运 行机制, 当shuffle read task数量小于等于`spark.shuffle.sort.bypassMergeThreshold`参数值时(默认为200),就会启用bypass机制.
> 
> 1.普通运行机制
> 在该模式下,数据会先写入一个内存数据结构中,此时根据不同的shuffle算子,可能选用不同的数据结构,如果是reduceByKey这种聚合类的shuffle算子,那么会选用Map数据结构,一边通过Map进行聚合,一边写入内存,如果是join这种普通的shuffle算子,那么会选用Array数据结构,直接写入内存,接着每写一条数据进入内存数据结构之后,就会判断一下,是否达到了某个临界阈值,如果达到临界阈值的话,那么就会尝试将内存数据结构中的数据溢写到磁盘,然后清空内存数据结构.
> 
> 在溢写到磁盘文件之前,会先根据key对内存数据结构中已有的数据进行排序,排序过后,会分批将数据写入磁盘文件,默认的batch数量是10000条,也就是说排序好的数据,会以每批1万条数据的形式分批写入磁盘文件,写入磁盘文件是通过Java的BufferedOutputStream实现的,BufferedOutputStream是Java的缓冲输出流,首先会将数据缓冲在内存中,当内存缓冲满溢之后再一次写入磁盘文件中,这样可以减少磁盘IO次数,提升性能.
> 
> 一个task将所有数据写入内存数据结构的过程中,会发生多次磁盘溢写操作,也就会产生多个临时文件,最后会将之前所有的临时磁盘文件都进行合并,这就是merge过程,此时会将之前所有临时磁盘文件中的数据读取出来,然后依次写入最终的磁盘文件之中,此外由于一个task就只对应一个磁盘文件,也就意味着该task为下游stage的task准备的数据都在这一个文件中,因此还会单独写一份索引文件,其中标识了下游各个task的数据在文件中的start offset与end offset.
> 
> SortShuffleManager由于有一个磁盘文件merge的过程,因此大大减少了文件数量,比如第一个stage有50个task,总共有10个Executor,每个Executor执行5个task,而第二个stage有100个task,由于每个task最终只有一个磁盘文件,因此此时每个Executor上只有5个磁盘文件,所有Executor只有50个磁盘文件.
> 
> 普通运行机制 SortShuffleManager工作原理图
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_058.jpg)

> 2.bypass运行机制
> bypass运行机制的触发条件如下 : 
> shuffle map task数量小于`spark.shuffle.sort.bypassMergeThreshold`参数的值.
> 不是聚合类的shuffle算子.
> 
> 此时每个task会为每个下游task都创建一个临时磁盘文件,并将数据按key进行hash然后根据key的hash值,将key写入对应的磁盘文件之中,当然写入磁盘文件时也是先写入内存缓冲,缓冲写满之后再溢写到磁盘文件的,最后同样会将所有临时磁盘文件都合并成一个磁盘文件,并创建一个单独的索引文件.
> 
> 该过程的磁盘写机制其实跟未经优化的HashShuffleManager是一模一样的,因为都要创建数量惊人的磁盘文件,只是在最后会做一个磁盘文件的合并而已,因此少量的最终磁盘文件,也让该机制相对未经优化的HashShuffleManager来说,shuffle read的性能会更好.
> 
> 而该机制与普通SortShuffleManager运行机制的不同在于 : 第一磁盘写机制不同,第二，不会进行排序,也就是说启用该机制的最大好处在于,shuffle write过程中,不需要进行数据的排序操作,也就节省掉了这部分的性能开销.
> 
> 普通运行机制 SortShuffleManager工作原理图
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/spark/start_059.jpg)

#### 2.1.7 Spark 内存管理
> 在执行Spark应用程序时,Spark集群会启动Driver和Executor两种JVM进程,前者为主控进程,负责创建Spark上下文,提交Spark作业(Job),并将作业转化为计算任务(Task),在各个Executor进程间协调任务的调度,后者负责在工作节点上执行具体的计算任务,并将结果返回给Driver,同时为需要持久化的RDD提供存储功能,由于Driver的内存管理相对来说较为简单,本节主要对Executor 的内存管理进行分析,下文中的Spark内存均特指Executor内存.

##### 2.1.7.1 堆内和堆外内存规划
> 作为一个JVM进程,Executor内存管理建立在JVM 的内存管理之上,Spark对JVM的堆内(On-heap)空间进行了更为详细的分配,以充分利用内存,同时Spark引入了堆外(Off-heap)内存,使之可以直接在工作节点的系统内存中开辟空间,进一步优化了内存的使用.
> 
> 1.堆内内存
> 堆内内存的大小,由Spark 应用程序启动时的`–executor-memory`或`spark.executor.memory`参数配置,Executor 内运行的并发任务共享JVM堆内内存,这些任务在缓存RDD数据和广播(Broadcast)数据时占用的内存被规划为存储(Storage)内存,而这些任务在执行Shuffle时占用的内存被规划为执行(Execution)内存,剩余的部分不做特殊规划,那些Spark 内部的对象实例,或者用户定义的Spark应用程序中的对象实例,均占用剩余的空间,不同的管理模式下,这三部分占用的空间大小各不相同.
> 
> 2.堆外内存
> 为了进一步优化内存的使用以及提高Shuffle时排序的效率,Spark 引入了堆外(Off-heap)内存,使之可以直接在工作节点的系统内存中开辟空间,存储经过序列化的二进制数据.
> 
> 堆外内存意味着把内存对象分配在Java虚拟机的堆以外的内存,这些内存直接受操作系统管理(而不是虚拟机),这样做的结果就是能保持一个较小的堆,以减少垃圾收集对应用的影响.

##### 2.1.7.2 内存空间分配
> 1.静态内存管理
> 在Spark最初采用的静态内存管理机制下,存储内存、执行内存和其他内存的大小在Spark 应用程序运行期间均为固定的,但用户可以应用程序启动前进行配置.
> 
> 静态内存管理机制实现起来较为简单,但如果用户不熟悉Spark 的存储机制,或没有根据具体的数据规模和计算任务或做相应的配置,很容易造成”一半海水,一半火焰”的局面,即存储内存和执行内存中的一方剩余大量的空间,而另一方却早早被占满,不得不淘汰或移出旧的内容以存储新的内容,由于新的内存管理机制的出现,这种方式目前已经很少有开发者使用,出于兼容旧版本的应用程序的目的,Spark仍然保留了它的实现.
> 
> 2.统一内存管理
> spark 1.6之后引入的统一内存管理机制,与静态内存管理的区别在于存储内存和执行内存共享同一块空间,可以动态占用对方的空闲区域,统一内存管理的堆内内存.
> 
> 其中最重要的优化在于动态占用机制,其规则如下 : 
> 1.设定基本的存储内存和执行内存区域`spark.storage.storageFraction 参数`,该设定确定了双方各自拥有的空间的范围.
> 2.双方的空间都不足时,则存储到硬盘,若己方空间不足而对方空余时,可借用对方的空间,(存储空间不足是指不足以放下一个完整的Block)
> 3.执行内存的空间被对方占用后,可让对方将占用的部分转存到硬盘,然后”归还”借用的空间.
> 4.存储内存的空间被对方占用后,无法让对方”归还”,因为需要考虑Shuffle过程中的很多因素,实现起来较为复杂.


##### 2.1.7.3 存储内存管理
> 1.RDD 持久化机制
> 弹性分布式数据集(RDD)作为Spark最根本的数据抽象,是只读的分区记录(Partition)的集合,只能基于在稳定物理存储中的数据集上创建,或者在其他已有的RDD上执行转换(Transformation)操作产生一个新的RDD,转换后的RDD与原始的RDD之间产生依赖关系,构成了血统(Lineage),凭借血统,Spark保证了每一个RDD都可以被重新恢复,但RDD的所有转换都是惰性,即只有当一个返回结果给Driver的行动(Action)发生时,Spark才会创建任务读取RDD然后真正触发转换的执行.
> 
> Task在启动之初读取一个分区时,会先判断这个分区是否已经被持久化,如果没有则需要检查Checkpoint或按照血统重新计算,所以如果一个RDD上要执行多次行动,可以在第一次行动中使用persist或cache方法,在内存或磁盘中持久化或缓存这个RDD,从而在后面的行动时提升计算速度.
> 
> RDD的持久化由Spark的Storage 模块负责,实现了RDD 与物理存储的解耦合,Storage模块负责管理Spark在计算过程中产生的数据,将那些在内存或磁盘、在本地或远程存取数据的功能封装了起来,在具体实现时Driver端和Executor端的Storage模块构成了主从式的架构,即Driver端的BlockManager为Master,Executor端的BlockManager为Slave.
> 
> Spark中7种存储级别如下 : 
> | 持久化级别      |     含义 |
> | :--------: | :--------:|
> | MEMORY_ONLY    |   以非序列化的Java对象的方式持久化在JVM内存中,如果内存无法完全存储RDD所有的partition,那么那些没有持久化的partition就会在下一次需要使用它们的时候,重新被计算 |
> | MEMORY_AND_DISK    |   同上,但是当某些partition无法存储在内存中时,会持久化到磁盘中,下次需要使用这些partition时,需要从磁盘上读取 |
> | MEMORY_ONLY_SER    |   同MEMORY_ONLY,但是会使用Java序列化方式,将Java对象序列化后进行持久化,可以减少内存开销,但是需要进行反序列化,因此会加大CPU开销 |
> | MEMORY_AND_DISK_SER    |   同MEMORY_AND_DISK,但是使用序列化方式持久化Java对象 |
> | DISK_ONLY    |   使用非序列化Java对象的方式持久化,完全存储到磁盘上 |
> | MEMORY_ONLY_2 & MEMORY_AND_DISK_2    |   如果是尾部加了2的持久化级别,表示将持久化数据复用一份,保存到其他节点,从而在数据丢失时,不需要再次计算,只需要使用备份数据即可 |
> 
> 通过对数据结构的分析,可以看出存储级别从三个维度定义了RDD的Partition(同时也就是Block)存储方式 : 
> 1.存储位置 : 磁盘／堆内内存／堆外内存,如`MEMORY_AND_DISK`是同时在磁盘和堆内内存上存储,实现了冗余备份,`OFF_HEAP`则是只在堆外内存存储,目前选择堆外内存时不能同时存储到其他位置.
> 2.存储形式 : Block缓存到存储内存后,是否为非序列化的形式,如`MEMORY_ONLY`是非序列化方式存储,`OFF_HEAP`是序列化方式存储.
> 3.副本数量 : 大于1 时需要远程冗余备份到其他节点,如`DISK_ONLY_2`需要远程备份1个副本.

> 2.RDD 缓存过程
> RDD在缓存到存储内存之前,Partition中的数据一般以迭代器(Iterator)的数据结构来访问,这是Scala语言中一种遍历数据集合的方法,通过Iterator可以获取分区中每一条序列化或者非序列化的数据项(Record),这些Record的对象实例在逻辑上占用了JVM 堆内内存的other 部分的空间,同一Partition的不同Record的存储空间并不连续.
> 
> RDD在缓存到存储内存之后,Partition被转换成Block,Record 在堆内或堆外存储内存中占用一块连续的空间,将Partition由不连续的存储空间转换为连续存储空间的过程,Spark称之为"展开"(Unroll)

> 3.淘汰与落盘
> 由于同一个Executor的所有的计算任务共享有限的存储内存空间,当有新的Block需要缓存但是剩余空间不足且无法动态占用时,就要对LinkedHashMap中的旧Block进行淘汰(Eviction),而被淘汰的Block如果其存储级别中同时包含存储到磁盘的要求,则要对其进行落盘(Drop),否则直接删除该Block.
> 
> 存储内存的淘汰规则为 : 
> 被淘汰的旧Block要与新Block的MemoryMode相同,即同属于堆外或堆内内存.
> 新旧Block不能属于同一个RDD,避免循环淘汰.
> 旧Block所属RDD不能处于被读状态,避免引发一致性问题.
> 遍历LinkedHashMap中Block,按照最近最少使用(LRU)的顺序淘汰,直到满足新Block所需的空间,其中LRU是LinkedHashMap特性.
> 落盘的流程则比较简单,如果其存储级别符合`_useDisk`为true的条件,再根据其`_deserialized`判断是否是非序列化的形式,若是则对其进行序列化,最后将数据存储到磁盘,在Storage模块中更新其信息.

##### 2.1.7.4 执行内存管理
> 执行内存主要用来存储任务在执行Shuffle时占用的内存,Shuffle是按照一定规则对RDD 数据重新分区的过程,Shuffle的Write和Read两阶段对执行内存的使用.
> 
> Shuffle Write : 在map端会采用ExternalSorter进行外排,在内存中存储数据时主要占用堆内执行空间.
> Shuffle Read : 在对reduce端的数据进行聚合时,要将数据交给Aggregator处理,在内存中存储数据时占用堆内执行空间.
> 如果需要进行最终结果排序,则要将再次将数据交给ExternalSorter处理,占用堆内执行空间.
> 在ExternalSorter和Aggregator中,Spark会使用一种叫AppendOnlyMap哈希表在堆内执行内存中存储数据,但在Shuffle过程中所有数据并不能都保存到该哈希表中,当这个哈希表占用的内存会进行周期性地采样估算,当其大到一定程度,无法再从MemoryManager申请到新的执行内存时,Spark就会将其全部内容存储到磁盘文件中,这个过程被称为溢存(Spill),溢存到磁盘的文件最后会被归并(Merge).
> 
> Spark 的存储内存和执行内存有着截然不同的管理方式 : 对于存储内存来说Spark用一个LinkedHashMap来集中管理所有的Block,Block由需要缓存的RDD的Partition转化而成,而对于执行内存Spark用AppendOnlyMap来存储Shuffle过程中的数据,在Tungsten 排序中甚至抽象成为页式内存管理,开辟了全新的JVM 内存管理机制.

#### 2.1.8 Spark 核心组件解析
##### 2.1.8.1 BlockManager 数据存储与管理机制
> BlockManager是整个Spark底层负责数据存储与管理的一个组件,Driver和Executor的所有数据都由对应的BlockManager进行管理.
> 
> Driver上有BlockManagerMaster,负责对各个节点上的BlockManager内部管理的数据的元数据进行维护,比如block的增删改等操作,都会在这里维护好元数据的变更.
> 
> 每个节点都有一个BlockManager,每个BlockManager创建之后,第一件事即使去向BlockManagerMaster进行注册,此时BlockManagerMaster会为其长难句对应的BlockManagerInfo.
> 
> BlockManagerMaster与BlockManager的关系非常像NameNode与DataNode的关系,BlockManagerMaster中保存中BlockManager内部管理数据的元数据,进行维护，当BlockManager进行Block增删改等操作时，都会在BlockManagerMaster中进行元数据的变更，这与NameNode维护DataNode的元数据信息，DataNode中数据发生变化时NameNode中的元数据信息也会相应变化是一致.


##### 2.1.8.2 Spark 共享变量底层实现
> Spark一个非常重要的特性就是共享变量.
> 默认情况下,如果在一个算子的函数中使用到了某个外部的变量,那么这个变量的值会被拷贝到每个task中,此时每个task只能操作自己的那份变量副本,如果多个task想要共享某个变量,那么这种方式是做不到的.
> 
> Spark为此提供了两种共享变量,一种是Broadcast Variable(广播变量),另一种是Accumulator(累加变量),Broadcast Variable会将用到的变量,仅仅为每个节点拷贝一份,即每个Executor拷贝一份,更大的用途是优化性能,减少网络传输以及内存损耗,Accumulator则可以让多个task共同操作一份变量,主要可以进行累加操作,Broadcast Variable是共享读变量,task不能去修改它,而Accumulator可以让多个task操作一个变量.

###### 2.1.8.2.1 广播变量
> 广播变量允许编程者在每个Executor上保留外部数据的只读变量,而不是给每个任务发送一个副本.
> 
> 每个task都会保存一份它所使用的外部变量的副本,当一个Executor上的多个task都使用一个大型外部变量时,对于Executor内存的消耗是非常大的,因此可以将大型外部变量封装为广播变量此时一个Executor保存一个变量副本此Executor上的所有task共用此变量不再是一个task单独保存一个副本这在一定程度上降低了Spark任务的内存占用.


###### 2.1.8.2.2 累加器
> 累加器(accumulator) ：Accumulator是仅仅被相关操作累加的变量,因此可以在并行中被有效地支持,它们可用于实现计数器(如MapReduce)或总和计数.


#### 2.1.9 Spark 内核解析总结
> Spark内核原理对于更好使用Spark完成开发任务有着非常重要的作用,同时Spark内核知识也是面试过程中经常被问到的知识点.
> 
> Spark的部署模式、通信架构、任务调度机制、Shuffle过程、内存管理机制以及Spark的核心组件进行了详细分析,这些内容都是Spark最为重要的架构原理,希望在之后的学习中可以不断深化对于Spark内核架构的理解,在更高的层次上去使用Spark技术框架.

### 2.2 Spark 性能调优
#### 2.2.1 Spark 性能调优
#### 2.2.2 Spark 数据倾斜
#### 2.2.3 Spark Troubleshooting

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