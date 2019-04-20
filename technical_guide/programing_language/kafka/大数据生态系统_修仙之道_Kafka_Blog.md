# 大数据生态系统 修仙之道 Kafka Blog

@(2019-04-01)[ Docs Language:简体中文 & English|Programing Language:Kafka|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)|![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg) | ![GitHub repo size in bytes](https://img.shields.io/github/repo-size/geekparkhub/geekparkhub.github.io.svg) | GeekDeveloper:[JEEP-711](https://github.com/jeep711)|Github:[github.com/geekparkhub](https://github.com/geekparkhub)|Gitee:[gitee.com/geekparkhub](https://gitee.com/geekparkhub) ]

##  🐘 Kafka Technology 修仙之道 炼虚合道 🐘

![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/kafka/kafka.jpg)

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



## 1. Kafka 概述
### 1.1 消息队列

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/kafka/start_002.jpg)
> `点对点模式` (一对一,消费者主动拉取数据,消息收到后消息清除)点对点模型通常是一个基于拉取或者轮询的消息传送模型,这种模型从队列中请求信息,而不是将消息推送到客户端.这个模型的特点是发送到队列的消息被一个且只有一个接收者接收处理,即使有多个消息监听者也是如此.
> 
> `发布/订阅模式` (一对多,数据生产后,推送给所有订阅者)
> 发布订阅模型则是一个基于推送的消息传送模型,发布订阅模型可以有多种不同的订阅者,临时订阅者只在主动监听主题时才接收消息,而持久订阅者则监听主题的所有消息,即使当前订阅者不可用,处于离线状态.
### 1.2 为什么需要消息队列
> `解耦` : 允许你独立的扩展或修改两边的处理过程,只要确保它们遵守同样的接口约束.
> 
> `冗余` : 消息队列把数据进行持久化直到它们已经被完全处理,通过这一方式规避了数据丢失风险,许多消息队列所采用的"插入-获取-删除"范式中,在把一个消息从队列中删除之前,需要你的处理系统明确的指出该消息已经被处理完毕,从而确保你的数据被安全的保存直到你使用完毕.
> 
> `扩展性` : 因为消息队列解耦了你的处理过程,所以增大消息入队和处理的频率是很容易的,只要另外增加处理过程即可.
> 
> `灵活性&峰值处理能力` : 在访问量剧增的情况下,应用仍然需要继续发挥作用,但是这样的突发流量并不常见,如果为以能处理这类峰值访问为标准来投入资源随时待命无疑是巨大的浪费,使用消息队列能够使关键组件顶住突发的访问压力,而不会因为突发的超负荷的请求而完全崩溃.
> 
> `可恢复性` : 系统的一部分组件失效时,不会影响到整个系统,消息队列降低了进程间的耦合度,所以即使一个处理消息的进程挂掉,加入队列中的消息仍然可以在系统恢复后被处理.
> 
> `顺序保证` : 在大多使用场景下,数据处理的顺序都很重要,大部分消息队列本来就是排序的,并且能保证数据会按照特定的顺序来处理,(Kafka保证一个Partition内的消息的有序性).
> 
> `缓冲` : 有助于控制和优化数据流经过系统的速度,解决生产消息和消费消息的处理速度不一致的情况.
> 
> `异步通信` : 很多时候用户不想也不需要立即处理消息,消息队列提供了异步处理机制,允许用户把一个消息放入队列,但并不立即处理它,想向队列中放入多少消息就放多少,然后在需要的时候再去处理它们.

### 1.3 Kafka 简介
> 在流式计算中,Kafka一般用来缓存数据,Storm通过消费Kafka数据进行计算.
> 
> Apache Kafka是一个开源消息系统,是由Scala编程语言编写,Apache软件基金会开发一个开源消息系统项目.
> 
> Kafka最初是由LinkedIn公司开发,并于2011年初开源,2012年10月从Apache Incubator毕业,该项目的目标是为处理实时数据提供一个统一 / 高通量 / 低等待平台.
> 
> Kafka是一个分布式消息队列,Kafka对消息保存时根据Topic进行归类,发送消息者称为Producer,消息接受者称为Consumer,此外Kafka集群有多个Kafka实例组成,每个实例(Server)成为Broker.
> 
> 无论是Kafka集群,还是Producer和consumer都依赖于Zookeeper集群保存一些Meta信息来保证系统可用性.

### 1.4 Kafka 架构

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/kafka/start_003.jpg)

> `Producer` : 消息生产者,向Kafka Broker发消息的客户端.
> 
> `Consumer` : 消息消费者,向Kafka Broker拉取消息的客户端.
> 
> `Topic` : 可以理解为一个队列.
> 
> `Consumer Group`(CG) : 这是Kafka用来实现Topic消息广播(发给所有Consumer)单播(发给任意一个Consumer)手段,一个Topic可以有多个CG,Topic消息会复制(仅仅只是概念上的复制)所有CG,但每个Partion只会把消息发给该CG中一个Consumer.
> 如果需要实现广播,只要每个Consumer有一个独立CG就可以了,要实现单播只要所有Consumer在同一个CG,用CG还可以将Consumer进行自由分组而不需要多次发送消息到不同的Topic.
> 
> `Broker` : 一台Kafka服务器就是一个Broker,一个集群由多个Broker组成,一个Broker可以容纳多个Topic.
> 
> `Partition` : 为了实现扩展性,一个非常大的Topic可以分布到多个Broker(即是服务器),一个Topic可以分为多个Partition,每个Partition是一个有序队列,Partition中每条消息都会被分配一个有序Id(Offset),Kafka只保证按一个Partition中顺序将消息发给Consumer,不保证一个Topic整体(多个Partition间)顺序.
> 
> `Offset` : Kafka存储文件都是按照offset.kafka来命名,用Offset作为名称的好处是方便查找,例如想找位于2049位置,只要找到2048.kafka文件即可,当然`the first offset`就是00000000000.kafka.

