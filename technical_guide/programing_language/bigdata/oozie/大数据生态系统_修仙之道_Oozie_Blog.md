# 大数据生态系统 修仙之道 Oozie Blog

@(2019-04-23)[ Docs Language:简体中文 & English|Programing Language:Oozie|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)|![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg) | ![GitHub repo size in bytes](https://img.shields.io/github/repo-size/geekparkhub/geekparkhub.github.io.svg) | GeekDeveloper:[JEEP-711](https://github.com/jeep711)|Github:[github.com/geekparkhub](https://github.com/geekparkhub)|Gitee:[gitee.com/geekparkhub](https://gitee.com/geekparkhub) ]

##  🐘 Oozie Technology 修仙之道 内炼金丹 🐘

![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/oozie/oozie.jpg)

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


## 1. Oozie 概述
- Oozie英文翻译为 : 驯象人,一个基于工作流引擎开源框架,由Cloudera公司贡献给Apache,提供对Hadoop / MapReduce / Pig Jobs任务调度与协调,
- Oozie需要部署到Java Servlet容器中运行,主要用于定时调度任务,多任务可以按照执行的逻辑顺序调度.

## 2. Oozie 功能模块
### 2.1 模块
#### 2.2.1 Workflow
- 顺序执行流程节点,支持fork(分支多节点) , join(合并多个节点为一个).

#### 2.2.2 Coordinator
- (定时器)定时触发workflow

#### 2.2.3 Bundle Job
- 绑定多个Coordinator


### 2.2 节点
#### 2.2.1 控制流节点 (Control Flow Nodes)
- 控制流节点一般是定义在工作流开始或者结束位置,比如start,end,kill等,以及提供工作流执行路径机制,如decision,fork,join等.

#### 2.2.2 动作节点 (Action Nodes)
- 负责执行具体动作节点,比如 : 拷贝文件,执行某个Shell脚本等.

## 3. Oozie 部署
### 3.1 Hadoop (CDH Version) 部署
- Hadoop CDH 官方下载 : [archive.cloudera.com/cdh5/cdh/5/](http://archive.cloudera.com/cdh5/cdh/5/)
- Hadoop CDH 官方文档 :  [archive.cloudera.com/hadoop-2.5.0-cdh5.3.6/](http://archive.cloudera.com/cdh5/cdh/5/hadoop-2.5.0-cdh5.3.6/)

#### 3.1.1 Hadoop 配置
##### 3.1.1.1 创建`cdh_flow`目录,存放CDH版本资源
```
[root@systemhub511 module]# mkdir cdh_flow
```
##### 3.1.1.2 解压Hadoop资源包
```
[root@systemhub511 software]# tar -zxvf hadoop-2.5.0-cdh5.3.6.tar.gz -C /opt/module/cdh_flow/
```
##### 3.1.1.3 重命名资源包名称
```
[root@systemhub511 cdh_flow]# mv hadoop-2.5.0-cdh5.3.6 hadoop-cdh
```

##### 3.1.1.4 vim `hadoop-env.sh`
```
[root@systemhub511 hadoop]# pwd
/opt/module/cdh_flow/hadoop-cdh/etc/hadoop
[root@systemhub511 ~]# cd /opt/module/cdh_flow/hadoop-cdh/etc/hadoop
[root@systemhub511 hadoop]# echo $JAVA_HOME
/opt/module/jdk1.8.0_162
[root@systemhub511 hadoop]# vim hadoop-env.sh
```
```
# The java implementation to use.
export JAVA_HOME=/opt/module/jdk1.8.0_162
```
##### 3.1.1.5 vim `mapred-env.sh`
```
export JAVA_HOME=/opt/module/jdk1.8.0_162
```

##### 3.1.1.6 vim `yarn-env.sh`
```
export JAVA_HOME=/opt/module/jdk1.8.0_162
```
##### 3.1.1.7 vim `core-site.xml`
``` xml
<configuration>

<!-- 指定HDFS中的NameNode地址 -->
<property>
  <name>fs.defaultFS</name>
    <value>hdfs://systemhub511:8020</value>
</property>

<!-- 指定Hadoop运行时产生文件的存储目录 -->
<property>
  <name>hadoop.tmp.dir</name>
  <value>/opt/module/cdh_flow/hadoop-cdh/data/tmp</value>
</property>

<!--Oozie Server Hostname -->
<property>
  <name>hadoop.proxyuser.root.hosts</name>
  <value>*</value>
</property>

<!--允许被Oozie代理用户组-->
<property>
  <name>hadoop.proxyuser.root.groups</name>
  <value>*</value>
</property>

</configuration>
```

##### 3.1.1.8 vim `hdfs-site.xml`
```
<configuration>

<!-- 指定Hadoop辅助名称节点主机配置 -->
<property>
  <name>dfs.namenode.secondary.http-address</name>
  <value>systemhub711:50090</value>
</property>

</configuration>
```

##### 3.1.1.9 mv `mapred-site.xml.template` & vim `mapred-site.xml`
```
[root@systemhub511 hadoop]# mv mapred-site.xml.template mapred-site.xml
[root@systemhub511 hadoop]# vim mapred-site.xml
```
```
<configuration>

<!-- 指定MR运行在Yarn上 -->
<property>
  <name>mapreduce.framework.name</name>
  <value>yarn</value>
</property>

<!-- 历史服务器地址 -->
<property>
  <name>mapreduce.jobhistory.address</name>
  <value>systemhub511:10020</value>
</property>

<!-- 历史服务器WEB地址 -->
<property>
  <name>mapreduce.jobhistory.webapp.address</name>
  <value>systemhub511:19888</value>
</property>

</configuration>
```


##### 3.1.1.10 vim `yarn-site.xml`
```
<configuration>

<!-- Site specific YARN configuration properties -->
<!-- Reducer获取数据方式 -->
<property>
  <name>yarn.nodemanager.aux-services</name>
  <value>mapreduce_shuffle</value>
</property>

<!-- 指定Yarn的ResourceManager地址-->
<property>
  <name>yarn.resourcemanager.hostname</name>
  <value>systemhub611</value>
</property>

<!-- 日志聚集功能使用 -->
<property>
  <name>yarn.log-aggregation-enable</name>
  <value>true</value>
</property>

<!-- 日志保留时间设置为7天 根据开发情况,时间可自定义-->
<!-- 一天=3600秒 3600*24*7=604800 -->
<property>
  <name>yarn.log-aggregation.retain-seconds</name>
  <value>604800</value>
</property>

</configuration>
```

##### 3.1.1.11 vim `slaves`
```
systemhub511
systemhub611
systemhub711
```

##### 3.1.1.12 将HadoopCDH分发集群节点
```
[root@systemhub511 module]# scp -r cdh_flow/ root@systemhub611:/opt/module/cdh_flow/
[root@systemhub511 module]# scp -r cdh_flow/hadoop-cdh/ root@systemhub711:/opt/module/cdh_flow/
```
##### 3.1.1.13 格式化NameNode
```
[root@systemhub511 hadoop-cdh]# bin/hdfs namenode -format
```
##### 3.1.1.14 分别启动 HDFS & YARN服务
```
[root@systemhub511 hadoop-cdh]# sbin/start-dfs.sh
[root@systemhub611 hadoop-cdh]# sbin/start-yarn.sh
```
##### 3.1.1.15 启动HistoryServer
```
[root@systemhub511 hadoop-cdh]# sbin/mr-jobhistory-daemon.sh start historyserver
starting historyserver, logging to /opt/module/cdh_flow/hadoop-cdh/logs/mapred-root-historyserver-systemhub511.out
[root@systemhub511 hadoop-cdh]# 
```
##### 3.1.1.16 查看进程结果
```
[root@systemhub511 hadoop-cdh]# jps.sh
================        root@systemhub511 All Processes         ===========
22416 org.apache.hadoop.hdfs.server.namenode.NameNode
28321 sun.tools.jps.Jps
22690 org.apache.hadoop.hdfs.server.datanode.DataNode
23748 org.apache.hadoop.yarn.server.nodemanager.NodeManager
25991 org.apache.hadoop.mapreduce.v2.hs.JobHistoryServer
================        root@systemhub611 All Processes         ===========
18563 org.apache.hadoop.yarn.server.resourcemanager.ResourceManager
18069 org.apache.hadoop.hdfs.server.datanode.DataNode
21222 sun.tools.jps.Jps
18686 org.apache.hadoop.yarn.server.nodemanager.NodeManager
================        root@systemhub711 All Processes         ===========
18165 org.apache.hadoop.hdfs.server.namenode.SecondaryNameNode
18487 org.apache.hadoop.yarn.server.nodemanager.NodeManager
20858 sun.tools.jps.Jps
17918 org.apache.hadoop.hdfs.server.datanode.DataNode
[root@systemhub511 hadoop-cdh]# 
```
##### 3.1.1.17 访问 HDFS WebPage
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/oozie/start_001.jpg)

##### 3.1.1.18 停止 HDFS & YARN & HistoryServer
```
[root@systemhub511 hadoop-cdh]# sbin/mr-jobhistory-daemon.sh stop historyserver
stopping historyserver
[root@systemhub511 hadoop-cdh]# sbin/stop-dfs.sh
[root@systemhub611 hadoop-cdh]# sbin/stop-yarn.sh
```


### 3.2 Oozie (CDH Version) 部署
#### 3.2.1 Oozie 配置
##### 3.2.1.1 解压Oozie
```
[root@systemhub711 software]# tar -zxvf oozie-4.0.0-cdh5.3.6.tar.gz -C /opt/module/cdh_flow/
```
##### 3.2.1.2 重命名资源包名称
```
[root@systemhub711 cdh_flow]# mv oozie-4.0.0-cdh5.3.6 oozie-cdh
```

##### 3.2.1.3 在oozie根目录下解压`hadooplibsoozie-hadooplibs-4.0.0-cdh5.3.6.tar.gz`
```
[root@systemhub711  oozie-4.0.0-cdh5.3.6]# tar -zxvf oozie-hadooplibs-4.0.0-cdh5.3.6.tar.gz -C ../
```

##### 3.2.1.4 在Oozie根目录下创建libext目录
```
[root@systemhub711 oozie-cdh]# mkdir libext
```
##### 3.2.1.5 将依赖jar包拷贝到libext目录下
```
[root@systemhub711 oozie-cdh]# cp hadooplibs/hadooplib-2.5.0-cdh5.3.6.oozie-4.0.0-cdh5.3.6/* ./libext/
```

##### 3.2.1.6 将Mysql驱动包拷贝到libext目录下
```
[root@systemhub711 oozie-cdh]# cp /opt/software/mysql-libs/mysql-connector-java-5.1.27/mysql-connector-java-5.1.27-bin.jar ./libext/
```

##### 3.2.1.7 将ext-2.2.zip拷贝到libext目录下
```
[root@systemhub711 oozie-cdh]# cp /opt/software/ext-2.2.zip ./libext/
```

##### 3.2.1.8 修改Oozie配置文件
###### 3.2.1.8.1 vim `oozie-site.xml`
- 修改参数如下 : 
- `oozie.service.JPAService.jdbc.driver` | JDBC驱动类型
- `oozie.service.JPAService.jdbc.url` | 数据库地址
- `oozie.service.JPAService.jdbc.username` | 数据库用户名
- `oozie.service.JPAService.jdbc.password` | 数据库密码
- `oozie.service.HadoopAccessorService.hadoop.configurations` | Oozie引用Hadoop配置文件
``` xml
<?xml version="1.0"?>
<!--
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at
  
       http://www.apache.org/licenses/LICENSE-2.0
  
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<configuration>

    <!--
        Refer to the oozie-default.xml file for the complete list of
        Oozie configuration properties and their default values.
    -->

    <property>
        <name>oozie.service.ActionService.executor.ext.classes</name>
        <value>
            org.apache.oozie.action.email.EmailActionExecutor,
            org.apache.oozie.action.hadoop.HiveActionExecutor,
            org.apache.oozie.action.hadoop.ShellActionExecutor,
            org.apache.oozie.action.hadoop.SqoopActionExecutor,
            org.apache.oozie.action.hadoop.DistcpActionExecutor,
            org.apache.oozie.action.hadoop.Hive2ActionExecutor
        </value>
    </property>

    <property>
        <name>oozie.service.SchemaService.wf.ext.schemas</name>
        <value>
            shell-action-0.1.xsd,shell-action-0.2.xsd,shell-action-0.3.xsd,email-action-0.1.xsd,email-action-0.2.xsd,
            hive-action-0.2.xsd,hive-action-0.3.xsd,hive-action-0.4.xsd,hive-action-0.5.xsd,sqoop-action-0.2.xsd,
            sqoop-action-0.3.xsd,sqoop-action-0.4.xsd,ssh-action-0.1.xsd,ssh-action-0.2.xsd,distcp-action-0.1.xsd,
            distcp-action-0.2.xsd,oozie-sla-0.1.xsd,oozie-sla-0.2.xsd,hive2-action-0.1.xsd
        </value>
    </property>

    <property>
        <name>oozie.system.id</name>
        <value>oozie-${user.name}</value>
        <description>
            The Oozie system ID.
        </description>
    </property>

    <property>
        <name>oozie.systemmode</name>
        <value>NORMAL</value>
        <description>
            System mode for  Oozie at startup.
        </description>
    </property>

    <property>
        <name>oozie.service.AuthorizationService.security.enabled</name>
        <value>false</value>
        <description>
            Specifies whether security (user name/admin role) is enabled or not.
            If disabled any user can manage Oozie system and manage any job.
        </description>
    </property>

    <property>
        <name>oozie.service.PurgeService.older.than</name>
        <value>30</value>
        <description>
            Jobs older than this value, in days, will be purged by the PurgeService.
        </description>
    </property>

    <property>
        <name>oozie.service.PurgeService.purge.interval</name>
        <value>3600</value>
        <description>
            Interval at which the purge service will run, in seconds.
        </description>
    </property>

    <property>
        <name>oozie.service.CallableQueueService.queue.size</name>
        <value>10000</value>
        <description>Max callable queue size</description>
    </property>

    <property>
        <name>oozie.service.CallableQueueService.threads</name>
        <value>10</value>
        <description>Number of threads used for executing callables</description>
    </property>

    <property>
        <name>oozie.service.CallableQueueService.callable.concurrency</name>
        <value>3</value>
        <description>
            Maximum concurrency for a given callable type.
            Each command is a callable type (submit, start, run, signal, job, jobs, suspend,resume, etc).
            Each action type is a callable type (Map-Reduce, Pig, SSH, FS, sub-workflow, etc).
            All commands that use action executors (action-start, action-end, action-kill and action-check) use
            the action type as the callable type.
        </description>
    </property>

    <property>
		<name>oozie.service.coord.normal.default.timeout
		</name>
		<value>120</value>
		<description>Default timeout for a coordinator action input check (in minutes) for normal job.
            -1 means infinite timeout</description>
	</property>

    <property>
        <name>oozie.db.schema.name</name>
        <value>oozie</value>
        <description>
            Oozie DataBase Name
        </description>
    </property>

    <property>
        <name>oozie.service.JPAService.create.db.schema</name>
        <value>false</value>
        <description>
            Creates Oozie DB.

            If set to true, it creates the DB schema if it does not exist. If the DB schema exists is a NOP.
            If set to false, it does not create the DB schema. If the DB schema does not exist it fails start up.
        </description>
    </property>
    <!-- JDBC驱动类型 -->
    <property>
        <name>oozie.service.JPAService.jdbc.driver</name>
        <value>com.mysql.jdbc.Driver</value>
        <description>
            JDBC driver class.
        </description>
    </property>
    <!-- JDBC驱动地址 -->
    <property>
        <name>oozie.service.JPAService.jdbc.url</name>
        <value>jdbc:mysql://systemhub711:3306/oozie</value>
        <description>
            JDBC URL.
        </description>
    </property>
    <!-- 数据库用户名 -->
    <property>
        <name>oozie.service.JPAService.jdbc.username</name>
        <value>root</value>
        <description>
            DB user name.
        </description>
    </property>
    <!-- 数据库密码 -->
    <property>
        <name>oozie.service.JPAService.jdbc.password</name>
        <value>ax014ad</value>
        <description>
            DB user password.

            IMPORTANT: if password is emtpy leave a 1 space string, the service trims the value,
                       if empty Configuration assumes it is NULL.
        </description>
    </property>

    <property>
        <name>oozie.service.JPAService.pool.max.active.conn</name>
        <value>10</value>
        <description>
             Max number of connections.
        </description>
    </property>

    <property>
        <name>oozie.service.HadoopAccessorService.kerberos.enabled</name>
        <value>false</value>
        <description>
            Indicates if Oozie is configured to use Kerberos.
        </description>
    </property>

    <property>
        <name>local.realm</name>
        <value>LOCALHOST</value>
        <description>
            Kerberos Realm used by Oozie and Hadoop. Using 'local.realm' to be aligned with Hadoop configuration
        </description>
    </property>

    <property>
        <name>oozie.service.HadoopAccessorService.keytab.file</name>
        <value>${user.home}/oozie.keytab</value>
        <description>
            Location of the Oozie user keytab file.
        </description>
    </property>

    <property>
        <name>oozie.service.HadoopAccessorService.kerberos.principal</name>
        <value>${user.name}/localhost@${local.realm}</value>
        <description>
            Kerberos principal for Oozie service.
        </description>
    </property>

    <property>
        <name>oozie.service.HadoopAccessorService.jobTracker.whitelist</name>
        <value> </value>
        <description>
            Whitelisted job tracker for Oozie service.
        </description>
    </property>

    <property>
        <name>oozie.service.HadoopAccessorService.nameNode.whitelist</name>
        <value> </value>
        <description>
            Whitelisted job tracker for Oozie service.
        </description>
    </property>
    <!-- Oozie引用Hadoop配置文件 -->
    <property>
        <name>oozie.service.HadoopAccessorService.hadoop.configurations</name>
        <value>*=/opt/module/cdh_flow/hadoop-cdh/etc/hadoop</value>
        <description>
            Comma separated AUTHORITY=HADOOP_CONF_DIR, where AUTHORITY is the HOST:PORT of
            the Hadoop service (JobTracker, HDFS). The wildcard '*' configuration is
            used when there is no exact match for an authority. The HADOOP_CONF_DIR contains
            the relevant Hadoop *-site.xml files. If the path is relative is looked within
            the Oozie configuration directory; though the path can be absolute (i.e. to point
            to Hadoop client conf/ directories in the local filesystem.
        </description>
    </property>

    <property>
        <name>oozie.service.WorkflowAppService.system.libpath</name>
        <value>/user/${user.name}/share/lib</value>
        <description>
            System library path to use for workflow applications.
            This path is added to workflow application if their job properties sets
            the property 'oozie.use.system.libpath' to true.
        </description>
    </property>

    <property>
        <name>use.system.libpath.for.mapreduce.and.pig.jobs</name>
        <value>false</value>
        <description>
            If set to true, submissions of MapReduce and Pig jobs will include
            automatically the system library path, thus not requiring users to
            specify where the Pig JAR files are. Instead, the ones from the system
            library path are used.
        </description>
    </property>

    <property>
        <name>oozie.authentication.type</name>
        <value>simple</value>
        <description>
            Defines authentication used for Oozie HTTP endpoint.
            Supported values are: simple | kerberos | #AUTHENTICATION_HANDLER_CLASSNAME#
        </description>
    </property>

    <property>
        <name>oozie.authentication.token.validity</name>
        <value>36000</value>
        <description>
            Indicates how long (in seconds) an authentication token is valid before it has
            to be renewed.
        </description>
    </property>

    <property>
      <name>oozie.authentication.cookie.domain</name>
      <value></value>
      <description>
        The domain to use for the HTTP cookie that stores the authentication token.
        In order to authentiation to work correctly across multiple hosts
        the domain must be correctly set.
      </description>
    </property>

    <property>
        <name>oozie.authentication.simple.anonymous.allowed</name>
        <value>true</value>
        <description>
            Indicates if anonymous requests are allowed.
            This setting is meaningful only when using 'simple' authentication.
        </description>
    </property>

    <property>
        <name>oozie.authentication.kerberos.principal</name>
        <value>HTTP/localhost@${local.realm}</value>
        <description>
            Indicates the Kerberos principal to be used for HTTP endpoint.
            The principal MUST start with 'HTTP/' as per Kerberos HTTP SPNEGO specification.
        </description>
    </property>

    <property>
        <name>oozie.authentication.kerberos.keytab</name>
        <value>${oozie.service.HadoopAccessorService.keytab.file}</value>
        <description>
            Location of the keytab file with the credentials for the principal.
            Referring to the same keytab file Oozie uses for its Kerberos credentials for Hadoop.
        </description>
    </property>

    <property>
        <name>oozie.authentication.kerberos.name.rules</name>
        <value>DEFAULT</value>
        <description>
            The kerberos names rules is to resolve kerberos principal names, refer to Hadoop's
            KerberosName for more details.
        </description>
    </property>

    <!-- Proxyuser Configuration -->

    <!--

    <property>
        <name>oozie.service.ProxyUserService.proxyuser.#USER#.hosts</name>
        <value>*</value>
        <description>
            List of hosts the '#USER#' user is allowed to perform 'doAs'
            operations.

            The '#USER#' must be replaced with the username o the user who is
            allowed to perform 'doAs' operations.

            The value can be the '*' wildcard or a list of hostnames.

            For multiple users copy this property and replace the user name
            in the property name.
        </description>
    </property>

    <property>
        <name>oozie.service.ProxyUserService.proxyuser.#USER#.groups</name>
        <value>*</value>
        <description>
            List of groups the '#USER#' user is allowed to impersonate users
            from to perform 'doAs' operations.

            The '#USER#' must be replaced with the username o the user who is
            allowed to perform 'doAs' operations.

            The value can be the '*' wildcard or a list of groups.

            For multiple users copy this property and replace the user name
            in the property name.
        </description>
    </property>

    -->

    <!-- Default proxyuser configuration for Hue -->

    <property>
        <name>oozie.service.ProxyUserService.proxyuser.hue.hosts</name>
        <value>*</value>
    </property>

    <property>
        <name>oozie.service.ProxyUserService.proxyuser.hue.groups</name>
        <value>*</value>
    </property>

</configuration>
```

##### 3.2.1.9 Mysql中创建Oozie数据库
```
[root@systemhub711 ~]# mysql -uroot -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.

mysql> create database oozie;
Query OK, 1 row affected (0.00 sec)
mysql> 
```

#### 3.2.2 初始化 Oozie
##### 3.2.2.0 开启Hadoop相关服务
```
[root@systemhub511 hadoop-cdh]# sbin/start-dfs.sh
[root@systemhub611 hadoop-cdh]# sbin/start-yarn.sh
[root@systemhub511 hadoop-cdh]# sbin/mr-jobhistory-daemon.sh start historyserver
```
##### 3.2.2.1 将Oozie目录下yarn.tar.gz文件上传至HDFS
- yarn.tar.gz文件会自行解压
```
[root@systemhub711 oozie-cdh]# bin/oozie-setup.sh sharelib create -fs hdfs://systemhub511:8020 -locallib oozie-sharelib-4.0.0-cdh5.3.6-yarn.tar.gz
  setting CATALINA_OPTS="$CATALINA_OPTS -Xmx1024m"
log4j:WARN No appenders could be found for logger (org.apache.hadoop.util.Shell).
the destination path for sharelib is: /user/root/share/lib/lib_20190512195606
[root@systemhub711 oozie-cdh]# 
```
- 执行成功后,查看结果
```
[root@systemhub511 hadoop-cdh]# bin/hadoop fs -cat /user/root/share/lib/lib_20000522105606

Found 9 items
drwxr-xr-x   - root supergroup  0 /user/root/share/lib/lib_20190512195606/distcp
drwxr-xr-x   - root supergroup 0 /user/root/share/lib/lib_20190512195606/hcatalog
drwxr-xr-x   - root supergroup 0 /user/root/share/lib/lib_20190512195606/hive
drwxr-xr-x   - root supergroup 0 /user/root/share/lib/lib_20190512195606/hive2
drwxr-xr-x   - root supergroup 0 /user/root/share/lib/lib_20190512195606/mapreduce-streaming
drwxr-xr-x   - root supergroup 0 /user/root/share/lib/lib_20190512195606/oozie
drwxr-xr-x   - root supergroup 0 /user/root/share/lib/lib_20190512195606/pig
-rw-r--r--   3 root supergroup 1364 /user/root/share/lib/lib_20190512195606/sharelib.properties
drwxr-xr-x   - root supergroup 0 /user/root/share/lib/lib_20190512195606/sqoop
[root@systemhub511 hadoop-cdh]# 
```

##### 3.2.2.2 创建oozie.sql文件
```
[root@systemhub711 oozie-cdh]# bin/ooziedb.sh create -sqlfile oozie.sql -run

The SQL commands have been written to: oozie.sql
[root@systemhub711 oozie-cdh]#
```

##### 3.2.2.3 打包项目,生成war包
```
[root@systemhub711 oozie-cdh]# bin/oozie-setup.sh prepare-war
INFO: Oozie is ready to be started
```

#### 3.2.3 启动 Oozie服务
- 1.开启服务
```
[root@systemhub711 oozie-cdh]# bin/oozied.sh start
```

- 2.访问 Oozie WebPage | `http://hostname:11000`

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/oozie/start_002.jpg)

- 关闭服务
```
[root@systemhub711 oozie-cdh]# bin/oozied.sh stop
```



## 4. Oozie 任务调度
### 4.1 Oozie 调度Shell脚本
- 使用Oozie调度Shell脚本
#### 4.1.1 创建工作目录
```
[root@systemhub711 oozie-cdh]# mkdir oozie_workflow
```
#### 4.1.2 解压官方案例模板
```
[root@systemhub711 oozie-cdh]# tar -zxvf oozie-examples.tar.gz -C ./
```
#### 4.1.3 将shell任务模板拷贝至oozie_workflow目录下
```
[root@systemhub711 oozie-cdh]# cp -r examples/apps/shell/ ./oozie_workflow/
```

#### 4.1.4 编写脚本
- 1.vim `shell_workflow.sh`
```
[root@systemhub711 shell]# pwd
/opt/module/cdh_flow/oozie-cdh/oozie_workflow/shell
[root@systemhub711 shell]# vim shell_workflow.sh
```
``` powershell
#!/bin/bash
ifconfig > /opt/module/cdh_flow/oozie-cdh/shell_workflow.log
```
#### 4.1.5 修改配置文件 job.properties & workflow.xml
- 1.vim `job.properties`
```
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# HDFS 地址
nameNode=hdfs://systemhub511:8020
# ResourceManager 地址
jobTracker=systemhub611:8032
# 队列名称
queueName=default
# 队列工作路径
examplesRoot=oozie_workflow

oozie.wf.application.path=${nameNode}/user/${user.name}/${examplesRoot}/shell

EXEC=shell_workflow.sh
```
- 2.vim `workflow.xml`
``` xml
<!--
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<workflow-app xmlns="uri:oozie:workflow:0.4" name="shell-wf">
    <start to="shell-node"/>
    <action name="shell-node">
        <shell xmlns="uri:oozie:shell-action:0.2">
            <job-tracker>${jobTracker}</job-tracker>
            <name-node>${nameNode}</name-node>
            <configuration>
                <property>
                    <name>mapred.job.queue.name</name>
                    <value>${queueName}</value>
                </property>
            </configuration>
            <exec>${EXEC}</exec>
            <file>/user/root/oozie_workflow/shell/${EXEC}#${EXEC}</file>
            <!-- <argument>my_output=Hello Oozie</argument> -->
            <capture-output/>
        </shell>
        <ok to="end"/>
        <error to="fail"/>
    </action>
    <kill name="fail">
        <message>Shell action failed, error message[${wf:errorMessage(wf:lastErrorNode())}]</message>
    </kill>
    <kill name="fail-output">
        <message>Incorrect output, expected [Hello Oozie] but was [${wf:actionData('shell-node')['my_output']}]</message>
    </kill>
    <end name="end"/>
</workflow-app>
```

#### 4.1.6 上传任务
```
[root@systemhub711 oozie-cdh]# /opt/module/cdh_flow/hadoop-cdh/bin/hadoop fs -put ./oozie_workflow/ /user/root
```
#### 4.1.7 执行任务
```
[root@systemhub711 oozie-cdh]# bin/oozie job -oozie http://systemhub711:11000/oozie -config oozie_workflow/shell/job.properties -run
job: 0000000-190512201415314-oozie-root-W
[root@systemhub711 oozie-cdh]# 
```
- 查看运行结果
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/oozie/start_003.jpg)
```
[root@systemhub711 oozie-cdh]# cat shell_workflow.log
CST 2019
[root@systemhub711 oozie-cdh]# 
```

