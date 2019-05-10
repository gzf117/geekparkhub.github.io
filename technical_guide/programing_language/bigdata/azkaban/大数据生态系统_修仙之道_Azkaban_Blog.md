# 大数据生态系统 修仙之道 Azkaban Blog

@(2019-04-22)[ Docs Language:简体中文 & English|Programing Language:Azkaban|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)|![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg) | ![GitHub repo size in bytes](https://img.shields.io/github/repo-size/geekparkhub/geekparkhub.github.io.svg) | GeekDeveloper:[JEEP-711](https://github.com/jeep711)|Github:[github.com/geekparkhub](https://github.com/geekparkhub)|Gitee:[gitee.com/geekparkhub](https://gitee.com/geekparkhub) ]

##  🐘 Azkaban Technology 修仙之道 动静兼修 🐘

![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/azkaban/azkaban.jpg)

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


## 1. Azkaban 概述
### 1.1 工作流调度系统
- 一个完成数据分析系统通常都是由大量任务单元组成 : (Shell / Java / MapReduce / Hive Sell等).
- 各个任务单元之间存在时间先后以及前后依赖关系.
- 为了更好的组织这样复杂执行计划,需要一个工作流调度系统来调度执行.


- 在某个业务系统,每天系统产生20GB元数据业务,每天都要对其进行处理,处理步骤如下 : 
- 1.通过Hadoop先将原始数据上传至HDFS / 简称(HDFS操作).
- 2.使用MapReduce对原始数据进行ETL / 简称(MapReduce操作).
- 3.将清洗后的数据导入Hive数据表中 / 简称(Hive导入操作).
- 4.对Hive中多个数据表的数据进程Join处理,得到一张Hive明细数据表 / 简称(创建中间表).
- 5.通过对明细数据表的统计个分析,得到结果报表信息 / 简称(Hive查询操作).




### 1.2 Azkaban 应用场景
### 1.3 什么是Azkaban
### 1.4 Azkaban 特点
### 1.5 常见工作流调度系统
### 1.6 Oozie与Azkaban特性对比
### 1.7 Azkaban 架构



## 2. Azkaban 部署
### 2.1 Azkaban Official Download
- `官方文档` : [azkaban.readthedocs.io/en/latest/](https://azkaban.readthedocs.io/en/latest/)
- `官方下载` : [azkaban.github.io/downloads.html](https://azkaban.github.io/downloads.html)

### 2.2 部署
### 2.3 生成密钥库
### 2.4 时间同步
### 2.5 配置文件
### 2.6 启动 Executor Server
### 2.7 启动 Web Server

## 3. Azkaban 应用实战
### 3.1 单一Job
### 3.2 多Job工作流
### 3.3 Java任务操作
### 3.4 HDFS任务操作
### 3.5 MapReduce任务操作
### 3.6 Hive脚本任务