	
# 大数据生态系统 修仙之道 PornhubAction Blog

@(2019-03-25)[ Docs Language:简体中文 & English|Programing Language:Statistical Analysis|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)|![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg) | ![GitHub repo size in bytes](https://img.shields.io/github/repo-size/geekparkhub/geekparkhub.github.io.svg) | GeekDeveloper:[JEEP-711](https://github.com/jeep711)|Github:[github.com/geekparkhub](https://github.com/geekparkhub)|Gitee:[gitee.com/geekparkhub](https://gitee.com/geekparkhub) ]

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hive/project_cover/cover-3.jpg)

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

## 0. PornhubAction Statistical Analysis 📌

| Ⅰ | Ⅱ | Ⅲ | Ⅳ | Ⅴ | Ⅵ | Ⅶ | Ⅷ | Ⅸ | Ⅹ |
| :--------: | :---------: | :---------: | :---------: | :---------: | :---------:| :---------: | :-------: | :-------:| :------:|
|Cloud [☁️](#网络-cloud)|Computer [💻](#操作系统-computer)| Algorithm [✏️](#数据结构与算法-pencil2)| Object Oriented [👫](#面向对象-couple) |DataBase [💾](#数据库-floppy_disk)| Java [☕](#java-coffee)| Distributed 式[💦](#分布式-sweat_drops)| Tools [🔧](#工具-hammer)| Coding [👨‍💻](#编码实践-speak_no_evil)| Notes [📃](#后记-memo) |


## 1. Pornhub 简介 🔍
> Pornhub形式类似于Youtube,是一个(🇨🇦加拿大🇨🇦)🚫🚫视频分享网站,传说中老司机引以为傲的影片天堂🤭🤭,它是当前最大的🚫🚫视频网站之一,总访问量过一亿人次,Pornhub宣布预计于2018年推出识别系统,系统将自动识别视频内演员,并将之分门别类,服务分享遍及全球.   —— [维基百科](https://zh.wikipedia.org/wiki/Pornhub)


## 2. PornhubActionProject 简介 🔍

> 数据存储单位: **`bit`**/**`Byte`**/**`KB`**/**`MB`**/**`GB`**/**`TB`**/ **`PB`**/**`EB`**/**`ZB`**/**`YB`**/**`BB`**/**`NB`**/**`DB`**
> 
> **`1 Byte = 8bit`** | **`1 KB = 1024Byte`** | **`1 MB = 1024KB`** | **`1 GB = 1024MB`**
> 
> **`1 TB = 1024GB`** | **`1 PB = 1024TB`** |  **`1 EB = 1024PB`** | **`1 ZB = 1024EB`**
> 
> **`1 YB = 1024ZB`** | **`1 BB = 1024YB`** | **`1 NB = 1024BB`** | **`1 DB = 1024NB`**
> 
> PornhubAction诞生:源于Pornhub(用户群体/视频集合/多元化访问量&日志信息/地域国际化等等)数据量已达到EB级别.
> 
> 为此进一步激发你的学习欲望,万事俱备,只欠东风,庞大的数据集在向我们挥手👋,我们将站在巨人肩膀上Work.
> 
> 当然这仅仅是个起点,任何人都可以用PornhubAction (学生/研究员/爱好者/极客/工程师/开发者/发明家/创业者等等)都可以在Apache2.0开源协议下开发PornhubAction.
> 
> 我们希望能鼓励你们创造自己最喜欢的语言界面,PornhubAction尚未竣工,它还需要被进一步扩展和上层建构,我们刚发布了源代码最初版本,并且将持续完善它.


## 3. PornhubAction 需求描述
> 统计Pornhub视频网站常规指标,各种TopN指标.
> 
> 🔥 统计视频观看数`Top10`.
> 🔥 统计视频类别热度`Top10`.
> 🔥 统计视频观看数`Top20`所属类别.
> 🔥 统计视频观看数`Top50`所关联视频的所属类别Rank.
> 🔥 统计每个类别中视频热度`Top10`.
> 🔥 统计每个类别中视频流量`Top10`.
> 🔥 统计上传视频最多的用户`Top10`以及相关视频.
> 🔥 统计每个类别视频观看数`Top10`.


## 4. PornhubAction 技术选型
- Hadoop2.7.2 : HDFS / MapReduce 
- 
- Hive 1.2.2 : Order By / Sort By / Distribute By / Cluster By / UDAF & UDTF / Orc存储 / Hive 分区 & 分桶
- 
- Mysql 5.6

### 4.1 Pornhub 原数据存储位置
> 在本地服务器 创建Pornhub原数据多级目录.
> 将Pornhub原数据依次上传 本地服务器.
```
[root@systemhub711 ~]# cd /opt/module/datas/

[root@systemhub711 datas]# mkdir -p core_flow/develop/project/analysis/pornhub_action/metadata/

[root@systemhub711 datas]# mkdir -p core_flow/develop/project/analysis/pornhub_action/metadata/pornhub_user/001

[root@systemhub711 datas]# mkdir -p core_flow/develop/project/analysis/pornhub_action/metadata/pornhub_video/001
```

> 在HDFS 创建Pornhub原数据多级目录.
```
[root@systemhub711 metadata]# hadoop fs -mkdir -p /core_flow/develop/project/analysis/pornhub_action/metadata

[root@systemhub711 metadata]# hadoop fs -mkdir -p /core_flow/develop/project/analysis/pornhub_action/metadata/pornhub_user/001

[root@systemhub711 metadata]# hadoop fs -mkdir -p /core_flow/develop/project/analysis/pornhub_action/metadata/pornhub_video/001

[root@systemhub711 metadata]# hadoop fs -ls /core_flow/develop/project/analysis/pornhub_action/metadata/
Found 2 items
drwxr-xr-x   - root supergroup 0  /core_flow/develop/project/analysis/pornhub_action/metadata/pornhub_user/001
drwxr-xr-x   - root supergroup 0  /core_flow/develop/project/analysis/pornhub_action/metadata/pornhub_video/001
[root@systemhub711 metadata]#
```
> 再将本地服务器原数据依次上传 HDFS分布式文件系统中存储.
```
[root@systemhub711 /]# hadoop fs -copyFromLocal /opt/module/datas/core_flow/develop/project/analysis/pornhub_action/metadata/pornhub_user/001/pornhub_user.txt /core_flow/develop/project/analysis/pornhub_action/metadata/pornhub_user/001/pornhub_user.txt

[root@systemhub711 /]# hadoop fs -copyFromLocal /opt/module/datas/core_flow/develop/project/analysis/pornhub_action/metadata/pornhub_video/001/pornhub_video.txt /core_flow/develop/project/analysis/pornhub_action/metadata/pornhub_video/001/pornhub_video.txt

[root@systemhub711 /]# hadoop fs -ls /core_flow/develop/project/analysis/pornhub_action/metadata/*
Found 1 items
drwxr-xr-x   - root supergroup 0  /core_flow/develop/project/analysis/pornhub_action/metadata/pornhub_user/001
Found 1 items
drwxr-xr-x   - root supergroup 0  /core_flow/develop/project/analysis/pornhub_action/metadata/pornhub_video/001
```

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hive/project_cover/start_001.jpg)

> 视频数据集: `/core_flow/develop/project/analysis/pornhub_action/metadata/pornhub_video/001`
> 
> 用户数据集:`/core_flow/develop/project/analysis/pornhub_action/metadata/pornhub_user/001`

### 4.2 数据清洗
> Hadoop MapReduce

### 4.3 数据分析
> MapReduce or Hive


## 5. Develop PornhubAction

### 5.1 数据结构
#### 5.1.1 视频 数据表结构
| 字段      |     备注 |   详细描述   |
| :--------: | :--------:| :------:|
| videoid | 视频唯一id | 11位字符串 |
| uploader|视频上传者 | 上传视频用户名:String类型 |
| updates | 视频日期 | 视频上传日期|
| category | 视频类别 | 上传视频指定视频分类 |
| length | 视频长度 | 标识视频长度:整数类型 |
| views | 观看次数 | 视频被浏览次数 |
| rate | 视频评分 | 满分5分 |
| ratings | 流量 | 视频流量:整数类型 |
| conments | 评论数 | 一个视频评论数:整数类型 |
| relatedids | 相关视频id | 相关视频id,最多20个 |

#### 5.1.2 用户 数据表结构
| 字段      |     备注 |   详细描述   |
| :--------: | :--------:| :------:|
| uploader  |   上传者用户名 |  string |
| videos    |   上传视频数 |  int |
| friends   |   朋友数量 |  int  |

### 5.2 ETL原始数据
> 通过观察原始数据形式可以发现,视频可以有多个所属分类,每个所属分类用&符号分割,且分割两边有空格字符,同时相关视频也是可以有多个元素,多个相关视频又用“\t”进行分割,为了分析数据时方便对存在多个子元素的数据进行操作.
> 
> 首先进行是对数据重组清洗操作,即将所有类别用“&”分割,同时去除两边空格,多个相关视频id使用“&”进行分割.

### 5.3 JetBrains IntelliJ IDEA New Maven Project | 此过程省略
#### 5.3.1 Update Maven pom.xml
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.geekparkhub.core.application.analysis.pornhub</groupId>
    <artifactId>PornhubAction</artifactId>
    <version>1.0-SNAPSHOT</version>

    <dependencies>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-core</artifactId>
            <version>2.8.2</version>
        </dependency>

        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-common</artifactId>
            <version>2.7.2</version>
        </dependency>

        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-client</artifactId>
            <version>2.7.2</version>
        </dependency>

        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-hdfs</artifactId>
            <version>2.7.2</version>
        </dependency>

        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-yarn-server-resourcemanager</artifactId>
            <version>2.7.2</version>
        </dependency>

    </dependencies>

</project>
```

#### 5.3.2 Create PornhubActionETLMapper.class
``` java
package com.geekparkhub.core.application.analysis.pornhub;

import org.apache.commons.lang.StringUtils;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

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
 * PornhubActionETLMapper
 * <p>
 */

public class PornhubActionETLMapper extends Mapper<LongWritable, Text, Text, NullWritable> {

    /**
     * Extract k
     * 提取k
     */
    Text k = new Text();

    /**
     * Rewrite the map() method
     * 重写map()方法
     *
     * @param key
     * @param value
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {

        /**
         * 1. Get the first row of data
         * 1. 获取第一行数据
         */
        String line = value.toString();

        /**
         * 2. Cleaning data
         * 2. 清洗数据
         */
        String etlString = PornhubActionETLUtil.getETLString(line);
        // 如果数据为空,则直接返回.
        if (StringUtils.isBlank(etlString)){
            return;
        }

        /**
         * 3.Package object
         * 3.封装对象
         */
        k.set(etlString);

        /**
         * 4.data input
         * 4.写入数据
         */
        context.write(k, NullWritable.get());

    }
}
```
#### 5.3.3 Create PornhubActionETLUtil.class
``` java
package com.geekparkhub.core.application.analysis.pornhub;

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
 * PornhubActionETLUtil
 * <p>
 * 过滤不合法数据 | Filter illegal data
 * 去除类别字段中的空格 | Remove spaces in the category field
 * 将\t替换成&符 | Replace \t with ampersand
 * <p>
 */

