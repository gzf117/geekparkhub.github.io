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
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/azkaban/start_001.jpg)
- 在某个业务系统,每天系统产生20GB元数据业务,每天都要对其进行处理,处理步骤如下 : 
- 1.通过Hadoop先将原始数据上传至HDFS / 简称(HDFS操作).
- 2.使用MapReduce对原始数据进行ETL / 简称(MapReduce操作).
- 3.将清洗后的数据导入Hive数据表中 / 简称(Hive导入操作).
- 4.对Hive中多个数据表的数据进程Join处理,得到一张Hive明细数据表 / 简称(创建中间表).
- 5.通过对明细数据表的统计个分析,得到结果报表信息 / 简称(Hive查询操作).


### 1.2 Azkaban 应用场景
- 业务场景 : (2)任务依赖 / (1) 任务结果 / (3)任务依赖 / (2) 任务结果 / (4) 任务依赖 / (5) 任务结果 , 一般做法是先执行完 (1),(2),在一次执行(3),(4),(5).
- 整个执行过程都需要仍参与,并且时刻注意任务进度,但是很多任务都是在深夜执行,通过编写脚本设置Crontab执行,其实整个过程类似于一个有向无环图(DGA),每个子任务相当于大任务的一个节点,也就是需要一个工作流调度器,而Azkban就是解决上述问题的调度器.


### 1.3 Azkaban 简介
- Azkaban是由Linkedin公司推出的一个轻量级批量工作流任务调度器.
- 
- 主要用于在工作流内以一个特定顺序运行一组工作和流程,配置是通过简单的`<Key/Value>`键值对方式,通过配置中的`dependencies`关键字来设置关系依赖.
- 
- Azkaban使用Job配置文件建立任务之间依赖关系,并提供一个易于使用的Web图形化应用来维护和跟踪工作流.

### 1.4 Azkaban 特点
- 1.兼容任何版本Hadoop.
- 2.易于使用Web图形化界面
- 3.简单工作流上传
- 4.快捷设置任务之间关系
- 5.调度工作流
- 6.模块化 / 可插拔插件机制
- 7.认证 / 授权(权限工作)
- 8.能够结束并重新启动工作流
- 9.友好电子邮箱提醒


### 1.5 常见工作流调度系统
- 简单任务调度 : 可使用crontab实现.
- 负载任务调度 : 开发调度平台或使用现有开源调度系统,如Oozie / Azkaban等


### 1.6 Oozie与Azkaban特性对比
- 技术选型对比
| 特性      |     Oozie |   Azkaban   |
| :--------: | :--------:| :------: |
| 工作流描述语言    |   Xml |  text file with key/value pairs  |
| 是否要Web容器    |   Yes |  Yes  |
| 进度跟踪    |   Web Page |  Web Page  |
| Hadoop Job调度支持    |   Yes |  Yes  |
| 运行模式    |   daemon |  daemon  |
| 事件通知    |   No |  Yes  |
| 需要安装    |   Yes |  Yes  |
| 兼容Hadoop版本    |   0.20+ |  currently unknown  |
| 重试支持    |   work flow node evel |  Yes  |
| 运行任意指令    |   Yes |  Yes  |


### 1.7 Azkaban 架构
- Azkaban由三个关键组件组成
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/azkaban/start_002.jpg)
- 1.`AzkabanWebServer` : AzkabanWebServer是整个Azkaban工作流主要管理者,它负责用户的登录认证 / 负责Project管理 / 定时执行工作流 / 跟踪工作执行进度等一系列任务. 
- 2.`AzkabanExecutorServer` : 负责具体工作流提交 / 执行 / 通过MySQL数据库来协调任务执行.
- 3.关系型数据库(MySQL) : 存储大部分执行流状态 , AzkabanWebServer / AzkabanExecutorServer都需要访问数据库.