#### 4.1.8 结束某个任务
```
[root@systemhub711 oozie-cdh]# bin/oozie job -oozie http://systemhub711:11000/oozie -kill 0000000-190512201415314-oozie-root-W
```

### 4.2 Oozie 逻辑调度执行多Job
- 使用Oozie执行多个Job调度
#### 4.2.1 编写脚本 | vim `shell_workflow2.sh`
```
#!/bin/bash
/bin/date > /opt/module/cdh_flow/oozie-cdh/shell_workflow2.log
```

#### 4.2.2 修改配置文件 job.properties & workflow.xml
- 1.vim `job.properties`
```
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# HDFS 地址
nameNode=hdfs://systemhub511:8020
# ResourceManager 地址
jobTracker=systemhub611:8032
# 队列名称
queueName=default
# 队列工作路径
examplesRoot=oozie_workflow

oozie.wf.application.path=${nameNode}/user/${user.name}/${examplesRoot}/shell

EXEC1=shell_workflow.sh
EXEC2=shell_workflow2.sh
```
- 2.vim `workflow.xml`
``` xml
<!--
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<workflow-app xmlns="uri:oozie:workflow:0.4" name="shell-wf">
    <start to="shell-node1"/>
    <!-- Action 1 -->
    <action name="shell-node1">
        <shell xmlns="uri:oozie:shell-action:0.2">
            <job-tracker>${jobTracker}</job-tracker>
            <name-node>${nameNode}</name-node>
            <configuration>
                <property>
                    <name>mapred.job.queue.name</name>
                    <value>${queueName}</value>
                </property>
            </configuration>
            <exec>${EXEC1}</exec>
            <file>/user/root/oozie_workflow/shell/${EXEC1}#${EXEC1}</file>
            <!-- <argument>my_output=Hello Oozie</argument> -->
            <capture-output/>
        </shell>
        <ok to="shell-node2"/>
        <error to="fail"/>
    </action>
    <!-- Action 2 -->
    <action name="shell-node2">
        <shell xmlns="uri:oozie:shell-action:0.2">
            <job-tracker>${jobTracker}</job-tracker>
            <name-node>${nameNode}</name-node>
            <configuration>
                <property>
                    <name>mapred.job.queue.name</name>
                    <value>${queueName}</value>
                </property>
            </configuration>
            <exec>${EXEC2}</exec>
            <file>/user/root/oozie_workflow/shell/${EXEC2}#${EXEC2}</file>
            <!-- <argument>my_output=Hello Oozie</argument> -->
            <capture-output/>
        </shell>
        <ok to="end"/>
        <error to="fail"/>
    </action>
    <kill name="fail">
        <message>Shell action failed, error message[${wf:errorMessage(wf:lastErrorNode())}]</message>
    </kill>
    <kill name="fail-output">
        <message>Incorrect output, expected [Hello Oozie] but was [${wf:actionData('shell-node')['my_output']}]</message>
    </kill>
    <end name="end"/>
</workflow-app>
```