public class PornhubActionETLUtil {

    /**
     * Data cleaning Method
     * 数据清洗方法
     *
     * @param ori
     * @return
     */
    public static String getETLString(String ori) {

        /**
         * 1.Get data and cut data
         * 获取数据并切割数据
         */
        String[] split = ori.split("\t");

        /**
         * 2.Filter illegal data
         * 过滤不合法数据
         */
        if (split.length < 9) {
            return null;
        }

        /**
         * 3.Remove spaces in the category field
         * 去除类别字段中的空格
         */
        split[3] = split[3].replace(" ", "");

        /**
         * 4.Replace \t with ampersand
         * 将\t替换成&符
         */
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < split.length; i++) {
            if (i < 9) {
                // 如果字段长度相等,则不追加\t字符
                if (i == split.length - 1) {
                    sb.append(split[i]);
                } else {
                    // 如果字段长度小于9,则追加\t字符
                    sb.append(split[i] + "\t");
                }
            } else {
                // 如果字段长度相等,则不追加字符
                if (i == split.length - 1) {
                    sb.append(split[i]);
                } else {
                    // 如果字段长度小于9,则追加&字符
                    sb.append(split[i] + "&");
                }
            }
        }
        return sb.toString();
    }
}
```
#### 5.3.4 Create PornhubActionETLDriver.class
``` java
package com.geekparkhub.core.application.analysis.pornhub;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
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
 * PornhubActionETLDriver
 * <p>
 */