## 2. Azkaban 部署
### 2.1 Azkaban Official Download
- Azkaban`官方文档` : [azkaban.readthedocs.io/en/latest/](https://azkaban.readthedocs.io/en/latest/)
- Azkaban`官方下载` : [azkaban.github.io/downloads.html](https://azkaban.github.io/downloads.html)
- Azkaban安装包列表详情 | 选择MySQL作为Azkaban数据库,以方便Azkaban设置并增强可靠性.
```
azkaban-executor-server-2.5.0.tar.gz
azkaban-sql-script-2.5.0.tar.gz
azkaban-web-server-2.5.0.tar
mysql-libs.zip
```

### 2.2 部署
- 1.在 /opt/module/目录下创建azkaban目录
```
[root@systemhub711 module]# mkdir azkaban
```
- 2.分别将三个安装包解压到指定目录
```
[root@systemhub711 software]# tar -zxvf azkaban-executor-server-2.5.0.tar.gz -C /opt/module/azkaban/

[root@systemhub711 software]# tar -zxvf azkaban-web-server-2.5.0.tar.gz -C /opt/module/azkaban/

[root@systemhub711 software]# tar -zxvf azkaban-sql-script-2.5.0.tar.gz -C /opt/module/azkaban/
```
- 3.分别对包名重命名
```
[root@systemhub711 module]# cd azkaban/
[root@systemhub711 azkaban]# mv azkaban-2.5.0 azkaban
[root@systemhub711 azkaban]# mv azkaban-executor-2.5.0 azkaban-executor
[root@systemhub711 azkaban]# mv azkaban-web-2.5.0 azkaban-web
```
- 4.azkaban导入脚本
- 进入MySQL客户端,创建azkaban数据库,并将脚本导入到azkaban数据库中.
- `source`关键字用于批量处理`.sql`文件中sql语句.
``` sql
[root@systemhub711 software]# mysql -uroot -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.

mysql> create database azkaban;
Query OK, 1 row affected (0.01 sec)

mysql> use azkaban;
Database changed
mysql> source /opt/module/azkaban/azkaban/create-all-sql-2.5.0.sql
Query OK, 0 rows affected (0.08 sec)
```
- 5.查看导入数据表结果
```
mysql> show tables;
+------------------------+
| Tables_in_azkaban      |
+------------------------+
| active_executing_flows |
| active_sla             |
| execution_flows        |
| execution_jobs         |
| execution_logs         |
| project_events         |
| project_files          |
| project_flows          |
| project_permissions    |
| project_properties     |
| project_versions       |
| projects               |
| properties             |
| schedules              |
| triggers               |
+------------------------+
15 rows in set (0.00 sec)
mysql> 
```

### 2.3 生成密钥库
#### 2.3.1 密钥参数说明
- `Keytool`是java数据证书管理工具,开发者能够管理自身的公私密钥对以及相关证书.
- `-keystore` 指定密钥库名称以及位置(产生各类信息将不在.keystore文件中).
- `-genkey` 在开发者目录中创建一个以`.keystore`默认文件.
- `-alias` 对生成的.keystore进行指认识别,如果没有默认则是mykey
- `-keyalg` 指定密钥算法 RSA / DSA , 默认是DSA

- 1.生成keystore密码以及相关信息密钥库
```
[root@systemhub711 azkaban]# keytool -keystore keystore -alias core_flow -genkey -keyalg RSA
Enter keystore password:  
Re-enter new password: 
What is your first and last name?
  [Unknown]:  
What is the name of your organizational unit?
  [Unknown]:  
What is the name of your organization?
  [Unknown]:  
What is the name of your City or Locality?
  [Unknown]:  
What is the name of your State or Province?
  [Unknown]:  
What is the two-letter country code for this unit?
  [Unknown]:  
Is CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown correct?
  [no]:  y

Enter key password for <core_flow>
        (RETURN if same as keystore password):  
Re-enter new password: 
[root@systemhub711 azkaban]# 
```
- 2.将keystore文件移动至azkaban-web目录下
```
[root@systemhub711 azkaban]# mv keystore /opt/module/azkaban/azkaban-web
```

### 2.4 时间同步
- 事先配置好集群节点上时区.
- 1.如在/usr/share/zoneinfo/目录下不存在时区配置文件Asia/Shanghai,就需要使用`tzselect`生成。
- 如果此目录存在可跳过此步骤.
```
[root@systemhub711 azkaban-web]# ll /usr/share/zoneinfo/Asia/Shanghai
-rw-r--r--. 3 root root 405 Oct 16  2013 /usr/share/zoneinfo/Asia/Shanghai
[root@systemhub711 azkaban-web]# 
```

### 2.5 配置文件
#### 2.5.1 WebServer 配置
- 1.进入 azkaban-web/conf/目录下
```
[root@systemhub711 azkaban]# cd azkaban-web/conf/
[root@systemhub711 conf]# ll
total 8
-rw-r--r-- 1 root root 1022 Apr 22  2014 azkaban.properties
-rw-r--r-- 1 root root  266 Apr 22  2014 azkaban-users.xml
[root@systemhub711 conf]# vim azkaban.properties
```
- 2.配置`azkaban.properties`文件 | vim `azkaban.properties`
```
#Azkaban Personalization Settings
# Web 显示名称
azkaban.name=System Flow
# Web 描述
azkaban.label=Azkaban Core Flow
azkaban.color=#FF3601
azkaban.default.servlet.path=/index
# 默认WebServer存放web文件目录
web.resource.dir=/opt/module/azkaban/azkaban-web/web/
# 默认时区,默认值为美国,已配置为亚洲/上海
default.timezone.id=Asia/Shanghai

#Azkaban UserManager class
user.manager.class=azkaban.user.XmlUserManager
# 用户权限管理默认类(绝对路径)
user.manager.xml.file=/opt/module/azkaban/azkaban-web/conf/azkaban-users.xml

#Loader for projects
executor.global.properties=/opt/module/azkaban/azkaban-executor/conf/global.properties
azkaban.project.dir=projects

database.type=mysql
mysql.port=3306
mysql.host=systemhub711
mysql.database=azkaban
mysql.user=root
mysql.password=ax0pix
mysql.numconnections=100

# Velocity dev mode
velocity.dev.mode=false

# Azkaban Jetty server properties.
jetty.maxThreads=25
jetty.ssl.port=8443
jetty.port=8081
# SSL 文件名 / 绝对路径
jetty.keystore=/opt/module/azkaban/azkaban-web/keystore
# SSL 文件密码
jetty.password=ax0pix
# SSL 与主密码相同
jetty.keypassword=ax0pix
# SSL 文件名 / 绝对路径
jetty.truststore=/opt/module/azkaban/azkaban-web/keystore
# SSL 文件密码
jetty.trustpassword=ax0pix

# Azkaban Executor settings
executor.port=12321

# mail settings
mail.sender=
mail.host=
job.failure.email=
job.success.email=

lockdown.create.projects=false

cache.directory=cache
```
- 3.vim `azkaban-users.xml`
```
[root@systemhub711 conf]# vim azkaban-users.xml
```
- 添加admin用户
``` xml
<azkaban-users>
        <user username="azkaban" password="azkaban" roles="admin" groups="azkaban" />
        <user username="metrics" password="metrics" roles="metrics"/>
        <user username="admin" password="admin" roles="admin,metrics"/>
        <role name="admin" permissions="ADMIN" />
        <role name="metrics" permissions="METRICS"/>
</azkaban-users>
```


#### 2.5.2 ExecutorServer 配置
- 1.进入/opt/module/azkaban/azkaban-executor/conf目录下
- vim `azkaban.properties` | 配置 azkaban.properties文件
```
#Azkaban
default.timezone.id=Asia/Shanghai

# Azkaban JobTypes Plugins
azkaban.jobtype.plugin.dir=plugins/jobtypes

#Loader for projects
executor.global.properties=/opt/module/azkaban/azkaban-executor/conf/global.properties
azkaban.project.dir=projects

database.type=mysql
mysql.port=3306
mysql.host=systemhub711
mysql.database=azkaban
mysql.user=root
mysql.password=ax0pix
mysql.numconnections=100

# Azkaban Executor settings
executor.maxThreads=50
executor.port=12321
executor.flow.threads=30
```

### 2.6 启动 Executor Server
- 0.`先执行ExecutorServer,再执行WebServer,避免WebServer找不到执行器导致启动失败`.
- 1.在azkaban-executor/目录下执行启动命令.
```
[root@systemhub711 azkaban-executor]# pwd
/opt/module/azkaban/azkaban-executor
[root@systemhub711 azkaban-executor]# bin/azkaban-executor-start.sh
```

### 2.7 启动 Web Server
- 1.在azkaban-web/目录下执行启动命令.
```
[root@systemhub711 azkaban-web]# pwd
/opt/module/azkaban/azkaban-web
[root@systemhub711 azkaban-web]# bin/azkaban-web-start.sh
```
- 2.jps查看进程
```
[root@systemhub711 ~]# jps
29392 AzkabanWebServer
28037 AzkabanExecutorServer
30040 Jps
[root@systemhub711 ~]# 
```
- 3.启动完成,在浏览器输入`https://hostname:8443`地址,即登录可访问服务.
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/azkaban/start_003.gif)


## 3. Azkaban 任务调度
### 3.1 单一Job 任务调度
- 使用Azkaban调度单一Job程序.
- 1.在此目录创建core_jobs文件夹.
```
[root@systemhub711 ~]# cd /opt/module/azkaban/
[root@systemhub711 azkaban]# mkdir core_jobs
```
- 2.进入core_jobs目录,创建以`.job`为结尾的工作流文件.
```
[root@systemhub711 core_jobs]# vim single_workflow.job
```
```
# first job
type=command
command=echo 'This is a Single Jobs'
```
- 3.将single_workflow.job压缩为以后缀名`.zip`压缩包.
```
[root@systemhub711 core_jobs]# zip single_workflow.zip single_workflow.job
adding: single_workflow.job (deflated 8%)
[root@systemhub711 core_jobs]# ll
total 8
-rw-r--r-- 1 root root  61 May 10 20:54 single_workflow.job
-rw-r--r-- 1 root root 244 May 10 20:57 single_workflow.zip
[root@systemhub711 core_jobs]# 
```
- 4.将压缩包下载到系统桌面,并创建工作流

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/azkaban/start_004.jpg)

