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
  * HackerParkHub | 黑客公园
  * Website | https://www.hackerparkhub.org/
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
 * HackerParkHub | 黑客公园
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
  * HackerParkHub | 黑客公园
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
- 1.Scala与Java有着相同的数据类型,在Scala中数据类型都是对象,也就是说Scala没有Java中的原生类型.
- 2.Scala数据类型分为两大类`AnyVal(值类型)`和`AnyRef(引用类型)`,注意:不管是AnyVal还是AnyRef都是对象.
- 3.相对于java类型系统,scala要复杂些,也正是这复杂多变的类型系统才让面向对象编程和函数式编程完美的融合在一起.

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
- 1.Scala对各种变量、方法、函数等命名时使用的字符序列称为标识符
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
> 1.函数的形参列表可以是多个,如果函数没有形参,调用时可以不带()
> 
> 2.形参列表和返回值列表的数据类型可以是值类型和引用类型.
> 
> 3.Scala中的函数可以根据函数体最后一行代码自行推断函数返回值类型,那么在这种情况下,return关键字可以省略.
> 
> 4.因为Scala可以自行推断,所以在省略return关键字的场合,返回值类型也可以省略.
> 
> 5.如果函数明确使用return关键字,那么函数返回就不能使用自行推断了,这时要明确写成: 返回类型=,当然如果什么都不写,即使有return返回值为()
> 
> 6.如果函数明确声明无返回值(声明Unit),那么函数体中即使使用return关键字也不会有返回值.
> 
> 7.如果明确函数无返回值或不确定返回值类型,那么返回值类型可以省略或声明为Any
> 
> 8.Scala语法中任何的语法结构都可以嵌套其他语法结构(灵活),即函数中可以再声明/定义函数,类中可以再声明类,方法中可以再声明/定义方法.
> 
> 9.Scala函数的形参,在声明参数时,直接赋初始值(默认值),这时调用函数时,如果没有指定实参,则会使用默认值,如果指定了实参,则实参会覆盖默认值.
> 
> 10.如果函数存在多个参数,每一个参数都可以设定默认值,那么传递的参数到底是覆盖默认值,还是赋值给没有默认值的参数,就不确定了(默认按照声明顺序[从左到右]),在这种情况下,可以采用带名参数.
> 
> 11.递归函数未执行之前是无法推断出来结果类型,在使用时必须有明确的返回值类型.
> 
> 12.Scala函数支持可变参数.

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
> 1.将可疑代码封装在try块中,在try块之后使用了一个catch处理程序来捕获异常,如果发生任何异常,catch处理程序将处理它,程序将不会异常终止.
> 
> 2.Scala异常的工作机制和Java一样,但是Scala没有“checked(编译期)”异常,即Scala没有编译异常概念,异常都是在运行时捕获处理.
> 
> 3.用throw关键字,抛出一个异常对象,所有异常都是Throwable的子类型,throw表达式是有类型的,就是Nothing,因为Nothing是所有类型的子类型,所以throw表达式可以用在需要类型的地方.
> 
> 4.在Scala里,借用了模式匹配的思想来做异常的匹配,因此在catch的代码里,是一系列case子句来匹配异常.当匹配上后=> 有多条语句可以换行写,类似java 的switch case x: 代码块.
> 
> 5.异常捕捉的机制与其他语言中一样，如果有异常发生，catch子句是按次序捕捉的。因此，在catch子句中,越具体的异常越要靠前m越普遍的异常越靠后m如果把越普遍的异常写在前m把具体的异常写在后m在scala中也不会报错m但这样是非常不好的编程风格.
> 
> 6.finally子句用于执行不管是正常处理还是有异常发生时都需要执行的步骤,一般用于对象的清理工作,这点和Java一样.
> 
> 7.Scala提供了throws关键字来声明异常,可以使用方法定义声明异常,它向调用者函数提供了此方法可能引发此异常的信息,它有助于调用函数处理并将该代码包含在try-catch块中,以避免程序异常终止,在scala中可以使用throws注释来声明异常.
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
- Scala中方法其实就是函数,声明规则请参考函数式编程中函数声明.
- `基本语法`
``` scala
def 方法名(参数列表) [：返回值类型] = {
 方法体
}
```

#### 6.12.3 构造器
##### 6.12.3.1 Java 构造器
```
[修饰符] 方法名(参数列表){
 构造方法体
}
```
- `Java构造器特点`
- 在Java中一个类可以定义多个不同的构造方法,构造方法重载.
- 如果没有定义构造方法,系统会自动给类生成一个默认无参构造方法(也叫默认构造器).
- 一旦定义了自己的构造方法(构造器),默认的构造方法就被覆盖,就不能再使用默认无参构造方法.

##### 6.12.3.2 Scala 构造器
- 和Java一样,Scala构造对象也需要调用构造方法,并且可以有任意多个构造方法(即scala中构造器也支持重载).
- Scala类的构造器包括 : 主构造器和辅助构造器.
- `Scala构造器基本语法`
- 说明 : 辅助构造器函数的名称this,可以有多个,编译器通过不同参数来区分.
``` scala
// 主构造器
class 类名(形参列表) {    
// 类体
def this(形参列表) {
 // 辅助构造器
}

def this(形参列表) {    
 // 辅助构造器可以有多个...
 }
}
```
- `Scala 构造器实例`
``` scala
object DemoTest015 {
  def main(args: Array[String]): Unit = {
    // 初始化对象
    val people = new People("tom", 18)
    println(people)
  }

  // 创建类
  class People(inName: String, inAge: Int) {
    // 定义属性
    var name: String = inName
    var age: Int = inAge

    // 重写toString方法
    override def toString: String = {
      "name = " + this.name + " , age = " + this.age
    }
  }
}
```

##### 6.12.3.3 Scala构造器注意事项
- 1.Scala构造器作用是完成对新对象的初始化,构造器没有返回值.
- 2.主构造器的声明直接放置于类名之后.
- 3.主构造器会执行类定义中的所有语句,这里可以体会到Scala函数式编程和面向对象编程融合在一起,即构造器也是方法(函数),传递参数和使用方法和前面的函数部分内容没有区别.
- 4.如果主构造器无参数,小括号可省略,构建对象时调用的构造方法的小括号也可以省略.
- 5.辅助构造器名称为this(和Java是不一样),多个辅助构造器通过不同参数列表进行区分,在底层就是构造器重载.
- 6.如果想让主构造器变成私有,可以在()之前加上private,这样只能通过辅助构造器来构造对象.
- 7.辅助构造器的声明不能和主构造器的声明一致,会发生错误(即构造器名重复).

#### 6.12.4 属性高级
##### 6.12.4.1 构造器参数
- 1.Scala类的主构造器的形参未用任何修饰符修饰,那么这个参数是局部变量.
- 2.如果参数使用val关键字声明,那么Scala会将参数作为类的私有的只读属性使用.
- 3.如果参数使用var关键字声明,那么那么Scala会将参数作为类的成员属性使用,并会提供属性对应xxx()[类似getter]/xxx_$eq()[类似setter]方法,即这时的成员属性是私有,但是可读写.
- `构造器参数实例`
``` scala
package com.geekparkhub.core.scala.demo

object DemoTest016 {
  def main(args: Array[String]): Unit = {

    val worker = new worker("tom")
    worker.name

    val worker2 = new worker2("jack")
    worker2.inName

    val worker3 = new worker3("macs")
    worker3.inName = "tomcat"
    println(worker3.inName)
  }

  class worker(inName: String) {
    var name = inName
  }

  // 只读属性
  class worker2(val inName: String) {
    var name = inName
  }

  // 可读写属性
  class worker3(var inName: String) {
    var name = inName
  }
}
```
##### 6.12.4.2 Bean属性
- JavaBeans规范定义了Java属性是像getXxx()和setXxx()方法.
- 许多Java工具(框架)都依赖命名习惯,为了Java互操作性,将Scala字段加`@BeanProperty`时,这样会自动生成规范的setXxx/getXxx方法,这时可以使用对象.setXxx()和对象.getXxx()来调用属性.
- 注意:给某个属性加入`@BeanPropetry`注解后,会生成getXXX和setXXX方法,并且对原来底层自动生成类似xxx(),xxx_$eq()方法,没有冲突,二者可以共存.
- `Bean属性实例`
``` scala
object DemoTest017 {
  def main(args: Array[String]): Unit = {
    val car = new Car()
    car.name = "G500"
    println(car.name)

    car.setName("G630")
    println(car.getName)
  }

  class Car {
    @BeanProperty var name: String = _
  }
}
```


#### 6.12.5 Scala对象创建流程分析
- 对象创建实例
``` scala
class Person {
 var age: Short = 90
 var name: String = _
def this(n: String, a: Int) {
 this()
 this.name = n
 this.age = a
 }
}
var p : Person = new Person("tom",18)
```
- 流程分析
- 1.加载类的信息(属性信息,方法信息)
- 2.在内存中(堆)开辟空间
- 3.使用父类构造器(主和辅助)进行初始
- 4.使用主构造器对属性进行初始化(age:18,name:null)
- 5.使用辅助构造器对属性进行初始化(age:18,name:tom)
- 6.将开辟对象的地址赋给p的引用


### 6.13 Scala 面向对象编程 (中级部分)
#### 6.13.1 包
##### 6.13.1.1 Java包三大作用
- 1.区分相同名称的类
- 2.当类很多时,可以很好管理类
- 3.控制访问范围
##### 6.13.1.2 Java打包命令
- 打包基本语法
```
package com.geekparkhub.core
```
- 打包的本质分析
- 实际上就是创建不同文件夹来保存类文件

##### 6.13.1.3 Scala包基本介绍
- 和Java一样,Scala中管理项目可以使用包,但Scala中的包的功能更加强大,使用也相对复杂些.
##### 6.13.1.4 Scala包快速入门
- 在不用包下创建相同名称类
```  scala
package com.geekparkhub.core.scala.package_flow.test001

class Test {

}
```
``` scala
package com.geekparkhub.core.scala.package_flow.test002

class Test {

}
```
- 创建对象
``` scala
package com.geekparkhub.core.scala.package_flow

object PackageTest {
  def main(args: Array[String]): Unit = {
    val test001 = new com.geekparkhub.core.scala.package_flow.test001.Test
    val test002 = new com.geekparkhub.core.scala.package_flow.test002.Test
    println("test001 = " + test001 + "\n" + "test002 = " + test002)
  }
}
```
- 运行程序查看日志计结果
```
test001 = com.geekparkhub.core.scala.package_flow.test001.Test@56cbfb61
test002 = com.geekparkhub.core.scala.package_flow.test002.Test@1134affc
```
##### 6.13.1.5 Scala包特点概述
- 基本语法
```
package 包名
```
- Scala包的三大作用(和Java一样)
- 1.区分相同名称的类
- 2.当类很多时,可以很好的管理类
- 3.控制访问范围
- 4.可以对类的功能进行扩展
- Scala中包名和源码所在系统文件目录结构要可以不一致,但是编译后的字节码文件路径和包名会保持一致.

##### 6.13.1.6 Scala包命名
- 命名规则 : 
- 只能包含数字、字母、下划线、点,但不能以数字开头,也不要使用关键字.
- 命名规范 : 
- `com.公司名称.项目名称.业务模块名称`

##### 6.13.1.7 Scala自动引入常用包
`java.lang.*` / `scala包` / `Predef包`


##### 6.13.1.8 Scala包注意事项和使用细节
- 1.包也可以像嵌套类那样嵌套使用(包中有包),在使用第三种方式时的好处是:可以在同一个文件中,将类(class / object)、trait创建在不同的包中,这样就非常灵活.
- 包嵌套实例
``` scala
package com.geekparkhub.core.scala.package_flow

/**
  * 创建test003包
  */
package test003 {
  /**
    * 创建类
    */
  class Test {
    // 定义属性
    var name: String = _

    // 定义函数
    def info(name: String): Unit = {
      println("name")
    }
  }
  /**
    * 创建对象
    */
  object RunTest003 {
    def main(args: Array[String]): Unit = {
      // 实例化对象
      val test003 = new Test()
      // 调用对象函数
      test003.info("tomcat")
      println("test003 is = " + test003)
    }
  }
}

/**
  * 创建包test004包
  */
package test004 {
  /**
    * 创建类
    */
  class Test {
    // 定义属性
    var age: Int = _
    // 定义函数
    def infos(age: Int): Unit = {
      println("age")
    }
  }
  /**
    * 创建对象
    */
  object RunTest004 {
    def main(args: Array[String]): Unit = {
      val test004 = new Test()
      test004.infos(18)
      println("test004 is = " + test004)
    }
  }
}
```
- 2.作用域原则 : 可以直接向上访问,即: Scala中子包中直接访问父包中的内容,大括号体现作用域,(提示:Java中子包使用父包的类,需要import),在子包和父包类重名时,默认采用就近原则,如果希望指定使用某个类,则带上包名即可.
- 3.父包要访问子包的内容时,需要import对应的类等.
- 4.可以在同一个.scala文件中,声明多个并列的package(建议嵌套的pakage不要超过3层).
- 5.包名可以相对也可以绝对,比如访问`BeanProperty`绝对路径是：`_root_. scala.beans.BeanProperty` ,在一般情况下:使用相对路径来引入包,只有当包名冲突时,使用绝对路径来处理.


##### 6.13.1.9 包对象
- 包可以包含类、对象和特质trait,但不能包含函数/方法或变量的定义,这是Java虚拟机的局限,为了弥补这一点不足,scala提供了包对象的概念来解决这个问题.
- `包对象实例`
``` scala
package com.geekparkhub.core.scala.package_flow {

  /**
    * 创建包对象
    *
    * 每一个包都可以有一个包对象
    * 包对象名称字需要和子包一致
    * 在包对象中可以定义变量,方法
    * 在包对象中定义的变量和方法,就可以在对应的包中使用
    */
  package object scala {
    // 定义属性
    var age: Int = 18
    // 定义函数
    def info(): Unit = {
      println("this info")
    }
  }

  /**
    * 创建包
    */
  package scala {
    // 创建类
    class Test {
      var name: String = _
    }
    // 创建主函数
    object RunTest {
      def main(args: Array[String]): Unit = {
        // 调用包对象属性
        println("age = " + age)
        // 调用包对象函数
        info()
      }
    }
  }
}
```
##### 6.13.1.9 包对象注意事项
- 每个包都可以有一个包对象.
- 包对象名称需要和包名一致.

#### 6.13.2 包可见性问题
##### 6.13.2.1 Java访问修饰符
- java提供四种访问控制修饰符号控制方法和变量访问权限(范围):
- 1.公开级别:用public修饰,对外公开.
- 2.受保护级别:用protected修饰,对子类和同一个包中的类公开.
- 3.默认级别:没有修饰符号,向同一个包的类公开.
- 4.私有级别:用private修饰,只有类本身可以访问,不对外公开.

##### 6.13.2.2 Java访问修饰符使用注意事项
- 1.修饰符可以用来修饰类中的属性,成员方法以及类.
- 2.只有默认的和public才能修饰类,并且遵循上述访问权限的特点.

##### 6.13.2.3 Scala 包可见性
- 在Java中,访问权限分为: public,private,protected和默认.
- 在Scala中,可以通过类似修饰符达到同样效果,但是使用上有区别.
- `包可见性实例`
``` scala
package com.geekparkhub.core.scala.package_flow

object Visit {
  def main(args: Array[String]): Unit = {
    // 实例化对象
    val test = new Test
    // 调用info函数
    test.info()
    // 调用半生对象函数
    Test.run(test)
  }

  // 创建半生类
  class Test {
    // 定义属性
    var name: String = "tomcat"
    // 定义私有属性
    private var age: Int = 18
    // 定义函数
    def info(): Unit = {
      println("name is " + name + " , " + "age is " + age)
    }
  }

  // 创建半生对象
  object Test {
    def run(t: Test) {
      println("name = " + t.name + " , age = " + t.age)
    }
  }
}
```
##### 6.13.2.4 Scala 包可见性和访问修饰符使用
> 1.当属性访问权限为默认时,从底层看属性是private,但是因为提供了`xxx_$eq()`[类似setter]/xxx()[类似getter]方法,因此从使用效果看是任何地方都可以访问.
> 
> 2.当方法访问权限为默认时,默认为public访问权限.
> 
> 3.private为私有权限,只在类内部和伴生对象中可用.
> 
> 4.protected为受保护权限,scala中受保护权限比Java中更严格,只能子类访问,同包无法访问.
> 
> 5.在scala中没有public关键字,即不能用public显式修饰属性和方法.
> 
> 6.包访问权限(表示属性有限制,同时包也有限制),这点和Java不一样,体现出Scala包使用的灵活性.
> 
- `包访问权限实例`
```  scala
package com.geekparkhub.core.scala.package_flow

object Visit {
  def main(args: Array[String]): Unit = {
    // 实例化对象
    val test = new Test
    // 调用半生类属性
    println("age is = " + test.age)
  }

  // 创建半生类
  class Test {
    // 定义属性
    var name: String = "tomcat"
    // 定义私有属性
    private[package_flow] var age: Int = 18
    // 定义函数
    def info(): Unit = {
      println("name is " + name + " , " + "age is " + age)
    }
  }

  // 创建半生对象
  object Test {
    def run(t: Test) {
      println("name = " + t.name + " , age = " + t.age)
    }
  }
}
```
#### 6.13.3 包引入
##### 6.13.3.1 Scala引入包基本介绍
- Scala引入包也是使用`import`,基本的原理和机制和Java一样,但是Scala中的import功能更加强大,也更灵活.
- 因为Scala语言源自于Java,所以java.lang包中的类会自动引入到当前环境中,而Scala中的scala包和Predef包的类也会自动引入到当前环境中,即起其下面的类可以直接使用.
- 如果想要把其他包中的类引入到当前环境中,需要使用import语言.
##### 6.13.3.2 Scala引入包细节和注意事项
- 1.在Scala中,import语句可以出现在任何地方,并不仅限于文件顶部,import语句的作用一直延伸到包含该语句的块末尾,这种语法的好处是:在需要时在引入包,缩小import包的作用范围,提高效率.
- 2.Java中如果想要导入包中所有的类,可以通过通配符`*`,Scala中采用下划线`_`
- 3.如果不想要某个包中全部的类,而是其中的几个类,可以采用选取器(大括号).
- 4.如果引入的多个包中含有相同的类,那么可以将不需要的类进行重命名进行区分,这个就是重命名.
- 5.如果某个冲突的类根本就不会用到,那么这个类可以直接隐藏掉.

#### 6.13.4 面向对象编程 三大特征
- 面向对象编程有三大特征 : 封装 / 继承 / 多态

#### 6.13.5 面向对象编程方法 - 抽象
- 实际上就是把一类事物共有的属性和行为提取出来,形成一个物理物理模型,这种方式就称之为抽象.

##### 6.13.5.1 Scala 抽象快速入门案例
- `抽象实例`
``` scala
package com.geekparkhub.core.scala.demo

object AbstractBankDemo {
  def main(args: Array[String]): Unit = {
    // 创建 账户类
    val account = new Account("4693803346873533", 5.0, "123456")

    // 调用 查询余额函数
    account.check_balances("4693803346873533", "123456")

    // 调用 存款函数
    account.deposit("4693803346873533","123456",1.1)

    // 调用 取款函数
    account.withDrawal("4693803346873533","123456",0.6)
  }

  /**
    * 创建银行账户类
    * 共有信息属性
    * 账户/余额/密码/查询余额/取款/存款
    */
  class Account(inAccount: String, inBalance: Double, inPassword: String) {
    // 定义银行账户属性
    private val account: String = inAccount
    // 定义银行余额属性
    private var balance: Double = inBalance
    // 定义银行密码属性
    private var password: String = inPassword

    /**
      * 定义银行查询余额函数
      *
      * @param account
      * @param password
      */
    def check_balances(account: String, password: String): Any = {
      if (!this.account.equals(account)) {
        println("Account error, please verify your account!")
        return
      }
      if (!this.password.equals(password: String)) {
        println("The password is wrong, please try again!")
        return
      }
      printf("Account : %s\nBalance : %.2f\n", this.account, this.balance)
    }

    /**
      * 定义银行取款函数
      *
      * @param password
      * @param money
      */
    def withDrawal(account: String, password: String, money: Double): Any = {
      if (!this.account.equals(account)) {
        println("Account error, please verify your account!")
        return
      }
      if (!this.password.equals(password)) {
        println("The password is wrong, please try again!")
        return
      }
      if (this.balance < money) {
        println("Failed withdrawal, insufficient current account balance!")
        return
      }
      this.balance -= money
      money
      printf("Account : %s\nBalance : %.2f\n", this.account, this.balance)
    }

    /**
      * 定义银行存款函数
      *
      * @param account
      * @param password
      * @param money
      */
    def deposit(account: String, password: String, money: Double): Any = {
      if (!this.account.equals(account)) {
        println("Account error, please verify your account!")
        return
      }
      if (!this.password.equals(password)) {
        println("The password is wrong, please try again!")
        return
      }
      this.balance += money
      money
      printf("Account : %s\nBalance : %.2f\n", this.account, this.balance)
    }
  }
}
```

#### 6.13.6 面向对象编程 - 封装
##### 6.13.6.1 封装介绍
- 封装(encapsulation)就是把抽象出的数据和对数据的操作封装在一起,数据被保护在内部,程序的其它部分只有通过被授权的操作(成员方法),才能对数据进行操作.

##### 6.13.6.2 封装理解和好处
- 1.隐藏实现细节
- 2.提可以对数据进行验证,保证安全合理
- 3.同时可以加入业务逻辑

##### 6.13.6.3 如何体现封装
- 1.对类中的属性进行封装.
- 2.通过成员方法,包实现封装

##### 6.13.6.4 封装 实现步骤
- 1.将属性进行私有化.
- 2.提供一个公共的set方法,用于对属性判断并赋值.
- 3.提供一个公共的get方法,用于获取属性的值.

##### 6.13.6.5 Scala 封装快速入门案例
``` scala
package com.geekparkhub.core.scala.demo

object AccountCore {
  def main(args: Array[String]): Unit = {
    val account = new Account_Flow("4693803346873533", "张三丰", 110, "123456")
    account.setName("初始值")
    account.setPassword("111111")
    account.setBalance(100)
  }

  class Account_Flow(inAccount: String, inName: String, inBalance: Double, inPassword: String) {
    // 定义银行账户属性
    private val account: String = inAccount
    // 定义银行用户名属性
    private var name: String = ""
    // 定义银行余额属性
    private var balance: Double = inBalance
    // 定义银行密码属性
    private var password: String = inPassword
    
    // 设置用户名限制
    def setName(name: String): Unit = {
      if (!this.inName.length.equals(name.length)) {
        printf("初始化(%s)账户名设置必须大于三位,请重试!\n", this.account)
        return
      } else {
        this.name = name
        println("账户名设置成功!")
      }
    }

    // 设置用户密码限制
    def setPassword(password: String): Unit = {
      if (!this.inPassword.length.equals(password.length)) {
        printf("初始化(%s)账户密码必须设置大于6位数以上,请重试!\n", this.account)
        return
      }
      this.password = password
      println("账户密码设置成功!")
    }

    // 设置余额限制
    def setBalance(balance: Double): Unit = {
      if (this.inBalance.toDouble < balance) {
        printf("当前(%s)账户余额不足:%.2f,请及时充值!\n", this.account,this.balance)
        return
      }
      this.balance = balance
      printf("当前(%s)账户余额%.2f", this.account, this.balance)
    }
  }
}
```

##### 6.13.6.6 Scala 封装注意事项
- 1.Scala中为了简化代码的开发,当声明属性var时,本身就自动提供了对应setter/getter方法,如果属性声明为private,那么自动生成的setter/getter方法也是private,如果属性省略访问权限修饰符,那么自动生成的setter/getter方法是public.
- 2.目前很多新的框架.在进行反射时,也支持对属性的直接反射.

