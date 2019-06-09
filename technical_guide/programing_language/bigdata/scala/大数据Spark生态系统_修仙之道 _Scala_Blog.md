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

#### 6.8.8 Scala 值类型转换
##### 6.8.8.1 值类型隐式转换
- 当Scala程序在进行赋值或者运算时,精度小的类型自动转换为精度大的数据类型,这个就是自动类型转换(隐式转换).
- 数据类型按精度(容量)大小排序.
- 有多种类型的数据混合运算时,系统首先自动将所有数据转换成容量最大的那种数据类型,然后再进行计算.
- 当精度(容量)大的数据类型赋值给精度(容量)小的数据类型时,就会报错,反之就会进行自动类型转换.
- (byte,short)和char之间不会相互自动转换.
- byte / short / char 三者可以计算,在计算时首先转换为int类型.
- 自动提升原则 : 表达式结果的类型自动提升为操作数中最大类型.


##### 6.8.8.2 高级隐式转换和隐式函数
- scala还提供了非常强大隐式转换机制(隐式函数,隐式类等等).
- 此章节放在高级部分,专门用一个章节来讲解.


##### 6.8.8.3 强制类型转换
- `介绍` : 
- 自动类型转换的逆过程,将容量大的数据类型转换为容量小的数据类型,使用时要加上强制转函数,但可能造成精度降低或溢出,格外要注意.
- 案例演示 : 
```
java : int num = (int)2.5
scala : var num : Int = 2.7.toInt //对象
```
- `强制类型转换细节说明` : 
- 当进行数据从大`——>`小,就需要使用到强制转换.
- 强转符号只针对于最近的操作数有效,往往会使用小括号提升优先级.
``` scala
object DemoTest002 {
  def main(args: Array[String]): Unit = {
    val num1: Int = 10 * 3.5.toInt + 6 * 1.5.toInt
    val num2: Int = (10 * 3.5 + 6 * 1.5).toInt
    println(num1 +" - "+num2)
  }
}
```
- Char类型可以保存Int的常量值,但不能保存Int变量值,需要强转.
- Byte和Short类型在进行运算时,当做Int类型处理.

##### 6.8.8.4 `数据类型转换 实例`
- 判断是否能够通过编译,并说明原因
```
1. var s : Short = 5 //ok
s = s-2 //error Int -> Short

2. var b : Byte = 3 //ok
b = b + 4 // error Int ->Byte
b = (b+4).toByte // ok,使用强制转换

3. var c : Char = 'a' //ok
var i : Int = 5 //ok
var d : Float = .314F //ok
var result : Double = c+i+d //ok Float->Double

4. var b : Byte = 5 //ok
var s : Short = 3 //ok
var t : Short = s + b //error Int->Short
var t2 = s + b //ok,使用类型推导
```

##### 6.8.8.5 值类型和String类型转换
- `介绍` : 
- 在程序开发中,经常需要将基本数据类型转成String类型,或者将String类型转成基本数据类型.
- `基本类型转String类型` : 
- 语法 : 将基本类型的值+`""`即可.
``` scala
    // 基本类型转String类型
    val d1 = 1.2
    val s1 = d1 + ""
    println(d1 +" ~ "+ s1)
```
- `String类型转基本数据类型`
- 语法 : 通过基本类型String调用toXxx方法即可.
``` scala
    // String类型转基本数据类型
    val s2 = "11"
    val int: Int = s2.toInt
    val byte: Byte = s2.toByte
    val double: Double = s2.toDouble
    val long: Long = s2.toLong
    println(s2 +" ~ "+ int +" ~ "+ byte +" ~ "+ double +" ~ "+ long)
```
- `注意事项和细`
- 在将String类型转成基本数据类型时,要确保String类型能够转成有效的数据,比如可以把"123",转成一个整数,但是不能把"hello"转成一个整数.
- 在scala中,不是将小数点后的数据进行截取,而是会抛出异常


##### 6.8.8.6 标识符命名规范
###### 6.8.8.6.1 `标识符概念`
- 1.Scala 对各种变量、方法、函数等命名时使用的字符序列称为标识符
- 2.凡是自己可以起名字的地方都叫标识符

###### 6.8.8.6.2 `标识符命名规则`
- 1.Scala中标识符声明,基本和Java是一致,但是细节上会有所变化.
- 2.首字符为字母,后续字符任意字母和数字,美元符号,可后接下划线_
- 3.数字不可以开头.
- 4.首字符为操作符(比如+ -* /),后续字符也需跟操作符,至少一个(反编译).
- 5.操作符(比如+-*/)不能在标识符中间和最后.
- 6.用反引号`....`包括的任意字符串,即使是关键字(39个)也可以[true]