- 5.通过Azkaban Web管理平台创建project
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/azkaban/start_005.jpg)

- 6.上传压缩包,并启动执行Job工作流任务
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/azkaban/start_006.gif)

- 7.查看工作流日志信息
```
Job Logs
CST single_workflow INFO - Starting job single_workflow at 1557494992670
CST single_workflow INFO - Building command job executor. 
CST single_workflow INFO - 1 commands to execute.
CST single_workflow INFO - Command: echo 'This is a Single Jobs'
CST single_workflow INFO - Environment variables: {JOB_OUTPUT_PROP_FILE=/opt/module/azkaban/azkaban-executor/executions/1/single_workflow_output_6225901896375074204_tmp, JOB_PROP_FILE=/opt/module/azkaban/azkaban-executor/executions/1/single_workflow_props_9124304639650346490_tmp, JOB_NAME=single_workflow}
CST single_workflow INFO - Working directory: /opt/module/azkaban/azkaban-executor/executions/1
CST single_workflow INFO - This is a Single Jobs
CST single_workflow INFO - Process completed successfully in 0 seconds.
CST single_workflow INFO - Finishing job single_workflow at 1557494992835 with status SUCCEEDED
```

### 3.2 多Job工作流 任务调度
- 使用`dependencies`关键字来调度多Job程序.
- 多任务流程 | (1)文件上传至HDFS `->` (2)创建外部表 `->` (3)查询数据表
- 0.在HDFS创建multitasking目录
```
[root@systemhub711 core_jobs]# hadoop fs -mkdir -p /core_flow/azkaban/multitasking
[root@systemhub711 core_jobs]# 
```
- 1.将本地文件上传至HDFS | vim `multitasking_hdfs_workflow.job`
```
# Multitasking HSFD WorkFlow
type=command
command=/opt/module/hadoop/bin/hadoop fs -put /opt/module/datas/test.txt /core_flow/azkaban/multitasking
```
- 2.创建job描述文件与hive脚本.
- vim `multitasking_hive_workflow.sql`
``` sql
use default;
create external table multitasking_hive_workflow(
    id int ,
    name string)
row format delimited fields terminated by '\t'
location '/core_flow/azkaban/multitasking';
```
- vim `multitasking_hive_workflow.job`
```
# Multitasking Hive WorkFlow
type=command
command=/opt/module/hive/bin/hive -f /opt/module/azkaban/core_jobs/multitasking_hive_workflow.sql
dependencies=multitasking_hdfs_workflow
```
- 3.创建数据表 | vim `multitasking_select_workflow.job`
```
# Multitasking Select WorkFlow
type=command
command=/opt/module/hive/bin/hive -e 'select * from multitasking_hive_workflow;'
dependencies=multitasking_hive_workflow
```
- 4.将三个job资源文件压缩为以后缀名`.zip`压缩包.
- 文件资源详情 : `multitasking_hdfs_workflow.job` | `multitasking_hive_workflow.job` | `multitasking_select_workflow.job`
```
[root@systemhub711 core_jobs]# zip multitasking_workflow.zip multitasking_hdfs_workflow.job multitasking_hive_workflow.job multitasking_select_workflow.job
adding: multitasking_hdfs_workflow.job (deflated 28%)
adding: multitasking_hive_workflow.job (deflated 35%)
adding: multitasking_select_workflow.job (deflated 33%)
[root@systemhub711 core_jobs]#
```
- 5.通过Azkaban Web管理平台创建project并上传压缩包,启动执行Job应用.
- 此步骤与单Job实例一致,Gif演示图已省略 | 如不明确步骤,请回看`单Job实例`Gif演示图

