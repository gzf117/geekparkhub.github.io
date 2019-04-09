# 大数据生态系统 修仙之道 Flume Blog

@(2019-03-25)[ Docs Language:简体中文 & English|Programing Language:Flume|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)|![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg) | ![GitHub repo size in bytes](https://img.shields.io/github/repo-size/geekparkhub/geekparkhub.github.io.svg) | GeekDeveloper:[JEEP-711](https://github.com/jeep711)|Github:[github.com/geekparkhub](https://github.com/geekparkhub)|Gitee:[gitee.com/geekparkhub](https://gitee.com/geekparkhub) ]

##  🐘 Flume Technology 修仙之道 炼神返虚 🐘

![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hive/hive.jpg)

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


## 1. Flume 概述
> Flume是Cloudera公司提供的一个`高可用`/`高可靠`/`分布式海量日志采集`/`聚合`/`传输`系统.
> Flume作为Hadoop平台日志收集的核心组件,提供了强大可扩展性的设计架构和

### 1.1 Flume 定义
> Flume基于流式架构,灵活简单.
> 
> Flume支持从多种数据源收集数据,对数据进行处理后,将数据写入到数据接收方.
> 
> Flume提供从`本地文件`/`实时日志`/`REST消息`/`Thrift`/`Avro`/`Syslog`/`Kafka`等数据源收集数据的能力.
> 
> Flume具有可靠性机制和许多故障转移和恢复机制强大和容错能力,它使用一个简单可扩展数据模型,允许在线分析应用程序.
> 
> Flume用于实时收集服务器(Apache/Ngnix等)数据框架,Flume很多时候与Storm以及Spark Streaming等流式处理框架结合使用.

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/start_001.jpg)
> Flume主要作用是实时读取服务器本地磁盘数据,将数据写入到HDFS.

### 1.2 Flume 组成架构

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/start_002.jpg)
> Flume 基础架构
> 
> Flume架构非常简单,只需要部署Agent代理一个角色,通过Agent获取外部日志数据再传输到目标存储HDFS中,上图中是使用单Agent架构直接采集数据集,主要用于采集集群内数据.

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/start_006.jpg)
> Flume 多Agent架构
> 
> Flume也支持多Agent架构,可以将多个Agent级联工作,Flume从最初的数据源收集数据,经过两个Agent传输,最终将数据存储到HDFS中,多Agent架构可以起到复制/分流等作用,主要用于将集群外数据导入到集群内.

#### 1.2.1 Agent
> Agent主要由三大模块组成：`Source`/ `Channel` / `Sink`, 一个Agent内可以有多个Channel & Sink , Agent是一个java进程.
> 
> Agent具有字节有效载荷和可选的一组字符串属性的数据流的单元.
> 
> Flume代理(Agent)是一个(JVM)程,它承载事件从外部源传递到下一个目标(跳)组件,是Flume数据传输的基本单元,以事件的形式将数据从源头送至目的地.

#### 1.2.2 Source
> Source用于采集数据,Source是产生数据流的地方,同时Source会将产生的数据流传输到Channel,这有点类似于Java IO部分的Channel.
> 
> Source分为驱动型和轮询行,可以对接多种数据源.
> 
> 驱动型Source工作模式是数据源主动发送数据给Flume,驱动Flume接收数据,如Exec Source / Avro Source / Thrift Source / HTTP Source.
> 
> 轮询型Source工作模式是Flume周期性主动从数据源获取数据,如Syslog Source / Spooling Directory Source / Jms Source / Kafka Source.
> 
> 开发者可以对Source进行自定义开发.
> 
> Source 类型表
| Source类型 | 	 说明   |
| :--------: | :--------:|
| Exec Source    |   执行某个命令或脚本,并将其执行结果的输出作为数据源. |
| Avro Source    |   提供一个基于Avro协议的Server,将其绑定到某个端口上,等待Avro协议客户端发送数据. |
| Thrift Source    |   提供一个基于Thrift协议的Server,将其绑定到某个端口上,等待Thrift协议客户端发送数据. |
| HTTP Source    |   支持HTTP的post发送数据. |
| Syslog Source    |   采集系统Syslog日志. |
| Spooling Directory Source    |   采集本地静态文件. |
| Jms Source    |   从消息队列获取数据. |
| Kafka Source    |   从Kafka获取数据. |

#### 1.2.3 Channel
> Channel位于Source & Sink之间,Channel作用是类似于队列,用于临时缓存Agent中间的Event.
> 
> 开发者可以对Channel自定义开发,不同的Channel类型提供的数据持久化水平是不一样的,缓存位置也不同,Channel可以将Event存放到内存/文系统/数据库中.
> 
> Channel 类型表
| Channel类型  |     说明 |
| :--------: | :--------:|
| Memory Channel  |   Event存放在内存中,提供高吞吐,但不提供可靠性,可能丢失数据. |
| File Channel    |   Event存放在文件中,对数据进行持久化,但配置比较繁琐,需要配置数据目录和Checkpoint目录,不同的FileChannel需要配置一个Checkpoint目录. |
| JDBC Channel    |   Event存放在Flume内置的Derby数据库中,并对Event进行持久化,提供高可靠型. |


#### 1.2.4 Sink
> Sink负责将Event传输到下一个条跳或最终目的存储,Event写入成功后,会从Channel中被移除,Sink必须作用于一个确切的Channel.
> 
> 开发者可以使用不同类型的Sink将数据传输到不同目标储存(HDFS/HBase/Kafka/Sorr/本地文件系统),同样开发者也可以对Sink进行自定义开发.
> 
> Sink 类型表
| Sink类型   |     说明 |
| :--------:| :--------:|
| HDFS     |   将数据写入到HDFS |
| Avro Sink    |   使用Avro协议将数据发送给下一个跳的Flume. |
| Thrift Sink    |   使用Thrift协议将数据发送给另下一个跳的Flume. |
| File Rool Sink    |   将数据保存在本地文件系统中. |
| HBase Sink    |   将数据写入到HBase中. |
| Kafka Sink    |   将数据写入到Kafka中. |
| MorphlineSolr Sink    |   将数据写入到Solr中. |


#### 1.2.5 Event
> Event是Flume数据传输的基本单元,Event代表着一个数据流的最小完整单元,来自外部数据源,流向最终目的存储.
> 
> Event由`Header(报头)`&`Body(主体)`组成,Event以事件的形式将数据从源头送至目的地.

### 1.3 Flume 拓扑结构
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/flume/start_005.jpg)

### 1.4 Flume Agent内部原理





## 10. 修仙之道 技术架构迭代 登峰造极之势
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