public class PornhubActionETLDriver implements Tool {

    Configuration configuration;

    public static void main(String[] args) throws Exception {
        int run = ToolRunner.run(new PornhubActionETLDriver(), args);
        System.out.println("Result is = " + run);
    }

    public int run(String[] args) throws Exception {
        /**
         * 1. Get the Job object
         * 1. 获取Job对象
         */
        Job job = Job.getInstance(getConf());

        /**
         * 2. Set the jar storage location
         * 2. 设置jar存储位置
         */
        job.setJarByClass(PornhubActionETLDriver.class);

        /**
         * 3. Associate Map classes
         * 3. 关联Map类
         */
        job.setMapperClass(PornhubActionETLMapper.class);

        /**
         * 4. Set the key and value types of the output data in the Mapper stage.
         * 4. 设置Mapper阶段输出数据的key与value类型
         */
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(NullWritable.class);

        /**
         * 5. Set the key and value types for the final data output
         * 5. 设置最终数据输出的key与value类型
         */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(NullWritable.class);

        /**
         * 6. Set the input path and output path
         * 6. 设置输入路径和输出路径
         */
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         * 7. Submit the Job
         * 7. 提交Job
         */
        boolean result = job.waitForCompletion(true);

        return result ? 0 : 1;
    }

    public void setConf(Configuration conf) {
        configuration = conf;
    }

    public Configuration getConf() {
        return configuration;
    }
}
```
#### 5.3.5 将ETL程序打包并上传
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/hive/project_cover/start_003.jpg)

> 创建jars目录,将jar上传到此目录中.
```
[root@systemhub711 datas]# cd core_flow/develop/project/analysis/pornhub_action/
[root@systemhub711 pornhub_action]# mkdir jars
[root@systemhub711 pornhub_action]# ll
total 8
drwxr-xr-x. 2 root root 4096 Apr  4 01:15 jars
drwxr-xr-x. 4 root root 4096 Apr  3 22:36 metadata
[root@systemhub711 pornhub_action]# cd jars
[root@systemhub711 jars]# ll
total 8
-rw-r--r--. 1 root root 6916 Apr  4 01:15 PornhubAction-1.0.jar
[root@systemhub711 jars]# 
```
#### 5.3.6 执行ETL程序
> 设置PornhubActionETLDriver主类全包名 / 设置输入路径 / 设置输出路径
```
[root@systemhub711 jars]# yarn jar PornhubAction-1.0.jar com.geekparkhub.core.application.analysis.pornhub.PornhubActionETLDriver /core_flow/develop/project/analysis/pornhub_action/metadata/pornhub_video/001 /core_flow/develop/project/analysis/pornhub_action/metadata/pornhub_video/output
INFO client.RMProxy: Connecting to ResourceManager at systemhub611/172.16.168.131:8032
INFO input.FileInputFormat: Total input paths to process : 1
INFO mapreduce.JobSubmitter: number of splits:1
INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1554299879739_0001
INFO impl.YarnClientImpl: Submitted application application_1554299879739_0001
INFO mapreduce.Job: The url to track the job: http://systemhub611:8088/proxy/application_1554299879739_0001/
INFO mapreduce.Job: Running job: job_1554299879739_0001
INFO mapreduce.Job: Job job_1554299879739_0001 running in uber mode : false
INFO mapreduce.Job:  map 0% reduce 0%
INFO mapreduce.Job:  map 100% reduce 0%
INFO mapreduce.Job:  map 100% reduce 100%
INFO mapreduce.Job: Job job_1554299879739_0001 completed successfully
INFO mapreduce.Job: Counters: 49
        File System Counters
                FILE: Number of bytes read=56878
                FILE: Number of bytes written=348933
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=56277
                HDFS: Number of bytes written=55764
                HDFS: Number of read operations=6
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
        Job Counters 
                Launched map tasks=1
                Launched reduce tasks=1
                Data-local map tasks=1
                Total time spent by all maps in occupied slots (ms)=8729
                Total time spent by all reduces in occupied slots (ms)=4809
                Total time spent by all map tasks (ms)=8729
                Total time spent by all reduce tasks (ms)=4809
                Total vcore-milliseconds taken by all map tasks=8729
                Total vcore-milliseconds taken by all reduce tasks=4809
                Total megabyte-milliseconds taken by all map tasks=8938496
                Total megabyte-milliseconds taken by all reduce tasks=4924416
        Map-Reduce Framework
                Map input records=189
                Map output records=189
                Map output bytes=56129
                Map output materialized bytes=56878
                Input split bytes=184
                Combine input records=0
                Combine output records=0
                Reduce input groups=189
                Reduce shuffle bytes=56878
                Reduce input records=189
                Reduce output records=189
                Spilled Records=378
                Shuffled Maps =1
                Failed Shuffles=0
                Merged Map outputs=1
                GC time elapsed (ms)=223
                CPU time spent (ms)=2120
                Physical memory (bytes) snapshot=297361408
                Virtual memory (bytes) snapshot=4124475392
                Total committed heap usage (bytes)=139624448
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters 
                Bytes Read=56093
        File Output Format Counters 
                Bytes Written=55764
Result is = 0
[root@systemhub711 jars]# 
```

### 5.4 创建数据库&数据表
#### 5.4.1 创建 : `pornhub_action`数据库
```
hive (default)> create database if not exists pornhub_action;
OK
Time taken: 1.06 seconds
hive (default)> show databases;
OK
database_name
pornhub_action
Time taken: 0.308 seconds, Fetched: 3 row(s)
hive (default)> use pornhub_action;
OK
Time taken: 0.043 seconds
hive (pornhub_action)>
```
#### 5.4.2 创建原数据表 : `pornhub_video_ori` / `pornhub_user_ori`
> 
> `create table pornhub_video_ori`
``` sql
hive (pornhub_action)> create table pornhub_video_ori(
                     > videoId string,
                     > uploader string,
                     > updates int,
                     > category array<string>,
                     > length int,
                     > views int,
                     > rate float,
                     > ratings int,
                     > comments int,
                     > relatedId array<string>)
                     > row format delimited
                     > fields terminated by "\t"
                     > collection items terminated by "&"
                     > stored as textfile;
OK
Time taken: 0.321 seconds
hive (pornhub_action)> 
```
> `create table pornhub_user_ori`
```
hive (pornhub_action)> create table pornhub_user_ori(
                     > uploader string,
                     > videos int,
                     > friends int)
                     > row format delimited
                     > fields terminated by "\t"
                     > stored as textfile;