## 2. Kafka 集群部署
### 2.1 环境准备
#### 2.1.1 集群规划
| Server Node | Zookooper Server | Kafka Server |
| :--------: | :--------:| :------: |
| systemhub511 🖥️ | zookeeper ✅ | kafka ✅  |
| systemhub611 🖥️ | zookeeper ✅ | kafka ✅  |
| systemhub711 🖥️ | zookeeper ✅ | kafka ✅  |

#### 2.1.2 Download
- `Download Zookeeper` : [archive.apache.org/dist/zookeeper](https://archive.apache.org/dist/zookeeper/)
- `Download Kafka` : [kafka.apache.org/downloads](http://kafka.apache.org/downloads.html)

#### 2.1.3 安装 Zookeeper
##### 2.1.3.1 解压 zookeeper
```
[root@systemhub511 ~]#  cd /opt/software/
[root@systemhub511 software]# ll
total 512064
-rwxrwxrwx. 1 root root  35042811 Jan 17 19:18 zookeeper-3.4.10.tar.gz
[root@systemhub511 software]# tar -zxvf zookeeper-3.4.10.tar.gz -C /opt/module/
zookeeper-3.4.10/
zookeeper-3.4.10/LICENSE.txt
zookeeper-3.4.10/lib/
zookeeper-3.4.10/lib/log4j-1.2.16.LICENSE.txt
[root@systemhub511 software]#
```
##### 2.1.3.2 重命名 zookeeper
```
[root@systemhub511 module]# mv zookeeper-3.4.10 zookeeper
[root@systemhub511 module]# ll
total 20
drwxr-xr-x.  9 root  root  4096 Feb 24 21:55 apache-tomcat
drwxr-xr-x. 10 root  root  4096 Apr 11 17:02 flume
drwxr-xr-x. 12 10011 10011 4096 Mar  3 00:42 hadoop
drwxr-xr-x.  8 uucp    143 4096 Dec 20  2017 jdk1.8.0_162
drwxr-xr-x. 10  1001  1001 4096 Mar 23  2017 zookeeper
```
##### 2.1.3.3 创建 zkData目录
```
[root@systemhub511 zookeeper]# mkdir zkData
```
##### 2.1.3.4 重命名配置文件
```
[root@systemhub511 conf]# mv zoo_sample.cfg zoo.cfg
[root@systemhub511 conf]# ll
total 12
-rw-rw-r--. 1 1001 1001  535 Mar 23  2017 configuration.xsl
-rw-rw-r--. 1 1001 1001 2161 Mar 23  2017 log4j.properties
-rw-rw-r--. 1 1001 1001  922 Mar 23  2017 zoo.cfg
[root@systemhub511 conf]# 
```
##### 2.1.3.5 配置 zoo.cfg文件
> 配置数据缓存路径
```
[root@systemhub511 zkData]# pwd
/opt/module/zookeeper/zkData
[root@systemhub511 zookeeper]# cd conf/
[root@systemhub511 conf]# vim zoo.cfg
```
> 修改配置信息
> 
> 配置参数解读 : `Server.A = B:C:D`
> A表示 标识服务器节点ID.
> B表示 标识服务器节点名称.
> C表示 标识服务器与集群中Leader服务器交换信息端口.
> D表示 如集群中Leader服务器宕机时,需要一个端口来重新进行选举,并选出新的Leader,而这个端口就是用来执行选举时服务器相互通信端口.
``` dsconfig
# The number of milliseconds of each tick
tickTime=2000
# The number of ticks that the initial 
# synchronization phase can take
initLimit=10
# The number of ticks that can pass between 
# sending a request and getting an acknowledgement
syncLimit=5
# the directory where the snapshot is stored.
# do not use /tmp for storage, /tmp here is just 
# example sakes.
dataDir=/opt/module/zookeeper/zkData
# the port at which the clients will connect
clientPort=2181

################### Cluster ######################
server.1=systemhub511:2888:3888
server.2=systemhub611:2888:3888
server.3=systemhub711:2888:3888
```

##### 2.1.3.6 Zookeeper 集群
> 集群模式下需配置myid文件,此文件是在dataDir目录下,此文件数据中就是A值,Zookeeper启动时读取此文件,得到的数据与zoo.cfg中配置信息比较从而判断哪个Server.
> 
> 创建myid
```
[root@systemhub511 zookeeper]# cd zkData/
[root@systemhub511 zkData]# touch myid
[root@systemhub511 zkData]# vim myid
```
> 根据zoo.cfg服务节点配置对应id,在当前systemhub511服务器,id如1
```
1
```
> 集群分发
```
[root@systemhub511 module]# scp -r zookeeper/ root@systemhub611:/opt/module/zookeeper/
README.txt 100% 1585     1.6KB/s   00:00 
zookeeper-3.4.10-recipes-election.jar 100%   13KB  13.4KB/s   00:00    
[root@systemhub511 module]# 
[root@systemhub511 module]# scp -r zookeeper/ root@systemhub711:/opt/module/zookeeper/
README.txt 100% 1585     1.6KB/s   00:00 
zookeeper-3.4.10-recipes-election.jar 100%   13KB  13.4KB/s   00:00    
[root@systemhub511 module]#  
```
> 分别配置myid文件
```
[root@systemhub611 module]# cd zookeeper/zkData/
[root@systemhub611 zkData]# vim myid
```
```
2
```
```
[root@systemhub711 module]# cd zookeeper/zkData/
[root@systemhub711 zkData]# vim myid
```
```
3
```
> 启动 Zookeeper Server 集群
> 
> 应事先关闭集群防火墙
> 
>  Start systemhub511 Server Node
```
[root@systemhub511 zookeeper]# bin/zkServer.sh start
ZooKeeper JMX enabled by default
Using config: /opt/module/zookeeper/bin/../conf/zoo.cfg
Starting zookeeper ... already running as process 31221.
[root@systemhub511 zookeeper]#
```
>  Start systemhub611 Server Node
```
[root@systemhub611 zookeeper]# bin/zkServer.sh start
ZooKeeper JMX enabled by default
Using config: /opt/module/zookeeper/bin/../conf/zoo.cfg
Starting zookeeper ... already running as process 29605.
[root@systemhub611 zookeeper]# 
```
>  Start systemhub711 Server Node
```
[root@systemhub711 zookeeper]# bin/zkServer.sh start
ZooKeeper JMX enabled by default
Using config: /opt/module/zookeeper/bin/../conf/zoo.cfg
Starting zookeeper ... already running as process 29650.
[root@systemhub711 zookeeper]#
```
> 查看 Zookeeper Server 集群状态
> 
> systemhub511 Server Node Info
```
[root@systemhub511 zookeeper]# bin/zkServer.sh status
ZooKeeper JMX enabled by default
Using config: /opt/module/zookeeper/bin/../conf/zoo.cfg
Mode: follower
[root@systemhub511 zookeeper]#
```
> systemhub611 Server Node Info
```
[root@systemhub611 zookeeper]# bin/zkServer.sh status
ZooKeeper JMX enabled by default
Using config: /opt/module/zookeeper/bin/../conf/zoo.cfg
Mode: leader
[root@systemhub611 zookeeper]# 
```
> systemhub711 Server Node Info
```
[root@systemhub711 zookeeper]# bin/zkServer.sh status
ZooKeeper JMX enabled by default
Using config: /opt/module/zookeeper/bin/../conf/zoo.cfg
Mode: follower
[root@systemhub711 zookeeper]#
```


### 2.2 Kafka 集群部署
#### 2.2.1 解压 kafka
```
[root@systemhub511 software]# tar -zxvf kafka_2.11-0.11.0.0.tgz -C /opt/module/
kafka_2.11-0.11.0.0/
kafka_2.11-0.11.0.0/LICENSE
kafka_2.11-0.11.0.0/NOTICE
kafka_2.11-0.11.0.0/bin/
[root@systemhub511 software]#
```
#### 2.2.2 重命名文件名称
```
[root@systemhub511 module]# mv kafka_2.11-0.11.0.0 kafka
[root@systemhub511 module]# ll
drwxr-xr-x.  6 root  root  4096 Jun 23  2017 kafka
[root@systemhub511 module]# 
```
#### 2.2.3 创建logs目录
```
[root@systemhub511 module]# cd kafka/
[root@systemhub511 kafka]# mkdir logs
```
#### 2.2.4 修改配置文件
```
[root@systemhub511 kafka]# cd config/
[root@systemhub511 config]# vim server.properties
```
> 
```
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

# see kafka.server.KafkaConfig for additional details and defaults

############################# Server Basics #############################

# The id of the broker. This must be set to a unique integer for each broker.
broker.id=0

# Switch to enable topic deletion or not, default value is false
delete.topic.enable=true

############################# Socket Server Settings #############################

# The address the socket server listens on. It will get the value returned from 
# java.net.InetAddress.getCanonicalHostName() if not configured.
#   FORMAT:
#     listeners = listener_name://host_name:port
#   EXAMPLE:
#     listeners = PLAINTEXT://your.host.name:9092
#listeners=PLAINTEXT://:9092

# Hostname and port the broker will advertise to producers and consumers. If not set, 
# it uses the value for "listeners" if configured.  Otherwise, it will use the value
# returned from java.net.InetAddress.getCanonicalHostName().
#advertised.listeners=PLAINTEXT://your.host.name:9092

# Maps listener names to security protocols, the default is for them to be the same. See the config documentation for more details
#listener.security.protocol.map=PLAINTEXT:PLAINTEXT,SSL:SSL,SASL_PLAINTEXT:SASL_PLAINTEXT,SASL_SSL:SASL_SSL

# The number of threads that the server uses for receiving requests from the network and sending responses to the network
num.network.threads=3

# The number of threads that the server uses for processing requests, which may include disk I/O
num.io.threads=8

# The send buffer (SO_SNDBUF) used by the socket server
socket.send.buffer.bytes=102400

# The receive buffer (SO_RCVBUF) used by the socket server
socket.receive.buffer.bytes=102400

# The maximum size of a request that the socket server will accept (protection against OOM)
socket.request.max.bytes=104857600


############################# Log Basics #############################

# A comma seperated list of directories under which to store log files
log.dirs=/opt/module/kafka/logss

# The default number of log partitions per topic. More partitions allow greater
# parallelism for consumption, but this will also result in more files across
# the brokers.
num.partitions=1

# The number of threads per data directory to be used for log recovery at startup and flushing at shutdown.
# This value is recommended to be increased for installations with data dirs located in RAID array.
num.recovery.threads.per.data.dir=1

############################# Internal Topic Settings  #############################
# The replication factor for the group metadata internal topics "__consumer_offsets" and "__transaction_state"
# For anything other than development testing, a value greater than 1 is recommended for to ensure availability such as 3.
offsets.topic.replication.factor=1
transaction.state.log.replication.factor=1
transaction.state.log.min.isr=1

############################# Log Flush Policy #############################

# Messages are immediately written to the filesystem but by default we only fsync() to sync
# the OS cache lazily. The following configurations control the flush of data to disk.
# There are a few important trade-offs here:
#    1. Durability: Unflushed data may be lost if you are not using replication.
#    2. Latency: Very large flush intervals may lead to latency spikes when the flush does occur as there will be a lot of data to flush.
#    3. Throughput: The flush is generally the most expensive operation, and a small flush interval may lead to exceessive seeks.
# The settings below allow one to configure the flush policy to flush data after a period of time or
# every N messages (or both). This can be done globally and overridden on a per-topic basis.

# The number of messages to accept before forcing a flush of data to disk
#log.flush.interval.messages=10000

# The maximum amount of time a message can sit in a log before we force a flush
#log.flush.interval.ms=1000

############################# Log Retention Policy #############################

# The following configurations control the disposal of log segments. The policy can
# be set to delete segments after a period of time, or after a given size has accumulated.
# A segment will be deleted whenever *either* of these criteria are met. Deletion always happens
# from the end of the log.

# The minimum age of a log file to be eligible for deletion due to age
log.retention.hours=168

# A size-based retention policy for logs. Segments are pruned from the log as long as the remaining
# segments don't drop below log.retention.bytes. Functions independently of log.retention.hours.
#log.retention.bytes=1073741824

# The maximum size of a log segment file. When this size is reached a new log segment will be created.
log.segment.bytes=1073741824

# The interval at which log segments are checked to see if they can be deleted according
# to the retention policies
log.retention.check.interval.ms=300000

############################# Zookeeper #############################

# Zookeeper connection string (see zookeeper docs for details).
# This is a comma separated host:port pairs, each corresponding to a zk
# server. e.g. "127.0.0.1:3000,127.0.0.1:3001,127.0.0.1:3002".
# You can also append an optional chroot string to the urls to specify the
# root directory for all kafka znodes.
zookeeper.connect=systemhub511:2181,systemhub611:2181,systemhub711:2181

# Timeout in ms for connecting to zookeeper
zookeeper.connection.timeout.ms=6000


############################# Group Coordinator Settings #############################

# The following configuration specifies the time, in milliseconds, that the GroupCoordinator will delay the initial consumer rebalance.
# The rebalance will be further delayed by the value of group.initial.rebalance.delay.ms as new members join the group, up to a maximum of max.poll.interval.ms.
# The default value for this is 3 seconds.
# We override this to 0 here as it makes for a better out-of-the-box experience for development and testing.
# However, in production environments the default value of 3 seconds is more suitable as this will help to avoid unnecessary, and potentially expensive, rebalances during application startup.
group.initial.rebalance.delay.ms=0
```
#### 2.2.5 配置环境变量
```
[root@systemhub511 kafka]# pwd
/opt/module/kafka
[root@systemhub511 kafka]# vim /etc/profile
```
> 配置信息
```
## SET KAFKA_HOME
export KAFKA_HOME=/opt/module/kafka
export PATH=$PATH:$KAFKA_HOME/bin	
```
> 更新配置文件
```
[root@systemhub511 kafka]# source /etc/profile
[root@systemhub511 kafka]# echo $KAFKA_HOME
/opt/module/kafka
```

#### 2.2.6 分发 kafka集群
```
[root@systemhub511 module]# scp -r kafka/ root@systemhub611:/opt/module/kafka/
connect-file-source.properties 100%  881     0.9KB/s   00:00    
.server.properties.swp 100%   16KB  16.0KB/s   00:00    
connect-file-sink.properties 100%  883     0.9KB/s   00:00
[root@systemhub511 module]#
```
```
[root@systemhub511 module]# scp -r kafka/ root@systemhub711:/opt/module/kafka/
connect-file-source.properties 100%  881     0.9KB/s   00:00    
.server.properties.swp 100%   16KB  16.0KB/s   00:00 
[root@systemhub511 module]#
```
> 分别修改配置文件,broker.id不得重复
```
[root@systemhub611 ~]# cd /opt/module/kafka/config/
[root@systemhub611 config]# vim server.properties
```
```
# The id of the broker. This must be set to a unique integer for each broker.
broker.id=1
```
```
[root@systemhub711 ~]# cd /opt/module/kafka/config/
[root@systemhub711 config]# vim server.properties
```
```
# The id of the broker. This must be set to a unique integer for each broker.
broker.id=2
```

#### 2.2.7 启动 kafka集群
> 因KafkaServer依赖于ZookeeperServer,所以要事先开启ZookeeperServer.
```
[root@systemhub511 kafka]#  bin/kafka-server-start.sh config/server.properties
[1] 23152
```

```
[root@systemhub611 kafka]#  bin/kafka-server-start.sh config/server.properties
[1] 22647
```

```
[root@systemhub711 kafka]# bin/kafka-server-start.sh config/server.properties &
[1] 22736
```
#### 2.2.8 关闭 kafka集群
```
[root@systemhub511 kafka]# bin/kafka-server-stop.sh stop
```
```
[root@systemhub611 kafka]# bin/kafka-server-stop.sh stop
```
```
[root@systemhub711 kafka]# bin/kafka-server-stop.sh stop
```


### 2.3 Kafka 指令
#### 2.3.1 创建Topic
> 参数说明 : 
> `--topic` 定义topic名称
> `--replication-factor` 定义副本数量
> `--partitions`   定义分区数量
```
[root@systemhub511 kafka]# bin/kafka-topics.sh --create --zookeeper systemhub511:2181 -partitions 2 --replication-factor 2 --topic topic001
Created topic "topic001".
[root@systemhub511 kafka]# 
```
#### 2.3.2 查看当前服务中所有Topic
```
[root@systemhub511 kafka]# bin/kafka-topics.sh --list --zookeeper systemhub511:2181
topic001
[root@systemhub511 kafka]# 
```

#### 2.3.3 生产者
```
[root@systemhub511 kafka]# bin/kafka-console-producer.sh --broker-list systemhub511:9092 --topic topic001
>hello kafka
```
#### 2.3.4 消费者
> 过时版本语法
```
[root@systemhub711 kafka]# bin/kafka-console-consumer.sh --zookeeper systemhub511:2181 --topic topic001
Using the ConsoleConsumer with old consumer is deprecated and will be removed in a future major release. Consider using the new consumer by passing [bootstrap-server] instead of [zookeeper].
hello kafka
```
> 新版本语法
``` dsconfig
[root@systemhub711 kafka]# bin/kafka-console-consumer.sh --bootstrap-server systemhub511:9092 --topic topic001 --from-beginning

hello kafka
```
#### 2.3.5 查看Topic详情
```
[root@systemhub511 kafka]# bin/kafka-topics.sh --describe --zookeeper systemhub511 --topic topic001
Topic:topic001  PartitionCount:2        ReplicationFactor:2     Configs:
        Topic: topic001 Partition: 0    Leader: 1       Replicas: 1,0   Isr: 0,1
        Topic: topic001 Partition: 1    Leader: 2       Replicas: 2,1   Isr: 1,2
[root@systemhub511 kafka]# 
```
#### 2.3.6 删除Topic
> 需要在server.properties配置文件中设置`delete.topic.enable=true`
> 否则只是标记删除或者直接重启
```
[root@systemhub511 kafka]# bin/kafka-topics.sh --delete --zookeeper systemhub511:2181 --topic topic001
Topic topic001 is marked for deletion.
Note: This will have no impact if delete.topic.enable is not set to true.
[root@systemhub511 kafka]# 
```

### 2.4 Kafka 配置信息
#### 2.4.1 Broker 配置信息

| 属性        |     默认值 |   描述   |
| :--------: | :--------:| :------: |
| broker.id     |   0/1/2/3/... |  必填参数,broker唯一标识.  |
| log.dirs     |   /tmp/kafka-logs |  Kafka数据存放的目录,可以指定多个目录,中间用逗号分隔,当新partition被创建时会被存放到当前存放partition最少的目录.  |
| port     |   9092 |  BrokerServer接受客户端连接端口号  |
| zookeeper.connect     |   null |  Zookeeper连接串格式为:`hostname1:port1,hostname2:port2,hostname3:port3`,注意,此配置允许指定一个zookeeper路径来存放此kafka集群所有数据,为了与其他应用集群区分开,建议在此配置中指定本集群存放目录格式为:`hostname1:port1,hostname2:port2,hostname3:port3/chroot/path`,要注意的是,消费者参数要和此参数一致.  |
| message.max.bytes     |   1000000 |  服务器可以接收到最大消息的大小,注意此参数要和consumer的`maximum.message.size`值大小一致,否则会因为生产者生产消息太大导致消费者无法消费.  |
| num.io.threads     |   8 |  服务器用来执行读写请求IO线程数,此参数数量至少要等于服务器上磁盘数量.  |
| queued.max.requests     |   500 |  I/O线程可以处理请求队列大小,若实际请求数超过此大小,网络线程将停止接收新请求.  |
| socket.send.buffer.bytes     |   100 * 1024 |  The SO_SNDBUFF buffer    the server prefers for socket connections  |
| socket.receive.buffer.bytes.     |   field2 |  field3  |
| field1     |   100 * 1024 |  The SO_RCVBUFF buffer the server prefers for socket connections.  |
| socket.request.max.bytes     |   100 * 1024 * 1024 |  服务器允许请求最大值,用来防止内存溢出,其值应该小于Java heap size.  |
| num.partitions     |   1 |  默认partition数量,如果topic在创建时没有指定partition数量,默认使用此值,建议改为5.  |
| log.segment.bytes     |   1024 * 1024 * 1024 |  Segment文件大小,超过此值将会自动新建一个segment,此值可以被topic级别参数覆盖.  |
| log.roll.{ms,hours}     |   24 * 7 hours |  新建segment文件时间,此值可以被topic级别参数覆盖.  |
| log.retention.{ms,minutes,hours}     |   7 days |  Kafka segment log保存周期,保存周期超过此时间日志就会被删除,此参数可以被topic级别参数覆盖,数据量大时建议减小此值.  |
| log.retention.bytes     |   -1 |  每个partition最大容量,若数据量超过此值,partition数据将会被删除,注意这个参数控制每个partition而不是topic,此参数可以被log级别参数覆盖.  |
| log.retention.check.interval.ms     |   5 minutes |  删除策略的检查周期  |
| auto.create.topics.enable     |   true |  自动创建topic参数,建议此值设置为false,严格控制topic管理,防止生产者错写topic.  |
| default.replication.factor     |   1 |  默认副本数量,建议改为2  |
| replica.lag.time.max.ms     |   10000 |  在此窗口时间内没有收到follower fetch请求,leader会将其从ISR(in-syncreplicas)中移除.  |
| replica.lag.max.messages     |   4000 |  如果replica节点落后leader节点此值大小消息数量,leader节点就会将其从ISR中移除.  |
| replica.socket.timeout.ms     |   30 * 1000 |  replica向leader发送请求的超时时间.  |
| replica.socket.receive.buffer.bytes     |   64 * 1024 |  The socket  receive buffer for network requests tothe leader for replicating data.  |
| replica.fetch.max.bytes     |   1024 * 1024 |  The number of byes   of messages to attempt to fetch for each partition in the fetch requests  the replicas send to the leader.  |
| replica.fetch.wait.max.ms     |   500 |  The maximum amount of time  towait time for data to arrive on the leader in the fetch requests sent by the replicas to the leader.  |
| num.replica.fetchers     |   1 |  Number of threads used to replicate messages from leaders. Increasing this value can increase the degree of  I/O parallelism in thefollower broker  |
| fetch.purgatory.purge.interval.requests     |   1000 |  The purge    interval (in number of requests) of the fetch request purgatory.  |
| zookeeper.session.timeout.ms     |   6000 |  ZooKeeper session超时时间,如果在此时间内server没有向zookeeper发送心跳,zookeeper就会认为此节点已挂掉,此值太低导致节点容易被标记死亡,若太高会导致太迟发现节点死亡. |
| zookeeper.connection.timeout.ms     |   6000 |  客户端连接zookeeper超时时间.  |
| controlled.shutdown.enable     |   true |  允许broker shutdown,如果启用broker在关闭之前会把它上面所有leaders转移到其它brokers上,建议启用增加集群稳定性.  |
| auto.leader.rebalance.enable     |   true |  If this is enabled the   controller will automatically try to balance leadership for partitions   among the brokers by periodically returning leadership to the “preferred”  replica for each partition if it is available.  |
| leader.imbalance.per.broker.percentage     |   10 |  The percentage   of leader imbalance allowed per broker. The controller will rebalance  leadership if this ratio goes above the configured value per broker  |
| delete.topic.enable     |   false |  启用deletetopic参数,建议设置为true.  |


#### 2.4.2 Producer 配置信息

| 属性        |     默认值 |   描述   |
| :--------: | :--------:| :------: |
| metadata.broker.list     |   |  启动时producer查询brokers列表,可以是集群中所有brokers一个子集,注意这个参数只是用来获取topic元信息,producer会从元信息中挑选合适的broker并与之建立socket连接,格式为:`host1:port1,host2:port2`  |
| request.timeout.ms     |   10000 |  Broker等待ack超时时间,若等待时间超过此值,会返回客户端错误信息.  |
| producer.type     |   sync |  同步异步模式,async表示异步,sync表示同步,如果设置成异步模式,可以允许生产者以batch形式push数据,这样会极大提高broker性能,推荐设置为异步.  |
| serializer.class     |   kafka.serializer.DefaultEncoder |  序列号类,默认序列化类型为byte[]  |
| key.serializer.class     |   |  Key序列化类,默认同上  |
| partitioner.class     |   kafka.producer.DefaultPartitioner |  Partition类,默认对key进行hash.  |
| compression.codec     |   none |  指定producer消息压缩格式,可选参数为：none / gzip / snappy  |
| compressed.topics     |   null |  启用压缩topic名称,若上面参数选择了一个压缩格式,那么压缩仅对本参数指定的topic有效,若本参数为空则对所有topic有效.  |
| message.send.max.retries     |   3 |  Producer发送失败时重试次数,若网络出现问题可能会导致不断重试.  |
| queue.buffering.max.ms     |   5000 |  启用异步模式时,producer缓存消息时间,比如设置成1000时,它会缓存1秒数据再一次发送出去,这样可以极大增加broker吞吐量,但也会造成时效性降低.  |
| queue.buffering.max.messages     |   10000 |  采用异步模式时producer  buffer队列里最大缓存消息数量,如果超过这个数值,producer就会阻塞或者丢掉消息.  |
| queue.enqueue.timeout.ms     |   -1 |  当达到上面参数值时producer阻塞等待时间,如果值设置为0,buffer队列满时producer不会阻塞,消息直接被丢掉,若值设置为-1,producer会被阻塞不会丢消息.  |
| batch.num.messages     |   200 |  用异步模式时,一个batch缓存消息数量,达到这个数量值时producer才会发送消息.  |
| send.buffer.bytes     |   100 * 1024 |  Socket write buffer size  |


#### 2.4.3 Consumer 配置信息
| 属性        |     默认值 |   描述   |
| :--------: | :--------:| :------: |
| group.id     |   |  Consumer组ID,相同goup.id的consumer属于同一个组.  |
| zookeeper.connect     |   |  Consumer的zookeeper连接串,要和broker的配置一致. |
| consumer.id     |   null |  如果不设置会自动生成.  |
| socket.timeout.ms     |   30 * 1000 |  网络请求socket超时时间,实际超时时间由`max.fetch.wait` + `socket.timeout.ms` 确定. |
| fetch.message.max.bytes     |   1024 * 1024 |  查询topic-partition时允许的最大消息大小,consumer会为每个partition缓存此大小消息到内存,因此这个参数可以控制consumer内存使用量,这个值应该至少比server允许最大消息大小大,以免producer发送消息大于consumer允许消息.  |
| auto.commit.enable     |   true |  如果此值设置为true,consumer会周期性把当前消费offset值保存到zookeeper,当consumer失败重启之后将会使用此值作为新开始消费的值.  |
| auto.commit.interval.ms     |   60 * 1000 |  Consumer提交offset值到zookeeper周期.  |
| queued.max.message.chunks     |   2 |  用来被consumer消费message chunks 数量,每个chunk可以缓存`fetch.message.max.bytes`大小数据量.  |
| auto.commit.interval.ms     |   60 * 1000 |  Consumer提交offset值到zookeeper周期.  |
| queued.max.message.chunks     |   2 |  用来被consumer消费message chunks 数量,每个chunk可以缓存`fetch.message.max.bytes`大小数据量.  |
| consumer.timeout.ms     |   -1 |  若在指定时间内没有消息消费,consumer将会抛出异常.  |


## 3. Kafka 工作流分析
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/kafka/start_003.jpg)

### 3.1 Kafka 生产过程
#### 3.1.1 写入方式
> producer采用推(push)模式将消息发布到broker,每条消息都被追加(append)到分区(patition)中,属于顺序写磁盘(顺序写磁盘效率比随机写内存要高,保障kafka吞吐率).

#### 3.1.2 分区 (Partition)
> 消息发送时都被发送到一个topic,其本质就是一个目录,而topic是由一些Partition Logs(分区日志)组成,其组织结构如下图所示

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/kafka/start_004.jpg)
> 每个Partition中的消息都是有序,生产消息被不断追加到Partition log上,其中每一个消息都被赋予了一个唯一的offset值.
> 
> `分区原因`
> 1.方便在集群中扩展,每个Partition可以通过调整以适应它所在机器,而一个topic又可以有多个Partition组成,因此整个集群就可以适应任意大小数据了.
> 
> 2.因为以Partition为单位读写,所以可以提高并发.
> 
> `分区规则`
> 指定patition,则直接使用.
> 未指定patition但指定key,通过对key的value进行hash出一个patition.
> patition和key都未指定,使用轮询选出一个patition.
> 
> DefaultPartitioner类
``` java
    public int partition(String topic, Object key, byte[] keyBytes,
        Object value, byte[] valueBytes, Cluster cluster) {
        List<PartitionInfo> partitions = cluster.partitionsForTopic(topic);
        intnumPartitions = partitions.size();

        if (keyBytes == null) {
            intnextValue = nextValue(topic);

            List<PartitionInfo> availablePartitions = cluster.availablePartitionsForTopic(topic);

            if (availablePartitions.size() > 0) {
                intpart = Utils.toPositive(nextValue) % availablePartitions.size();

                return availablePartitions.get(part).partition();
            } else {
                // no partitions are available, give a non-available partition
                return Utils.toPositive(nextValue) % numPartitions;
            }
        } else {
            // hash the keyBytes to choose a partition
            return Utils.toPositive(Utils.murmur2(keyBytes)) % numPartitions;
        }
    }
```