###### 6.8.8.6.3 `标识符举例说明`
``` scala
    // 首字符为操作符(比如+ -* /),后续字符也需跟操作符,至少一个
    val ++ = "hello,scala"
    println(++)

    val -+*/ = 90
    println(-+*/)

    val `true` = "hello"
    println(`true`)
```
###### 6.8.8.6.4 `标识符命名注意事项`
- 1.包名 : 尽量采取有意义的包名,简短,有意义.
- 2.变量名、函数名、方法名采用驼峰法.

###### 6.8.8.6.5 `Scala 39个关键字` 
```
package, import, class, object, trait, extends, with, type, forSome
private, protected, abstract, sealed, final, implicit, lazy, override
try, catch, finally, throw
if, else, match, case, do, while, for, return, yield
true, false, null
def, val, var
this, super
new
```

### 6.9 Scala 运算符
#### 6.9.1 运算符介绍
- 运算符是一种特殊的符号,用以表示数据的运算赋值和比较等.
- 1.算术运算符
- 2.赋值运算符
- 3.比较运算符(关系运算符)
- 4.逻辑运算符
- 5.位运算符


#### 6.9.2 算术运算符
- 算术运算符(arithmetic)是对数值类型变量进行运算,在Scala程序中使用非常多.
- 算术运算符预览图

| 运算符      |     运算 |   范例   |   结果  |
| :--------: | :--------:| :------: | :------: |
| `+`    |   正号 |  +1  |  1  |
| `-`    |   负号 |  b=4; -b  |  -4  |
| `+`    |   加 |  5+5  |  10  |
| `-`    |   减 |  6-4  |  2  |
| `*`    |   乘 |  3*4  |  12  |
| `/`    |   除 |  5/5  |  1  |
| `%`    |   取余 |  7%5  |  2  |
| `+`    |   字符串相加 |  "he"+"llo"  |  "hello"  |

