# 大数据生态系统 修仙之路 Linux Blog

@(2019-01-03)[Programing Language:Linux|GeekDeveloper:JEEP-711|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)]


![Alt text](./nopic.jpg)

- **极客实验室**是极客国际公园旗下为未来而构建的极客社区；
- **我们正在**构建一个活跃的小众社区,汇聚众多优秀开发者与设计师；
- **关注极具**创新精神的前沿技术&分享交流&项目合作机会等互联网行业服务；
- **Future Vision : **Establishment of the Geek Foundation
- Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见！

-------------------

[TOC]

## linux 简介

> Linux是一套免费使用和自由传播的类Unix操作系统,是一个基于POSIX和UNIX的多用户、多任务、支持多线程和多CPU的操作系统。它能运行主要的UNIX工具软件、应用程序和网络协议。它支持32位和64位硬件。Linux继承了Unix以网络为核心的设计思想,是一个性能稳定的多用户网络操作系统.   —— [维基百科](https://en.wikipedia.org/wiki/Linux)


## linux 目录结构
>  linux的文件目是采用层级式的树状目录结构,linux目录中有且只有一个根目录
linux各个目录存放内容都是规范性的,不可随意放置文件
linux是以文件的形式管理设备,因此在linux生态系统中,一切皆为文件

```
/ 根目录
/root -- 该目录为系统管理员,也称为超级权限者的用户主目录
/bin -- 存放最经常使用的指令
/sbin -- SuperUser,存放系统管理员使用的系统管理程序
/boot -- 存放启动linux及使用的一些核心文件,包括一些连接文件以及镜像文件
/dev -- 类似于windows的设备管理器,把所有的硬件用文件的形式储存
/etc -- 所有的系统管理所需要的配置文件和子目录
/opt -- 给主机额外安装软件的目录,如安装MYSQL数据库就可以存放在此目录
/tmp -- 此目录是用来存放一些临时文件
/sys --  此目录是linux2.6内核的一个很大的变化,该目录安装了2.6内核中新出现的一个文件
/srv -- service缩写,该目录存放一些服务启动后需要提取的数据
/proc -- 此目录是虚拟目录,它是系统内存的映射,访问此目录来获取系统信息
/home -- 存放普通用户的主目录,每个账户都会有自己的home目录,一般该目录名是以账户名命名
/var -- 此目录存放着不断扩充的文件,习惯将经常被修改的目录存放在这里,包括各种日志文件
/lib -- 系统开机所需要最基本的动态连接共享库,其作用类似于Windows里的dll文件,几乎所有的应用程序都需要用到这些共享库
/lost+founf -- 此目录一般情况下为空,当系统非法关机,这里就会存放一些文件
/usr -- 尤为重要的目录,用户的很多应用程序和文件都存放在此目录,类似于windows下的programfiles目录
/usr/local -- 另一个给主机额外安装软件的安装目录,一般是通过编译源码方式安装程序
/media -- linux系统会自动识别一些设备,例如U盘,光驱等等,当失败后,linux会把识别的设备挂载到此目录
/mnt -- 系统提供此目录是为了让用户临时挂载其他文件系统,可以将外部存储挂载在/mnt上,然后进入此目录就可以查看内容
/selinux[Security-Enhanced Linux] -- SElinux是一种安全子系统,它能控制程序只能访问特定文件
```

## 远程登录 linux客户端
> 通过`ifconfig`命令获取linuxIP地址
通过finalshell ssh远程登录并连接此服务器,如连接失败需要检查linux是否开启`ssd`服务端口
IPaddr+22端口+username+password即可成功远程连接并可以使用指令来操作linux系统


## linux Vi与Vim编辑器
> 所有的linux系统都会内建vi文本编辑器
Vim具有程序编辑的能力,可以看做是vi的增强版,可以主动的以字体颜色辨别语法的正确性,
方便程序设计,代码补全,编译及错误跳转等方便编程的功能特别丰富,在开发者中被广泛使用

#### 常用三种模式
#### **`正常模式`**
当vim打开一个档案就直接进入一般模式(默认模式),在这个模式中,可以使用上下左右按键来移动光标,
可以使用删除字符或删除整行来处理文档内容,也可以使用复制粘贴来处理文件数据

#### **`插入模式(编辑模式)`**
以 `i`,`I`,`o`,`O`,`a`,`A`,`r`,`R`等任一个字母之后才会进入编辑模式,一般来说按`i`键即可

#### **`命令行模式`**
在此模式中,可以提供相关指令,完成读取,存盘,替换,离开vim,显示行号等的动作则是此模式的达成

#### **`vi与vim模式相互切换`**
在命令行下 #vim xxx
从一般正常模式下,快捷键i或a进入 插入/编辑模式,快捷键esc返回一般正常模式
从一般正常模式下,快捷键:或/进入 命令模式,在命令行下,`:wp`表示写入并退出,`:q`既是不保存退出,
`:q!`既是强制性退出,快捷键esc返回一般正常模式

#### **`vi与vim快捷键`**
1.拷当前行快捷键`yy`,拷贝当前行向下5行并粘贴,快捷键`5yy`,`p`
2.删除当前行快捷键`dd`,删除当前行向下5行,快捷键`5dd`
3.在文件中查找某个单词,(切换命令行下 快捷键/关键字,回车查找,输入`n`就是查找下一个)
4.设置文件行号,取消文件行号,(切换命令行下 快捷键 `:set nu` 和 `:set nonu`)
5.在正常模式下,编辑/etc/profile文件,使用快捷键到底部文档的最末行快捷键`G`和最首行快捷键`gg`
6.在正常模式下,在一个文件中输入"hello",然后又撤销这个动作 快捷键`u`
7.编辑/etc/profile文件,并将光标移动到20行 快捷键`shift+g`
先切换命令行模式下,显示行号,`:set nu`,然后esc返回正常模式,然后输入20,并`shift+g`即可


## linux 关机&重启命令
```
shutdown -h now 立即进行关机
shutdown -h 1 一分钟后关机
shutdown -r now 重新启动计算机
halt 关机
reboot 重新启动计算机
sync 把内存数据同步到磁盘
```
**注意细节**:当关机或重启时候,都应该先执行sync指令,把内存的数据写入磁盘,放置数据丢失.

用户登录和注销
登录时尽量少使用root账号,因为是系统管理员,有着最大权限,避免操作失误,
可以利用普通管理员,登录后再用 `su-username` 命令来切换成系统管理员身份
在提示符下输入 `logout`即可注销用户,logout注销指令在图形化界面运行级别无效.

## linux 用户与组管理
> linux系统是一个多用户多任务的操作系统,任何一个要使用系统资源的用户,
都必须首先向系统管理员申请一个账号,然后以这个账号的身份进入系统.

### 用户管理
> linux系统是一个多用户多任务的操作系统,任何一个要使用系统资源的用户,
都必须首先向系统管理员申请一个账号,然后以这个账号的身份进入系统

#### 添加用户指令
```
useradd username
```
添加一个用户为jeep711
```
useradd jeep711
```
当创建用户以后,会自动创建和用户同名的home目录,也可以通过`useradd-d` 指定目录新的用户名,给新创建的用户指定home目录
#### 创建指定目录下的用户命令
```
useradd -d /home/test testuser
```
#### 指定用户修改密码
```
passwd  username
```
#### 删除用户
```
userdel username
```
删除用户,但保留用户home目录 ``userdel username``
删除用户以及删除用户主目录 ``userdel -r username``

#### 查询用户信息指令
```
id username
```

#### 切换用户
在操作linux,如果当前用户权限不够,可以通过``su - ``指令,切换到高权限用户, 比如root
```
su - root
```
从权限高的用户切换到权限低的用户,不需要输入密码,反之需要,当需要返回到原来用户时,使用exit指令

#### 查看当前用户/登录用户
``whoam`` 或 ``who am i``


### 用户组
> 类似于角色,系统可以对共性的多用户进行统一管理
#### 新增组指令
```
groupadd groupname
```
#### 删除组指令
```
groupdel groupname
```
#### 新增用户指定组指令
```
useradd -g groupname username
```
#### 修改用户组指令
```
usermod -g groupname username
```
#### 用户和组的相关文件

> ``/etc/passwd``文件
用户的配置文件,记录用户的各种信息
每行含义: 用户名:口令:用户标识号:组织标识号:注释性描述:主目录:登录shell

> ``/etc/shadow``文件
口令的配置文件
每行含义: 登录名:加密口令:最后一次修改时间:最小时间间隔:最大时间间隔:警告时间:不活动时间:失效时间:标志

> ``/etc/group``文件
组的配置文件,记录linux包含组的信息
每行含义: 组名:口令:组标识号:组内用户列表

## linux 实用指令

### 指定运行级别
> 运行级别说明:
0:关机
1:单用户[找回丢失密码]
2:多用户状态没有网络服务
3:多用户状态有网络服务
4:系统未使用保留给用户
5:图形化界面
6:系统重启
常用的级别是3和5,要修改默认运行级别顺序可以更改配置文件
/etc/inittab的id:5:initdefault:这一行中的数字
命令:init[012356]
如何找回root密码,进入单用户模式,进行修改密码,因单用户模式,root不需要密码,开机按住回车键,选择第二选项即可

### 帮助指令
当我们对某一个指令不熟悉时,可以使用linux提供的帮助指令来了解指令使用
``man`` [指令或配置文件] (功能描述,获取帮助信息)
``help``指令 (功能描述,获得shell内置命令帮助信息)

### 文件目录类
#### pwd指令
```
pwd (功能描述:显示当前工作目录的绝对路径)
```
#### ls指令
```
ls [选项] [目录或文件]
常用选项
-a 显示当前目录所有文件和目录,包括隐藏
-i 以列表方式显示信息
```
#### cd指令
```
cd [参数] (功能描述:切换到指定目录)
```
#### mkdir指令
```
mkdir指令用于创建目录
mkdri [选项] 创建目录名称
-p 创建多级目录
```
#### rmdir指令
```
删除目录
rmdir指令 删除空目录
```
#### touch指令
````
touch指令创建空文件
touch filename
```
#### cp指令
```
cd指令拷贝文件到指定目录
cp 选项 source dest
常用选项
-r 递归复制整个文件
cp aa/a.txt bb/
cp -r aa/ bb/
反斜杠 \ 强制性覆盖
```
#### rm指令
```
rm指令移除文件或目录
rm 选项 deletefilename
-r 递归删除整个文件夹
-f 强制删除不提示
```
#### mv指令
```
移动文件与文件重命名
mv oldNameFile newNanmeFile 重命名文件指令
mv /temp/movefile/tagrgetFloder 移动文件指令
```
#### cat指令
```
cat查看文件内容
cat 选项 filename
-n 显示行号
cat只能浏览文件,但不能修改文件,为了浏览方便,一般会带上 管道命令 | more
```
#### more指令
```
more指令是一个基于VI编辑器的文本过滤器,它以全屏方式按分页显示文本文件内容
more指令中内置了若干个快捷键,详情说明如下
more filename
空格键 表示下翻页
回车键 表示下翻一行
q 表示立即离开more,不下显示该文件内容
ctrl+f 向下滚动一屏
ctrl+b 返回上一屏
= 输入当前行的行号
:f 输出文件名和当前行号
```
#### less指令
```
less指令用来分屏查看文件内容,功能与more指令相似,但是比more指令更强大,
支持各种显示终端,less指令在显示文件内容时,并不是一次将整个文件加载之后才显示,
而是根据显示需要加载内容,对于显示大型文件具有较高的效率
less filename
空格键 向下翻动一页
pagedown 向下翻动一页
pageup 向上翻动一页
/关键字 向下搜索关键字,小写n 向下查找,大写N 向上查找
?关键字 向上搜寻关键字,小写n 向上查找,大写N 向下查找
q 离开less程序
```
#### >输出重定向指令(会将原来内容覆盖) 和 >>追加指令
```
ls-l>filename 列表的内容写入文件a.txt(覆写)
ls-al>>filename 列表的内容追加到文件aa.txt的末尾
cat filename1 >filename2 将文件1内容覆盖到文件2
echo "contents" >> filename
将日历信息追加到指定文件中 cal >> /home/a.txt
```
#### echo指令
```
echo指令输出内容到控制台
echo 选项 输出内容
echo $PATH 输出linux环境变量
```
#### head指令
```
head指令用于显示文件的开头部分内容,默情况下head指令显示文件的前10行内容
haed filen 查看文件前10行内容
head -n 5filena 查看文件头5行内容,5可以自定义
```
#### tail指令
```
tail指令输出文件中尾部部分,默认情况下tail指令显示文件的后10行内容
tail filename 查看文件后10行内容
tail -n 5 filename 查看文件后5行内容
tali -f filename 实时追踪该文档的所以更新
```
#### ln指令
````
软连接指令也称作符号链接,类似于windows里的快捷方式,主要存放了链接其他文件的路径
ln -s 原文件或目录 软连接名称 (功能描述:给原文件创建一个软连接)
当时有pwd指令查看目录时,仍然看到的是软连接所在的目录
```
#### history指令
````
查看已经执行过历史命令,也可以执行历史命令 
history 
查询历史命令,想再次执行某一条命令,可以使用 ! id 感叹号
```
#### 时间日期类相关指令
```
date指令 显示当前日期
date 显示当前时间
date +%Y 显示当前年份
date +%m 显示当前月份
date +%d 显示当前哪一天
date "+%Y-%m-%d %H:%M:%S" 显示年月日时分秒
设置日期指令
date -s 字符串时间
```
#### cal指令
```
cal 查看日历指令 不加选项,显示本月日历
cal 2020 显示2020年日历
```

#### 搜索查找类
```
find指令
find指令将从指定目录向下递归遍历其各个子目录,将满足条件的文件或目录显示在终端
find 搜索范围 选项
-name 按照指定文件名称查找模式查找文件
-user 查找属于指定用户名所有文件
-size 按照指定文件大小查找文件
超找整个linux系统下大于20M文件 (+n 大于 -n小于 n等于)
find / -size +20M
```
#### locate指令
````
locate指令可以快速定位文件路径,locate指令利用事先建立的系统中所有文件名称及路径
的locate数据库实现快速定位给定的文件,locate指令无需遍历整个文件系统,查询速度快
为了保证查询结果的准确度,管理员必须定期更新locate时刻
初始化先执行 updatedb指令在执行查询指令
locate filename
由于locate指令基于数据库进行查询,所以第一次运行前,必须使用updatedb指令创建locate数据库
```
#### grep指令 和 管道符号 |
```
grep过滤查找,管道符|,表示将前一个命令的处理结果输出传递给后面的命令处理
grep 选项 查找内容 源文件
-n 显示匹配行及行号
-i 忽略字母大小写
查找文件中含有55252关键字以及行号大小写并打印控制台
cat Hello.java | grep -ni 55252
```
#### 压缩与解压指令
##### gzip filename 用于压缩文件指令,只能将文件压缩为*.gz文件
```
gunzip filename.gz 用于解压指令
zip/uzip指令
zip 指令用压缩文件,uzip用于解压文件
zip 选项 filename.zip 将要压缩的内容,压缩文件和目录命令
-r 递归压缩,压缩目录
unzip 选项 filename.zip 解压文件
-d<目录> 指定解压后文件的存放目录
```
##### tar指令
```
tar指令是打包指令,最后打包的文件是.targz文件
tar 选项 filename.tar.gz 打包目录,压缩后文件格式tar.gz
-c 产生.tar打包文件
-v 显示详情信息
-f 指定压缩后的文件名
-z 打包同时压缩
-x 解压.tar文件
tar -zvcf a.tar.z a.txt b.txt 将a.txtb.txt打包为a.tar.gz文件指令
tar -zxvf  a.tar.gz 将a.tar.gz解压
```

#### cut指令 (重点-看家本领)
> 功能：cut工作就是剪,具体就是在文件中负责剪切数据使用,cut指令从文件的每一行剪切字节/字符/字段并将这些内容输出
> 基本语法 默认分隔符是制表符
**`cut 选项参数 filename`**
**`-f`** 列号,提取第几列
**`-d`** 分隔符,按照指定分隔符分割列
##### cut指令应用案例
###### 选取系统PATH变量值,第二个:,开始后的所有路径
```
echo $PATH | cut -d : -f 3-

效果如下
[root@servicehub]# echo $PATH | cut -d : -f 3-
/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin
```
###### 获取IP地址并截取IP地址
```
ifconfig eth0 | grep "inet addr" | cut -d : -f 3 | cut -d " " -f 1
```
#### sed指令 (重点-看家本领)
> sed是一种流编辑器,它一次处理一行内容,处理时,把当前处理的行储存在临时缓冲区中,称为模式空间
> 接着用sed指令处理缓冲区的内容,处理完成后,把缓冲区的内容送往屏幕,接着处理下一行,这样一直不断重复,
> 直至文件末尾,文件内容并没有改变,除非使用重定向储存输出
##### 基本语法
**`sed 选项参数 命令参数 filename`**
**`-e`** 直接在指令模式上进行sed动作编辑
命令参数
**`a`** 新增 a的后面可以拼接字符串,在一行出现
**`d`** 删除
**`s`** 查找并替换

##### sed指令应用案例
在sed.txt文件内容基础上将ssssss加入到到内容第二行并打印
```
sed "2a ssssss" sed.txt
```

#### awk指令 (重点-看家本领)
> 一个强大的文本分析工具,把文件逐行读写,一空格为默认分隔符将每行切片,切开的部分在进行分析处理
##### 基本用法
**`awk 选项参数 'pattern1{action1} pattern2{action2}...' filename`**
**`pattern`** 表示AWK在数据中查找内容,就是匹配模式
**`action`** 在找到匹配内容时所执行的一系列命令
##### 选项参数
**`-F`** 指定输入文件拆分隔符
**`-v`** 赋值一个用户定义变量

#### sort指令 (重点-看家本领)
> 将文件进行排序,并将排序结果标准输出
##### sort 选项 参数
**`-n`** 依照数值大小排序
**`-r`** 以倒序排序
**`-t`** 设置排序是所用的分隔符
**`-k`** 指定需要排序的列

## linux 组管理与权限管理
> linux组的基本介绍
在linux中每个用户必须属于一个组,不能独立于组外,在linux中每个文件有所有者,所在组,其他组的概念

`所有者` | `所在组` | `其他组` | `改变用户所在的组`

### 文件是目录的所有者
一般为文件的创建者,谁创建了该文件,就自然的成为该文件的所有者
#### 查看文件所有者
```
ls -ahl
```
#### 修改文件所有者
```
chown username filename
```
#### 组的创建
```
groupadd groupname
```
#### 创建monster组指令
```
groupadd monster
```
#### 创建fox用户并添加到monster组中
```
useradd -g monster fox 
```
### 文件/目录所在组
> 当某个用户创建了一个文件之后,这个文件的所在组就是该用户所在的组
#### 查看文件/目录所在组
```
ls -ahl
```
#### 修改文件所在组
```
chgrp groupname filename
```
#### 其他组
> 除文件的所有者和所在组的用户外,系统的其他用户都是文件的其他组

#### 改变用户所在组
> 再添加用户时,可以指定将用户添加到哪个组中,同样的用root的管理权限可以改变某个用户的所在组
```
usermod -g groupname username
usermod -d 目录名 username 改变该用户登录初始化目录
```

## linux 权限基本介绍
### 0-9位说明
第0位确定文件类型(`d`,`-`,`l`,`c`,`b`)
```
- 普通文件
d 目录
l 软连接
c 字符设备
b 块文件 
```
第1-3位确定所有者(该文件的所有者)拥有该文件的权限 -- User
第4-6位确认所属组(同用户组的)拥有该文件的权限 -- Group
第7-9位确认其他组用户拥有该文件的权限 -- Other

### rwx权限详情
`r` 代表可读(read) 可以读取查看
`w` 代表可写(write) 可以修改,但不代表可以删除该文件,删除一个文件的前提是对文件所在的目录有写权限才能删除文件
`x` 代表可执行(execute) 可以被执行

#### 文件及目录权限案例
```
[geek-developer@servicehub /]$ ls -l
total 98
dr-xr-xr-x.   2 root root  4096 Jan  4 03:33 bin
dr-xr-xr-x.   5 root root  1024 Jan  2 03:20 boot
drwxr-xr-x.  18 root root  3740 Jan 19 18:15 dev
drwxr-xr-x. 102 root root 12288 Jan 19 18:15 etc
drwxr-xr-x.   9 root root  4096 Jan  9 19:07 home
dr-xr-xr-x.  10 root root  4096 Jan  2 03:15 lib
dr-xr-xr-x.   9 root root 12288 Jan  2 04:24 lib64
drwx------.   2 root root 16384 Jan  2 03:12 lost+found
drwxr-xr-x.   2 root root  4096 Jan  2 03:29 media
drwxr-xr-x.   3 root root  4096 Jan  2 03:20 mnt
drwxr-xr-x.   7 root root  4096 Jan 17 17:23 opt
dr-xr-xr-x. 177 root root     0 Jan 19 18:15 proc
dr-xr-x---.  31 root root  4096 Jan 19 18:16 root
dr-xr-xr-x.   2 root root 12288 Jan  2 04:24 sbin
drwxr-xr-x.   7 root root     0 Jan 19 18:15 selinux
drwxr-xr-x.   2 root root  4096 Sep 23  2011 srv
drwxr-xr-x.  13 root root     0 Jan 19 18:15 sys
drwxrwxrwt.  57 root root  4096 Jan 19 19:45 tmp
drwxr-xr-x.  13 root root  4096 Jan  2 03:13 usr
drwxr-xr-x.  21 root root  4096 Jan  2 03:17 var
```
#### 文件目录权限表
| 文件类型      |    属主权限 |   属组权限   | 其他用户权限  |
| :-------- | --------:| :------: | :------: |
|  0    |  1   2   3 |  4  5  6  |  7  8  9  |
|  d     |   r   w   x |  r-x  |  r-x  |
|  目录文件     |   读 写 执行 |  读 写 执行  |  读 写 执行  |

```
-rwxrw-r-- 1 root root 1213 Feb 2 09:39 abc
```
> 10个字符确定不同用户能对文件做什么
第一个字符代表文件类型 文件- 目录d 链接 l
其余字符每3个一组(rwx) 读r 写w 执行x
第一组rwx 文件拥有者的权限是读写执行
第二组rw- 与文件拥有者同一组的用户权限是读写但不能执行
第三组r-- 不与文件拥有者同组的其他用户的权限是读不能写和执行

```
可读数字表示 r=4,w=2,x=1,因此rwx=4+2+1=7
```
> 1 文件 硬连接数和目录 子目录
root 用户
root 组
1213 文件大小(字节),如果是文件夹,显示4096
Feb 2 09:39 最后修改日期
abc 文件名

#### chmod 修改权限指令
通过chmod指令,可以修改文件或目录的权限

第一种方式 **`+`**,**`-`**,**`=`** 变更权限

`u 所有者` | `g 所有组` | `o 其他人` | `a 所有人(u,g,o的总和)`
```
chmod u=rwx,g=rx,o=x 目录文件名
chmod o+w 目录文件名
chmod a-x 目录文件名
```
##### 应用案例
###### 给helloworld文件的所有者读写执行权限,给所在组读执行权限,给其他组读执行权限
```
chmod u=rwx,g=rx,o=rx helloworld
```
###### 给helloworld文件所有者移除执行权限,增加组的写权限
```
chmod u-x,g+w helloworld
```
###### 给helloworld文件所以用户添加读的权限
```
chmod a+r helloworld
```

> 第二种方式 通过数字变更权限
权限公式 r=4 w=2 x=1 rwx=4+2+1=7
```
chmod u=rwx,g=rx,o=x 目录文件名
```

###### 将/home/helloworld.txt文件的权限修改成 rwx r-x r-x,使用给数字的方式实现
```
rwx = 4+2+1=7
r-x = 4+1=5
r-x = 4+1=5
chmod 755/home/helloworld.txt
```

###### 修改文件所以者
```
chown tom helloworld.txt

```
###### 将home/kkk目录下的文件和目录的所有者修改成tom
```
chown -R tom kkk/
```

###### 修改文件所在组
chgrp 新组 文件名 改变文件的所有组

###### 将home/abc.txt文件所在组修改iuser组
```
chgrp iuser /home/abc.txt
```

###### 将home/kkk目录下的所有文件和目录的所在组修改成iuser组
```
chgrp -R iuser /home/kkk
```

## linux 定时任务调度
> 任务调度,是指系统在某个时间执行的特定命名或程序
### 任务调度分类
> 1.系统工作,有些重要的工作必须周而复始的执行,如病毒扫描等
> 2.个别一用户工作,个别用户工作可能希望执行某些程序,比如对mysql数据库备份
> 3..........

### crontab 指令
```
crontab 指令
-e 编辑crontab定时任务
-l 查询crontab任务
-r 删除当前用户所有的crontab任务
```
```
设置任务调度文件 /etc/crontab
设置个人任务调度,执行crontab -e命令
输入任务调度文件,*/1**** ls -l /etc/ >> out.txt
每小时每分钟执行 ls -l /ect/ >> /tmp/out.txt
```
### 5个占位符说明
> 第一个**`*`** : 表示一小时当中的第几分钟 0-59
第二个**`*`** : 表示一天当中的第几小时 0-23
第三个**`*`** : 表示一个月当中的第几天 1-31
第四个**`*`** : 表示一年当中的第几个月 1-12
第五个**`*`** : 表示一周当中的星期几 0-7(0和7都代表星期日)

> 特殊符号说明
**`*`** : 代表任何时间,比如第一个*就代表一个小时中每分钟都执行一次
**`,`** : 代表不连续时间,比如0,8,12,16***命令,就代表在每天的8点,12点,16点都执行一次命令
**`-`** : 代表连续的时间范围,比如*05**1-6命令,代表在周一到周六的凌晨5点执行命名
**`*/n`** : 代表每隔多久执行一次,不如*/10****命令,代表每隔10分钟就执行一遍命名

> 特定时间执行
**`4552***`** : 命令 在22点45分执行命令
**`017**1`** : 命令 每周一的17点执行命令
**`051,1,15**`** : 命令 每月一号和15号凌晨5点执行命令
**`404**1-5`** : 命令 每周一到周五的流程四点四十分执行命令
**`*/104***`** : 命令 每天的凌晨四点,每隔10分钟执行一次命令
**`001,15*1`** : 命令 每月一号和15号,每周一凌晨执行命令,注:星期几和几号最好不要同时出现,因为它们定义
都是天,非常容易让管理员混乱

### 任务调度实用指令
```
crontab -r 终止任务调度指令
crontab -l 列出发当前任务调度指令
service crontab restart 重启任务调度指令
```

## linux 磁盘分区&挂载
### 分区基础知识
> 分区方式
> 
> **mdr分区**
> 最多支持四个分区
> 系统只能安装在主分区
> 扩展分区要占一个主分区
> MBR最大只支持2TB,但拥有最好的兼容性
> 
> **gtp分区**
> 支持无线多个主分区(但操作系统可能限制,比如windows下最多128个分区)
> 最大支持18EB的大容量(1EB=1024PB,1PB=1024TB)
> windows7 64位以后版本支持gtp

### Linux分区
> 原理介绍
> 
> 对于linux来说无论有几个分区,分给哪一个目录使用,它归根结底就只有一个根目录,一个独立且唯一的文件结构,linux中每一个分区都是用来组成整个文件系统的一部分.
> 
> linux采用一种叫载入的处理方法,它的整个文件系统中包含了一整套的文件和目录,且将一个分区和一个目录联系起来,这时候要载入的是一个分区将使它的储存空间在一个目录下获得

### 硬盘说明
> linux硬盘分`IDE`硬盘和`SCSI`硬盘,目前基本上是`SCSI`硬盘
> 对于`IDE`硬盘,驱动器标识符为`hdx~`,其中`hd`表明分区所在设备的类型,这里是指`IDE`硬盘,`x`为盘号(`a`为基本盘,`b`为基本从属盘,`c`为辅助盘,`d`为辅助从属盘),`~`代表分区,前四个分区用数字1到4表示,它们是主分区或扩展分区,从5开始就是逻辑分区,；例如`hda3`表示为第一个`IDE`盘上的第三个主分区或扩展分区,`hdb2`表示为第二个`IDE`硬盘上的第二个主分区或扩展区
> 对于`SCSI`硬盘则标识为`sdx~`,`SCSI`硬盘是用`sd`来表示分区所在设备的类型,其余则和IDE硬盘表示方法一样

### 查看分区和挂载情况指令
```
lsblk -f  
```
### 挂载案例
```
虚拟机增加硬盘
虚拟机添加硬盘
分区 fdisk /dev/sdb
格式化 mkfs -t ext4 /dev/sdb1
挂载 先创建一个 /home/newdisk文件,后挂载 mount /dev/sdb1 /home/newdisk 
设置自动挂载 vim /etc/fstab
/dev/sdb1 /home/newdisk ext4 defaults 0 0
mount -a 自动挂载指令
umount /dev/sdb1 卸载sdb1硬盘
```
### 磁盘情况查询
#### 查询系统整体磁盘使用情况指令
```
df -h
```
查询指定目录的磁盘占用情况指令
```
du -h /目录名称
``` 
#### 选项参数详情
```
-s 指定目录占用大小汇总
-h 带计量单位
-a 含文件
--max-depth=1 子目录深度
-c 列出明细同时,增加汇总值
```

### 磁盘情况 工作实用指令
#### 统计/home文件夹下文件个数
```
ls -l /home | grep "^-" | wc -l
```
#### 统计/home文件夹下目录个数
```
ls -l /home | grep "^d" | wc -l
```
#### 统计/home文件夹下文件的个数,包括子文件夹
```
ls -lR /home | grep "^-" | wc -l
```
#### 统计文件夹下目录的个数,包括子文件夹
```
ls -lR /home | grep "^d" | wc -l
```
#### 以树状显示目录结构
```
tree指令
如提示comand not found,需要安装tree,安装指令 yum install tree
```

## linux 网络配置
> 目前VMwareWorkstatio虚拟机采用的网络模式是NAT模式

### linux网络环境配置

#### 自动获取
缺点 : linux启动后自动获取IP,缺点是每次自动获取IP地址都会更变

#### 指定固定IP
直接修改配置文件来指定IP,并可以连接到外网(推荐)
要求:将IP地址配置的静态的,IP地址为`192.168.184.130`
0.当前需要是root用户,才能有rwx权限
1.编辑 **`vim /etc/sysconfig/network-scripts/ifcfg-eth0`**
2.输入**`i`**,进入编辑模式
3.开始输入Code

```
IPADDR=192.168.184.130 指定IP
GATEWAY=192.168.184.2 网关
DNS1=192.168.184.2 DNS
BOOTPROTO="static" 更改为静态模式
```

4.写入设置并退出
```
编写Code后,按Esc按键,在输入:wq 写入即可
```
5.重启网络服务
```
service network restart
```

### 修改主机名
hostname 修改linux主机映射文件
0.当前需要是root用户,才能有rwx权限
1.**`vim /etc/sysconfig/network`**
2.输入**`i`**,进入编辑模式
3.开始输入Code
```
NETWORKING=yes
HOSTNAME=servicehub
```
4.写入设置并退出
```
编写Code后,按Esc按键,在输入:wq 写入即可
```
5.编辑主机映射 **`vim /etc/hosts`**
```
127.0.0.1   localhost servicehub localhost4 localhost4.localdomain4
::1         localhost servicehub localhost6 localhost6.localdomain6
```
6.写入设置并退出
```
编写Code后,按Esc按键,在输入:wq 写入即可
```

### 修改注意事项
> 主机名称不能带有下划线
修改`/etc/hosts` 增加IP和主机映射
`192.168.1.100` `servicehub`
并重启设备,即可生效
如果希望windows也可以通关主机名连接centos,进入C:\Windows\System32\
drivrs\etc\hosts 192.168.2.100 servicehub

## linux 进程管理(重点)
### 进程的基本介绍
> 在linux中,每个执行的程序都会称为一个进程,每一个进程都会分配一个ID号
> 每一个进程,都会对应一个父进程,而这个父进程可以复制多个子个进程,例如www服务
> 每一个进程可以以两种方式存在,前台和后台(守护进程),所谓前台进程就是用户目前在图形化界面可以进行操作,后台进程则是实际在操作,但是由于屏幕无法看到进程,通常使用后台方式执行
> 一般系统的服务都是以后台进程方式存在,而且都会常驻在系统中,直到关机才结束
### 显示系统执行进程
**`ps`** 指令用来查看目前系统中,有哪些正在执行,以及它们执行状况,可以不加任何参数

效果如下
```
[root@servicehub]# ps
   PID TTY          TIME CMD
  2441 pts/0    00:00:00 su
  2447 pts/0    00:00:00 bash
  2515 pts/0    00:00:39 java
  3532 pts/0    00:00:00 ps
```
> 参数说明
**`System V`**展示风格
**`USER`** 用户名称
**`PID`** 进程号
**`%CPU`** 进程占用CPU的百分比
**`%MEM`** 进程占用物理内存的百分比
**`VSZ`** 进程占用的虚拟内存大小(单位: `kb`)
**`RSS`**进程占用物理内存大小(单位: `kb`)
**`TT`** 终端名称缩写
**`STA`** 进程状态,其中`S-`睡眠,`s-`表示该进程会话的先导进程,`N-`表示进程拥有比普通优先级更低的优先级
,`R-`正在运行,`D-`短暂等待,`Z-`僵死进程,`T-`被跟踪或者停止等
**`STARTED`** 进程启用时间
**`TIME`** CPU时间,即进程使用CPU时间
**`COMMAND`** 启用进程所用的命令和参数,如果过长会被截断显示

### 查询指定进程指令
```
ps -aux | grep sshd
```
### 查询父进程指令
```
ps -ef | more
```
### 以用户格式显示进程信息指令
```
ps -a ps -u 
```
### 显示后台进程运行参数指令
```
ps -x 
```

### 终止进程kill 和 lillall
> 若是某一个进程执行一半需要停止时,或是已消耗了很大的系统资源时,此时可以考虑停止该进程,使用kill命令来完成此执行
> **``kill  选项 进程号 (通过进程号结束进程)``**
> 
> **``killall 进程名称 (通过进程名称结束进程,也支持通配符,系统因负载过大而变得很慢,则可时使用)``**
> 
> **`-9`** 表示强迫进程立即停止
> 
> 查看进程树 (初始化使用,需要执行安装tree,yum install tree)
> **`pstree 选项 可以直观查看进程信息`**
> **`-p`** 显示进程PID
> **`-u`**显示进程所属用户

### linux service服务管理
> 服务本质就是进程,但是是运行在后台,通常都会监听某个端口,等待其他程序的请求,比如mysql，sshd，防火墙等,因此我们又称为守护进程,是linux中非常重要的知识点
**`service 服务名 start | stop | restart | reload | status`**
contos7.0不再使用`service`指令,而是使用 `systectl`查看当前防火墙状况,关闭防火墙和重启防火墙
telnet 192.168.184.130 22 监听端口

#### chkcnfig 指令
> 通过chkconfig命令可以给各个运行级别设置自启动或关闭
##### 查看指定服务 
```
chkconfig --list | grep xxx
```
##### 查看指定服务
```
chkconfig 服务名 --list
```
##### 指定某个服务修改级别并设置自启动或关闭
```
chkconfig --level 5 服务名 on/off
```
#### 服务管理应用案例
##### 请显示当前系统所有服务各个运行级别运行状态
```
chkconfig --list
```
##### 请查看sshd服务运行状态
```
service ssha status
```
##### 请将ssdh服务在运行级别5下设置为不自启
```
chkconfig --level sshd 5 off
```
##### 当运行级别为5时,关闭防火墙
```
chkconfig --level iptables 5 off
```
##### 在所有运行级别下,关闭防火墙
```
chkconfig iptables off
```
##### 在所以运行级别下,开启防火墙
```
chkconfig iptables on
注意:chkconfig重新设置服务后自启和关闭,需要重启机器reboot才能生效
```
### 动态监控进程
**`top`**与**`ps`**指令很相似,它们都用来显示正在运行的进程
**`top`**与**`ps`**最大的不同之处在于,**`top在执行一段时间可以更新正在运行的进程`**

#### top 选项参数
**`-d`** 指定top命令每隔几秒更新,默认是3秒在top命令的交互模式当中可以执行
**`-i`** 是top不显示任何闲置或僵死进程
**`-p`** 通过指定监控进程ID来仅仅监控某个进程状态

#### 监控进程互动指令
**`P`** 以CPU使用率排序,默认是此项
**`M`** 以内存使用率排序
**`N`** 以PID排序
**`q`** 退出top

#### 动态监控进程应用案例
##### 监听特定用户
```
top指令 加u 输入用户名即可
```
##### 终止指定进程
```
top指令 加k 输入PID即可
```
##### 指定系统状态更新时间(每隔10秒自动更新)
```
top -d 10 指令即可
```

### 监控网络状态
#### netstat 指令
#### netstat参数说明
**`-an`** 按一定顺序排列输出
**`-p`** 显示哪个进程在调用
#### 查询服务名为sshd服务信息
```
netstat -anp | grep sshd
```

## linux RPM&YUM软件包管理
> 一种用于互联网下载包的打包及安装工具,它包含在某些linux分发版中,它生成具有.RPM扩展名的文件,RPM(RedHat Package Manager)缩写,这一文件格式名称虽然打上了RedHat的标志,但理念是通用的.
> 
> Linux分发版都采用(suse,redhat,centos等等),可以算是公认的行业标准

### RPM包管理
#### rpm包的简单查询指令
```
查询已安装的rpm列表 rpm -qa | grep xxx
rpm包其他查询指令
rpm -qa 查询所有安装rpm软件包
rpm -qa | more 分页查询所有
rpm -q 软件名称
rpm -qi 软件名 查询软件信息
rpm -qi file
rpm -ql 软件名 查询软件安装位置
rpm -qf 目录 反向查询所在位置
```
#### 卸载rpm包
```
rpm -e 包名称
安装rpm包
rpm -ivh 软件包全路径名称
i = install 安装
v = verbose 提示
h = hash 进度条
强制性卸载指令 rpm -e -nodeps 软件名
```
### YUM包管理
> yum是一个shell前端软件包管理器,基于RPM包管理,能够从指定的服务器
> 自动下载RPM包并安装,可以自动处理依赖关系,并且一次安装所有依赖的软件包
#### 查询yum服务器是否有需要安装的软件
```
yum list | grep application name
```
#### 安装指定yum包
```
yum install application name
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