# 大数据生态系统 修仙之道 Zookeeper Blog

@(2019-01-17)[Docs Language:简体中文 & English|Programing Language:Zookeeper|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)|![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg)|GeekDeveloper:[JEEP-711](https://github.com/jeep711)|Github:[github.com/geekparkhub](https://github.com/geekparkhub)|Gitee:[gitee.com/geekparkhub](https://gitee.com/geekparkhub)]


![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/zookeeper/zookeeper.jpg)

- **极客实验室是极客国际公园旗下为未来而构建的极客社区;**
- **我们正在构建一个活跃的小众社区,汇聚众多优秀开发者与设计师;**
- **关注极具创新精神的前沿技术&分享交流&项目合作机会等互联网行业服务;**
- **Open开放 `·` Creation创想 `|` OpenSource开放成就梦想 GeekParkHub共建前所未见!**
- **Future Vision : Establishment of the Geek Foundation;**
- **GeekParkHub GithubHome:**<https://github.com/geekparkhub>
- **GeekParkHub GiteeHome:**<https://gitee.com/geekparkhub>
- **欢迎贡献`各领域开源野生Blog`&`笔记`&`文章`&`片段`&`分享`&`创想`&`OpenSource Project`&`Code`&`Code Review`**
- 🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈 issues: [geekparkhub.github.io/issues](https://github.com/geekparkhub/geekparkhub.github.io/issues) 🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈


-------------------

[TOC]



## 1. zookeeper 简介

> Apache ZooKeeper是Apache软件基金会的一个软件项目,他为大型分布式计算提供开源的分布式配置服务、同步服务和命名注册,ZooKeeper曾经是Hadoop的一个子项目,但现在是一个独立的顶级项目。
> 
> ZooKeeper的架构通过冗余服务实现高可用性,因此,如果第一次无应答,客户端就可以询问另一台ZooKeeper主机,ZooKeeper节点将它们的数据存储于一个分层的命名空间,非常类似于一个文件系统或一个前缀树结构,客户端可以在节点读写,从而以这种方式拥有一个共享的配置服务,更新是全序的.   —— [维基百科](https://zh.wikipedia.org/zh-hans/Apache_ZooKeeper)

## 2. zookeeper 工作机制
> zookeeper从设计模式角度来理解,是一个基于观察者模式设计的分布式服务管理框架,它负责存储和管理数据,然后接受观察者注册,一旦这些数据状态发送变化,zookeeper就将负责通知已经在zookeeper上注册的那些观察者做出相应反应

## 3. zookeeper 特点
> 1.zookeeper一个**`领导者 leader`**,多个**`跟随者 follower`**组成集群
> 2.集群中只要有半数以上节点存活,zookeeper集群就能正常服务
> 3.全局数据一致,每个server保存一份相同的数据备份,Client无论连接哪一个服务,数据都是一致的
> 4.更新请求顺序执行,来自同一个客户端的更新请求按其发送顺序依次执行
> 5.数据更新原子性,一次数据更新要么成功要么失败
> 6.实时性,在一定时间范围内,客户端能读到最新数据

## 4. zookeeper 数据结构
> zookeeper数据模型与Unix文件系统很相似,整体上可以看作是一棵树,每个节点称作一个znode,每个zonde默认能够储存1MB数据,每个znode都可以通过其路径唯一标识

## 5. zookeeper 应用场景
> 提供服务包括:**`统一命名服务`**,**`统一配置管理`**,**`统一集群管理`**,**`服务节点动态上下线`**,**`软负载均衡`**
> 
> 统一命名服务:在分布式环境下,经常需要对应用/服务进行统一命名,便于识别.
> 
> 统一配置管理:分布式环境下,配置文件同步,一般要求一个集群中,所有节点配置信息是一致的,对配置文件修改后,希望能够快速同步到各个节点上,配置管理可交由zookeeper实现,可将配置信息写入zookeeper上znode节点,各个客户端服务器监听此znode,一旦znode中数据被修改,zookeeper将通知各个客户端服务器.
> 
> 统一集群管理:在分布式环境中,实现掌握每个节点的状态,可根据节点实时状态做出一些调整,zookeeper可以实现实时监控节点状态变化,可以将节点信息写入zookeeper上一个znode,监听znode可以获取实时状态变化.
> 
> 软负载均衡:在zookeeper中记录每台服务器的访问数,让王文数量少的服务器去处理最新客户端请求.

## 6. zookeeper 快速安装
> Zookeeper Download Address: [archive.apache.org/dist/zookeeper](https://archive.apache.org/dist/zookeeper/)
### 本地模式安装部署
#### 1.将zookeeper.tar.gz存放到linux系统/opt/自定义目录中
```
[geek-developer@servicehub opt]$ ll
total 408816
-rw-r--r--.  1 root root  35042811 Jan 17 00:00 zookeeper-3.4.10.tar.gz
```
#### 2.解压zookeeper.tar.gz文件并重命名
``` bash
#解压zookeeper.tar.gz
tar -zxvf zookeeper-3.4.10.tar.gz
```
```
#将zookeeper-3.4.10重命名为zookeeper
mv zookeeper-3.4.10 zookeeper
```
#### 3.在zookeeper目录下创建用于存放数据的文件夹
``` 
#cd指令进入到/opt/zookeeper/目录下
[geek-developer@servicehub opt]$ cd /opt/zookeeper/
# 列表查看当前目录下文件
[geek-developer@servicehub zookeeper]$ ll
total 2752
drwxr-xr-x.  2 1001 1001    4096 Mar 23  2017 bin
-rw-rw-r--.  1 1001 1001   84725 Mar 23  2017 build.xml
drwxr-xr-x.  2 1001 1001    4096 Jan 19 18:11 conf
drwxr-xr-x. 10 1001 1001    4096 Mar 23  2017 contrib
drwxr-xr-x.  2 1001 1001    4096 Mar 23  2017 dist-maven
drwxr-xr-x.  6 1001 1001    4096 Mar 23  2017 docs
-rw-rw-r--.  1 1001 1001    1709 Mar 23  2017 ivysettings.xml
-rw-rw-r--.  1 1001 1001    5691 Mar 23  2017 ivy.xml
drwxr-xr-x.  4 1001 1001    4096 Mar 23  2017 lib
-rw-rw-r--.  1 1001 1001   11938 Mar 23  2017 LICENSE.txt
-rw-rw-r--.  1 1001 1001    3132 Mar 23  2017 NOTICE.txt
-rw-rw-r--.  1 1001 1001    1770 Mar 23  2017 README_packaging.txt
-rw-rw-r--.  1 1001 1001    1585 Mar 23  2017 README.txt
drwxr-xr-x.  5 1001 1001    4096 Mar 23  2017 recipes
drwxr-xr-x.  8 1001 1001    4096 Mar 23  2017 src
-rw-rw-r--.  1 1001 1001 1456729 Mar 23  2017 zookeeper-3.4.10.jar
-rw-rw-r--.  1 1001 1001     819 Mar 23  2017 zookeeper-3.4.10.jar.asc
-rw-rw-r--.  1 1001 1001      33 Mar 23  2017 zookeeper-3.4.10.jar.md5
-rw-rw-r--.  1 1001 1001      41 Mar 23  2017 zookeeper-3.4.10.jar.sha1
-rw-r--r--.  1 root root 1183464 Jan 20 02:06 zookeeper.out
[geek-developer@servicehub zookeeper]$ 
```
```
#在此目录创建zkData文件夹,可以根据官方说明创建或自定义文件夹名称
mkdir zkData
```

#### 4.修改zookeeper  zoo_sample.cfg配置文件并将文件重命名
```
#cd指令进入到/opt/zookeeper/conf目录下
[geek-developer@servicehub opt]$ cd /opt/zookeeper/conf
# 列表查看当前目录下文件
[geek-developer@servicehub conf]$ ll
total 12
-rw-rw-r--. 1 1001 1001  535 Mar 23  2017 configuration.xsl
-rw-rw-r--. 1 1001 1001 2161 Mar 23  2017 log4j.properties
-rw-rw-r--. 1 1001 1001 1053 Jan 19 00:00  zoo_sample.cfg
[geek-developer@servicehub conf]$
```
```
#将zoo_sample.cfg文件重命名为zoo.cfg
mv zoo_sample.cfg zoo.cfg
```
#### 5.修改zoo.cfg dataDir路径
```
#切换管理员身份
[geek-developer@corehub ~]$ su - root
#输入密码 注意:密码隐藏不可见,输入正确回车即可
Password: 
#cd指令进入到/opt/zookeeper/conf目录下
[root@corehub ~]# cd /opt/devtool/zookeeper/conf
# 列表查看当前目录下文件
[root@corehub-001 conf]# ll
total 12
-rw-rw-r--. 1 1001 1001  535 Mar 23  2017 configuration.xsl
-rw-rw-r--. 1 1001 1001 2161 Mar 23  2017 log4j.properties
-rw-rw-r--. 1 1001 1001 1055 Jan 18 19:41 zoo.cfg
#vim编辑zoo.cfg文件
[root@corehub conf]# vim zoo.cfg
```
```
#按住i键进入编辑模式 找到名称为dataDir并修改配置
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
############需要修改当前数据存放位置#############
###编辑完毕,按Esc键,返回并输入:wq写入并退出vim模式###
dataDir=/opt/devtool/zookeeper/zkData
# the port at which the clients will connect
clientPort=2181
# the maximum number of client connections.
# increase this if you need to handle more clients
#maxClientCnxns=60
#
# Be sure to read the maintenance section of the 
# administrator guide before turning on autopurge.
#
# http://zookeeper.apache.org/doc/current/zookeeperAdmin.html#sc_maintenance
#
# The number of snapshots to retain in dataDir
#autopurge.snapRetainCount=3
# Purge task interval in hours
# Set to "0" to disable auto purge feature
#autopurge.purgeInterval=1
```
#### 6.启动zookeeper服务端
```
#返回上一层目录
[root@corehub conf]# cd ..
#在bin目录下执行zkServer.sh脚本
[root@corehub zookeeper]# bin/zkServer.sh start
```
#### 7.启动zookeeper客户端
```
#在bin目录下执行zkCli.sh脚本
[root@corehub zookeeper]# bin/zkCli.sh
```
#### 8.关闭zookeeper服务端
```
#在bin目录下执行zkServer.sh脚本
[root@corehub zookeeper]# bin/zkServer.sh stop
```
#### 9.关闭zookeeper客户端
```
quit
```
### zookeeper zoo.cfg 配置参数解读
```
1.tickTime=2000 : 通信心跳数,zookeeper服务端与客户端心跳时间,单位毫秒,zookeeper使用基本时间,服务器之间或客户端之间维持心跳时间的间隔,也就是每个tickTime时间就会发送一个心跳,时间单位为毫秒,它用于心跳机制,并且设置最小的session超时时间为两倍心跳时间(session最小超时时间是2*tickTime)

2.initLimit=10 : LF初始化通信时限集群中的follower跟随者服务器Leader领导者服务器之间初始化连接时能容忍的最多心跳数
(tickTime数量),用它来跟限定集群中的zookeeper服务器连接到leader时限

3.syncLimit=5 : LF同步通信时限集群中leader与follower之间最大响应时间单位,响应超过syncLimit*tickTime
4.dataDir 数据文件目录+数据持久化路径 保存zookeeper数据
5.clientProt 客户端 端口号 监听客户端连接端口
```

## 7. zookeeper 内部原理
### 选举机制(面试重点)
> 半数机制,集群中半数以上机器存活,集群可用,所以zookeeper适合安装奇数台服务器,zookeeper虽然在配置文件中并没有指定,但是zookeeper工作时,是有一个节点为leader,其他则为follower,leader是通过内部选举机制临时产生
### 节点类型
> **`持久(Persistent)`** 客户端和服务端断开连接后,创建节点不删除,持久化目录节点,客户端与zookeeper断开连接后,该节点依旧存在,持久化顺序编号目录和节点,客户端与zookeeper断开连接后,该节点依旧存在,只是zookeeper给节点名称进行顺序编号,说明:创建znode时设置顺序标识,znode名称后会附加一个值,顺序号是一个单调递增的计数器,由父节点维护在分布式系统中,顺便号可以被用于为所以的事情进行全局排序,这样客户端可以通过顺序号推断事件顺序
>
> **`短暂(Ephemeral)`** 客户端和服务端断开连接后,创建节点自动删除

### stat结构体
> **`czxid-`**创建节点的事物zxid,每次修改zookeeper状态都会收到一个zxid形式的时间戳,也就是zookeeper事物的id号,事物id是zookeeper中所有修改总的次序,每个修改都有唯一的zxid,如zxid1小于zxid2,那么zxid1在zxid2之前发生
> 
> **`ctime-znode`** 被创建的毫秒数(从1970年开始)
> 
> **`mzxid-znode`** 最后更新的事物id
> 
> **`pZxid-znode`** 最后修改的毫秒数(从1970年开始)
> 
> **`eversion-znode`** 子节点变化号,znode子节点修改次数
> 
> **`dataversion-znode`** 数据变化号
> 
> **`aclVersion-znode`** 访问控制列表的变化号
> 
> **`ephemeralOwner-`** 如果是临时节点,这个是znode拥有这的session id,如果不是临时节点则是0
> 
> **`dataLength-znode`** 数据长度
> 
> **`numChildren-znode`** 子节点数量

### 监听器原理(面试重点)
#### 监听器原理详解
> 1.首先要有一个**`main()`**客户端线程.
> 2.在main线程中创建zookeeper客户端,这时候就会创建两个线程,一个负责**`网络连接通信(connect)`**,一个负责**`监听(listener)`**.
> 3.通过connect线程将注册的监听事件发送给zookeeper服务端.
> 4.在zookeeper服务端注册监听器列表中进注册的监听事件添加到列表中.
> 5.zookeeper服务端监听到所有数据或路径变化,就会将这个消息发送给listener线程.
> 6.listener线程内部调用了**`process()`**方法
#### 常见的监听
> 1.监听节点数据变化 **`get path[watch]`**
> 2.监听子节点增减变化 **`ls path[watch]`**


### 写数据流程
![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/zookeeper/data.jpg)


## 8. zookeeper 实战(开发重点)
### zookeeper分布式安装部署
#### 1.集群规划:至少配置三台以上linux服务器集群
#### 2.配置zookeeper服务器编号id
```
#cd指令进入到zkData/目录下
[root@corehub zookeeper]# cd zkData/
#touch指令创建myid文件
[root@corehub zkData]# touch myid
#vim模式编辑此文件
[root@corehub zkData]# vim myid
#输入1,表示zookeeper服务器编号id为1,后两台服务器配置步骤如法炮制
1
~   
esc退出编辑模式 输入:wq写入并退出
[root@corehub zkData]# vim myid
#输入2
2
~   
esc退出编辑模式 输入:wq写入并退出
[root@corehub zkData]# vim myid
#输入3
3
~  
esc退出编辑模式 输入:wq写入并退出
```
#### 3.增加节点配置
> 配置参数解读 **`server.A=B:C:D`**
**`A`**映射myid,代表第几号服务器
**`B`**映射服务器hostname
**`C`**服务器与集群中leader服务交换信息端口
**`D`**代表备选服务交换信息端口
```
[root@corehub conf]# vim zoo.cfg

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
dataDir=/opt/devtool/zookeeper/zkData
# the port at which the clients will connect
clientPort=2181
# the maximum number of client connections.
# increase this if you need to handle more clients
#maxClientCnxns=60
################增加节点配置####################
#编辑完毕后,esc退出编辑模式 输入:wq写入并退出
server.1=corehub-001:2888:3888
server.2=corehub-002:2888:3888
server.3=corehub-003:2888:3888
#
# Be sure to read the maintenance section of the 
# administrator guide before turning on autopurge.
#
# http://zookeeper.apache.org/doc/current/zookeeperAdmin.html#sc_maintenance
#
# The number of snapshots to retain in dataDir
#autopurge.snapRetainCount=3
# Purge task interval in hours
# Set to "0" to disable auto purge feature
#autopurge.purgeInterval=1
~    
~ 
```
#### 4.分别启动zookeeper服务端
```
#在bin目录下执行并启动001号服务端
[root@corehub-001 zookeeper]# bin/zkServer.sh start
#查看001号服务端状态
[root@corehub-001 zookeeper]# bin/zkServer.sh status

#在bin目录下执行并启动002号服务端
[root@corehub-002 zookeeper]# bin/zkServer.sh start
#查看002号服务端状态
[root@corehub-002 zookeeper]# bin/zkServer.sh status

#在bin目录下执行并启动003号服务端
[root@corehub-003 zookeeper]# bin/zkServer.sh start
#查看003号服务端状态
[root@corehub-003 zookeeper]# bin/zkServer.sh status
```

## 9. zookeeper客户端命令操作
> **`help`**指令 显示所有操作命令
> **`ls / `**查看当前znode中所包含的内容指令
> **`ls2 / `**查看当前节点详细数据指令
> **`create /znode "commit"`** 创建两个普通节点
> **`get / `** 获得节点信息指令
> **`create -e / `** 创建短暂节点指令


## 10. API 应用
### IntelliJ IDEA环境搭建
#### 创建zookeeper客户端
> 💻 IntelliJ IDEA 全宇宙神器 构建maven project 💻
##### 1.修改pom配置文件
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.geekparkhub</groupId>
    <artifactId>ZookeeperTest</artifactId>
    <version>1.0-SNAPSHOT</version>
    <dependencies>
        <!-- add junit单元测试 -->
        <!-- https://mvnrepository.com/artifact/junit/junit -->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>RELEASE</version>
        </dependency>
        <!-- add log4j日志管理 -->
        <!-- https://mvnrepository.com/artifact/org.apache.logging.log4j/log4j-core -->
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-core</artifactId>
            <version>2.8.2</version>
        </dependency>
        <!-- add zookeeper -->
        <!-- https://mvnrepository.com/artifact/org.apache.zookeeper/zookeeper -->
        <dependency>
            <groupId>org.apache.zookeeper</groupId>
            <artifactId>zookeeper</artifactId>
            <version>3.4.10</version>
        </dependency>
    </dependencies>
</project>
```
##### 2.创建log4j.properties并添加日志参数
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

##### 3.分别启动三台zookeeper linux服务端
###### **`Start corehub-001号 zookeeper服务端 并查看本机IP地址`**
> ![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/zookeeper/start_001.jpg)

Code Snippet | (corehub-001号 服务端)代码片段
```
##### bin/zkServer.sh start指令 启动zookeeper corehub-001号 服务端 #####
[root@corehub-001 zookeeper]# bin/zkServer.sh start
ZooKeeper JMX enabled by default
Using config: /opt/devtool/zookeeper/bin/../conf/zoo.cfg
Starting zookeeper ... already running as process 3548.
##### jps指令 查看zookeeper进程 #####
[root@corehub-001 zookeeper]# jps
3548 QuorumPeerMain
3710 Jps
##### ifconfig指令 查看本机IP地址 #####
[root@corehub-001 zookeeper]# ifconfig
eth0      Link encap:Ethernet  HWaddr 00:0C:29:15:A8:CC  
          inet addr:192.168.177.128  Bcast:192.168.177.255  Mask:255.255.255.0
          inet6 addr: fe80::20c:29ff:fe15:a8cc/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:3966 errors:0 dropped:0 overruns:0 frame:0
          TX packets:779 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:276552 (270.0 KiB)  TX bytes:64739 (63.2 KiB) 
          lo Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:10 errors:0 dropped:0 overruns:0 frame:0
          TX packets:10 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:584 (584.0 b)  TX bytes:584 (584.0 b)
[root@corehub-001 zookeeper]# 
```

######  **`Start corehub-002号 zookeeper服务端 并查看本机IP地址`**
> ![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/zookeeper/start_002.jpg)

Code Snippet | (corehub-002号 服务端)代码片段
```
##### bin/zkServer.sh start指令 启动zookeeper corehub-002号 服务端 #####
[root@corehub-002 zookeeper]# bin/zkServer.sh start
ZooKeeper JMX enabled by default
Using config: /opt/devtool/zookeeper/bin/../conf/zoo.cfg
Starting zookeeper ... already running as process 3194.
##### jps指令 查看zookeeper进程 #####
[root@corehub-002 zookeeper]# jps
3376 Jps
3194 QuorumPeerMain
##### ifconfig指令 查看本机IP地址 #####
[root@corehub-002 zookeeper]# ifconfig
eth1      Link encap:Ethernet  HWaddr 00:0C:29:98:7B:7D  
          inet addr:192.168.177.129  Bcast:192.168.177.255  Mask:255.255.255.0
          inet6 addr: fe80::20c:29ff:fe98:7b7d/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:2103 errors:0 dropped:0 overruns:0 frame:0
          TX packets:654 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:157031 (153.3 KiB)  TX bytes:52690 (51.4 KiB)
          lo Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:10 errors:0 dropped:0 overruns:0 frame:0
          TX packets:10 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:584 (584.0 b)  TX bytes:584 (584.0 b)
[root@corehub-002 zookeeper]# 
```
###### **`Start corehub-003号 zookeeper服务端 并查看本机IP地址`**
>![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/zookeeper/start_003.jpg)

Code Snippet | (corehub-003号 服务端)代码片段
```
##### bin/zkServer.sh start指令 启动zookeeper corehub-003号 服务端 #####
[root@corehub-003 zookeeper]# bin/zkServer.sh start
ZooKeeper JMX enabled by default
Using config: /opt/devtool/zookeeper/bin/../conf/zoo.cfg
Starting zookeeper ... already running as process 3242.
##### jps指令 查看zookeeper进程 #####
[root@corehub-003 zookeeper]# jps
3505 Jps
3242 QuorumPeerMain
##### ifconfig指令 查看本机IP地址 #####
[root@corehub-003 zookeeper]# ifconfig
eth1      Link encap:Ethernet  HWaddr 00:0C:29:12:C5:F0  
          inet addr:192.168.177.130  Bcast:192.168.177.255  Mask:255.255.255.0
          inet6 addr: fe80::20c:29ff:fe12:c5f0/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:2078 errors:0 dropped:0 overruns:0 frame:0
          TX packets:633 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:156371 (152.7 KiB)  TX bytes:51085 (49.8 KiB)
          lo Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:10 errors:0 dropped:0 overruns:0 frame:0
          TX packets:10 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:584 (584.0 b)  TX bytes:584 (584.0 b)
[root@corehub-003 zookeeper]#
```
######  ⚠️⚠️**`为了大家在第四步避免入坑,以当前三台虚拟机为例,需在windows系统中映射对应IP地址与主机名`**⚠️⚠️
![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/zookeeper/start_004.jpg)

```
#### Copy Addr ####
C:\Windows\System32\drivers\etc
#### 使用编辑器打开hosts文件 ####
#### 新增IP地址和主机名 ####
192.168.177.128     corehub-001
192.168.177.129     corehub-002
192.168.177.130     corehub-003
```

##### 4.创建zookeeper客户端并RunTest,回调返回结果集
``` java
package com.geekparkhub.zookeeper;

import org.apache.log4j.Logger;
import org.apache.zookeeper.*;
import org.junit.Test;
import java.io.IOException;

/**
 * GeekParkHub | 极客国际公园
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 *
 * Zookeeper测试类
 */

public class ZookeeperTest {

	 /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(ZookeeperTest.class);

    /**
     * 服务端主机名称:Zookeeper客户端 端口号
     * Server HostName : Zookeeper Client port
     */
    private String connectString="corehub-001:2181,corehub-002:2181,corehub-003:2181";

    /**
     * 设置会话超时间 5000毫秒 = 5秒
     * Set session timeout 5000 milliseconds = 5 seconds
     */
    private int sessionTimeout = 5000;

    /**
     * 全局ZooKeeper客户端
     * Global Zoo Keeper client
     */
    private ZooKeeper zkClient;

    /**
     * 初始化方法
     * Initialization Method
     */
    @Test
    public void init() throws IOException {
      zkClient = new ZooKeeper(connectString, sessionTimeout, new Watcher() {
            public void process(WatchedEvent watchedEvent) {
            }
        });
    }
}
```
###### ✅✅如图所示:证明客户端与zookeeper服务端连接成功,并回调参数打印对应结果集✅✅
![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/zookeeper/start_005.jpg)


### 创建子节点
#### ❌❌ 运行 失败版本 | `Error contacting service. It is probably not running.`❌❌
##### 失败代码片段 | zkServer.sh status 查看状态 进程正常开启,但服务没有运行
corehub-001号 | 进程正常开启,但服务没有运行
```
[root@corehub-001 zookeeper]# bin/zkServer.sh status
ZooKeeper JMX enabled by default
Using config: /opt/devtool/zookeeper/bin/../conf/zoo.cfg
Error contacting service. It is probably not running.
[root@corehub-001 zookeeper]# jps
4293 Jps
3548 QuorumPeerMain
```
corehub-002号 | 进程正常开启,但服务没有运行
```
[root@corehub-002 zookeeper]# bin/zkServer.sh status
ZooKeeper JMX enabled by default
Using config: /opt/devtool/zookeeper/bin/../conf/zoo.cfg
Error contacting service. It is probably not running.
[root@corehub-002 zookeeper]# jps
3809 Jps
3194 QuorumPeerMain
```
corehub-003号 | 进程正常开启,但服务没有运行
```
[root@corehub-003 zookeeper]# bin/zkServer.sh status
ZooKeeper JMX enabled by default
Using config: /opt/devtool/zookeeper/bin/../conf/zoo.cfg
Error contacting service. It is probably not running.
[root@corehub-003 zookeeper]# jps
3956 Jps
3242 QuorumPeerMain
[root@corehub-003 zookeeper]#
```
> 解决当前问题的前提,确保myid中的ID号正确无误
> 原因是**`防火墙没有关闭`**,在关闭防火墙前提下,先需要依次停止01,02,03号zookeeper服务端
```
[root@corehub-001 zookeeper]# bin/zkServer.sh stop
ZooKeeper JMX enabled by default
Using config: /opt/devtool/zookeeper/bin/../conf/zoo.cfg
Stopping zookeeper ... STOPPED
```
```
[root@corehub-002 zookeeper]# bin/zkServer.sh stop
ZooKeeper JMX enabled by default
Using config: /opt/devtool/zookeeper/bin/../conf/zoo.cfg
Stopping zookeeper ... STOPPED
```
```
[root@corehub-003 zookeeper]# bin/zkServer.sh stop
ZooKeeper JMX enabled by default
Using config: /opt/devtool/zookeeper/bin/../conf/zoo.cfg
Stopping zookeeper ... STOPPED
```
最后依次关闭01,02,03号防火墙,并依次重新启动01,02,03号zookeeper服务端
依次启动和关闭的步骤就在此省略了,步骤按照案例以此类推即可
```
[root@corehub-001 zookeeper]# service iptables stop
iptables: Setting chains to policy ACCEPT: filter          [  OK  ]
iptables: Flushing firewall rules:                         [  OK  ]
iptables: Unloading modules:                               [  OK  ]
```


#### ✔️✔️ 测试 成功版本 ✔️✔️
#### 再次启动后,接下来查看运行成功状态
> 此时此刻我们看到了令人满意的结果😄😄
> 通过zookeeper 选举机制,我们可看出在集群中只要半数以上机器存活,就可以推选出Leader最为集群中的领导者
> 很显然corehub-002号服务作为Leader领导者,而剩下的corehub-001&corehub-003将作为follower跟随者
```
[root@corehub-001 zookeeper]# bin/zkServer.sh status
ZooKeeper JMX enabled by default
Using config: /opt/devtool/zookeeper/bin/../conf/zoo.cfg
Mode: follower
[root@corehub-001 zookeeper]#
```
```
[root@corehub-002 zookeeper]# bin/zkServer.sh status
ZooKeeper JMX enabled by default
Using config: /opt/devtool/zookeeper/bin/../conf/zoo.cfg
Mode: leader
[root@corehub-002 zookeeper]#
```
```
[root@corehub-003 zookeeper]# bin/zkServer.sh status
ZooKeeper JMX enabled by default
Using config: /opt/devtool/zookeeper/bin/../conf/zoo.cfg
Mode: follower
[root@corehub-003 zookeeper]#
```
#### 创建子节点方法并RunTest,返回结果集
``` java
package com.geekparkhub.zookeeper;

import org.apache.log4j.Logger;
import org.apache.zookeeper.*;
import org.junit.Before;
import org.junit.Test;
import java.io.IOException;

/**
 * GeekParkHub | 极客国际公园
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 *
 * Zookeeper测试类
 */

public class ZookeeperTest {

    /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(ZookeeperTest.class);

    /**
     * 服务端主机名称:Zookeeper客户端 端口号
     * Server HostName : Zookeeper Client port
     */
    private String connectString="corehub-001:2181,corehub-002:2181,corehub-003:2181";

    /**
     * 设置会话超时间 5000毫秒 = 5秒
     * Set session timeout 5000 milliseconds = 5 seconds
     */
    private int sessionTimeout = 5000;

    /**
     * 全局ZooKeeper客户端
     * Global Zoo Keeper client
     */
    private ZooKeeper zkClient;


    /**
     * 初始化方法
     * Initialization Method
     */
    @Before
    public void init() throws IOException {
      zkClient = new ZooKeeper(connectString, sessionTimeout, new Watcher() {
            public void process(WatchedEvent watchedEvent) {
            }
        });
    }

    /**
     * 创建子节点方法
     * Create child node method
     */
    @Test
    public void createNode() throws KeeperException, InterruptedException {
        /**
         * 引用客户端对象 调用create方法
         *
         * create(path,data,acl,createMode);
         * path 表示节点路径,在根目录下创建/geekparkhub路径
         * data 表示节点内容,内容不支持String类型字符串,应转型为字节类型
         * acl 表示访问权限控制,在ZooDefs.Ids中定义了接口变量,OPEN_ACL_UNSAFE不需要权限即可访问
         * createMode 表示节点储存数据类型 / 持久(Persistent) & 短暂(Ephemeral)
         */
        String path = zkClient.create("/geekparkhub","Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见".getBytes(),ZooDefs.Ids.OPEN_ACL_UNSAFE,CreateMode.PERSISTENT);
        log.info("Info : "+path);
    }
}
```
##### ✅✅如图所示:证明子节点方法与zookeeper服务端连接成功,并创建子节点,将数据写入节点中,打印结果集✅✅
![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/zookeeper/start_006.jpg)

##### 在linux中开启 zookeeper客户端 
```
[root@corehub-001 zookeeper]# bin/zkCli.sh
Connecting to localhost:2181
2019-01-22 01:17:08,677 [myid:] - INFO  [main:Environment@100] - Client environment:user.name=root
2019-01-22 01:17:08,677 [myid:] - INFO  [main:Environment@100] - Client environment:user.home=/root
JLine support is enabled
2019-01-22 01:17:09,001 [myid:] - INFO  [main-SendThread(localhost:2181):ClientCnxn$SendThread@876] - Socket connection established to localhost/127.0.0.1:2181, initiating session
2019-01-22 01:17:09,028 [myid:] - INFO  [main-SendThread(localhost:2181):ClientCnxn$SendThread@1299] - Session establishment complete on server localhost/127.0.0.1:2181, sessionid = 0x16871456f950001, negotiated timeout = 30000
WATCHER::
```
##### 通过 **`get / `** 指令,查询当前客户端向服务端写入的数据
```
[zk: localhost:2181(CONNECTED) 0] get /geekparkhub
Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
cZxid = 0x100000002
ctime = Tue Jan 22 00:38:11 CST 2019
mZxid = 0x100000002
mtime = Tue Jan 22 00:38:11 CST 2019
pZxid = 0x100000002
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 89
numChildren = 0
[zk: localhost:2181(CONNECTED) 1]
```

### 获取子节点并监听节点变化
#### 🤣🤣 有趣好玩的地方开始了 实时监听节点变化🤣🤣
![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/zookeeper/start_007.jpg)


#### 1.创建getChildren方法,RunTest,实时监听节点变化
``` java
package com.geekparkhub.zookeeper;

import org.apache.log4j.Logger;
import org.apache.zookeeper.*;
import org.junit.Before;
import org.junit.Test;
import java.io.IOException;
import java.util.List;

/**
 * GeekParkHub | 极客国际公园
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 *
 * Zookeeper测试类
 */

public class ZookeeperTest {

    /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(ZookeeperTest.class);

    /**
     * 服务端主机名称:Zookeeper客户端 端口号
     * Server HostName : Zookeeper Client port
     */
    private String connectString="corehub-001:2181,corehub-002:2181,corehub-003:2181";

    /**
     * 设置会话超时间 5000毫秒 = 5秒
     * Set session timeout 5000 milliseconds = 5 seconds
     */
    private int sessionTimeout = 5000;

    /**
     * 全局ZooKeeper客户端
     * Global Zoo Keeper client
     */
    private ZooKeeper zkClient;


    /**
     * 实时监听器 初始化方法
     * Initialization Method
     */
    @Before
    public void init() throws IOException {
      zkClient = new ZooKeeper(connectString, sessionTimeout, new Watcher() {
            public void process(WatchedEvent watchedEvent) {
                /**
                 * 引用客户端对象 调用getChildren方法
                 * getChildren(path,watcher);
                 * path 获取根路径下,所有的子节点
                 * watcher 是否监听 false / true
                 *
                 */
                log.info("--------- Start ---------");
                List<String> children = null;
                try {
                    children = zkClient.getChildren("/",true);
                    /**
                     * for循环 实时监听 遍历输出节点变化
                     */
                    for (String child : children){
                        log.info("Znode : "+child);
                    }
                    log.info("--------- End ---------");
                } catch (KeeperException e) {
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });
    }

    /**
     * 创建子节点方法
     * Create child node method
     */
    @Test
    public void createNode() throws KeeperException, InterruptedException {

        /**
         * 引用客户端对象 调用create方法
         *
         * create(path,data,acl,createMode);
         * path 表示节点路径,在根目录下创建/geekparkhub路径
         * data 表示节点内容,内容不支持String类型字符串,应转型为字节类型
         * acl 表示访问权限控制,在ZooDefs.Ids中定义了接口变量,OPEN_ACL_UNSAFE不需要权限即可访问
         * createMode 表示节点储存数据类型 / 持久(Persistent) & 短暂(Ephemeral)
         */

        String path = zkClient.create("/geekparkhub","Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见".getBytes(),ZooDefs.Ids.OPEN_ACL_UNSAFE,CreateMode.PERSISTENT);
        log.info("Info : "+path);
    }

    /**
     * 获取子节点并监听节点变化
     */
    @Test
    public void getDataWatcher() throws KeeperException, InterruptedException {
        /**
         * 为避免循环结束,无法实时监听,调用sleep方法
         */
        Thread.sleep(Long.MAX_VALUE);
    }
}
```
#### 2.在linux客户端,通过 **`create / `** 指令执行创建节点指令
```
[zk: localhost:2181(CONNECTED) 1] ls /
[zookeeper, geekparkhub]
[zk: localhost:2181(CONNECTED) 2] create /jeep-711 "GeekDeveloper"
Created /jeep-711
[zk: localhost:2181(CONNECTED) 3] create /geek "geek"             
Created /geek
[zk: localhost:2181(CONNECTED) 4] create /geeklab "geeklab"
Created /geeklab
[zk: localhost:2181(CONNECTED) 5] create /geekpark "geekpark"
Created /geekpark
[zk: localhost:2181(CONNECTED) 6] create /geekparks "geekparks"
Created /geekparks
[zk: localhost:2181(CONNECTED) 7] ls /                         
[zookeeper, geekparkhub, geek, geeklab, geekparks, jeep-711, geekpark]
[zk: localhost:2181(CONNECTED) 8] 
```

### 判断Zonde是否存在
#### 效果如图所示
![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/zookeeper/start_008.jpg)

##### 创建exists方法,RunTest,查询/geek节点与数据是否存在
``` java
package com.geekparkhub.zookeeper;

import org.apache.log4j.Logger;
import org.apache.zookeeper.*;
import org.apache.zookeeper.data.Stat;
import org.junit.Before;
import org.junit.Test;
import java.io.IOException;
import java.util.List;

/**
 * GeekParkHub | 极客国际公园
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 *
 * Zookeeper测试类
 */

public class ZookeeperTest {

    /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(ZookeeperTest.class);

    /**
     * 服务端主机名称:Zookeeper客户端 端口号
     * Server HostName : Zookeeper Client port
     */
    private String connectString="corehub-001:2181,corehub-002:2181,corehub-003:2181";

    /**
     * 设置会话超时间 5000毫秒 = 5秒
     * Set session timeout 5000 milliseconds = 5 seconds
     */
    private int sessionTimeout = 5000;

    /**
     * 全局ZooKeeper客户端
     * Global Zoo Keeper client
     */
    private ZooKeeper zkClient;

    /**
     * 实时监听器 初始化方法
     * Initialization Method
     */
    @Before
    public void init() throws IOException {
      zkClient = new ZooKeeper(connectString, sessionTimeout, new Watcher() {
            public void process(WatchedEvent watchedEvent) {

                /**
                 * 引用客户端对象 调用getChildren方法
                 * getChildren(path,watcher);
                 * path 获取根路径下,所有的子节点
                 * watcher 是否监听 false / true
                 *
                 */
//                log.info("--------- Start ---------");
//                List<String> children = null;
//                try {
//                    children = zkClient.getChildren("/",true);
//                    /**
//                     * for循环 实时监听 遍历输出节点变化
//                     */
//                    for (String child : children){
//                        log.info("Znode : "+child);
//                    }
//                    log.info("--------- End ---------");
//                } catch (KeeperException e) {
//                    e.printStackTrace();
//                } catch (InterruptedException e) {
//                    e.printStackTrace();
//                }
            }
        }
        );
    }

    /**
     * 创建子节点方法
     * Create child node method
     */
    @Test
    public void createNode() throws KeeperException, InterruptedException {

        /**
         * 引用客户端对象 调用create方法
         *
         * create(path,data,acl,createMode);
         * path 表示节点路径,在根目录下创建/geekparkhub路径
         * data 表示节点内容,内容不支持String类型字符串,应转型为字节类型
         * acl 表示访问权限控制,在ZooDefs.Ids中定义了接口变量,OPEN_ACL_UNSAFE不需要权限即可访问
         * createMode 表示节点储存数据类型 / 持久(Persistent) & 短暂(Ephemeral)
         */

        String path = zkClient.create("/geekparkhub","Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见".getBytes(),ZooDefs.Ids.OPEN_ACL_UNSAFE,CreateMode.PERSISTENT);
        log.info("Info : "+path);
    }

    /**
     * 获取子节点并监听节点变化
     */
    @Test
    public void getDataWatcher() throws KeeperException, InterruptedException {
        /**
         * 为避免循环结束,无法实时监听,调用sleep方法
         */
//        Thread.sleep(Long.MAX_VALUE);
    }

    /**
     * 判断Zonde是否存在
     */
    @Test
    public void exist() throws KeeperException, InterruptedException {

        /**
         * 引用客户端对象 调用exists方法
         * exists(path,watcher); 判断此节点是否有数据
         * path 获取此路径下,所有数据
         * watcher 是否监听 false / true
         *
         * 判断 /geek节点中,是否有数据
         */
         
        Stat exists = zkClient.exists("/geek",true);
        log.info("该节点存在且有数据 : "+exists == null ? "该节点不存在!":"该节点存在且有数据");
    }
}
```

## 11. 监听服务器节点动态
### 1.监听服务器节点动态 需求分析
> 在分布式系统中,主节点可以有多台,可以动态上下线,任意一台客户端都有可以实时感知到主节点服务器上下线
> 
> ![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/zookeeper/start_009.jpg)

### 2.Create Zookeeper 客户端节点
```
create /servers "server" 
Created /servers
[zk: localhost:2181(CONNECTED) 1] ls / 
[servers, zookeeper]
[zk: localhost:2181(CONNECTED) 2] 
```

### 3.Create 监听节点服务端 Class
![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/zookeeper/start_010.jpg)

``` java
package com.geekparkhub.zookeeper;

import org.apache.log4j.Logger;
import org.apache.zookeeper.*;
import java.io.IOException;

/**
 * GeekParkHub | 极客国际公园
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * <p>
 * 分发服务端 Class
 */

public class DistributeServer {

    /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(DistributeServer.class);

    /**
     * 服务端主机名称:Zookeeper客户端 端口号
     * Server HostName : Zookeeper Client port
     */
    private String connectString = "corehub-001:2181,corehub-002:2181,corehub-003:2181";

    /**
     * 设置会话超时间 5000毫秒 = 5秒
     * Set session timeout 5000 milliseconds = 5 seconds
     */
    private int sessionTimeout = 5000;

    /**
     * 全局ZooKeeper客户端
     * Global Zoo Keeper client
     */
    private ZooKeeper zkClient;

    public static void main(String[] args) throws IOException, KeeperException, InterruptedException {

        /**
         * 实例化 DistributeServer
         */
        DistributeServer server = new DistributeServer();

        /**
         * 连接 Zookeeper服务端集群
         * 调用getConnect()方法,建立网络连接
         */
        server.getConnect();

        /**
         * 向Zookeeper服务器 注册节点
         * 调用regist()方法,
         */
        server.regist(args[0]);

        /**
         * 实现 业务逻辑
         */
        server.business();

    }

    /**
     * 定义 建立网络连接方法
     */
    private void getConnect() throws IOException {
        zkClient = new ZooKeeper(connectString, sessionTimeout, new Watcher() {
            public void process(WatchedEvent watchedEvent) {
            }
        });
    }

    /**
     * 定义 注册方法
     * CreateMode.EPHEMERAL_SEQUENTIAL 表示短暂并带序号的数据存储,实现节点上下线
     * String hostname,当前属性需要动态获取主机名称,客户端每注册一次,就更新一次记录
     */
    private void regist(String hostname) throws KeeperException, InterruptedException {
        String path = zkClient.create("/servers/server", hostname.getBytes(), ZooDefs.Ids.OPEN_ACL_UNSAFE, CreateMode.EPHEMERAL_SEQUENTIAL);
        log.info("⬆️" + hostname + "is Online!");
    }

    /**
     * 业务逻辑
     */
    private void business() throws InterruptedException {
        /**
         * 让程序在睡一会
         */
        Thread.sleep(Long.MAX_VALUE);
    }
}
```

### 4.Create 监听节点客户端 Class
![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/zookeeper/start_011.jpg)

``` java
package com.geekparkhub.zookeeper;

import org.apache.log4j.Logger;
import org.apache.zookeeper.KeeperException;
import org.apache.zookeeper.WatchedEvent;
import org.apache.zookeeper.Watcher;
import org.apache.zookeeper.ZooKeeper;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * GeekParkHub | 极客国际公园
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * <p>
 * 分发客户端 Class
 */

public class DistributeClient {

    /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(DistributeClient.class);

    /**
     * 服务端主机名称:Zookeeper客户端 端口号
     * Server HostName : Zookeeper Client port
     */
    private String connectString = "corehub-001:2181,corehub-002:2181,corehub-003:2181";

    /**
     * 设置会话超时间 5000毫秒 = 5秒
     * Set session timeout 5000 milliseconds = 5 seconds
     */
    private int sessionTimeout = 5000;

    /**
     * 全局ZooKeeper客户端
     * Global Zoo Keeper client
     */
    private ZooKeeper zkClient;

    public static void main(String[] args) throws IOException, KeeperException, InterruptedException {

        /**
         * 实例化 DistributeClient
         */
        DistributeClient client = new DistributeClient();
        
        /**
         * 获取 Zookeeper服务端集群连接
         * 调用getConnect()方法,建立网络连接
         */
        client.getConnect();

        /**
         * 注册监听节点
         */
        client.getMonitor();

        /**
         * 业务逻辑
         */
        client.business();
    }

    /**
     * 定义 建立网络连接方法
     */
    private void getConnect() throws IOException {
        zkClient = new ZooKeeper(connectString, sessionTimeout, new Watcher() {
            /**
             * 无限实时监听 getMonitor方法
             * @param watchedEvent
             */
            public void process(WatchedEvent watchedEvent) {
                try {
                    getMonitor();
                } catch (KeeperException e) {
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });
    }

    /**
     * 定义 注册监听节点
     */
    private void getMonitor() throws KeeperException, InterruptedException {

        List<String> children = zkClient.getChildren("/servers", true);

        /**
         * 用于存储服务器节点主机名称集合
         */
        ArrayList<String> hosts = new ArrayList<String>();

        for (String child : children) {
            // 获取当前节点下的所以数据源
            byte[] data = zkClient.getData("/servers/" + child, false, null);
            hosts.add(new String(data));
        }
        // 将所有 在线主机名称 打印结果集
        log.info("==♨️== " + hosts + " ==♨️==");
    }

    /**
     * 定义 业务逻辑
     */
    private void business() throws InterruptedException {
        /**
         * 让程序在睡一会
         */
        Thread.sleep(Long.MAX_VALUE);
    }
}
```


## 12. 修仙之道 技术架构迭代 登峰造极之势
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
- Email：<jeep711.home.@gmail.com>—— <jeep-711@outlook.com> —— <geekparkhub@outlook.com>



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