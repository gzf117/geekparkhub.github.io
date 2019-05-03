# 大数据生态系统 修仙之道 HBase Blog

@(2019-04-10)[ Docs Language:简体中文 & English|Programing Language:HBase|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)|![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg) | ![GitHub repo size in bytes](https://img.shields.io/github/repo-size/geekparkhub/geekparkhub.github.io.svg) | GeekDeveloper:[JEEP-711](https://github.com/jeep711)|Github:[github.com/geekparkhub](https://github.com/geekparkhub)|Gitee:[gitee.com/geekparkhub](https://gitee.com/geekparkhub) ]

##  🐘 HBase Technology 修仙之道 刻苦修持 🐘

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



## 1. HBase 概述

### 1.1 HBase 简介
> HBase是基于谷歌公司BigTable开发的开源分布式数据库,具有`高可靠`/`高性能`/`面向列`/`可伸缩等特点`.
> 
> HBase运行在HDFS之上,主要用来存储`非结构化数据`和`半结构化数据`.
> 
> HBase通过水平扩展的方式实现于存储大表数据(表规模可以达到数十亿行以及数百列),并且对大表数据读写访问可达到实时级别.

- HBase由Powerset公司在2007年发起,最初是Hadoop的一部分,在此之后,HBase项目逐渐发展成为Apache软件基金会旗下顶级项目.
- HBase发展里程碑简述 : 
- 2006年11月 Google发布BigTable论文.
- 2007年2月 HBase作为Hadoop项目的子项目成立.
- 2007年10月 HBase第一个可用版本发布(Hadoop 0.15.0).
- 2010年5月 HBase成为Apache软件基金会顶级项目.
- 2011年1月 HBase0.90.0发布,该版本为面向所有用户的稳定版本.
- 2017年2月 HBase 1.2.x版本发布.


### 1.2 HBase 特点
#### 1.2.1 海量存储
> HBase适合存储PB级别海量数据,在PB级别数据以及采用廉价PC存储情况下,能在几十到百毫秒内返回数据,这与HBase极易扩展性息息相关,正式因为HBase良好的扩展性,才为海量数据存储提供了便利.

#### 1.2.2 列式存储
> 列式存储也就是列族存储,HBase是根据列族来存储数据,列族下面可以有非常之多的列,列族在创建表示就必须指定.

#### 1.2.3 极易扩展
> HBase扩展性主要体现在 : 
> 基于上层处理能力(RegionServer)的扩展
> 基于存储扩展(HDFS)
> 通过横向添加RegionServer机器,进行水平扩展,提升HBase上层处理能力,提升HBase服务更多Region能力.

#### 1.2.4 高并发
> 由于大部分使用HBase架构,都是采用廉价PC,因此单个I/O延迟其实并不小,一般在几十到几百毫秒之间,高并发其实是在并发情况下,HBase单个I/O延迟下降并不多,能获得高并发,低延时服务.

#### 1.2.5 稀疏
> 稀疏主要针对HBase列的灵活性,在列族中,可以指定任意列,在列数据为空的情况下,是不会占用存储空间.

### 1.3 HBase 应用场景
- 高吞吐量.
- 性能可伸缩.
- 海量数据(TB/PB).
- 能够同时处理结构化和非结构化数据.
- 需要在海量数据中实现高效随机读取.
- 不需要完全拥有传统关系型数据库所具备(原子性/一致性/独立性/持久性)ACID特性.

### 1.4 HBase 架构
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hbase/start_001.jpg)
- HBase一种是作为存储分布式文件系统,另一种是作为数据处理模型的MR框架,因为日常开发人员比较熟练的是结构化的数据进行处理,但是在HDFS直接存储的文件往往不具有结构化,所以催生出了HBase在HDFS上操作,如果需要查询数据,只需要通过键值便可以成功访问.
- HBase采用Master/Slave架构,主要角色包括(HMaster,管理节点)Master服务器,(HRegionServer,数据节点)Region服务器,Zookeeper服务器以及客户端,HBase以HDFS作为其底层存储来实现数据高可用,其本身不具备数据复制功能.

### 1.5 HBase 角色

#### 1.5.1 HMaster
> `HMaster 主节点`, HMaster主要负责 : HRegionServer管理以及元数据更改,包括以下内容(新HRegionServer注册 / 表的增删改查 / HRegionServer负载均衡 / Region表分区 / 分布调整 / Region分裂 / 裂变后分配以及迁移).
> 
> HMaster采用主备模式部署,集群启动时,通过竞争获得主HMaster角色,主HMaster只能有一个,备HMaster进程在集群运行期间处于休眠状态,不干涉任何集群事务,当主HMaster故障时,备用HMaster将取代主用HMaster对外提供服务.
- `HMaster 功能`
- 监控 RegionServer
- 处理 RegionServer故障转移
- 维护集群负载均衡
- 维护集群元数据信息
- 处理Region分配或移除
- 通过Zookeeper发布自身位置给客户端

#### 1.5.2 HRegionServer
> HRegionServer是HBase从节点,HRegionServer负责提供表数据读写服务,是数据存储和和计算单元,HRegionServer与HDFS集群的DataNode部署在一起,实现数据存储功能.
- `HRegionServer 功能`
- 处理客户端读写请求
- 负责存储HBase实际数据
- 处理分配给Region
- 刷新缓存到HDFS
- 维护HLog
- 执行压缩

#### 1.5.3 HDFS
> HDFS为HBase提供最终底层数据存储服务,同时为HBase提供高可用.
> HDFS提供元数据和表数据的底层分布式存储服务.
> HDFS数据副本,保证高可靠性和高可用性.

#### 1.5.4 Zookeeper
> Zookeeper为HBase集群各进程提供分布式协作服务,各HRegionServer将自身信息注册到Zookeeper中,HMaster据此感知各个HRegionServer健康状态.
> 
> HBase通过Zookeeper来作为master高可用 / HRegionServer监控 / 元数据入口 / 集群配置维护等.
> 
> 通过Zookeeper来保证集群中只有1个master运行,如master异常,会通过竞争机制产生新的master对外提供服务.
> 
> 通过Zookeeper来监控HRegionServer状态,当HRegionServer有异常时,通过回调形式通知MasterHRegionServer上下线信息.
> 
> 通过Zookeeper存储元数据信息统一入口地址.

#### 1.5.5 Client
> Client包括访问HBase接口,另外Client还维护对应的Cache来加速HBase访问.

#### 1.5.6 其他组件
##### 1.5.6.1 Write-Ahead logs
> HBase修改记录,当对HBase读写数据时,数据不是直接写进磁盘,它会在内存中保留一段时间(时间以及数据量阈值可以设定),但把数据保存在内存中可能有更高的概率引起数据丢失,为了解决这个问题,数据会先写在一个叫做Write-Ahead logfile文件中,然后再写入内存中,所以在系统出现故障时,数据可以通过这个日志文件重建.
##### 1.5.6.2 HFile
> 在磁盘上保存原始数据实际的物理文件,是实际存储文件.
##### 1.5.6.3 Store
> HFile存储在Store中,一个Store对应HBase表中一个列族.
##### 1.5.6.4 MemStore
> 内存存储位于内存中,用来保存当前数据操作,所以当数据保存在WAL中之后,RegsionServer会在内存中存储键值对.
##### 1.5.6.5 Region
> Hbase表分片,HBase表会根据RowKey值被切分成不同Region存储在RegionServer中,在一个RegionServer中可以有多个不同的Region.