#### 3.1.3 副本 (Replication)
> 同一个partition可能会有多个replication(对应server.properties配置中的`default.replication.factor=N`)
> 
> 没有replication情况下,一旦broker宕机,其上所有patition数据都不可被消费.
> 
> 同时producer也不能再将数据存于其上的patition,引入replication之后,同一个partition可能会有多个replication,而这时需要在这些replication之间选出一个leader,producer和consumer只与这个leader交互,其它replication作为follower从leader中复制数据.


#### 3.1.4 写入流程
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/kafka/start_005.jpg)
> 1.producer先从zookeeper `/brokers/.../state`节点找到该partition的leader.
> 
> 2.producer将消息发送给该leader.
> 
> 3.leader将消息写入本地log.
> 
> 4.followers从leader pull消息,写入本地log后向leader发送ACK.
> 
> 5.leader收到所有ISR中的replication的ACK后,增加HW(high watermark,最后commit 的offset)向producer发送ACK


### 3.2 Broker 存储过程
#### 3.2.1 存储方式
> 物理上把topic分成一个或多个patition(对应server.properties中`num.partitions=3`配置),每个patition物理上对应一个文件夹(该文件夹存储该patition的所有消息和索引文件).
```
[root@systemhub511 kafka]# cd logs
[root@systemhub511 logs]# ll
total 312
-rw-r--r--. 1 root root   293 Apr 17 21:07 controller.log
-rw-r--r--. 1 root root     0 Apr 17 14:15 kafka-authorizer.log
-rw-r--r--. 1 root root     0 Apr 17 14:15 kafka-request.log
-rw-r--r--. 1 root root 21691 Apr 18 00:01 kafkaServer-gc.log.0.current
-rw-r--r--. 1 root root   318 Apr 17 22:37 log-cleaner.log
-rw-r--r--. 1 root root   195 Apr 18 00:01 server.log
-rw-r--r--. 1 root root 32012 Apr 17 22:37 state-change.log
[root@systemhub511 logs]# 
```
#### 3.2.2 存储策略
> 无论消息是否被消费,kafka都会保留所有消息,有两种策略可以删除旧数据:
> 1.基于时间 : log.retention.hours=168
> 2.基于大小 : log.retention.bytes=1073741824
> 需要注意的是,因为Kafka读取特定消息的时间复杂度为O(1),即与文件大小无关,所以这里删除过期文件与提高Kafka性能无关.