OK
Time taken: 0.103 seconds
hive (pornhub_action)> 
```
> show tables
```
hive (pornhub_action)> show tables;
OK
tab_name
pornhub_user_ori
pornhub_video_ori
Time taken: 0.037 seconds, Fetched: 2 row(s)
hive (pornhub_action)> 
```
#### 5.4.3 创建列式存储数据表 : `pornhub_video_orc` / `pornhub_user_orc`
> create table pornhub_video_orc
``` sql
hive (pornhub_action)> create table pornhub_video_orc(
                     > videoId string,
                     > uploader string,
                     > updates int,
                     > category array<string>,
                     > length int,
                     > views int,
                     > rate float,
                     > ratings int,
                     > comments int,
                     > relatedId array<string>)
                     > row format delimited
                     > fields terminated by "\t"
                     > collection items terminated by "&"
                     > stored as orc;
OK
Time taken: 0.142 seconds
hive (pornhub_action)> 
```
> create table pornhub_user_orc
```
hive (pornhub_action)> create table pornhub_user_orc(
                     > uploader string,
                     > videos int,
                     > friends int)
                     > row format delimited
                     > fields terminated by "\t"
                     > stored as orc;
OK
Time taken: 0.086 seconds
hive (pornhub_action)> 
```
> show tables
```
hive (pornhub_action)> show tables;
OK
tab_name
pornhub_user_orc
pornhub_user_ori
pornhub_video_orc
pornhub_video_ori
Time taken: 0.037 seconds, Fetched: 4 row(s)
hive (pornhub_action)>
```

### 5.5 加载数据
#### 5.5.1 Load Data For `pornhub_video_ori`
```
hive (pornhub_action)> load data inpath '/core_flow/develop/project/analysis/pornhub_action/metadata/pornhub_video/output/part-r-00000' into table pornhub_video_ori;
Loading data to table pornhub_action.pornhub_video_ori
Table pornhub_action.pornhub_video_ori stats: [numFiles=1, totalSize=55764]
OK
Time taken: 0.922 seconds
hive (pornhub_action)> 
```
#### 5.5.2 Load Data For `pornhub_user_ori`
```
hive (pornhub_action)> load data inpath '/core_flow/develop/project/analysis/pornhub_action/metadata/pornhub_user/001/pornhub_user.txt' into table pornhub_user_ori;
Loading data to table pornhub_action.pornhub_user_ori
Table pornhub_action.pornhub_user_ori stats: [numFiles=1, totalSize=36498109]
OK
Time taken: 0.476 seconds
hive (pornhub_action)> 
```
#### 5.5.3 Insert Table For `pornhub_video_orc`
```
hive (pornhub_action)> insert overwrite table pornhub_video_orc
                     > select * from pornhub_video_ori;
Query ID = root_4633_abb46085-5540-42cd-8f07-c38dbb5f2b75
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 1   Cumulative CPU: 2.2 sec   HDFS Read: 60976 HDFS Write: 35178 SUCCESS
Total MapReduce CPU Time Spent: 2 seconds 200 msec
OK
pornhub_video_ori.videoid       pornhub_video_ori.uploader      pornhub_video_ori.updates       pornhub_video_ori.category      pornhub_video_ori.length  pornhub_video_ori.views pornhub_video_ori.rate  pornhub_video_ori.ratings       pornhub_video_ori.comments      pornhub_video_ori.relatedid
Time taken: 38.165 seconds
hive (pornhub_action)> 
```
#### 5.5.4 Insert Table For `pornhub_user_orc`
```
hive (pornhub_action)> insert overwrite table pornhub_user_orc
                     > select * from pornhub_user_ori;
Query ID = root_53_7e79a39b-7ca2-498e-ba34-37ecf6112423
Table pornhub_action.pornhub_user_orc stats: [numFiles=1, numRows=2139109, totalSize=18167801, rawDataSize=218189118]
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 1   Cumulative CPU: 8.17 sec   HDFS Read: 36501990 HDFS Write: 18167900 SUCCESS
Total MapReduce CPU Time Spent: 8 seconds 170 msec
OK
pornhub_user_ori.uploader       pornhub_user_ori.videos pornhub_user_ori.friends
Time taken: 33.949 seconds
hive (pornhub_action)> 
```

### 5.6 👨‍💻👩‍💻👨🏻‍💻 Start Coding ! 👨‍💻👩‍💻👨🏻‍💻
> 事先开启两个SSH窗口,StartCoding
> 
> 窗口一 : 开启服务端
```
[root@systemhub711 ~]# cd /opt/module/hive/bin/
[root@systemhub711 bin]# ./hiveserver2
OK
```
> 窗口二 : 开启客户端,并进入pornhub_action数据库.
```
[root@systemhub711 ~]# cd /opt/module/hive/
[root@systemhub711 hive]# bin/beeline
beeline> !connect jdbc:hive2://systemhub711:10000
Connecting to jdbc:hive2://systemhub711:10000
Enter username for jdbc:hive2://systemhub711:10000: root
Enter password for jdbc:hive2://systemhub711:10000: 
Connected to: Apache Hive (version 1.2.1)
Driver: Hive JDBC (version 1.2.1)
Transaction isolation: TRANSACTION_REPEATABLE_READ
0: jdbc:hive2://systemhub711:10000> show databases;
+-----------------+--+
|  database_name  |
+-----------------+--+
| default         |
| hive_db         |
| pornhub_action  |
+-----------------+--+
3 rows selected (2.303 seconds)
0: jdbc:hive2://systemhub711:10000> usr pornhub_action;
0: jdbc:hive2://systemhub711:10000> show tables;
+--------------------+--+
|      tab_name      |
+--------------------+--+
| pornhub_user_orc   |
| pornhub_user_ori   |
| pornhub_video_orc  |
| pornhub_video_ori  |
+--------------------+--+
4 rows selected (0.095 seconds)
0: jdbc:hive2://systemhub711:10000>
```

#### 5.6.1 🔥 统计视频观看数`Top5` 🔥
> 👨🏻‍💻 Coding思路 👨🏻‍💻 : 使用`order by`按照views字段全局排序即可,同时设置只显示前5条数据.
``` powershell
0: jdbc:hive2://systemhub711:10000> SSELECT
	videoid,
	uploader,
	updates,
	category,
	length,
	views,
	rate,
	ratings,
	comments 
