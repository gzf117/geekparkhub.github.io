# 大数据生态系统 修仙之路 Shell Blog

@(2019-01-14)[Programing Language:Shell|GeekDeveloper:JEEP-711|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)]


![Alt text](./nopic.jpg)

- **极客实验室是极客国际公园旗下为未来而构建的极客社区；**
- **我们正在构建一个活跃的小众社区,汇聚众多优秀开发者与设计师；**
- **关注极具创新精神的前沿技术&分享交流&项目合作机会等互联网行业服务；**
- **Future Vision : Establishment of the Geek Foundation**
- **Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见！**
- **GeekParkHub GithubHome：**<https://github.com/geekparkhub>
- **GeekParkHub GiteeHome：**<https://gitee.com/geekparkhub>

-------------------

[TOC]

## shell 简介

> Shell脚本(英语：Shell script),又称Shell命令稿、程序化脚本,是一种计算机程序使用的文本文件,内容由一连串的shell命令组成,经由Unix Shell直译其内容后运作,被当成是一种脚本语言来设计,其运作方式与解释型语言相当,由Unix shell扮演命令行解释器的角色,在读取shell脚本之后,依序运行其中的shell命令,之后输出结果,利用shell脚本可以进行系统管理,文件操作等.在Unix及所有的类Unix系统中,如Linux、FreeBSD等操作系统,都存在shell脚本,依照Unix shell的各种不同类型,shell脚本也有各种不同方言,在DOS、OS/2、Microsoft Windows中的批处理文件,跟shell脚本有类似的功能 .   —— [维基百科](https://zh.wikipedia.org/wiki/Shell%E8%84%9A%E6%9C%AC)

## Shell 编程概述
> linux运维工程师在进行服务器集群管理时,需要编写shell程序来进行服务器管理
> 对java和python开发者来说,工作的需要,可能会编写shell脚本进行程序或者服务器维护
> 比如编写一个定时备份数据库的脚本,对于大数据开发者来说,需要编写shell程序来管理集群

## shell 工作原理 
> 外层应用程序调用shell,shell调用linux内核,linux内核调用驱动硬件

## Shell 既是命令解释器
> 它为用户提供一个向linux内核发送请求以便运行程序的界面系统程序,用户可以使用
> Shell是一个命令行解释器,它接收应用从程序/用户命令,然后调用操作系统内核
> shell启动/挂起/停止/甚是编写一些程序

## shell 快速入门
### shell 脚本执行方式 & 脚本格式要求
脚本以**`#!/bin/bash`** 开头
脚本需要有(x)可执行权限
### shell入门应用案例
#### 编写第一个 HelloWorld Shell脚本
1.创建一个shell脚本,输出HelloWorld!
```
[root@corehub]# vim HelloWorld.sh
```
2.输入**`i`**,进入编辑模式
```
echo "Hello World!"
~                                                                               
~                                                         
```
3.按esc键,写入设置并退出
```
echo "Hello World!"
~                                                                               
~                                                                               
:wq
```
### 脚本常用执行方式
#### 方式一:输入脚本绝对路径或相对路径
```
chmod 744 
./ .sh 执行脚本
```
#### 方式二:(sh+脚本)
```
sh ./ .sh
不用赋予脚本权限,直接执行即可
```

## shell 变量
### linux shell变量分为 系统变量和用户自定义变量
系统变量 **`$HOME`** **`$PWD`** **`$SHELL`** **`$USER`**等等
比如**`echo $HOME`**等等
显示当前shell中所有的变量 **`:set`**

### 定义变量规则
变量名称可以有**`字母`**、**`数字`**、**`下划线`**组成,但不能以**`数字开头`**
等号两侧不能有空格
变量名一般习惯大写风格
将命令的返回值赋给变量
A=`ls -la` 反引号,运行里面的命令,并把结果返回给变量A
A=$(ls -la) 等价于反引号

### shell变量定义
定义变量: **`变量 = 值`**
撤销变量: **`unset 变量`**
声明静态变量: **`readonly 变量`**,注意 不能unset
#### 变量定义 快速入门案例
##### 输出系统预变量
```
echo "PATH=$PATH"
echo "user=$USER"
```
##### 定义变量A
```
A=100 echo "A=$A"
```
##### 撤销变量A
```
unset A echo "A=$A"
```
##### 声明静态变量B=2,不能unset
```
readonly A=99 echo "A=$A"
```
##### 可把变量提升为全局环境变量,可提供其他shell程序使用
##### 多行注释:  
```
:<<!dwdwdwqed!
```
#### 设置环境变量
**`export 变量名=变量值 / 将shell变量输出为环境变量`**
**`source 配置文件 / 让修改后的配置信息立即生效`**
**`echo $变量名 / 查询环境变量的值`**
##### 设置环境变量快速入门
###### 在/etc/profile文件中定义TOMCAT_HOME环境变量
```
vim /etc/profile
TOMCAT_HOME=/opt/tomcat
export $TOMCAT_HOME
```
###### 查看环境变量TOMCAT_HOME的值
```
source /opt/profile
echo $TOMCAT_HOME
```
###### 在另外一个shell程序中使用TOMCAT_HOME
```
echo "tomcathome=$TOMCAT_HOME"
注意:在输出JAVA_HOME环境变量前,需要让其生效 source/etc/profile
```

#### 位置参数变量
> 当执行shell脚本时,如果希望获取到命令行参数信息,就可以使用到位置参数变量
> 比如: ./myshell100 200,这个就是一个执行shell的命令行,可以在myshell脚本中获取参数信息
##### 基本语法
**`$n`** (n为数字,$0代表命令本身,$1-$9代表第一到第九个参数,十以上的参数需要用花括号包含,如${10})
**`$*`** (这个变量代表命令行中所有的参数,$*把所有的参数看成一个整体)
**`$@`** (这个变量也代表命令行中给所有的参数,不过$@把每个参数区分对待)
**`$#`** (这个变量代表命令行中所有参数的个数)
##### 位置参数变量应用案例
###### 编写一个shell脚本,positionPara.sh,在脚本中获取命令行的各个参数信息
```
#!/bin/bash
#获取整个参数
echo "$0 $1 $2"
echo "$*"
echo "$@"
echo "参数个数=$#"
```
:wq保存退出
执行 sh positionPara.sh 30 60
```
positionPara.sh 30 60
30 60
30 60
参数个数=2
```

#### 预定义变量
> 就是shell设计者事先已经定义好的变量,可以直接在shell脚本中使用
##### 基本语法
**`$$`** (当前进程的进程号PID)
**`$!`** (后台运行的最后一个进程的进程号PID)
**`$?`** (最后一次执行的命令的返回状态,如果这个变量值为0,证明上一个命令正确执行,
如果这个变量的值为非0,具体是哪个数,由命自己来决定,则证明上一个命令执行不正确)
##### 预定义变量应用实例
###### 在一个shell脚本中简单实用一下预定义变量
```
vim preVar.sh
echo "当前进程号=$$"
#后台方式运行 myShell.sh
./myShell.sh &
echo "最后的进程号=$!"
echo "执行值 0为正确 非0不正确 =$?"
```

## shell 运算符
> 学习如何在shell中进行各种运算操作
### 基本语法
1. `$((运算式)) 或 $[运算式]`
2.`expr m + n 加法注意expr运算符间要有空格`
3.`expr m - n 减法`
4.`expr \*乘 /除 %取余`

### 运算符应用案例
#### 计算 (2+3) x 4 的值
##### 第一种计算方式 **`$(())`**
```
vim number.sh
NUMBER=$(((3+2)*4))
echo "NUMBER=$NUMBER"
NUMBER=20
```
##### 第二种计算方式 **`$[]`**
请求命令行的两个参数的和
```
NUMBERTOW=$[(2+3)*4]
echo "NUMBERTOW=$NUMBER"
NUMBERTOW=20
3.使用expr
4.求出两个参数的和
SUM=$[$1+$2]
echo "sum=$SUM"
```
## shell 条件判断
### 判断语句
**`[ condition ] (注意condition前后要有空格)`**
非空返回true,可使用**`$?`**验证 (0为true,1>为false)
### 常用判断语句
#### 1.两个整数的比较
**`=`** 字符串比较
**`-lt`** 小于
**`-le`** 小于等于
**`-eq`** 等价
**`-gt`** 大于
**`-ge`** 大于等于
**`-ne`** 不等于
#### 2.按照文件权限进行判断
**`-r`** 有读权限
**`-w`** 有写权限
**`-x`** 有执行权限
#### 3.按照文件类型进行判断
**`-f`** 文件存在并且是一个常规文件
**`-e`** 文件存在
**`-d`** 文件存在病史一个目录
#### 4.条件判断 应用实例
##### ok是否等于ok,判断语句
```
#!/bin/bash
if [ "ok" = "ok"]
then
    echo "Equal"
 fi
```
##### 23是都大于等于22,判断语句
```
#!/bin/bash
if[23 -gt 23]
then 
    echo  "Greater than"
fi
```
##### /root/install.log目录中的文件是否存在,判断语句
```
#!/bin/bash
if [ - e /root/install.log ]
then 
        echo "Existence"
fi
```

## shell 流程控制
### 流程控制 基本语法
```
if 判断
基本语句
if[条件判断式];then
程序
fi
```
或者
```
elif[条件判断式]
then 
程序
fi
```
> 注意事项:[条件判断式] 中括号和条件判断之间必须有空格
> 推荐使用第二种方式

### 流程控制应用案例
#### 请编写一个shell程序,如果输入的参数,大于等于60,则输出及格,如果小于60则不及格
1.创建equal.sh指令
```
touch equal.sh
```
2.编写equal.sh指令
```
vim equal.sh
```
3.写入Code Content
```
#!/bin/bash
if [ $1 -ge 60 ]
then
    echo "Congratulations on your passing grades!"
elif [ $1 -lt 60 ]
then 
    echo "I'm sorry, but I failed."
fi
```
4.Esc键退出,并输入**`:wq`**写入并退出
5.更改sh文件可执行权限
```
chmod 744 equal.sh
```
6.执行脚本equal.sh
```
#执行当前脚本并输入60 sh equal.sh 60
[root@corehub]# sh equal.sh 60
Congratulations on your passing grades!
```
```
#执行当前脚本并输入50 sh equal.sh 60
[root@corehub]# sh equal.sh 50
I'm sorry, but I failed.
```

## case语句
### 基本语法
```
case $变量名 in
"值1")
如果变量值等于1,则执行程序1
;;
"值2")
如果变量值等于2,则执行程序2
;;
esac
```
### case语句应用案例
#### 当命令行接受参数是1时,输出周一,是2输出周二,其他情况输出Other
```
#!/bin/bash
case $1 in
"1")
echo "Monday"
;;
"2")
echo "Tuesday"
;;
*)
echo "Other"
;;
esac
```

## for循环
### 基本语法
```
for 变量  in 值1 值2 值3...
do
    程序
done
```
### 基本语法2
```
for ((初始值;循环控制条件;变量变化))
do
程序
done
```
### for循环应用案例
#### 打印命令行输入参数
```
#使用$*方式
#!/bin/bash
for i in "$*"
do 
    echo "The number is $i"
done
```
```
#使用$@方式
#!/bin/bash
for i in "$@"
do 
    echo "The number is $i"
done
```
#### 从1加到100的值输出显示
```
#!/bin/bash
SUM=0
for((i=1;i<=100;i++))
do
    SUM=$[ $SUM+$i ]
done
    echo "sum=$SUM"
```

## while循环
### 基本语法
```
while [ 条件判断式 ]
do 
    程序
done
```
### while循环应用案例
#### 从一个命令行输入一个数n,统计从1+..n的值是多少
```
#!/bin/bash
SUM=0
i=0
while [ $i -le $1]
do
        SUM=$[ $SUM+$i ]
        i=$[ $i+1 ]
done
echo "sum=$SUM"
```

## read读取控制台输入
### 基本语句
```
read 选择 参数
```
### 选项参数
**`-p`** 指定读取值时的提示符
**`-t`** 指定读取值时等待时间(秒),如果没有在指定的时间内输入,就不在等待
### read应用案例
#### 读取控制台输入一个num值
```
read -p "请输入一个Num=" NUMBER
echo "当前输入的Num=$NUMBER"
```
#### 读取控制台输入一个num值,在10秒内输入
```
read -p "请在10秒内输入一个NUM：" -t 10 NUMBER
echo "当前输入的Num=$NUMBER"
```
## shell 函数
### 函数介绍
> shell编程和其他编程语言一样,有系统函数,也可以自定义函数
### 系统函数
#### basename 基本语法
功能:返回完整路径最后/部分,常用于获取文件名
**`basename pathname suffix`**
功能描述:basename命令会删掉所有的前缀包括最后一个/字符,然后将字符串显示打印
选项suffix为后缀,如果suffix被指定了,basename会将pathname或string中的suffix去掉
#### basename 应用案例
请返回/home/aaa/test.txt的test.txt部分
```
basename /home/aaa/test.txt
```
#### dirname函数
功能:返回完整路径最后/的前部分,常用语返回路径部分
dir文件绝对路径(功能:从给定的包含绝对路径的文件名去除文件(非目录部分)然后返回剩下的路径)
#### dirname应用案例
1.返回/home/aaa/test.txt的home/aaa
```
dirname /home/aaa/test.txt
```

### 自定义函数
#### 基本语法
```
[ function ] funname[()]
{ 
    Action;
    [return int;] 
}
调用直接写函数名:funname [值]
```
#### 自定义函数应用案例
##### 计算输入两个参数的和
```
#!/bin/base
#计算输入两个参数的和
function getSum(){
    SUM=$[$n1+$n2]
    echo "两数之和：$SUM"
}
#接收用户输入参数
read -p "请输入第一个数N1：" n1
read -p "请输入第二个数N2：" n2
#调用getSum方法名 获取结果
getSum $n1 $n2
```

## shell 综合案例
### 案例要求
> 1.每天凌晨两点十分备份数据库
> 2.备份开始和备份结束能够给出相应提示信息
> 3.备份后文件要求一备份时间文件名,并打包成.tar.gz形式
> 4.在备份同时,检查是否有十天前备份的数据库文件,如果有就将其删除操作
### 开始构建
#### 1.创建update_db.sh
```
touch update_db.sh
```
#### 2.编写update_db.sh
```
vim update_db.sh
```
#### 3.编写CoreCode
```
#!/bin/bash
BACKUP=/data/backup/db
DATETIME=&(date + %Y_%m_%d_%H:%M:%S)
echo "+++++ Start backing up Data +++++"
echo "+++++ Backup target location : $BACKUP/$DATETIME.tar.gz +++++"
HOST=geekparkhub
DB_USER=root
DB_PW=root
DATABASE=geekparkhub.db
[ ! -d "$BACKUP/$DATETIME" ] && mkdir -P "$BACKUP/$DATETIME"
mysqldump -u${DB_USER} -p${DB_PW} --host=$HOST $DATABASE | gzip > $BACKUP/$DATETIME.sql.gz
cd $BACKUP
tar -zcvf $DATETIME.tar.gz $DATETIME
rm -rf $BACKUP/$DATETIME
find $BACKUP -mtime +10 -name "*.tar.gz" -exec rm -rf {} \;
echo "+++++ Data Backup Successful !!! +++++"
```





## 修仙之路 技术架构迭代规划图 
![Alt text](./Technical_Framework_v0.0.5.png)


-----


#### 希望每一篇文章都能够对读者们提供帮助与提升,这乃是每一位笔者的初衷                          



-----


## 感谢您的阅读 欢迎您的留言与建议

- FaceBook：[JEEP SevenEleven](https://www.facebook.com/Jeep-711-433673250337229/)
- Twitter：[@JEEP7ll](https://twitter.com/JEEP7ll)
- Sina Weibo: [@JEEP-711](http://weibo.com/5990854742/profile)
- GeekParkHub GithubHome：<https://github.com/geekparkhub>
- GeekParkHub GiteeHome：<https://gitee.com/geekparkhub>
- Blog GardenHome：<http://www.cnblogs.com/JEEP711/>
- W3C/BlogHome：<https://www.w3cschool.cn/jeep711blog/>
- CSDN/BlogHome：<http://blog.csdn.net/jeep911>
- 51CTO/BlogHome：<http://jeep711.blog.51cto.com/>
- Email：<jeep711.home.@gmail.com>—— <jeep-711@outlook.com> —— <geekparkhub@outlook.com>

---------