#### 4.2.3 上传任务
- 删除shell目录下所有文件资源
```
[root@systemhub711 oozie-cdh]# /opt/module/cdh_flow/hadoop-cdh/bin/hadoop fs -rm -r /user/root/oozie_workflow/shell/*
```
- 上传最新配置文件
```
[root@systemhub711 oozie-cdh]# /opt/module/cdh_flow/hadoop-cdh/bin/hadoop fs -put ./oozie_workflow/shell/* /user/root/oozie_workflow/shell/
```

#### 4.2.4 执行任务
```
[root@systemhub711 oozie-cdh]# bin/oozie job -oozie http://systemhub711:11000/oozie -config ./oozie_workflow/shell/job.properties -run
job: 0000004-1415314-oozie-root-W
[root@systemhub711 oozie-cdh]# 
```

#### 4.2.5 查看任务结果
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/oozie/start_004.jpg)

```
[root@systemhub711 oozie-cdh]# cat shell_workflow.log
Sun May CST 2019
[root@systemhub711 oozie-cdh]# cat shell_workflow2.log
CST 2019
[root@systemhub711 oozie-cdh]# 
```

### 4.3 Oozie 调度MapReduce任务
- 使用Oozie调度MapReduce任务
#### 4.3.1 引用MapReduce官方jar包
#### 4.3.2 将map-reduce官方模板拷贝至oozie_workflow目录下
```
[root@systemhub711 oozie-cdh]# cp -r examples/apps/map-reduce/ ./oozie_workflow/
```
- 1.在hadoop-cdh目录下创建datas文件并创建oozie_wordcount文件
```
[root@systemhub711 cdh_flow]# cd hadoop-cdh/
[root@systemhub711 hadoop-cdh]# mkdir datas
[root@systemhub711 hadoop-cdh]# cd datas
[root@systemhub711 datas]# vim oozie_wordcount.txt
```
```
hadoop hive zookeeper
flume kafka hbase
azkaban oozie
```
- 2.将oozie_wordcount文件上传至HDFS
```
[root@systemhub711 hadoop-cdh]# bin/hadoop fs -mkdir -p /datas/001
[root@systemhub711 hadoop-cdh]# bin/hadoop fs -put ./datas/oozie_wordcount.txt /datas/001
```
- 3.执行Yarn jar程序
```
[root@systemhub711 hadoop-cdh]# bin/yarn jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.5.0-cdh5.3.6.jar wordcount /datas/001/oozie_wordcount.txt /out/001
```
- 4.查看运行结果
```
[root@systemhub711 hadoop-cdh]# bin/hadoop fs -cat /out/001/*
WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
azkaban 1
flume   1
hadoop  1
hbase   1
hive    1
kafka   1
oozie   1
zookeeper       1
[root@systemhub711 hadoop-cdh]# 
```