FROM
	pornhub_video_orc 
ORDER BY
	views DESC 
	LIMIT 10;
INFO  : MapReduce Total cumulative CPU time: 4 seconds 560 msec
INFO  : Ended Job = job_1554353095768_0005
+--------------+------------------+----------+--------------------+---------+-----------+--------------------+----------+-----------+--+
|   videoid    |     uploader     | updates  |      category      | length  |   views   |        rate        | ratings  | comments  |
+--------------+------------------+----------+--------------------+---------+-----------+--------------------+----------+-----------+--+
| dMH0bHeiRNg  | judsonlaipply    | 415      | ["Comedy"]         | 360     | 42513417  | 4.679999828338623  | 87520    | 22718     |
| 0XxI-hvPRRA  | smosh            | 286      | ["Comedy"]         | 194     | 20282464  | 4.489999771118164  | 80710    | 35408     |
| 1dmVU08zVpA  | NBC              | 670      | ["Entertainment"]  | 165     | 16087899  | 4.789999961853027  | 30085    | 5945      |
| RB-wUgnyGv0  | ChrisInScotland  | 506      | ["Entertainment"]  | 159     | 15712924  | 4.78000020980835   | 8222     | 1996      |
| QjA5faZF1A8  | guitar90         | 308      | ["Music"]          | 320     | 15256922  | 4.840000152587891  | 120506   | 38393     |
+--------------+------------------+----------+--------------------+---------+-----------+--------------------+----------+-----------+--+
5 rows selected (42.078 seconds)
0: jdbc:hive2://systemhub711:10000> 
```
#### 5.6.1.2 🔥 统计视频类别热度`Top10` 🔥
> 👨🏻‍💻 Coding思路 👨🏻‍💻 : 
> 即统计每个类别有视频数量,显示出包含视频最多前10个类别.
> 需要按照类别`group by`聚合,然后`count`组内videoId个数即可.
> 当前表结构为,一个视频对应一个或多个类别,所以如果要`group by`类别,需要先将类别进行列转行(展开),然后再进行count,最后按照热度排序,显示前10条.
``` sql
0: jdbc:hive2://systemhub711:10000> 
SELECT
	category_name AS category,
	count(pronhub.videoId) AS hot 
FROM
	(
	SELECT
		videoId,
		category_name 
	FROM
		pornhub_video_orc lateral VIEW explode (category) t_catetory AS category_name 
	) pronhub 
GROUP BY
	pronhub.category_name 
ORDER BY
	hot DESC 
	LIMIT 10;
INFO  : Number of reduce tasks not specified. Estimated from input data size: 1
INFO  : MapReduce Total cumulative CPU time: 3 seconds 900 msec
INFO  : Ended Job = job_1554353095768_0007
+----------------+------+--+
|    category    | hot  |
+----------------+------+--+
| Comedy         | 46   |
| Entertainment  | 41   |
| Music          | 23   |
| Film           | 21   |
| Animation      | 21   |
| Blogs          | 20   |
| People         | 20   |
| Politics       | 16   |
| News           | 16   |
| Sports         | 9    |
+----------------+------+--+
10 rows selected (79.143 seconds)
0: jdbc:hive2://systemhub711:10000> 
```
#### 5.6.1.3 🔥 统计视频观看数`Top20`所属类别 🔥
> 👨🏻‍💻 Coding思路 👨🏻‍💻 : 
> 先找到观看数最高20个视频所属条目的所有信息,降序排列.
> 将20条信息中的`category`分裂出来(列转行),最后查询视频分类名称和该分类下有多少个Top20的视频.
```
0: jdbc:hive2://systemhub711:10000> 
SSELECT
	category_name AS category,
	count(pronhub2.videoId) AS hot_with_views 
FROM
	(
	SELECT
		videoId,
		category_name 
	FROM
		(
		SELECT
			* 
		FROM
			pornhub_video_orc 
		ORDER BY
			views DESC 
			LIMIT 20 
		) pronhub1 lateral VIEW explode (category) t_catetory AS category_name 
	) pronhub2 
GROUP BY
	category_name 
ORDER BY
	hot_with_views DESC;
INFO  : Number of reduce tasks determined at compile time: 1
INFO  : MapReduce Total cumulative CPU time: 3 seconds 580 msec
INFO  : Ended Job = job_1554353095768_0010
+----------------+-----------------+--+
|    category    | hot_with_views  |
+----------------+-----------------+--+
| Entertainment  | 6               |
| Comedy         | 6               |
| Music          | 5               |
| People         | 2               |
| Blogs          | 2               |
| UNA            | 1               |
+----------------+-----------------+--+
6 rows selected (109.713 seconds)
0: jdbc:hive2://systemhub711:10000> 
```
#### 5.6.1.4 🔥 统计视频观看数`Top50`所关联视频的所属类别Rank 🔥
> 👨🏻‍💻 Coding思路 👨🏻‍💻 : 
> 查询观看数最多的前50个视频所有信息(包含每个视频对应的关联视频),记为临时表pronhub1
> 将找到的50条视频信息相关视频`relatedId`列转行,记为临时表pronhub2
> 将相关视频id和pornhub_video_orc表进行`inner join`操作.
> 按照视频类别进行分组,统计每组视频个数,然后排行.
> 
> 1.pronhub1 : 观看数前50视频.
``` sql
0: jdbc:hive2://systemhub711:10000>
SELECT
	* 
FROM
	pornhub_video_orc 
ORDER BY
	views DESC 
	LIMIT 50;
INFO  : Number of reduce tasks determined at compile time: 1
```
> 2.pronhub2 : 将相关视频的id进行列转行操作.
``` sql
0: jdbc:hive2://systemhub711:10000>
SELECT
	explode ( relatedId ) AS videoId
FROM
	pornhub1;
INFO  : Number of reduce tasks determined at compile time: 1
```

> 3.将相关视频的id和youtube_orc表进行inner join操作
``` sql
0: jdbc:hive2://systemhub711:10000>
(SELECT DISTINCT
	(pornhub2.videoId),
	pornhub3.category 
	FROM
		pornhub2
	INNER JOIN pornhub_video_orc pornhub3 ON pornhub2.videoId = pornhub3.videoId 
	) pornhub4 lateral VIEW explode (category) t_catetory AS category_name;
