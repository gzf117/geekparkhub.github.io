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
> 无论是Kafka集群,还是Producer和Consumer都依赖于Zookeeper集群保存一些Meta信息来保证系统可用性.

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

## 3. Kafka 工作流分析

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