#### 4.3.3 修改配置文件 job.properties & workflow.xml
- 1.vim `job.properties`
```
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

nameNode=hdfs://systemhub511:8020
jobTracker=systemhub611:8032
queueName=default
examplesRoot=oozie_workflow

oozie.wf.application.path=${nameNode}/user/${user.name}/${examplesRoot}/map-reduce/workflow.xml
outputDir=map-reduce
```

- 2.vim `workflow.xml`
``` xml
<!--
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at
  
       http://www.apache.org/licenses/LICENSE-2.0
  
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<workflow-app xmlns="uri:oozie:workflow:0.2" name="map-reduce-wf">
  <start to="mr-node"/>
  <action name="mr-node">
    <map-reduce>
      <job-tracker>${jobTracker}</job-tracker>
      <name-node>${nameNode}</name-node>
      <prepare>
        <delete path="${nameNode}/output/001"/>
      </prepare>
      <configuration>
        <property>
          <name>mapred.job.queue.name</name>
          <value>${queueName}</value>
        </property>
        <!--配置调度MR任务时,使用新API -->
        <property>
          <name>mapred.mapper.new-api</name>
          <value>true</value>
        </property>
        <property>
          <name>mapred.reducer.new-api</name>
          <value>true</value>
        </property>
        <!--指定Job Key输出类型-->
        <property>
          <name>mapreduce.job.output.key.class</name>
          <value>org.apache.hadoop.io.Text</value>
        </property>
        <!--指定Job Value输出类型-->
        <property>
          <name>mapreduce.job.output.value.class</name>
          <value>org.apache.hadoop.io.IntWritable</value>
        </property>
        <!--指定输入路径-->
        <property>
          <name>mapred.input.dir</name>
          <value>/datas/001/oozie_wordcount.txt</value>
        </property>
        <!--指定输出路径-->
        <property>
          <name>mapred.output.dir</name>
          <value>/output/001</value>
        </property>
        <!--指定Map类-->
        <property>
          <name>mapreduce.job.map.class</name>
          <value>org.apache.hadoop.examples.WordCount$TokenizerMapper</value>
        </property>
        <!--指定Reduce类-->
        <property>
          <name>mapreduce.job.reduce.class</name>
          <value>org.apache.hadoop.examples.WordCount$IntSumReducer</value>
        </property>
        <property>
          <name>mapred.map.tasks</name>
          <value>1</value>
        </property>
      </configuration>
    </map-reduce>
    <ok to="end"/>
    <error to="fail"/>
  </action>
  <kill name="fail">
    <message>Map/Reduce failed, error message[${wf:errorMessage(wf:lastErrorNode())}]</message>
  </kill>
  <end name="end"/>
</workflow-app>
```