INFO  : Number of reduce tasks determined at compile time: 1
```

> 4.按照视频类别进行分组,统计每组视频个数,然后排行.
``` sql
0: jdbc:hive2://systemhub711:10000>
SELECT
	category_name AS category,
	count(pronhub5.videoId) AS hot 
FROM
	(
	SELECT
		videoId,
		category_name 
	FROM
		(
		SELECT DISTINCT
			(pronhub2.videoId),
			pronhub3.category 
		FROM
			(
			SELECT
				explode (relatedId) AS videoId 
			FROM
				(
				SELECT
					* 
				FROM
					pornhub_video_orc 
				ORDER BY
					views DESC 
					LIMIT 50 
				) pronhub1 
			) pronhub2
			INNER JOIN pornhub_video_orc pronhub3 ON pronhub2.videoId = pronhub3.videoId 
		) pronhub4 lateral VIEW explode (category) t_catetory AS category_name 
	) pronhub5 
GROUP BY
	category_name 
ORDER BY
	hot DESC;
INFO  : Number of reduce tasks determined at compile time: 1

INFO  : MapReduce Total cumulative CPU time: 3 seconds 60 msec
INFO  : Ended Job = job_1554353095768_0015
+----------------+------+--+
|    category    | hot  |
+----------------+------+--+
| Music          | 5    |
| Entertainment  | 5    |
| Comedy         | 3    |
| Film           | 2    |
| Animation      | 2    |
| Sports         | 1    |
| Games          | 1    |
| Gadgets        | 1    |
+----------------+------+--+
8 rows selected (140.911 seconds)
0: jdbc:hive2://systemhub711:10000>
```


#### 5.6.1.5 🔥 统计每个类别中视频热度`Top10` 🔥
> 👨🏻‍💻 Coding思路 👨🏻‍💻 : 
> 要想统计Music类别中视频热度Top10,需要先找到Music类别,那么就需要将`category`展开,所以可以创建一张表用于存放categoryId展开的数据,并向`category`展开表中插入数据,统计对应类别(Music)中视频热度.
> 
> 创建表 (pornhub_category / 类别表)
``` sql
0: jdbc:hive2://systemhub711:10000> 
CREATE TABLE pornhub_category(
	videoId string,
	uploader string,
	updates int,
	categoryId string,
	length int,
	views int,
	rate float,
	ratings int,
	comments int,
relatedId array <string> 
) ROW format delimited FIELDS TERMINATED BY "\t"
collection items TERMINATED BY "&"
stored AS orc;
No rows affected (0.283 seconds)
0: jdbc:hive2://systemhub711:10000> 
```
> 向类别表中插入数据
``` sql
0: jdbc:hive2://systemhub711:10000>
INSERT INTO TABLE pornhub_category
SELECT
videoId,
uploader,
updates,
categoryId,
length,
views,
rate,
ratings,
comments,
relatedId 
FROM
	pornhub_video_orc lateral VIEW explode (category) catetory AS categoryId;
INFO  : Number of reduce tasks is set to 0 since there's no reduce operator
INFO  : number of splits:1
0: jdbc:hive2://systemhub711:10000> show tables;
+--------------------+--+
|      tab_name      |
+--------------------+--+
| pornhub_category   |
| pornhub_user_orc   |
| pornhub_user_ori   |
| pornhub_video_orc  |
| pornhub_video_ori  |
+--------------------+--+
5 rows selected (0.044 seconds)
0: jdbc:hive2://systemhub711:10000> 
```
> 统计Music类别Top10
``` sql
0: jdbc:hive2://systemhub711:10000>
SELECT
	videoId,
	views 
FROM
	pornhub_category 
WHERE
	categoryId = "Music" 
ORDER BY
	views DESC 
	LIMIT 10;
INFO  : Number of reduce tasks determined at compile time: 1
INFO  : MapReduce Total cumulative CPU time: 3 seconds 880 msec
INFO  : Ended Job = job_1554353095768_0019
+--------------+-----------+--+
|   videoid    |   views   |
+--------------+-----------+--+
| QjA5faZF1A8  | 15256922  |
| tYnn51C3X_w  | 11823701  |
| pv5zWaTEVkI  | 11672017  |
| 8bbTtPL1jRs  | 9579911   |
| UMf40daefsI  | 7533070   |
| seGhTWE98DU  | 3296342   |
| Ddn4MGaS3N4  | 2417724   |
| OMndH4egfSk  | 1258781   |
| AbndgwfG22k  | 1069404   |
| OUi9-jqq_i0  | 862371    |
+--------------+-----------+--+
10 rows selected (31.534 seconds)
0: jdbc:hive2://systemhub711:10000> 
```


#### 5.6.1.6 🔥 统计每个类别中视频流量`Top10` 🔥
> 👨🏻‍💻 Coding思路 👨🏻‍💻 : 
> 创建视频类别展开表(`categoryId`列转行后的表),按照ratings排序即可.
``` sql
0: jdbc:hive2://systemhub711:10000>
SELECT
	videoId,
	views,
	ratings 
FROM
	pornhub_category 
WHERE
	categoryId = "Music" 
ORDER BY
	ratings DESC 
	LIMIT 10;
INFO  : Number of reduce tasks determined at compile time: 1
INFO  : MapReduce Total cumulative CPU time: 3 seconds 860 msec
INFO  : Ended Job = job_1554353095768_0020
+--------------+-----------+----------+--+
|   videoid    |   views   | ratings  |
+--------------+-----------+----------+--+
| QjA5faZF1A8  | 15256922  | 120506   |
| pv5zWaTEVkI  | 11672017  | 42386    |
| UMf40daefsI  | 7533070   | 31886    |
| tYnn51C3X_w  | 11823701  | 29479    |
| Ddn4MGaS3N4  | 2417724   | 18998    |
| seGhTWE98DU  | 3296342   | 13657    |
| crfrKqFp0Zg  | 824902    | 6816     |
| OUi9-jqq_i0  | 862371    | 5640     |
| 8bbTtPL1jRs  | 9579911   | 5352     |
| O9mEKMz2Pvo  | 632893    | 4779     |
+--------------+-----------+----------+--+
10 rows selected (29.872 seconds)
0: jdbc:hive2://systemhub711:10000> 
```


#### 5.6.1.7 🔥 统计上传视频最多的用户`Top10`以及相关视频 🔥
> 👨🏻‍💻 Coding思路 👨🏻‍💻 : 
> 先找到上传视频最多的10个用户的用户信息,通过`uploader`字段与pornhub_video_orc表进行join,得到的信息按照views观看次数进行排序即可.
> 
> 查询上传视频最多的10个用户的用户信息
``` sql
0: jdbc:hive2://systemhub711:10000> 
SELECT
	* 
