# 大数据生态系统 修仙之道 HBase Blog

@(2019-04-10)[ Docs Language:简体中文 & English|Programing Language:HBase|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)|![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg) | ![GitHub repo size in bytes](https://img.shields.io/github/repo-size/geekparkhub/geekparkhub.github.io.svg) | GeekDeveloper:[JEEP-711](https://github.com/jeep711)|Github:[github.com/geekparkhub](https://github.com/geekparkhub)|Gitee:[gitee.com/geekparkhub](https://gitee.com/geekparkhub) ]

##  🐘 HBase Technology 修仙之道 内炼金丹 🐘

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
-
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
## 3. HBase Shell
## 4. HBase 数据结构
## 5. HBase 原理
## 6. HBase API
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