#### 4.3.4 将执行jar包拷贝至map-reduce lib目录下
- 删除老版本jar包
```
[root@systemhub711 hadoop-cdh]# cd /opt/module/cdh_flow/oozie-cdh/oozie_workflow/map-reduce/lib/
[root@systemhub711 lib]# ll
total 28
-rw-r--r-- 1 root root 24707 May 12 23:53 oozie-examples-4.0.0-cdh5.3.6.jar
[root@systemhub711 lib]# rm -rf oozie-examples-4.0.0-cdh5.3.6.jar
```
- 拷贝新版本jar包
```
[root@systemhub711 oozie-cdh]# cp /opt/module/cdh_flow/hadoop-cdh/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.5.0-cdh5.3.6.jar ./oozie_workflow/map-reduce/lib/
[root@systemhub711 oozie-cdh]# 
```

#### 4.3.5 上传配置
```
[root@systemhub711 oozie-cdh]# /opt/module/cdh_flow/hadoop-cdh/bin/hadoop fs -put ./oozie_workflow/map-reduce/ /user/root/oozie_workflow
```

#### 4.3.6 执行任务
```
[root@systemhub711 oozie-cdh]# bin/oozie job -oozie http://systemhub711:11000/oozie -config ./oozie_workflow/map-reduce/job.properties -run
job: 0000005-190512201415314-oozie-root-W
[root@systemhub711 oozie-cdh]# 
```