- 6.查看运行结果

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/azkaban/start_007.jpg)

```
CST multitasking_select_workflow INFO - multitasking_hive_workflow.id	multitasking_hive_workflow.name
CST multitasking_select_workflow INFO - 1	TestUser001
CST multitasking_select_workflow INFO - 2	TestUser002
CST multitasking_select_workflow INFO - 3	TestUser003
CST multitasking_select_workflow INFO - 4	TestUser004
```



### 3.3 Java 任务调度
- 使用Azkaban调度java程序.
- 1.Create AzkabanWorkFlow.class
```java
package com.geekparkhub.core.azkaban.api.producehub;

import java.io.FileOutputStream;
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
 * AzkabanWorkFlow
 * <p>
 */

public class AzkabanWorkFlow {

    /**
     * Core Method
     *
     * @throws IOException
     */
    public void rum() throws IOException {
        FileOutputStream fileOutputStream = new FileOutputStream("/opt/module/azkaban/output.txt");
        fileOutputStream.write("This is a Java Task".getBytes());
        fileOutputStream.close();
    }

    public static void main(String[] args) throws IOException {
        AzkabanWorkFlow workFlow = new AzkabanWorkFlow();
        workFlow.rum();
    }
}
```

- 2.使用Maven将程序打包成jar包,上传至`/opt/module/azkaban/`目录下
```
[root@systemhub711 module]# cd azkaban/
[root@systemhub711 azkaban]# ll
total 40
drwxr-xr-x  2 root root  4096 May 10 16:50 azkaban
drwxr-xr-x 10 root root  4096 May 10 19:43 azkaban-executor
drwxr-xr-x  9 root root  4096 May 10 19:43 azkaban-web
-rw-r--r--  1 root root 21518 May 10 22:02 AzkabanWorkFlow.jar
drwxr-xr-x  2 root root  4096 May 10 22:10 core_jobs
[root@systemhub711 azkaban]# 
```
- 3.进入core_jobs目录,创建以`.job`为结尾的工作流文件.
```
[root@systemhub711 azkaban]# cd core_jobs/
[root@systemhub711 core_jobs]# vim java_workflow.job
```
```
# java work flow
type=javaprocess
java.class=com.geekparkhub.core.azkaban.api.producehub.AzkabanWorkFlow
classpath=/opt/module/azkaban/AzkabanWorkFlow.jar
```
- 4.将java_workflow.job压缩为以后缀名`.zip`压缩包.
```
[root@systemhub711 core_jobs]# zip java_workflow.zip java_workflow.job
adding: java_workflow.job (deflated 25%)
[root@systemhub711 core_jobs]# 
```
- 5.通过Azkaban Web管理平台创建project并上传压缩包,启动执行Job应用.
- 此步骤与单Job实例一致,Gif演示图已省略 | 如不明确步骤,请回看`单Job实例`Gif演示图