FROM
	pornhub_user_orc 
ORDER BY
	videos DESC 
	LIMIT 10;
INFO  : Number of reduce tasks determined at compile time: 1
INFO  : MapReduce Total cumulative CPU time: 13 seconds 10 msec
INFO  : Ended Job = job_1554353095768_0024
+----------------------------+--------------------------+---------------------------+--+
| pornhub_user_orc.uploader  | pornhub_user_orc.videos  | pornhub_user_orc.friends  |
+----------------------------+--------------------------+---------------------------+--+
| expertvillage              | 86228                    | 5659                      |
| TourFactory                | 49078                    | 0                         |
| myHotelVideo               | 33506                    | 102                       |
| AlexanderRodchenko         | 24315                    | 22                        |
| VHTStudios                 | 20230                    | 3                         |
| ephemeral8                 | 19498                    | 11                        |
| HSN                        | 15371                    | 309                       |
| rattanakorn                | 12637                    | 677                       |
| Ruchaneewan                | 10059                    | 774                       |
| futifu                     | 9668                     | 118                       |
+----------------------------+--------------------------+---------------------------+--+
10 rows selected (45.521 seconds)
0: jdbc:hive2://systemhub711:10000> 
```
> 通过uploader字段与pornhub_video_orc表进行join,得到的信息按照views观看次数进行排序即可.
``` sql
0: jdbc:hive2://systemhub711:10000>
SELECT
	pornhub2.videoId,
	pornhub2.views,
	pornhub2.ratings,
	pornhub1.videos,
	pornhub1.friends 
FROM
	(
	SELECT
		* 
	FROM
		pornhub_user_orc 
	ORDER BY
		videos DESC 
		LIMIT 10 
	) pornhub1
	JOIN pornhub_video_orc pornhub2 ON pornhub1.uploader = pornhub2.uploader 
ORDER BY
	views DESC 
	LIMIT 20;
INFO  : Number of reduce tasks determined at compile time: 1
```

#### 5.6.1.8 🔥 统计每个类别视频观看数`Top10` 🔥
> 👨🏻‍💻 Coding思路 👨🏻‍💻 : 
> 先得到categoryId展开的表数据,子查询按照categoryId进行分区,然后分区内排序,并生成递增数字,该递增数字这一列起名为rank列,通过子查询产生的临时表,查询rank值小于等于10的数据行即可.
``` sql
0: jdbc:hive2://systemhub711:10000>
SELECT
	pronhub1.* 
FROM
	(
	SELECT
		videoId,
		categoryId,
		views,
		row_number () over (PARTITION BY categoryId ORDER BY views DESC) rank 
	FROM
		pornhub_category 
	) pronhub1 
WHERE
	rank <= 10;