#### 4.3.7 查看运行结果
```
[root@systemhub711 oozie-cdh]# /opt/module/cdh_flow/hadoop-cdh/bin/hadoop fs -cat /output/001/*
applicable
azkaban 1
flume   1
hadoop  1
hbase   1
hive    1
kafka   1
oozie   1
zookeeper       1
[root@systemhub711 oozie-cdh]# 
```

### 4.4 Oozie 定时任务
- Coordinator周期性调度任务
- 事先配置Linux时区以及时间服务器
#### 4.4.1 配置oozie-site.xml文件
- 该属性在oozie-default.xml中找到即可
``` xml
<!-- 修改时区为东八区区时 -->
<property>
  <name>oozie.processing.timezone</name>
  <value>GMT+0800</value>
  <description>
    Oozie server timezone. Valid values are UTC and GMT(+/-)####, for example 'GMT+0530' would be India
    timezone. All dates parsed and genered dates by Oozie Coordinator/Bundle will be done in the specified
    timezone. The default value of 'UTC' should not be changed under normal circumtances. If for any reason
    is changed, note that GMT(+/-)#### timezones do not observe DST changes.
  </description>
</property>
```

#### 4.4.2 修改js框架 时间设置
``` javascript
function getTimeZone() {
    Ext.state.Manager.setProvider(new Ext.state.CookieProvider());
    return Ext.state.Manager.get("TimezoneId","GMT+0800");
}
```

