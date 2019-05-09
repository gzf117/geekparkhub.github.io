# 大数据生态系统 修仙之道 Hadoop HA Blog

@(2019-04-17)[ Docs Language:简体中文 & English|Programing Language:Hadoop HA|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)|![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg) | ![GitHub repo size in bytes](https://img.shields.io/github/repo-size/geekparkhub/geekparkhub.github.io.svg) | GeekDeveloper:[JEEP-711](https://github.com/jeep711)|Github:[github.com/geekparkhub](https://github.com/geekparkhub)|Gitee:[gitee.com/geekparkhub](https://gitee.com/geekparkhub) ]

##  🐘 Hadoop HA Technology 修仙之道 刻苦修持 🐘

![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hbase/hbase.jpg)

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



## 1. HDFS-HA 高可用
### 1.1 HA 概述
- 1.所谓HA(High Available),即高可用(7*24小时不中断服务).
- 2.实现高可用最关键的策略是`消除单点故障`,HA严格来说应该分成各个组件的HA机制：HDFS的HA和YARN的HA.
- 3.Hadoop2.0版本之前,在HDFS集群中NameNode存在单点故障(SPOF).
- 4.NameNode主要在以下两个方面影响HDFS集群
- NameNode机器发生意外,如宕机,集群将无法使用,直到管理员重启
- NameNode机器需要升级,包括软件,硬件升级,此时集群也将无法使用
- HDFS HA功能通过配置Active/Standby两个nameNodes实现在集群中对NameNode热备来解决上述问题,如果出现故障,如机器崩溃或机器需要升级维护,这时可通过此种方式将NameNode很快切换到另外一台机器.

### 1.2 HDFS-HA 工作机制
- 通过双NameNode消除单点故障

#### 1.2.1 HDFS-HA 工作要点
> 1.元数据管理方式需要改变 : 内存中各自保存一份元数据,Edits日志只有Active状态NameNode节点可以做写操作,两个NameNode都可以读取edits,共享edits放在一个共享存储中管理(Quorum Journal Manager和NFS两个主流实现)
> 
> 2.需要一个状态管理功能模块实现了一个zkfailover,常驻在每一个NameNode所在节点，每一个zkfailover负责监控自己所在namenode节点,利用zk进行状态标识,当需要进行状态切换时,由zkfailover来负责切换,切换时需要防止brain split现象的发生.
> 
> 3.必须保证两个NameNode之间能够ssh无密码登录.
> 
> 4.隔离(Fence),即同一时刻仅仅有一个NameNode对外提供服务.

#### 1.2.2 HDFS-HA 自动故障转移工作机制
> 自动故障转移为HDFS部署增加了两个新组件 : ZooKeeper和ZKFailoverController(ZKFC)进程.
> 
> ZooKeeper是维护少量协调数据,通知客户端这些数据改变和监视客户端故障的高可用服务,HA自动故障转移依赖于ZooKeeper的以下功能:
> 
> 1.故障检测 : 集群中每个NameNode在ZooKeeper中维护了一个持久会话,如果机器崩溃,ZooKeeper中的会话将终止,ZooKeeper通知另一个NameNode需要触发故障转移.
> 
> 2.现役NameNode选择 : ZooKeeper提供了一个简单的机制用于唯一选择一个节点为active状态,如果目前现役NameNode崩溃,另一个节点可能从ZooKeeper获得特殊排外锁以表明它应该成为现役NameNode,ZKFC是自动故障转移中另一个新组件,是ZooKeeper客户端,也监视和管理NameNode的状态,每个运行NameNode主机也运行了一个ZKFC进程,ZKFC负责:
> 
> 1.健康监测 : ZKFC使用一个健康检查命令定期地ping与之在相同主机的NameNode,只要该NameNode及时地回复健康状态,ZKFC认为该节点是健康,如果该节点崩溃,冻结或进入不健康状态,健康监测器标识该节点为非健康.
> 
> 2.ZooKeeper会话管理 : 当本地NameNode是健康,ZKFC保持一个在ZooKeeper中打开的会话,如果本地NameNode处于active状态,ZKFC也保持一个特殊znode锁,该锁使用了ZooKeeper对短暂节点支持,如果会话终止,锁节点将自动删除.
> 
> 3.基于ZooKeeper选择:如果本地NameNode是健康,且ZKFC发现没有其它节点当前持有znode锁,它将为自己获取该锁,如果成功则它已经赢得了选择,并负责运行故障转移进程以使它的本地NameNode为active,故障转移进程与前面描述手动故障转移相似,首先如果必要保护之前现役NameNode,然后本地NameNode转换为active状态.

## 2. HDFS-HA 集群配置
### 2.1 环境准备
- 1.修改IP 
- 2.修改主机名及主机名和IP地址映射
- 3.关闭防火墙
- 4.ssh免密登录
- 5.安装JDK,配置环境变量等

### 2.2 配置HDFS-HA集群
- 1.[HDFS-HA官方配置文档](https://hadoop.apache.org/docs/r2.7.7/hadoop-project-dist/hadoop-hdfs/HDFSHighAvailabilityWithQJM.html)
- 2.在/opt/module/目录下创建HA文件夹,并将hadoop拷贝到此目录下.
```
[root@systemhub511 module]# mkdir HA
[root@systemhub511 module]# cp -r ./hadoop/ HA/
```
- 3.配置hdfs-site.xml | vim `hdfs-site.xml`
``` xml
<configuration>

<!-- 配置对外暴露服务名称 -->
<property>
  <name>dfs.nameservices</name>
  <value>mycluster</value>
</property>

<!-- 配置NameNode别名 -->
<property>
  <name>dfs.ha.namenodes.mycluster</name>
  <value>nn1,nn2</value>
</property>

<!-- 配置RPC/HTTP通讯地址 -->
<property>
  <name>dfs.namenode.rpc-address.mycluster.nn1</name>
  <value>systemhub511:8020</value>
</property>
<property>
  <name>dfs.namenode.rpc-address.mycluster.nn2</name>
  <value>systemhub611:8020</value>
</property>
<property>
  <name>dfs.namenode.http-address.mycluster.nn1</name>
  <value>systemhub511:50070</value>
</property>
<property>
  <name>dfs.namenode.http-address.mycluster.nn2</name>
  <value>systemhub611:50070</value>
</property>

<!-- 配置共享数据地址 -->
<property>
  <name>dfs.namenode.shared.edits.dir</name>
  <value>qjournal://systemhub511:8485;systemhub611:8485;systemhub711:8485/mycluster</value>
</property>

<!-- 配置失效备援配置代理 -->
<property>
  <name>dfs.client.failover.proxy.provider.mycluster</name>
 <value>org.apache.hadoop.hdfs.server.namenode.ha.ConfiguredFailoverProxyProvider</value>
</property>

<!-- 配置隔离机制 -->
<property>
  <name>dfs.ha.fencing.methods</name>
  <value>sshfence</value>
</property>
<property>
  <name>dfs.ha.fencing.ssh.private-key-files</name>
  <value>/home/root/.ssh/id_rsa</value>
</property>

<!-- 关闭权限检查-->
<property>
  <name>dfs.permissions.enable</name>
  <value>false</value>
</property>

</configuration>
```
- 4.配置core-site.xml | vim `core-site.xml`
``` xml
<configuration>

<!-- 对外暴露服务名称 -->
<property>
  <name>fs.defaultFS</name>
  <value>hdfs://mycluster</value>
</property>

<!-- 指定Hadoop运行时产生文件的存储目录 -->
<property>
  <name>hadoop.tmp.dir</name>
  <value>/opt/module/HA/hadoop/data/tmp</value>
</property>

<!-- 指定journalnode运行时产生文件的存储目录 -->
<property>
  <name>dfs.journalnode.edits.dir</name>
  <value>/opt/module/HA/hadoop/data/tmp/jn</value>
</property>

</configuration>
```
- 5.删除数据日志目录
```
[root@systemhub511 hadoop]# rm -rf data/ logs/
```
- 6.将hadoopHA分发到其他集群节点
```
[root@systemhub511 hadoop]# scp -r ./HA/ root@systemhub611:/opt/module/HA/
[root@systemhub511 hadoop]# scp -r ./HA/ root@systemhub711:/opt/module/HA/
```


### 2.3 启动HDFS-HA集群
#### 2.3.1 HDFS-HA 手动故障转移
- 1.分别启动JournalNode节点
```
[root@systemhub511 hadoop]# sbin/hadoop-daemon.sh start journalnode
starting journalnode, logging to /opt/module/HA/hadoop/logs/hadoop-root-journalnode-systemhub511.out
[root@systemhub511 hadoop]# 
```
```
[root@systemhub611 hadoop]# sbin/hadoop-daemon.sh start journalnode
starting journalnode, logging to /opt/module/HA/hadoop/logs/hadoop-root-journalnode-systemhub611.out
[root@systemhub611 hadoop]# 
```
```
[root@systemhub711 hadoop]# sbin/hadoop-daemon.sh start journalnode
starting journalnode, logging to /opt/module/HA/hadoop/logs/hadoop-root-journalnode-systemhub711.out
[root@systemhub711 hadoop]#
```
- 2.查看进程状态
``` powershell
[root@systemhub511 hadoop]# jps.sh
================        root@systemhub511 All Processes         ===========
1976 sun.tools.jps.Jps
32765 org.apache.hadoop.hdfs.qjournal.server.JournalNode
================        root@systemhub611 All Processes         ===========
1442 org.apache.hadoop.hdfs.qjournal.server.JournalNode
3087 sun.tools.jps.Jps
================        root@systemhub711 All Processes         ===========
2666 sun.tools.jps.Jps
1115 org.apache.hadoop.hdfs.qjournal.server.JournalNode
[root@systemhub511 hadoop]# 
```
- 3.对[nn1]进行格式化,并启动服务
``` powershell
[root@systemhub511 hadoop]# bin/hadoop namenode -format
[root@systemhub511 hadoop]# sbin/hadoop-daemon.sh start namenode
starting namenode, logging to /opt/module/HA/hadoop/logs/hadoop-root-namenode-systemhub511.out
```
- 4.在[nn2]上,同步nn1元数据信息
```
[root@systemhub611 hadoop]# sbin/hadoop-daemon.sh start journalnode
starting journalnode, logging to /opt/module/HA/hadoop/logs/hadoop-root-journalnode-systemhub611.out
```
- 5.启动[nn2]服务
```
[root@systemhub611 hadoop]# sbin/hadoop-daemon.sh start namenode
starting namenode, logging to /opt/module/HA/hadoop/logs/hadoop-root-namenode-systemhub611.out
```
- 6.查看web页面显示
- 分别访问`systemhub511:50070`,`systemhub611:50070`
- 首页显示为备用状态
```
Overview 'systemhub511:8020' (standby)
```
```
Overview 'systemhub611:8020' (standby)
```

- 7.在[nn1]启动所有DataNode服务
```
[root@systemhub511 hadoop]# sbin/hadoop-daemons.sh start datanode
systemhub711: starting datanode, logging to /opt/module/HA/hadoop/logs/hadoop-root-datanode-systemhub711.out
systemhub511: starting datanode, logging to /opt/module/HA/hadoop/logs/hadoop-root-datanode-systemhub511.out
systemhub611: starting datanode, logging to /opt/module/HA/hadoop/logs/hadoop-root-datanode-systemhub611.out
[root@systemhub511 hadoop]# 
```
- 8.查看所有进程状态
```
[root@systemhub511 hadoop]# jps.sh 
================        root@systemhub511 All Processes         ===========
12113 org.apache.hadoop.hdfs.server.namenode.NameNode
23994 org.apache.hadoop.hdfs.server.datanode.DataNode
32765 org.apache.hadoop.hdfs.qjournal.server.JournalNode
25614 sun.tools.jps.Jps
================        root@systemhub611 All Processes         ===========
1442 org.apache.hadoop.hdfs.qjournal.server.JournalNode
26515 sun.tools.jps.Jps
24888 org.apache.hadoop.hdfs.server.datanode.DataNode
14942 org.apache.hadoop.hdfs.server.namenode.NameNode
================        root@systemhub711 All Processes         ===========
25834 sun.tools.jps.Jps
1115 org.apache.hadoop.hdfs.qjournal.server.JournalNode
24191 org.apache.hadoop.hdfs.server.datanode.DataNode
[root@systemhub511 hadoop]# 
```
- 9.将[nn1]切换为Active状态
```
[root@systemhub511 hadoop]# bin/hdfs haadmin -transitionToActive nn1
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/opt/module/HA/hadoop/share/hadoop/common/lib/slf4j-log4j12-1.7.10.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/opt/module/hbase/lib/slf4j-log4j12-1.7.5.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
[root@systemhub511 hadoop]#
```

- 10.`haadmin指令手册`
```
Usage: haadmin
    [-transitionToActive <serviceId>]
    [-transitionToStandby <serviceId>]
    [-failover [--forcefence] [--forceactive] <serviceId> <serviceId>]
    [-getServiceState <serviceId>]
    [-checkHealth <serviceId>]
    [-help <command>]
```
- 11.查看是否Active
```
[root@systemhub511 hadoop]# bin/hdfs haadmin -getServiceState nn1
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/opt/module/HA/hadoop/share/hadoop/common/lib/slf4j-log4j12-1.7.10.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/opt/module/hbase/lib/slf4j-log4j12-1.7.5.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
active
[root@systemhub511 hadoop]#
```
- 12.再次查看首页显示状态
```
Overview 'systemhub511:8020' (active)
```
```
Overview 'systemhub611:8020' (standby)
```


#### 2.3.2 HDFS-HA 自动故障转移
##### 2.3.2.1 HDFS-HA 自动故障转移工作机制
> 自动故障转移为HDFS部署增加了两个新组件 : ZooKeeper和ZKFailoverController(ZKFC)进程.
> 
> ZooKeeper是维护少量协调数据,通知客户端这些数据改变和监视客户端故障的高可用服务,HA自动故障转移依赖于ZooKeeper的以下功能:
> 
> 1.故障检测 : 集群中每个NameNode在ZooKeeper中维护了一个持久会话,如果机器崩溃,ZooKeeper中的会话将终止,ZooKeeper通知另一个NameNode需要触发故障转移.
> 
> 2.现役NameNode选择 : ZooKeeper提供了一个简单的机制用于唯一选择一个节点为active状态,如果目前现役NameNode崩溃,另一个节点可能从ZooKeeper获得特殊排外锁以表明它应该成为现役NameNode,ZKFC是自动故障转移中另一个新组件,是ZooKeeper客户端,也监视和管理NameNode的状态,每个运行NameNode主机也运行了一个ZKFC进程,ZKFC负责:
> 
> 1.健康监测 : ZKFC使用一个健康检查命令定期地ping与之在相同主机的NameNode,只要该NameNode及时地回复健康状态,ZKFC认为该节点是健康,如果该节点崩溃,冻结或进入不健康状态,健康监测器标识该节点为非健康.
> 
> 2.ZooKeeper会话管理 : 当本地NameNode是健康,ZKFC保持一个在ZooKeeper中打开的会话,如果本地NameNode处于active状态,ZKFC也保持一个特殊znode锁,该锁使用了ZooKeeper对短暂节点支持,如果会话终止,锁节点将自动删除.
> 
> 3.基于ZooKeeper选择:如果本地NameNode是健康,且ZKFC发现没有其它节点当前持有znode锁,它将为自己获取该锁,如果成功则它已经赢得了选择,并负责运行故障转移进程以使它的本地NameNode为active,故障转移进程与前面描述手动故障转移相似,首先如果必要保护之前现役NameNode,然后本地NameNode转换为active状态.

##### 2.3.2.2 HDFS-HA 规划集群

| systemhub511 | systemhub611| systemhub711 |
| :--------: | :--------:| :------: |
| NameNode    |   NameNode |   |
| JournalNode    |   JournalNode |  JournalNode |
| DataNode    |   DataNode | DataNode  |
| Zookeeper    |   Zookeeper |  Zookeeper |
|   |   ResourceManager |   |
| NodeManager | NodeManager | NodeManager  |

##### 2.3.2.3 配置 HDFS-HA自动故障转移
###### 2.3.2.3.1 配置
- 1.停止HDFS集群服务
```
[root@systemhub511 hadoop]# sbin/stop-dfs.sh
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
Stopping namenodes on [systemhub511 systemhub611]
systemhub611: stopping namenode
systemhub511: stopping namenode
systemhub711: stopping datanode
systemhub611: stopping datanode
systemhub511: stopping datanode
Stopping journal nodes [systemhub511 systemhub611 systemhub711]
systemhub711: stopping journalnode
systemhub611: stopping journalnode
systemhub511: stopping journalnode
SLF4J: Class path contains multiple SLF4J bindings.
[root@systemhub511 hadoop]#
```
- 2.vim `hdfs-site.xml` 
```
<!-- 启用自动故障转移 -->
<property>
  <name>dfs.ha.automatic-failover.enabled</name>
  <value>true</value>
</property>
```
- 3.vim  `core-site.xml`
```
<!-- 启用zookeeper集群 -->
<property>
  <name>ha.zookeeper.quorum</name>
  <value>systemhub511:2181,systemhub611:2181,systemhub711:2181</value>
</property>
```
- 4.配置文件 分发集群
```
[root@systemhub511 hadoop]# scp -r etc/hadoop/hdfs-site.xml root@systemhub611:/opt/module/HA/hadoop/etc/hadoop/
hdfs-site.xml
100% 2383     2.3KB/s   00:00    
[root@systemhub511 hadoop]# scp -r etc/hadoop/core-site.xml root@systemhub611:/opt/module/HA/hadoop/etc/hadoop/
core-site.xml
100% 1394     1.4KB/s   00:00    
[root@systemhub511 hadoop]# scp -r etc/hadoop/hdfs-site.xml root@systemhub711:/opt/module/HA/hadoop/etc/hadoop/
hdfs-site.xml
100% 2383     2.3KB/s   00:00    
[root@systemhub511 hadoop]# scp -r etc/hadoop/core-site.xml root@systemhub711:/opt/module/HA/hadoop/etc/hadoop/
core-site.xml  
100% 1394     1.4KB/s   00:00    
[root@systemhub511 hadoop]# 
```

###### 2.3.2.3.2 启动
- 1.启动Zookeeper集群
```
[root@systemhub511 hadoop]# cd /opt/module/zookeeper/
[root@systemhub511 zookeeper]# bin/zkServer.sh start
ZooKeeper JMX enabled by default
Using config: /opt/module/zookeeper/bin/../conf/zoo.cfg
Starting zookeeper ... STARTED
[root@systemhub511 zookeeper]# 
```
```
[root@systemhub611 hadoop]# cd /opt/module/zookeeper/
[root@systemhub611 zookeeper]# bin/zkServer.sh start
ZooKeeper JMX enabled by default
Using config: /opt/module/zookeeper/bin/../conf/zoo.cfg
Starting zookeeper ... STARTED
[root@systemhub611 zookeeper]# 
```
```
[root@systemhub611 hadoop]# cd /opt/module/zookeeper/
[root@systemhub611 zookeeper]# bin/zkServer.sh start
ZooKeeper JMX enabled by default
Using config: /opt/module/zookeeper/bin/../conf/zoo.cfg
Starting zookeeper ... STARTED
[root@systemhub611 zookeeper]#
```
- 2.初始化HA Zookeeper状态
```
[root@systemhub511 hadoop]# bin/hdfs zkfc -formatZK
SLF4J: Class path contains multiple SLF4J bindings.
```
- 3.启动Zookeeper客户端查看状态
```
[root@systemhub511 zookeeper]# bin/zkCli.sh
[zk: localhost:2181(CONNECTED) 0] ls /
[zookeeper, hadoop-ha]
[zk: localhost:2181(CONNECTED) 1] ls /hadoop-ha
[mycluster]
[zk: localhost:2181(CONNECTED) 2] 
```
- 4.启动HDFS服务
```
[root@systemhub511 hadoop]# sbin/start-dfs.sh
SLF4J: Class path contains multiple SLF4J bindings.
```
- 5.查看当前服务进程
```
[root@systemhub511 hadoop]# jps.sh
================        root@systemhub511 All Processes         ===========
18576 org.apache.zookeeper.server.quorum.QuorumPeerMain
22289 sun.tools.jps.Jps
19845 org.apache.hadoop.hdfs.server.namenode.NameNode
25081 org.apache.zookeeper.ZooKeeperMain
21034 org.apache.hadoop.hdfs.qjournal.server.JournalNode
21723 org.apache.hadoop.hdfs.tools.DFSZKFailoverController
20159 org.apache.hadoop.hdfs.server.datanode.DataNode
================        root@systemhub611 All Processes         ===========
8548 sun.tools.jps.Jps
7429 org.apache.hadoop.hdfs.server.datanode.DataNode
7270 org.apache.hadoop.hdfs.server.namenode.NameNode
19993 org.apache.zookeeper.server.quorum.QuorumPeerMain
7852 org.apache.hadoop.hdfs.qjournal.server.JournalNode
8221 org.apache.hadoop.hdfs.tools.DFSZKFailoverController
================        root@systemhub711 All Processes         ===========
6609 sun.tools.jps.Jps
5537 org.apache.hadoop.hdfs.server.datanode.DataNode
5958 org.apache.hadoop.hdfs.qjournal.server.JournalNode
18477 org.apache.zookeeper.server.quorum.QuorumPeerMain
[root@systemhub511 hadoop]# 
```
- 6.查看首页显示状态
```
Overview 'systemhub511:8020' (standby)
Overview 'systemhub611:8020' (active)
```

###### 2.3.2.3.3 验证
- 上传数据测试
```
[root@systemhub511 hadoop]# bin/hadoop fs -put LICENSE.txt /
```

- 结束 systemhub611 NameNode进程
```
[root@systemhub611 hadoop]# kill -9 7270
```

```
[root@systemhub511 hadoop]# jps.sh
================        root@systemhub511 All Processes         ===========
18576 org.apache.zookeeper.server.quorum.QuorumPeerMain
19845 org.apache.hadoop.hdfs.server.namenode.NameNode
25081 org.apache.zookeeper.ZooKeeperMain
10345 sun.tools.jps.Jps
21034 org.apache.hadoop.hdfs.qjournal.server.JournalNode
21723 org.apache.hadoop.hdfs.tools.DFSZKFailoverController
20159 org.apache.hadoop.hdfs.server.datanode.DataNode
================        root@systemhub611 All Processes         ===========
19008 sun.tools.jps.Jps
7429 org.apache.hadoop.hdfs.server.datanode.DataNode
7270 org.apache.hadoop.hdfs.server.namenode.NameNode
19993 org.apache.zookeeper.server.quorum.QuorumPeerMain
7852 org.apache.hadoop.hdfs.qjournal.server.JournalNode
8221 org.apache.hadoop.hdfs.tools.DFSZKFailoverController
================        root@systemhub711 All Processes         ===========
5537 org.apache.hadoop.hdfs.server.datanode.DataNode
16979 sun.tools.jps.Jps
5958 org.apache.hadoop.hdfs.qjournal.server.JournalNode
18477 org.apache.zookeeper.server.quorum.QuorumPeerMain
[root@systemhub511 hadoop]# 
```
- 查看首页显示状态
```
Overview 'systemhub511:8020' (standby)
Overview 'systemhub611:8020' (active)
```



## 3. YARN-HA 配置
### 3.1 YARN-HA 工作机制
![enter image description here](http://hadoop.apache.org/docs/r2.7.2/hadoop-yarn/hadoop-yarn-site/images/rm-ha-overview.png)


### 3.2 配置 YARN-HA集群
#### 3.2.1 环境准备
- 1.修改IP 
- 2.修改主机名及主机名和IP地址的映射
- 3.关闭防火墙
- 4.ssh免密登录
- 5.安装JDK,配置环境变量等
- 6.配置Zookeeper集群

#### 3.2.2 规划集群
| systemhub511 | systemhub611| systemhub711 |
| :--------: | :--------:| :------: |
| NameNode    |   NameNode |   |
| JournalNode    |   JournalNode |  JournalNode |
| DataNode    |   DataNode | DataNode  |
| Zookeeper    |   Zookeeper |  Zookeeper |
| ResourceManager |   ResourceManager |   |
| NodeManager | NodeManager | NodeManager  |


#### 3.2.3 配置集群
- vim `yarn-site.xml`
``` xml
<configuration>
  <!-- Reducer获取数据方式 -->
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
  <!-- 启用ResourceManager HA -->        
  <property>
    <name>yarn.resourcemanager.ha.enabled</name>
    <value>true</value>
  </property>
  <!-- 声明两台ResourceManager地址 -->         
  <property>
    <name>yarn.resourcemanager.cluster-id</name>
    <value>cluster-yarn1</value>
  </property>
  <property>
    <name>yarn.resourcemanager.ha.rm-ids</name>
    <value>rm1,rm2</value>
  </property>
  <property>
    <name>yarn.resourcemanager.hostname.rm1</name>
    <value>systemhub511</value>
  </property>
  <property>
    <name>yarn.resourcemanager.hostname.rm2</name>
    <value>systemhub611</value>
  </property>
  <!-- 指定Zookeeper集群地址 -->         
  <property>
    <name>yarn.resourcemanager.zk-address</name>
    <value>systemhub511:2181,systemhub611:2181,systemhub711:2181</value>
  </property>
  <!-- 启用自动恢复 -->         
  <property>
    <name>yarn.resourcemanager.recovery.enabled</name>
    <value>true</value>
  </property>
  <!-- 指定ResourceManager状态信息存储在Zookeeper集群 -->         
  <property>
    <name>yarn.resourcemanager.store.class</name>
    <value>org.apache.hadoop.yarn.server.resourcemanager.recovery.ZKRMStateStore</value>
  </property>
  <!-- 日志聚集功能使用 -->
  <property>
    <name>yarn.log-aggregation-enable</name>
    <value>true</value>
  </property>
  <!-- 日志保留时间设置为7天 根据开发情况,时间可自定义 -->
  <!-- 一天=3600秒 3600*24*7=604800 -->
  <property>
    <name>yarn.log-aggregation.retain-seconds</name>
    <value>604800</value>
  </property>
</configuration>
```
- 将配置文件分发其他集群节点
```
[root@systemhub511 hadoop]# scp -r ./etc/hadoop/yarn-site.xml root@systemhub611:/opt/module/HA/hadoop/etc/hadoop/
yarn-site.xml                                                                                                    100% 2473     2.4KB/s   00:00    
[root@systemhub511 hadoop]# scp -r ./etc/hadoop/yarn-site.xml root@systemhub711:/opt/module/HA/hadoop/etc/hadoop/
yarn-site.xml 
```
- 启动yarn
```
[root@systemhub511 hadoop]# sbin/start-yarn.sh
starting yarn daemons
starting resourcemanager, logging to /opt/module/HA/hadoop/logs/yarn-root-resourcemanager-systemhub511.out
systemhub711: starting nodemanager, logging to /opt/module/HA/hadoop/logs/yarn-root-nodemanager-systemhub711.out
systemhub611: starting nodemanager, logging to /opt/module/HA/hadoop/logs/yarn-root-nodemanager-systemhub611.out
systemhub511: starting nodemanager, logging to /opt/module/HA/hadoop/logs/yarn-root-nodemanager-systemhub511.out
[root@systemhub511 hadoop]# 
```

```
[root@systemhub611 hadoop]# sbin/yarn-daemon.sh start resourcemanager
starting resourcemanager, logging to /opt/module/HA/hadoop/logs/yarn-root-resourcemanager-systemhub611.out
[root@systemhub611 hadoop]# 
```

```
[root@systemhub511 hadoop]# bin/yarn rmadmin -getServiceState rm1
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/opt/module/HA/hadoop/share/hadoop/common/lib/slf4j-log4j12-1.7.10.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/opt/module/hbase/lib/slf4j-log4j12-1.7.5.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
active
[root@systemhub511 hadoop]# 
```
## 4. HDFS Federation架构设计



## 5. 修仙之道 技术架构迭代 登峰造极之势
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