INFO  : MapReduce Total cumulative CPU time: 4 seconds 30 msec
INFO  : Ended Job = job_1554353095768_0023
+-------------------+----------------------+-----------------+----------------+--+
| pronhub1.videoid  | pronhub1.categoryid  | pronhub1.views  | pronhub1.rank  |
+-------------------+----------------------+-----------------+----------------+--+
| LHyJH1yGKZY       | Animals              | 1085020         | 1              |
| Qz_nZixWX6Q       | Animals              | 1027067         | 2              |
| yg2enZsknZM       | Animals              | 2429            | 3              |
| sdUUx5FdySs       | Animation            | 5840839         | 1              |
| 6B26asyGKDo       | Animation            | 5147533         | 2              |
| JzqumbhfxRo       | Animation            | 3230774         | 3              |
| ElrldD02if0       | Animation            | 2337238         | 4              |
| Gm6XszMrw9Y       | Animation            | 1227020         | 5              |
| hBRjiLPNJAA       | Animation            | 927340          | 6              |
| zRVts7TFw-Y       | Animation            | 607456          | 7              |
| Jy09vLHkIes       | Animation            | 544237          | 8              |
| bqZauhidT1w       | Animation            | 374550          | 9              |
| A0eZ9qkUvJU       | Animation            | 351288          | 10             |
| pdiuDXwgrjQ       | Autos                | 1013697         | 1              |
| zgpbblz9wHw       | Autos                | 11322           | 2              |
| -_CSo1gOd48       | Blogs                | 13199833        | 1              |
| D2kJZOfq7zk       | Blogs                | 11184051        | 2              |
| PL4Uzun4CKA       | Blogs                | 1235410         | 3              |
| kzwa8NBlUeo       | Blogs                | 759912          | 4              |
| 5LELNIVyMqo       | Blogs                | 635085          | 5              |
| ihhEp3uTZck       | Blogs                | 533936          | 6              |
| f9_oaKYFM0c       | Blogs                | 328022          | 7              |
| TweU77cDrgE       | Blogs                | 318045          | 8              |
| H-ucblRMjuY       | Blogs                | 299935          | 9              |
| LfAaY1p_2Is       | Blogs                | 168389          | 10             |
| dMH0bHeiRNg       | Comedy               | 42513417        | 1              |
| 0XxI-hvPRRA       | Comedy               | 20282464        | 2              |
| 49IDp76kjPw       | Comedy               | 11970018        | 3              |
| 5P6UU6m3cqk       | Comedy               | 10107491        | 4              |
| _BuRwH59oAo       | Comedy               | 9566609         | 5              |
| MNxwAU_xAMk       | Comedy               | 7066676         | 6              |
| N0TR0Irx4Y0       | Comedy               | 3836122         | 7              |
| CQO3K8BcyGM       | Comedy               | 3083875         | 8              |
| P1OXAQHv09E       | Comedy               | 3068566         | 9              |
| nojWJ6-XmeQ       | Comedy               | 2667887         | 10             |
| 6gmP4nk0EOE       | DIY                  | 1353059         | 1              |
| 1dmVU08zVpA       | Entertainment        | 16087899        | 1              |
| RB-wUgnyGv0       | Entertainment        | 15712924        | 2              |
| vr3x_RRJdd4       | Entertainment        | 10786529        | 3              |
| lsO6D1rwrKc       | Entertainment        | 10334975        | 4              |
| ixsZy2425eY       | Entertainment        | 7456875         | 5              |
| RUCZJVJ_M8o       | Entertainment        | 6952767         | 6              |
| 3gg5LOd_Zus       | Entertainment        | 4200257         | 7              |
| o4x-VW_rCSE       | Entertainment        | 3534116         | 8              |
| tScm-eZInBE       | Entertainment        | 2675254         | 9              |
| IsyWlcQAy-Q       | Entertainment        | 2486628         | 10             |
| sdUUx5FdySs       | Film                 | 5840839         | 1              |
| 6B26asyGKDo       | Film                 | 5147533         | 2              |
| JzqumbhfxRo       | Film                 | 3230774         | 3              |
| ElrldD02if0       | Film                 | 2337238         | 4              |
| Gm6XszMrw9Y       | Film                 | 1227020         | 5              |
| hBRjiLPNJAA       | Film                 | 927340          | 6              |
| zRVts7TFw-Y       | Film                 | 607456          | 7              |
| Jy09vLHkIes       | Film                 | 544237          | 8              |
| bqZauhidT1w       | Film                 | 374550          | 9              |
| A0eZ9qkUvJU       | Film                 | 351288          | 10             |
| 7wt5FiZQrgM       | Gadgets              | 1399531         | 1              |
| wwLrgxtALWs       | Gadgets              | 584871          | 2              |
| 7wt5FiZQrgM       | Games                | 1399531         | 1              |
| wwLrgxtALWs       | Games                | 584871          | 2              |
| 6gmP4nk0EOE       | Howto                | 1353059         | 1              |
| QjA5faZF1A8       | Music                | 15256922        | 1              |
| tYnn51C3X_w       | Music                | 11823701        | 2              |
| pv5zWaTEVkI       | Music                | 11672017        | 3              |
| 8bbTtPL1jRs       | Music                | 9579911         | 4              |
| UMf40daefsI       | Music                | 7533070         | 5              |
| seGhTWE98DU       | Music                | 3296342         | 6              |
| Ddn4MGaS3N4       | Music                | 2417724         | 7              |
| OMndH4egfSk       | Music                | 1258781         | 8              |
| AbndgwfG22k       | Music                | 1069404         | 9              |
| OUi9-jqq_i0       | Music                | 862371          | 10             |
| bfZ_gXCHaMw       | News                 | 1039066         | 1              |
| 4G-D0F4Q9yk       | News                 | 882123          | 2              |
| zx2ytr2Oyv4       | News                 | 647446          | 3              |
| qmjvSM3x86o       | News                 | 535103          | 4              |
| qHO8l-Bd1O4       | News                 | 425284          | 5              |
| CmO3voBR3SE       | News                 | 158585          | 6              |
| JwAtNILh6uY       | News                 | 77817           | 7              |
| bVGRc5b3iD4       | News                 | 77065           | 8              |
| K4u3KNo2bs8       | News                 | 40268           | 9              |
| OKpyYdpiT88       | News                 | 34275           | 10             |
| -_CSo1gOd48       | People               | 13199833        | 1              |
| D2kJZOfq7zk       | People               | 11184051        | 2              |
| PL4Uzun4CKA       | People               | 1235410         | 3              |
| kzwa8NBlUeo       | People               | 759912          | 4              |
| 5LELNIVyMqo       | People               | 635085          | 5              |
| ihhEp3uTZck       | People               | 533936          | 6              |
| f9_oaKYFM0c       | People               | 328022          | 7              |
| TweU77cDrgE       | People               | 318045          | 8              |
| H-ucblRMjuY       | People               | 299935          | 9              |
| LfAaY1p_2Is       | People               | 168389          | 10             |
| LHyJH1yGKZY       | Pets                 | 1085020         | 1              |
| Qz_nZixWX6Q       | Pets                 | 1027067         | 2              |
| yg2enZsknZM       | Pets                 | 2429            | 3              |
| bNF_P281Uu4       | Places               | 5231539         | 1              |
| _5QUdvUhCZc       | Places               | 819974          | 2              |
| MEvoy_owET8       | Places               | 109673          | 3              |
| bfZ_gXCHaMw       | Politics             | 1039066         | 1              |
| 4G-D0F4Q9yk       | Politics             | 882123          | 2              |
| zx2ytr2Oyv4       | Politics             | 647446          | 3              |
+-------------------+----------------------+-----------------+----------------+--+
| pronhub1.videoid  | pronhub1.categoryid  | pronhub1.views  | pronhub1.rank  |
+-------------------+----------------------+-----------------+----------------+--+
| qmjvSM3x86o       | Politics             | 535103          | 4              |
| qHO8l-Bd1O4       | Politics             | 425284          | 5              |
| CmO3voBR3SE       | Politics             | 158585          | 6              |
| JwAtNILh6uY       | Politics             | 77817           | 7              |
| bVGRc5b3iD4       | Politics             | 77065           | 8              |
| K4u3KNo2bs8       | Politics             | 40268           | 9              |
| OKpyYdpiT88       | Politics             | 34275           | 10             |
| 7vL19q8yL54       | Sports               | 2527713         | 1              |
| u2pW7PSyZhw       | Sports               | 1160798         | 2              |
| K5saBDOE6Sc       | Sports               | 236918          | 3              |
| sMEnn0xJ0l0       | Sports               | 223511          | 4              |
| -keC9GymLpI       | Sports               | 99425           | 5              |
| ztIH6tc6Aa4       | Sports               | 61128           | 6              |
| cn34xQU2M94       | Sports               | 53556           | 7              |
| YpOnJBL6Ky0       | Sports               | 24643           | 8              |
| F9qvkMq7EIE       | Sports               | 22309           | 9              |
| bNF_P281Uu4       | Travel               | 5231539         | 1              |
| _5QUdvUhCZc       | Travel               | 819974          | 2              |
| MEvoy_owET8       | Travel               | 109673          | 3              |
| aRNzWyD7C9o       | UNA                  | 8825788         | 1              |
| 3jLRNiK6oWY       | UNA                  | 663407          | 2              |
| pdiuDXwgrjQ       | Vehicles             | 1013697         | 1              |
| zgpbblz9wHw       | Vehicles             | 11322           | 2              |
+-------------------+----------------------+-----------------+----------------+--+
123 rows selected (32.988 seconds)
0: jdbc:hive2://systemhub711:10000> 
```


## 5.7. 修仙之道 技术架构迭代 登峰造极之势
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