## 2. HBase 部署
### 2.1 Zookeeper 服务
- 保证Zookeeper集群服务正常运行
```
[root@systemhub511 zookeeper]$ bin/zkServer.sh start
```
```
[root@systemhub611 zookeeper]$ bin/zkServer.sh start
```
```
[root@systemhub711 zookeeper]$ bin/zkServer.sh start
```
### 2.2 Hadoop 服务
- 保证Hadoop集群服务正常运行
```
[root@systemhub511 hadoop]$ sbin/start-dfs.sh
```
```
[root@systemhub611 hadoop]$ sbin/start-yarn.sh
```
### 2.3 HBase 服务
- 解压HBase到指定目录
```
[root@systemhub511 software]# tar -zxvf hbase-1.3.1-bin.tar.gz -C /opt/module/
```
- 重命名包名称
```
[root@systemhub511 module]# mv hbase-1.3.1 hbase
```
- 查看HBase目录结构
```
[root@systemhub511 hbase]# ll
total 348
drwxr-xr-x.  4 root root   4096 Apr  5  2017 bin
-rw-r--r--.  1 root root 148959 Apr  7  2017 CHANGES.txt
drwxr-xr-x.  2 root root   4096 Apr  5  2017 conf
drwxr-xr-x. 12 root root   4096 Apr  7  2017 docs
drwxr-xr-x.  7 root root   4096 Apr  7  2017 hbase-webapps
-rw-r--r--.  1 root root    261 Apr  7  2017 LEGAL
drwxr-xr-x.  3 root root   4096 Apr 26 14:43 lib
-rw-r--r--.  1 root root 130696 Apr  7  2017 LICENSE.txt
-rw-r--r--.  1 root root  43258 Apr  7  2017 NOTICE.txt
-rw-r--r--.  1 root root   1477 Sep 21  2016 README.txt
[root@systemhub511 hbase]# 
```
- 配置HBase
- vim `hbase-env.sh`配置文件
```
[root@systemhub511 hbase]# echo $JAVA_HOME
/opt/module/jdk1.8.0_162
[root@systemhub511 hbase]# cd conf/
[root@systemhub511 conf]# vim hbase-env.sh
```
```
# The java implementation to use.  Java 1.7+ required.
export JAVA_HOME=/opt/module/jdk1.8.0_162
export HBASE_MANAGES_ZK=false
```
- vim `hbase-site.xml`配置文件
```
<configuration>
  <property>
   <name>hbase.rootdir</name>   
   <value>hdfs://systemhub511:9000/hbase</value>     
  </property>
  <property>             
    <name>hbase.cluster.distributed</name>
    <value>true</value>
  </property>
  <!--0.98后的新变动,之前版本没有.port,默认端口为60000 -->
  <property>
    <name>hbase.master.port</name>
    <value>16000</value>
  </property>          
  <property>            
    <name>hbase.zookeeper.quorum</name>
    <value>systemhub511:2181,systemhub611:2181,systemhub711:2181</value>
  </property>
  <property>                        
    <name>hbase.zookeeper.property.dataDir</name>
    <value>/opt/module/zookeeper/zkData</value>
  </property>
</configuration>
```

- vim `regionservers`配置文件
```
systemhub511
systemhub611
systemhub711
```
- 在/usr/local/bin目录下创建脚本
- 启动所有集群节点
- vim `start-cluster.sh`
```
#!/bin/bash
echo "================          Start All Node Services         ==========="
echo "================================================================"
echo "================          Starting Zookeeper              ==========="
echo "================================================================"

for i in root@systemhub511 root@systemhub611 root@systemhub711
do
    ssh $i 'source /etc/profile;/opt/module/zookeeper/bin/zkServer.sh start'
done

echo "================          Starting HDFS           ==========="
ssh root@systemhub511 '/opt/module/hadoop/sbin/start-dfs.sh'

echo "================          Starting YARN           ==========="
ssh root@systemhub611 '/opt/module/hadoop/sbin/start-yarn.sh'

echo "================          Starting JobHistoryServer       ==========="
ssh root@systemhub511 '/opt/module/hadoop/sbin/mr-jobhistory-daemon.sh start historyserver'
```
- 关闭所有集群节点
- vim `stop-cluster.sh`
```
#!/bin/bash
echo "================          Stopping All Node Services      ==========="
echo "================          Stopping JobHistoryServer       ==========="
ssh root@systemhub511 '/opt/module/hadoop/sbin/mr-jobhistory-daemon.sh stop historyserver'

echo "================          Stopping YARN           ==========="
ssh root@systemhub611 '/opt/module/hadoop/sbin/stop-yarn.sh'

echo "================          Stopping HDFS           ==========="
ssh root@systemhub511 '/opt/module/hadoop/sbin/stop-dfs.sh'

echo "================          Stopping Zookeeper      ==========="
for i in root@systemhub511 root@systemhub611 root@systemhub711
do
    ssh $i 'source /etc/profile;/opt/module/zookeeper/bin/zkServer.sh stop'
done
```
- 查看所有集群节点状态
- vim `jps.sh`
```
 #!/bin/bash
for host in root@systemhub511 root@systemhub611 root@systemhub711
do
    echo "================      $host All Processes             ==========="
    ssh $host '/opt/module/jdk1.8.0_162/bin/jps'
done
```
- HBase软连接Hadoop配置
```
[root@systemhub511 ~]# ln -s /opt/module/hadoop/etc/hadoop/core-site.xml /opt/module/hbase/conf/core-site.xml
[root@systemhub511 ~]#
[root@systemhub511 ~]# ln -s /opt/module/hadoop/etc/hadoop/hdfs-site.xml /opt/module/hbase/conf/hdfs-site.xml
[root@systemhub511 ~]#
```
- HBase远程分发其他集群
```
[root@systemhub511 ~]# scp -r /opt/module/hbase/ systemhub611:/opt/module/hbase/
[root@systemhub511 ~]# scp -r /opt/module/hbase/ systemhub711:/opt/module/hbase/
```
- 启动HBase服务
- 方式一
```
[root@systemhub511 hbase]# bin/hbase-daemon.sh start master
[root@systemhub511 hbase]# bin/hbase-daemon.sh start regionserver
```
- 方式二
```
[root@systemhub511 hbase]# bin/start-hbase.sh
starting master, logging to /opt/module/hbase/bin/../logs/hbase-root-master-systemhub511.out
systemhub711: starting regionserver, logging to /opt/module/hbase/bin/../logs/hbase-root-regionserver-systemhub711.out
systemhub611: starting regionserver, logging to /opt/module/hbase/bin/../logs/hbase-root-regionserver-systemhub611.out
systemhub511: starting regionserver, logging to /opt/module/hbase/bin/../logs/hbase-root-regionserver-systemhub511.out
```
- 如果集群之间的节点时间不同步,会导致regionserver无法启动,抛出`ClockOutOfSyncException`异常
- 方式一:修改集群同步时间服务 - [快速回顾通道](https://geekparkhub.github.io/technical_guide/programing_language/hadoop/hadoop.html#集群时间同步)
- 方式二:在配置文件中追加 `hbase.master.maxclockskew`属性值为最大值即可
```
<property>
  <name>hbase.master.maxclockskew</name>
  <value>180000</value>
  <description>Time difference of regionserver from master</description>
</property>
```
- 启动服务后,查看运行结果
- 可以通过`host:port`方式访问HBase管理页
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hbase/start_002.jpg)

## 3. HBase Shell
### 3.1 基本操作
#### 3.1.1 进入HBase客户端命令行窗口
- `bin/hbase shell`
``` powershell
[root@systemhub511 hbase]# bin/hbase shell
hbase(main):001:0> 
```
#### 3.1.2 查看帮助命令
- `help`
```
hbase(main):001:0> help
HBase Shell, version 1.3.1, r930b9a55528fe45d8edce7af42fef2d35e77677a, Thu Apr  6 19:36:54 PDT 2017
Type 'help "COMMAND"', (e.g. 'help "get"' -- the quotes are necessary) for help on a specific command.
Commands are grouped. Type 'help "COMMAND_GROUP"', (e.g. 'help "general"') for help on a command group.

COMMAND GROUPS:
  Group name: general
  Commands: status, table_help, version, whoami

  Group name: ddl
  Commands: alter, alter_async, alter_status, create, describe, disable, disable_all, drop, drop_all, enable, enable_all, exists, get_table, is_disabled, is_enabled, list, locate_region, show_filters

The HBase shell is the (J)Ruby IRB with the above HBase-specific commands added.
For more on the HBase Shell, see http://hbase.apache.org/book.html
hbase(main):002:0> 
```
#### 3.1.3 查看当前数据库中有哪些表
- `list`
```
hbase(main):002:0> list
TABLE        
0 row(s) in 0.4020 seconds
=> []
hbase(main):003:0>
```