#### 6.13.7 面向对象编程 - 继承
##### 6.13.7.1 Java继承
```
class 子类名extends 父类名{ 类体}
子类继承父类的属性和方法
```
##### 6.13.7.2 继承基本介绍
- 继承可以解决代码复用,让编程更加靠近人类思维.当多个类存在相同的属性(变量)和方法时,可以从这些类中抽象出父类(比如Student),在父类中定义这些相同的属性和方法,所有的子类不需要重新定义这些属性和方法,只需要通过extends语句来声明继承父类即可.
- 和Java一样,Scala也支持类的单继承.

##### 6.13.7.3 Scala 继承基本语法
```
class 子类名 extends 父类名 { 类体 }
```
##### 6.13.7.4 Scala 继承快速入门
``` scala
package com.geekparkhub.core.scala.demo

object DemoTest018 {
  def main(args: Array[String]): Unit = {
    val teacher = new Teacher
    teacher.name = "Tomcat"
    teacher.work()
  }

  class Person {
    var name: String = _
    var age: Int = _
    def info(): Unit = {
      println("info : " + this.name)
    }
  }

  class Teacher extends Person {
    def work(): Unit = {
      println(this.name + " Working!")
    }
  }
}
```
##### 6.13.7.5 Scala继承优势
- 1.代码复用性提高
- 2.代码扩展性和维护性提高,当修改父类时,对应的子类就会继承相应的方法和属性.
##### 6.13.7.6 重写方法
- scala明确规定,重写一个非抽象方法需要用override修饰符,调用超类的方法使用super关键字.
``` scala
package com.geekparkhub.core.scala.demo

object DemoTest018 {
  def main(args: Array[String]): Unit = {
    val teacher = new Teacher
    teacher.name = "Tomcat"
    teacher.info()
    teacher.work()
  }

  class Person {
    var name: String = "mac"
    var age: Int = _
    def info(): Unit = {
      println("info : " + this.name)
    }
  }

  class Teacher extends Person {
    override def info() {
      println("override info : "+ name)
      super.info()
    }
    def work(): Unit = {
      println(this.name + " Working!")
    }
  }
}
```
##### 6.13.7.7 Scala中类型检查和转换
- 基本介绍
- 要测试某个对象是否属于某个给定的类,可以用isInstanceOf方法,用asInstanceOf方法将引用转换为子类的引用,classOf获取对象的类名.
- `classOf[String]`就如同JavaString.class
- `obj.isInstanceOf[T]`就如同Java obj instanceof T 判断obj是不是T类型.
- `obj.asInstanceOf[T]`就如同Java(T)obj 将obj强转成T类型.
- 类型检查和转换的最大价值在于 : 可以判断传入对象的类型,然后转成对应的子类对象,进行相关操作,这里也体现出多态的特点.
``` scala
package com.geekparkhub.core.scala.demo

object DemoTest019 {
  def main(args: Array[String]): Unit = {
    // 使用ClassOf得到类名
    println(classOf[String])
    var str = "tomcat"
    println(str.getClass.getName)

    // 将子类引用给父类(向上转型,自动)
    var base = new Base
    var teacher = new Teacher
    base = teacher

    // 将父类的引用重新转成子类引用(多态),即向下转型
    var teachers = base.asInstanceOf[Teacher]
    teachers.work()
  }

  class Base {
    var name: String = "mac"
    var age: Int = _

    def info(): Unit = {
      println("info : " + this.name)
    }
  }

  class Teacher extends Base {
    override def info() {
      println("override info : " + name)
      super.info()
    }

    def work(): Unit = {
      println(this.name + " Working!")
    }
  }
}
```

##### 6.13.7.8 Scala超类构造
- 类有一个主构器和任意数量的辅助构造器,而每个辅助构造器都必须先调用主构造器(也可以是间接调用.)
- 只有主构造器可以调用父类的构造器,辅助构造器不能直接调用父类的构造器.

##### 6.13.7.9 覆写字段
- 在Scala中,子类改写父类的字段,称为覆写/重写字段,覆写字段需使用override修饰.
- `覆写字段注意事项和细节`
- def只能重写另一个def(即:方法只能重写另一个方法)
- val只能重写另一个val 属性或重写不带参数的def
- 抽象属性 : 声明未初始化的变量就是抽象的属性,抽象属性在抽象类
- 一个属性没有初始化,那么这个属性就是抽象属性.
- 抽象属性在编译成字节码文件时,属性并不会声明,但是会自动生成抽象方法,所以类必须声明为抽象类.
- 如果是覆写一个父类的抽象属性,那么override 关键字可省略[原因 : 父类的抽象属性,生成的是抽象方法,因此就不涉及到方法重写的概念,因此override可省略].

##### 6.13.7.10 抽象类
- 在Scala中,通过abstract关键字标记不能被实例化的类.
- 方法不用标记abstract,只要省掉方法体即可,抽象类可以拥有抽象字段,抽象字段/属性就是没有初始值的字段.
- 说明 : 抽象类的价值更多是在于设计,是设计者设计之后,让子类继承并实现抽象类方法.
- `抽象类实例`
``` scala
package com.geekparkhub.core.scala.demo

object DemoTest022 {
  def main(args: Array[String]): Unit = {
    println("abstract")
  }

  // 抽象类
  abstract class Base {
    // 抽象字段
    var name: String
    // 抽象字段
    var age: Int
    // 普通属性
    var color: String = "black"

    // 抽象方法,不需要标记abstract
    def cry()
  }
}
```
##### 6.13.7.11 Scala 抽象类使用注意事项
- 1.抽象类不能被实例.
- 2.抽象类不一定要包含abstract方法,也就是说抽象类可以没有abstract方法.
- 3.一旦类包含了抽象方法或者抽象属性,则这个类必须声明为abstrac
- 4.抽象方法不能有主体,不允许使用abstract修饰.
- 5.如果一个类继承了抽象类,则它必须实现抽象类的所有抽象方法和抽象属性,除非它自己也声明为abstract类.
- 6.抽象方法和抽象属性不能使用private、final来修饰,因为这些关键字都是和重写/实现相违背.
- 7.抽象类中可以有实现方法.
- 8.子类重写抽象方法不需要override

##### 6.13.7.12 匿名子类
- 和Java一样,可以通过包含带有定义或重写的代码块的方式创建一个匿名的子类.
- `匿名子类案例`
``` scala
package com.geekparkhub.core.scala.demo

object DemoTest023 {
  def main(args: Array[String]): Unit = {
  
    val base = new Base {
      override var name: String = "Mac"
      override def cry(): Unit = {
        println("Anonymous subclass\t" + name)
      }
    }
    base.cry()
  }

  abstract class Base {
    var name: String
    def cry()
  }
}
```
##### 6.13.7.13 继承层级
- 1.在scala中,所有其他类都是AnyRef的子类,类似Java Object
- 2.AnyVal和AnyRef都扩展自Any类,Any类是根节点.
- 3.Any中定义了isInstanceOf、asInstanceOf方法,以及哈希方法等.
- 4.Null类型的唯一实例就是null对象,可以将null赋值给任何引用,但不能赋值给值类型的变量.
- 5.Nothing类型没有实例,它对于泛型结构是有用处的,举例 : 空列表Nil的类型是List[Nothing],它是List[T]的子类型,T可以是任何类.


### 6.14 Scala 面向对象编程 (高级特性)
#### 6.14.1 静态属性和静态方法
- Scala中静态概念-伴生对象
- Scala语言是完全面向对象(万物皆对象)的语言，所以并没有静态的操作(即在Scala中没有静态的概念)。但是为了能够和Java语言交互(因为Java中有静态概念)，就产生了一种特殊的对象来模拟类对象，我们称之为类的伴生对象。这个类的所有静态内容都可以放置在它的伴生对象中声明和调用.
- `伴生对象快速入门`
``` scala
package com.geekparkhub.core.scala.demo

object DemoTest024 {
  def main(args: Array[String]): Unit = {
    println(Base.sex)
    Base.info()
  }

  // 半生类
  class Base{
    var name : String = _
  }

  // 半生对象
  object Base{
    var sex : Boolean = true
    def info(): Unit ={
      println("object ScalaPerson")
    }
  }
}
```
- 伴生对象总结
- Scala中伴生对象采用object关键字声明,伴生对象中声明的全是"静态"内容,可以通过伴生对象名称直接调用.
- 伴生对象对应的类称之为伴生类,伴生对象的名称应该和伴生类名一致.
- 伴生对象中的属性和方法都可以通过伴生对象名(类名)直接调用访问.
- 从语法角度来讲,所谓的伴生对象其实就是类的静态方法和成员的集合.
- 从技术角度来讲,scala还是没有生成静态的内容,只不过是将伴生对象生成了一个新的类,实现属性和方法的调用.
- 从底层原理看伴生对象实现静态特性是依赖于`public static final MODULE$`实现.

#### 6.14.2 接口
##### 6.14.2.1 Java 接口
- interface 接口名
- class 类名implements 接口名1,接口2
- java接口使用
- 在Java中,一个类可以实现多个接口.
- 在Java中,接口之间支持多继承.
- 接口中属性都是常量
- 接口中的方法都是抽象

##### 6.14.2.2 Scala 接口
- 从面向对象来看,接口并不属于面向对象的范畴,Scala是纯面向对象的语言,在Scala中,没有接口.
- Scala语言中,采用特质trait(特征)来代替接口的概念,也就是说多个类具有相同的特征(特征)时,就可以将这个特质(特征)独立出来,采用关键字trait声明,理解trait等价于(interface + abstract class)

#### 6.14.3 特质 (trait)
##### 6.14.3.0 Scala 创建对象时有四种方式
- 1.new Object
- 2.apply 创建
- 3.匿名子类 创建
- 4.动态混入

##### 6.14.3.1 trait 声明语法
- 说明 : 
- trait命名一般首字母大写
```
trait 特质名{
 trait体
}
```
##### 6.14.3.2 Scala trait 使用
- 一个类具有某种特质(特征),就意味着这个类满足了这个特质(特征)所有要素,所以在使用时也采用了extends关键字,如果有多个特质或存在父类,那么需要采用with关键字连接.
```
没有父类
class   类名extends     特质1      with       特质2      with     特质3...

有父类
class   类名extends     父类with   特质1      with     特质2      with 特质3
```
##### 6.14.3.3 特质快速入门
``` scala
package com.geekparkhub.core.scala.demo

object DemoTest025 {
  def main(args: Array[String]): Unit = {
    val c  = new C()
    c.getConnect()
    val f = new F()
    f.getConnect()
  }

  // 定义特质
  trait Base {
    def getConnect()
  }

  // A类
  class A {}

  // B类
  class B extends A {}

  // C类
  class C extends A with Base {
    override def getConnect(): Unit = {
      println("Connect to a new network")
    }
  }

  // D类
  class D {}

  // E类
  class E extends D {}

  // F类
  class F extends D with Base {
    override def getConnect(): Unit = {
      println("Connect to a new database")
    }
  }
}
```

##### 6.14.3.3 特质trait说明
- Scala提供了特质(trait),特质可以同时拥有抽象方法和具体方法,一个类可以实现/继承多个特质.
- 特质中没有实现的方法就是抽象方法,类通过extends继承特质,通过with可以继承多个特质.
- 所有java接口都可以当做Scala特质使用.

##### 6.14.3.4 特质对象 动态混入
- 1.除了可以在类声明时继承特质以外,还可以在构建对象时混入特质,扩展目标类的功能.
- 2.此种方式也可以应用于对抽象类功能进行扩展.
- 3.态混入是Scala特有的方式(java没有动态混入),可在不修改类声明/定义的情况下,扩展类的功能,非常的灵活,耦合性低.
- 4.动态混入可以在不影响原有的继承关系的基础上,给指定的类扩展功能.
- `动态混入实例`
``` scala
package com.geekparkhub.core.scala.demo

object DemoTest026 {
  def main(args: Array[String]): Unit = {
    val t1 = new T1 with Base
    val t2 = new T2 with Base
    val t1_ : T1_ with Base = new T1_ with Base {
      override def t1(): Unit = {
        println("The is t1")
      }
    }
    t1_.t1()
    t1.select(0)
    t2.select(1)
  }

  trait Base {
    def select(id: Int): Unit = {
      println("id is = " + id)
    }
  }

  abstract class T1 {}

  abstract class T1_ {
    def t1()
  }

  class T2 {}
}
```

##### 6.14.3.5 叠加特质
- 构建对象的同时如果混入多个特质，称之为叠加特质，那么特质声明顺序从左到右，方法执行顺序从右到左.
- `叠加特质实例`
- 说明 : 分析叠加特质时,对象构建顺序,和执行方法顺序.
``` scala
package com.geekparkhub.core.scala.demo

object DemoTest027 {
  def main(args: Array[String]): Unit = {
    val base = new Base4 with Base2 with Base3
    println(base)
    base.info(1)
  }

  // 特质 Base类
  trait Base {
    println("Base")
    def info(id: Int)
  }

  // 特质Base1继承Base
  trait Base1 extends Base {
    println("Base1")
    def info(id: Int): Unit = {
      println("insert = " + id)
    }
  }

  // Base2继承Base1
  trait Base2 extends Base1 {
    println("Base2")
    override def info(id: Int): Unit = {
      println("-Base2-")
      super.info(id)
    }
  }

  trait Base3 extends Base2{
    println("Base3")
    override def info(id: Int): Unit = {
      println("-Base3-")
      super.info(id)
    }
  }

  class Base4{}
}
```
- 叠加特质注意事项和细节
- 1.特质声明顺序从左到右.
- 2.Scala在执行叠加对象的方法时,会首先从后面的特质(从右向左)开始执行.
- 3.Scala中特质中如果调用super,并不是表示调用父特质的方法,而是向前面(左边)继续查找特质,如果找不到才会去父特质查找.
- 4.如果想要调用具体特质的方法,可以指定: `super[特质].xxx(...)`其中的泛型必须是该特质的直接超类类型.
- `在特质中重写抽象方法实例`
``` scala
package com.geekparkhub.core.scala.demo

object DemoTest028 {
  def main(args: Array[String]): Unit = {
    val b3 = new B3 with B2 with B1
    b3.info(1)
  }

  trait Base {
    def info(id: Int)
  }

  trait B1 extends Base {
    abstract override def info(id: Int): Unit = {
      println("B1")
      super.info(id)
    }
  }

  trait B2 extends Base {
    def info(id: Int): Unit = {
      println("B2")
    }
  }

  class B3 {}
}
```

##### 6.14.3.6 富接口
- 富接口 : 即该特质中既有抽象方法,又有非抽象方法
``` scala
  trait Operate {
    def insert(id: Int)
    def pageQuery(pageno: Int, pagesize: Int): Unit = {
      println("Query")
    }
  }
```

##### 6.14.3.7 特质中具体字段
- 特质中可以定义具体字段,如果初始化了就是具体字段,如果不初始化就是抽象字段,混入该特质的类就具有了该字段,字段不是继承,而是直接加入类,成为自己的字段.


##### 6.14.3.8 特质中抽象字段
- 特质中未被初始化的字段在具体的子类中必须被重写

##### 6.14.3.9 特质构造顺序
- 特质也是有构造器,构造器中的内容由“字段的初始化”和一些其他语句构成,具体实现请参考特质叠加.
- `第一种特质构造顺序(声明类的同时混入特质)`
- 1.调用当前类的超类构造器
- 2.第一个特质的父特质构造器
- 3.第一个特质构造器
- 4.第二个特质构造器的父特质构造器, 如果已经执行过,就不再执行
- 5.第二个特质构造器
- 6.重复4,5步骤(如果有第3个,第4个特质)
- 7.当前类构造器
- `第二种特质构造顺序(在构建对象时,动态混入特质)`
- 1.调用当前类的超类构造器
- 2.当前类构造器
- 3.第一个特质构造器的父特质构造器
- 4.第一个特质构造器
- 5.第二个特质构造器的父特质构造器,如果已经执行过,就不再执行
- 6.第二个特质构造器
- 7.重复5,6的步骤(如果有第3个,第4个特质)
- 8.当前类构造器
- `分析两种方式对构造顺序的影响`
- 第1种方式实际是构建类对象,在混入特质时,该对象还没有创建.
- 第2种方式实际是构造匿名子类,可以理解成在混入特质时,对象已经创建.

##### 6.14.3.10 扩展类特质
- 特质可以继承类,以用来拓展该特质的一些功能
``` scala
  // 特质扩展类
  trait LoggedException extends Exception {
    def log(): Unit = {
      // 方法来自于Exception类
      println(getMessage())
    }
  }
```
- 所有混入该特质的类,会自动成为特质所继承的超类的子类
``` scala
  // 特质扩展类
  trait LoggedException extends Exception {
    def log(): Unit = {
      // 方法来自于Exception类
      println(getMessage())
    }
  }

  /**
    * 已经是Exception的子类了，所以可以重写方法
    * 如果混入该特质的类,已经继承了另一个类(A类),则要求A类是特质超类的子类
    * 否则就会出现了多继承现象,发生错误.
    * @return
    */
  class UnhappyException extends LoggedException {
    override def getMessage = "错误消息!"
  }
```
- 如果混入该特质的类,已经继承了另一个类(A类),则要求A类是特质超类的子类,否则就会出现了多继承现象,发生错误.

##### 6.14.3.11 自身类型
- 自身类型 : 主要是为了解决特质的循环依赖问题,同时可以确保特质在不扩展某个类的情况下,依然可以做到限制混入该特质的类的类型.
``` scala
  trait Logger {
    // 明确告诉编译器,,如果不是Exception就无法调用getMessage
    this: Exception =>
    def log(): Unit = {
      println(getMessage)
    }
  }

  class Console extends Exception with Logger {}
```

#### 6.14.4 嵌套类
- 在Scala中,可以在任何语法结构中内嵌任何语法结构,如在类中可以再定义一个类,这样就是嵌套类,嵌套类类似Java中内部类.

##### 6.14.4.1 Scala 嵌套类使用 一
- 定义Scala成员内部类和静态内部类,并创建相应的对象实例.
``` scala
package com.geekparkhub.core.scala.demo
import com.geekparkhub.core.scala

object DemoTest029 {
  def main(args: Array[String]): Unit = {
    val test01: Test01 = new Test01
    val test02: Test01 = new Test01

    // 创建内部类
    val test00 = new test01.Test002
    val test001 = new test02.Test002

    // 创建静态内部类实例
    val static = new scala.demo.DemoTest029.Test01.Test004
  }

  // 外部类
  class Test01 {
    // 成员内部类
    class Test002 {}
  }

  // 半生对象
  object Test01 {
    // 静态内部类
    class Test004 {}
  }
}
```
##### 6.14.4.2 Scala 嵌套类使用 二
- 在内部类中访问外部类的属性
- `方式 1` : 内部类如果想要访问外部类的属性,可以通过外部类对象访问.
- 访问方式 : 外部类名.this.属性名
``` scala
package com.geekparkhub.core.scala.demo
import com.geekparkhub.core.scala

object DemoTest029 {
  def main(args: Array[String]): Unit = {
    val test01: Test01 = new Test01
    val test02: Test01 = new Test01

    // 创建内部类
    val test00 = new test01.Test002
    val test001 = new test02.Test002

    test00.info()

    // 创建静态内部类实例
    val static = new scala.demo.DemoTest029.Test01.Test004
  }

  // 外部类
  class Test01 {

    // 定义属性
    var user = "root"
    private var password = 78542

    // 成员内部类
    class Test002 {
      def info() = {
        // 访问方式 : 外部类名.this.属性名
        println("user = " + Test01.this.user + "\npassword = " + Test01.this.password)
      }
    }
  }

  // 半生对象
  object Test01 {
    // 静态内部类
    class Test004 {}

  }
}
```
- `方式 2` : 内部类如果想要访问外部类的属性,也可以通过外部类别名访问.
- 访问方式 : 外部类别名.属性名
``` scala
package com.geekparkhub.core.scala.demo
import com.geekparkhub.core.scala

object DemoTest029 {
  def main(args: Array[String]): Unit = {
    val test01: Test01 = new Test01
    val test02: Test01 = new Test01

    // 创建内部类
    val test00 = new test01.Test002
    val test001 = new test02.Test002

    test00.info()

    // 创建静态内部类实例
    val static = new scala.demo.DemoTest029.Test01.Test004
  }

  // 外部类
  class Test01 {
    // 外部类别名
    alias =>
    // 成员内部类
    class Test002 {
      def info() = {
        // 访问方式 : 外部类名.this.属性名
        println("user = " + alias.user + "\npassword = " + alias.password)
      }
    }
    // 定义属性
    var user = "root"
    private var password = 78542
  }

  // 半生对象
  object Test01 {
    // 静态内部类
    class Test004 {}
  }
}
```

##### 6.14.4.3 类型投影
- 解决方式-使用类型投影
- 类型投影是指 : 在方法声明上,如果使用外部类#内部类的方式,表示忽略内部类的对象关系,等同于Java中内部类的语法操作,将这种方式称之为类型投影(即 : 忽略对象的创建方式,只考虑类型).
``` scala
package com.geekparkhub.core.scala.demo

import com.geekparkhub.core.scala

object DemoTest029 {
  def main(args: Array[String]): Unit = {
    val test01: Test01 = new Test01
    val test02: Test01 = new Test01

    // 创建内部类
    val test00 = new test01.Test002
    val test001 = new test02.Test002

    test00.info()

    // 类型投影
    test00.test(test00)
    test00.test(test001)
    test001.test(test00)
    test001.test(test001)

    // 创建静态内部类实例
    val static = new scala.demo.DemoTest029.Test01.Test004
  }

  // 外部类
  class Test01 {
    // 外部类别名
    alias =>

    // 成员内部类
    class Test002 {
      def info() = {
        // 访问方式 : 外部类名.this.属性名
        println("user = " + alias.user + "\npassword = " + alias.password)
      }
      // 接受Test002实例
      // 类型投影的作用就是屏蔽外部对象对内部类对象的影响
      def test(ic: Test01#Test002): Unit = {
        System.out.println("使用类型投影 " + ic)
      }
    }

    // 定义属性
    var user = "root"
    private var password = 78542
  }

  // 半生对象
  object Test01 {
    // 静态内部类
    class Test004 {}
  }
}
```

### 6.15 Scala 隐式转换 & 隐式值
- 隐式转换函数是以`implicit`关键字声明的带有单个参数的函数,这种函数将会自动应用,将值从一种类型转换为另一种类型.

#### 6.15.1 隐式函数快速入门
``` scala
package com.geekparkhub.core.scala.demo

object DemoTest030 {
  def main(args: Array[String]): Unit = {
    // 定义隐式函数
    implicit def d(d: Double): Int = {
      d.toInt
    }
    val num: Int = 1.5
    println("num = " + num)
  }
}
```
- 隐式转换的注意事项和细节
- 1.隐式转换函数的函数名可以是任意,隐式转换与函数名称无关,只与函数签名(函数参数类型和返回值类型)有关.
- 2.隐式函数可以有多个(即 : 隐式函数列表),但是需要保证在当前环境下,只有一个隐式函数能被识别.
``` scala
package com.geekparkhub.core.scala.demo

object DemoTest030 {
  def main(args: Array[String]): Unit = {
    // 定义隐式函数
    implicit def d(d: Double): Int = {
      d.toInt
    }
    val num: Int = 1.5
    println("num = " + num)
    
    // 定义隐式函数
    implicit def f(f: Float): Int = {
      f.toInt
    }
    val num1: Int = 2.5f
    println("num1 = " + num1)
  }
}
```

#### 6.15.2 隐式转换丰富类库功能
- 如果需要一个类增加一个方法,可以通过隐式转换来实现,(动态增加功能).
- 快速入门案例 | 使用隐式转换方式动态给类增加delete方法.
``` scala
package com.geekparkhub.core.scala.demo

object DemoTest031 {
  def main(args: Array[String]): Unit = {
    val base = new BaseDB
    base.select()
    base.delete()
  }

  class BaseDB {
    def select(): Unit = {
      println("select")
    }
  }

  class DB {
    def delete(): Unit = {
      println("delete")
    }
  }
  // 隐式转换
  implicit def addDelete(baseDB: BaseDB): DB = {
    new DB
  }
}
```