#### 4.4.3 重启Oozie服务
```
[root@systemhub711 oozie-cdh]# bin/oozied.sh stop
[root@systemhub711 oozie-cdh]# bin/oozied.sh start
```
#### 4.4.4 将官方模板定时任务拷贝至oozie_workflow目录下
```
[root@systemhub711 oozie-cdh]# cp -r examples/apps/cron/ ./oozie_workflow/
```

#### 4.4.5 修改配置文件 job.properties & workflow.xml & coordinator.xml
- 1.vim `job.properties`
```
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

nameNode=hdfs://systemhub511:8020
jobTracker=systemhub611:8032
queueName=default
examplesRoot=oozie_workflow

oozie.coord.application.path=${nameNode}/user/${user.name}/${examplesRoot}/cron
# start : 必须设置为未来时间,否则任务失败
start=2019-05-13T01:30+0800
end=2019-05-13T01:45+0800
workflowAppUri=${nameNode}/user/${user.name}/${examplesRoot}/cron

EXEC3=shell_workflow3.sh
```

- 2.vim `workflow.xml`
``` xml
<!--
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at
  
       http://www.apache.org/licenses/LICENSE-2.0
  
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<workflow-app xmlns="uri:oozie:workflow:0.5" name="one-op-wf">
  <start to="p3-shell-node"/>
  <action name="p3-shell-node">
    <shell xmlns="uri:oozie:shell-action:0.2">
      <job-tracker>${jobTracker}</job-tracker>
      <name-node>${nameNode}</name-node>
      <configuration>
        <property>
          <name>mapred.job.queue.name</name>
          <value>${queueName}</value>
        </property>
      </configuration>
      <exec>${EXEC3}</exec>
      <file>/user/root/oozie_workflow/cron/${EXEC3}#${EXEC3}</file>
      <capture-output/>
    </shell>
    <ok to="end"/>
    <error to="fail"/>
  </action>
  <kill name="fail">
    <message>Shell action failed, error message[${wf:errorMessage(wf:lastErrorNode())}]</message>
  </kill>
  <kill name="fail-output">
    <message>Incorrect output, expected [Hello Oozie] but was [${wf:actionData('shell-node')['my_output']}]</message>
  </kill>
  <end name="end"/>
</workflow-app>
```
- 3.vim `coordinator.xml`
```
<!--
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at
  
       http://www.apache.org/licenses/LICENSE-2.0
  
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<coordinator-app name="cron-coord" frequency="${coord:minutes(5)}" start="${start}" end="${end}" timezone="GMT+0800"
                 xmlns="uri:oozie:coordinator:0.2">
        <action>
        <workflow>
            <app-path>${workflowAppUri}</app-path>
            <configuration>
                <property>
                    <name>jobTracker</name>
                    <value>${jobTracker}</value>
                </property>
                <property>
                    <name>nameNode</name>
                    <value>${nameNode}</value>
                </property>
                <property>
                    <name>queueName</name>
                    <value>${queueName}</value>
                </property>
            </configuration>
        </workflow>
    </action>
</coordinator-app>
```

- 4.vim `shell_workflow3.sh`
```
#!/bin/bash
date >> /opt/module/cdh_flow/oozie-cdh/shell_workflow3.log
```

#### 4.4.6 上传配置
```
[root@systemhub711 oozie-cdh]# /opt/module/cdh_flow/hadoop-cdh/bin/hadoop fs -put ./oozie_workflow/cron/ /user/root/oozie_workflow
```
#### 4.4.7 启动定时任务
- oozie允许最小执行任务频率为`5分钟`
```
[root@systemhub711 oozie-cdh]# bin/oozie job -oozie http://systemhub711:11000/oozie -config ./oozie_workflow/cron/job.properties -run 
job: 0000000-190513005930530-oozie-root-C
[root@systemhub711 oozie-cdh]#
```
#### 4.4.8 查看定时结果

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/oozie/start_005.jpg)
```
[root@systemhub711 oozie-cdh]# cat shell_workflow3.log
01:30:17 CST 2019
[root@systemhub711 oozie-cdh]# 
```




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