### 3.2 表操作
#### 3.2.1 创建表
- `create '表名','列族名'`
```
hbase(main):003:0> create 'test','info'
0 row(s) in 2.8000 seconds

=> Hbase::Table - test
hbase(main):004:0>
```
#### 3.2.2 插入数据到表
- `put '表名','主键ID','列族名:列名称','value'`
```
hbase(main):004:0> put 'test','0001','info:name','testuser001'
0 row(s) in 0.3590 seconds

hbase(main):005:0>
```
#### 3.2.3 扫描查看表数据
- `scan '表名'`
```
hbase(main):008:0> scan 'test'
ROW                        COLUMN+CELL                                                                 
 0001                      column=info:age, timestamp=1556459945452, value=60                          
 0001                      column=info:name, timestamp=1556459442613, value=testuser001                
 0002                      column=info:age, timestamp=1556459962770, value=70                          
 0002                      column=info:name, timestamp=1556459836540, value=testuser002                
2 row(s) in 0.0450 seconds

hbase(main):009:0> 
hbase(main):012:0> scan 'test',{STARTROW => '0001',STOPROW => '0002'}
ROW                        COLUMN+CELL
 0001                      column=info:age, timestamp=1556459945452, value=60                          
 0001                      column=info:name, timestamp=1556459442613, value=testuser001                
1 row(s) in 0.0310 seconds

hbase(main):013:0> 
```
#### 3.2.4 查看 指定行或指定列族:列数据
- `get '表名','主键ID'`
```
hbase(main):009:0> get 'test','0001'
COLUMN                     CELL         
 info:age                  timestamp=1556459945452, value=60   
 info:name                 timestamp=1556459442613, value=testuser001
1 row(s) in 0.0460 seconds
hbase(main):010:0> get 'test','0001','info:name'
COLUMN                     CELL                                                                        
 info:name                 timestamp=1556459442613, value=testuser001
1 row(s) in 0.0260 seconds
hbase(main):011:0> 
```
#### 3.2.5 查看表结构
```
hbase(main):011:0> describe 'test'
Table test is ENABLED
test                                                                                                   
COLUMN FAMILIES DESCRIPTION
{NAME => 'info', BLOOMFILTER => 'ROW', VERSIONS => '1', IN_MEMORY => 'false', KEEP_DELETED_CELLS => 'FA
LSE', DATA_BLOCK_ENCODING => 'NONE', TTL => 'FOREVER', COMPRESSION => 'NONE', MIN_VERSIONS => '0', BLOC
KCACHE => 'true', BLOCKSIZE => '65536', REPLICATION_SCOPE => '0'}                                      
1 row(s) in 0.1010 seconds
hbase(main):012:0> 
```
#### 3.2.6 变更表信息
- 将info列族中的数据存放3个版本
```
hbase(main):014:0> alter 'test',{NAME=>'info',VERSIONS=>3}
Updating all regions with the new schema...
0/1 regions updated.
1/1 regions updated.
Done.
0 row(s) in 3.0960 seconds
hbase(main):015:0> 
hbase(main):015:0> get 'test','0001',{COLUMN=>'info:name',VERSIONS=>3}
COLUMN                     CELL
 info:name                 timestamp=1556459442613, value=testuser001                                  
1 row(s) in 0.0260 seconds
hbase(main):016:0>
```
#### 3.2.7 更新指定字段数据
```
hbase(main):004:0> put 'test','0001','info:name','testuser003'
0 row(s) in 0.3590 seconds

hbase(main):005:0>
```
#### 3.2.8 统计表数据行数
```
hbase(main):016:0> count 'test'
2 row(s) in 0.1140 seconds
=> 2
hbase(main):017:0> 
```
#### 3.2.9 删除数据
- 删除某rowkey某一列数据
```
hbase(main):017:0> delete 'test','0002','info:age'
```
- 删除某rowkey全部数据
```
hbase(main):016:0> deleteall 'test','0001'
```
#### 3.2.10 清空表数据
- 清空表操作顺序为先disable,然后再truncate
```
hbase(main):018:0> truncate 'test'
```
#### 3.2.11 删除表
- 需要先让该表为disable状态,然后才能删除表
- 如果直接drop表,会抛出异常：`Drop the named table. Table must first be disabledERROR: Table test is enabled. Disable it first.`
```
hbase(main):019:0> disable 'test'
```
```
hbase(main):020:0> drop 'test'
```

## 4. HBase 数据结构
### 4.1 Row Key
> 与nosql数据库们一样,`row key`是用来检索记录主键,访问HBASE表中的行,只有三种方式 :
- 1.通过单个`row key`访问
- 2.通过`row key`的range(正则)
- 3.全表扫描
> `Row key`行键(Row key)可以是任意字符串(最大长度是`64KB`,实际应用中长度一般为10-100bytes),在HBASE内部,`row key`保存为字节数组, 存储时数据按照`Row key`的字典序(byte order)排序存储,设计key时,要充分排序存储这个特性,将经常一起读取的行存储放到一起(位置相关性).

### 4.2 Columns Family
> 列族 : HBASE表中每个列都归属于某个列族,列族是表的schema的一部分(而列不是),必须在使用表之前定义,列名都以列族作为前缀,例如`courses:history,courses:math`都属于`courses`这个列族.

### 4.3 Cell
> 由`{row key, columnFamily, version}` 唯一确定单元,cell中数据是没有类型的,全部是字节码形式存贮,关键字 : 无类型/字节码.

### 4.4 Time Stamp
> HBASE中通过`rowkey`和`columns`确定为一个存贮单元称为cell,每个cell都保存着同一份数据的多个版本,版本通过时间戳来索引,`时间戳类型`是`64位整型`,时间戳可以由HBASE(在数据写入时自动)赋值,此时时间戳是精确到毫秒的当前系统时间,时间戳也可以由开发者显式赋值,如果应用程序要避免数据版本冲突,就必须自己生成具有唯一性的时间戳,每个cell中,不同版本的数据按照时间倒序排序,即最新的数据排在最前面.
> 
> 为了避免数据存在过多版本造成管理(包括存贮和索引)负担,HBASE提供了两种数据版本回收方式.
> 一是保存数据的最后n个版本.
> 二是保存最近一段时间内的版本(比如最近七天),用户可以针对每个列族进行设置.

### 4.5 命名空间
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hbase/start_003.jpg)

> 1.`Table` : 表 , 所以的表都是命名空间的成员,既表必属于某个命名空间,如果没有指定,则在default默认命名空间中.
> 
> 2.`RegionServerGroup` : 一个命名空间包含了默认的RegionServerGroup.
> 
> 3.`Permission` : 权限 , 命名空间能够让开发者来定义访问控制表ACL(Access Control List). 例如 : 创建表 / 读取表 / 删除 / 更新等操作. 
> 
> 4.`Quota` : 限额 , 可以强制一个命名空间可包含的region数据.


## 5. HBase 原理

### 5.1 HBase 读数据流程

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hbase/start_005.jpg)
- 1.Client先访问Zookeeper,从meta表读取region位置,然后读取meta表中数据,meta中又存储了用户表的region信息.
- 2.根据namespace、表名和rowkey在meta表中找到对应的region信息.
- 3.找到region对应的RegionServer.
- 4.查找对应的region.
- 5.先从MemStore找数据,如果没有,再到StoreFile上读(为了读取效率).
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hbase/start_008.jpg)