#### 6.15.3 隐式值
- 隐式值也叫隐式变量,将某个形参变量标记为`implicit`,所以编译器会在方法省略隐式参数的情况下去搜索作用域内的隐式值作为缺省参数.
- 编译器的优先级为 传值 > 隐式值 > 默认值
- `隐式值实例`
``` scala
package com.geekparkhub.core.scala.demo

object DemoTest032 {
  def main(args: Array[String]): Unit = {
    // 隐式值
    implicit var name: String = "mac"

    // 函数
    def info(implicit name: String): Unit = {
      println(name + "\tWorking!")
    }
    info
  }
}
```
#### 6.15.4 隐式类
- 在scala2.10后提供了隐式类,可以使用`implicit`声明类,隐式类非常强大,同样可以扩展类的功能,比前面使用隐式转换丰富类库功能更加的方便,在集合中隐式类会发挥重要作用.
- `隐式类实例`
``` scala
package com.geekparkhub.core.scala.demo

object DemoTest033 {
  def main(args: Array[String]): Unit = {

    // 隐式类
    implicit class DB(baseDB: BaseDB) {
      def add(): String = {
        baseDB + "DB"
      }
    }
    val baseDB = new BaseDB
    baseDB.select()
    baseDB.add()
  }
}

// 半生类
class BaseDB {
  def select(): Unit = {
    println("select")
  }
}
```


##### 6.15.4.1 隐式类使用特点
- 1.其所带的构造参数有且只能有一个
- 2.隐式类必须被定义在“类”或“伴生对象”或“包对象”里,即隐式类不能是顶级的(top-level objects)
- 3.隐式类不能是case class(case class 在后续介绍样例类)
- 4.作用域内不能有与之相同名称的标识符.


#### 6.15.5 隐式转换时机
- 1.当方法中的参数的类型与目标类型不一致时,或者是赋值时
- 2.当对象调用所在类中不存在的方法或成员时,编译器会自动将对象进行隐式转换(根据类型)

#### 6.15.6 隐式解析机制
> 即编译器是如何查找到缺失信息的,解析具有以下两种规则 : 
> 
> 1.首先会在当前代码作用域下查找隐式实体(隐式方法、隐式类、隐式对象).
> 
> 2.如果第一条规则查找隐式实体失败,会继续在隐式参数的类型的作用域里查找,类型的作用域是指与该类型相关联的全部伴生模块,一个隐式实体的类型T它的查找范围如下(第二种情况范围广且复杂在使用时,应当尽量避免出现).
> 
> 3.如果T被定义为T with A with B with C,那么A,B,C都是T的部分,在T的隐式解析过程中,它们的半生对象都会被搜索.
> 
> 4.如果T是参数化类型,那么类型参数和与类型参数相关联的部分都算作T的部分,比如List[String]的隐式搜索会搜索List的半生对象和String的半生对象.
> 
> 5.如果T是一个单例类型p.T,即T是属于某个p对象内,那么这个p对象也会被搜索.
> 
> 6.如果T是个类型注入S#T,那么S和T都会被搜索.


#### 6.15.7 隐式转换使用陷阱
- 1.不能存在二义性.
- 2.隐式操作不能嵌套使用.
``` scala
package com.geekparkhub.core.scala.demo

object DemoTest034 {
  def main(args: Array[String]): Unit = {
    // 隐式函数
    implicit def test(d: Double): Int = {
      d.toInt
      // 错误示范 : 隐式操作递归调用,不能嵌套使用
      val num: Int = 1.9
    }

    // 正确示范
    val num: Int = 2.0
  }
}
```