#### 3.2.3 Zookeeper 存储结构
> 注意：producer不在zk中注册,而消费者在zk中注册.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/kafka/start_006.jpg)


### 3.3 Kafka 消费过程
> Kafka提供两套consumer API : 高级Consumer API 和 低级API
#### 3.3.1 高级 API
> `高级API 优点`
- 高级API编写起来非常简单. 
- 不需要自行管理offset,系统通过zookeeper自行管理.
- 不需要管理分区,副本等情况,系统自动管理.
- 消费者断线会自动根据上一次记录在zookeeper中的offset获取数据(默认设置1分钟更新一下zookeeper中存的offset).
- 可以使用group来区分对同一个topic不同程序访问分离开来(不同的group记录不同的offset,这样不同程序读取同一个topic才不会因为offset互相影响).

> `高级API 缺点`
- 对于某些特殊需求来说,不能自行控制offset.
- 不能细化控制如分区、副本、zk等.

#### 3.3.2 低级 API
> `低级API 优点`
- 能让开发者自控offset.
- 自行控制连接分区,对分区自定义进行负载均衡.
- 对zookeeper依赖性降低 (如 : offset不一定要靠zk存储,自行存储offset即可,比如存在文件或者内存中).

> `低级API 缺点`
- 操作太过复杂,需要自行控制offset,连接分区,找到分区leader等.