- 查看HBase元数据内容
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hbase/start_004.jpg)
- 查看Zookeeper存储数据内容
```
[zk: localhost:2181(CONNECTED) 0] ls /
[cluster, controller_epoch, controller, brokers, zookeeper, admin, isr_change_notification, consumers, latest_producer_id_block, config, hbase]
```
- 查看Zookeeper存储HBase数据内容
```
[zk: localhost:2181(CONNECTED) 1] ls /hbase
[replication, meta-region-server, rs, splitWAL, backup-masters, table-lock, flush-table-proc, region-in-transition, online-snapshot, switch, master, running, recovering-regions, draining, namespace, hbaseid, table]
[zk: localhost:2181(CONNECTED) 2] 
```
- 查看Zookeeper存储HBase meta-region-server
```
[zk: localhost:2181(CONNECTED) 4] get /hbase/meta-region-server
�regionserver:16020e��;0Z�PBUF
⎽≤⎽├␊└␤┤␉711�£�����-
␌Z│␋␍ = 0│1␊00000051
␌├␋└␊ = M⎺┼ A⎻⎼ 29 01:37:37 CST 2019
└Z│␋␍ = 0│1␊00000051
└├␋└␊ = M⎺┼ A⎻⎼ 29 01:37:37 CST 2019
⎻Z│␋␍ = 0│1␊00000051
␌┴␊⎼⎽␋⎺┼ = 0
␍▒├▒V␊⎼⎽␋⎺┼ = 0
▒␌┌V␊⎼⎽␋⎺┼ = 0
␊⎻␤␊└␊⎼▒┌O┬┼␊⎼ = 0│0
␍▒├▒L␊┼±├␤ = 65
┼┤└C␤␋┌␍⎼␊┼ = 0
[≥┐: ┌⎺␌▒┌␤⎺⎽├:2181(CONNECTED) 5] 
```
- 查看hbase:meta元数据信息表
```
hbase(main):002:0> scan 'hbase:meta'
ROW                        COLUMN+CELL                                                                 
 hbase:namespace,,15562836 column=info:regioninfo, timestamp=1556473360414, value={ENCODED => d89184e0b
 52968.d89184e0b0e8bf9782b 0e8bf9782b86edf991f56d2, NAME => 'hbase:namespace,,1556283652968.d89184e0b0e
 86edf991f56d2.            8bf9782b86edf991f56d2.', STARTKEY => '', ENDKEY => ''}                      
 hbase:namespace,,15562836 column=info:seqnumDuringOpen, timestamp=1556473360414, value=\x00\x00\x00\x0
 52968.d89184e0b0e8bf9782b 0\x00\x00\x00\x14                                                           
 86edf991f56d2.                                                                                        
 hbase:namespace,,15562836 column=info:server, timestamp=1556473360414, value=systemhub511:16020       
 52968.d89184e0b0e8bf9782b                                                                             
 86edf991f56d2.                                                                                        
 hbase:namespace,,15562836 column=info:serverstartcode, timestamp=1556473360414, value=1556473045363   
 52968.d89184e0b0e8bf9782b                                                                             
 86edf991f56d2.                                                                                        
 test,,1556459101215.6b00f column=info:regioninfo, timestamp=1556473359938, value={ENCODED => 6b00fc62a
 c62ac627c675022a7fafb6fbf c627c675022a7fafb6fbfa0, NAME => 'test,,1556459101215.6b00fc62ac627c675022a7
 a0.                       fafb6fbfa0.', STARTKEY => '', ENDKEY => ''}                                 
 test,,1556459101215.6b00f column=info:seqnumDuringOpen, timestamp=1556473359938, value=\x00\x00\x00\x0
 c62ac627c675022a7fafb6fbf 0\x00\x00\x00\x13                                                           
 a0.                                                                                                   
 test,,1556459101215.6b00f column=info:server, timestamp=1556473359938, value=systemhub611:16020       
 c62ac627c675022a7fafb6fbf                                                                             
 a0.                                                                                                   
 test,,1556459101215.6b00f column=info:serverstartcode, timestamp=1556473359938, value=1556473042292   
 c62ac627c675022a7fafb6fbf                                                                             
 a0.                                                                                                   
2 row(s) in 0.0530 seconds

hbase(main):003:0> 
```

### 5.2 HBase 写数据流程
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hbase/start_007.jpg)
- 1.Client向HregionServer发送写请求
- 2.HregionServer将数据写到HLog(write ahead log),为了数据持久化和恢复.
- 3.HregionServer将数据写到内存(MemStore)
- 4.反馈Client写入成功.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hbase/start_006.jpg)

### 5.3 HBase 数据Flush过程
- 1.当MemStore数据达到阈值(默认是128M,老版本是64M),将数据刷到硬盘,将内存中数据删除,同时删除HLog中历史数据.
- 2.并将数据存储到HDFS中.
- 3.在HLog中做标记点.

### 5.4 HBase 数据Compact过程
- 1.当数据块达到4块,Hmaster将数据块加载到本地进行合并.
- 2.当合并数据超过256M,进行拆分,将拆分后的Region分配给不同的HregionServer管理.
- 3.当HregionServer宕机后,将HregionServer上的hlog拆分,然后分配给不同HregionServer加载,修改.META
- 4.注意 : HLog会同步到HDFS.

### 5.5 Hmaster 职责
- 1.管理用户对Table增、删、改、查操作.
- 2.记录Region在哪一台HRegion Server服务器上.
- 3.在Region Split后,负责新Region分配.
- 4.新机器加入时,管理HRegion Server负载均衡,调整Region分布.
- 5.在HRegion Server宕机后,负责失效HRegion Server上的Regions迁移.

### 5.6 HRegionServer 职责
- 1.HRegion Server主要负责响应用户I/O请求.向HDFS文件系统中读写数据.是HBASE中最核心模块.
- 2.HRegion Server管理了很多table分区,也就是region.

### 5.7 Client 职责
- 1.HBASE Client使用HBASE的RPC机制与HMaster和RegionServer进行通信.
- 2.管理类操作 : Client与HMaster进行RPC.
- 3.数据读写类操作 : Client与HRegionServer进行RPC.

## 6. HBase New API
### 6.1 环境准备
- JetBrains IntelliJ IDEA New Maven Project | 此过程省略
- Add pom.xml
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.geekparkhub.core.hbase.api</groupId>
    <artifactId>hbase_server</artifactId>
    <version>1.0-SNAPSHOT</version>
    <dependencies>
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
            <groupId>jdk.tools</groupId>
            <artifactId>jdk.tools</artifactId>
            <version>1.8</version>
            <scope>system</scope>
            <systemPath>/Library/Java/JavaVirtualMachines/jdk1.8.0_201.jdk/Contents/Home/lib/tools.jar</systemPath>
        </dependency>
    </dependencies>
</project>
```

### 6.2 判断数据表是否存在
``` java
package com.geekparkhub.core.hbase.api.producehub;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.*;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.util.Bytes;

import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * HbaseHub
 * <p>
 */

public class HbaseHub {

    /**
     * Public Configuration information
     * 公共配置信息
     */
    private static Admin admin = null;
    private static Connection connection = null;
    private static Configuration configuration;