- 6.查看运行结果 | 查看`output.txt`文件
```
[root@systemhub711 azkaban]# ll
total 44
drwxr-xr-x  2 root root  4096 May 10 16:50 azkaban
drwxr-xr-x 10 root root  4096 May 10 19:43 azkaban-executor
drwxr-xr-x  9 root root  4096 May 10 19:43 azkaban-web
-rw-r--r--  1 root root 21518 May 10 22:02 AzkabanWorkFlow.jar
drwxr-xr-x  2 root root  4096 May 10 22:23 core_jobs
-rw-r--r--  1 root root    19 May 10 22:29 output.txt
[root@systemhub711 azkaban]# cat output.txt
This is a Java Task
[root@systemhub711 azkaban]# 
```


### 3.4 HDFS 任务调度
- 使用Azkaban调度HDFS程序.
- 1.进入core_jobs目录,创建以`.job`为结尾的工作流文件.
```
[root@systemhub711 core_jobs]# vim hdfs_workflow.job
```
```
# hdfs work flow
type=command
command=/opt/module/hadoop/bin/hadoop fs -mkdir /core_flow/azkaban
```
- 2.将hdfs_workflow.job压缩为以后缀名`.zip`压缩包.
```
[root@systemhub711 core_jobs]# zip hdfs_workflow.zip hdfs_workflow.job
adding: hdfs_workflow.job (deflated 14%)
[root@systemhub711 core_jobs]#
```