#### 3.3.3 消费者组
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/kafka/start_007.jpg)
> 消费者是以consumer group消费者组的方式工作,由一个或者多个消费者组成一个组，共同消费一个topic.
> 
> 每个分区在同一时间只能由group中的一个消费者读取,但是多个group可以同时消费这个partition.
> 
> 如图所示,一个由三个消费者组成的group,有一个消费者读取主题中两个分区,另外两个分别读取一个分区,某个消费者读取某个分区,也可以叫做某个消费者是某个分区的拥有者.
> 
> 在这种情况下,消费者可以通过水平扩展方式同时读取大量消息,另外,如果一个消费者失败了,那么其他group成员会自动负载均衡读取之前失败消费者读取分区.


#### 3.3.4 消费方式
> consumer采用pull(拉)模式从broker中读取数据.
> 
> push(推)模式很难适应消费速率不同消费者,因为消息发送速率是由broker决定.
> 它目标是尽可能以最快速度传递消息,但是这样很容易造成consumer来不及处理消息,典型表现就是拒绝服务以及网络拥塞,而pull模式则可以根据consumer消费能力以适当速率消费消息.
> 
> 对于Kafka而言,pull模式更合适,它可简化broker的设计,consumer可自主控制消费消息速率,同时consumer可以自己控制消费方式——即可批量消费也可逐条消费,同时还能选择不同提交方式从而实现不同传输语义.
> 
> pull模式不足之处是,如果kafka没有数据,消费者可能会陷入循环中,一直等待数据到达.
> 
> 为了避免这种情况,在拉请求中有参数,允许消费者请求在等待数据到达“长轮询”中进行阻塞(并且可选地等待到给定的字节数,以确保大的传输大小)