    static {
        /**
         * HBase ConfigurationFile
         * HBase 配置文件
         */
        configuration = HBaseConfiguration.create();
        configuration.set("hbase.zookeeper.quorum", "172.16.168.130");
        configuration.set("hbase.zookeeper.property.clientPort", "2181");
        try {
            /**
             * Get Connected
             * 获取连接
             */
            connection = ConnectionFactory.createConnection(configuration);

            /**
             * Get HBase Administrator Object
             * 获取HBase管理员对象
             */
            admin = connection.getAdmin();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Close Resource
     * 关闭资源
     *
     * @param conf
     * @param admin
     */
    private static void close(Connection conf, Admin admin) {
        if (conf != null) {
            try {
                conf.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        if (admin != null) {
            try {
                admin.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * Determine if DataTable Exists
     * 判断数据表是否存在
     *
     * @param tableName
     */
    public static boolean isTableExist(String tableName) throws IOException {

        /**
         * Execution Method
         * 执行方法
         */
        boolean tableExists = admin.tableExists(TableName.valueOf(tableName));

        return tableExists;
    }

    public static void main(String[] args) throws IOException {

        /**
         * isTableExist Result
         */
        System.out.printf("test isTableExist Result is = " + String.valueOf(isTableExist("test")) + "\n");
        System.out.printf("test001 isTableExist Result is = " + String.valueOf(isTableExist("test001")) + "\n");
        System.out.printf("test002 isTableExist Result is = " + String.valueOf(isTableExist("test002")) + "\n");
        System.out.printf("test003 isTableExist Result is = " + String.valueOf(isTableExist("test003")) + "\n");

        /**
         * Close Resource
         * 关闭资源
         */
        close(connection, admin);
    }
}
```
- 执行返回结果
``` prolog
test isTableExist Result is = true
test001 isTableExist Result is = true
test002 isTableExist Result is = false
test003 isTableExist Result is = false
```


### 6.3 创建数据表
``` java
package com.geekparkhub.core.hbase.api.producehub;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.*;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.util.Bytes;

import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * HbaseHub
 * <p>
 */

public class HbaseHub {

    /**
     * Public Configuration information
     * 公共配置信息
     */
    private static Admin admin = null;
    private static Connection connection = null;
    private static Configuration configuration;

    static {

        /**
         * HBase ConfigurationFile
         * HBase 配置文件
         */
        configuration = HBaseConfiguration.create();
        configuration.set("hbase.zookeeper.quorum", "172.16.168.130");
        configuration.set("hbase.zookeeper.property.clientPort", "2181");
        try {
            /**
             * Get Connected
             * 获取连接
             */
            connection = ConnectionFactory.createConnection(configuration);

            /**
             * Get HBase Administrator Object
             * 获取HBase管理员对象
             */
            admin = connection.getAdmin();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Close Resource
     * 关闭资源
     *
     * @param conf
     * @param admin
     */
    private static void close(Connection conf, Admin admin) {
        if (conf != null) {
            try {
                conf.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        if (admin != null) {
            try {
                admin.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * Determine if DataTable Exists
     * 判断数据表是否存在
     *
     * @param tableName
     */
    public static boolean isTableExist(String tableName) throws IOException {

        /**
         * Execution Method
         * 执行方法
         */
        boolean tableExists = admin.tableExists(TableName.valueOf(tableName));

        return tableExists;
    }

    /**
     * Create DataTable
     * 创建数据表
     *
     * @param tableName
     * @param columnFamily
     * @throws IOException
     */
    public static void createTable(String tableName, String... columnFamily) throws IOException {

        /**
         * Verify that the DataTable Exists Before Creating the DataTable
         * 创建数据表前,验证数据表是否存在
         */
        if (isTableExist(tableName)) {
            System.out.printf(tableName + " Data table creation failed , " + tableName + " Data table already exists!" + "\n");
            return;
        }

        /**
         * Instantiation Table Description information
         * 实例化 表描述信息
         */
        HTableDescriptor tableDescriptor = new HTableDescriptor(TableName.valueOf(tableName));

        /**
         * Add Multiple Column Families
         * 添加多个列族
         */
        for (String cn : columnFamily) {
            /**
             * Instantiation Column Name Description information
             * 实例化 列名描述信息
             */
            HColumnDescriptor columnDescriptor = new HColumnDescriptor(String.valueOf(cn));
            tableDescriptor.addFamily(columnDescriptor);
        }
        /**
         * Execution Method
         * 执行方法
         */
        admin.createTable(tableDescriptor);

        /**
         * Logger INFO
         */
        System.out.printf(tableName + " Data Sheet Was Created Successfully!" + "\n");
    }

    public static void main(String[] args) throws IOException {

        /**
         * CreateTable Result
         */
        createTable("test001", "info");
        createTable("test_factory", "factorymode", "factoryinfo");
        System.out.printf("factory TableExist Result is = " + String.valueOf(isTableExist("factory")) + "\n");
        System.out.printf("test_factory TableExist Result is = " + String.valueOf(isTableExist("test_factory")) + "\n");

        /**
         * Close Resource
         * 关闭资源
         */
        close(connection, admin);
    }
}
```
- 执行返回结果
``` prolog
test001 Data sheet was created successfully!
test_factory Data sheet was created successfully!
test_factory TableExist Result is = true
factory TableExist Result is = false
```


### 6.4 删除数据表
``` java
package com.geekparkhub.core.hbase.api.producehub;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.*;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.util.Bytes;

import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * HbaseHub
 * <p>
 */

public class HbaseHub {

    /**
     * Public Configuration information
     * 公共配置信息
     */
    private static Admin admin = null;
    private static Connection connection = null;
    private static Configuration configuration;

    static {

        /**
         * HBase ConfigurationFile
         * HBase 配置文件
         */
        configuration = HBaseConfiguration.create();
        configuration.set("hbase.zookeeper.quorum", "172.16.168.130");
        configuration.set("hbase.zookeeper.property.clientPort", "2181");
        try {
        
            /**
             * Get Connected
             * 获取连接
             */
            connection = ConnectionFactory.createConnection(configuration);

            /**
             * Get HBase Administrator Object
             * 获取HBase管理员对象
             */
            admin = connection.getAdmin();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Close Resource
     * 关闭资源
     *
     * @param conf
     * @param admin
     */
    private static void close(Connection conf, Admin admin) {
        if (conf != null) {
            try {
                conf.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        if (admin != null) {
            try {
                admin.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * Determine if DataTable Exists
     * 判断数据表是否存在
     *
     * @param tableName
     */
    public static boolean isTableExist(String tableName) throws IOException {

        /**
         * Execution Method
         * 执行方法
         */
        boolean tableExists = admin.tableExists(TableName.valueOf(tableName));

        return tableExists;
    }

    /**
     * Delete Data Table
     * 删除数据表
     *
     * @param tableName
     * @throws IOException
     */
    public static void deleteTable(String tableName) throws IOException {

        /**
         * Before Deleting the Data Table, Verify that the Data Table Exists.
         */
        if (!isTableExist(tableName)) {
            System.out.println("Data Table Deletion Failed , Reason : The Data Table Does Not Exist !");
            return;
        }

        /**
         * Data Table Offline
         * 数据表下线
         */
        admin.disableTable(TableName.valueOf(tableName));

        /**
         * Delete Data Table
         * 删除数据表
         */
        admin.deleteTable(TableName.valueOf(tableName));

        /**
         * Logger INFO
         */
        System.out.println("Data Table Has Been Deleted Successfully!");
    }

    public static void main(String[] args) throws IOException {

        /**
         * Delete Data Table
         */
        deleteTable("test_factory");

        /**
         * Close Resource
         * 关闭资源
         */
        close(connection, admin);
    }
}
```
- 执行返回结果
```
INFO [org.apache.hadoop.hbase.client.HBaseAdmin] - Disabled test_factory
INFO [org.apache.hadoop.hbase.client.HBaseAdmin] - Deleted test_factory
Data Table Has Been Deleted Successfully!
```


### 6.5 添加数据
``` java
package com.geekparkhub.core.hbase.api.producehub;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.*;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.util.Bytes;

import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * HbaseHub
 * <p>
 */

public class HbaseHub {

    /**
     * Public Configuration information
     * 公共配置信息
     */
    private static Admin admin = null;
    private static Connection connection = null;
    private static Configuration configuration;

    static {

        /**
         * HBase ConfigurationFile
         * HBase 配置文件
         */
        configuration = HBaseConfiguration.create();
        configuration.set("hbase.zookeeper.quorum", "172.16.168.130");
        configuration.set("hbase.zookeeper.property.clientPort", "2181");
        try {
            
            /**
             * Get Connected
             * 获取连接
             */
            connection = ConnectionFactory.createConnection(configuration);

            /**
             * Get HBase Administrator Object
             * 获取HBase管理员对象
             */
            admin = connection.getAdmin();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    /**
     * Close Resource
     * 关闭资源
     *
     * @param conf
     * @param admin
     */
    private static void close(Connection conf, Admin admin) {
        if (conf != null) {
            try {
                conf.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        if (admin != null) {
            try {
                admin.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
    
    /**
     * Determine if DataTable Exists
     * 判断数据表是否存在
     *
     * @param tableName
     */
    public static boolean isTableExist(String tableName) throws IOException {

        /**
         * Execution Method
         * 执行方法
         */
        boolean tableExists = admin.tableExists(TableName.valueOf(tableName));

        return tableExists;
    }
    
    /**
     * Adding Data
     * 添加数据
     *
     * @param tableName
     * @param rowKey
     * @param columnFamily
     * @param columnName
     * @param value
     * @throws IOException
     */
    public static void addData(String tableName, String rowKey, String columnFamily, String columnName, String value) throws IOException {

        /**
         * Instantiated Table Object
         * 实例化 表对象
         */
        Table table = connection.getTable(TableName.valueOf(tableName));

        /**
         * Verify that the data table exists before adding data
         * 添加数据前,验证数据表是否存在
         */
        if (!isTableExist(String.valueOf(TableName.valueOf(tableName)))) {
            System.out.println("Adding Data Failed, Reason: " + table + "DataTable Does Not Exist !");
            return;
        }

        /**
         * Instantiate Put Object
         * 实例化 Put对象
         *
         * Convert String type primary key ID to byte data
         * 将String类型主键ID转换字节数据
         */
        Put put = new Put(Bytes.toBytes(rowKey));

        /**
         * Add data (column family/column name/numeric) and convert the String type to a byte array
         * 添加数据 (列族/ 列名 / 数值)并将String类型转换为字节数组
         */
        put.addColumn(Bytes.toBytes(columnFamily), Bytes.toBytes(columnName), Bytes.toBytes(value));

        /**
         * Execution method
         * 执行方法
         */
        table.put(put);

        System.out.println(table.toString() + " Data added Successfully !");

        /**
         * Close resource
         * 关闭资源
         */
        table.close();
    }
    
    public static void main(String[] args) throws IOException {

        /**
         * Adding Data
         */
        addData("test001", "0003", "info", "name", "testUser003");

        /**
         * Close Resource
         * 关闭资源
         */
        close(connection, admin);
    }
}
```
- 执行返回结果
```
test001;hconnection-0x281e3708 Data added Successfully
```

### 6.6 修改数据
``` java
package com.geekparkhub.core.hbase.api.producehub;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.*;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.util.Bytes;

import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * HbaseHub
 * <p>
 */

public class HbaseHub {

    /**
     * Public Configuration information
     * 公共配置信息
     */
    private static Admin admin = null;
    private static Connection connection = null;
    private static Configuration configuration;

    static {

        /**
         * HBase ConfigurationFile
         * HBase 配置文件
         */
        configuration = HBaseConfiguration.create();
        configuration.set("hbase.zookeeper.quorum", "172.16.168.130");
        configuration.set("hbase.zookeeper.property.clientPort", "2181");
        try {

            /**
             * Get Connected
             * 获取连接
             */
            connection = ConnectionFactory.createConnection(configuration);

            /**
             * Get HBase Administrator Object
             * 获取HBase管理员对象
             */
            admin = connection.getAdmin();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Close Resource
     * 关闭资源
     *
     * @param conf
     * @param admin
     */
    private static void close(Connection conf, Admin admin) {
        if (conf != null) {
            try {
                conf.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        if (admin != null) {
            try {
                admin.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * Determine if DataTable Exists
     * 判断数据表是否存在
     *
     * @param tableName
     */
    public static boolean isTableExist(String tableName) throws IOException {

        /**
         * Execution Method
         * 执行方法
         */
        boolean tableExists = admin.tableExists(TableName.valueOf(tableName));

        return tableExists;
    }

    /**
     * Change Data
     * 修改数据
     *
     * @param tableName
     * @param rowKey
     * @param columnFamily
     * @param columnName
     * @param value
     */
    public static void changeData(String tableName, String rowKey, String columnFamily, String columnName, String value) throws IOException {

        /**
         * Instantiated Table Object
         * 实例化 表对象
         */
        Table table = connection.getTable(TableName.valueOf(tableName));

        /**
         * Verify that the data table exists before modifying the data
         * 修改数据前,验证数据表是否存在
         */
        if (!isTableExist(String.valueOf(TableName.valueOf(tableName)))) {
            System.out.println("Change Data Failed, Reason: " + table + "DataTable Does Not Exist !");
            return;
        }

        /**
         * Instantiate Put Object
         * 实例化 Put对象
         *
         * Convert String type primary key ID to byte data
         * 将String类型主键ID转换字节数据
         */
        Put put = new Put(Bytes.toBytes(rowKey));

        /**
         * Change data (column family/column name/numeric) and convert the String type to a byte array
         * 修改数据 (列族/ 列名 / 数值)并将String类型转换为字节数组
         */
        put.addColumn(Bytes.toBytes(columnFamily), Bytes.toBytes(columnName), Bytes.toBytes(value));

        /**
         * Execution method
         * 执行方法
         */
        table.put(put);

        System.out.println(table.toString() + " Data Change Successfully !");

        /**
         * Close resource
         * 关闭资源
         */
        table.close();
    }

    public static void main(String[] args) throws IOException {

        /**
         * Change Data
         */
        changeData("test001", "0003", "info", "name", "testUser004");

        /**
         * Close Resource
         * 关闭资源
         */
        close(connection, admin);
    }
}
```
- 执行返回结果
```
test001;hconnection-0x281e3708 Data Change Successfully!
```


### 6.7 查询数据
#### 6.7.1 全表扫描
``` java
package com.geekparkhub.core.hbase.api.producehub;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.*;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.util.Bytes;

import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * HbaseHub
 * <p>
 */

public class HbaseHub {

    /**
     * Public Configuration information
     * 公共配置信息
     */
    private static Admin admin = null;
    private static Connection connection = null;
    private static Configuration configuration;

    static {

        /**
         * HBase ConfigurationFile
         * HBase 配置文件
         */
        configuration = HBaseConfiguration.create();
        configuration.set("hbase.zookeeper.quorum", "172.16.168.130");
        configuration.set("hbase.zookeeper.property.clientPort", "2181");
        try {

            /**
             * Get Connected
             * 获取连接
             */
            connection = ConnectionFactory.createConnection(configuration);

            /**
             * Get HBase Administrator Object
             * 获取HBase管理员对象
             */
            admin = connection.getAdmin();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Close Resource
     * 关闭资源
     *
     * @param conf
     * @param admin
     */
    private static void close(Connection conf, Admin admin) {
        if (conf != null) {
            try {
                conf.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        if (admin != null) {
            try {
                admin.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * Determine if DataTable Exists
     * 判断数据表是否存在
     *
     * @param tableName
     */
    public static boolean isTableExist(String tableName) throws IOException {

        /**
         * Execution Method
         * 执行方法
         */
        boolean tableExists = admin.tableExists(TableName.valueOf(tableName));

        return tableExists;
    }

    /**
     * Full Table Scan - Query Data
     * 全表扫描 - 查询数据
     *
     * @param tableName
     */
    public static void scanTable(String tableName) throws IOException {

        /**
         * Instantiated Table Object
         * 实例化 表对象
         */
        Table table = connection.getTable(TableName.valueOf(tableName));

        /**
         * Verify that the data table exists before modifying the data
         * 查询数据前,验证数据表是否存在
         */
        if (!isTableExist(String.valueOf(TableName.valueOf(tableName)))) {
            System.out.println("Inquire Data Failed, Reason: " + table + "DataTable Does Not Exist !");
            return;
        }

        /**
         * Instantiation Scanner
         * 实例化 扫描器
         */
        Scan scan = new Scan();

        /**
         * Execution Method
         * 执行方法
         */
        ResultScanner results = table.getScanner(scan);

        /**
         * Traversing RowKey data
         * 遍历RowKey数据
         */
        for (Result result : results) {
            Cell[] cells = result.rawCells();
            /**
             * Traversing the Row Key collection data
             * 遍历RowKey集合数据
             */
            for (Cell cell : cells) {
                System.out.println("RowKey is = " + Bytes.toString(CellUtil.cloneRow(cell))
                        + " & " + "ColumnFamily is = " + Bytes.toString(CellUtil.cloneFamily(cell))
                        + " & " + "ColumnName is = " + Bytes.toString(CellUtil.cloneQualifier(cell))
                        + " & " + "Value is = " + Bytes.toString(CellUtil.cloneValue(cell))
                        + "\n" + ("===========================================================================")
                );
            }
        }

        /**
         * Logger INFO
         */
        System.out.println("FullTable Data Query Success !");

        /**
         * Close resource
         * 关闭资源
         */
        table.close();
    }

    public static void main(String[] args) throws IOException {

        /**
         * Full Table Scan - Query Data
         */
        scanTable("test");

        /**
         * Close Resource
         * 关闭资源
         */
        close(connection, admin);
    }
}
```
- 全表扫描 执行返回结果
```
RowKey is = 0001 & ColumnFamily is = info & ColumnName is = age & Value is = 60
===========================================================================
RowKey is = 0001 & ColumnFamily is = info & ColumnName is = name & Value is = testuser001
===========================================================================
RowKey is = 0002 & ColumnFamily is = info & ColumnName is = age & Value is = 70
===========================================================================
RowKey is = 0002 & ColumnFamily is = info & ColumnName is = name & Value is = testuser002
===========================================================================
FullTable Data Query Success !
```

#### 6.7.2 指定参数查询数据
``` java
package com.geekparkhub.core.hbase.api.producehub;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.*;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.util.Bytes;

import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * HbaseHub
 * <p>
 */

public class HbaseHub {

    /**
     * Public Configuration information
     * 公共配置信息
     */
    private static Admin admin = null;
    private static Connection connection = null;
    private static Configuration configuration;

    static {

        /**
         * HBase ConfigurationFile
         * HBase 配置文件
         */
        configuration = HBaseConfiguration.create();
        configuration.set("hbase.zookeeper.quorum", "172.16.168.130");
        configuration.set("hbase.zookeeper.property.clientPort", "2181");
        try {

            /**
             * Get Connected
             * 获取连接
             */
            connection = ConnectionFactory.createConnection(configuration);

            /**
             * Get HBase Administrator Object
             * 获取HBase管理员对象
             */
            admin = connection.getAdmin();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Close Resource
     * 关闭资源
     *
     * @param conf
     * @param admin
     */
    private static void close(Connection conf, Admin admin) {
        if (conf != null) {
            try {
                conf.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        if (admin != null) {
            try {
                admin.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * Determine if DataTable Exists
     * 判断数据表是否存在
     *
     * @param tableName
     */
    public static boolean isTableExist(String tableName) throws IOException {

        /**
         * Execution Method
         * 执行方法
         */
        boolean tableExists = admin.tableExists(TableName.valueOf(tableName));

        return tableExists;
    }

    /**
     * Specified Parameter - Query Data
     * 指定参数 - 查询数据
     *
     * @param tableName
     * @param rowKey
     * @param columnFamily
     * @param columnName
     * @throws IOException
     */
    public static void getData(String tableName, String rowKey, String columnFamily, String columnName) throws IOException {

        /**
         * Instantiated Table Object
         * 实例化 表对象
         */
        Table table = connection.getTable(TableName.valueOf(tableName));

        /**
         * Verify that the data table exists before modifying the data
         * 查询数据前,验证数据表是否存在
         */
        if (!isTableExist(String.valueOf(TableName.valueOf(tableName)))) {
            System.out.println("Inquire Data Failed, Reason: " + table + "DataTable Does Not Exist !");
            return;
        }

        /**
         * Instantiate the Get object
         * 实例化Get对象
         */
        Get get = new Get(Bytes.toBytes(rowKey));

        /**
         * Specify column family & column name
         * 指定列族&列名
         */
        get.addColumn(Bytes.toBytes(columnFamily), Bytes.toBytes(columnName));

        /**
         * Execution method
         * 执行方法
         */
        Result result = table.get(get);

        Cell[] cells = result.rawCells();

        /**
         * Traversing the Row Key collection data
         * 遍历RowKey集合数据
         */
        for (Cell cell : cells) {
            System.out.println("RowKey is = " + Bytes.toString(CellUtil.cloneRow(cell))
                    + " & " + "ColumnFamily is = " + Bytes.toString(CellUtil.cloneFamily(cell))
                    + " & " + "ColumnName is = " + Bytes.toString(CellUtil.cloneQualifier(cell))
                    + " & " + "Value is = " + Bytes.toString(CellUtil.cloneValue(cell))
                    + "\n" + ("===========================================================================")
            );
        }

        /**
         * Logger INFO
         */
        System.out.println("Specified Parameter Data Query Success !");

        /**
         * Close resource
         * 关闭资源
         */
        table.close();
    }

    public static void main(String[] args) throws IOException {

        /**
         * Specified Parameter - Query Data
         */
        getData("test", "0001", "info", "name");

        /**
         * Close Resource
         * 关闭资源
         */
        close(connection, admin);
    }
}
```
- 指定参数查询数据 执行返回结果
```
RowKey is = 0001 & ColumnFamily is = info & ColumnName is = name & Value is = testuser001
===========================================================================
Specified Parameter Data Query Success !
```

### 6.8 删除数据
``` java
package com.geekparkhub.core.hbase.api.producehub;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.*;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.util.Bytes;

import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * HbaseHub
 * <p>
 */

public class HbaseHub {

    /**
     * Public Configuration information
     * 公共配置信息
     */
    private static Admin admin = null;
    private static Connection connection = null;
    private static Configuration configuration;

    static {

        /**
         * HBase ConfigurationFile
         * HBase 配置文件
         */
        configuration = HBaseConfiguration.create();
        configuration.set("hbase.zookeeper.quorum", "172.16.168.130");
        configuration.set("hbase.zookeeper.property.clientPort", "2181");
        try {

            /**
             * Get Connected
             * 获取连接
             */
            connection = ConnectionFactory.createConnection(configuration);

            /**
             * Get HBase Administrator Object
             * 获取HBase管理员对象
             */
            admin = connection.getAdmin();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Close Resource
     * 关闭资源
     *
     * @param conf
     * @param admin
     */
    private static void close(Connection conf, Admin admin) {
        if (conf != null) {
            try {
                conf.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        if (admin != null) {
            try {
                admin.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * Determine if DataTable Exists
     * 判断数据表是否存在
     *
     * @param tableName
     */
    public static boolean isTableExist(String tableName) throws IOException {

        /**
         * Execution Method
         * 执行方法
         */
        boolean tableExists = admin.tableExists(TableName.valueOf(tableName));

        return tableExists;
    }

    /**
     * Delete Data
     * 删除数据
     *
     * @param tableName
     * @param rowKey
     * @param columnFamily
     * @param columnName
     * @throws IOException
     */
    public static void deleteData(String tableName, String rowKey, String columnFamily, String columnName) throws IOException {

        /**
         * Instantiated Table Object
         * 实例化 表对象
         */
        Table table = connection.getTable(TableName.valueOf(tableName));

        /**
         * Verify that the data table exists before modifying the data
         * 删除数据前,验证数据表是否存在
         */
        if (!isTableExist(String.valueOf(TableName.valueOf(tableName)))) {
            System.out.println("Delete Data Failed, Reason: " + table + "DataTable Does Not Exist !");
            return;
        }

        /**
         * Instantiate the delete object
         * 实例化 delete对象
         */
        Delete delete = new Delete(Bytes.toBytes(rowKey));

        /**
         * 删除指定数据
         */
        delete.addColumns(Bytes.toBytes(columnFamily), Bytes.toBytes(columnName));

        /**
         * Execution method
         * 执行方法
         */
        table.delete(delete);

        /**
         * Logger INFO
         */
        System.out.println("Data Deletion is Successful!");

        /**
         * Close resource
         * 关闭资源
         */
        table.close();
    }

    public static void main(String[] args) throws IOException {

        /**
         * Delete Data
         */
        deleteData("test001", "0003", "name", "testUser004");

        /**
         * Close Resource
         * 关闭资源
         */
        close(connection, admin);
    }
}
```
- 执行返回结果
```
Data Deletion is Successful!
```

### 6.9 MapReduce
- 使用MapReduce将数据从本地文件系统导入到HBase的表中,从HBase中读取原始数据后使用MapReduce数据分析.

#### 6.9.1 官方HBase-MapReduce
- 查看HBase的MapReduce任务执行
```
[root@systemhub511 hbase]# bin/hbase mapredcp
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/opt/module/hbase/lib/slf4j-log4j12-1.7.5.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/opt/module/hadoop/share/hadoop/common/lib/slf4j-log4j12-1.7.10.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
/opt/module/hbase/lib/netty-all-4.0.23.Final.jar:/opt/module/hbase/lib/hbase-client-1.3.1.jar:/opt/module/hbase/lib/metrics-core-2.2.0.jar:/opt/module/hbase/lib/zookeeper-3.4.10.jar:/opt/module/hbase/lib/hbase-prefix-tree-1.3.1.jar:/opt/module/hbase/lib/hbase-common-1.3.1.jar:/opt/module/hbase/lib/protobuf-java-2.5.0.jar:/opt/module/hbase/lib/guava-12.0.1.jar:/opt/module/hbase/lib/htrace-core-3.1.0-incubating.jar:/opt/module/hbase/lib/hbase-protocol-1.3.1.jar:/opt/module/hbase/lib/hbase-hadoop-compat-1.3.1.jar:/opt/module/hbase/lib/hbase-server-1.3.1.jar
[root@systemhub511 hbase]#
```
#### 6.9.2 执行环境变量导入
- 关闭所有Hadoop相关服务
- vim `/etc/profile`
```
## SET HBASE_HOME
export HBASE_HOME=/opt/module/hbase
```
```
[root@systemhub511 hadoop]# source /etc/profile
```
- vim `hadoop-env.sh` / 注意 : 在for语句后追加此配置参数.
```
export HADOOP_CLASSPATH=$HADOOP_CLASSPATH:/opt/module/hbase/lib/*
```
- 配置文件分发集群
- 逐一开启相关服务

#### 6.9.3 运行官方MapReduce任务
- `Demo1` : 统计test表中有多少行数据
```
[root@systemhub511 hbase]# /opt/module/hadoop/bin/yarn jar lib/hbase-server-1.3.1.jar rowcounter test
HBase Counters
                BYTES_IN_REMOTE_RESULTS=0
                BYTES_IN_RESULTS=74
                MILLIS_BETWEEN_NEXTS=549
                NOT_SERVING_REGION_EXCEPTION=0
                NUM_SCANNER_RESTARTS=0
                NUM_SCAN_RESULTS_STALE=0
                REGIONS_SCANNED=1
                REMOTE_RPC_CALLS=0
                REMOTE_RPC_RETRIES=0
                ROWS_FILTERED=0
                ROWS_SCANNED=2
                RPC_CALLS=3
                RPC_RETRIES=0
        org.apache.hadoop.hbase.mapreduce.RowCounter$RowCounterMapper$Counters
                ROWS=2
        File Input Format Counters 
                Bytes Read=0
        File Output Format Counters 
                Bytes Written=0
```

- `Demo2` : 使用MapReduce将本地数据导入到HBase
- 创建后缀为.tsv格式文件
```
[root@systemhub511 hbase]# touch test002.tsv
[root@systemhub511 hbase]# vim test002.tsv
```
```
1001    Test001 Red
1002    Test002 Yellow
1003    Test003 Yellow
```
- 将文件上传到HDFS
```
[root@systemhub511 hbase]# hadoop fs -put test002.tsv /core_flow/test/
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/opt/module/hadoop/share/hadoop/common/lib/slf4j-log4j12-1.7.10.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/opt/module/hbase/lib/slf4j-log4j12-1.7.5.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
[root@systemhub511 hbase]# 
```
- 创建HBase表
```
hbase(main):001:0> create 'test002','info'
0 row(s) in 3.1610 seconds

=> Hbase::Table - test002
hbase(main):002:0> 
```
- 执行MapReduce
```
[root@systemhub511 hbase]# /opt/module/hadoop/bin/yarn jar ./lib/hbase-server-1.3.1.jar importtsv -Dimporttsv.columns=HBASE_ROW_KEY,info:name,info:color test002 hdfs://systemhub511:9000/core_flow/test/test002.tsv
Map-Reduce Framework
                Map input records=3
                Map output records=3
                Input split bytes=116
                Spilled Records=0
                Failed Shuffles=0
                Merged Map outputs=0
                GC time elapsed (ms)=131
                CPU time spent (ms)=1690
                Physical memory (bytes) snapshot=108429312
                Virtual memory (bytes) snapshot=2071105536
                Total committed heap usage (bytes)=16318464

```
- 使用scan指令查看导入后结果
```
hbase(main):001:0> scan 'test002'
ROW                        COLUMN+CELL                                                                 
 1001                      column=info:color, timestamp=1556886127536, value=Red                       
 1001                      column=info:name, timestamp=1556886127536, value=Test001                    
 1002                      column=info:color, timestamp=1556886127536, value=Yellow                    
 1002                      column=info:name, timestamp=1556886127536, value=Test002                    
 1003                      column=info:color, timestamp=1556886127536, value=Yellow                    
 1003                      column=info:name, timestamp=1556886127536, value=Test003                    
3 row(s) in 0.5090 seconds
hbase(main):002:0> 
```

#### 6.9.4 自定义 HBase-MapReduce (1)
- 将test002表中一部分数据,通过MapReduce迁入到test002_mr表中.
- Create `TestMapper.class` / 用于读取test002表中数据.
``` java
package com.geekparkhub.core.hbase.api.mapreduce;

import org.apache.hadoop.hbase.Cell;
import org.apache.hadoop.hbase.CellUtil;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.client.Result;
import org.apache.hadoop.hbase.io.ImmutableBytesWritable;
import org.apache.hadoop.hbase.mapreduce.TableMapper;
import org.apache.hadoop.hbase.util.Bytes;

import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * TestMapper
 * <p>
 */

public class TestMapper extends TableMapper<ImmutableBytesWritable, Put> {

    @Override
    protected void map(ImmutableBytesWritable key, Result value, Context context) throws IOException, InterruptedException {

        /**
         * Instantiate Put object
         * 实例化 Put对象
         */
        Put put = new Put(key.get());

        /**
         * Traversing rowkey data
         * 遍历rowkey数据
         */
        Cell[] cells = value.rawCells();
        for (Cell cell : cells) {
            if ("name".equals(Bytes.toString(CellUtil.cloneQualifier(cell)))) {
                put.add(cell);
            }
        }
        context.write(key, put);
    }
}
```
- Create `TestReducer.class` / 用于将读取test002表数据写入到test002_mr表中.
``` java
package com.geekparkhub.core.hbase.api.mapreduce;

import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.io.ImmutableBytesWritable;
import org.apache.hadoop.hbase.mapreduce.TableReducer;
import org.apache.hadoop.io.NullWritable;

import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * TestReducer
 * <p>
 */

public class TestReducer extends TableReducer<ImmutableBytesWritable, Put, NullWritable> {

    @Override
    protected void reduce(ImmutableBytesWritable key, Iterable<Put> values, Context context) throws IOException, InterruptedException {
        for (Put value : values) {
            context.write(NullWritable.get(), value);
        }
    }
}
```
- Create `TestDriver.class` / 用于组装运行Job任务
``` java
package com.geekparkhub.core.hbase.api.mapreduce;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.client.Scan;
import org.apache.hadoop.hbase.io.ImmutableBytesWritable;
import org.apache.hadoop.hbase.mapreduce.TableMapReduceUtil;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * TestDriver
 * <p>
 */

public class TestDriver extends Configuration implements Tool {

    Configuration configuration = null;

    public int run(String[] args) throws Exception {

        /**
         * 实例化 Job对象
         */
        Job job = Job.getInstance(configuration);
        job.setJarByClass(TestDriver.class);

        TableMapReduceUtil.initTableMapperJob("test002", new Scan(), TestMapper.class, ImmutableBytesWritable.class, Put.class, job);

        TableMapReduceUtil.initTableReducerJob("test002_mr", TestReducer.class, job);

        boolean completion = job.waitForCompletion(true);

        return completion ? 0 : 1;
    }

    public void setConf(Configuration conf) {
        this.configuration = conf;
    }

    public Configuration getConf() {
        return configuration;
    }

    public static void main(String[] args) throws Exception {
        Configuration configuration = HBaseConfiguration.create();
        int run = ToolRunner.run(configuration, new TestDriver(), args);
    }
}
```
- 运行任务前,如果待数据导入表不存在,则需要提前创建
```
[root@systemhub511 hbase]# bin/hbase shell
hbase(main):001:0> create 'test002_mr','info'
0 row(s) in 2.8570 seconds
=> Hbase::Table - test002_mr
hbase(main):002:0> 
```
- 打包运行任务
```
[root@systemhub511 hbase]# /opt/module/hadoop/bin/yarn jar ./hbase_server-1.0.jar com.geekparkhub.core.hbase.api.mapreduce.TestDriver
 INFO mapreduce.Job: Counters: 62
        File System Counters
                FILE: Number of bytes read=195
                FILE: Number of bytes written=298305
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=109
                HDFS: Number of bytes written=0
                HDFS: Number of read operations=1
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=0
        Job Counters 
                Launched map tasks=1
                Launched reduce tasks=1
                Rack-local map tasks=1
                Total time spent by all maps in occupied slots (ms)=21676
                Total time spent by all reduces in occupied slots (ms)=10110
                Total time spent by all map tasks (ms)=21676
                Total time spent by all reduce tasks (ms)=10110
                Total vcore-milliseconds taken by all map tasks=21676
                Total vcore-milliseconds taken by all reduce tasks=10110
                Total megabyte-milliseconds taken by all map tasks=22196224
                Total megabyte-milliseconds taken by all reduce tasks=10352640
        Map-Reduce Framework
                Map input records=3
                Map output records=3
                Map output bytes=183
                Map output materialized bytes=195
                Input split bytes=109
                Combine input records=3
                Combine output records=3
                Reduce input groups=3
                Reduce shuffle bytes=195
                Reduce input records=3
                Reduce output records=3
                Spilled Records=6
                Shuffled Maps =1
                Failed Shuffles=0
                Merged Map outputs=1
                GC time elapsed (ms)=612
                CPU time spent (ms)=6990
                Physical memory (bytes) snapshot=333955072
                Virtual memory (bytes) snapshot=4147179520
                Total committed heap usage (bytes)=144588800
        HBase Counters
                BYTES_IN_REMOTE_RESULTS=0
                BYTES_IN_RESULTS=255
                MILLIS_BETWEEN_NEXTS=1667
                NOT_SERVING_REGION_EXCEPTION=0
                NUM_SCANNER_RESTARTS=0
                NUM_SCAN_RESULTS_STALE=0
                REGIONS_SCANNED=1
                REMOTE_RPC_CALLS=0
                REMOTE_RPC_RETRIES=0
                ROWS_FILTERED=0
                ROWS_SCANNED=3
                RPC_CALLS=3
                RPC_RETRIES=0
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters 
                Bytes Read=0
        File Output Format Counters 
                Bytes Written=0
[root@systemhub511 hbase]# 
```
- 查看执行结果
```
hbase(main):002:0> scan 'test002_mr'
ROW                        COLUMN+CELL                                                                 
 1001                      column=info:name, timestamp=1556886127536, value=Test001                    
 1002                      column=info:name, timestamp=1556886127536, value=Test002                    
 1003                      column=info:name, timestamp=1556886127536, value=Test003                    
3 row(s) in 0.0290 seconds
hbase(main):004:0> 
```

#### 6.9.5 自定义 HBase-MapReduce (2)
- 实现将HDFS中数据写入到HBase表中.

### 6.10 HBase集成Hive


## 7. HBase 优化


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