- 3.通过Azkaban Web管理平台创建project并上传压缩包,启动执行Job应用.
- 此步骤与单Job实例一致,Gif演示图已省略 | 如不明确步骤,请回看`单Job实例`Gif演示图

- 4.查看运行结果
```
[root@systemhub711 azkaban]# hadoop fs -ls /core_flow/
drwxr-xr-x   - root supergroup /core_flow/azkaban
drwxr-xr-x   - root supergroup /core_flow/develop
drwxr-xr-x   - root supergroup /core_flow/test
[root@systemhub711 azkaban]#
```

### 3.5 MapReduce 任务调度
- 使用Azkaban调度MapReduce程序.
- 1.进入core_jobs目录,创建以`.job`为结尾的工作流文件.
```
[root@systemhub711 core_jobs]# vim mapreduce_workflow.job
```
```
# mapreduce work flow
type=command
command=/opt/module/hadoop/bin/hadoop jar /opt/module/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.2.jar wordcount /user/geekparkhub/input /core_flow/azkaban/output
```
- 2.将mapreduce_workflow.job压缩为以后缀名`.zip`压缩包.
```
[root@systemhub711 core_jobs]# zip mapreduce_workflow.zip mapreduce_workflow.job
adding: mapreduce_workflow.job (deflated 34%)
[root@systemhub711 core_jobs]# 
```
- 3.通过Azkaban Web管理平台创建project并上传压缩包,启动执行Job应用.
- 此步骤与单Job实例一致,Gif演示图已省略 | 如不明确步骤,请回看`单Job实例`Gif演示图

- 4.查看运行结果
```
[root@systemhub711 core_jobs]# hadoop fs -cat /core_flow/azkaban/output/*
geek    2
geekparkhub     1
hackerparkhub   5
hadoop  3
helloworld      2
test    1
[root@systemhub711 core_jobs]# 
```

### 3.6 Hive脚本 任务调度
- 使用Azkaban调度Hive程序. | 预先启动Hive服务
- 1.创建job描述文件与hive脚本.
- Hive脚本 | vim `hive_workflow.sql`
``` sql
use default;

create table hive_workflow(
    id int , 
    name string 
  )row format delimited fields terminated   
by
  "\t";

load data local inpath "/opt/module/datas/test.txt"   
into
  table hive_workflow;

insert overwrite
    directory '/core_flow/azkaban/hive_workflow' row format delimited fields terminated       
  by
    '\t' select
      *           
    from
      hive_workflow;
```
- Job描述文件 | vim `hive_workflow.job`
```
# hive work flow
type=command
command=/opt/module/hive/bin/hive -f /opt/module/azkaban/core_jobs/hive_workflow.sql
```

- 2.将hive_workflow.job压缩为以后缀名`.zip`压缩包.
```
[root@systemhub711 core_jobs]# zip hive_workflow.zip hive_workflow.job
adding: hive_workflow.job (deflated 22%)
[root@systemhub711 core_jobs]# 
```

- 3.通过Azkaban Web管理平台创建project并上传压缩包,启动执行Job应用.
- 此步骤与单Job实例一致,Gif演示图已省略 | 如不明确步骤,请回看`单Job实例`Gif演示图

- 4.查看运行结果
```
[root@systemhub711 core_jobs]# hadoop fs -cat /core_flow/azkaban/hive_workflow/*
1       TestUser001
2       TestUser002
3       TestUser003
4       TestUser004
[root@systemhub711 core_jobs]# 
```

## 4. 修仙之道 技术架构迭代 登峰造极之势
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