```
    // 除法 算数运算使用
    val r1: Int = 10 /3
    val r2: Double = 10 /3
    val r3: Double = 10.0 /3
    println(r1 +" ~ "+ r2 +" ~ " + r3 + " ~ " +r3.formatted("%.2f"))

    // 取余 算数运算使用 | 取余运算原则 : a % b = a - a/b * b
    println(10 % 3)
    println(10 % -3)
    println(-10 % 3)
    println(-10 % -3)
```
- 细节说明
- 对于除号“/”,它的整数除和小数除是有区别的 : 整数之间做除法时,只保留整数部分而舍弃小数部分.
- 当对一个数取模时,可以等价a%b=a-a/b*b ,这样可以看到取模的一个本质运算(和java 的取模规则一样.
- 注意 : Scala中没有++、--操作符,需要通过+=、-=来实现同样效果

#### 6.9.3 关系运算符 (比较运算符)
- 关系运算符结果都是boolean型,也就是要么是true,要么是false.
- 关系表达式经常用在if结构的条件中或循环结构的条件中.
- 关系运算符使用和java一样
- 关系运算符预览图
| 运算符      |     运算 |   范例   |   结果  |
| :--------: | :--------:| :------: | :------: |
| `==`    |   相等于 |  4==3  |  false  |
| `!=`    |   不等于|  4!=3  |  true  |
| `<`    |   小于 |  4<3  |  false  |
| `>`    |   大于 |  4>3  |  true  |
| `<=`    |   小于等于 |  4<=3  |  false  |
| `>=`    |   大于等于 |  4>=3  |  true  |


#### 6.9.4 逻辑运算符
- 用于连接多个条件(一般来讲就是关系表达式),最终的结果也是一个Boolean值.
- 逻辑运算符预览图 | 变量A为true,变量B为false
| 运算符      |     运算 |   范例   |   结果  |
| :--------: | :--------:| :------: | :------: |
| `&&`    |   逻辑与 |  `(A&&B)`  |  false  |
| 或 |   逻辑或 |  (A或B)  |  true  |
| `!`    |   逻辑非 |  `!(A&&B)`  |  true  |


#### 6.9.5 赋值运算符
- 赋值运算符就是将某个运算后的值,赋给指定的变量
- 赋值运算符预览图
| 运算符      |     运算 |   范例   |   结果  |
| :--------: | :--------:| :------: | :------: |
| `=`    |   将值赋给左值 |  C = A + B |  将A+B结果赋值为C  |
| `+=`    |   相加后再赋值|  C += A  |  C = C + A  |
| `-=`    |   相减后再赋值 |  C -= A  |  C = C - A  |
| `*=`    |   相乘后再赋值 |  C *= A |  C = C * A  |
| `/=`    |   相除后再赋值 |  C /= A |  C = C / A  |
| `%=`    |   取余后再赋值 |  C %= A  |  C = C % A  |
| `<<=`    |   左移后再赋值 |  C <<= 2  |  C = C << 2  |
| `>>=`    |   右移后再赋值 |  C >>= 2  |  C = C >> 2  |
| `&=`    |   按位与再赋值 |  C $= 2  |  C = C & 2  |
| `^=`    |   按位异或后再赋值 |  C ^= 2  |  C = C ^ 2  |
| `或=`    |   按位或后再赋值 |  C 或= 2  |  C = C 或 2  |

- 赋值运算符特点
- 运算顺序从右往左.
- 赋值运算符的左边只能是变量,右边可以是变量、表达式、常量值/字面量
- 复合赋值运算符等价于下面的效果 | a+=3 等价于a=a+3
- `位运算符`
- 位运算符预览图
| 运算符      |     运算 |   范例   |   结果  |
| :--------: | :--------:| :------: | :------: |
| `&`    |   按位与运算符 |  (a&b)|  结果12,二进制0000 1100  |
| `或`    |   按位或与运算符|  (a或b)  |  结果61,二进制0011 1101  |
| `^`    |   按位异或运算符 |  (a^b)  |  结果49,二进制0011 0001  |
| `~`    |   按位取反运算符 |  (~a) |  结果-61,二进制1100 0011,在一个有符号二进制数的补码形式  |
| `<<`    |   左移动运算符 |  a<<2 |  结果240,二进制1111 0000  |
| `>>`    |   右移动运算符 |  a>>2  |  结果15,二进制0000 1111  |
| `>>>`    |   无符号右移 |  A>>>2  |  结果,二进制0000 1111  |

- 运算符特别说明
- Scala不支持三目运算符,在Scala中使用if else方式实现.

#### 6.9.6 运算符优先级
- 运算符有不同的优先级,所谓优先级就是表达式运算中的运算顺序,上一行运算符总优先于下一行.
- 只有单目运算符、赋值运算符是从右向左运算.
- 运算符的优先级和Java一样.

#### 6.9.7 键盘输入语句
- 在编程中,需要接收用户输入数据,就可以使用键盘输入语句来获取.
- 可以从控制台接收用户信息
``` scala
object DemoTest003 {
  def main(args: Array[String]): Unit = {
    println("Please type in your name")
    val name = StdIn.readLine()
    println("Please enter age")
    val age = StdIn.readInt()
    println("Please enter the height")
    val height = StdIn.readDouble()
    printf("Your input information is : name=%s age=%d height=%.2f", name, age, height)
  }
}
```

### 6.10 Scala 程序流程控制
- 在程序中,程序运行的流程控制决定程序是如何执行,是必须掌握的,主要有三大流程控制语句 : 
- scala语言中控制结构和Java语言中的控制结构基本相同,在不考虑特殊应用场景情况下,代码书写方式以及理解方式都没有太大的区别.
- 1.顺序控制
- 2.分支控制
- 3.循环控制

#### 6.10.1 分支控制 if-else
- 让程序有选择的执行,分支控制有三种 : 1.单分支 | 2.双分支 | 3.多分支


##### 6.10.1.1 单分支
- `基本语法`
- 说明 : 当条件表达式为true时,会执行花括号内代码块内容.
```
if(条件表达式){
   执行代码块
}
```
- `单分支实例`
``` scala
object DemoTest004 {
  def main(args: Array[String]): Unit = {
    println("Please enter age")
    val age = StdIn.readInt()
    if (age > 18) {
      printf("age > " + age)
    }
  }
}
```
##### 6.10.1.2 双分支
- `基本语法`
- 说明 : 当条件表达式成立,即执行代码块1,否则执行代码块2
```
if (条件表达式) {
    执行代码块1
} else {
    执行代码块2
}
```
- `双分支实例`
``` scala
object DemoTest004 {
  def main(args: Array[String]): Unit = {
    val ages = 17
    if (ages > 18) {
      println(ages + " > 17")
    } else {
      println(ages + " < 17")
    }
  }
}
```

##### 6.10.1.3 多分支
- `基本语法`
- 说明 : 当条件表达式1成立时,既执行代码块1,如表达式1不成立,才去判断表达式2是否成立,如表达式2成立,就执行代码块2,以此类推,如果所有的表达式偶不成立,则执行else代码块,只能由一个执行入口.
```
if (条件表达式1) {
    执行代码块1
} else if (条件表达式2) {
    执行代码块2
} 
......
else {
执行代码块n
}
```
- `多分支实例`
``` scala
object DemoTest005 {
  def main(args: Array[String]): Unit = {
    while (true) {
      println("------------")
      println("请输入修仙等级")
      println("------------")
      val grade = StdIn.readInt()
      if (grade == 100) {
        println("+++++++")
        println("登峰造极")
      } else if (grade > 80 && grade <= 99) {
        println("+++++++")
        println("炉火纯青")
      } else if (grade >= 60 && grade <= 80) {
        println("+++++++")
        println("热化提纯")
      } else {
        println("+++++++")
        println("无名小卒")
      }
    }
  }
}
```
##### 6.10.1.4 分支控制if-else 注意事项
- 如果大括号{}内的逻辑代码只有一行,大括号可以省略,这点和java规定一样.
- Scala中任意表达式都是有返回值,也就意味着if else表达式其实是有返回结果,具体返回结果值取决于满足条件代码体的最后一行内容.
- Scala中是没有三元运算符.


#### 6.10.2 嵌套分支
- 在一个分支结构中又完整的嵌套了另一个完整的分支结构,里面的分支的结构称为内层分支外面的分支结构称为外层分支,嵌套分支不要超过3层.
- `基本语法`
```
if(){
 if(){
} else {
 }
}
```

- `嵌套分支实例`
``` scala
object DemoTest006 {
  def main(args: Array[String]): Unit = {
    println("请输入你的年龄")
    val age = StdIn.readInt()
    if (age >= 18) {
      println("你的年龄大于18岁,请输入你的性别")
      val sex = StdIn.readChar()
      if (sex == '男') {
        println("已进入男子竞技频道")
      } else {
        println("已进入女子竞技频道")
      }
    } else {
      println("你的年龄小于18岁,游戏结束")
    }
  }
}
```


#### 6.10.3 switch 分支结构
- 在scala中没有switch,而是使用模式匹配来处理.


#### 6.10.4 for 循环控制
- Scala也为for循环这一常见的控制结构提供了非常多特性,这些for循环特性被称为for推导式(for comprehension)或for表达式(for expression)

##### 6.10.4.1 范围数据循环方式 1
- `基本语法`
- 说明 : i 表示循环变量,<-规定好 to规定
- i 将会从1-3循环,前后闭合
``` scala
for(i <-1 to 3){
 print(i + " ")
}
```
- `for循环实例`
``` scala
object DemoTest007 {
  def main(args: Array[String]): Unit = {
    val start = 1
    val end = 10
    for (i <- start to end) {
      println(i + " - hello")
    }
  }
}
```
##### 6.10.4.2 范围数据循环方式 2
- `基本语法`
- 说明 : 这种方式和前面的区别在于i 是从1 到3-1,前闭合后开的范围,和java的arr.length() 类似
``` scala
for(i <-1 until 3) {
  print(i + " ")
}
```
- `for循环实例`
``` scala
object DemoTest007 {
  def main(args: Array[String]): Unit = {
    val start = 1
    val end = 10
    for (i <- start until end) {
      println(i + " - hey")
    }
  }
}
```

##### 6.10.4.3 循环守卫
- `基本语法`
- 说明 : 循环守卫,即循环保护式(也称条件判断式,守卫),保护式为true则进入循环体内部,为false则跳过,类似于continue
``` scala
for(i <- 1 to 3 if i != 2) {
 print(i + " ")
}
```
- `循环守卫实例`
``` scala
 object DemoTest007 {
  def main(args: Array[String]): Unit = {
    for (i <- 1 to 3 if i !=2){
      println("num is = " + i)
    }
  }
}
```
##### 6.10.4.4 引入变量
- `基本语法`
- 说明 : 没有关键字,所以范围后一定要通过分号来隔断逻辑
```scala
for(i <-1 to 3; j = 4 -i) {
 print(j + " ")
}
```
- `引入变量实例`
``` scala
object DemoTest007 {
  def main(args: Array[String]): Unit = {
    for(i <- 1 to 3 ; j = 4 - i){
      println("num j is = " + j)
    }
  }
}
```


##### 6.10.4.5 嵌套循环
- `基本语法`
- 说明 : 没有关键字,所以范围后一定要通过分号来隔断逻辑
``` scala
for(i <-1 to 3; j <-1 to 3) {
 println(" i =" + i + " j = " + j)
}
```
- `嵌套循环实例`
``` scala
object DemoTest007 {
  def main(args: Array[String]): Unit = {
    for (i <- 1 to 3 ; j <- 1 to 5){
      println("i is = " + i + " , " + "j is = " + j)
    }
  }
```

##### 6.10.4.6 循环返回值
- `基本语法`
- 说明 : 将遍历过程中处理的结果返回到一个新Vector集合中,使用`yield`关键字.
``` scala
val res = for(i <-1 to 10) yield i
println(res)
```
- `循环返回值实例`
``` scala
object DemoTest007 {
  def main(args: Array[String]): Unit = {
    /**
      * 对1 to 10 进行遍历
      * yield i 将每次循环得到i放入到集合Vector中,并返回给res
      */
    val res = for (i <- 1 to 10) yield {
      if (i % 2 == 0) {
        i
      } else {
        0
      }
    }
    println(res)
  }
}
```


##### 6.10.4.7 使用花括号{}代替小括号()
- `基本语法`
- 说明 : {}和()对于for表达式来说都可以使用.
- for推导式有一个不成文约定 : 当for推导式仅包含单一表达式时使用圆括号,当其包含多个表达式时使用大括号.
- 当使用{}来换行写表达式时,分号就不用编写.
``` scala
for(i <-1 to 3; j = i * 2) {
 println(" i= " + i + " j= " + j)
}
println("------------------------------------")
for {
  i <-1 to 3
  j = i * 2} {
  println(" i= " + i + " j= " + j)
}
```

##### 6.10.4.8 注意事项和细节说明
- 1.scala的for循环形式和java是较大差异,但是基本原理还是一样.
- 2.scala的for循环步长如何控制`! [for(i <-Range(1,3,2)]`
``` scala
for (i <- Range(1,10,2)){
  println(i)
}
```
- 3.使用循环守卫控制步长
``` scala
for (i <- 1 to 10 if i % 2 == 1) {
 println(i)
}
```

#### 6.10.5 while 循环控制
- `基本语法`
- 说明 : 循环条件是返回一个布尔值的表达式.
- while循环是先判断再执行语句.
- 与If语句不同，While语句本身没有值，即整个While语句的结果是Unit类型的()
- 因为while中没有返回值,所以当要用该语句来计算并返回结果时,就不可避免的使用变量，而变量需要声明在while循环的外部，那么就等同于循环的内部对外部的变量造成了影响，所以不推荐使用，而是推荐使用for循环
``` scala
while (循环条件) {
循环体(语句)
循环变量迭代
}
```
- `while实例`
``` scala
var i = 0
while (i < 10){
 println(i)
 i += 1
}
```

#### 6.10.6 do..while 循环控制
- `基本语法`
- 说明 : 循环条件是返回一个布尔值的表达式.
- do..while循环是先执行,再判断.
- 和while 一样,因为do...while中没有返回值,所以当要用该语句来计算并返回结果时,就不可避免的使用变量,而变量需要声明在do...while循环的外部,那么就等同于循环的内部对外部的变量造成了影响,所以不推荐使用,而是推荐使用for循环.
``` scala
do{
循环体(语句)
循环变量迭代
} while(循环条件)
```
- `do..while实例`
``` scala
var is = 0
do{
 println(is)
 is += 1
} while (is < 10)
```

#### 6.10.7 多重循环控制
- 说明 : 
- 将一个循环放在另一个循环体内,就形成了嵌套循环。其中for/while/do...while均可以作为外层循环和内层循环.(建议一般使用两层,最多不要超过3层)
- 实质上,嵌套循环就是把内层循环当成外层循环的循环体,当只有内层循环的循环条件为false时,才会完全跳出内层循环,才可结束外层的当次循环,开始下一次循环.
- 设外层循环次数为m次,内层为n次,则内层循环体实际上需要执行m*n=mn次.
- `实例`
``` scala
for (i <- 1 to 9){
 for (j <- 1 to i){
  printf("%d * %d = %d\t",j,i,j*i)
 }
  printf("\n")
}
```


#### 6.10.8 while 循环中断
- `基本语法`
- 说明 : Scala内置控制结构特地去掉了break和continue,是为了更好的适应函数化编程,推荐使用函数式的风格解决break和contine的功能,而不是一个关键字.
- breakable是一个高阶函数 : 可以接收函数的函数就是高阶函数.
- breakable对break()抛出异常做了处理,代码就继续执行.
- 当传入的是代码块,scala程序员会将()改成{}
- Scala内置控制结构特地也去掉了continue,是为了更好的适应函数化编程,可以使用if –else或是循环守卫实现continue效果.
- `实例`
``` scala
    var n = 1
    breakable {
      while (n <= 20) {
        n += 1
        println ("n=" + n)
        if (n == 18) {
          // 使用函数式break函数中断循环
          break()
        }
      }
    }
    println("ok")
```

### 6.11 Scala 函数式编程 基础
#### 6.11.1 函数式编程内容
> 函数式编程基础 : 
> 函数定义/声明
> 函数运行机制
> 递归 难点[最短路径,邮差问题,迷宫问题,回溯]
> 过程
> 过程
> 
> 函数式编程高级 : 
> 值函数(函数字面量)
> 高阶函数
> 闭包
> 应用函数
> 柯里化函数 抽象控制


#### 6.11.2 函数式编程介绍
> 在学习Scala中将方法 / 函数 / 函数式编程和面向对象编程需要明确 : 
> 1.在scala中方法和函数几乎可以等同(比如定义、使用、运行机制都一样),只是函数使用方式更加的灵活多样.
> 2.函数式编程是从编程方式(范式)角度来谈,可以这样理解 : 函数式编程把函数当做一等公民,充分利用函数、支持的函数多种使用方式.
> 3.面向对象编程是以对象为基础的编程方式.
> 4.在scala中函数式编程和面向对象编程融合在一起.
> 
> 函数式编程思想
> 函数式编程是一种"编程范式" (programming paradigm)
> 它属于"结构化编程"的一种,主要思想是把运算过程尽量写成一系列嵌套函数调用.
> 函数式编程中,将函数也当做数据类型,因此可以接受函数当作输入(参数)和输出(返回值).
> 函数式编程中最重要的就是函数.

#### 6.11.3 函数的定义
- `基本语法`
- 说明 : 
- 1.函数声明关键字为def (definition)
- 2.[参数名: 参数类型], ... 表示函数的输入(就是参数列表),,可以没有,如果有,多个参数使用逗号间隔.
- 3.函数中的语句 : 表示为了实现某一功能代码块.
- 4.函数可以有返回值,也可以没有
- 返回值形式1: 返回值类型 =
- 返回值形式2:  = 表示返回值类型不确定,使用类型推导完成.
- 返回值形式3: 表示没有返回值,return不生效.
- 5.如果没有return,默认以执行到最后一行的结果作为返回值.
```
def 函数名([参数名: 参数类型], ...)[[: 返回值类型] =] {
 语句...
 return 返回值
}
```
- `函数实例`
``` scala
object DemoTest009 {
  def main(args: Array[String]): Unit = {
    val sum: Any = getSum(10, 5, '+')
    println("res is = " + sum)
  }
  
  // 定义函数/方法
  def getSum(n1: Int, n2: Int, oper: Char) = {
    if (oper == '+') {
      n1 + n2
    } else if (oper == '-') {
      n1 - n2
    } else {
      null
    }
  }
}
```
#### 6.11.4 函数注意事项
- 1.函数的形参列表可以是多个,如果函数没有形参,调用时可以不带()
- 2.形参列表和返回值列表的数据类型可以是值类型和引用类型.
- 3.Scala中的函数可以根据函数体最后一行代码自行推断函数返回值类型,那么在这种情况下,return关键字可以省略.
- 4.因为Scala可以自行推断,所以在省略return关键字的场合,返回值类型也可以省略.
- 5.如果函数明确使用return关键字,那么函数返回就不能使用自行推断了,这时要明确写成: 返回类型=,当然如果什么都不写,即使有return返回值为()
- 6.如果函数明确声明无返回值(声明Unit),那么函数体中即使使用return关键字也不会有返回值.
- 7.如果明确函数无返回值或不确定返回值类型,那么返回值类型可以省略或声明为Any
- 8.Scala语法中任何的语法结构都可以嵌套其他语法结构(灵活),即函数中可以再声明/定义函数,类中可以再声明类,方法中可以再声明/定义方法.
- 9.Scala函数的形参,在声明参数时,直接赋初始值(默认值),这时调用函数时,如果没有指定实参,则会使用默认值,如果指定了实参,则实参会覆盖默认值.
- 10.如果函数存在多个参数,每一个参数都可以设定默认值,那么传递的参数到底是覆盖默认值,还是赋值给没有默认值的参数,就不确定了(默认按照声明顺序[从左到右]),在这种情况下,可以采用带名参数.
- 11.递归函数未执行之前是无法推断出来结果类型,在使用时必须有明确的返回值类型
- 12.Scala函数支持可变参数.
- 13


#### 6.11.5 过程
- `基本介绍`
- 将函数的返回值类型为Unit函数称为过程(procedure),如果明确函数没有返回值,那么等号可以省略.
- `注意事项`
- 1.注意区分 : 如果函数声明时没有返回值类型,但是有`=`等号,可以进行类型推断最后一行代码,这时这个函数实际是有返回值,该函数并不是过程.
- 2.开发工具自动代码补全功能,虽然会自动加上Unit,但是考虑到Scala语言简单灵活,最好不加.


#### 6.11.6 惰性函数
- 惰性计算(尽可能延迟表达式求值)是许多函数式编程语言的特性.
- 惰性集合在需要时提供其元素,无需预先计算它们,这带来了一些好处,首先可以将耗时的计算推迟到绝对需要的时候,其次可以创造无限个集合,只要它们继续收到请求,就会继续提供元素,函数的惰性使用让您能够得到更高效的代码,Java并没有为惰性提供原生支持,而Scala提供惰性函数.

##### 6.11.6.1 Java实现懒加载
``` java
public class LazyDemo {
    private String property;

    // 属性也可能是一个数据库连接,文件等资源
    public String getProperty() {
        if (property == null) {
            // 如果没有初始化过,那么进行初始化
            property = initProperty();
        }
        return property;
    }

    private String initProperty() {
        return "property";
    }
}
```
##### 6.11.6.2 惰性函数介绍
- 当函数返回值被声明为lazy时,函数的执行将被推迟,直到首次对此取值,该函数才会执行,这种函数称之为惰性函数,在Java的某些框架代码中称之为懒加载(延迟加载).
- `惰性函数实例`
```scala
object DemoTest010 {
  def main(args: Array[String]): Unit = {
    lazy val res = sum(10, 20)
    println("-----------------")
    println("res=" + res)
    def sum(n1: Int, n2: Int): Int = {
      println("sum() 执行..")
      return n1 + n2
    }
  }
}
```
- `注意事项`
- lazy不能修饰var类型变量.
- 不但是在调用函数时,加了lazy,会导致函数的执行被推迟,在声明一个变量时,如果给声明了lazy,那么变量值得分配也会推迟.


#### 6.11.7 异常
- Scala提供try和catch块来处理异常.
- try块用于包含可能出错的代码,catch块用于处理try块中发生的异常,可以根据需要在程序中有任意数量的try...catch块.
- 语法处理上和Java类似,但是又不尽相同.

##### 6.11.7.1 Java异常处理
``` java
public class JavaExceptionDemo01 {
    public static void main(String[] args) {
        try {
            // 可疑代码
            int i = 0;
            int b = 10;
            int c = b / i;
            // 执行代码时，会抛出ArithmeticException异常
        } catch (ArithmeticException ex) {
            ex.printStackTrace();
        } catch (Exception e) {
            //java中不可以把返回大的异常写在前，否则报错!!
            e.printStackTrace();
        } finally {
            // 最终要执行的代码
            System.out.println("java finally");
        }
        System.out.println("ok~~~继续执行...");
    }
}
```
##### 6.11.7.2 Java异常处理注意点
- java语言按照try—catch-catch...—finally的方式来处理异常.
- 不管有没有异常捕获,都会执行finally,因此通常可以在finally代码块中释放资源.
- 可以有多个catch,分别捕获对应的异常,这时需要把范围小的异常类写在前面,把范围大的异常类写在后面,否则编译错误,会提示"`Exception 'java.lang.xxxxxx' has already been caught`"


##### 6.11.7.3 Scala异常处理
``` scala
object DemoTest011 {
  def main(args: Array[String]): Unit = {
    try {
      val s = 10 / 0
    } catch {
      /**
        * 在scala中只有一个catch
        * 在catch中有多个case,每个case可以匹配一种异常case ex: ArithmeticException
        * => 关键符号,表示后面是对该异常的处理代码块
        * finally是最终执行
        **/
      case ex: ArithmeticException => println("Trapping arithmetic exception")
      case ex: Exception => println("Capture exception")
    } finally {
      println("Scala finally")
    }
    println("Continue execution")
  }
}
```
##### 6.11.7.4 Scala异常处理小结
- 1.将可疑代码封装在try块中,在try块之后使用了一个catch处理程序来捕获异常,如果发生任何异常,catch处理程序将处理它,程序将不会异常终止.
- 2.Scala异常的工作机制和Java一样,但是Scala没有“checked(编译期)”异常,即Scala没有编译异常概念,异常都是在运行时捕获处理.
- 3.用throw关键字,抛出一个异常对象,所有异常都是Throwable的子类型,throw表达式是有类型的,就是Nothing,因为Nothing是所有类型的子类型,所以throw表达式可以用在需要类型的地方.
- 4.在Scala里,借用了模式匹配的思想来做异常的匹配,因此在catch的代码里,是一系列case子句来匹配异常.当匹配上后=> 有多条语句可以换行写,类似java 的switch case x: 代码块
- 5.异常捕捉的机制与其他语言中一样，如果有异常发生，catch子句是按次序捕捉的。因此，在catch子句中,越具体的异常越要靠前m越普遍的异常越靠后m如果把越普遍的异常写在前m把具体的异常写在后m在scala中也不会报错m但这样是非常不好的编程风格.
- 6.finally子句用于执行不管是正常处理还是有异常发生时都需要执行的步骤,一般用于对象的清理工作,这点和Java一样.
- 7.Scala提供了throws关键字来声明异常,可以使用方法定义声明异常,它向调用者函数提供了此方法可能引发此异常的信息,它有助于调用函数处理并将该代码包含在try-catch块中,以避免程序异常终止,在scala中可以使用throws注释来声明异常.
``` scala
  def main(args: Array[String]): Unit = {
    f11()
  }

  //等同于NumberFormatException.class
  @throws(classOf[NumberFormatException])
  def f11() = {
    "abc".toInt
  }
```

### 6.12 Scala 面向对象编程 (基础部分)
#### 6.12.1 类与对象
##### 6.12.1.1 Scala语言是面向对象
- 1.Java是面向对象的编程语言,由于历史原因,Java中还存在着非面向对象的内容:基本类型,null,静态方法等.
- 2.Scala语言来自于Java,所以天生就是面向对象的语言,而且Scala是纯粹的面向对象的语言,即在Scala中一切皆为对象.
- 3.在面向对象的学习过程中可以对比着Java语言学习.
- `面向对象实例`
``` scala
object DemoTest013 {
  def main(args: Array[String]): Unit = {
    // 创建对象
    val cat = new CatDemo
    // 给对象属性赋值
    cat.name = "kaka"
    cat.age = 10
    cat.colour = "black"
    printf("Info : %s %d %s",cat.name,cat.age,cat.colour)
  }

  class CatDemo {
    // 定义声明属性
    var name: String = ""
    var age: Int = _
    var colour: String = ""
  }
}
```

##### 6.12.1.2 类和对象区别和联系
- 1.类是抽象概念,代表一类事物,比如人类,猫类
- 2.对象是具体实际,代表一个具体事物
- 3.类是对象模板,对象是类的一个个体,对应一个实例.
- 4.Scala中类和对象的区别和联系和Java是一样的.


##### 6.12.1.3 如何定义类
- `基本语法`
``` scala
[修饰符] class 类名{
 类体
}
```
- `定义类注意事项`
- 1.scala语法中,类并不声明为public,所有这些类都具有公有可见性(即默认就是public).
- 2.一个Scala源文件可以包含多个类,而且默认都是public


##### 6.12.1.4 属性
- `基本介绍`
- 属性是类的一个组成部分,一般是值数据类型,也可是引用类型.


##### 6.12.1.5 属性/成员变量
- `注意事项和细节说明`
- 1.属性定义语法同变量,示例 : `[访问修饰符] var 属性名称[：类型] = 属性值`
- 2.属性的定义类型可以为任意类型,包含值类型或引用类型.
- 3.Scala中声明一个属性,必须显示的初始化,然后根据初始化数据的类型自动推断,属性类型可以省略(这点和Java不同).
- 4.如果赋值为null,则一定要加类型,因为不加类型,那么该属性的类型就是Null类型.
- 5.如果在定义属性时,暂时不赋值,也可以使用符号_(下划线),让系统分配默认值.

| 类型      |     _ 对应默认值 |
| :--------: | :--------:|
| Byte / Short / Int / Long    |   0 |
| Float / Double    |   0.0 |
| String / 引用类型    |   null |
| Bollean    |   false |

##### 6.12.1.6 属性高级部分
- `说明`
- 属性的高级部分和构造器(构造方法/函数)相关.

##### 6.12.1.7 如何创建对象
- `基本语法`
- `val | var 对象名[：类型] = new 类型()`
- 说明
- 1.如果不希望改变对象引用(即 : 内存地址),应该声明为val性质,否则声明为var,scala设计者推荐使用val,因为一般来说在程序中,只是改变对象属性值,而不是改变对象的引用.
- 2.scala在声明对象变量时,可以根据创建对象的类型自动推断,所以类型声明可以省略,但当类型和后面new对象类型有继承关系即多态时就必须编写.



#### 6.12.2 方法
#### 6.12.3 类与对象应用实例
#### 6.12.4 构造器
#### 6.12.5 属性高级
#### 6.12.6 Scala对象创建流程分析





## 🔒 尚未解锁 正在探索中... 尽情期待 Blog更新! 🔒
### 6.13 Scala 面向对象编程 (中级部分)
### 6.14 Scala 面向对象编程 (高级特性)
### 6.15 Scala 隐式转换 & 隐式值
### 6.16 Scala 数据结构 (上) - 集合
### 6.17 Scala 数据结构 (下) - 集合操作
### 6.18 Scala 模式匹配
### 6.19 Scala 函数式编程 高级
### 6.20 Scala 使用递归方式去思考编程


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