### 6.16 Scala 数据结构 (上) - 集合
#### 6.16.1 数据结构特点
##### 6.16.1 Scala集合基本介绍
> 1.Scala同时支持不可变集合和可变集合,不可变集合可以安全的并发访问.
> 不可变集合：`scala.collection.immutable`
> 可变集合：`scala.collection.mutable`
> 
> 2.Scala默认采用不可变集合,对于几乎所有的集合类,Scala都同时提供了可变(mutable)和不可变(immutable)的版本.
> 
> 3.Scala的集合有三大类 : 序列Seq(有序,Linear Seq)、集Set、映射Map[key->value],所有的集合都扩展自Iterable特质,在Scala中集合有可变(mutable)和不可变(immutable)两种类型.
> 
> ![enter image description here](https://docs.scala-lang.org/resources/images/tour/collections-diagram.svg)
##### 6.16.2 可变集合和不可变集合
> 1.不可变集合 : Scala不可变集合就是这个集合本身不能动态变化,(类似java的数组,是不可以动态增长).
> 
> 2.可变集合:可变集合就是这个集合本身可以动态变化,(比如:ArrayList,是可以动态增长).

#### 6.16.2 不可变集合
- scala.collection.immutable中的所有集合类
![enter image description here](https://docs.scala-lang.org/resources/images/tour/collections-immutable-diagram.svg)
- IndexSeq和LinearSeq区别
- [IndexSeq是通过索引来查找和定位,因此速度快,比如String就是一个索引集合,通过索引即可定位] 
-  [LineaSeq是线型的,即有头尾的概念,这种数据结构一般是通过遍历来查找] 

	
#### 6.16.3 可变集合
- scala.collection.mutable中的所有集合类
![enter image description here](https://docs.scala-lang.org/resources/images/tour/collections-mutable-diagram.svg)
- 在可变集合中比不可变集合更加丰富
- 在Seq集合中,增加了Buffer集合
- 如果涉及到线程安全可以选择使用syn.. 开头集合

#### 6.16.4 数组-定长数组(声明泛型)
##### 6.16.4.1 第一种方式定义数组
- 数组等同于Java中的数组,中括号的类型就是数组的类型
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow001 {
  def main(args: Array[String]): Unit = {
    // 创建Array对象
    val array001 = new Array[Int](4)
    println("array001 数组长度 = "+ array001.length)
    array001(0) = 10
    array001(3) = 11
    for (index <- 0 until array001.length) {
      printf("array001[%d] = %s", index, array001(index) + "\n")
    }
  }
}
```

##### 6.16.4.2 第二种方式定义数组
- 在定义数组时,直接赋值,使用apply方法创建数组对象
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow002 {
  def main(args: Array[String]): Unit = {
    val array002 = Array(1, 3, "xyz")
    println("array002 数组长度 = " + array002.length)
    array002(0) = "tz"
    array002(1) = "zz"
    for (index <- 0 until array002.length) {
      printf("array002[%d] = %s", index, array002(index) + "\n")
    }
  }
}
```
#### 6.16.5 数组-变长数组(声明泛型)
- 对数组进行追加/修改/删除/查询
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable.ArrayBuffer

object CollectionFlow003 {
  def main(args: Array[String]): Unit = {

    // Create ArrayBuffer
    val array003 = ArrayBuffer[Int](2, 4, 6)

    // array003 下标1元素数值
    println("array003(1) = " + array003(1))

    // 循环遍历array003所有下标元素数值
    for (i <- array003) {
      println("array003 所有下标元素数值 = " + i)
    }

    // array003数组长度以及array003哈希值
    println("array003数组长度 = " + array003.length)
    println("array003.hashCode() = " + array003.hashCode())

    // 追加元素array003及array003哈希值
    array003.append(1, 3, 5)
    println("array003.hashCode() = " + array003.hashCode())

    // 修改array003 下标1元素数值
    array003(1) = 87
    for (i <- array003) {
      println("array003 修改后所有下标元素数值 = " + i)
    }

    // 删除array003 下标0元素数值
    array003.remove(0)
    for (i <- array003) {
      println("array003 删除后所有下标元素数值 = " + i)
    }
    println("array003删除后数组长度 = " + array003.length)

  }
}
```
##### 6.16.5.1 变长数组分析总结
> ArrayBuffer是变长数组,类似java的ArrayList
> `val arr2 = ArrayBuffer[Int]()`也是使用的apply方法构建对象.
> `def append(elems: A*) { appendAll(elems) }` 接收的是可变参数.
> 每append一次,arr在底层会重新分配空间,进行扩容,arr2的内存地址会发生变化,也就成为新的ArrayBuffer.

##### 6.16.5.2 定长数组与变长数组 转换
- `xxx.toBuffer` 定长数组转可变数组.
- `xxx.toArray` 可变数组转定长数组
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable.ArrayBuffer

object CollectionFlow004 {
  def main(args: Array[String]): Unit = {
    // Create ArrayBuffer
    val array004 = ArrayBuffer[Int]()
    array004.append(1, 3, 5)
    println(array004)

    // 可变数组转定长数组
    val newArray = array004.toArray
    println("newArray = " + newArray)

    // 定长数组转可变数组
    val newArray2 = newArray.toBuffer
    newArray2.append(246)
    println("newArray2 = " + newArray2)
  }
}
```

##### 6.16.5.3 多维数组定义和使用
- 定义
``` scala
// 二维数组中有三个一维数组,每个一维数组中有四个元素,可以理解为三行四列
Array.ofDim[Double](3,4)
``` 
- `多维数组实例`
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow005 {
  def main(args: Array[String]): Unit = {
    // 创建二维数组
    val array005 = Array.ofDim[Int](3, 4)

    // 双层循环遍历二维数组元素
    // 遍历一维数组元素
    for (i <- array005) {
      // 对一维数组元素结果遍历二维数组元素
      for (j <- i) {
        printf(j + "\t")
      }
      println()
    }

    // 指定访问二维数字元素
    println("array005(1)(1) = " + array005(1)(1))

    // 修改二维数字元素
    array005(1)(1) = 100
    for (i <- array005) {
      // 对一维数组元素结果遍历二维数组元素
      for (j <- i) {
        printf(j + "\t")
      }
      println()
    }

    for (i <- 0 to array005.length - 1) {
      for (j <- 0 to array005(i).length - 1) {
        printf("array005[%d][%d]=%d\t", i, j, array005(i)(j))
      }
      println()
    }
  }
}
```


#### 6.16.6 数组-Scala数组与JavaList互转
##### 6.16.6.1 Scala数组转JavaList
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable.ArrayBuffer

object CollectionFlow006 {
  def main(args: Array[String]): Unit = {
    var array006 = ArrayBuffer("2", "4", "6")
    import scala.collection.JavaConversions.bufferAsJavaList
    val builder = new ProcessBuilder(array006)
    val list = builder.command()
    println(list)
  }
}
```
##### 6.16.6.2 JavaList转Scala数组(mutable.Buffer)
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable.ArrayBuffer

object CollectionFlow006 {
  def main(args: Array[String]): Unit = {
    var array006 = ArrayBuffer("2", "4", "6")
    import scala.collection.JavaConversions.bufferAsJavaList
    val builder = new ProcessBuilder(array006)
    val list = builder.command()
    println(list)

    println("=====================")

    import scala.collection.JavaConversions.asScalaBuffer
    import scala.collection.mutable
    val scalaArray: mutable.Buffer[String] = list
    scalaArray.append("mac")
    scalaArray.remove(0)
    println(scalaArray)
  }
}
```


#### 6.16.7 元组Tuple-元组
##### 6.16.7.1 基本介绍
> 元组也是可以理解为一个容器,可以存放各种相同或不同类型数据.
> 
> 元组中最大只能有22个元素,简单的说就是将多个无关数据封装为一个整体称为元组,最多特点灵活,对数据没有过多约束.

##### 6.16.7.2 元组创建
- 说明
- 为了高效的操作元组,编译器根据元素的个数不同,对应不同的元组类型
- tuple1类型是Tuple5类是scala特有类型
- tuple1类型取决于tuple1后面有多少个元素,有对应关系比如4个元素=>Tuple4
- 元组中最大只能有22个元素即`Tuple1...Tuple22`
- `创建元组实例`
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow007 {
  def main(args: Array[String]): Unit = {
    // 创建 元祖
    val tuple1 = (2, 4, 6, "mac", 8)
    println("tuple1 = " + tuple1)
  }
}
```
- `反编译源码实例`
``` java
package com.geekparkhub.core.scala.collection;

public final class CollectionFlow007$
{
  public static final CollectionFlow007$ MODULE$;
  
  private CollectionFlow007$() { MODULE$ = this; }
  
  static  {
  
  }
  
  public void main(String[] args) { // Byte code:
    //   0: new scala/Tuple5
    //   3: dup
    //   4: iconst_2
    //   5: invokestatic boxToInteger : (I)Ljava/lang/Integer;
    //   8: iconst_4
    //   9: invokestatic boxToInteger : (I)Ljava/lang/Integer;
    //   12: bipush #6
    //   14: invokestatic boxToInteger : (I)Ljava/lang/Integer;
    //   17: ldc 'mac'
    //   19: bipush #8
    //   21: invokestatic boxToInteger : (I)Ljava/lang/Integer;
    //   24: invokespecial <init> : (Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)V
    //   27: astore_2
    //   28: getstatic scala/Predef$.MODULE$ : Lscala/Predef$;
    //   31: aload_2
    //   32: invokevirtual println : (Ljava/lang/Object;)V
    //   35: return
    // Line number table:
    //   Java source line number -> byte code offset
    //   #6	-> 0
    //   #7	-> 28
    // Local variable table:
    //   start	length	slot	name	descriptor
    //   0	36	0	this	Lcom/geekparkhub/core/scala/collection/CollectionFlow007$;
    //   0	36	1	args	[Ljava/lang/String;
    //   28	7	2	tuple1	Lscala/Tuple5; }
}
```
#### 6.16.8 元组Tuple-元组数据访问
- 访问元组中数据,可以采用顺序号(_顺序号),也可以通过索引(productElement)访问.
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow007 {
  def main(args: Array[String]): Unit = {
    // 创建 元祖
    val tuple1 = (2, 4, 6, "mac", 8)
    println("tuple1 = " + tuple1)

    // 访问元祖第一个元素,从_1开始
    println("tuple1._1  = " + tuple1._1)
    // 访问元祖第一个元素,从0开始
    println("tuple1.productElement(0) = " + tuple1.productElement(0))
  }
}
```
#### 6.16.9 元组Tuple-元组数据遍历
- Tuple是一个整体,遍历需要调其迭代器
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow007 {
  def main(args: Array[String]): Unit = {
    // 创建 元祖
    val tuple1 = (2, 4, 6, "mac", 8)
    println("tuple1 = " + tuple1)

    // 遍历元祖
    for (i <- tuple1.productIterator){
      println("tuple1 = " + i)
    }
  }
}
```

#### 6.16.10 列表List-创建List
- Scala中的List和Java List不一样,在Java中List是一个接口,真正存放数据是ArrayList,而Scala的List可以直接存放数据,就是一个object,默认情况下Scala的List是不可变,List属于序列Seq.
- `创建List实例`
- 说明 : 
- 1.List默认为不可变的集合.
- 2.List在scala包对象声明的,因此不需要引入其它包也可以使用.
- 3.List 中可以放任何数据类型,比如arr1类型为List[Any]
- 4.如果希望得到一个空列表,可以使用Nil对象,在scala包对象声明,因此不需要引入其它包也可以使用.
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow008 {
  def main(args: Array[String]): Unit = {
    // 创建List集合
    val list001 = List(1, 3, 5)
    println("list001 = " + list001)
    // 创建List空集合
    val list002 = Nil
    println("list002 = " + list002)
  }
}
```

#### 6.16.11 列表List-访问List元素
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow008 {
  def main(args: Array[String]): Unit = {
    // 创建List集合
    val list001 = List(1, 3, 5)
    println("list001 = " + list001)

    // 创建List空集合
    val list002 = Nil
    println("list002 = " + list002)

    // 访问List集合
    val value0: Int = list001(0)
    val value1: Int = list001(1)
    val value2: Int = list001(2)
    println("value0 = " + value0 + "\n" + "value1 = " + value1 + "\n" + "value2 = " + value2)
  }
}
```

#### 6.16.12 列表List-元素追加
- 向列表中增加元素,会返回新的列表/集合对象.
- 注意 : Scala中List元素追加形式非常独特,和Java不一样.

##### 6.16.12.1 方式1-在列表最后增加数据
- 说明 : 使用`:+`运算符追加数据
- `追加数据实例`
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow008 {
  def main(args: Array[String]): Unit = {
    // 创建List集合
    val list001 = List(1, 3, 5)
    println("list001 = " + list001)

    // 访问List集合
    val value0: Int = list001(0)
    val value1: Int = list001(1)
    val value2: Int = list001(2)
    println("value0 = " + value0 + "\n" + "value1 = " + value1 + "\n" + "value2 = " + value2)

    /**
      * 在List集合后追加数据
      * :+ 运算符表示在列表最后增加数据
      */
    val list003 = list001 :+ 9
    println("list001 = " + list001)
    println("list003 = " + list003)
  }
}
```


##### 6.16.12.2 方式2-在列表最前面增加数据
- 说明 : 使用`+:`运算符追加数据
- `追加数据实例`
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow008 {
  def main(args: Array[String]): Unit = {
    // 创建List集合
    val list001 = List(1, 3, 5)
    println("list001 = " + list001)

    // 访问List集合
    val value0: Int = list001(0)
    val value1: Int = list001(1)
    val value2: Int = list001(2)
    println("value0 = " + value0 + "\n" + "value1 = " + value1 + "\n" + "value2 = " + value2)

    /**
      * 在List集合前追加数据
      * +: 运算符表示在列表最前增加数据
      */
    val list004 = 0 +: list001
    println("list001 = " + list001)
    println("list004 = " + list004)
  }
}
```

##### 6.16.12.3 方式3-在列表最后增加数据
- 符号`::`表示向集合中新建集合添加元素.
- 符号`:::`运算符是将集合中每一个元素加入到集合中.
- 运算规则,从右向左.
- 运算时,集合对象一定要放置在最右边.
- `追加数据实例`
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow008 {
  def main(args: Array[String]): Unit = {
    // 创建List集合
    val list001 = List(1, 3, 5)
    println("list001 = " + list001)

    // 访问List集合
    val value0: Int = list001(0)
    val value1: Int = list001(1)
    val value2: Int = list001(2)
    println("value0 = " + value0 + "\n" + "value1 = " + value1 + "\n" + "value2 = " + value2)

    /**
      * 在List集合后追加数据
      * :: 运算符,向集合中新建集合添加元素
      */
    val list005 = List(1, 2, 3, "mac")
    val list006 = 4 :: 5 :: 6 :: list005 :: Nil
    println("list006 = " + list006)

    /**
      * 在List集合后追加数据
      * ::: 运算符,将集合中每一个元素加入到集合中
      */
    val list007 = List(1, 2, 3, "mac")
    val list008 = 4 :: 5 :: 6 :: list005 ::: Nil
    println("list008 = " + list008)
  }
}
```
##### 6.16.12.3 List集合测试题
- 简述集合函数001/002/003/004 输出结果
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow009 {
  def main(args: Array[String]): Unit = {
    val testFlow = new TestFlow
    testFlow.collectionFunction001()
    testFlow.collectionFunction002()
    testFlow.collectionFunction003()
    testFlow.collectionFunction004()
  }

  // 创建半生类
  class TestFlow {

    // 集合函数001
    def collectionFunction001(): Unit = {
      val list001 = List(1, 2, 3, "tomcat")
      val list002 = 4 :: 5 :: list001
      println("list002 = " + list002)
    }

    // 集合函数002
    def collectionFunction002(): Unit = {
      val list001 = List(1, 2, 3, "tomcat")
       // 程序错误,9不是集合对象,最右侧应该存放集合对象
      val list002 = 4 :: 5 :: list001 :: 9
      println("list002 = " + list002)
    }

    // 集合函数003
    def collectionFunction003(): Unit = {
      val list001 = List(1, 2, 3, "tomcat")
      // 程序错误,运行顺序从右向左执行,6不是集合类型
      val list002 = 4 :: 5 :: 6 ::: list001 ::: Nil
      println("list002 = " + list002)
    }

    // 集合函数004
    def collectionFunction004(): Unit = {
      val list001 = List(1, 2, 3, "tomcat")
      val list002 = 4 :: 5 :: list001 ::: list001 ::: Nil
      println("list002 = " + list002)
    }

  }
}
```

#### 6.16.13 列表ListBuffer
- ListBuffer是可变list集合,可以添加,删除元素,ListBuffer属于序列.
- `ListBuffer实例`
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable.ListBuffer

object CollectionFlow010 {
  def main(args: Array[String]): Unit = {

    // 创建listBuffer
    val listBuffer001 = ListBuffer[Int](1, 2, 3)
    println("listBuffer001(2) = " + listBuffer001(2))
    for (i <- listBuffer001) {
      println("i = " + i)
    }

    // 创建listBuffer
    val listBuffer002 = new ListBuffer[Int]
    // 添加单个元素
    listBuffer002 += 4
    listBuffer002.append(5)
    println("listBuffer002 = " + listBuffer002)

    // 将listBuffer002集合元素(4,5,)添加到另一个listBuffer001集合元素(1,2,3)
    listBuffer001 ++= listBuffer002
    println("listBuffer001 = " + listBuffer001)

    //将listBuffer001集合元素与listBuffer002集合元素相加
    val listBuffer003 = listBuffer001 ++ listBuffer002
    println("listBuffer003 = " + listBuffer003)

    // 在listBuffer001集合追加元素
    val listBuffer004 = listBuffer001 :+ 6
    println("listBuffer004 = " + listBuffer004)

    // 指定删除集合元素
    println("listBuffer002 = " + listBuffer002)
    // 删除将下标为1的元素
    listBuffer002.remove(1)
    for (i <- listBuffer002) {
      println("i = " + i)
    }
  }
}
```

#### 6.16.14 队列Queue
##### 6.16.14.1 队列说明
- 1.队列是一个有序列表,在底层可以用数组或是链表来实现.
- 2.其输入和输出要遵循先入先出原则,即先存入队列数据要先取出,后存入的数据要后取.
- 3.在Scala中由设计者直接提供队列类型Queue使用.
- 4.在Scala中,有`scala.collection.mutable.Queue`和`scala.collection.immutable.Queue`一般来说在开发中通常使用可变集合队列.

#### 6.16.15 队列Queue-队列创建
- 引入`scala.collection.mutable`包,即可创建可变集合队列.
- `队列创建实例` 
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow011 {
  def main(args: Array[String]): Unit = {
    // 创建Queue队列对象
    val queue = new mutable.Queue[Int]()
    println("queue = " + queue)
  }
}
```
#### 6.16.16 队列Queue-队列元素追加数据
- 向队列追加单个元素和List
- `队列创建实例` 
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow011 {
  def main(args: Array[String]): Unit = {

    // 创建Queue队列对象
    val queue = new mutable.Queue[Any]()
    println("queue = " + queue)

    // 向Queue队列追加元素
    queue += 1
    println("queue = " + queue)

    // 元素数值默认添加到Queue队列后
    queue ++= List(3, 5, 7)
    println("queue = " + queue)

    // 将list集合作为一个元素追加到Queue队列,且类Queue队列类型必须设置为Any类型
    queue += List(9, 11, 13)
    println("queue = " + queue)
  }
}
```

#### 6.16.17 队列Queue-删除和加入队列元素
- 在队列中严格的遵守,入队列的数据放在队位,出队列的数据是队列的头部取出.
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow011 {
  def main(args: Array[String]): Unit = {

    // 创建Queue队列对象
    val queue = new mutable.Queue[Any]()
    println("queue = " + queue)

    // 向Queue队列追加元素
    queue += 1
    println("queue = " + queue)

    // 元素数值默认添加到Queue队列后
    queue ++= List(3, 5, 7)
    println("queue = " + queue)

    // 将list集合作为一个元素追加到Queue队列,且Queue队列类型必须设置为Any类型
    queue += List(9, 11, 13)
    println("queue = " + queue)

    // 出队列,从队列头部中删除元素
    val queueElement = queue.dequeue()
    println("queueElement = " + queueElement + " | queue = "+queue)

    // 入队列,默认在队列尾部加入元素
    queue.enqueue(15,17,19)
    println("queue = " + queue)
  }
}
```


#### 6.16.18 队列Queue-返回队列元素
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow011 {
  def main(args: Array[String]): Unit = {

    // 创建Queue队列对象
    val queue = new mutable.Queue[Any]()
    println("queue = " + queue)

    // 向Queue队列追加元素
    queue += 1
    println("queue = " + queue)

    // 元素数值默认添加到Queue队列后
    queue ++= List(3, 5, 7)
    println("queue = " + queue)

    // 将list集合作为一个元素追加到Queue队列,且Queue队列类型必须设置为Any类型
    queue += List(9, 11, 13)
    println("queue = " + queue)

    // 出队列,从队列头部中删除元素
    val queueElement = queue.dequeue()
    println("queueElement = " + queueElement + " | queue = " + queue)

    // 入队列,默认在队列尾部加入元素
    queue.enqueue(15, 17, 19)
    println("queue = " + queue)

    /**
      * 返回Queue队列元素
      */
    // 获取队列第一个元素
    println("head = " + queue.head)

    // 获取队列最后一个元素
    println("last = " + queue.last)

    // 取出队尾数据,返回除了第一个以外剩余元素,可以级联使用
    println("tail = " + queue.tail)
    println("tail.tail.tail = " + queue.tail.tail.tail)
  }
}
```

#### 6.16.19 映射Map
##### 6.16.19.1 Java Map
- HashMap是一个散列表(数组+链表),它存储内容是键值对(key-value)映射,Java中的HashMap是无序,key不能重复.
- `Java Map实例`
``` java
package com.geekparkhub.core.scala.collection;
import java.util.HashMap;

public class JavaHashMap {
    public static void main(String[] args) {
        HashMap<String, Integer> hm = new HashMap();
        hm.put("node1", 100);
        hm.put("node2", 200);
        hm.put("node3", 300);
        hm.put("node4", 400);
        hm.put("node1", 500);
        System.out.println(hm);
        System.out.println(hm.get("node2"));
    }
}
```
##### 6.16.19.2 Scala Map
- 说明 : 
- Scala中的Map和Java类似,也是一个散列表,它存储的内容也是键值对(key-value)映射,Scala中不可变的Map是有序的,可变的Map是无序.
- Scala中有可变Map(`scala.collection.mutable.Map`)和不可变Map(`scala.collection.immutable.Map`)


#### 6.16.20 映射Map-四种Map构建方式
##### 6.16.20.1 方式1-构造不可变映射
- Scala中的不可变Map是有序,构建Map中元素底层是Tuple2类型.
- 不可变map输出顺序和声明顺序是一致
- `创建不可变Map实例`
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow012 {
  def main(args: Array[String]): Unit = {
    // 创建不可变Map对象
    val map = Map("Hadoop" -> 1, "Scala" -> 2, "Spark" -> 3, "Flink" -> 4)
    println("map = " + map)
  }
}
```

##### 6.16.20.2 方式2-构造可变映射
- 可变map输出顺序和声明顺序不会一致
- `创建可变Map实例`
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow012 {
  def main(args: Array[String]): Unit = {

    // 创建不可变Map对象
    val map = Map("Hadoop" -> 1, "Scala" -> 2, "Spark" -> 3, "Flink" -> 4)
    println("map = " + map)

    // 创建可变Map对象
    val map2 = mutable.Map("Hadoop" -> 1, "Scala" -> 2, "Spark" -> 3, "Flink" -> 4)
    println("map2 = " + map2)
  }
}
```
##### 6.16.20.3 方式3-创建空Map映射
- `创建空Map实例`
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow012 {
  def main(args: Array[String]): Unit = {

    // 创建不可变Map对象
    val map = Map("Hadoop" -> 1, "Scala" -> 2, "Spark" -> 3, "Flink" -> 4)
    println("map = " + map)

    // 创建可变Map对象
    val map2 = mutable.Map("Hadoop" -> 1, "Scala" -> 2, "Spark" -> 3, "Flink" -> 4)
    println("map2 = " + map2)

    // 创建空Map对象
    val map3 = new mutable.HashMap[String, Int]
    println("map3 = " + map3)
  }
}
```

##### 6.16.20.4 方式4-对偶元组
- 说明 : 
- 即创建包含键值对的二元组,和第一种方式等价,只是形式上不同而已.
- 只含有两个数据的元组就称之为对偶元组.
- `对偶元组实例`
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow012 {
  def main(args: Array[String]): Unit = {

    // 创建不可变Map对象
    val map = Map("Hadoop" -> 1, "Scala" -> 2, "Spark" -> 3, "Flink" -> 4)
    println("map = " + map)

    // 创建可变Map对象
    val map2 = mutable.Map("Hadoop" -> 1, "Scala" -> 2, "Spark" -> 3, "Flink" -> 4)
    println("map2 = " + map2)

    // 创建空Map对象
    val map3 = new mutable.HashMap[String, Int]
    println("map3 = " + map3)

    // 创建对偶元组
    val map4 = mutable.Map(("Hadoop", 1), ("Scala", 2), ("Spark", 3), ("Flink", 4))
    println("map4 = " + map4)
  }
}
```


#### 6.16.21 映射Map-四种Map取值方式
##### 6.16.21.1 方式1-使用map(key)
- 说明 : 
- 1.如果key存在,则返回对应值.
- 2.如果key不存在,则抛出异常`[java.util.NoSuchElementException]`
- 3.在Java中,如果key不存在则返回null
- `map(key)取值实例`
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow012 {
  def main(args: Array[String]): Unit = {

    // 创建可变Map对象
    val map2 = mutable.Map("Hadoop" -> 1, "Scala" -> 2, "Spark" -> 3, "Flink" -> 4)
    println("map2 = " + map2)

    // map(key)取值
    println("map2(\"Hadoop\") = " + map2("Hadoop"))
  }
}
```

##### 6.16.21.2 方式2-使用`contains`方法检查key是否存在
- 说明 : 
- 使用`containts`先判断在取值,可以防止异常,并加入相应处理逻辑.
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow012 {
  def main(args: Array[String]): Unit = {

    // 创建可变Map对象
    val map2 = mutable.Map("Hadoop" -> 1, "Scala" -> 2, "Spark" -> 3, "Flink" -> 4)
    println("map2 = " + map2)

    // 使用contains方法检查key是否存在
    if (map2.contains("Sparks")) {
      println("Key exists , Value = " + map2("Sparks"))
    } else {
      println("Key does not exist :)")
    }

  }
}
```

##### 6.16.21.3 方式3-使用map.get(key).get取值
- 说明 : 
- 1.通过映射.get(键)调用返回一个Option对象,要么是Some,要么是None
- 2.map.get方法会将数据进行包装.
- 3.如果map.get(key) key存在返回some,如果key不存在,则返回None
- 4.如果map.get(key).getkey存在则返回key对应的值,否则抛出异常`java.util.NoSuchElementException: None.get`
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow012 {
  def main(args: Array[String]): Unit = {

    // 创建可变Map对象
    val map2 = mutable.Map("Hadoop" -> 1, "Scala" -> 2, "Spark" -> 3, "Flink" -> 4)
    println("map2 = " + map2)

    /**
      * 使用map.get(key).get取值
      * 如果key存在,则就会返回Some(value),通过Some(value).get取出元素
      * 如果key不存在,则就会返回None
      */
    println("map2.get(\"Spark\") = " + map2.get("Spark"))
    println("map2.get(\"Spark\").get = " + map2.get("Spark").get)
    println("map2.get(\"Sparks\").get = " + map2.get("Sparks").get)

  }
}
```

##### 6.16.21.4 使用map.getOrElse()取值
- 说明 : 
- 1.getOrElse方法 : `def getOrElse[V1 >: V](key: K, default: => V1)`
- 2.如果key存在,返回key对应值.
- 3.如果key不存在返回默认值,在java中底层有很多类似操作.
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow012 {
  def main(args: Array[String]): Unit = {

    // 创建可变Map对象
    val map2 = mutable.Map("Hadoop" -> 1, "Scala" -> 2, "Spark" -> 3, "Flink" -> 4)
    println("map2 = " + map2)

    // 使用map.getOrElse()取值
    println("map2.getOrElse = " + map2.getOrElse("Spark", "Defaults"))
    println("map2.getOrElse = " + map2.getOrElse("Sparks", "Defaults = 5"))

  }
}
```

##### 6.16.21.5 如何选择取值方式
> 1.如果确定map有key时,则应当使用map(key),因为取值速度快.
> 
> 2.如果不能确定map是否有key时,而且有不同业务逻辑,则使用`map.contains()`先判断在加入逻辑.
> 
> 3.如果只是简单希望得到一个值,则使用map.getOrElse("ip","127.0.0.1")即可.


#### 6.16.22 映射Map-对Map修改/添加/删除
##### 6.16.22.1 更新map元素
- 说明 : 
- 1.map为可变时才能修改,否则抛出异常
- 2.如果key存在 : 则修改对应值,key不存在等价于添加一个key-val
- `更新map元素实例`
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow012 {
  def main(args: Array[String]): Unit = {

    // 创建可变Map对象
    val map2 = mutable.Map("Hadoop" -> 1, "Scala" -> 2, "Spark" -> 3, "Flink" -> 4)
    println("map2 = " + map2)

    // 更新map元素
    map2("Flink") = 5
    println("map2 = "+ map2)
    map2("Storm") = 6
    println("map2 = "+ map2)

  }
}
```
##### 6.16.22.2 添加map元素
- 当增加一个key-value,如果key存在就是更新,如果不存在就是添加
###### 6.16.22.2.1 添加单个map元素
- `添加单个map元素实例`
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow012 {
  def main(args: Array[String]): Unit = {

    // 创建可变Map对象
    val map2 = mutable.Map("Hadoop" -> 1, "Scala" -> 2, "Spark" -> 3, "Flink" -> 4)
    println("map2 = " + map2)

    // 添加单个map元素
    map2 += ("Hive" -> 7)
    map2 += ("Flume" -> 8)
    println("map2 = " + map2)
    
  }
}
```
###### 6.16.22.2.1 添加多个map元素
- `添加多个map元素实例`
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow012 {
  def main(args: Array[String]): Unit = {

    // 创建可变Map对象
    val map2 = mutable.Map("Hadoop" -> 1, "Scala" -> 2, "Spark" -> 3, "Flink" -> 4)
    println("map2 = " + map2)

    // 添加多个map元素
    map2 += ("Kafka" -> 9, "Sqoop" -> 10)
    println("map2 = " + map2)
    val map5 = map2 + ("Oozie" -> 11, "Hbase" -> 12)
    println("map5 = " + map5)
  }
}
```
##### 6.16.22.3 删除map元素
- 说明 : 
- "key","key"就是要删除的key,可以写多个key.
- 如果key存在就删除,如果key不存在也不会抛异常.
- `删除map元素实例`
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow012 {
  def main(args: Array[String]): Unit = {

    // 创建可变Map对象
    val map2 = mutable.Map("Hadoop" -> 1, "Scala" -> 2, "Spark" -> 3, "Flink" -> 4)
    println("map2 = " + map2)

    // 删除map元素
    map2 -= ("Hadoop","Scala","HashMap")
    println("map2 = " + map2)

  }
}
```

#### 6.16.23 映射Map-map遍历
> 说明 :
> 每遍历一次,返回元素是Tuple2,取出时可以按照元组方式来取值.
>  
> 对map元素(元组Tuple2对象)进行遍历方式很多种 : 方式如下 
> 
> `map遍历实例` 
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow012 {
  def main(args: Array[String]): Unit = {

    // 创建可变Map对象
    val map2 = mutable.Map("Hadoop" -> 1, "Scala" -> 2, "Spark" -> 3, "Flink" -> 4)
    println("map2 = " + map2)

    // map遍历
    println("--------------------------------------")
    for ((key, value) <- map2) println(key + " is Mapped To " + value)
    println("--------------------------------------")

    for (value <- map2.keys) println("keys = " + value)
    println("--------------------------------------")

    for (value <- map2.values) println("values = " + value)
    println("--------------------------------------")

    for (value <- map2) println(value + " | key = " + value._1 + " | value = " + value._2)
    println("--------------------------------------")
  }
}
```

#### 6.16.24 集合Set
- 集是不重复元素的结合,集不保留顺序,默认是以哈希集实现.
- Java中Set回顾
- java中HashSet是实现`Set<E>`接口的一个实体类,数据是以哈希表的形式存放,里面的不能包含重复数据,Set接口是一种不包含重复元素的collection,HashSet中的数据也是没有顺序.
##### 6.16.24.1 集合Set-创建
- `Scala 创建Set实例`
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow013 {
  def main(args: Array[String]): Unit = {
    // 创建不可变Set对象
    val set01 = Set(2, 4, 6)
    println("set01 = " + set01)
    // 创建可变Set对象
    val set02 = mutable.Set(1, 3, 5, "mac")
    println("set02 = " + set02)
  }
}
```

##### 6.16.24.2 集合Set-可变集合元素添加/删除
###### 6.16.24.2.1 可变集合元素添加
- `添加元素实例`
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow013 {
  def main(args: Array[String]): Unit = {
    // 创建不可变Set对象
    val set01 = Set(2, 4, 6)
    println("set01 = " + set01)
    // 创建可变Set对象
    val set02 = mutable.Set(1, 3, 5, "mac")
    println("set02 = " + set02)

    // 添加元素
    set02.add(7)
    set02 += 9
    set02.+=("pro")
    println("set02 = " + set02)

  }
}
```

###### 6.16.24.2.2 可变集合元素删除
- `删除元素实例`
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow013 {
  def main(args: Array[String]): Unit = {
    // 创建不可变Set对象
    val set01 = Set(2, 4, 6)
    println("set01 = " + set01)
    // 创建可变Set对象
    val set02 = mutable.Set(1, 3, 5, "mac")
    println("set02 = " + set02)

    // 添加元素
    set02.add(7)
    set02 += 9
    set02.+=("pro")
    println("set02 = " + set02)

    // 删除元素
    set02.-= ("pro")
    set02.remove(9)
    println("set02 = " + set02)
    
  }
}
```


##### 6.16.24.3 集合Set-集合遍历
- `遍历集合实例`
``` scala
package com.geekparkhub.core.scala.collection

import scala.collection.mutable

object CollectionFlow013 {
  def main(args: Array[String]): Unit = {
    // 创建不可变Set对象
    val set01 = Set(2, 4, 6)
    println("set01 = " + set01)
    // 创建可变Set对象
    val set02 = mutable.Set(1, 3, 5, "mac")
    println("set02 = " + set02)

    // 添加元素
    set02.add(7)
    set02 += 9
    set02.+=("pro")
    println("set02 = " + set02)

    // 删除元素
    set02.-=("pro")
    set02.remove(9)
    println("set02 = " + set02)

    // 遍历集合
    for (i <- set02) {
      println("for set002 = " + i)
    }
  }
}
```



### 6.17 Scala 数据结构 (下) - 集合操作
#### 6.17.1 集合元素映射-map映射操作
> 请将List(3,5,7)中所有元素*2,将其结果放到一个新集合中返回,即返回一个新的List(6,10,14),请编写程序实现.

##### 6.17.1.0 map映射操作
> 在Scala中可以通过map映射操作来解决,将集合每一个元素通过指定函数映射转换成为新的结果集合.
> 
> 所谓将函数作为参数传递给另一个函数,这既是函数式编程特点.


##### 6.17.1.1 使用常规方法
- 分析常规方法优缺点
- 优点 : 处理方法比较直接,易于理解
- 缺点 : 代码不够简洁高效 / 没有体现函数式编程特点 / 不利于处理复杂数据处理业务
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow014 {
  def main(args: Array[String]): Unit = {
    // 创建集合
    var list001 = List(3, 5, 7)
    var list002 = List[Int]()
    for (i <- list001) {
      list002 = list002 :+ i * 2
    }
    println("list002 = " + list002)
  }
}
```

##### 6.17.1.2 高阶函数应用实例一
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow015 {
  def main(args: Array[String]): Unit = {
    // 指定function001函数
    val res: Double = function001(function002,4.0)
    println("res = " + res)
  }

  /**
    * function001表示为高阶函数
    * f: Double => Double表示一个函数,该函数可以接受一个Double,返回Double类型
    * n1: Double 普通参数
    * f(n1) 在function001函数中,执行传入函数
    * @param f
    * @param n1
    * @return
    */
  def function001(f: Double => Double, n1: Double) = {
    f(n1)
  }

  /**
    * function002表示为普通函数
    * 可以接受一个Double,返回Double
    * @param d
    * @return
    */
  def function002(d: Double): Double = {
    println("function002 被调用")
    d + d
  }
}
```


##### 6.17.1.3 高阶函数应用实例二
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow016 {
  def main(args: Array[String]): Unit = {
    function003(test001)
//    function003(test002)
  }

  // 定义function003高阶函数,可以接受一个没有输入,返回为Unit函数
  def function003(f: () => Unit): Unit = {
    f()
  }

  def test001(): Unit = {
    println("test001")
  }

  def test002(n: Int => Int): Unit = {
    println("test002")
  }

}
```

##### 6.17.1.4 使用map映射函数解决问题
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow017 {
  def main(args: Array[String]): Unit = {
    // 创建集合
    var list001 = List(3, 5, 7)

    /**
      * 调用map函数
      *
      * map函数执行机制
      * 1.将list集合元素依次遍历
      * 2.将各个元素传递给multiple 函数=> 新Int
      * 3.将得到新Int,放入到一个新集合并返回
      * 4.因此multiple函数被调用3次
      */
    val res: List[Int] = list001.map(function004)
    println("res = " + res)
  }

  // 创建function004函数并将集合元素*2
  def function004(n: Int): Int = {
    2 * n
  }
}
```

##### 6.17.1.5 深刻理解map映射函数机制-模拟实现
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow017 {
  def main(args: Array[String]): Unit = {
    // 创建集合
    var list001 = List(3, 5, 7)

    /**
      * 调用map函数
      *
      * map函数执行过程
      * 1.将list集合元素依次遍历
      * 2.将各个元素传递给multiple 函数=> 新Int
      * 3.将得到新Int,放入到一个新集合并返回
      * 4.因此multiple函数被调用3次
      */
    val res: List[Int] = list001.map(function004)
    println("res = " + res)
  }

  // 创建function004函数并将集合元素*2
  def function004(n: Int): Int = {
    2 * n
  }
  
  val mapMode = MapMode()
  // 调用maps函数
  val res001: List[Int] = mapMode.maps(function004)
  println("mapMode = " + res001)
}


/**
  * 模拟实现map映射函数机制
  * 创建半生类
  */
class MapMode {
  // 创建集合
  var list002 = List(3, 5, 7)
  var list003 = List[Int]()

  // 构建map函数
  def maps(n: Int => Int): List[Int] = {
    // 依次遍历List集合元素
    for (item <- this.list002) {
      list003 = list003 :+ n(item)
    }
    list003
  }
}

// 创建半生对象
object MapMode {
  def apply(): MapMode = new MapMode()
}
```
##### 6.17.1.6 flatmap 扁平化映射
- flatmap : flat即压扁压平,扁平化效果就是将集合中每个元素的子元素映射到某个函数并返回新的集合.
- `flatmap实例`
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow019 {
  def main(args: Array[String]): Unit = {
  
    /**
      * 将所有单词全部转换字母大写,返回到新List集合
      */
    val names = List("Alice", "Bob", "Nick")
    // 调用flatMap函数,将集合所有元素扁平化操作
    val list: List[Char] = names.flatMap(function006)
    println("list = " + list)
  }

  // 构建function006函数 转化字母大写
  def function006(v: String): String = {
    v.toUpperCase
  }
}
```


##### 6.17.1.7 filter 集合元素过滤
- filter : 将符合要求的数据(筛选)放置到新的集合.
- `filter实例`
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow020 {
  def main(args: Array[String]): Unit = {
    /**
      * 将所有单词全部转换字母大写,返回到新List集合
      */
    val names = List("Alice", "Bob", "Nick")
    // 调用filter函数将首字母为'A'的元素筛选到新的集合
    val list: List[String] = names.filter(function007)
    println("list = " + list)
  }

  // 构建function007函数 筛选母为'A'的元素
  def function007(v: String): Boolean = {
    v.startsWith("A")
  }
}
```
##### 6.17.1.8 化简
###### 6.17.1.8.1 reduceLeft
- 化简 : 将二元函数引用于集合中的函数.
- `reduceLeft 运行机制说明`
- 1.`def reduceLeft[B >: A](@deprecatedName('f) op: (B, A) => B): B`
- 2.`reduceLeft(f) 接收函数需要的形式为op: (B, A) => B): B`
- 3.`educeleft(f) 运行规则是从左边开始执行将得到的结果返回给第一个参数`
- 4.`reduceLeft实例`
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow021 {
  def main(args: Array[String]): Unit = {

    // 使用化简方式来计算list集合之和
    val list = List(1, 3, 5, 7, 9)

    // 调用reduceLeft函数 计算集合之和
    val res: Int = list.reduceLeft(sum)
    println("sum = " + res)
  }

  // 集合元素相加
  def sum(n1: Int, n2: Int): Int = {
    n1 + n2
  }
}
```

##### 6.17.1.9 fold 折叠
- 1.fold函数将上一步返回值作为函数的第一个参数继续传递参与运算,直到list中所有元素被遍历.
- 2.可以把reduceLeft看做简化版foldLeft.
- 3.fold相关函数 : fold / foldLeft / foldRight,可以参考reduce相关方法理解.
- 4.`fold实例`
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow023 {
  def main(args: Array[String]): Unit = {
    // 折叠理解和化简的运行机制几乎一样
    val list = List(1, 3, 5, 7, 9)
    // 调用左折叠函数
    val left = list.foldLeft(11)(function010)
    // 调用右折叠函数
    val right = list.foldRight(11)(function010)

    println("left = " + left)
    println("right = " + right)
  }

  def function010(n1: Int, n2: Int): Int = {
    n1 - n2
  }
}
```
###### 6.17.1.9.1 foldLeft和foldRight缩写
- 1.`/:`表示foldLeft缩写方式
- 2.`:\`表示foldRight缩写方式
- 3.`缩写实例`
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow024 {
  def main(args: Array[String]): Unit = {

    val list = List(2, 4, 6, 8)

    /**
      * /: 表示foldLeft缩写方式
      * :\ 表示foldRight缩写方式
      */

    // (10 /: list) (function011) 等价于 list.foldLeft(10)(function011)
    val res001 = (10 /: list) (function011)

    // (list :\ 10) (function011) 等价于 list.foldRight(10)(function011)
    val res002 = (list :\ 10) (function011)

    println("res001 = " + res001)
    println("res002 = " + res002)
  }

  def function011(n1: Int, n2: Int): Int = {
    n1 - n2
  }
}
```


##### 6.17.1.10 扫描
- 1.扫描即对某个集合所有元素做fold操作,但是会把产生的所有中间结果放置于一个集合中保存.
- 2.`扫描实例`
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow025 {
  def main(args: Array[String]): Unit = {

    val left = (1 to 5).scanLeft(6)(function012)
    val right = (1 to 5).scanRight(6)(function013)
    println("left = " + left)
    println("right = " + right)
  }

  def function012(n1: Int, n2: Int): Int = {
    n1 - n2
  }

  def function013(n1: Int, n2: Int): Int = {
    n1 + n2
  }
}
```

##### 6.17.1.11 扩展-拉链(合并)
- 将两个集合进行对偶元组合并,可以使用拉链.
- `拉链实例`
``` scala
package scala.com.geekparkhub.core.scala.collection

object CollectionFlow027 {
  def main(args: Array[String]): Unit = {
    val list1 = List(1, 2, 3)
    val list2 = List(4, 5, 6)
    val res = list1.zip(list2)
    println("res = " + res)
  }
}
```
- `拉链使用注意事项`
- 拉链的本质就是两个集合合并操作,合并后每个元素是一个对偶元组.
- 如果两个集合个数不对应,会造成数据丢失.
- 集合不限于List,也可以是其它集合比如Array
- 如果要取出合并后的各个对偶元组数据,可以遍历


##### 6.17.1.12 扩展-迭代器
- 通过iterator方法从集合获得一个迭代器，通过while循环和for表达式对集合进行遍历.
- 说明 : 
- iterator构建实际是AbstractIterator的一个匿名子类.
- 该AbstractIterator子类提供了hasNext next等方法.
- 可以使用while的方式,使用hasNext next方法变量.
- `迭代器实例`
``` scala
package scala.com.geekparkhub.core.scala.collection

object CollectionFlow028 {
  def main(args: Array[String]): Unit = {
    val list = List(1, 2, 3).iterator
    while (list.hasNext){
      println(list.next())
    }
    for (i <- list){
      println(i)
    }
  }
}
```


##### 6.17.1.13 扩展-流 Stream
- stream是一个集合,可以用于存放无穷多个元素,但是这无穷个元素并不会一次性生产,而是需要用到多大的区间就会动态生产,末尾元素遵循lazy规则.
- 说明 : 
- Stream集合存放的数据类型是BigInt
- numsForm是自定义函数,函数名是有开发者指定.
- 创建的集合的第一个元素是n,后续元素生成规则是n + 1
- 后续元素生成的规则是可以开发者指定.
- `创建Stream对象实例`
``` scala
package scala.com.geekparkhub.core.scala.collection

object CollectionFlow029 {
  def main(args: Array[String]): Unit = {
    // 创建Stream
    def dataflow(n: BigInt): Stream[BigInt] = n #:: dataflow(n + 1)
    val stream: Stream[BigInt] = dataflow(1)
  }
}
```
- `Stream实例`
``` scala
package scala.com.geekparkhub.core.scala.collection

object CollectionFlow029 {
  def main(args: Array[String]): Unit = {
    // 创建Stream
    def dataflow(n: BigInt): Stream[BigInt] = n #:: dataflow(n + 1)

    val stream: Stream[BigInt] = dataflow(5).map(function014)
    println("stream = " + stream)

    // 取出第一个元素
    println("stream head = " + stream.head)
    // 当对流执行tail操作时会生成一个新的数据
    println("stream tail = " + stream.tail)
  }

  def function014(n1: BigInt): BigInt = {
    n1 * n1
  }
}
```


##### 6.17.1.14 扩展-视图View
- Stream懒加载特性,也可以对其他集合应用view方法来得到类似效果,具有如下特点 : 
- view方法产出一个总是被懒执行集合.
- view不会缓存数据,每次都要重新计算,比如遍历View时.
- `View实例`
``` scala
package scala.com.geekparkhub.core.scala.collection

object CollectionFlow030 {
  def main(args: Array[String]): Unit = {
    val view001 = (1 to 10).filter(eq)
    val view002 = (1 to 10).view.filter(eq)
    println("view001 = " + view001)
    println("view002 = " + view002)
    for (i <- view001) {
      println("res = " + i)
    }
  }

  def eq(n: Int): Boolean = {
    n.toString.equals(n.toString.reverse)
  }

  def function015(n2: Int): Int = {
    n2
  }
}
```

##### 6.17.1.15 扩展-线程安全集合
- 所有线程安全集合都是以`Synchronized`开头的集合.
- `SynchronizedBuffer` / `SynchronizedMap` / `SynchronizedPriorityQueue` / `SynchronizedQueue` / `SynchronizedSet` / `SynchronizedStack`

##### 6.17.1.15 扩展-并行集合
- Scala为了充分使用多核CPU,提供了并行集合(有别于前面的串行集合),用于多核环境的并行计算.
- 并行机制算法 : 
- Divide and conquer : 分治算法,Scala通过splitters(分解器),combiners（组合器）等抽象层来实现,主要原理是将计算工作分解很多任务,分发给一些处理器去完成,并将它们处理结果合并返回.
- Work stealin算法 : 主要用于任务调度负载均衡（load-balancing）.
- `查看并行集合中元素访问的线程实例`
``` scala
package scala.com.geekparkhub.core.scala.collection

object CollectionFlow031 {
  def main(args: Array[String]): Unit = {

    // 非并行
    var res = (1 to 10).map {
      case _ => Thread.currentThread.getName
    }.distinct

    // 并行
    var res02 = (1 to 10).par.map {
      case _ => Thread.currentThread.getName
    }.distinct

    println("res = " + res)
    println("res02 = " + res02)
  }
}
```

##### 6.17.1.16 扩展-操作符
- 操作符扩展
- 如果想在变量名、类名等定义中使用语法关键字(保留字),可以配合反引号反引号如: ``` val `val` = 42 ```
- `中置操作符` : A 操作符B 等同于A.操作符(B)
- `后置操作符` : A`操作符`等同于A`.操作符`,如果操作符定义时不带`()`,则调用时不能加括号.
- `前置操作符` : `+、-、！、~` 等操作符A等同于A.`unary_`操作符.
- `赋值操作符` : A 操作符= B 等同于A = A 操作符B,比如A += B 等价A = A + B



### 6.18 Scala 模式匹配
#### 6.18.1 match
> 1.Scala中模式匹配类似于Java中的switch语法,但是更加强大.
> 
> 2.模式匹配语法中,采用`match`关键字声明,每个分支采用`case`关键字进行声明.
> 
> 3.当需要匹配时,会从第一个case分支开始,如果匹配成功,那么执行对应的逻辑代码,如果匹配不成功,继续执行下一个分支进行判断,如果所有case都不匹配,那么会执行case _ 分支,类似于Java中default语句.
> 
> 4.`match细节说明` : 
> 如果所有case都不匹配,那么会执行case _ 分支,类似于Java中default语句.
> 
> 如果所有case都不匹配,又没有写case _ 分支,那么会抛出MatchError.
> 
> 每个case中不用break语句,自动中断case.
> 
> 可以在match中使用其它类型,而不仅仅是字符.
> 
> `=>` 等价于java swtich,`=>`后面的代码块到下一个case是作为一个整体执行,可以使用{}扩起来,也可以不扩.
> 
> 5.`match实例`
``` scala
package scala.com.geekparkhub.core.scala.matching

object PatternMatchingFloat {
  def main(args: Array[String]): Unit = {
    val parameter = "~"
    val n1 = 5
    val n2 = 5
    var res = 0

    /**
      * match (类似java switch) 和case 关键字
      * 匹配的顺序是从上到下,匹配到一个就执行对应的代码
      * 如果匹配成功,则执行=> 后代码块
      * 如果一个都没有匹配到,则执行case _ 后代码块
      */
    parameter match {
      case "+" => res = n1 + n2
      case "-" => res = n1 - n2
      case "*" => res = n1 * n2
      case "/" => res = n1 / n2
      case _ => println("error")
    }
    println("res = " + res)
  }
}
```

#### 6.18.2 守卫
- 如果想要表达匹配某个范围的数据,就需要在模式匹配中增加条件守卫.
- `守卫实例`
``` scala
package scala.com.geekparkhub.core.scala.matching

object PatternMatchingFloat001 {
  def main(args: Array[String]): Unit = {

    for (i <- "+-3!") {
      var start = 0
      var end = 0
      i match {
        case '+' => start = 1
        case '-' => end = -1
        case _ if i.toString.equals("3") => start = 3
        case _ if i > 1100 => printf("i > 1100")
        case _ => end = 2
      }
      println(i + "," + start + "," + end)
    }

  }
}
```

#### 6.18.3 模式变量
- 如果在case关键字后跟变量名,那么match前表达式的值会赋给那个变量.
- `模式变量实例`
``` scala
package scala.com.geekparkhub.core.scala.matching

object PatternMatchingFloat002 {
  def main(args: Array[String]): Unit = {
    var i = "S"
    var res = i match {
      case "+" => println("+")
      case variable => variable
      case _ => println("error")
    }
    println("res = " + res)
  }
}
```



#### 6.18.4 类型匹配
- 可以匹配对象的任意类型,这样做避免使用isInstanceOf和asInstanceOf方法.
- `类型匹配注意事项`
- 1.`Map[String, Int]` 和`Map[Int, String]`是两种不同类型,其它类推.
- 2.在进行类型匹配时,编译器会预先检测是否有可能的匹配,如果没有则报错.
- 3.如果case _ 出现在match中间,则表示隐藏变量名,即不使用,而不是表示默认匹配.
- 4.`类型匹配实例`
``` scala
package scala.com.geekparkhub.core.scala.matching

object PatternMatchingFloat003 {
  def main(args: Array[String]): Unit = {

    val num = 4
    var objects = if (num == 1) 1
    else if (num == 2) "2"
    else if (num == 3) BigInt(3)
    else if (num == 4) Map("map" -> 1)
    else if (num == 5) Map(1 -> "map")
    else if (num == 6) Array(1, 2, 3)
    else if (num == 7) Array("array", 1)
    else if (num == 8) Array("array")

    val res = objects match {
      case a: Int => a
      case b: Map[String, Int] => "字符串-数字Map集合"
      case c: Map[Int, String] => "数字-字符串Map集合"
      case d: Array[String] => "字符串数组"
      case e: Array[Int] => "数字数组"
      case f: BigInt => Int.MaxValue
      case _ => "Defaults"
    }
    println("res = " + res)
  }
}
```

#### 6.18.5 匹配数组
- 1.Array(0) 匹配只有一个元素且为0的数组.
- 2.Array(x,y)匹配数组有两个元素,并将两个元素赋值为x和y,当然可以依次类推Array(x,y,z)匹配数组有3个元素.
- 3.Array(0,_*) 匹配数组以0开始.
``` scala
package scala.com.geekparkhub.core.scala.matching

object PatternMatchingFloat004 {
  def main(args: Array[String]): Unit = {

    var arrays = Array(Array(0), Array(1, 0), Array(0, 1, 0), Array(1, 1, 0), Array(1, 1, 0, 1))
    for (i <- arrays) {
      val res = i match {
        case Array(0) => "0"
        case Array(x, y) => x + " = " + y
        case Array(0, _*) => "以0开头数组"
        case _ => "Defaults"
      }
      println("res = " + res)
    }
  }
}
```

#### 6.18.6 匹配列表
- `匹配列表实例`
``` scala
package scala.com.geekparkhub.core.scala.matching

object PatternMatchingFloat005 {
  def main(args: Array[String]): Unit = {
    var arrays = Array(List(0), List(1, 0), List(0, 1, 0), List(1, 1, 0), List(1, 1, 0, 1))
    for (i <- arrays) {
      val res = i match {
        case 0 :: Nil => 0
        case x :: y :: Nil => x + " = " + y
        case 0 :: tail => "0..."
        case _ => "Defaults"
      }
      println("res = " + res)
    }
  }
}
```

#### 6.18.7 匹配元组
``` scala
package scala.com.geekparkhub.core.scala.matching

object PatternMatchingFloat006 {
  def main(args: Array[String]): Unit = {
    val arrays = Array((0, 1), (55, 33), (1, 0), (1, 1), (2, 3, 8))
    for (i <- arrays) {
      val res = i match {
        case (0, _) => "0 ..."
        case (y, 0) => y
        case (x, y) => (y, x)
        case _ => "Other"
      }
      println("res = " + res)
    }
  }
}
```


#### 6.18.8 对象匹配
- 对象匹配,case中对象的unapply方法(对象提取器)返回Some集合则为匹配成功.
- 返回None集合则为匹配失败
- 构建对象时apply方法会被调用.
- 当Square(n)写在case后时会默认调用unapply方法(对象提取器)
- `对象匹配实例`
``` scala
package scala.com.geekparkhub.core.scala.matching

object PatternMatchingFloat007 {
  def main(args: Array[String]): Unit = {
    val num = 36.0
    num match {
      case Square(n) => println("n  = " + n)
      case _ => println("Object matching loss败")
    }
  }
}

object Square {
  // unapply方法是对象提取器
  def unapply(z: Double): Option[Double] = {
    Some(math.sqrt(z))
    None
  }
  def apply(z: Double): Double = z * z
}
```

- 当case后面的对象提取器方法的参数为多个,则会默认调用def unapplySeq()方法.
- 如果unapplySeq返回是Some,获取其中的值,判断得到的sequence中的元素的个数是否是三个如果是三个,则把三个元素分别取出赋值给v1, v2, v3
- 其它的规则不变
``` scala
package scala.com.geekparkhub.core.scala.matching

object PatternMatchingFloat008 {
  def main(args: Array[String]): Unit = {
    val v = "A,B,C"
    v match {
      case Values(v1, v2, v3) => {
        println(s"$v1 + $v2 + $v3")
      }
      case _ => println("Nothing Matched")
    }
  }
}

object Values {
  // 当构造器是多个参数时,会触发对象提取器
  def unapplySeq(vs: String): Option[Seq[String]] = {
    if (vs.contains(",")) Some(vs.split(","))
    else None
  }
}
```

#### 6.18.9 变量声明模式
- match中每一个case都可以单独提取出来.
- `变量声明实例`
``` scala
package scala.com.geekparkhub.core.scala.matching

object PatternMatchingFloat009 {
  def main(args: Array[String]): Unit = {

    /**
      * 变量的快速简写
      * val (x, y, z) = (1, 2, "max") 既是 val x = 1 , val y = 2 , val z = "max" 这种形式的简写
      */
    val (x, y, z) = (1, 2, "max")
    println("x = " + x + " , y = " + y + " , z = " + z)

    // 10除3结果以及10对3取余结果各自交给变量
    val (w, e) = BigInt(10) /% 3
    println("w = " + w + " , e = " + e)

    // 过去数组前两个元素
    val array = Array(1, 3, 5, 7, 9)
    val Array(first, second, _*) = array
    println("array = " + first, second)
  }
}
```

#### 6.18.10 for循环表达式模式
- for循环也可以进行模式匹配.
- `for循环表达式模式实例`
``` scala
package scala.com.geekparkhub.core.scala.matching

object PatternMatchingFloat010 {
  def main(args: Array[String]): Unit = {

    val map = Map("A" -> 1, "B" -> 2, "C" -> 3, "D" -> 0)

    // 循环方式一 : 遍历所有Map元素
    for ((k, v) <- map) {
      println("k = " + k + " -> " + "v = " + v)
    }
    println("----------------------")

    // 循环方式二 : 只遍历value=0的key-value,其它元素过滤
    for ((k, 0) <- map) {
      println("k = " + k + " -> " + "v = " + 0)
    }
    println("----------------------")

    // 循环方式三 : 加入判断,用法更加灵活强大
    for ((k, v) <- map if v >= 1 && v  >= 0) {
      println("k = " + k + " -> " + "v = " + v)
    }
    println("----------------------")
  }
}
```

#### 6.18.11 样例(模板)类
> 1.说明 : 
> 
> 样例类仍然是类.
> 
> 样例类用case关键字进行声明.
> 
> 样例类是为模式匹配而优化的类.
> 
> 构造器中的每一个参数都成为val —— 除非它被显式地声明为var
> 
> 在样例类对应的伴生对象中提供apply方法,不用new关键字就能构造出相应的对象.
> 
> 提供unapply方法让模式匹配可以工作.
> 
> 将自动生成toString、equals、hashCode和copy方法(有点类似模板类,直接给生成使用).
> 
> 样例类和其他类完全一样,还可以添加方法和字段扩展它们.
> 
> 2.`样例类快速入门实例1`
``` scala
package scala.com.geekparkhub.core.scala.matching

object PatternMatchingFloat011 {
  def main(args: Array[String]): Unit = {
    println("test")
  }
}

abstract class Test

// 创建样例类
case class Test001(value: Double) extends Test

// 创建样例类
case class Test002(value: Double, unit: String) extends Test

// 创建样例类
case object Test003 extends Test
```
- 3.`样例类快速入门实例2`
``` scala
package scala.com.geekparkhub.core.scala.matching

/**
  * 使用样例类方式进行对象匹配简洁性
  */
object PatternMatchingFloat012 {
  def main(args: Array[String]): Unit = {

    val arrays = Array(Test004(111.1), Test005(123.5, "CD"), Test006)

    for (i <- arrays) {
      val res = i match {
        case Test004(v) => "$ " + v
        case Test005(q, a) => q + " " + a
        case Test006 => "/"
      }
      println("res = " + res)
    }

  }
}

abstract class Tests

// 创建样例类
case class Test004(value: Double) extends Tests

// 创建样例类
case class Test005(value: Double, unit: String) extends Tests

// 创建样例类
case object Test006 extends Tests
```

- 4.`样例类快速入门实例3`
``` scala
package scala.com.geekparkhub.core.scala.matching

object PatternMatchingFloat013 {
  def main(args: Array[String]): Unit = {
    
    /**
      * 样例类 copy方法和带名参数
      * copy创建一个与现有对象值相同的新对象,并可以通过带名参数来修改某些属性
      */
    val test008 = new Test008(1000.3, "PX")
    
    val test009 = test008.copy()
    val test010: Test008 = test008.copy(value = 999.1)
    val test011: Test008 = test008.copy(unit = "CS")

    println("test009 = " + test009)
    println("test009.value = " + test009.value + " , test009.unit = " + test009.unit)
    println("test010.value = " + test010.value)
    println("test011.unit = " + test011.unit)
  }
}


abstract class Testse

// 创建样例类
case class Test007(value: Double) extends Testse

// 创建样例类
case class Test008(value: Double, unit: String) extends Testse

// 创建样例类
case object Test009 extends Testse
```

#### 6.18.12 case语句中置(缀)表达式
- 什么是中置表达式? 1  +  2,这就是一个中置表达式.
- 如果unapply方法产出一个元组,可以在case语句中使用中置表示法,比如可以匹配一个List序列.
``` scala
package scala.com.geekparkhub.core.scala.matching

object PatternMatchingFloat014 {
  def main(args: Array[String]): Unit = {
    List(1,3,5,1) match {
      case first :: second :: res => println("first = " + first + " , second = " + second + ", res.length = " + res.length + " , res = " + res)
      case _ => println("Match failed")
    }
  }
}
```

#### 6.18.13 匹配嵌套结构
- 操作原理类似于正则表达式
- `匹配嵌套结构实例`
- 现在有一些商品,使用Scala设计相关的样例类,完成商品可以捆绑打折出售.
- 商品捆绑可以是单个商品,也可以是多个商品.
- 统计出所有捆绑商品打折后的最终价格
``` scala
package scala.com.geekparkhub.core.scala.matching

object PatternMatchingFloat015 {
  def main(args: Array[String]): Unit = {

    // 创建匹配嵌套结构
    val sale = Bundle("Books", 10, Book("沉浮", 40), Bundle("修真", 20, Book("《雪中悍刀行》", 80), Book("《四月围城》", 30),Book("《天龙八部》", 200)))

    // 1.使用case语句得到"漫画",使用`_`忽略即可,`_*`表示忽略所有
    val res001 = sale match {
      case Bundle(_, _, Book(description, _), _*) => description
    }
    println("res001 = " + res001)

    // 2.通过`@`表示法将嵌套的值绑定到变量,`_*`绑定剩余Item绑定到res3
    val res002 = sale match {
      case Bundle(_, _, res2@Book(_, _), res3@_*) => (res2, res3)
    }
    println("res002 = " + res002)

    // 3.不使用`_*`绑定,剩余Item绑定到res5
    val res003 = sale match {
      case Bundle(_, _, res4@Book(_, _), res5) => (res4, res5)
    }
    println("res003 = " + res003)

    println("process(sale) = " + process(sale))
  }

  // 定义处理函数
  def process(it: Item): Double = {
    it match {
      case Book(_, res6) => res6
      case Bundle(_, discount, res7@_*) => res7.map(process).sum - discount
    }
  }
}

/**
  * 创建样例类
  */
abstract class Item

// 创建 书籍样例类
case class Book(description: String, price: Double) extends Item

// 创建 书籍套餐样例类
case class Bundle(description: String, discount: Double, item: Item*) extends Item
```


#### 6.18.14 密封类
- 如果想让case类的所有子类必须在声明该类的相同的源文件中定义,可以将样例类的通用超类声明为`sealed`,这种超类称之为密封类.
- 密封就是不能在其他子类定义子类.
- `密封类实例`
``` scala
package scala.com.geekparkhub.core.scala.matching

object PatternMatchingFloat016 {
  def main(args: Array[String]): Unit = {

  }
}

/**
  * 定义非密封抽象类
  */
abstract class Seals01

case class Subclass01(name: String) extends Seals01

case class Subclass02(age: Int) extends Seals01


/**
  * 定义密封抽象类
  */
abstract sealed class Seals02

case class Subclass03(name: String) extends Seals02

case class Subclass04(age: Int) extends Seals02
```
``` scala
package scala.com.geekparkhub.core.scala.matching

object PatternMatchingFloat017 {
  def main(args: Array[String]): Unit = {
  }

  // 可以继承Seals01
  class Tests extends Seals01

  // 不可以继承Seals02,因为Seals02声明为sealed密封类
  class Tests extends Seals02
}
```

### 6.19 Scala 函数式编程 高级

#### 6.19.1 偏函数(partial function)
> 提出需求,引起思考
> 
> `val list = List(1, 2, 3, 4, "abc")`
> 
> 将集合list中的所有数字+1,并返回一个新的集合,要求忽略掉非数字的元素,即返回的新的集合形式为(2, 3, 4, 5)
> 
> 解决方式1 : filter+map+返回新的集合,引出偏函数.
> 虽然可以解决问题,但还是过于繁琐.
``` scala
package scala.com.geekparkhub.core.scala.functionflow

object FunctionFlow001 {
  def main(args: Array[String]): Unit = {
    val list = List(1, 2, 3, 4, "abc")
    // 先过滤后汇总
    val ints: List[Int] = list.filter(f1).map(f2).map(f3)
    println("ints = " + ints)
  }

  // 接收int类型
  def f1(n: Any): Boolean = {
    n.isInstanceOf[Int]
  }

  // 将Any类型转换为int
  def f2(n: Any): Int = {
    n.asInstanceOf[Int]
  }

  // 将元素+1
  def f3(n: Int): Int = {
    n + 1
  }
}
```

> 解决方式2 : 模式匹配
> 虽然使用模式匹配比较简单,但还是不够完美,因此引出了偏函数
``` scala
package scala.com.geekparkhub.core.scala.functionflow

object FunctionFlow002 {
  def main(args: Array[String]): Unit = {
    val list = List(1, 2, 3, 4, "abc")
    val res = list.map(f1)
    println("res = " + res)
  }

  // 模式匹配
  def f1(n: Any): Any = {
    n match {
      case x: Int => x + 1
      case _ =>
    }
  }
}
```

> 解决方式3 : 偏函数
> 在对符合某个条件,而不是所有情况进行逻辑操作时,使用偏函数是一个不错的选择.
> 
> 将包裹在大括号内的一组case语句封装为函数称之为偏函数,它只会对作用于指定类型的参数或范围值实施计算,如超出范围的值会忽略.
> 
> 偏函数在Scala中是一个特质PartialFunction.
> 
> `偏函数快速入门实例`
``` scala
package scala.com.geekparkhub.core.scala.functionflow

object FunctionFlow003 {
  def main(args: Array[String]): Unit = {
    // 使用偏函数
    val list = List(1, 2, 3, 4, "abc")

    /**
      * 定义偏函数
      * PartialFunction[Any,Int] 即表示偏函数接收输入类型是Any类型,返回类型是Int类型
      *
      */
    val res = new PartialFunction[Any, Int] {

      /**
        * isDefinedAt(x: Any)
        * 如果结果返回true,则会调用apply函数去构建一个对象实例,反言之如果结果返回false,则不会调用apply函数.
        *
        * @param x
        * @return
        */
      override def isDefinedAt(x: Any): Boolean = if (x.isInstanceOf[Int]) true else false

      // 构造器,对传入的参数+1并返回新的集合结果
      override def apply(v1: Any): Int = {
        v1.asInstanceOf[Int] + 1
      }
    }

    // 调用偏函数
    val listres = list.collect(res)
    println("listres = " + listres)

  }
}
```
> 偏函数说明 : 
> 
> 1.使用构建特质的实现类(使用的方式是PartialFunction的匿名子类).
> 
> 2.构建偏函数时,参数形式[Any, Int]是泛型,第一个表示参数类型,第二个表示返回参数.
> 
> 3.当使用偏函数时会遍历集合的所有元素,编译器执行流程时先执行`isDefinedAt()`如果为true,就会执行apply,构建一个新的Int对象返回.
> 
> 4.执行isDefinedAt()为false就过滤掉此元素,即不构建新的Int对象.
> 
> 5.map函数不支持偏函数,因为map底层机制就是所有循环遍历,无法过滤处理原来集合的元素.
> 
> 6.List集合中collect函数支持偏函数.
> 
> 7.`偏函数简写实例`
> 声明偏函数,需要重写特质中的方法,有时会略显繁琐,而Scala提供简单的实现方法.
``` scala
package scala.com.geekparkhub.core.scala.functionflow

object FunctionFlow004 {
  def main(args: Array[String]): Unit = {

    val list = List(1, 2, 3, 4, 2.6, 5.6, "abc")

    // 定义隐式转换,将Double类型隐式转换为Int类型
    implicit def typeconversion(value: Double): Int = {
      value.toInt
    }

    // 偏函数简化形式 一
    def pf1: PartialFunction[Any, Int] = {
      case x: Int => x + 1
      case d: Double => d * 2
    }
    
    val res01 = list.collect(pf1)
    println("res01 = " + res01)

    // 偏函数简化形式 二
    val res02 = list.collect { case x: Int => x + 1 }
    println("res02 = " + res02)
  }
}
```

#### 6.19.2 作为参数函数
- 函数作为一个变量传入到了另一个函数中,那么该作为参数的函数的类型是 : function1,即 : (参数类型) => 返回类型.
- 说明 : 
- `map(plus(_))` 中`plus(_)` 就是将plus这个函数当做一个参数传给了map,`_`这里代表从集合中遍历出来一个元素.
- plus(_)也可以写成plus表示对Array(1, 3, 5, 7)遍历,将每次遍历元素传给plus的n变量.
- 进行3 + n 运算后,返回新的Int,并加入到新的集合.
- `def map[B, That](f: A => B)` 声明中的f: A => B 一个函数
- `参数函数实例`
``` scala
package scala.com.geekparkhub.core.scala.functionflow

object FunctionFlow005 {
  def main(args: Array[String]): Unit = {

    def puls(n: Int): Int = 3 + n

    val list = Array(1, 3, 5, 7).map(puls(_))
    println(list.mkString(","))

    println("puls函数类型 = " + (puls _))
  }
}
```


#### 6.19.3 匿名函数
- 没有名字的函数就是匿名函数,可以通过函数表达式来设置匿名函数.
- `匿名函数说明` : 
- 1.不需要写def 函数名.
- 2.不需要写返回类型,则使用类型推导.
- 3.`=` 变成 `=>`
- 4.如果有多行,则使用{}包括
- 5.`匿名函数实例`
``` scala
package scala.com.geekparkhub.core.scala.functionflow

object FunctionFlow006 {
  def main(args: Array[String]): Unit = {

    /**
      * 创建匿名函数
      * `(d: Double) => d * 3` 既是匿名函数
      * `(d: Double)` 既表示形参列表
      * `=>` 既表示规定语法后面是函数体
      * `d * 3` 既是表示函数体,如果有多个逻辑,可以使用{}将逻辑写在换括号内
      * `anonymous_function` 既表示指向匿名函数的变量
      */
    val anonymous_function = (d: Double) => d * 3
    println("anonymous function type = " + anonymous_function)
    println("anonymous function = " + anonymous_function(3))

    /**
      * 编写一个匿名函数,可以返回2个整数之和,并输出该匿名函数类型
      */
    val sum = (n1: Int, n2: Int) => n1 + n2
    println("sum type = " + sum)
    println("sum = " + sum(10, 20))
    
  }
}
```

#### 6.19.4 高阶函数
- 能够接受函数作为参数的函数叫做高阶函数(higher-order function),可使应用程序更加健壮.
- `高阶函数快速实例`
``` scala
package scala.com.geekparkhub.core.scala.functionflow

object FunctionFlow007 {
  def main(args: Array[String]): Unit = {

    def test(f: Double => Double, f2: Double => Int, d: Double) = {
      f(f2(d))
    }

    // sum
    def sum(n1: Double): Double = {
      n1 + n1
    }

    // mod
    def mod(n2: Double): Int = {
      n2.toInt % 2
    }

    val res = test(sum, mod, 6.0)
    println("res = " + res)
    
  }
}
```
- 高阶函数可以返回函数类型
``` scala
package scala.com.geekparkhub.core.scala.functionflow

object FunctionFlow008 {
  def main(args: Array[String]): Unit = {

    // 创建高阶函数
    def test(n: Int) = {

    /**
      * 创建匿名函数
      * 返回的匿名函数 (m: Int) => n - m`
      * 返回的匿名函数可以使用变量接收
      **/
      (m: Int) => n - m
    }

    // 常规风格
    val res01 = test(30)
    println("res01 type = " + res01)
    println("res01 = " + res01(10))
    println("res01 = " + res01(20))

    // 柯里化风格
    val res02 = test(20)(10)
    println("res02 = " + res02)
    
  }
}
```

#### 6.19.5 参数(类型)推断
- 参数推断省去类型信息(在某些情况下需要有应用场景,参数类型是可以推断出来,如list=(1,2,3),list.map(),map中函数参数类型是可以推断),同时也可以进行相应简写.
- `参数类型推断写法说明` :
- 参数类型是可以推断时,可以省略参数类型.
- 当传入的函数,只有单个参数时可以省去括号.
- 如果变量只在`=>`右边只出现一次可以用`_`下划线来代替.
- `参数(类型)推断实例`
- `参数(类型)推断知识点` : 
- 1.map是一个高阶函数,因此可以直接传入一个匿名函数.
- 2.当遍历list时参数类型可以推断出来,因此可以省略数据类型.
- 3.当传入函数,只有单个参数时,可以省略括号.
- 4.如果变量只在=>右边出现一次时,可以使用`_`下划线来代替.
``` scala
package scala.com.geekparkhub.core.scala.functionflow

object FunctionFlow009 {
  def main(args: Array[String]): Unit = {

    val list = List(1, 3, 5, 7, 9)

    /**
      * 创建匿名函数
      */

    // 参数类型未简写状态
    val anonymous01 = list.map((x: Int) => x + 1)
    // 通过类型推断,参数类型可以简写
    val anonymous02 = list.map((x) => x + 1)
    // 可以继续简写
    val anonymous03 = list.map(x => x + 1)
    // 还可以继续简写,最终简写为`_+1`
    val anonymous04 = list.map(_ + 1)
    println("anonymous01 = " + anonymous01)
    println("anonymous02 = " + anonymous02)
    println("anonymous03 = " + anonymous03)
    println("anonymous04 = " + anonymous04)


    // 常规调用f1函数
    val res01 = list.reduce(f1)
    // 参数类型未简写状态
    val res02 = list.reduce((n1: Int, n2: Int) => n1 + n2)
    // 通过类型推断,参数类型可以简写
    val res03 = list.reduce((n1, n2) => n1 + n2)
    // 可以继续简写,最终以简写为`_+_`
    val res04 = list.reduce(_ + _)
    println("res01 = " + res01)
    println("res02 = " + res02)
    println("res03 = " + res03)
    println("res04 = " + res04)
  }

  // 创建高阶函数
  def f1(n1: Int, n2: Int): Int = {
    n1 + n2
  }
}
```



#### 6.19.6 闭包(closure)
- 闭包就是一个函数和与其相关引用环境组合的一个整体(实体).
``` scala
// 1.用等价理解方式改写 2.对象属性理解
def minusxy(x: Int) = (y: Int) => x -y
// 3.f函数就是闭包
val f = minusxy(20)
println("f(1)=" + f(1))
println("f(2)=" + f(2))
```
- `(y: Int) => x –y`
- 返回的是一个匿名函数,因为该函数引用到到函数外的x,那么该函数和x整体形成一个闭包如 : 这里`val f = minusxy(20)` 的f函数就是闭包.
- 可以理解为返回函数是一个对象,而x就是该对象的一个字段,它们共同形成一个闭包.
- 当多次调用f时(可以理解多次调用闭包),发现使用的是同一个x,所以x不变.
- 在使用闭包时,主要搞清楚返回函数引用了函数外的哪些变量,因为它们会组合成一个整体(实体),形成一个闭包.
- `闭包实例`
``` scala
package scala.com.geekparkhub.core.scala.functionflow

object FunctionFlow010 {
  def main(args: Array[String]): Unit = {

    /**
      * 编写函数makeSuffix(suffix: String)
      * 可以接收一个文件后缀名(比如.jpg)]并返回一个闭包.
      * 调用闭包可以传入一个文件名,如果该文件名没有指定的后缀(比如.jpg)
      * 则返回文件名.jpg, 如果已经有.jpg后缀,则返回原文件名.
      * 要求使用闭包的方式完成
      */
    val f = makeSuffix(".jpg")
    println("f(\"1\") = " + f("1"))
    println("f(\"2.png\") = " + f("2.png"))
    println("f(\"3.jpg\") = " + f("3.jpg"))
  }

  //创建处理函数
  def makeSuffix(suffix: String) = {
    // 创建匿名函数
    (filename: String) => {
      // 如果文件后缀名等于.jpg,则返回原文件名
      if (filename.endsWith(suffix)) {
        filename
      } else {
        // 否则文件名+后缀名
        filename + suffix
      }
    }
  }
}
```


#### 6.19.7 函数柯里化(curry)
- 函数编程中,接受多个参数的函数都可以转化为接受单个参数的函数,这个转化过程就叫柯里化.
- 柯里化就是证明了函数只需要一个参数而已.
- 不用设立柯里化存在的意义这样的命题,柯里化就是以函数为主体这种思想发展必然产生的结果,(即 :  柯里化是面向函数思想的必然产生结果).
- `函数柯里化快速入门实例`
- 编写一个函数,接收两个整数,返回两个数的乘积.
``` scala
package scala.com.geekparkhub.core.scala.functionflow

object FunctionFlow011 {
  def main(args: Array[String]): Unit = {

    // 使用常规方式
    def product01(x: Int, y: Int) = x * y
    println("product01 = " + product01(2, 5))

    // 使用闭包方式
    def product02(x: Int) = (y: Int) => x * y
    println("product02 = " + product02(2)(5))

    // 使用函数柯里化方式
    def product03(x: Int)(y: Int) = x * y
    println("product03 = " + product03(2)(5))

  }
}
```
- `函数柯里化应用实例`
- 使用函数柯里化方式,比较两个字符串在忽略大小写的情况下是否相等.
``` scala
package scala.com.geekparkhub.core.scala.functionflow

object FunctionFlow012 {
  def main(args: Array[String]): Unit = {

    // 定义函数接收字符串是否相等
    def eq(s1: String, s2: String): Boolean = {
      s1.equals(s2)
    }

    // 定义隐式类
    implicit class Eq(s: String) {
      // 定义函数
      def core(s3: String)(f: (String, String) => Boolean): Boolean = {
        // core函数完转换大小写
        // f函数完成比较任务
        f(s.toLowerCase, s3.toLowerCase)
      }
    }

    val string = "scala"
    val res = string.core("Scala")(eq)
    println("res = " + res)

  }
}
```

#### 6.19.8 控制抽象
- 控制抽象是满足如下条件
- 1.参数是函数.
- 2.函数参数没有输入值也没有返回值.
- `实现类似while until函数实例`
``` scala
package scala.com.geekparkhub.core.scala.functionflow

object FunctionFlow013 {
  def main(args: Array[String]): Unit = {
    var x = 10

    // 函数名为until,实现了类似while循环效果
    until(x > 0) {
      x -= 1
      println("until x = " + x)
    }
  }

  // v: => Boolean 是后一个没有输入值,返回Boolean类型函数
  // block: => Unit 没有输入值,也没有返回值函数
  def until(v: => Boolean)(block: => Unit): Unit = {
    // 类似while循环,递归
    if (v) {
      block
      until(v)(block)
    }
  }
}
```



### 6.20 使用递归方式去思考Scala编程
#### 6.20.1 基本介绍
> Scala是运行在Java虚拟机(Java Virtual Machine)之上,因此具有如下特点 : 
> 
> 轻松实现和丰富的Java类库互联互通.
> 
> 它既支持面向对象的编程方式,又支持函数式编程.
> 
> 它写出的程序像动态语言一样简洁,但事实上它确是严格意义上的静态语言.
> 
> Scala就像一位武林中的集大成者,将过去几十年计算机语言发展历史中的精萃集于一身,化繁为简,为程序员们提供了一种新的选择.
> 
> 设计者马丁·奥得斯基希望程序员们将编程作为简洁,高效,令人愉快的工作,同时也让程序员们进行关于编程思想的新的思考.

#### 6.20.2 Scala提倡函数式编程(递归思想)
> 编程范式 : 
> 
> 在所有编程范式中,面向对象编程(Object-Oriented Programming)无疑是最大赢家.
> 
> 但其实面向对象编程并不是一种严格意义上编程范式.
> 
> 严格意义上编程范式分为 : 
> 
> 命令式编程 (Imperative Programming)
> 函数式编程 (Functional Programming)
> 逻辑式编程 (Logic Programming)
> 
> 面向对象编程只是上述几种范式一个交叉产物,更多的还是继承了命令式编程的基因.
> 
> 在传统的语言设计中,只有命令式编程得到了强调,那就是程序员要告诉计算机应该怎么做,而递归则通过灵巧的函数定义,告诉计算机做什么.
> 
> 因此在使用命令式编程思维的程序中,是现在多数程序采用的编程方式,递归出镜的几率很少,而在函数式编程中,可以随处见到递归方式.


#### 6.20.3 应用实例 一
> scala中循环不建议使用while和do...while,而建议使用递归.

##### 6.20.3.1 常规方式循环计算
``` scala
package scala.com.geekparkhub.core.scala.instance

import java.text.SimpleDateFormat
import java.util.Date

object InstanceFlow {
  def main(args: Array[String]): Unit = {

    // 使用常规方式循环计算
    var num = BigInt(1)
    var res = BigInt(0)
    var max = BigInt(99999999l)

    /**
      * 执行开始时间
      */
    val now: Date = new Date()
    val dateFormat: SimpleDateFormat = new SimpleDateFormat("ss")
    val time1 = dateFormat.format(now)
    println("执行开始时间 = " + time1 + ".s")


    while (num <= max) {
      res += num
      num += 1
    }
    println("res = " + res)

    /**
      * 执行结束时间
      */
    val now2: Date = new Date()
    val time2 = dateFormat.format(now2)
    println("执行结束时间 = " + time2 + ".s")

  }
}
```
##### 6.20.3.1 使用函数式编程方式-递归
- 函数式编程重要思想就是尽量不要产生额外的影响,上面的常规方式就不符合函数式编程思想.
``` scala
package scala.com.geekparkhub.core.scala.instance

import java.text.SimpleDateFormat
import java.util.Date

object InstanceFlow002 {
  def main(args: Array[String]): Unit = {

    // 使用递归方式循环计算
    var num = BigInt(1)
    var sum = BigInt(0)
    var max = BigInt(99999999l)

    /**
      * 执行开始时间
      */
    val now: Date = new Date()
    val dateFormat: SimpleDateFormat = new SimpleDateFormat("ss")
    val time1 = dateFormat.format(now)
    println("执行开始时间 = " + time1 + ".s")

    var res = mx(num, sum)
    println("res = " + res)

    /**
      * 执行结束时间
      */
    val now2: Date = new Date()
    val time2 = dateFormat.format(now2)
    println("执行结束时间 = " + time2 + ".s")
  }

  // 定义递归函数
  def mx(num: BigInt, sum: BigInt): BigInt = {
    if (num <= 99999999l) return mx(num + 1, sum + num)
    else return sum
  }
}
```


#### 6.20.4 应用实例 二
- 求最大值最小值
``` scala
package scala.com.geekparkhub.core.scala.instance

object InstanceFlow003 {
  def main(args: Array[String]): Unit = {
    // 定义集合
    var maxs = max(List(1, 3, 5, 7, 9, 11, 13, 15, 17,100))
    var mins = min(List(1, 3, 5, 7, 9, 11, 13, 15, 17,100))
    println("max is = " + maxs)
    println("min is = " + mins)
  }

  /**
    * 定义递归函数
    * @param n
    * @return
    */
  def max(n: List[Int]): Int = {
    // 如果集合元素为空,则抛出异常
    if (n.isEmpty)
      throw new java.util.NoSuchElementException
    // 如果集合元素为一个元素,则返回本身
    if (n.size == 1)
      n.head
    // 如果集合头部元素大于集合末尾元素,则返回集合头部元素
    else if (n.head > max(n.tail)) n.head
    // 否则返回集合末尾元素
    else max(n.tail)
  }

  /**
    * 定义递归函数
    * @param n
    * @return
    */
  def min(n: List[Int]): Int = {
    // 如果集合元素为空,则抛出异常
    if (n.isEmpty)
      throw new java.util.NoSuchElementException
    // 如果集合元素为一个元素,则返回本身
    if (n.size == 1)
      n.head
    // 如果集合头部元素大小于集合末尾元素,则返回集合头部元素
    else if (n.head < max(n.tail)) n.head
    // 否则返回集合末尾元素
    else max(n.tail)
  }
}
```


#### 6.20.5 使用函数式编程方式-字符串翻转
``` scala
package scala.com.geekparkhub.core.scala.instance

object InstanceFlow004 {
  def main(args: Array[String]): Unit = {
    var res = reverse("scala")
    println("res = " + res)
  }

  /**
    * 定义递归函数
    */
  def reverse(v: String): String = {
    // 如果字符串长度等于1,则返回字符串本身
    if (v.length == 1) v
    // 否则调用自身递归函数,将字符串尾部反转到头部在与头部相加,即实现字符串反转
    else reverse(v.tail) + v.head
  }
}
```

#### 6.20.6 使用递归-求阶乘
``` scala
package scala.com.geekparkhub.core.scala.instance

object InstanceFlow005 {
  def main(args: Array[String]): Unit = {
    var res = factorial(4)
    println("res = " + res)
  }

  /**
    * 定义递归函数
    */
  def factorial(n: Int): Int = {
    // 如果接收参数为0,则返回1
    if (n == 0) 1
    // 否则接收参数的乘以自身递归函数
    else n * factorial(n - 1)
  }
}
```


### 6.21 并发编程模型 Akka
#### 6.21.1 Akka 介绍
![enter image description here](https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2537727085,4267953402&fm=26&gp)
> Akka官方地址 : [https://akka.io/](https://akka.io/)
> 
> Akka官方文档 : [https://akka.io/docs/](https://akka.io/docs/)
> 
>  Scala版本 Akka官方文档 : [doc.akka.io/docs/akka/language=scala](https://doc.akka.io/docs/akka/current/guide/introduction.html?language=scala)
> 
> Akka是JAVA 虚拟机JVM平台上构建高并发、分布式和容错应用的工具包和运行时,可以理解成Akka是编写并发程序框架.
> 
> Akka是基于Scala编程语言构建而成,同时提供了Scala和JAVA的开发接口.
> 
> Akka主要解决问题是 : 可以轻松的编写出高效稳定并发程序,不再过多考虑线程、锁和资源竞争等细节.

#### 6.21.2 Actor模型 用于解决哪些问题?
> 处理并发问题关键是要保证共享数据一致性和正确性,因为程序是多线程时,多个线程对同一个数据进行修改,若不加同步条件,势必会造成数据污染,但是当我们对关键代码加入同步条件synchronized后,实际上大并发就会阻塞在这段代码,对程序效率有很大影响.
>
> 若是用单线程处理则不会有数据一致性的问题,但是系统性能又不能保证.
> 
> Actor模型出现解决了这个问题,简化并发编程提升程序性能,你可以理解为：Actor模型是一种处理并发问题很牛的解决方案.


#### 6.21.3 Akka Actor模型
##### 6.21.3.1 Actor模型 说明
![enter image description here](https://image-static.segmentfault.com/352/265/3522656644-5907d984e8b76_articlex)
> 1.Akka处理并发的方法基于Actor模型.
> 
> 2.在基于Actor系统里所有事物都是Actor,就好像在面向对象设计里面所有的事物都是对象一样.

> 3.Actor模型是作为一个并发模型设计和架构,Actor与Actor之间只能通过消息通信,如图的信封.

> 4.Actor与Actor之间只能用消息进行通信,当一个Actor给另外一个Actor发消息,消息是有顺序的(消息队列),只需要将消息投寄的相应的邮箱即可.
> 
> 5.怎么处理消息是由接收消息的Actor决定,发送消息Actor可以等待回复,也可以异步处理Ajax.
> 
> 6.ActorSystem职责是负责创建并管理其创建的Actor,ActorSystem是单例模式(ActorSystem可以是一个工厂专门创建Actor),一个JVM进程中有一个即可,而Acotr是可以有多个.
> 
> 7.Actor模型是对并发模型进行了更高抽象.
> 
> 8.Actor模型是异步、非阻塞、高性能事件驱动编程模型.
> 
> 9.Actor模型是轻量级事件处理(1GB内存可容纳百万级别个Actor),因此处理大并发性能高.

##### 6.21.3.2 Actor模型 工作机制
> 1.ActorySystem创建Actor.
> 
> 2.ActorRef:可以理解成是Actor的代理或者引用,消息是通过ActorRef来发送,而不能通过Actor发送消息,通过哪个ActorRef发消息,就表示把该消息发给哪个Actor.
> 
> 3.消息发送到Dispatcher Message (消息分发器),它得到消息后会将消息进行分发到对应的MailBox,(注: Dispatcher Message可以理解成是一个线程池,MailBox可以理解成是消息队列,可以缓冲多个消息遵守FIFO).
> 
> 4.Actor可以通过receive方法来获取消息然后进行处理.


##### 6.21.3.3 Actor模型 消息机制
![enter image description here](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/scala/start_005.jpg)

> 1.每一个消息就是一个Message对象,Message继承Runable,因为Message就是线程类.
> 
> 2.从Actor模型工作机制看上去很麻烦,但是程序员编程时只需要编写Actor就可以,其它的交给Actor模型完成即可.
> 
> 3.`A Actor`要给`B Actor`发送消息,那么`A Actor`要先拿到(也称为持有)`B Actor`代理对象ActorRef才能发送消息.


#### 6.21.4 Actor模型 快速入门
- 创建Actor可以给自身发送消息.
- 在Maven项目中创建子模块 | 此过程省略
- 在子模块中向`pom.xml`追加相关依赖信息.
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.geekparkhub.core.scala</groupId>
    <artifactId>scala_server</artifactId>
    <packaging>pom</packaging>
    <version>1.0-SNAPSHOT</version>

    <!-- 定义版本常量 -->
    <properties>
        <encoding>UTF-8</encoding>
        <scala.version>2.11.8</scala.version>
        <scala.compat.version>2.11</scala.compat.version>
        <akka.version>2.4.18</akka.version>
    </properties>

    <dependencies>
        <!-- 添加scala依赖 -->
        <dependency>
            <groupId>org.scala-lang</groupId>
            <artifactId>scala-library</artifactId>
            <version>${scala.version}</version>
        </dependency>

        <!-- 添加akka actor依赖 -->
        <dependency>
            <groupId>com.typesafe.akka</groupId>
            <artifactId>akka-actor_${scala.compat.version}</artifactId>
            <version>${akka.version}</version>
        </dependency>

        <!-- 多进程之间Actor通信 -->
        <dependency>
            <groupId>com.typesafe.akka</groupId>
            <artifactId>akka-remote_${scala.compat.version}</artifactId>
            <version>${akka.version}</version>
        </dependency>
    </dependencies>

    <!-- 指定插件-->
    <build>
        <!-- 指定源码包&测试包位置 -->
        <sourceDirectory>src/main/scala</sourceDirectory>
        <testSourceDirectory>src/test/scala</testSourceDirectory>
        <plugins>
            <!-- 指定编译scala插件 -->
            <plugin>
                <groupId>net.alchim31.maven</groupId>
                <artifactId>scala-maven-plugin</artifactId>
                <version>3.2.2</version>
                <executions>
                    <execution>
                        <goals>
                            <goal>compile</goal>
                            <goal>testCompile</goal>
                        </goals>
                        <configuration>
                            <args>
                                <arg>-dependencyfile</arg>
                                <arg>${project.build.directory}/.scala_dependencies</arg>
                            </args>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>

    <modules>
        <module>akka-flow</module>
    </modules>
</project>
```
- `创建Actor实例`
``` scala
package com.geekparkhub.core.scala.akka.actor

import akka.actor.{Actor, ActorRef, ActorSystem, Props}

/**
  * 创建AkkaActorFlow并继承Actor
  */
class AkkaActorFlow extends Actor {
  
  /**
    * 重写Actor receive方法.
    * receive方法会被该ActorMailBox调用.
    * 当该ActorMailBox接收到消息,就会调用receive方法
    * @return
    */
  override def receive: Receive = {
    case "Hello Actor!" => println("Hey Mac!")
    case "I am eating fried chicken in the square." => println("Cool, I am drinking red wine in the cafe.")
    case "Goodbye" => {
      println("Goodbye 👋👋,See you tomorrow!")
      // 停止邮箱服务
      context.stop(self)
      // 停止ActorSystem服务
      context.system.terminate()
    }
    case _ => println("⚠️ : Message match failed!")
  }
}

object AkkaActorFlowRun {

  /**
    * 创建ActorSystem
    * ActorSystem负责创建Actor
    */
  val actorServer = ActorSystem("ActorServer")

  /**
    * 创建Actor同时并返回ActorRef
    * Props[AkkaActorFlow] 既表示使用反射创建AkkaActorFlow实例.
    * "AkkaActorFlow" 既表示为actor取名.
    * akkaActorFlowRef: ActorRef 既是Props[AkkaActorFlow]的ActorRef.
    * 创建AkkaActorFlow实例由ActorSystem接管
    */
  val akkaActorFlowRef: ActorRef = actorServer.actorOf(Props[AkkaActorFlow], "AkkaActorFlow")

  def main(args: Array[String]): Unit = {

    // 向发送消息
    akkaActorFlowRef ! "Hello Actor!"
    akkaActorFlowRef ! "I am eating fried chicken in the square."
    akkaActorFlowRef ! "follow me!"

    // 退出ActorSystem
    akkaActorFlowRef ! "Goodbye"
  }
}
```


#### 6.21.5 Actor模型应用实例 - Actor通讯
- 创建2个Actor,分别是AActor和BActor.
- AActor和BActor之间可以相互发送消息.
- `Actor通讯实例`
- 1.创建AActor
``` scala
package com.geekparkhub.core.scala.akka.actors

import akka.actor.{Actor, ActorRef}

/**
  * AActor
  * @param actorRef
  */
class AActor(actorRef: ActorRef) extends Actor {

  val bActorRef: ActorRef = actorRef

  override def receive: Receive = {
    // 开始建立消息
    case "Start Message" => {
      println("AActor 开始建立消息会话")
      self ! "Message001"
    }
    // A向B发送第一条消息
    case "Message001" => {
      println("AActor (Tomcat) : ✌️")
      Thread.sleep(1000)
      bActorRef ! "Message001"
    }
    // A向B发送第二条消息
    case "Message002" => {
      println("AActor (Tomcat) : 🐒")
      Thread.sleep(1000)
      bActorRef ! "Message002"
    }
    // A向B发送第三条消息
    case "Message003" => {
      println("AActor (Tomcat) : 🌛")
      Thread.sleep(1000)
      bActorRef ! "Message003"
    }
    // A向B发送第四条消息
    case "Message004" => {
      println("AActor (Tomcat) : 😎")
      Thread.sleep(1000)
      bActorRef ! "Message004"
    }
    // A向B发送第五条消息结束会话
    case "Stop Message" => {
      bActorRef ! "Stop"
      stopserver()
    }
  }

  /**
    * 停止服务函数
    * @return
    */
  def stopserver() = {
    println("AActor (Tomcat) : Goodbye")
    Thread.sleep(1000)
    // 停止邮箱服务
    context.stop(self)
    context.stop(bActorRef)
    // 停止ActorSystem服务
    context.system.terminate()
  }
}
```

- 2.创建BActor
``` scala
package com.geekparkhub.core.scala.akka.actors

import akka.actor.{Actor}

/**
  * BActor
  */
class BActor extends Actor {

  override def receive: Receive = {
    // 通过sender向AActor回复第一条消息
    case "Message001" => println("\t\t\t\t\t\tBActor (Mac) : ✋")
      Thread.sleep(1500)
      sender() ! "Message002"
    // 通过sender向AActor回复第二条消息
    case "Message002" => println("\t\t\t\t\t\tBActor (Mac) : 🐵")
      Thread.sleep(1500)
      sender() ! "Message003"
    // 通过sender向AActor回复第三条消息
    case "Message003" => println("\t\t\t\t\t\tBActor (Mac) : ✨")
      Thread.sleep(1500)
      sender() ! "Message004"
    // 通过sender向AActor回复第四条消息
    case "Message004" => println("\t\t\t\t\t\tBActor (Mac) : 😀")
      Thread.sleep(1500)
      sender() ! "Message004"
    case "Stop" => println("\t\t\t\t\t\tBActor (Mac) : Goodbye 👋👋,See you tomorrow!")
      sender() ! "Stop"
  }
}
```

- 3.创建ActorFlow
``` scala
package com.geekparkhub.core.scala.akka.actors

import akka.actor.{ActorRef, ActorSystem, Props}

/**
  * ActorFlow
  */
object ActorFlow extends App {

  /**
    * 创建ActorSystem
    * ActorSystem负责创建Actor
    */
  val actorServer = ActorSystem("ActorServer")

  // 创建BActor代理
  val bActorRef: ActorRef = actorServer.actorOf(Props[BActor], "BActor")

  // 创建AActor代理
  val aActorRef: ActorRef = actorServer.actorOf(Props(new AActor(bActorRef)), "AActor")

  // 开始消息
  aActorRef ! "Start Message"
  // 结束消息
  aActorRef ! {
    Thread.sleep(10000)
    "Stop Message"
  }
}
```

- 4.运行程序,查看执行结果
``` 
AActor 开始建立消息会话
AActor (Tomcat) : ✌️
						BActor (Mac) : ✋
AActor (Tomcat) : 🐒
						BActor (Mac) : 🐵
AActor (Tomcat) : 🌛
						BActor (Mac) : ✨
AActor (Tomcat) : 😎
						BActor (Mac) : 😀
AActor (Tomcat) : Goodbye
					BActor (Mac) : Goodbye 👋👋,See you tomorrow!
```


- `Actor通讯实例总结`
- 1.两个Actor通讯机制和自身Actor自身发送消息机制基本一样.
- 2.如果A Actor在需要给B Actor发送消息,则需要持有B Actor中的ActorRef,可以通过创建时,传入B Actor(代理对象/ActorRef).
- 3.当B ActorRef在receive()方法中接收到消息,需要回复时,可以通过sender()方法获取到发送A Actor代理对象.
- `如何理解Actor receive()方法被调用?`
- 每一个Actor都有对应的MailBox邮箱.
- MailBox实现了Runnable接口,处于运行状态.
- 当有消息时,就会到达MailBox并调用Actor receive()方法,将消息推送给receive


#### 6.21.6 Akka 网络编程
> Akka支持面向大并发后端服务程序,网络通信是服务端程序重要的一部分.
> 
> 网络编程有两种 : 
> 
> 1.`TCP socket编程`,是网络编程主流,之所以叫Tcp socket编程,是因为底层是基于Tcp/ip协议,比如:QQ聊天.
> 
> 2.`B/S结构Http编程`,使用浏览器去访问服务器时,使用的就是http协议,而http底层依旧是用tcp socket实现,比如:京东商城.
> 
> 端口(port)
> 所指端口不是指物理意义上的端口,而是特指TCP/IP协议中端口,是逻辑意义上的端口.
> 如果把IP地址比作一间房子,端口就是出入这间房子的门,真正的房子只有几个门,但是一个IP地址的端口可以有65535（即：256×256-1）个之多！端口是通过端口号来标记,(端口号0：Reserved).
> 
> 端口(port)-分类
> 0号是保留端口.
> 1-1024是固定端口,又叫有名端口,即被某些程序固定使用,一般不使用.
> 22: SSH远程登录协议 / 23: telnet使用 / 21: ftp使用
> 25: smtp服务使用 / 80: iis使用 / 7: echo服务
> 1025-65535是动态端口,这些端口可以使用.

#### 6.21.7 Akka网络编程 - 服务端与客户端交互
- 1.创建服务端
``` scala
package com.geekparkhub.core.scala.akka.workflow.server

import akka.actor.{Actor, ActorRef, ActorSystem, Props}
import com.geekparkhub.core.scala.akka.workflow.common.{ClientMessageFlow, ServerMessageFlow}
import com.typesafe.config.ConfigFactory

class ServerFlow extends Actor {
  // 复写receive()方法
  override def receive: Receive = {
    case "ServerStart" => println("---- Server Start ----")
    // 服务端接收ClientMessageFlow(mes)
    case ClientMessageFlow(mes) => {
      // 模式匹配分解客户端信息关键字
      mes match {
        case "Hello" => sender() ! ServerMessageFlow("Hey ✋✋")
        case "🐒" => sender() ! ServerMessageFlow("这是一只程序员!")
        case "🌛" => sender() ! ServerMessageFlow("你问我爱你有多深,月亮代表我的心!")
        case "😎" => sender() ! ServerMessageFlow("你酷帅到极致!")
        case "Goodbye" => sender() ! ServerMessageFlow("Goodbye 👋👋,See you tomorrow!")
        case _ => sender() ! ServerMessageFlow("❓❓❓")
      }
    }
  }
}

object ServerFlowRun extends App {

  //定义服务端ip和端口
  val serverHost = "127.0.0.1"
  val serverPort = 9088

  /**
    * 使用ConfigFactory parseString()方法解析字符串,指定客户端IP和端口
    */
  val config = ConfigFactory.parseString(
    s"""
       |akka.actor.provider="akka.remote.RemoteActorRefProvider"
       |akka.remote.netty.tcp.hostname=$serverHost
       |akka.remote.netty.tcp.port=$serverPort
        """.stripMargin)

  // 创建ActorSystem
  val server = ActorSystem("server", config)
  // 创建serverFlowRef
  val serverFlowRef: ActorRef = server.actorOf(Props[ServerFlow], "ServerFlow")
  // 启动serverFlowRef,指向自身服务端mailbox -> receive()方法
  serverFlowRef ! "ServerStart"
}
```

- 2.创建客户端
``` scala
package com.geekparkhub.core.scala.akka.workflow.client

import akka.actor.{Actor, ActorRef, ActorSelection, ActorSystem, Props}
import com.geekparkhub.core.scala.akka.workflow.common.{ClientMessageFlow, ServerMessageFlow}
import com.typesafe.config.ConfigFactory

import scala.io.StdIn

class ClientFlow(serverHost: String, serverPort: Int) extends Actor {

  // 定义服务端serverFlowRef
  var serverFlowRef: ActorSelection = _

  /**
    * 重写初始化方法
    * 在Akka开发中,通常将初始化工作交给preStart()方法
    * 因为preStart()方法会在运行前执行
    */
  override def preStart(): Unit = {

    serverFlowRef = context.actorSelection(s"akka.tcp://server@${serverHost}:${serverPort}/user/ServerFlow")
    // Println Test
    //    println("preStart() Method has been executed !")
    //    println("serverFlowRef IP = " + serverFlowRef)
  }

  // 复写receive()方法
  override def receive: Receive = {
    case "ClientStart" => println("---- Client Start ----")
    // 将接收到的客户端信息转发给服务端
    case mes: String => serverFlowRef ! ClientMessageFlow(mes)
    // 将服务端信息转发给客户端
    case ServerMessageFlow(mes) => println(s"(ServerFlow Mac) : $mes")
  }
}

object ClientFlowRun extends App {

  // 定义客户端IP和端口 & 指定服务端IP和端口
  val (clientHost, clientPort, serverHost, serverPort) = ("127.0.0.1", 9089, "127.0.0.1", 9088)

  /**
    * 使用ConfigFactory parseString()方法解析字符串,指定客户端IP和端口
    */
  val config = ConfigFactory.parseString(
    s"""
       |akka.actor.provider="akka.remote.RemoteActorRefProvider"
       |akka.remote.netty.tcp.hostname=$clientHost
       |akka.remote.netty.tcp.port=$clientPort
        """.stripMargin)

  // 创建ActorSystem
  val client = ActorSystem("client", config)
  // 创建serverFlowRef
  val clientFlowRef: ActorRef = client.actorOf(Props(new ClientFlow(serverHost, serverPort)), "ClientFlow")
  // 启动clientFlowRef,指向自身客户端mailbox -> receive()方法
  clientFlowRef ! "ClientStart"

  // 客户端向服务端发送消息
  while (true) {
    Thread.sleep(1000)
    println(s" 正在与$serverHost:$serverPort 建立连接,开始你的心灵探索吧!")
    // 接收客户端输入内容
    var mes = StdIn.readLine("(ClientFlow User) : ")
    clientFlowRef ! mes
  }
}
```

- 3.创建信息协议
``` scala
package com.geekparkhub.core.scala.akka.workflow.common

/**
  * 使用样例类模板 (自动实现序列化功能)
  * 创建信息协议
  */

// 定义客户端与服务端(信息序列化)交互协议
case class ClientMessageFlow(mes: String)

// 定义服务端与客户端(信息序列化)交互协议
case class ServerMessageFlow(mes: String)
```

- 4.查看9088服务端口是否启动
```
systemhub:~ system$ netstat -anb | grep 9088
tcp4       0      0  127.0.0.1.9088   *.*  LISTEN  0  0
systemhub:~ system$ 
```
- 5.查看9089客户端口是否启动
```
systemhub:~ system$ netstat -anb | grep 9089
tcp4       0      0  127.0.0.1.9089    *.* LISTEN  0  0
systemhub:~ system$
```

- 6.启动应用顺序 : 先启动服务端程序,依次启动客户端程序.
- 客户端向服务端发送信息,并查看消息结果.
```
---- Client Start ----
 正在与127.0.0.1:9088 建立连接,开始你的心灵探索吧!
(ClientFlow User) : Hello
(ServerFlow Mac) : Hey ✋✋

 正在与127.0.0.1:9088 建立连接,开始你的心灵探索吧!
(ClientFlow User) : 🐒
(ServerFlow Mac) : 这是一只程序员!

 正在与127.0.0.1:9088 建立连接,开始你的心灵探索吧!
(ClientFlow User) : 🌛
(ServerFlow Mac) : 你问我爱你有多深,月亮代表我的心!

 正在与127.0.0.1:9088 建立连接,开始你的心灵探索吧!
(ClientFlow User) : 😎
(ServerFlow Mac) : 你酷帅到极致!

 正在与127.0.0.1:9088 建立连接,开始你的心灵探索吧!
(ClientFlow User) : nice
(ServerFlow Mac) : ❓❓❓

 正在与127.0.0.1:9088 建立连接,开始你的心灵探索吧!
(ClientFlow User) : Goodbye
(ServerFlow Mac) : Goodbye 👋👋,See you tomorrow!
```

#### 6.21.6 Spark Master Worker 进程通讯
- `说明`
- 深入理解Spark的Master和Worker通讯机制.
- 加深对主从服务心跳检测机制(HeartBeat)的理解,方便以后spark源码二次开发
- `实例分析`
- 1.worker注册到Master,Master完成注册,并回复worker注册成功.
- 2.worker定时发送心跳,并在Master接收心跳状态.
- 3.Master接收到worker心跳后,要更新该worker最近一次发送心跳时间.
- 4.给Master启动定时任务,定时检测注册的worker有哪些没有更新心跳,并将其从hashmap中删除.
- 5.master worker进行分布式部署

- 创建Master
``` scala
package com.geekparkhub.core.scala.akka.sparkflow.master

import akka.actor.{Actor, ActorRef, ActorSystem, Props}
import com.geekparkhub.core.scala.akka.sparkflow.commonflow.{HearBeat, RegisteredWorkerFlowInfo, RegisteredWorkerFlowInfos, RemoveTimeOutWorker, StartTimeOutWorke, WorkerFlowInfo}
import com.typesafe.config.ConfigFactory

import scala.collection.mutable
import scala.concurrent.duration._

class MasterFlow extends Actor {
  // 定义HashMap用于管理WorkerFlowInfo
  val workers = mutable.Map[String, WorkerFlowInfo]()

  // 复写receive()方法
  override def receive: Receive = {
    case "MasterFlowStart" => {
      println("---- MasterFlow Start ----")
      self ! StartTimeOutWorke
    }
    // 接收WorkerFlow注册信息
    case RegisteredWorkerFlowInfo(id, cpu, ram) => {
      // 判断WorkerFlow注册信息是否已注册,如果未注册,则执行以下逻辑
      if (!workers.contains(id)) {
        // 创建workerFlowInfo对象
        val workerFlowInfo = new WorkerFlowInfo(id, cpu, ram)
        // 将workerFlowInfo追加到HashMap中
        workers += ((id, workerFlowInfo))
        println("All Workers = " + workers)
        // 追加完毕后,MasterFlow应回复WorkerFlow注册成功
        sender() ! RegisteredWorkerFlowInfos
      }
    }

    // master收到worker的心跳消息之后，更新woker的上一次心跳时间
    case HearBeat(id) => {
      val info: WorkerFlowInfo = workers(id)
      // 更改心跳时间
      info.lastHeartBeatTime = System.currentTimeMillis()
      println("master更新Worker心跳 ID = " + id)
    }
    case StartTimeOutWorke => {
      println("开启定时检测Worker心跳任务")
      // 使用调度器时候必须导入dispatcher,因为该包涉及到隐式转换
      import context.dispatcher
      /**
        * worker通过"context.system.scheduler.schedule"启动一个定时器，定时向master 发送心跳信息，需要指定
        * 四个参数：
        * 第一个参数是需要指定延时时间，此处指定的间隔时间为0毫秒；
        * 第二个参数是间隔时间，即指定定时器的周期性执行时间，我们这里指定为9秒；
        * 第三个参数是发送消息给谁，我们这里指定发送消息给自己，使用变量self即可；
        * 第四个参数是指发送消息的具体内容；
        * 注意：由于我们将消息周期性的发送给自己，因此我们自己需要接受消息并处理，也就是需要定义下面的RemoveTimeOutWorker
        */
      context.system.scheduler.schedule(0 millis, 9000 millis, self, RemoveTimeOutWorker)
    }
    case RemoveTimeOutWorker => {
      val workerInfos: Iterable[WorkerFlowInfo] = workers.values
      val nowTime: Long = System.currentTimeMillis()
      // //过滤超时worker,将过滤超时的worker删除
      workerInfos.filter(workerFlowInfo => (nowTime - workerFlowInfo.lastHeartBeatTime) > 6000).foreach(workerFlowInfo => workers.remove(workerFlowInfo.id))
      println(s"====== 存活Worker ${workers.size}  ======")
    }
  }
}

object MasterFlowRun {
  def main(args: Array[String]): Unit = {
    if (args.length != 3) {
      println("Please enter the following parameters <masterHost masterPort MasterActorName>")
      sys.exit()
    }

    // 定义Master服务端ip和端口
    val masterHost = args(0)
    val masterPort = args(1)
    val MasterActorName = args(2)

    //    val masterHost = "127.0.0.1"
    //    val masterPort = 10001

    /**
      * 使用ConfigFactory parseString()方法解析字符串,指定客户端IP和端口
      */
    val config = ConfigFactory.parseString(
      s"""
         |akka.actor.provider="akka.remote.RemoteActorRefProvider"
         |akka.remote.netty.tcp.hostname=${masterHost}
         |akka.remote.netty.tcp.port=${masterPort}
        """.stripMargin)

    // 创建 ActorSystem
    val master = ActorSystem("master", config)
    // 创建 masterFlowRef
    val masterFlowRef: ActorRef = master.actorOf(Props[MasterFlow], s"${MasterActorName}")
    // 启动masterFlowRef,指向自身服务端mailbox -> receive()方法
    masterFlowRef ! "MasterFlowStart"
  }
}
```
- 创建 InformationProtocol
``` scala
package com.geekparkhub.core.scala.akka.sparkflow.commonflow

/**
  * 使用样例类模板 (自动实现序列化功能)
  * 创建信息协议
  */

// 定义WorkerFlow与MasterFlow(注册信息序列化)交互协议
case class RegisteredWorkerFlowInfo(id: String, cpu: Int, ram: Int)


/**
  * 定义WorkerFlowInfo
  * 将WorkerFlowInfo保存在MasterFlow HashMap中
  * HashMap将管理与扩展WorkerFlow
  *
  * @param id
  * @param cpu
  * @param ram
  */
class WorkerFlowInfo(val id: String, val cpu: Int, val ram: Int){
  // 定义最后一次心跳时间
  var lastHeartBeatTime: Long = System.currentTimeMillis()
}

// worker给master发送心跳信息
case class HearBeat(id: String)

// 当WorkerFlow注册成功,MasterFlow将返回RegisteredWorkerFlowInfo实例对象
case object RegisteredWorkerFlowInfos

// worker定时向master发送心跳消息
case object SendHeartBeat

// master给自己发送一个触发检查超时worker的信息
case object StartTimeOutWorke

// master自己给自己发送一个检查超时worker的信息,并启动一个调度器，周期新检测删除超时worker
case object CheckTimeOutWorker

// master发送给自己的消息，删除超时的worker
case object RemoveTimeOutWorker
```
- 创建Worker
``` scala
package com.geekparkhub.core.scala.akka.sparkflow.workerflow

import akka.actor.{Actor, ActorRef, ActorSelection, ActorSystem, Props}
import com.geekparkhub.core.scala.akka.sparkflow.commonflow.{HearBeat, RegisteredWorkerFlowInfo, RegisteredWorkerFlowInfos, SendHeartBeat}
import com.typesafe.config.ConfigFactory

import scala.language.postfixOps
import scala.concurrent.duration._

class WorkerFlow(masterHost: String, masterPort: Int, MasterActorName: String) extends Actor {

  // 定义master(代理对象) masterRef
  var masterProxy: ActorSelection = _
  val id = java.util.UUID.randomUUID().toString

  /**
    * 重写初始化方法
    * 在Akka开发中,通常将初始化工作交给preStart()方法
    * 因为preStart()方法会在运行前执行
    */
  override def preStart(): Unit = {
    // 初始化 master(代理对象)
    masterProxy = context.actorSelection(s"akka.tcp://master@${masterHost}:${masterPort}/user/${MasterActorName}")
    // PrintlnTest
    println("preStart() Method has been executed !")
    println("masterProxy = " + masterProxy)
  }

  // 复写receive()方法
  override def receive: Receive = {
    case "WorkerFlowStart" => {
      println("---- WorkerFlow Start ----")
      // 向MasterFlow_01发送注册请求
      masterProxy ! RegisteredWorkerFlowInfo(id, 32, 32 * 1024)
    }

    // 如WorkerFlow注册成功,则输出WorkerFlow状态信息
    case RegisteredWorkerFlowInfos => {
      println("WorkerFlow ID = " + id + " , Registration Success!")

      // 使用调度器时候必须导入dispatcher,因为该包涉及到隐式转换
      import context.dispatcher
      /**
        * worker通过"context.system.scheduler.schedule"启动一个定时器，定时向master 发送心跳信息，需要指定
        * 四个参数：
        * 第一个参数是需要指定延时时间，此处指定的间隔时间为0毫秒；
        * 第二个参数是间隔时间，即指定定时器的周期性执行时间，我们这里指定为3秒；
        * 第三个参数是发送消息给谁，我们这里指定发送消息给自己，使用变量self即可；
        * 第四个参数是指发送消息的具体内容；
        * 注意：由于我们将消息周期性的发送给自己，因此我们自己需要接受消息并处理，也就是需要定义下面的SendHeartBeat
        */
      context.system.scheduler.schedule(0 millis, 3000 millis, self, SendHeartBeat)
    }

    case SendHeartBeat => {
      // 开始向master发送心跳
      println(s"------- WorkerFlow = $id 发送心跳 -------")
      masterProxy ! HearBeat(id)
    }
  }
}

object WorkerFlowRun {
  def main(args: Array[String]): Unit = {

    if (args.length != 6) {
      println("Please enter the following parameters <workerHost workerPort WorkerActorName masterHost masterPort MasterActorName>")
      sys.exit()
    }

    // 定义workerIP和端口 & 指定masterIP和端口
    val workerHost = args(0)
    val workerPort = args(1)
    val WorkerActorName = args(2)
    val masterHost = args(3)
    val masterPort = args(4)
    val MasterActorName = args(5)

    //  val (workerHost, workerPort, masterHost, masterPort) = ("127.0.0.1", 10002, "127.0.0.1", 10001)

    /**
      * 使用ConfigFactory parseString()方法解析字符串,指定客户端IP和端口
      */
    val config = ConfigFactory.parseString(
      s"""
         |akka.actor.provider="akka.remote.RemoteActorRefProvider"
         |akka.remote.netty.tcp.hostname=${workerHost}
         |akka.remote.netty.tcp.port=${workerPort}
        """.stripMargin)

    // 创建ActorSystem
    val worker = ActorSystem("worker", config)
    // 创建 workerFlowRef
    val workerFlowRef: ActorRef = worker.actorOf(Props(new WorkerFlow(masterHost, masterPort.toInt, MasterActorName)), s"${WorkerActorName}")
    // 启动workerFlowRef,指向自身服务端mailbox -> receive()方法
    workerFlowRef ! "WorkerFlowStart"
  }
}
```
- 运行顺序 : `1.启动1个MasterFlow` | `2.依次启动5个WorkerFlow` | `3.查看运行状态` | `4.依次停止WorkerFlow并查看MasterFlow心跳检测`

- `1.MasterFlow Log`
```
---- MasterFlow Start ----
开启定时检测Worker心跳任务
====== 存活Worker 0  ======
====== 存活Worker 0  ======
====== 存活Worker 0  ======
====== 存活Worker 1  ======
master更新Worker心跳 ID = 20bc4940-4f37-4271-9bda-8a9f0eeddc0c
master更新Worker心跳 ID = 20bc4940-4f37-4271-9bda-8a9f0eeddc0c
master更新Worker心跳 ID = 20bc4940-4f37-4271-9bda-8a9f0eeddc0c
====== 存活Worker 5  ======
master更新Worker心跳 ID = 20bc4940-4f37-4271-9bda-8a9f0eeddc0c
master更新Worker心跳 ID = 6e48fb10-7594-4947-b4cf-80b6828ba774
master更新Worker心跳 ID = a419c032-b89a-4804-8c39-5546f38280da
```
- `2.WorkerFlow Log`
```
---- WorkerFlow Start ----
WorkerFlow ID = 20bc4940-4f37-4271-9bda-8a9f0eeddc0c , Registration Success!
------- WorkerFlow = 20bc4940-4f37-4271-9bda-8a9f0eeddc0c 发送心跳 -------
------- WorkerFlow = 20bc4940-4f37-4271-9bda-8a9f0eeddc0c 发送心跳 -------
---- WorkerFlow Start ----
WorkerFlow ID = df2ca4fe-440f-4067-b77a-bcb146e3ba0c , Registration Success!
------- WorkerFlow = df2ca4fe-440f-4067-b77a-bcb146e3ba0c 发送心跳 -------
WorkerFlow ID = 6e48fb10-7594-4947-b4cf-80b6828ba774 , Registration Success!
------- WorkerFlow = 6e48fb10-7594-4947-b4cf-80b6828ba774 发送心跳 -------
------- WorkerFlow = 6e48fb10-7594-4947-b4cf-80b6828ba774 发送心跳 -------
```


#### 6.21.7 使用Scala方式 解决经典Wordcount实例
``` scala
package com.geekparkhub.core.scala.collection

object CollectionFlow032 {
  def main(args: Array[String]): Unit = {

    /**
      * val lines = List("hello hadoop", "hive scala spark flink storm scala flume")
      * 使用映射集合,list中各个单词出现的次数,并按出现次数排序
      */
    val lines = List("hello hadoop", "hive scala spark flink storm scala flume")

    /**
      * 分步骤编写
      *
      * 1. res001 = 单词扁平化 常规方式
      * 1. res01 = 单词扁平化 简写方式
      */
    val res001 = lines.flatMap((s: String) => s.split(" "))
    val res01 = lines.flatMap(_.split(" "))
    println("res01 = " + res01)

    /**
      * 2. res002 = 转换lits对偶 常规方式
      * 2. res02 = 转换lits对偶 简写方式
      */
    val res002 = res01.map((s: String) => (s, 1))
    val res02 = res01.map((_, 1))
    println("res02 = " + res02)

    /**
      * 3. res003 = 分组 常规方式
      * 3. res03 = 分组 简写方式
      */
    val res003 = res02.groupBy((x: (String, Int)) => x._1)
    val res03 = res02.groupBy(_._1)
    println("res03 = " + res03)

    /**
      * 4. res004 = 统计大小 常规方式
      * 4. res04 = 统计大小 简写方式
      */
    val res004 = res03.map((x: (String, List[(String, Int)])) => (x._1, x._2.size))
    val res04 = res03.map(x => (x._1, x._2.size))
    println("res04 = " + res04)

    /**
      * 5. res005 = 排序 常规方式
      * 5. res05 = 排序 简写方式
      * 5. res06 = 排序 简写方式 倒序排序
      */
    val res005 = res04.toList.sortBy((x: (String, Int)) => x._2)
    val res05 = res04.toList.sortBy(_._2)
    val res06 = res04.toList.sortBy(_._2).reverse
    println("res05 = " + res05)
    println("res06 = " + res06)

    /**
      * 将函数串联合并方式 计算结果
      */
    println("res07 = " + lines.flatMap(_.split(" ")).map((_, 1)).groupBy(_._1).map(x => (x._1, x._2.size)).toList.sortBy(_._2))

  }
}
```

### 6.22 泛型 & 上下界 & 视图界定 & 上下文界定 
#### 6.22.1 泛型基本介绍
> 如果要求函数的参数可以接受任意类型,可以使用泛型,这个类型可以代表任意的数据类型.
> 
> 例如List,在创建List 时,可以传入整型/字符串/浮点数等等任意类型,那是因为List在类定义时引用了泛型,比如在Java中:`public interface List<E> extends Collection<E>`

#### 6.22.2 Scala泛型实例 一
> 要求使用泛型来完成设计,编写Message类,不能使用Any
> 可以构建Int类型的Message,String类型的Message.
``` scala
package com.geekparkhub.core.scala.generic

object GenericFlow {
  def main(args: Array[String]): Unit = {
    val intMes = new IntMes(99)
    val stringMes = new StringMes("mes02")
    println("intMes = " + intMes)
    println("stringMes = " + stringMes)
  }
}

/**
  * 定义抽象类
  *
  * @param t
  * @tparam T
  */
abstract class Message[T](t: T) {
  def get: T = t
}

// 定义整型类
class IntMes[Int](n1: Int) extends Message(n1)

// 定义字符类型
class StringMes(str1: String) extends Message(str1)
```

#### 6.22.3 Scala泛型实例 二
> 定义一个函数,可以获取各种类型,List的中间index的值,使用泛型完成
``` scala
package com.geekparkhub.core.scala.generic

object GenericFlow02 {
  def main(args: Array[String]): Unit = {
    val list001 = List("q", "w", "e")
    val list002 = List(1, 3, 5)
    println("list001 = " + midList(list001))
    println("list002 = " + midList(list002))
  }

  def midList[E](l: List[E]): E = {
    l(l.length / 2)
  }
}
```

#### 6.22.4 类型约束
##### 6.22.4.1 上界 (Upper Bounds)
> 
> java中上界 : 
> 在Java泛型里表示某个类型是A类型的子类型则使用`extends`关键字,这种形式叫upper bounds(上限或上界),语法如下 : `<T extends A> 或用通配符形式：<? extends A>`
> 
> scala中上界 : 
> 在scala里表示某个类型是A类型的子类型,也称上界或上限,使用`<:`关键字,语法如下 : `[T <: A]  或用通配符: [_ <: A]`
> 
> 1.上界应用实例 一
> 编写通用的类,可以进行Int之间/Float之间等实现Comparable接口的值直接的比较.
> 分别使用传统方法和上界方式完成.
``` scala
package com.geekparkhub.core.scala.generic

object GenericFlow03 {
  def main(args: Array[String]): Unit = {
    val res01 = new CompareInt(50, 60)
    println("res01 = " + res01.maxs)

    // Integer类型
    val res02 = new CompareComm(Integer.valueOf(50), Integer.valueOf(60))
    println("res02 = " + res02.maxNum)

    // Float类型
    val res03 = new CompareComm(java.lang.Float.valueOf(50.5f), java.lang.Float.valueOf(60.7f))
    println("res03 = " + res03.maxNum)

    // 简写方式 内部使用隐式转换
    val res04 = new CompareComm[java.lang.Float](50.5f, 60.7f)
    println("res04 = " + res04.maxNum)
  }

  /**
    * 使用传统方式
    *
    * @param n1
    * @param n2
    */
  class CompareInt(n1: Int, n2: Int) {
    def maxs = if (n1 > n2) n1 else n2
  }

  /**
    * 使用上界方式
    */
  class CompareComm[T <: Comparable[T]](obj1: T, obj2: T) {
    def maxNum = if (obj1.compareTo(obj2) > 0) obj1 else obj2
  }

}
```

> 2.上界应用实例 二
> scala中上界 测试题(理解上界含义)
``` scala
package com.geekparkhub.core.scala.generic

object GenericFlow04 {
  def main(args: Array[String]): Unit = {
    biophony(Seq(new Bird, new Bird)) // 说出运行结果
    biophony(Seq(new Animal, new Animal)) // 说出运行结果
    biophony(Seq(new Animal, new Bird)) // 说出运行结果
    biophony(Seq(new Earth, new Earth)) // 说出运行结果
  }
  // 定义上界方法
  def biophony[T <: Animal](things: Seq[T]) = things map (_.sound)
}

/**
  * Earth 类
  */
class Earth {
  // 定义方法
  def sound() {
    println("hello !")
  }
}

class Animal extends Earth {
  // 重写了Earth sound()方法
  override def sound() = {
    println("animal sound")
  }
}

class Bird extends Animal {
  // 将Animal方法重写
  override def sound() = {
    print("bird sounds")
  }
}
```

##### 6.22.4.2 下界 (Lower Bounds)
> 1.Java中下界
> 在Java泛型里表示某个类型是A类型的父类型,使用`super`关键字.
> `<T super A> 或用通配符的形式 <? super A>`
> 
> 2.scala中下界
> 在scala的下界或下限,使用`>:`关键字,语法如下 : 
> `[T >: A] 或用通配符 [_ >: A]`
- scala中下界应用实例
``` scala
package com.geekparkhub.core.scala.generic

object GenericFlow05 {
  def main(args: Array[String]): Unit = {

    biophonys(Seq(new Earths, new Earths)).map(_.sound())
    biophonys(Seq(new Animals, new Animals)).map(_.sound())
    biophonys(Seq(new Birds ,new Birds)).map(_.sound())
    biophonys(Seq(new Moon))
  }

  // 定义下界方法
  def biophonys[T >: Animals](things: Seq[T]) = things
}

/**
  * Earth 类
  */
class Earths {
  // 定义方法
  def sound() {
    println("hello !")
  }
}

class Animals extends Earths {
  // 重写了Earth sound()方法
  override def sound() = {
    println("animal sound")
  }
}

class Birds extends Animals {
  // 将Animal方法重写
  override def sound() = {
    print("bird sounds")
  }
}

class Moon {}
```
> 3.scala中下界的使用总结
> 
> ```
> def biophony[T >: Animal](things: Seq[T]) = things
>```
>
> 1.对于下界,可以传入任意类型.
> 
> 2.如果传入的类是Animal直系并且是Animal父类,还是由父类处理.
> ```
> scala> biophonys(Seq(new Earths, new Earths))
> res6: Seq[Earths] = List(Earths@5e8507f1, Earths@4bcaa195)
> ```
> 3.如果传入的类是Animal子类,则按照Animal处理.
> ```
> scala> biophonys(Seq(new Birds ,new Birds))
> res4: Seq[Animals] = List(Birds@33db72bd, Birds@7f92b990)
> ```
> 4.传入的类与Animal无关一律按照Object处理.
> ```
> 
> scala> biophonys(Seq(new Moon))
> res5: Seq[Object] = List(Moon@3ee0b4f7)
> ```
> 5.下界传入的类可以随便传,只是处理是方式不一样.
> 
> 注意 : 不能使用上界的思路来类推下界的含义.
```
systemhub:~ system$ scala
scala> /**
     |   * Earth 类
     |   */
     | class Earths {
     |   // 定义方法
     |   def sound() {
     |     println("hello !")
     |   }
     | }
defined class Earths

scala> 

scala> class Animals extends Earths {
     |   // 重写了Earth sound()方法
     |   override def sound() = {
     |     println("animal sound")
     |   }
     | }
defined class Animals

scala> 

scala> class Birds extends Animals {
     |   // 将Animal方法重写
     |   override def sound() = {
     |     print("bird sounds")
     |   }
     | }
defined class Birds

scala> 

scala> class Moon {}
defined class Moon

scala> def biophonys[T >: Animals](things: Seq[T]) = things
biophonys: [T >: Animals](things: Seq[T])Seq[T]

scala> biophonys(Seq(new Birds ,new Birds))
res4: Seq[Animals] = List(Birds@33db72bd, Birds@7f92b990)

scala> biophonys(Seq(new Moon))
res5: Seq[Object] = List(Moon@3ee0b4f7)

scala> biophonys(Seq(new Earths, new Earths))
res6: Seq[Earths] = List(Earths@5e8507f1, Earths@4bcaa195)

scala> 
```

##### 6.22.4.3 视图界定 (View bounds)
> `<%`既表示视图界定,它比`<:`适用范围更广,除了支持所有子类型,还允许隐式转换类型.
> 
> `<%`除了方法使用之外,class声明类型参数时也可使用: `class A[T <% Int]`
> 
> ```
> def method [A <% B](arglist): R = ...
> 等价于
> def method [A](arglist)(implicit viewAB: A => B): R = ...
> 或等价于
> implicit def conver(a:A): B = …
> ```
- 1.视图界定实例 一
- 说明 : 使用视图界定会将类型隐式转换
``` scala
package com.geekparkhub.core.scala.generic

object GenericFlow06 {
  def main(args: Array[String]): Unit = {
    val res01 = new CompareComms(50, 60)
    val res02 = new CompareComms(50.5f, 60.7f)
    println("res01 = " + res01.max)
    println("res02 = " + res02.max)
  }
}

/**
  * 定义 视图界定 方法
  * 使用视图界定会将类型隐式转换
  * @param obj1
  * @param onj2
  * @tparam T
  */
class CompareComms[T <% Comparable[T]](obj1: T, onj2: T) {
  def max = if (obj1.compareTo(onj2) > 0) obj1 else onj2
}
```

- 2.视图界定实例 二
- 说明 : 使用视图界定方式,比较两个Persons对象年龄大小
``` scala
package com.geekparkhub.core.scala.generic

object GenericFlow07 {
  def main(args: Array[String]): Unit = {
    val mac = new Persons("mac", 18)
    val tom = new Persons("tom", 20)
    val res = new CompareCommt(mac, tom)
    println("res01 = " + res.maxl)
    println("res02 = " + res.maxi)
  }
}

/**
  * 定义Persons类并继承Ordered接口
  * 可以根据需求重写Ordered提供的方法
  * @param name
  * @param age
  */
class Persons(val name: String, val age: Int) extends Ordered[Persons] {
  // 复写compare方法
  override def compare(that: Persons): Int = this.age - that.age

  // 复写toString方法
  override def toString: String = "name: " + this.name + " , age: " + this.age
}

/**
  * 定义 视图界定 方法
  * Ordered 类似java Comparable接口
  * `T <% Ordered[T]` T表示传入的对象是Ordered子类型
  *
  * @param object1
  * @param object2
  * @tparam T
  */
class CompareCommt[T <% Ordered[T]](object1: T, object2: T) {
  // Ordered接口提供两种比较方法
  def maxl = if (object1 > object2) object1 else object2
  def maxi = if (object1.compareTo(object2) > 0) object1 else object2
}
```

- 3.视图界定实例 三
- 说明 : 编写隐式转换函数+视图界定方式,比较两个Persones对象年龄大小.
- 创建ImplicitFlow
``` scala
package com.geekparkhub.core.scala.generic

/**
  * 定义隐式函数
  */
object ImplicitFlow {
  /**
    * 定义 隐式conversions函数
    * 形参为Persones对象
    * 返回类型为Ordered
    * @param p
    * @return
    */
  implicit def conversions(p:Persones) = new Ordered[Persones] {
    // 复写compare方法
    override def compare(that: Persones): Int = {
      p.age - that.age
    }
  }
}
```
- 创建GenericFlow08
``` scala
package com.geekparkhub.core.scala.generic

object GenericFlow08 {
  def main(args: Array[String]): Unit = {
    val mac = new Persones("mac", 18)
    val tom = new Persones("tom", 30)
    // 引入隐式函数
    import ImplicitFlow._
    val res = new CompareCommts(mac,tom)
    println("res01 = " + res.maxl)
    println("res02 = " + res.maxi)
  }
}

/**
  * 定义Persones类
  * @param name
  * @param age
  */
class Persones(val name: String, val age: Int){
  // 复写toString方法
  override def toString: String = "name: " + this.name + " , age: " + this.age
}

/**
  * 定义 视图界定 方法
  * Ordered 类似java Comparable接口
  * `T <% Ordered[T]` T表示传入的对象是Ordered子类型
  * @param object1
  * @param object2
  * @tparam T
  */
class CompareCommts[T <% Ordered[T]](object1: T, object2: T) {
  // Ordered接口提供两种比较方法
  def maxl = if (object1 > object2) object1 else object2
  def maxi = if (object1.compareTo(object2) > 0) object1 else object2
}
```


##### 6.22.4.4 上下文界定 (Context bounds)
> 与view bounds一样 context bounds(上下文界定)也是隐式参数的语法糖.
> 为语法上的方便引入了”上下文界定”这个概念.
> 
> 上下文界定实例
> 使用上下文界定+隐式参数方式,比较两个Personse对象的年龄大小.
> 要求内部使用Ordering实现比较.
> 
> Ordered和Ordering区别
> 
> Ordering继承java中Comparator接口.
> 
> Ordered继承java Comparable接口,而在java中的Comparator是一个外部比较器(需要定义一个类来实现比较器),而Comparable则是一个内部比较器,在类内部重载compareTo函数.
- 创建ImplicitFlow02
``` scala
package com.geekparkhub.core.scala.generic

/**
  * 定义隐式值
  */
object ImplicitFlow02 {
  implicit val comparetor = new Ordering[Personse]{
    // 复写compare方法
    override def compare(x: Personse, y: Personse): Int = {
      x.age - y.age
    }
  }
}
```
- 创建GenericFlow09
``` scala
package com.geekparkhub.core.scala.generic

object GenericFlow09 {
  def main(args: Array[String]): Unit = {

    val mac = new Personse("mac", 18)
    val tom = new Personse("tom", 30)

    // 引入隐式值
    import ImplicitFlow02._

    // 方式一
    val res01 = new CompareComm01(mac, tom)
    println("res01 = " + res01.maxs)

    // 方式二
    val res02 = new CompareComm02(mac, tom)
    println("res02 = " + res02.maxs)

    // 方式三
    val res03 = new CompareComm03(mac,tom)
    println("res03 = " + res03.maxs)
  }
}

/**
  * 定义Personse类
  *
  * @param name
  * @param age
  */
class Personse(val name: String, val age: Int) {
  // 复写toString方法
  override def toString: String = "name: " + this.name + " , age: " + this.age
}

/**
  * 方式一 定义上下文界方法 实现比较大小
  * `obj01: T, obj02: T` 既表示接受T类型的对象
  * `(implicit comparetor: Ordering[T]) ` 既表示隐式参数
  *
  * @param obj01
  * @param obj02
  * @param `ordering$T`
  * @param comparetor
  * @tparam T
  */
class CompareComm01[T: Ordering](obj01: T, obj02: T)(implicit comparetor: Ordering[T]) {
  def maxs = if (comparetor.compare(obj01, obj02) > 0) obj01 else obj02
}

/**
  * 方式二 定义上下文界方法 实现比较大小
  * 将隐式参数嵌入到方法体内
  *
  * @param obj03
  * @param obj04
  * @tparam T
  */
class CompareComm02[T: Ordering](obj03: T, obj04: T) {
  def maxs = {
    def function01(implicit result01: Ordering[T]) = result01.compare(obj03, obj04)
    if (function01 > 0) obj03 else obj04
  }
}

/**
  * 方式三 定义上下文界方法 实现比较大小
  * 使用implicitly语法糖,最简单(推荐使用)
  * @param obj05
  * @param obj06
  * @tparam T
  */
class CompareComm03[T: Ordering](obj05: T, obj06: T) {
  def maxs = {
    val value: Ordering[T] = implicitly[Ordering[T]]
    println("hashCode = " + value.hashCode())
    if (value.compare(obj05, obj06) > 0) obj05 else obj06
  }
}
```

#### 6.22.5 协变 & 逆变 & 不变
> Scala中符号表示含义 : 
> 
> `+`既表示协变
> 
> `-`既表示逆变
> 
> `covariant`既表示协变
> 
> `contravariant`既表示逆变
> 
> `invariant`既表示不可变
> 
> 对于一个带类型参数的类型,比如List[T],如果对A及其子类型B,满足List[B]也符合List[A]的子类型,那么就称为covariance(协变).
> 
> 如果List[A]是List[B]的子类型,即与原来的父子关系正相反,则称为contravariance(逆变).
> 
> 如果一个类型支持协变或逆变,则称这个类型为variance(翻译为可变或变型),否则称为invariance(不可变).
> 
> 在Java中泛型类型都是(invariant)不可变,比如`List<String>`并不是`List<Object>`的子类型,而scala支持,可以在定义类型时声明(用加号表示为协变,减号表示逆变),如: `trait List[+T]` 在类型定义时声明为协变这样会把`List[String]`作为`List[Any]`的子类型.
- 举例说明
- 说明 : 在声明Scala泛型类型时,`+`表示协变,而`-`表示逆变. 
```
C[+T]：如果A是B的子类,那么C[A]是C[B]的子类,称为协变.
C[-T]：如果A是B的子类,那么C[B]是C[A]的子类,称为逆变.
C[T]：无论A和B是什么关系,C[A]和C[B]没有从属关系,称为不变.
```
- 应用实例
``` scala
 package com.geekparkhub.core.scala.generic

object GenericFlow010 extends App {
  val temp01: Temp01[Sub] = new Temp01[Sub]("temp01")
  val temp02: Temp02[Sub] = new Temp02[Sub]("temp02")
  val temp002: Temp02[Super] = new Temp02[Sub]("temp002")
  val temp003: Temp03[Sub] = new Temp03[Super]("temp003")
  println("temp01 = " + temp01 +"\n" + "temp02 = " + temp02 + "\n" + "temp002 = " + temp002 + "\n" + "temp003 = " + temp003)
}

/**
  * 定义 invariance(不变) Temp01类
  * `Temp01[A]` 既表示 invariance(不变)
  *
  * @param str
  * @tparam A
  */
class Temp01[A](str: String) {
  // 重写toString方法
  override def toString: String = str
}

/**
  * 定义 covariance(协变) Temp02类
  * `Temp02[+A]` 既表示 covariance(协变)
  *
  * @param str
  * @tparam A
  */
class Temp02[+A](str: String) {
  // 重写toString方法
  override def toString: String = str
}

/**
  * 定义 contravariance(逆变) Temp03类
  * `Temp03[-A]` 既表示 contravariance(逆变)
  *
  * @param str
  * @tparam A
  */
class Temp03[-A](str: String) {
  // 重写toString方法
  override def toString: String = str
}

/**
  * 定义 可协变 Super父类
  */
class Super

/**
  * 定义Sub子类继承Super父类
  */
class Sub extends Super
```



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