#### 3.3.5 消费者组案例
> 测试同一个消费者组中的消费者,同一时刻只能有一个消费者消费.
> 
> 在systemhub511、systemhub611服务器中修改`/opt/module/kafka/config/consumer.properties`配置文件中的`group.id`属性为任意组名.
```
[root@systemhub511 module]# cd kafka/
[root@systemhub511 kafka]# vim config/consumer.properties
```
```
#consumer group id
group.id=systemhub511
```
```
[root@systemhub611 module]# cd kafka/
[root@systemhub611 kafka]# vim config/consumer.properties
```
```
#consumer group id
group.id=systemhub611
```
> 分别启动消费者
```
[root@systemhub511 kafka]# bin/kafka-console-consumer.sh --zookeeper systemhub511:2181 --topic topic001 --consumer.config config/consumer.properties
Using the ConsoleConsumer with old consumer is deprecated and will be removed in a future major release. Consider using the new consumer by passing [bootstrap-server] instead of [zookeeper].
```
```
[root@systemhub611 kafka]# bin/kafka-console-consumer.sh --zookeeper systemhub511:2181 --topic topic001 --consumer.config config/consumer.properties
Using the ConsoleConsumer with old consumer is deprecated and will be removed in a future major release. Consider using the new consumer by passing [bootstrap-server] instead of [zookeeper].
[067] WARN [systemhub611_systemhub611-1555744110617-1d4d406d], no brokers found when trying to rebalance. (kafka.consumer.ZookeeperConsumerConnector)
```
> 在systemhub711服务器 启动生产者
```
[root@systemhub711 kafka]# bin/kafka-console-producer.sh --broker-list systemhub511:9092 --topic topic001
>hello kafka!
```
> 查看systemhub511和systemhub611 接收者
> 同一时刻只有一个消费者接收到消息.
```
[root@systemhub611 kafka]# bin/kafka-console-consumer.sh --zookeeper systemhub511:2181 --topic topic001 --consumer.config config/consumer.properties
Using the ConsoleConsumer with old consumer is deprecated and will be removed in a future major release. Consider using the new consumer by passing [bootstrap-server] instead of [zookeeper].
hello kafka!
```


## 4. Kafka API

## 5. Kafka Producer拦截器

## 6. Kafka Streams


## 7. 修仙之道 技术架构迭代 登峰造极之势
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