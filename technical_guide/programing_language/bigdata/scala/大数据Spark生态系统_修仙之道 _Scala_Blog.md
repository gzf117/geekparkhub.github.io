# 大数据Spark生态系统 修仙之道 Scala Blog

@(2019-05-01)[ Docs Language:简体中文 & English|Programing Scala|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)|![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg) | ![GitHub repo size in bytes](https://img.shields.io/github/repo-size/geekparkhub/geekparkhub.github.io.svg) | GeekDeveloper:[JEEP-711](https://github.com/jeep711)|Github:[github.com/geekparkhub](https://github.com/geekparkhub)|Gitee:[gitee.com/geekparkhub](https://gitee.com/geekparkhub) ]

##  🐘 Scala Technology 修仙之道 炼精化炁 🐘

![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/scala/scala.jpg)

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


## 0. 学习前你需要了解
> 在继续本教程之前,你应该了解一些基本计算机编程术语.
> 
> Spark是新一代基于内存级大数据计算框架,是大数据重要内容.
> 
> Spark是基于Scala编程语言构建完成,如果你学习过Java编程语言,将有助于你更快了解掌握Scala编程语言.


## 1. Scala 概述
> Scala是一门多范式(multi-paradigm)编程语言,设计初衷是要集成面向对象编程和函数式编程各种特性.
> 
> Scala运行在Java虚拟机上,并兼容现有Java程序.
> 
> Scala源代码被编译成Java字节码,所以它可以运行于JVM之上,并可以调用现有Java类库.
> 
> Spark的兴起,带动了Scala语言的发展.


## 2. Scala 语言诞生
> 创始人马丁 · 奥德斯基(Martin Oderskv)是编译器及编程的狂热爱好者.
> 
> 长时间的编程之后,希望发明一种语言,能够让写程序这样的基础工作变得高效,简单.
> 
> 所以当接触到JAVA语言后,对JAVA这门便携式,运行在网络,且存在垃圾回收的语言产生了极大的兴趣,所以决定将函数式编程语言的特点融合到JAVA中.
> 
> 由此发明了两种语言(Pizza & Scala) / Pizza 和 Scala极大地推动了JAVA编程语言的发展.
> jdk5.0泛型,for循环增强,自动类型转换等,都是从Pizza,引入的新特性.
> 
> jdk8.0的类型推断,Lambda表达式就是从Scala引入的特性.
> 
> 且现在主流JVM 的javac编译器就是马丁 · 奥德斯基编写出来的,Jdks5.0 & Jdk8.0的编辑器就是马丁 · 奥德斯基编写的,因此马丁 · 奥德斯基一个人的战斗力抵得上一个JAVA开发团队.

## 3. Scala 语言特点
> Scala是一门以java虚拟机(JVM)为运行环境并将面向对象和函数式编程的最佳特性结合在一起的静态类型编程语言.
> 
> Scala是一门多范式(multi-paradigm)的编程语言,Scala支持面向对象和函数式编程.
> 
> Scala源代码(.scala)会被编译成Java字节码(.class),然后运行于JVM之上，并可以调用现有的Java类库,实现两种语言的无缝对接.
> 
> Scala单作为一门语言来看,非常简洁高效(三元运算 / ++ / --).
> 
> Scala 在设计时,马丁·奥德斯基是参考了Java的设计思想,可以说Scala是源于java,同时马丁·奥德斯基也加入了自己的思想,将函数式编程语言的特点融合到JAVA中,因此,对于学习过Java的开发者,只要在学习Scala过程中,搞清楚Scala和java相同点和不同点,就可以快速的掌握Scala这门语言.
> 
- 快速有效掌握Scala的三点建议
- 1.学习scala的特有的语法
- 2.区别scala和Java 
- 3.如何规范使用scala

## 4. Scala 部署
- `注` : 部署Scala前提,需要事先部署JAVA (JDK1.8+),如部署完jdk,可跳过此步骤.
- Scala 官方下载 : [scala-lang.org/download/](https://www.scala-lang.org/download/)
- Scala 官方文档 : [docs.scala-lang.org](https://docs.scala-lang.org)

### 4.1 MacOs 部署 Scala
- 解压`scala-2.11.8.tgz`到指定目录
```
systemhub:dev_package system$ pwd
/Users/system/home/work/develop/work_flow/software/dev_package
systemhub:dev_package system$ tar -zxvf scala-2.11.8.tgz -C /Users/system/home/work/develop/work_flow/module/
```
- 重命名目录名称
```
systemhub:work_flow system$ cd module/
systemhub:module system$ mv scala-2.11.8/ scala
```
- 查看解压状况
```
systemhub:module system$ ls -ll
total 0
drwxr-xr-x  10 system  staff  340  2 25 20:52 maven
drwxr-xr-x@ 17 system  staff  578  5  9 11:46 tomcat
drwxr-xr-x  13 system  staff  442  2 28 23:28 hadoop
drwxr-xr-x   6 system  staff  204  3  4  2016 scala
systemhub:module system$
```
- vim `/etc/profile`
```
systemhub:module system$ cd scala/
systemhub:scala system$ pwd
/Users/system/home/work/develop/work_flow/module/scala
systemhub:scala system$ sudo vim /etc/profile
```
```
## SET SCALA_HOME
export SCALA_HOME=/Users/system/home/work/develop/work_flow/module/scala
export PATH=$PATH:$SCALA_HOME/bin
```

- source `/etc/profile`
```
systemhub:scala system$ source /etc/profile
```
- 运行 Scala | Hello World!
```
systemhub:scala system$ scala
Welcome to Scala 2.11.8 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8).
Type in expressions for evaluation. Or try :help.

scala> print("Hello World!");
Hello World!
scala> :quit
systemhub:scala system$
```



### 4.2 Linux 部署 Scala
- 解压`scala-2.11.8.tgz`到指定目录
```
[root@systemhub511 software]# tar -zxvf scala-2.11.8.tgz -C /opt/module/
```
- 重命名目录名称
```
[root@systemhub511 module]# mv scala-2.11.8/ scala
```
- 查看解压状况
```
[root@systemhub511 module]# ll
total 44
drwxr-xr-x.  9 root  root  4096 Feb 24 21:55 tomcat
drwxr-xr-x.  3 root  root  4096 May 12 16:12 cdh_flow
drwxr-xr-x.  3 root  root  4096 May 20 22:46 datas
drwxr-xr-x. 10 root  root  4096 Apr 11 17:02 flume
drwxr-xr-x.  3 root  root  4096 May  8 20:55 HA
drwxr-xr-x. 12 10011 10011 4096 Mar  3 00:42 hadoop
drwxr-xr-x.  8 root  root  4096 May  6 23:31 hbase
drwxr-xr-x.  8 uucp    143 4096 Dec 20  2017 jdk1.8
drwxr-xr-x.  8 root  root  4096 Apr 17 14:15 kafka
drwxrwxr-x.  6  1001  1001 4096 Mar  4  2016 scala
drwxr-xr-x. 11  1001  1001 4096 Apr 17 13:31 zookeeper
[root@systemhub511 module]# 
```

- vim `/etc/profile`
```
[root@systemhub511 module]# cd scala/
[root@systemhub511 scala]# pwd
/opt/module/scala
[root@systemhub511 scala]# vim /etc/profile
```

```
## SET SCALA_HOME
export SCALA_HOME=/opt/module/scala
export PATH=$PATH:$SCALA_HOME/bin
```

- source `/etc/profile`
```
[root@systemhub511 scala]# source /etc/profile
```

- 运行 Scala | Hello World!
```
[root@systemhub511 module]# scala
Welcome to Scala 2.11.8 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8).

Type in expressions for evaluation. Or try :help.
scala> print("Hello World!");
Hello World!
scala> :quit
[root@systemhub511 bin]# 
```

## 5. Scala 插件 For JetBrains IntelliJ IDEA
- 基于JetBrains IntelliJ IDEA部署Scala插件,如图所示
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/scala/start_001.jpg)


## 6. Scala Quick Start
- JetBrains IntelliJ IDEA New Maven Project | 此过程省略
- Create `QuickStartScala.scala`
``` scala
package com.geekparkhub.core.scala.quickstart

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
  * QuickStartScala
  * <p>
  */

object QuickStartScala {
  def main(args: Array[String]): Unit = {
    println("Scala ~ Hello World!");
  }
}
```
- Run main
```
Scala ~ Hello World!
```

![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/scala/start_002.jpg)

### 6.1 反编译 Scala程序 执行流程
#### 6.1.1 Java模拟Scala代码
``` java
package com.geekparkhub.core.scala.decompile;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.org/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * QuickStartScala
 *
 * Scala 执行流程
 * 1. object 在底层会生成两个类QuickStartScala,QuickStartScala$
 * 2. `QuickStartScala`中有main函数,调用`QuickStartScala$` 类的一个静态对象 `MODULES$`
 * <p>
 */

public final class QuickStartScala {

    public static void main(String[] paramArrayOfString) {
        // 3. QuickStartScala$.MODULE$. 对象是静态的,通过该对象调用QuickStartScala$的main函数
        QuickStartScala$.MODULE$.main(paramArrayOfString);
    }
}

final class QuickStartScala$ {
    public static final QuickStartScala$ MODULE$;

    static {
        MODULE$ = new QuickStartScala$();
    }

    /**
     * 可以理解为在main函数编写的代码放在QuickStartScala$的main函数中,其实是在底层执行scala编译器做了包装
     * @param args
     */
    public static void main(String[] args) {
        System.out.println("Scala ~ Hello World!");
    }
}
```
#### 6.1.2 Scala执行流程
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/scala/start_003.jpg)

#### 6.1.3 Scala程序 开发注意事项 (重点)
- 1.Scala源文件以`.scala`为扩展名
- 2.Scala程序执行入口是main()函数
- 3.Scala语言严格区分大小写
- 4.Scala方法由一条条语句构成,每个语句后不需要分号(Scala语言会在每行后自动加分号),这也体现出Scala简洁性
- 5.如果在同一行有多条语句,除了最后一条语句不需要分号,其它语句需要分号

### 6.2 Scala 转义字符
- `\t` : 制表符
- `\n` : 换行符
- `\\` : 表示一个`\`
- ```\"``` : 表示一个`"`
- `\r` : 表示一个回车

### 6.3 Scala 语言输出方式
- 字符串通过+号连接 (类似java)
- printf用法 (类似C语言)字符串通过`%`传值
- 字符串通过`$`引用 (类似PHP)
- Create `DemoTest.scala`
``` scala
package com.geekparkhub.core.scala.demo

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园枢纽
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  *  DemoTest
  * <p>
  */

object DemoTest {
  def main(args: Array[String]): Unit = {

    /**
      * String stitching output
      * 字符串拼接 输出
      */
    val parameter1: String = "Hello "
    var parameter2: String = "World!"
    println(parameter1 + parameter2)

    /**
      * Dividing line
      * 分割线
      */
    println(s"-----------------------------------------------------------------------------------------")

    /**
      * Printf formatted output
      * printf格式化 输出
      */
    var name: String = "TestUser001"
    var age: Int = 66;
    var investment: Float = 722.37f
    var assets: Double = 777777777.158
    printf("name is = %s | age is  = %d | investment is = %.2f | assets is = %.3f", name, age, investment, assets)

    /**
      * Dividing line
      * 分割线
      */
    println(s"\n-----------------------------------------------------------------------------------------")

    /**
      * String + $ output
      * 字符串+$ 输出
      */
    println(s"Demo1 info : \n name is  = $name \n age is = $age \n investment is = $investment \n assets is = $assets")

    /**
      * Dividing line
      * 分割线
      */
    println(s"-----------------------------------------------------------------------------------------")

    /**
      * Expression +$ output
      * 表达式+$ 输出
      */
    println(s"Demo2 info : \n name is  = $name \n age is = $age \n investment is = ${investment + 10} \n assets is = ${assets * 20}")
  }
}
```

- 执行查看结果
```
Hello World!
-----------------------------------------------------------------------------------------
name is = TestUser001 | age is  = 66 | investment is = 722.37 | assets is = 777777777.158
-----------------------------------------------------------------------------------------
Demo1 info : 
 name is  = TestUser001 
 age is = 66 
 investment is = 722.37 
 assets is = 7.77777777158E8
-----------------------------------------------------------------------------------------
Demo2 info : 
 name is  = TestUser001 
 age is = 66 
 investment is = 732.37 
 assets is = 1.555555554316E10
```


### 6.4 Scala 注释 (comment)
- 用于注解说明解释程序文字就是注释,注释提高了代码阅读性.
- 注释是一个开发者必须要具有良好编程习惯,将自己思想通过注释先整理出来,再用代码去体现.

- `Scala 注释类型`
- 1.单行注释
- 2.多行注释
- 3.文档注释

### 6.5 Scala 代码规范说明
- `正确注释和注释风格 | Scala源码`
``` scala
/** Contains a fallback builder for arrays when the element type
 *  does not have a class tag. In that case a generic array is built.
 */
class FallbackArrayBuilding {

  /** A builder factory that generates a generic array.
   *  Called instead of `Array.newBuilder` if the element type of an array
   *  does not have a class tag. Note that fallbackBuilder factory
   *  needs an implicit parameter (otherwise it would not be dominated in
   *  implicit search by `Array.canBuildFrom`). We make sure that
   *  implicit search is always successful.
   */
  implicit def fallbackCanBuildFrom[T](implicit m: DummyImplicit): CanBuildFrom[Array[_], T, ArraySeq[T]] =
    new CanBuildFrom[Array[_], T, ArraySeq[T]] {
      def apply(from: Array[_]) = ArraySeq.newBuilder[T]
      def apply() = ArraySeq.newBuilder[T]
    }
}
```
- `正确缩进和空白`
- 1.使用一次tab操作,实现缩进,默认整体向右边移动,时候用shift+tab整体向左移.
- 2.或者使用快捷键进行格式化
- 3.运算符两边习惯性各加一个空格,比如 : `2 + 4 * 5`
- 4.一行最长不超过80个字符,超过请使用换行展示,尽量保持格式优雅


### 6.6 Scala 官方API指南
Scala 官方API指南 : [scala-lang.org/api/2.11.8](https://www.scala-lang.org/api/2.11.8/#package)



### 6.7 Scala 变量
- 变量是程序基本组成单位
- 变量相当于内存中一个数据存储空间的表示,可以把变量看做是一个房间门牌号,通过门牌号可以找到房间,而通过变量名可以访问到变量(值).

变量使用基本步骤
- 1.声明/定义变量(scala要求变量声明时初始化) 
- 2.使用变量

Scala 变量基本使用
```
var age : Int = 10
var sal : Double = 10.9
var name : String = "tom"
var isPass : Boolean = true
var score : Float = 70.9f
```

Scala 变量使用说明

- 变量语法 : `var | val 变量名[: 变量类型] = 变量值`
- 1.声明变量时,类型可以省略 (编译器自动推导,即类型推导).
- 2.类型确定后,就不能修改,说明Scala是强数据类型语言.
- 3.在声明/定义一个变量时,可以使用`var`或者`val`来修饰,`var`修饰的变量可改变,`val`修饰的变量不可改.
- 4.`val`修饰的变量在编译后,等同于加上final
- 5.`var`修饰的对象引用可以改变,`val`修饰的则不可改变,但对象的状态(值)却是可以改变的,(比如:自定义对象、数组、集合等等)
- 6.变量声明时,需要初始值.


### 6.8 Scala 数据类型
- 1.Scala与Java有着相同的数据类型,在Scala中数据类型都是对象,也就是说Scala没有Hava中的原生类型.
- 2.Scala数据类型分为两大类`AnyVal(值类型)`和`AnyRef(引用类型)`,注意:不管是AnyVal还是AnyRef都是对象.
- 3.相对于java的类型系统,scala要复杂些,也正是这复杂多变的类型系统才让面向对象编程和函数式编程完美的融合在一起

#### 6.8.1 Scala 数据类型体系
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/scala/start_004.jpg)
- 1.在scala中有一个根类型`Any`,它是所有类的父类.
- 2.scala中一切皆为对象,分为两大类`AnyVal(值类型)`,`AnyRef(引用类型)`,它们都是Any子类.
- 3.Null类型是scala特别类型,它只有一个值null,它是bottom.calss,是所有AnyRef类型的子类.
- 4.Nothing类型也是bottom.class,它是所有类的子类,在开发中通常可以将Nothing类型的值返回给任意变量或者函数,在抛出异常应用场景时常用.

#### 6.8.2 Scala 数据类型列表

| 数据类型    |     描述 |
| :--------: | :--------:|
| Byte    |   8位有符号补码整数 |
| Short    |   16位有符号补码整数 |
| Int    |   32位有符号补码整数 |
| Long    |   64位有符号补码整数 |
| Float    |   32位标准单精度浮点数 |
| Double    |   64位标准单精度浮点数 |
| Char    |   16位无符号Unicode字符 |
| String    |   字符序列 |
| Boolean    |   true / false |
| Unit    |   表示无值等同于void |
| Null    |   null |
| Nothing    |   任何其他类型的子类型 |
| Any    |   所有类的超类 |
| AnyRef    |   引用类的基类 |


#### 6.8.3 Scala 整形数据类型
- Scala 整数类型就是用于存放整数值
- 整型类型

| 数据类型      |     描述 |
| :--------: | :--------:|
| Byte [1]    |   8位有符号补码整数,数值区间为-128到127 |
| Short [2]   |   16位有符号补码整数,数值区间为-32768到32767 |
| Int [4]    |   32位有符号补码整数,数值区间为-2147483648到2147483647 |
| Long [8]    |   64位有符号补码整数,数值区间为-9223372036854775808到9223372036854775807=2的(64-1)次方-1 |

- 1.Scala各整数类型有固定表数范围和字段长度,不受具体OS影响,以保证Scala程序可移植性.
- 2.Scala的整型常量/字面量默认为Int类型,声明Long型常量/字面量须后加`l`或`L`
- 3.Scala程序中变量常声明为Int类型,除非不足以表示大数,才使用Long.


#### 6.8.4 Scala 浮点数据类型
- Scala的浮点类型可以表示一个小数

| 数据类型      |     描述 |
| :--------: | :--------:|
| Float [4]    |   32位标准单精度浮点数 |
| Double [8]   |   64位标准双精度浮点数 |

- 1.与整数类型类似,Scala浮点类型也有固定的表数范围和字段长度,不受具体OS的影响.
- 2.Scala的浮点型常量默认为Double类型,声明Float类型常量,须后加`f`或`F`
- 3.浮点型常量有两种表示形式 : 
- 十进制数形式 如 : 
- `5.12` | `512.0f`| `.512` (必须保留小数点)
- 科学计数法形式 如 : 
- `5.12e2` = `5.12乘以10的2次方`
- `5.12E-2` = `5.12除以10的2次方`
- 4.通常情况下,应该使用Double类型,因为它比Float类型更精确(小数点后大致7位)


#### 6.8.5 Scala (Char) 字符数据类型
- 1.字符类型可以表示单个字符,字符类型是Char,16位无符号Unicode字符(2个字节),区间值为`U+0000`到`U+FFFF`.
- 2.字符常量是用单引号(‘’)括起来单个字符,例如 : `var c1 = 'a'` |  `var c2 = '中'` | `var c3 = '9'`
- 3.Scala也允许使用转义字符`'\'`来将其后的字符转变为特殊字符型常量,例如 : `var c3 = '\n'//`, `'\n'`表示换行符.
- 4.可以直接给Char赋一个整数,然后输出时会按照对应的`unicode`字符输出`['\u0061' 97]`
- 5.Char类型是可以进行运算,相当于一个整数,因为它都对应有Unicode码

#### 6.8.6 Scala (Boolean) 布尔数据类型
- 1.布尔类型也叫Boolean类型.Booolean类型数据只允许取值`true`和`false`.
- 2.boolean类型占1个字节,boolean类型适于逻辑运算,一般用于程序流程控制.
- 3.if条件控制语句 | while循环控制语句 | do-while循环控制语句 | for循环控制语句

#### 6.8.7 Scala (Unit / Null / Nothing) 数据类型
| 数据类型      |     描述 |
| :--------: | :--------:|
| Unit    |   表示无值等同于void |
| Null    |   null,Null类型只有一个实例null |
| Nothing    |   任何其他类型的子类型 |

- 1.Null类只有一个实例对象,null类似于Java中的null引用,null可以赋值给任意引用类型(AnyRef),但是不能赋值给值类型(AnyVal : 比如Int,Float,Char,Boolean,Long,Double,Byte, Short).
- 2.Unit类型用来标识过程,也就是没有明确返回值的函数,由此可见Unit类似于Java里的void,Unit只有一个实例()
- 3.Nothing,可以作为没有正常返回值的方法的返回类型,非常直观的告诉这个方法不会正常返回,而且由于Nothing是其他任意类型的子类,它还能跟要求返回值方法兼容.








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