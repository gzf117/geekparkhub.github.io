# 大数据生态系统 修仙之道 Sqoop Blog

@(2019-04-20)[ Docs Language:简体中文 & English|Programing Language:Sqoop|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)|![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg) | ![GitHub repo size in bytes](https://img.shields.io/github/repo-size/geekparkhub/geekparkhub.github.io.svg) | GeekDeveloper:[JEEP-711](https://github.com/jeep711)|Github:[github.com/geekparkhub](https://github.com/geekparkhub)|Gitee:[gitee.com/geekparkhub](https://gitee.com/geekparkhub) ]

##  🐘 Sqoop Technology 修仙之道 德功并进 🐘

![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/sqoop/sqoop.jpg)

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



## 1. Sqoop 概述

- Sqoop是一款开源工具,主要用于在Hadoop(Hive)与传统数据库(MySQL/PostgreSQL)等之间进行数据传递,可以将一个关系型数据库(例如:MySQL/Oracle/PostgreSQL等)中的数据导入到Hadoop HDFS中,也可以将HDFS数据导入到关系型数据库中.
- Sqoop项目开发始于2009年,于2012年3月孵化出世,最早是作为Hadoop第三方模块存在,后来为了让开发者能够快速部署,也为了开发者能够快速迭代开发,Sqoop独立成为一个Apache顶级项目.
- Sqoop2最新版本是1.99.7,请注意1.99.7与1.4.6不兼容,且没有特征不完整,它并不打算用于生产部署.



## 2. Sqoop 原理
- 将导入或导出命令翻译成MapReduce程序来实现.
- 在翻译出MapReduce中主要是对inputformat和outputformat进行定制.


## 3. Sqoop 部署
### 3.1 Sqoop Official Download
- 安装Sqoop前提是已经具备Java和Hadoop环境
- `官方文档` : [sqoop.apache.org/docs/1.4.6/](http://sqoop.apache.org/docs/1.4.6/SqoopUserGuide.html)
- `官方下载` : [archive.apache.org/dist/sqoop/1.4.6/](http://archive.apache.org/dist/sqoop/1.4.6/)

### 3.2 部署 Sqoop
#### 3.2.1 解压
> 1.解压sqoop安装包到指定目录
```
[root@systemhub711 software]# tar -zxvf sqoop-1.4.6.bin__hadoop-2.0.4-alpha.tar.gz -C /opt/module/
sqoop-1.4.6.bin__hadoop-2.0.4-alpha/
[root@systemhub711 software]#
```
> 2.重命名包名称
```
[root@systemhub711 module]# mv sqoop-1.4.6.bin__hadoop-2.0.4-alpha sqoop
```

#### 3.2.2 修改配置文件
> Sqoop配置文件与大多数大数据框架类似,在sqoop根目录下conf目录中.
> 1.重命名配置文件
```
[root@systemhub711 sqoop]# mv conf/sqoop-env-template.sh conf/sqoop-env.sh
```
> 2.修改配置文件
vim `sqoop-env.sh`
```
#Set path to where bin/hadoop is available
export HADOOP_COMMON_HOME=/opt/module/hadoop

#Set path to where hadoop-*-core.jar is available
export HADOOP_MAPRED_HOME=/opt/module/hadoop

#set the path to where bin/hbase is available
export HBASE_HOME=/opt/module/hbase

#Set the path to where bin/hive is available
export HIVE_HOME=/opt/module/hive

#Set the path for where zookeper config dir is
export ZOOKEEPER_HOME=/opt/module/zookeeper
export ZOOCFGDIR=/opt/module/zookeeper
```

#### 3.2.3 拷贝JDBC驱动
- 拷贝JDBC驱动到sqoop/`lib`目录下
```
[root@systemhub711 sqoop]# cp /opt/software/mysql-libs/mysql-connector-java-5.1.27/mysql-connector-java-5.1.27-bin.jar ./lib/
```

### 3.3 验证 Sqoop
#### 3.3.1 `bin/sqoop help`
```
[root@systemhub711 sqoop]# bin/sqoop help
Warning: /opt/module/sqoop/bin/../../hcatalog does not exist! HCatalog jobs will fail.
Please set $HCAT_HOME to the root of your HCatalog installation.
Warning: /opt/module/sqoop/bin/../../accumulo does not exist! Accumulo imports will fail.
Please set $ACCUMULO_HOME to the root of your Accumulo installation.
19/05/09 22:04:19 INFO sqoop.Sqoop: Running Sqoop version: 1.4.6
usage: sqoop COMMAND [ARGS]

Available commands:
  codegen            Generate code to interact with database records
  create-hive-table  Import a table definition into Hive
  eval               Evaluate a SQL statement and display the results
  export             Export an HDFS directory to a database table
  help               List available commands
  import             Import a table from a database to HDFS
  import-all-tables  Import tables from a database to HDFS
  import-mainframe   Import datasets from a mainframe server to HDFS
  job                Work with saved jobs
  list-databases     List available databases on a server
  list-tables        List available tables in a database
  merge              Merge results of incremental imports
  metastore          Run a standalone Sqoop metastore
  version            Display version information

See 'sqoop help COMMAND' for information on a specific command.
[root@systemhub711 sqoop]# 
```

#### 3.3.2 测试Sqoop连接数据库
- `bin/sqoop list-databases --connect jdbc:mysql://systemhub711:3306/ --username root --password ax0pix`
```
[root@systemhub711 sqoop]# bin/sqoop list-databases --connect jdbc:mysql://systemhub711:3306/ --username root --password ax0pix
Warning: /opt/module/sqoop/bin/../../hcatalog does not exist! HCatalog jobs will fail.
Please set $HCAT_HOME to the root of your HCatalog installation.
Warning: /opt/module/sqoop/bin/../../accumulo does not exist! Accumulo imports will fail.
Please set $ACCUMULO_HOME to the root of your Accumulo installation.
19/05/09 22:09:51 INFO sqoop.Sqoop: Running Sqoop version: 1.4.6
19/05/09 22:09:51 WARN tool.BaseSqoopTool: Setting your password on the command-line is insecure. Consider using -P instead.
19/05/09 22:09:51 INFO manager.MySQLManager: Preparing to use a MySQL streaming resultset.
information_schema
metastore
mysql
performance_schema
test
[root@systemhub711 sqoop]# 
```


## 4. Sqoop 实例
### 4.1 导入数据
- 在Sqoop中 , “`导入`” 概念指 : 从非大数据集群(RDBMS)向大数据集群(HDFS / HIVE / HBASE)中传输数据,叫做 “`导入`” , 即使用`import`关键字.

#### 4.1.1 RDBMS导入HDFS
##### 4.1.1 确保Mysql服务正常启动状态
##### 4.1.2 在Mysql中新建一张数据表并插入数据
```
[root@systemhub711 sqoop]# mysql -uroot -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 4
Server version: 5.6.24 MySQL Community Server (GPL)

mysql> create database company;
Query OK, 1 row affected (0.00 sec)

mysql> create table company.staff(id int(4) primary key not null auto_increment, name varchar(255), sex varchar(255));
Query OK, 0 rows affected (0.01 sec)

mysql> insert into company.staff(name, sex) values('test001', 'male');
Query OK, 1 row affected (0.00 sec)

mysql> insert into company.staff(name, sex) values('test002', 'female');
Query OK, 1 row affected (0.00 sec)

mysql> 
```
- 启动Hadoop集群服务
```
[root@systemhub511 ~]# start-cluster.sh
================                Start All Node Services         ===========
================================================================
```
- 查看所有节点进程状态
```
[root@systemhub511 ~]# jps.sh
================        root@systemhub511 All Processes         ===========
1845 sun.tools.jps.Jps
32550 org.apache.hadoop.yarn.server.nodemanager.NodeManager
31287 org.apache.zookeeper.server.quorum.QuorumPeerMain
31784 org.apache.hadoop.hdfs.server.datanode.DataNode
31561 org.apache.hadoop.hdfs.server.namenode.NameNode
32670 org.apache.hadoop.mapreduce.v2.hs.JobHistoryServer
================        root@systemhub611 All Processes         ===========
32209 org.apache.hadoop.yarn.server.resourcemanager.ResourceManager
1754 sun.tools.jps.Jps
31579 org.apache.hadoop.hdfs.server.datanode.DataNode
31324 org.apache.zookeeper.server.quorum.QuorumPeerMain
32381 org.apache.hadoop.yarn.server.nodemanager.NodeManager
================        root@systemhub711 All Processes         ===========
14516 org.apache.hadoop.yarn.server.nodemanager.NodeManager
13975 org.apache.hadoop.hdfs.server.namenode.SecondaryNameNode
17773 sun.tools.jps.Jps
13293 org.apache.hadoop.hdfs.server.datanode.DataNode
12863 org.apache.zookeeper.server.quorum.QuorumPeerMain
[root@systemhub511 ~]# 
```

##### 4.1.3 导入数据
###### 4.1.3.1 全部导入
- 1.导入语句
```
bin/sqoop import \
--connect jdbc:mysql://systemhub711:3306/company \
--username root \
--password ax0pix \
--table staff \
--target-dir /user/sqoop/core_flow/company \
--delete-target-dir \
--num-mappers 1 \
--fields-terminated-by "\t"
```
- 2.执行操作
```
[root@systemhub711 sqoop]# bin/sqoop import \
> --connect jdbc:mysql://systemhub711:3306/company \
> --username root \
> --password ax0pix \
> --table staff \
> --target-dir /user/sqoop/core_flow/company \
> --delete-target-dir \
> --num-mappers 1 \
> --fields-terminated-by "\t"
[root@systemhub711 sqoop]# 
```
- 3.`hadoop fs -cat`指令查看此时上传数据内容
```
[root@systemhub511 ~]# hadoop fs -cat /user/sqoop/core_flow/company/part-m-00000
SLF4J: Class path contains multiple SLF4J bindings.
1       test001 male
2       test002 female
[root@systemhub511 ~]# 
```
###### 4.1.3.2 查询导入
- `must contain '$CONDITIONS' in WHERE clause`.
- 如果query后使用是双引号,则`$CONDITIONS`前必须加转移符,防止shell识别为自身变量.
- `-query`选项,不能同时与`--table`选项使用.
- 1.查询导入语句
```
bin/sqoop import \
--connect jdbc:mysql://systemhub711:3306/company \
--username root \
--password ax0pix \
--target-dir /user/sqoop/core_flow/company \
--delete-target-dir \
--num-mappers 1 \
--fields-terminated-by "\t" \
--query 'select name,sex from staff where id <= 1 and $CONDITIONS;'
```
- 2.执行操作
```
[root@systemhub711 sqoop]# bin/sqoop import \
> --connect jdbc:mysql://systemhub711:3306/company \
> --username root \
> --password ax0pix \
> --target-dir /user/sqoop/core_flow/company \
> --delete-target-dir \
> --num-mappers 1 \
> --fields-terminated-by "\t" \
> --query 'select name,sex from staff where id <= 1 and $CONDITIONS;'
[root@systemhub711 sqoop]# 
```
- 3.`hadoop fs -cat`指令查看此时上传数据内容
```
[root@systemhub511 ~]# hadoop fs -cat /user/sqoop/core_flow/company/part-m-00000SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in
test001 male
[root@systemhub511 ~]# 
```


###### 4.1.3.3 导入指定列
- columns中如果涉及到多列,用逗号分隔,分隔时不要添加空格.
- 1.导入指定列语句
```
bin/sqoop import \
--connect jdbc:mysql://systemhub711:3306/company \
--username root \
--password ax0pix \
--columns id,sex \
--table staff \
--target-dir /user/sqoop/core_flow/company \
--delete-target-dir \
--num-mappers 1 \
--fields-terminated-by "\t"
```
- 2.执行操作
```
[root@systemhub711 sqoop]# bin/sqoop import \
> --connect jdbc:mysql://systemhub711:3306/company \
> --username root \
> --password ax0pix \
> --columns id,sex \
> --table staff \
> --target-dir /user/sqoop/core_flow/company \
> --delete-target-dir \
> --num-mappers 1 \
> --fields-terminated-by "\t"
[root@systemhub711 sqoop]# 
```
- 3.`hadoop fs -cat`指令查看此时上传数据内容
```
[root@systemhub511 ~]# hadoop fs -cat /user/sqoop/core_flow/company/part-m-00000
SLF4J: Class path contains multiple SLF4J bindings.
1       male
2       female
[root@systemhub511 ~]# 
```

###### 4.1.3.4 使用sqoop关键字筛选查询导入数据
- 在Sqoop中可以使用sqoop `import -D property.name=property.value`方式加入执行任务的参数,多个参数用空格隔开.
- 1.筛选查询导入数据语句
```
bin/sqoop import \
--connect jdbc:mysql://systemhub711:3306/company \
--username root \
--password ax0pix \
--target-dir /user/sqoop/core_flow/company \
-delete-target-dir \
--num-mappers 1 \
--fields-terminated-by "\t" \
--table staff \
--columns id,sex \
--where "id=1"
```
- 2.执行操作
```
[root@systemhub711 sqoop]# bin/sqoop import \
> --connect jdbc:mysql://systemhub711:3306/company \
> --username root \
> --password ax0pix \
> --target-dir /user/sqoop/core_flow/company \
> -delete-target-dir \
> --num-mappers 1 \
> --fields-terminated-by "\t" \
> --table staff \
> --columns id,sex \
> --where "id=1"
[root@systemhub711 sqoop]# 
```
- 3.`hadoop fs -cat`指令查看此时上传数据内容
```
[root@systemhub511 ~]# hadoop fs -cat /user/sqoop/core_flow/company/part-m-00000
SLF4J: Class path contains multiple SLF4J bindings.
1       male
[root@systemhub511 ~]# 
```

#### 4.1.2 RDBMS导入Hive
- 该过程分为两步,第一步将数据导入到HDFS,第二步将导入到HDFS的数据迁移到Hive仓库
- 1.开启Hive服务 / 若已开启,此步骤略过
```
[root@systemhub711 ~]# cd /opt/module/hive/
[root@systemhub711 hive]# bin/hive
hive (default)> 
```
- 2.导入Hive数据语句
```
bin/sqoop import \
--connect jdbc:mysql://systemhub711:3306/company \
--username root \
--password ax0pix \
--table staff \
--num-mappers 1 \
--hive-import \
--fields-terminated-by "\t" \
--hive-overwrite \
--hive-table staff_hive
```
- 3.执行操作
```
[root@systemhub711 sqoop]# bin/sqoop import \
> --connect jdbc:mysql://systemhub711:3306/company \
> --username root \
> --password ax0pix \
> --table staff \
> --num-mappers 1 \
> --hive-import \
> --fields-terminated-by "\t" \
> --hive-overwrite \
> --hive-table staff_hive
[root@systemhub711 sqoop]# INFO hive.HiveImport: Hive import complete.
```
- 4.查看导入数据结果
```
hive (default)> show tables;
OK
tab_name
staff_hive
Time taken: 0.2 seconds, Fetched: 23 row(s)
hive (default)> select * from staff_hive;
OK
staff_hive.id   staff_hive.name staff_hive.sex
1       test001 male
2       test002 female
Time taken: 0.871 seconds, Fetched: 2 row(s)
hive (default)> 
```

#### 4.1.3 RDBMS导入HBase
- 1.开启HBase服务
```
[root@systemhub511 ~]# /opt/module/hbase/bin/start-hbase.sh
starting master, logging to /opt/module/hbase/logs/hbase-root-master-systemhub511.out
systemhub711: starting regionserver, logging to /opt/module/hbase/bin/../logs/hbase-root-regionserver-systemhub711.out
systemhub611: starting regionserver, logging to /opt/module/hbase/bin/../logs/hbase-root-regionserver-systemhub611.out
systemhub511: starting regionserver, logging to /opt/module/hbase/bin/../logs/hbase-root-regionserver-systemhub511.out
systemhub611: starting master, logging to /opt/module/hbase/bin/../logs/hbase-root-master-systemhub611.out
[root@systemhub511 ~]# 
```
- 2.Sqoop1.4.6只支持HBase1.0.1之前版本自动创建HBase数据表功能.
- 解决方法 : 手动创建HBase数据表.
```
[root@systemhub511 ~]# /opt/module/hbase/bin/hbase shell
hbase(main):001:0> create 'hbase_company','info'
0 row(s) in 1.7970 seconds
=> Hbase::Table - hbase_company
hbase(main):002:0>
```
- 3.导入HBase数据语句
```
bin/sqoop import \
--connect jdbc:mysql://systemhub711:3306/company \
--username root \
--password ax0pix \
--table staff \
--columns "id,name,sex" \
--column-family "info" \
--hbase-create-table \
--hbase-row-key "id" \
--hbase-table "hbase_company"  \
--num-mappers 1 \
--split-by id
```
- 4.执行操作
```
[root@systemhub711 sqoop]# bin/sqoop import \
> --connect jdbc:mysql://systemhub711:3306/company \
> --username root \
> --password ax0pix \
> --table staff \
> --columns "id,name,sex" \
> --column-family "info" \
> --hbase-create-table \
> --hbase-row-key "id" \
> --hbase-table "hbase_company"  \
> --num-mappers 1 \
> --split-by id
[root@systemhub711 sqoop]# 
```
- 5.查看导入数据结果
```
hbase(main):002:0> scan 'hbase_company'
ROW  COLUMN+CELL                                                                                                  
 1   column=info:name, timestamp=1557417862576, value=test001                                                     
 1   column=info:sex, timestamp=1557417862576, value=male                                                         
 2   column=info:name, timestamp=1557417862576, value=test002                                                     
 2   column=info:sex, timestamp=1557417862576, value=female                                                       
2 row(s) in 0.4090 seconds
hbase(main):003:0>
```


### 4.2 导出数据
- 在Sqoop中 , “`导出`”概念指 : 从大数据集群(HDFS / HIVE / HBASE)向非大数据集群(RDBMS)中传输数据,叫做 : “`导出`” , 即使用`export`关键字.

#### 4.2.1 Hive/HDFS导出RDBMS
- Mysql中如果表不存在,不会自动创建.
- 清空staff表数据
```
mysql> use company;
Database changed
mysql> truncate table staff;
Query OK, 0 rows affected (0.01 sec)
mysql> 
```
- 1.导出数据语句
```
bin/sqoop export \
--connect jdbc:mysql://systemhub711:3306/company \
--username root \
--password ax0pix \
--table staff \
--num-mappers 1 \
--export-dir /user/hive/warehouse/staff_hive \
--input-fields-terminated-by "\t"
```
- 2.执行操作
```
[root@systemhub711 sqoop]# bin/sqoop export \
> --connect jdbc:mysql://systemhub711:3306/company \
> --username root \
> --password ax0pix \
> --table staff \
> --num-mappers 1 \
> --export-dir /user/hive/warehouse/staff_hive \
> --input-fields-terminated-by "\t"
[root@systemhub711 sqoop]#
```
- 3.查看导入数据结果
```
mysql> select * from staff;
+----+---------+--------+
| id | name    | sex    |
+----+---------+--------+
|  1 | test001 | male   |
|  2 | test002 | female |
+----+---------+--------+
2 rows in set (0.00 sec)
mysql> 
```

### 4.3 脚本打包
- 使用`.opt格式`文件打包sqoop执行,然后执行逻辑业务处理.
#### 4.3.1 创建.opt文件
```
[root@systemhub711 sqoop]# mkdir job_flow
[root@systemhub711 sqoop]# vim job_flow/sqp_job-001.opt
```
#### 4.3.2 编写Sqoop脚本
``` powershell
export
--connect
jdbc:mysql://systemhub711:3306/company
--username
root
--password
ax0pix 
--table
staff
--num-mappers
1
--export-dir
/user/hive/warehouse/staff_hive
--input-fields-terminated-by
"\t"
```

#### 4.3.3 执行脚本
- 1.清空staff表数据
```
mysql> use company;
Database changed
mysql> truncate table staff;
Query OK, 0 rows affected (0.01 sec)
mysql> 
```
- 2.执行脚本指令
```
[root@systemhub711 sqoop]# bin/sqoop --options-file job_flow/sqp_job-001.opt
```
- 3.查看导入数据结果
```
mysql> select * from staff;
+----+---------+--------+
| id | name    | sex    |
+----+---------+--------+
|  1 | test001 | male   |
|  2 | test002 | female |
+----+---------+--------+
2 rows in set (0.00 sec)
mysql> 
```

## 5. Sqoop 常用命令手册

### 5.1 常用命令列举

| ID      |     命令 |   类   |   说明   |
| :--------: | :--------:| :------: | :------: |
| 1    |   import |  ImportTool  |  将数据导入到集群  |
| 2    |   export |  ExportTool  |  将集群数据导出  |
| 3    |   codegen |  CodeGenTool  |  获取数据库中某张表数据生成Java并打包Jar  |
| 4    |   create-hive-table |  CreateHiveTableTool  |  创建Hive表  |
| 5    |   eval |  EvalSqlTool  |  查看SQL执行结果  |
| 6    |   import-all-tables |  ImportAllTablesTool  |  导入某个数据库下所有表到HDFS中.  |
| 7    |   job |  JobTool  |  用来生成一个sqoop任务,生成后该任务并不执行,除非使用命令执行该任务.  |
| 8    |   list-databases |  ListDatabasesTool  |  列出所有数据库名称  |
| 9    |   list-tables |  ListTablesTool  |  列出某个数据库下所有表  |
| 10    |   merge |  MergeTool  |  将HDFS中不同目录下面数据合在一起,并存放在指定的目录中.  |
| 11    |   metastore |  MetastoreTool  |  记录sqoop job元数据信息,如果不启动metastore实例,则默认元数据存储目录为: `~/.sqoop`,如果要更改存储目录,可以在配置文件`sqoop-site.xml`中进行更改.  |
| 12    |   help |  HelpTool  |  打印sqoop帮助信息  |
| 13    |   version |  VersionTool  |  打印sqoop版本信息  |


### 5.2 命令 & 参数详解
- 所谓公用参数,就是大多数命令都支持的参数.
#### 5.2.1 公用参数 : 数据库连接
| ID      |     参数 |   说明   |
| :--------: | :--------:| :------: |
| 1    |   `--connect` |  连接关系型数据库URL  |
| 2    |   `--connection-manager` |  指定要使用连接管理类  |
| 3    |   `--driver` |  JDBC Driver Class  |
| 4    |   `--help` |  打印帮助信息  |
| 5    |   `--username` |  连接数据库用户名  |
| 6    |   `--password` |  连接数据库密码  |
| 7    |   `--verbose` |  在控制台打印出详细信息  |


#### 5.2.2 公用参数 : import
| ID      |     参数 |   说明   |
| :--------: | :--------:| :------: |
| 1    |   `--enclosed-by<char>` |  给字段值前后加上指定字符  |
| 2    |   `--escaped-by<char>` |  对字段中双引号加转义符  |
| 3    |   `--fields-terminated-by<char>` |  设定每个字段以什么符号作为结束,默认为逗号  |
| 4    |   `--lines-terminated-by<char>` |  设定每行记录之间分隔符,默认是`\n`  |
| 5    |   `--mysql-delimiters` |  Mysql默认分隔符设置,字段之间以逗号分隔,行之间以`\n`分隔,默认转义符是`\`,字段值以单引号包裹.  |
| 6    |   `--optionally-enclosed-by<char>` |  给带有双引号或单引号字段值前后加上指定字符  |

#### 5.2.3 公用参数 : export
| ID      |     参数 |   说明   |
| :--------: | :--------:| :------: |
| 1    |   `--input-enclosed-by<char>` |  对字段值前后加上指定字符  |
| 2    |   `--input-escaped-by<char>` |  对含有转移符字段做转义处理  |
| 3    |   `--input-fields-terminated-by<char>` |  字段之间分隔符  |
| 4    |   `--input-lines-terminated-by<char>` |  行之间分隔符  |
| 5    |   `--input-optionally-enclosed-by<char>` |  给带有双引号或单引号字段前后加上指定字符  |


#### 5.2.4 公用参数 : hive
| ID      |     参数 |   说明   |
| :--------: | :--------:| :------: |
| 1    |   `--hive-delims-replacement<arg>` |  用自定义字符串替换掉数据中的`\r`,`\n`,`\013,`\010`等字符  |
| 2    |   `--hive-drop-import-delims` |  在导入数据到hive时,去掉数据中的`\r`,`\n`,`\013`,`\010`等字符  |
| 3    |   `--map-column-hive<map>` |  生成hive表时,可以更改生成字段数据类型  |
| 4    |   `--hive-partition-key` |  创建分区,后面直接跟分区名,分区字段默认类型为string  |
| 5    |   `--hive-partition-value<v>` |  导入数据时,指定某个分区的值  |
| 6    |   `--hive-home<dir>` |  hive安装目录,可以通过该参数覆盖之前默认配置目录  |
| 7    |   `--hive-import` |  将数据从关系数据库中导入到hive表中  |
| 8    |   `--hive-overwrite` |  覆盖掉在hive表中已经存在数据  |
| 9    |   `--create-hive-table` |  默认是false,即如果目标表已经存在了,那么创建任务失败  |
| 10    |   `--hive-table` |  后面接要创建的hive表,默认使用MySQL表名  |
| 11    |   `--table` |  指定关系数据库表名  |


#### 5.2.5 命令&参数 : import
- 将关系型数据库中数据导入到HDFS(包括Hive / HBase)中,如果导入的是Hive,那么当Hive中没有对应表时,则自动创建.
- 1.命令 | 导入数据到hive中
```
bin/sqoopimport \
--connect jdbc:mysql://systemhub711:3306/company \
--username root \
--password ax0pix \
--table staff \
--hive-import
```
- 如 : 增量导入数据到Hive中,`mode=append`
- append不能与`--hive-`等参数同时使用(Append mode for hive imports is not yet supported. Please remove the parameter --append-mode)
```
bin/sqoopimport \
--connect jdbc:mysql://systemhub711:3306/company \
--username root \
--password ax0pix \
--table staff \
--num-mappers 1 \
--fields-terminated-by "\t" \
--target-dir /user/hive/warehouse/staff_hive \
--check-column id \
--incremental append \
--last-value 3
```
- 如 : 增量导入数据到HDFS中,`mode=lastmodified`
- 使用`lastmodified`方式导入数据要指定增量数据是要`--append`(追加),还是要`--merge-key`(合并).
- last-value指定值是会包含于增量导入数据中.
```
// 建表并插入数据
mysql> create table company.staff_timestamp(
    id int (4), 
    name varchar (255), 
    sex varchar (255), 
    last_modified timestamp DEFAULT CURRENT_TIMESTAMP 
      ON UPDATE
        CURRENT_TIMESTAMP 
);
mysql> insert 
  into
    company.staff_timestamp
    (id, name, sex) 
  values
    (1, 'AAA', 'female');

mysql> insert 
  into
    company.staff_timestamp
    (id, name, sex) 
  values
    (2, 'BBB', 'female');
```
- 先导入一部分数据
```
bin/sqoopimport \
--connect jdbc:mysql://systemhub711:3306/company \
--username root \
--password ax0pix \
--table staff_timestamp \
--delete-target-dir \
--m 1
```
- 再增量导入一部分数据
```
mysql> insert 
  into
    company.staff_timestamp
    (id, name, sex) 
  values
    (3, 'CCC', 'female');
```
```
bin/sqoopimport \
--connect jdbc:mysql://systemhub711:3306/company \
--username root \
--password ax0pix \
--table staff_timestamp \
--check-column last_modified \
--incremental lastmodified \
--last-value "1800-00-01 00:00:00" \
--m 1\
--append
```

- 2.参数
| ID      |     参数 |   说明   |
| :--------: | :--------:| :------: |
| 1    |   `--append` |  将数据追加到HDFS中已经存在DataSet中,如果使用该参数,sqoop会把数据先导入到临时文件目录,再合并  |
| 2    |   `--as-avrodatafile` |  将数据导入到一个Avro数据文件中  |
| 3    |   `--as-sequencefile` |  将数据导入到一个sequence文件中  |
| 4    |   `--as-textfile` |  将数据导入到一个普通文本文件中  |
| 5    |   `--boundary-query <statement>` |  边界查询,导入数据为该参数值(一条sql语句)所执行结果区间内数据  |
| 6    |   `--columns<col1, col2, col3>` |  指定要导入字段  |
| 7    |   `--direct` |  直接导入模式,使用是关系数据库自带导入导出工具,以便加快导入导出过程  |
| 8    |   `--direct-split-size` |  在使用上面direct直接导入基础上,对导入流按字节分块,即达到该阈值就产生新文件  |
| 9    |   `--inline-lob-limit` |  设定大对象数据类型最大值  |
| 10    |   `--m`或`–num-mappers` |  启动N个map来并行导入数据,默认4个  |
| 11    |   `--query`或`--e<statement>` |  将查询结果数据导入,使用时必须伴随参`--target-dir`,`--hive-table`,如果查询中有where条件,则条件后必须加上`$CONDITIONS`关键字  |
| 12    |   `--split-by <column-name>` |  按照某一列来切分表工作单元,不能与`--autoreset-to-one-mapper`连用(请参考官方文档)  |
| 13    |   `--table<table-name>` |  关系数据库表名  |
| 14    |   `--target-dir <dir>` |  指定HDFS路径  |
| 15    |   `--warehouse-dir <dir>` |  与14参数不能同时使用,导入数据到HDFS时指定目录  |
| 16    |   `--where` |  从关系数据库导入数据时查询条件  |
| 17    |   `--z`或`--compress` |  允许压缩  |
| 18    |   `--compression-codec` |  指定hadoop压缩编码类,默认为gzip(Use Hadoop codec default gzip)  |
| 19    |   `--null-string <null-string>` |  string类型列,如果null替换为指定字符串  |
| 20    |   `--null-non-string <null-string>` |  非string类型列,如果null,替换为指定字符串  |
| 21    |   `--check-column<col>` |  作为增量导入判断列名  |
| 22    |   `--incremental<mode>` |  mode:`append`或`lastmodified`  |
| 23    |   `--last-value<value>` |  指定某一个值,用于标记增量导入位置  |



#### 5.2.6 命令&参数 : export
- 从HDFS(包括Hive和HBase)中将数据导出到关系型数据库中.
- 1.命令
```
bin/sqoop export \
--connect jdbc:mysql://systemhub711:3306/company \
--username root \
--password ax0pix \
--table staff \
--export-dir /user/sqoop/core_flow/company \
--input-fields-terminated-by "\t" \
--num-mappers 1
```
- 2.参数
| ID      |     参数 |   说明   |
| :--------: | :--------:| :------: |
| 1    |   `--direct` |  利用数据库自带导入导出工具,以便于提高效率  |
| 2    |   `--export-dir <dir>` |  存放数据HDFS源目录  |
| 3    |   `-m`或`--num-mappers <n>` |  启动N个map来并行导入数据,默认4个  |
| 4    |   `--table <table-name>` |  指定导出到哪个RDBMS中表  |
| 5    |   `--update-key <col-name>` |  对某一列字段进行更新操作  |
| 6    |   `--update-mode <mode>` |  updateonly / allowinsert(默认)  |
| 7    |   `--input-null-string <null-string>` |  请参考import该类似参数说明  |
| 8    |   `--input-null-non-string <null-string>` |  请参考import该类似参数说明  |
| 9    |   `--staging-table <staging-table-name>` |  创建一张临时表,用于存放所有事务的结果,然后将所有事务结果一次性导入到目标表中,防止错误  |
| 10    |   `--clear-staging-table` |  如果第9个参数非空,则可以在导出操作执行前,清空临时事务结果表  |


#### 5.2.7 命令&参数 : codegen
- 将关系型数据库中表映射为一个Java类,在该类中有各列对应的各个字段
```
bin/sqoop codegen \
--connect jdbc:mysql://systemhub711:3306/company \
--username root \
--password ax0pix \
--table staff \
--bindir /home/core_flow/code/staff \
--class-name Staff \
--fields-terminated-by "\t"
```
| ID      |     参数 |   说明   |
| :--------: | :--------:| :------: |
| 1    |   `--bindir<dir>` |  指定生成Java文件、编译成class文件及将生成文件打包为jar文件输出路径  |
| 2    |   `--class-name<name>` |  设定生成Java文件指定名称  |
| 3    |   `--outdir<dir>` |  生成Java文件存放路径  |
| 4    |   `--package-name <name>` |  包名,如com.geekparkhub,就会生成com和geekparkhub两级目录  |
| 5    |   `--input-null-non-string <null-str>` |  在生成Java文件中,可以将null字符串或者不存在字符串设置为想要设定的值(例如空字符串)  |
| 6    |   `--input-null-string <null-str>` |  将null字符串替换成想要替换的值(一般与5同时使用)  |
| 7    |   `--map-column-java <arg>` |  数据库字段在生成的Java文件中会映射成各种属性,且默认数据类型与数据库类型保持对应关系,该参数可以改变默认类型,例如 : `--map-column-java id=long,name=String`  |
| 8    |   `-null-non-string <null-str>` |  在生成Java文件时,可以将不存在或者null字符串设置为其他值  |
| 9    |   `--null-string <null-str>` |  在生成Java文件时,将null字符串设置为其他值(一般与8同时使用)  |
| 10    |   `--table<table-name>` |  对应关系数据库中表名,生成Java文件中各个属性与该表的各个字段一一对应  |

#### 5.2.8 命令&参数 : create-hive-table
- 生成与关系数据库表结构对应hive表结构
- 1.命令
```
bin/sqoop create-hive-table \
--connect jdbc:mysql://systemhub711:3306/company \
--username root \
--password ax0pix \
--table staff \
--hive-table hive_staff
```
- 2.参数
| ID      |     参数 |   说明   |
| :--------: | :--------:| :------: |
| 1    |   `--hive-home<dir>` |  Hive安装目录,可以通过该参数覆盖掉默认Hive目录  |
| 2    |   `--hive-overwrite` |  覆盖掉在Hive表中已经存在数据  |
| 3    |   `--create-hive-table` |  默认是false,如果目标表已经存在了,那么创建任务会失败  |
| 4    |   `--hive-table` |  后面接要创建hive表  |
| 5    |   `--table` |  指定关系数据库表名  |


#### 5.2.9 命令&参数 : eval
- 可以快速使用SQL语句对关系型数据库进行操作,经常用于在import数据之前,了解一下SQL语句是否正确,数据是否正常,并可以将结果显示在控制台.
- 1.命令
```
bin/sqoop eval \
--connect jdbc:mysql://systemhub711:3306/company \
--username root \
--password ax0pix \
--table staff \
--query "SELECT * FROM staff"
```
- 2.参数
| ID      |     参数 |   说明   |
| :--------: | :--------:| :------: |
| 1    |   `--query`或`--e` |  后跟查询SQL语句  |


#### 5.2.10 命令&参数 : import-all-tables
- 可以将RDBMS中所有表导入到HDFS中,每一个表都对应一个HDFS目录
- 1.命令
```
bin/sqoop import-all-tables \
--connect jdbc:mysql://systemhub711:3306/company \
--username root \
--password ax0pix \
--warehouse-dir/all_tables
```
- 2.参数
| ID      |     参数 |   说明   |
| :--------: | :--------:| :------: |
| 1    |   `--as-avrodatafile` |  参数含义均和import对应含义一致  |
| 2    |   `--as-sequencefile` |  参数含义均和import对应含义一致  |
| 3    |   `--as-textfile` |  参数含义均和import对应含义一致  |
| 4    |   `--direct` |  参数含义均和import对应含义一致  |
| 5    |   `--direct-split-size <n>` |  参数含义均和import对应含义一致  |
| 6    |   `--inline-lob-limit <n>` |  参数含义均和import对应含义一致  |
| 7    |   `--m`或`—num-mappers <n>` |  参数含义均和import对应含义一致  |
| 8    |   `--warehouse-dir <dir>` |  参数含义均和import对应含义一致  |
| 9    |   `-z`或`--compress` |  参数含义均和import对应含义一致  |
| 10    |   `--compression-codec` |  参数含义均和import对应含义一致  |

#### 5.2.11 命令&参数 : job
- 用来生成一个sqoop任务,生成后不会立即执行,需要手动执行.
- 1.命令
- 注意import-all-tables和它左边的`--`之间有一个空格
- 如果需要连接metastore,则`--meta-connect jdbc:hsqldb:hsql://systemhub711:16000/sqoop`
```
bin/sqoop job \
--create myjob--import-all-tables \
--connect jdbc:mysql://systemhub711:3306/company \
--username root \
--password ax0pix
```
```
bin/sqoop job \
--list
```
```
bin/sqoop job \
--exec myjob
```
- 2.参数
| ID      |     参数 |   说明   |
| :--------: | :--------:| :------: |
| 1    |   `--create<job-id>` |  创建job参数  |
| 2    |   `--delete <job-id>` |  删除job  |
| 3    |   `--exec <job-id>` |  执行job  |
| 4    |   `--help` |  显示job帮助  |
| 5    |   `--list` |  显示job列表  |
| 6    |   `--meta-connect <jdbc-uri>` |  用来连接metastore服务  |
| 7    |   `--show <job-id>` |  显示job信息  |
| 7    |   `--verbose` |  打印命令运行时详细信息  |
- 在执行一个job时,如果需要手动输入数据库密码,可以做如下优化
``` xml
<property>
  <name>sqoop.metastore.client.record.password</name>
  <value>true</value>
  <description>If true, allow saved passwords in the metastore.</description>
</property>
```

#### 5.2.12 命令&参数 : list-databases
- 1.命令
```
bin/sqoop list-databases \
--connect jdbc:mysql://systemhub711:3306/ \
--username root \
--password ax0pix
```
- 2.参数与公用参数一样


#### 5.2.13 命令&参数 : list-tables
- 1.命令
```
bin/sqoop list-tables \
--connect jdbc:mysql://systemhub711:3306/company \
--username root \
--password ax0pix
```
- 2.参数与公用参数一样


#### 5.2.14 命令&参数 : merge
- 将HDFS中不同目录下面数据合并在一起并放入指定目录中.
- 数据环境 | 数据的列之间的分隔符应该为`\t`,行与行之间的分割符为`\n`.
- `new_staff`
```
1	AAA	male
2	BBB	male
3	CCC	male
4	DDD	male
```
- `old_staff`
```
1	AAA	female
2	CCC	female
3	BBB	female
6	DDD	female
```
- 1.命令 | 创建JavaBean
```
bin/sqoop codegen \
--connect jdbc:mysql://systemhub711:3306/company \
--username root \
--password ax0pix \
--table staff \
--bindir /home/core_flow/code/staff \
--class-name Staff\
--fields-terminated-by "\t"
```
- 2.开始合并
```
bin/sqoop merge \
--new-data /test/new/ \
--onto /test/old/ \
--target-dir /test/merged \
--jar-file /home/core_flow/code/staff/Staff.jar \
--class-name Staff \
--merge-key id
```
- 3.查看结果
```
1	AAA	male
2	BBB	male
3	CCC	male
4	DDD	male
6	DDD	female
```
- 4.参数
| ID      |     参数 |   说明   |
| :--------: | :--------:| :------: |
| 1    |   `--new-data <path>` |  HDFS待合并的数据目录,合并后在新数据集中保留  |
| 2    |   `--onto <path>` |  HDFS合并后,重复部分在新数据集中被覆盖  |
| 3    |   `--merge-key <col>` |  合并键,一般是主键ID  |
| 4    |   `--jar-file <file>` |  合并时引入jar包,该jar包是通过Codegen工具生成的jar包  |
| 5    |   `--class-name <class>` |  对应表名或对象名,该class类是包含在jar包中  |
| 6    |   `--target-dir <path>` |  合并后数据在HDFS里存放目录  |


#### 5.2.15 命令&参数 : metastore
- 记录了Sqoopjob元数据信息,如果不启动该服务,那么默认job元数据存储目录为`~/.sqoop` , 可在`sqoop-site.xml`中修改.
- 1.命令 | 启动sqoop的metastore服务
```
[root@systemhub711 ~ ]# bin/sqoop metastore
```
- 2.参数
| ID      |     参数 |   说明   |
| :--------: | :--------:| :------: |
| 1    |   `--shutdown` |  关闭metastore  |


## 6. 修仙之道 技术架构迭代 登峰造极之势
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