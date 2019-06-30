# 漫谈 Scala 设计模式 & 数据结构 & 算法

@(2019-05-20)[ Docs Language:简体中文 & English|Programing Scala Algorithm|Website:[www.geekparkhub.com](https://www.geekparkhub.com/)|![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg) | ![GitHub repo size in bytes](https://img.shields.io/github/repo-size/geekparkhub/geekparkhub.github.io.svg) | GeekDeveloper:[JEEP-711](https://github.com/jeep711)|Github:[github.com/geekparkhub](https://github.com/geekparkhub)|Gitee:[gitee.com/geekparkhub](https://gitee.com/geekparkhub) ]

##  🐘 Scala Algorithm 修仙之道 金精炼顶 🐘

![Alt text](https://raw.githubusercontent.com/geekparkhub/geekparkhub.github.io/master/technical_guide/assets/media/scala/algorithm.jpg)

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



## 1. 📖 设计模式 📖
### 1.1 🔖 学习设计模式 必要性 🔖
> 1.阅读源码,尤其是一些框架大量使用到设计模式,如果不学会设计模式的话,当然是看不懂源码为什么这样写,比如Runtime单例模式.
> 
> 2.设计模式能让专业人之间交流方便.
> 
> 3.提高代码易维护.
> 
> 4.设计模式即是通用编程应用场景模式化.


### 1.2 🔖 掌握设计模式 层次 🔖
> 第一层 :  刚步入学习编程不久,听说过设计模式.
> 
> 第二层 : 有很长时间的编程经验,也编写过很代码,其中用到了设计模式,但自身却不知道.
> 
> 第三层 : 学习过设计模式,发现自身已经在使用设计模式,并且发现一些好用的新设计模式.
> 
> 第四层 : 阅读很多开发者框架和源码,在其中看到使用设计模式,并且能够领会使用设计模式的精妙以及所带来的好处.
> 
> 第五层 : 代码写着写着,自身并没有没意识到使用了设计模式,但出神入化般写出了一手好代码.


### 1.3 🔖 设计模式 介绍 🔖
> 1.设计模式是开发者在面对同类软件工程设计问题所总结出来有用的经验,模式不是代码,既是设计思想,是某类问题通用解决方案,设计模式(Design pattern)代表了最佳实践,这些解决方案是众多软件开发人员经过相当长的一段时间试验和错误总结出来的.
> 
> 2.设计模式本质提高软件的维护性,通用性和扩展性,并降低软件的复杂度.
> 
> 3.设计模式书籍推荐 : 经典书籍<<设计模式>>,作者是Erich  Gamma、Richard  Helm、Ralph  Johnson 和John Vlissides Design (俗称 四人组GOF).
> 
> 4.设计模式并不局限于某种语言 java，php，c++ 都有设计模式

### 1.4 🔖 设计模式 类型 🔖
> 设计模式分为`三种`类型,`共23种`.
> 
> ⚠️ 注意 ⚠️ : 不同书籍对设计模式分类以及名称略有差异.
> 
> 1.`创建型模式` : 单例模式 / 抽象工厂模式 / 建造者模式 / 工厂模式 / 原型模式
> 
> 2.`结构型模式` : 适配器模式 / 桥接模式 / 装饰模式 / 组合模式 / 外观模式 / 享元模式 / 代理模式
> 
> 3.`行为型模式` : 模版方法模式 / 命令模式 / 迭代器模式 / 观察者模式 / 中介者模式 / 备忘录模式 / 解释器模式 (Interpreter模式) / 状态模式 / 策略模式 / 职责链模式(责任链模式) / 访问者模式


### 1.5 🏷️ 简单工厂 🏷️
#### 1.5.1 基本介绍
> 1.简单工厂模式是属于创建型模式,但不属于23种GOF设计模式之一,简单工厂模式是由一个工厂对象决定创建出哪一种产品类的实例,简单工厂模式是工厂模式家族中最简单实用的模式.
> 
> 2.简单工厂模式 : 定义了一个创建对象类,由这个类来封装实例化对象行为.
> 3.在软件开发中,当用到大量创建某种、某类或者某批对象时,就会使用到工厂模式.

#### 1.5.2 简单工厂 引入实例需求
> 披萨项目 : 要便于披萨种类的扩展,要便于维护,完成披萨订购功能.

##### 1.5.2.1 使用传统方式完成
- 1.创建Pizza
``` scala
package com.geekparkhub.core.scala.designpatterns.t001

abstract class Pizza {

  var name: String = _

  //假定每种pizza准备原材料不同,因此做为抽象函数
  def prepare() //抽象方法

  def cut(): Unit = {
    println(this.name + " cutting ..")
  }

  def bake(): Unit = {
    println(this.name + " baking ..")
  }

  def box(): Unit = {
    println(this.name + " boxing ..")
  }
}
```

- 2.创建DurianPizza
``` scala
package com.geekparkhub.core.scala.designpatterns.t001

/**
  * 榴莲披萨
  */
class DurianPizza extends Pizza {
  // 复写prepare方法
  override def prepare(): Unit = {
    this.name = "DurianPizza"
    println(this.name + " prepare")
  }
}
```

-3.创建GreenTeaMustardPizza
``` scala
package com.geekparkhub.core.scala.designpatterns.t001

/**
  * 绿茶芥末披萨
  */
class GreenTeaMustardPizza extends Pizza {

  // 复写prepare方法
  override def prepare(): Unit = {
    this.name = "GreenTeaMustardPizza"
    println(this.name + " prepare")
  }
}
```

-4.创建OtherPizza
``` scala
package com.geekparkhub.core.scala.designpatterns.t002

import com.geekparkhub.core.scala.designpatterns.t001.{DurianPizza, GreenTeaMustardPizza, Pizza}

import util.control.Breaks._
import scala.io.StdIn

/**
  * 其他披萨
  */
class OtherPizza {
  var orderType: String = _
  var pizza: Pizza = _
  breakable {
    do {
      println("<使用传统方式 构建披萨> - 请输入pizza类型")
      orderType = StdIn.readLine()
      if (orderType.equals("DurianPizza")) {
        // 构建DurianPizza
        this.pizza = new DurianPizza
      } else if (orderType.equals("GreenTeaMustardPizza")) {
        // 构建GreenTeaMustardPizza
        this.pizza = new GreenTeaMustardPizza
      } else {
        println("退出程序....")
        break()
      }
      this.pizza.prepare()
      this.pizza.bake()
      this.pizza.cut()
      this.pizza.box()
    } while (true)
  }
}

// 创建半生类
object OtherPizza {
  def main(args: Array[String]): Unit = {
    new OtherPizza
  }
}
```

-5.运行程序并查看结果
```
<使用简单工厂模式 构建披萨> - 请输入pizza类型
GreenTeaMustardPizza
GreenTeaMustardPizza prepare
GreenTeaMustardPizza baking ..
GreenTeaMustardPizza cutting ..
GreenTeaMustardPizza boxing ..
<使用简单工厂模式 构建披萨> - 请输入pizza类型
DurianPizza
DurianPizza prepare
DurianPizza baking ..
DurianPizza cutting ..
DurianPizza boxing ..
<使用简单工厂模式 构建披萨> - 请输入pizza类型
none
退出程序....
```

-6.使用传统方式优缺点
> 1.优点是比较好理解,简单易操作.
> 
> 2.缺点是违反了设计模式的ocp原则,即对扩展开放,对修改关闭,即当给类增加新功能时,尽量不修改代码,或者尽可能少修改代码.

-7.改进的思路分析
> 分析 : 修改代码可以接受,但是如果在其它的地方也有创建Pizza的代码,就意味着也需要修改,而创建Pizza的代码,往往有多处.
> 
> 思路 : 把创建Pizza对象封装到一个类中,这样有新的Pizza种类时,只需要修改该类即可,其它有创建到Pizza对象的代码就不需要修改.

##### 1.5.2.2 使用简单工厂模式
> 简单工厂模式设计方案 : 定义一个实例化Pizaa对象的类.封装创建对象的代码.

- 1.创建Pizza
``` scala
package com.geekparkhub.core.scala.designpatterns.t001

abstract class Pizza {

  var name: String = _

  //假定每种pizza准备原材料不同,因此做为抽象函数
  def prepare() //抽象方法

  def cut(): Unit = {
    println(this.name + " cutting ..")
  }

  def bake(): Unit = {
    println(this.name + " baking ..")
  }

  def box(): Unit = {
    println(this.name + " boxing ..")
  }
}
```

- 2.创建DurianPizza
``` scala
package com.geekparkhub.core.scala.designpatterns.t001

/**
  * 榴莲披萨
  */
class DurianPizza extends Pizza {
  // 复写prepare方法
  override def prepare(): Unit = {
    this.name = "DurianPizza"
    println(this.name + " prepare")
  }
}
```

- 3.创建GreenTeaMustardPizza
``` scala
package com.geekparkhub.core.scala.designpatterns.t001

/**
  * 绿茶芥末披萨
  */
class GreenTeaMustardPizza extends Pizza {

  // 复写prepare方法
  override def prepare(): Unit = {
    this.name = "GreenTeaMustardPizza"
    println(this.name + " prepare")
  }
}
```

- 4.创建MexicanPizza
``` scala
package com.geekparkhub.core.scala.designpatterns.t001

/**
  * 墨西哥披萨
  */
class MexicanPizza extends Pizza {
  // 复写prepare方法
  override def prepare(): Unit = {
    this.name = "MexicanPizza"
    println(this.name + "prepare")
  }
}
```

- 5.创建SimpleFactory
``` scala
package com.geekparkhub.core.scala.designpatterns.t002

import com.geekparkhub.core.scala.designpatterns.t001.{DurianPizza, GreenTeaMustardPizza, MexicanPizza, Pizza}

/**
  * 简单工厂
  */
object SimpleFactory {
  // 定义 创建披萨函数
  def createPizza(pame: String): Pizza = {
    var pizza: Pizza = null
    if (pame.equals("GreenTeaMustardPizza")) {
      // 如果相等则创建 GreenTeaMustardPizza
      pizza = new GreenTeaMustardPizza
    } else if (pame.equals("DurianPizza")) {
      // 如果相等则创建 DurianPizza
      pizza = new DurianPizza
    } else if (pame.equals("MexicanPizza")) {
      // 如果相等则创建 MexicanPizza
      pizza = new MexicanPizza
    }
    return pizza
  }
}
```

- 6.创建OtherPizza
``` scala
package com.geekparkhub.core.scala.designpatterns.t002

import com.geekparkhub.core.scala.designpatterns.t001.{DurianPizza, GreenTeaMustardPizza, Pizza}

import util.control.Breaks._
import scala.io.StdIn

/**
  * 其他披萨
  */
class OtherPizza {
  var orderType: String = _
  var pizza: Pizza = _
  breakable {
    do {
      println()
      println("<使用简单工厂模式 构建披萨> - 请输入pizza类型")
      orderType = StdIn.readLine()
      pizza = SimpleFactory.createPizza(orderType)
      if (pizza == null) {
        break()
      }
      this.pizza.prepare()
      this.pizza.bake()
      this.pizza.cut()
      this.pizza.box()
    } while (true)
  }
}

// 创建半生类
object OtherPizza {
  def main(args: Array[String]): Unit = {
    new OtherPizza
  }
}
```
-7.运行程序查看结果
```
<使用简单工厂模式 构建披萨> - 请输入pizza类型
DurianPizza
DurianPizza prepare
DurianPizza baking ..
DurianPizza cutting ..
DurianPizza boxing ..

<使用简单工厂模式 构建披萨> - 请输入pizza类型
MexicanPizza
MexicanPizzaprepare
MexicanPizza baking ..
MexicanPizza cutting ..
MexicanPizza boxing ..

<使用简单工厂模式 构建披萨> - 请输入pizza类型
GreenTeaMustardPizza
GreenTeaMustardPizza prepare
GreenTeaMustardPizza baking ..
GreenTeaMustardPizza cutting ..
GreenTeaMustardPizza boxing ..

<使用简单工厂模式 构建披萨> - 请输入pizza类型
none
```


#### 1.5.3 工厂方法模式
> 实例需求 : 披萨项目新的需求,客户在点披萨时,可以点不同口味的披萨,比如欧式奶酪pizza、欧式胡椒pizza或者是美式奶酪pizza、美式胡椒pizza.
> 
> 思路1 : 使用简单工厂模式,创建不同的简单工厂类,比如XXXPizzaSimpleFactory、XXXPizzaSimpleFactory等等.
> 
> 思路2 : 使用工厂方法模式

> 工厂方法模式介绍
> 
> 工厂方法模式设计方案 : 将披萨项目的实例化功能抽象成抽象方法,在不同口味披萨子类中具体实现.
> 
> 工厂方法模式 : 定义创建对象抽象方法,由子类决定要实例化的类,工厂方法模式将对象的实例化推迟到子类.
> 
> 工厂方法模式实例
- 1.创建抽象Pizza
``` scala
package com.geekparkhub.core.scala.designpatterns.d02.t001

abstract class Pizza {

  var name: String = _

  //假定每种pizza准备原材料不同,因此做为抽象函数
  def prepare() //抽象方法

  def cut(): Unit = {
    println(this.name + " cutting ..")
  }

  def bake(): Unit = {
    println(this.name + " baking ..")
  }

  def box(): Unit = {
    println(this.name + " boxing ..")
  }
}
```

- 2.创建AmericanCheesePizza
``` scala
package com.geekparkhub.core.scala.designpatterns.d02.t001

/**
  * 美式奶酪披萨
  */
class AmericanCheesePizza extends Pizza {
  // 复写prepare方法
  override def prepare(): Unit = {
    this.name = "AmericanCheesePizza"
    println(this.name + " prepare")
  }
}
```

- 3.创建AmericanPepperPizza
``` scala
package com.geekparkhub.core.scala.designpatterns.d02.t001

/**
  * 美式胡椒披萨
  */
class AmericanPepperPizza extends Pizza {
  // 复写prepare方法
  override def prepare(): Unit = {
    this.name = "AmericanPepperPizza"
    println(this.name + " prepare")
  }
}
```

- 4.创建OtherPizza
``` scala
package com.geekparkhub.core.scala.designpatterns.d02.t002

import com.geekparkhub.core.scala.designpatterns.d02.t001
import com.geekparkhub.core.scala.designpatterns.d02.t001.Pizza

import scala.io.StdIn
import scala.util.control.Breaks._

/**
  * 其他披萨 抽象类
  */
abstract class OtherPizza {
  var orderType: String = null
  var pizza: t001.Pizza = null
  breakable {
    do {
      println()
      println("<使用工厂方法模式 构建披萨> - 请输入pizza类型")
      orderType = StdIn.readLine()
      pizza = createPizza(orderType)
      if (pizza == null) {
        break()
      }
      this.pizza.prepare()
      this.pizza.bake()
      this.pizza.cut()
      this.pizza.box()
    } while (true)
  }

  // 定义抽象方法,让子类实现创建披萨的抽象方法
  def createPizza(pame: String): Pizza
}

// 半生对象
object PizzaFlow {
  def main(args: Array[String]): Unit = {
    new AmericanOtherPizza
  }
}
```

- 5.创建AmericanOtherPizza
``` scala
package com.geekparkhub.core.scala.designpatterns.d02.t002

import com.geekparkhub.core.scala.designpatterns.d02.t001.{AmericanCheesePizza, AmericanPepperPizza, Pizza}

/**
  * 美式披萨实现类
  */
class AmericanOtherPizza extends OtherPizza {
  // 子类具体实现OtherPizza方法
  override def createPizza(pame: String): Pizza = {
    var pizza: Pizza = null
    if (pame.equals("AmericanCheesePizza")) {
      // 如果相等则创建AmericanCheesePizza
      pizza = new AmericanCheesePizza
    } else if (pame.equals("AmericanPepperPizza")) {
      // 如果相等则创建AmericanPepperPizza
      pizza = new AmericanPepperPizza
    }
    return pizza
  }
}
```

- 6.运行程序查看结果
```
<使用简单工厂模式 构建披萨> - 请输入pizza类型
AmericanPepperPizza
AmericanPepperPizza prepare
AmericanPepperPizza baking ..
AmericanPepperPizza cutting ..
AmericanPepperPizza boxing ..

<使用简单工厂模式 构建披萨> - 请输入pizza类型
AmericanCheesePizza
AmericanCheesePizza prepare
AmericanCheesePizza baking ..
AmericanCheesePizza cutting ..
AmericanCheesePizza boxing ..

<使用简单工厂模式 构建披萨> - 请输入pizza类型
none
```

#### 1.5.4 抽象工厂模式
> 1.抽象工厂模式 : 定义了一个trait用于创建相关或有依赖关系对象簇,而无需指明具体的类.
> 
> 2.抽象工厂模式可以将简单工厂模式和工厂方法模式进行整合.
> 
> 3.从设计层面看,抽象工厂模式就是对简单工厂模式改进(或者称为进一步的抽象).
> 
> 4.将工厂抽象成两层,AbsFactory(抽象工厂)和具体实现的工厂子类,可以根据创建对象类型使用对应的工厂子类,这样将单个简单工厂类变成了工厂簇,更利于代码维护和扩展.
> 
> 5.抽象工厂模式实例
- 1.创建Pizza
``` scala
package com.geekparkhub.core.scala.designpatterns.d03.t001

abstract class Pizza {

  var name: String = _

  //假定每种pizza准备原材料不同,因此做为抽象函数
  def prepare() //抽象方法

  def cut(): Unit = {
    println(this.name + " cutting ..")
  }

  def bake(): Unit = {
    println(this.name + " baking ..")
  }

  def box(): Unit = {
    println(this.name + " boxing ..")
  }
}
```

- 2.创建AmericanCheesePizza
``` scala
package com.geekparkhub.core.scala.designpatterns.d03.t001

/**
  * 美式奶酪披萨
  */
class AmericanCheesePizza extends Pizza {
  // 复写prepare方法
  override def prepare(): Unit = {
    this.name = "AmericanCheesePizza"
    println(this.name + " prepare")
  }
}
```

- 3.创建AmericanPepperPizza
``` scala
package com.geekparkhub.core.scala.designpatterns.d03.t001

/**
  * 美式胡椒披萨
  */
class AmericanPepperPizza extends Pizza {
  // 复写prepare方法
  override def prepare(): Unit = {
    this.name = "AmericanPepperPizza"
    println(this.name + " prepare")
  }
}
```

- 4.创建AbsFactory
``` scala
package com.geekparkhub.core.scala.designpatterns.d03.t002

import com.geekparkhub.core.scala.designpatterns.d03.t001.Pizza

/**
  * 抽象工厂
  */
trait AbsFactory {
  // 定义创建披萨 抽象方法
  def createPizza(names: String): Pizza
}
```

- 5.创建AmericanFactory
``` scala
package com.geekparkhub.core.scala.designpatterns.d03.t002

import com.geekparkhub.core.scala.designpatterns.d03.t001.{AmericanCheesePizza, AmericanPepperPizza, Pizza}

/**
  * 美式披萨子工厂 实现类
  */
class AmericanFactory extends AbsFactory {
  override def createPizza(names: String): Pizza = {
    var pizza: Pizza = null
    if (names.equals("AmericanCheesePizza")) {
      pizza = new AmericanCheesePizza
    } else if (names.equals("AmericanPepperPizza")) {
      pizza = new AmericanPepperPizza
    }
    return pizza
  }
}
```

- 6.创建OtherPizza
``` scala
package com.geekparkhub.core.scala.designpatterns.d03.t002

import com.geekparkhub.core.scala.designpatterns.d03.t001.Pizza

import scala.io.StdIn
import scala.util.control.Breaks._

/**
  * 其他披萨 抽象类
  */
class OtherPizza {
  var orderType: String = null
  var pizza: Pizza = null
  var absFactory: AbsFactory = _

  def this(absFactory: AbsFactory) {
    this
    breakable {
      do {
        println()
        println("<使用抽象工厂模式 构建披萨> - 请输入pizza类型")
        orderType = StdIn.readLine()
        pizza = absFactory.createPizza(orderType)
        if (pizza == null) {
          break()
        }
        this.pizza.prepare()
        this.pizza.bake()
        this.pizza.cut()
        this.pizza.box()
      } while (true)
    }
  }
}

// 半生对象
object PizzaFlow {
  def main(args: Array[String]): Unit = {
    new OtherPizza(new AmericanFactory)
  }
}
```

-7.运行程序查看结果
```
<使用抽象工厂模式 构建披萨> - 请输入pizza类型
AmericanPepperPizza
AmericanPepperPizza prepare
AmericanPepperPizza baking ..
AmericanPepperPizza cutting ..
AmericanPepperPizza boxing ..

<使用抽象工厂模式 构建披萨> - 请输入pizza类型
AmericanCheesePizza
AmericanCheesePizza prepare
AmericanCheesePizza baking ..
AmericanCheesePizza cutting ..
AmericanCheesePizza boxing ..

<使用抽象工厂模式 构建披萨> - 请输入pizza类型
none
```
- 8.工厂模式总总结
- 1.工厂模式的意义将实例化对象的代码提取出来,放到一个类中统一管理和维护,达到和主项目的依赖关系解耦,从而提高项目的扩展和维护性.
- 2.三种工厂模式,设计模式的依赖抽象原则.
- 3.创建对象实例时,不要直接new类,而是把new类的动作放在一个工厂的方法中并返回,变量不要直接持有具体类的引用.
- 4.不要让类继承具体类,而是继承抽象类或者是trait接口.
- 5.不要覆盖基类中已经实现的方法.


### 1.6 🏷️ 单例模式 🏷️
> 1.单例模式是指 : 保证在整个软件系统中,某个类只能存在一个对象实例.
> 
> 2.单例模式的应用场景
> 
> 比如Hibernate的SessionFactory,它充当数据存储源的代理,并负责创建Session对象,SessionFactory并不是轻量级,一般情况下一个项目通常只需要一个SessionFactory就够,这是使用到单例模式应用场景.
> 
> 3.单例模式实例
> Scala中没有静态的概念,所以为了实现Java中单例模式的功能,可以直接采用类对象(即伴生对象)方式构建单例对象.
- 1.创建单例模式 - 懒汉式
``` scala
package com.geekparkhub.core.scala.designpatterns.d04

/**
  * 单例模式 - 懒汉式
  */
object SingleTonFlow {
  def main(args: Array[String]): Unit = {
    val insance01: SingleTon = SingleTon.getInsance
    val insance02: SingleTon = SingleTon.getInsance

    if (insance01 == insance02) {
      println("value equal")
    }
  }
}

// SingleTon 构造方法私有化
class SingleTon private() {}

// 懒汉式
object SingleTon {
  private var s: SingleTon = null

  def getInsance = {
    if (s == null) {
      s = new SingleTon
    }
    s
  }
}
```

- 2.创建单例模式 - 饿汉模式
``` scala
package com.geekparkhub.core.scala.designpatterns.d04

/**
  * 单例模式 - 饿汉式
  */
object SingleTonFlows {
  def main(args: Array[String]): Unit = {
    val insance01: SingleTons = SingleTons.getInsance
    val insance02: SingleTons = SingleTons.getInsance
    if (insance01 == insance02) {
      println("value equal")
    }
  }
}

// SingleTons 构造方法私有化
class SingleTons private() {}

// 饿汉式
object SingleTons {
  private val s: SingleTons = new SingleTons
  def getInsance = {
    s
  }
}
```

### 1.7 🏷️ 装饰者模式 🏷️
> 1.实例需求 : 
> 咖啡馆订单系统项目
> 咖啡种类 - 单品咖啡 : 意大利浓咖啡、暗黑系咖啡、美式咖啡、无糖咖啡
> 调味品 : 牛奶 / 冰糖 / 巧克力 / 砂糖
> 要求在扩展新品咖啡种类时,具有良好扩展性、修改方便、维护方便.
> 使用面向对象来计算不同种类咖啡费用,可以选单品咖啡,也可以单品咖啡+调味品组合.
> 
> 2.装饰者模式原理
> 装饰者模式就像打包快递,装饰者模式分为主体和包装.
> (Component 主体)比如 : 陶瓷/衣服 , (Decorator 包装)比如 : 报纸填充/塑料泡沫/纸板.
> 
> 3.装饰者模式定义
> 装饰者模式 : 动态的将新功能附加到对象上,在对象功能扩展方面,它比继承更有弹性,装饰者模式也体现了开闭原则(OCP).
> 
> 4.装饰者模式咖啡订单实例
- 1.创建Drink
``` scala
package com.geekparkhub.core.scala.designpatterns.d05.t01

/**
  * 饮品 抽象类
  */
abstract class Drink {
  // 饮品描述
  var description = ""
  // 饮品价格
  private var price = 0.0f

  // 定义价格计算 抽象方法
  def cost(): Float

  def setDescription(description: String): Unit = {
    this.description = description
  }

  def getDescription(): String = {
    description + " 价格: " + this.getPrice()
  }

  def getPrice(): Float = {
    price
  }

  def setPrice(price: Float): Unit = {
    this.price = price
  }
}
```

- 2.创建Coffee
``` scala
package com.geekparkhub.core.scala.designpatterns.d05.t02

import com.geekparkhub.core.scala.designpatterns.d05.t01.Drink

/**
  * 饮品 咖啡缓冲扩展类
  */
class Coffee extends Drink {
  override def cost(): Float = {
    super.getPrice()
  }
}
```

- 3.创建ItalianEspresso
``` scala
package com.geekparkhub.core.scala.designpatterns.d05.t02

/**
  * 意大利浓咖啡
  */
class ItalianEspresso extends Coffee {
  // 设置咖啡描述
  super.setDescription("<ItalianEspresso | 意大利浓咖啡>")
  // 设置咖啡价格
  super.setPrice(50.2f)
}
```

- 4.创建DarkCoffee
``` scala
package com.geekparkhub.core.scala.designpatterns.d05.t02

/**
  * 暗黑系咖啡
  */
class DarkCoffee extends Coffee {
  // 设置咖啡描述
  super.setDescription("<Dark Coffee | 暗黑系咖啡>")
  // 设置咖啡价格
  super.setPrice(110.6f)
}
```

- 5.创建AmericanCoffee
``` scala
package com.geekparkhub.core.scala.designpatterns.d05.t02

/**
  * 美式咖啡
  */
class AmericanCoffee extends Coffee {
  // 设置咖啡描述
  super.setDescription("<American Coffee | 美式咖啡>")
  // 设置咖啡价格
  super.setPrice(45.6f)
}
```

- 6.创建SugarFreeCoffee
``` scala
package com.geekparkhub.core.scala.designpatterns.d05.t02

/**
  * 无糖咖啡
  */
class SugarFreeCoffee extends Coffee {
  // 设置咖啡描述
  super.setDescription("<SugarFreeCoffee | 无糖咖啡>")
  // 设置咖啡价格
  super.setPrice(32.2f)
}
```

- 7.创建Decorator
``` scala
package com.geekparkhub.core.scala.designpatterns.d05.t03

import com.geekparkhub.core.scala.designpatterns.d05.t01.Drink

/**
  * Decorator 装饰者
  */
class Decorator extends Drink {

  // obj既是被装饰的Drink对象
  var obj: Drink = null

  // 定义obj辅助构造器
  def this(obj: Drink) {
    this
    this.obj = obj
  }

  // 定义价格方法 使用递归方式计算价格总数
  override def cost(): Float = {
    super.getPrice() + obj.cost()
  }

  // 定义商品描述 使用递归方式获取尚商品信息
  override def getDescription(): String = {
    super.getDescription() + " && " + obj.getDescription()
  }
}
```

- 8.创建Milk
``` scala
package com.geekparkhub.core.scala.designpatterns.d05.t03

import com.geekparkhub.core.scala.designpatterns.d05.t01.Drink

/**
  * 调味品 : 牛奶
  * 主构造器 参数 : Drink
  */
class Milk(obj: Drink) extends Decorator(obj) {
  // 设置调味品描述
  setDescription("<Milk | 牛奶>")
  // 设置调味品价格
  setPrice(5.6f)
}
```

- 9.创建Chocolate
``` scala
package com.geekparkhub.core.scala.designpatterns.d05.t03

import com.geekparkhub.core.scala.designpatterns.d05.t01.Drink

/**
  * 调味品 : 巧克力
  * 主构造器 参数 : Drink
  */
class Chocolate(obj:Drink) extends Decorator(obj){
  // 设置调味品描述
  setDescription("<Chocolate | 巧克力>")
  // 设置调味品价格
  setPrice(15.6f)
}
```

- 10.创建GranulatedSugar
``` scala
package com.geekparkhub.core.scala.designpatterns.d05.t03

import com.geekparkhub.core.scala.designpatterns.d05.t01.Drink

/**
  * 调味品 : 砂糖
  * 主构造器 参数 : Drink
  */
class GranulatedSugar(obj:Drink) extends Decorator(obj) {
  // 设置调味品描述
  setDescription("<GranulatedSugar | 砂糖>")
  // 设置调味品价格
  setPrice(3.5f)
}
```

- 11.创建CrystalSugar
``` scala
package com.geekparkhub.core.scala.designpatterns.d05.t03

import com.geekparkhub.core.scala.designpatterns.d05.t01.Drink

/**
  * 调味品 : 冰糖
  */
class CrystalSugar(obj:Drink) extends Decorator(obj){
  // 设置调味品描述
  setDescription("<CrystalSugar | 冰糖>")
  // 设置调味品价格
  setPrice(4.5f)
}
```

- 12.创建CoffeeRunFlow
``` scala
package com.geekparkhub.core.scala.designpatterns.d05

import com.geekparkhub.core.scala.designpatterns.d05.t01.Drink
import com.geekparkhub.core.scala.designpatterns.d05.t02.{AmericanCoffee, DarkCoffee}
import com.geekparkhub.core.scala.designpatterns.d05.t03.{Chocolate, Milk}

/**
  * Coffee Shop 主程序入口
  */
object CoffeeRunFlow {
  def main(args: Array[String]): Unit = {
    println("++++++++++++++++++++++++++++++++++ Coffee Shop ++++++++++++++++++++++++++++++++++")

    // 单选一杯美式咖啡
    var americanCoffee: Drink = new AmericanCoffee
    val CoffeeDescription01: String = americanCoffee.getDescription()
    val CoffeeCost01: Float = americanCoffee.cost()
    // 输出描述并计算价格
    println("CoffeeDescription01 = " + CoffeeDescription01 + " | CoffeeCost01 = " + CoffeeCost01)
    println()
    println("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    // 选购一杯暗黑系咖啡+1份牛奶+2块巧克力
    var darkCoffee: Drink = new DarkCoffee
    // 1份牛奶
    darkCoffee = new Milk(darkCoffee)
    // 2块巧克力
    darkCoffee = new Chocolate(darkCoffee)
    darkCoffee = new Chocolate(darkCoffee)
    // 输出描述并计算价格
    println("CoffeeDescription02 = " + darkCoffee.getDescription() + " | CoffeeCost02 = " + darkCoffee.cost())
  }
}
```
- 13.运行程序并查看结果
```
++++++++++++++++++++++++++++++++++ Coffee Shop ++++++++++++++++++++++++++++++++++
CoffeeDescription01 = <American Coffee | 美式咖啡> 价格: 45.6 | CoffeeCost01 = 45.6

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
CoffeeDescription02 = <Chocolate | 巧克力> 价格: 15.6 && <Chocolate | 巧克力> 价格: 15.6 && <Milk | 牛奶> 价格: 5.6 && <Dark Coffee | 暗黑系咖啡> 价格: 110.6 | CoffeeCost02 = 147.40001
```

### 1.8 🏷️ 观察者模式 🏷️
> 1.实例需求 : 气象站
> 气象站可以将每天测量到温度/湿度/气压等等以公告的形式发布.
> 需要设计开放型API,便于其他第三方接入气象站获取数据.
> 提供温度/气压/湿度接口.
> 测量数据更新时,要能实时通知第三方.
> 
> 2.观察者模式原理
> 观察者模式类似订牛奶业务
> 牛奶站 = 气象局：Subject
> 用户 = 第三方网站：Observer
> 
> Subject具有注册/移除/通知等功能.
> registerObserver 注册
> removeObserver 移除
> notifyObservers() 通知所有注册用户
> 
> 观察者模式 : 对象之间多对一依赖的一种设计方案,被依赖对象为Subject,依赖对象为Observer,Subject通知Observer变化,比如气象站是Subject,第三方是Observer就形成了多对一.
> 
> 3.观察者模式实例
- 1.创建Subject
``` scala
package com.geekparkhub.core.scala.designpatterns.d06.t01

/**
  * 气象 接口
  */
trait Subject {

  // 定义注册 抽象方法
  def registerObserver(o: ObServer)

  // 定义移除 抽象方法
  def removeObserver(o: ObServer)

  // 定义通知 抽象方法
  def notifyObservers()
}
```

- 2.创建ObServer
``` scala
package com.geekparkhub.core.scala.designpatterns.d06.t01

/**
  * 第三方 接口
  */
trait ObServer {
  // 定义更新数据 抽象方法
  def update(mTemperatrue: Float, mPressure: Float, mHumidity: Float)
}
```

- 3.创建WeatherData
``` scala
package com.geekparkhub.core.scala.designpatterns.d06.t01

import scala.collection.mutable.ListBuffer

/**
  * 定义 天气数据
  */
class WeatherData extends Subject {

  // 定义温度属性
  private var mTemperature: Float = _
  // 定义气压属性
  private var mPressure: Float = _
  // 定义湿度属性
  private var mHumidity: Float = _

  // 定义集合,用于管理所有观察者
  private var mObservers: ListBuffer[ObServer] = ListBuffer()

  // 定义 获取温度方法
  def getTemperature() = {
    mTemperature
  }

  // 定义 获取气压方法
  def getPressure() = {
    mPressure
  }

  // 定义 获取湿度方法
  def getHumidity() = {
    mHumidity
  }

  // 设置天气变化属性
  def setData(mTemperature: Float, mPressure: Float, mHumidity: Float) = {
    this.mTemperature = mTemperature
    this.mPressure = mPressure
    this.mHumidity = mHumidity
    dataChange()
  }

  // 定义数据等新方法
  def dataChange() = {
    //当天气变化时通知所有观察者
    notifyObservers()
  }

  // 复写注册方法
  override def registerObserver(o: ObServer): Unit = {
    mObservers.append(o)
  }

  // 复写移除方法
  override def removeObserver(o: ObServer): Unit = {
    if (mObservers.contains(o)){
      mObservers -= o
    }
  }

  // 复写通知方法
  override def notifyObservers(): Unit = {
    for (m <- mObservers){
      m.update(mTemperature,mPressure,mHumidity)
    }
  }

}
```

- 4.创建CurrentConditions
``` scala
package com.geekparkhub.core.scala.designpatterns.d06.t02

import com.geekparkhub.core.scala.designpatterns.d06.t01.ObServer

/**
  * 定义气象台 观察者
  */
class CurrentConditions extends ObServer{

  // 定义温度属性
  private var mTemperature: Float = _
  // 定义气压属性
  private var mPressure: Float = _
  // 定义湿度属性
  private var mHumidity: Float = _

  // 定义数据展示方法
  def display() = {
    println()
    println("*** Today mTemperature: " + mTemperature + " ***")
    println("*** Today mPressure: " + mPressure + " ***")
    println("*** Today mHumidity: " + mHumidity + " ***")
    println()
  }

  // 复写数据更新方法
  override def update(mTemperatrue: Float, mPressure: Float, mHumidity: Float): Unit = {
    // 更新气象数据
    this.mTemperature = mTemperatrue
    this.mPressure = mPressure
    this.mHumidity = mHumidity
    // 调用数据展示方法
    display()
  }

}
```

- 5.ThirdParty
``` scala
package com.geekparkhub.core.scala.designpatterns.d06.t02

import com.geekparkhub.core.scala.designpatterns.d06.t01.ObServer

/**
  * 定义 第三方 观察者
  */
class ThirdParty extends ObServer {
  // 定义温度属性
  private var mTemperature: Float = _
  // 定义气压属性
  private var mPressure: Float = _
  // 定义湿度属性
  private var mHumidity: Float = _

  // 定义数据展示方法
  def display() = {
    println()
    println("*** ThirdParty Today mTemperature: " + mTemperature + " ***")
    println("*** ThirdParty Today mPressure: " + mPressure + " ***")
    println("*** ThirdParty Today mHumidity: " + mHumidity + " ***")
    println()
  }

  // 复写数据更新方法
  override def update(mTemperatrue: Float, mPressure: Float, mHumidity: Float): Unit = {
    // 更新气象数据
    this.mTemperature = mTemperatrue
    this.mPressure = mPressure
    this.mHumidity = mHumidity
    // 调用数据展示方法
    display()
  }
}
```

- 6.创建WeatherDataRunFlow
``` scala
package com.geekparkhub.core.scala.designpatterns.d06.t01

import com.geekparkhub.core.scala.designpatterns.d06.t02.{CurrentConditions, ThirdParty}

object WeatherDataRunFlow {
  def main(args: Array[String]): Unit = {

    // 创建 天气数据实例
    val weatherData = new WeatherData

    // 创建气象台实例
    val currentConditions = new CurrentConditions
    val thirdParty = new ThirdParty

    // 注册
    weatherData.registerObserver(currentConditions)
    weatherData.registerObserver(thirdParty)

    // 更新数据
    weatherData.setData(30, 160, 35)
  }
}
```


-7. 运行程序查看结果
```
*** Today mTemperature: 30.0 ***
*** Today mPressure: 160.0 ***
*** Today mHumidity: 35.0 ***


*** ThirdParty Today mTemperature: 30.0 ***
*** ThirdParty Today mPressure: 160.0 ***
*** ThirdParty Today mHumidity: 35.0 ***
```
- 8.Java内置观察者模式
- `java.util.Observable`
- 1.Observable作用和地位等价于Subject
- 2.Observable是类,并不是接口,其已实现核心 注册/移除/通知方法
- 3.Observable和Observer使用方法和Scala观察者模式实例基本一样,只是Observable是类,通过继承来实现观察者模式.


### 1.9 🏷️ 代理模式 🏷️
> 代理模式 : 为一个对象提供一个替身,以控制对这个对象的访问.
> 
> 被代理的对象可以是远程对象、创建开销大的对象或需要安全控制的对象.
> 
> 代理模式有不同形式(比如远程代理/静态代理/动态代理)都是为了控制与管理对象访问.

#### 1.9.1 本地监控实例
> 对本地机器状态和销售情况进行监控
- 1.创建State
``` scala
package com.geekparkhub.core.scala.designpatterns.d07

/**
  * 定义 机器状态 接口
  */
trait State extends Serializable {
  def insertCoin() //插入硬币
  def returnCoin() //返回硬币
  def turnCrank() // 转动曲柄
  def printstate() // 输出状态
  def getstatename(): String //返回状态名字
  def dispense() //分配状态,如卖出一块糖后,查看当前机器应进入哪个状态
}
```

- 2.创建CandyMachine
``` scala
package com.geekparkhub.core.scala.designpatterns.d07

/**
  * 糖果机状态
  */
class CandyMachine {

  var mSoldOutState: State = _
  var mOnReadyState: State = _
  var mHasCoin: State = _
  var mSoldState: State = _
  var mWinnerState: State = _
  private var location = ""
  private var state: State = _
  private var count = 0

  def this(location: String, count: Int) {
    this
    this.location = location
    this.count = count
    mSoldOutState = new SoldOutState(this);
    mOnReadyState = new OnReadyState(this);
    mHasCoin = new HasCoin(this);
    mSoldState = new SoldState(this);
    mWinnerState = new WinnerState(this);
    if (count > 0) {
      state = mOnReadyState;
    } else {
      state = mSoldOutState;
    }
  }

  //给糖果机设置状态
  def setState(state: State) = {
    this.state = state
  }

  def getLocation(): String = {
    location
  }
  
  def insertCoin() = {
    state.insertCoin()
  }

  def returnCoin() = {
    state.returnCoin()
  }

  def turnCrank() = {
    state.turnCrank()
    state.dispense()
  }

  def releaseCandy() = {
    if (count > 0) {
      count = count - 1
      println("a candy rolling out!");
    }
  }

  def getCount(): Int = {
    count
  }

  def printstate() = {
    state.printstate()
  }

  def getstate(): State = {
    state
  }
}
```

- 3.创建HasCoin
``` scala
package com.geekparkhub.core.scala.designpatterns.d07

/**
  * 用户投币状态
  */
class HasCoin extends State {
  //说明:@transient注解将字段标记为瞬态的,即表示一个域不是该对象串行化的一部分
  @transient private var mCandyMachine: CandyMachine = _

  //观察的是这个 mCandyMachine糖果机
  def this(mCandyMachine: CandyMachine) {
    this
    this.mCandyMachine = mCandyMachine
  }

  override def getstatename(): String = {
    "HasCoin State"
  }

  //根据当前状态，insertCoin有不同的业务逻辑
  override def insertCoin(): Unit = {
    println("you can't insert another coin!")
  }

  override def printstate(): Unit = {
    println("***HasCoin***")
  }

  override def returnCoin(): Unit = {
    println("coin return!")
    //如果在有Coin的状态下，执行了returnCoin,那么糖果机又进入到redayState
    mCandyMachine.setState(mCandyMachine.mOnReadyState);
  }

  //转动手柄
  override def turnCrank(): Unit = {
    println("crank turn...!");
    val ranwinner = new java.util.Random()
    //设置一个抽奖随机数,如果返回一个0,就再奖励一块糖
    var winner = ranwinner.nextInt(10)
    if (winner == 0) {
      mCandyMachine.setState(mCandyMachine.mWinnerState)

    } else {
      mCandyMachine.setState(mCandyMachine.mSoldState)
    }
  }
  //没有逻辑
  override def dispense(): Unit = {}
}
```

- 4.创建WinnerState 
``` scala
package com.geekparkhub.core.scala.designpatterns.d07

class WinnerState extends State {
  //说明:@transient注解将字段标记为瞬态的,即表示一个域不是该对象串行化的一部分
  @transient private var mCandyMachine: CandyMachine = _

  def this(mCandyMachine: CandyMachine) {
    this
    this.mCandyMachine = mCandyMachine
  }

  override def getstatename(): String = {
    "WinnerState"
  }

  //根据当前状态，我们的insertCoin有不同的业务逻辑
  override def insertCoin(): Unit = {
    println("please wait!we are giving you a candy!")
  }

  override def printstate(): Unit = {
    println("***WinnerState***")
  }

  override def returnCoin(): Unit = {
    println("you haven't inserted a coin yet!")

  }

  override def turnCrank(): Unit = {
    println("we are giving you a candy,turning another get nothing,!");

  }

  override def dispense(): Unit = {
    mCandyMachine.releaseCandy()
    if (mCandyMachine.getCount() == 0) {
      mCandyMachine.setState(mCandyMachine.mSoldOutState);
    } else {
      println("you are a winner!you get another candy!")
      mCandyMachine.releaseCandy()
      if (mCandyMachine.getCount() > 0) {
        mCandyMachine.setState(mCandyMachine.mOnReadyState);
      } else {
        println("Oo,out of candies");
        mCandyMachine.setState(mCandyMachine.mSoldOutState);
      }
    }
  }
}
```

- 5.创建SoldState 
``` scala
package com.geekparkhub.core.scala.designpatterns.d07

/**
  * 处于销售状态[正在出商品...]
  */
class SoldState extends State {
  //说明:@transient注解将字段标记为瞬态的,即表示一个域不是该对象串行化的一部分
  @transient private var mCandyMachine: CandyMachine = _

  def this(mCandyMachine: CandyMachine) {
    this
    this.mCandyMachine = mCandyMachine
  }

  override def getstatename(): String = {
    "SoldState"
  }

  //根据当前状态，我们的insertCoin有不同的业务逻辑
  //其它的方法同样存在这样的处理
  override def insertCoin(): Unit = {
    println("please wait!we are giving you a candy!")
  }

  override def printstate(): Unit = {
    println("******SoldState******")
  }

  override def returnCoin(): Unit = {
    println("you haven't inserted a coin yet!")

  }

  override def turnCrank(): Unit = {
    println("we are giving you a candy,turning another get nothing!")
  }

  override def dispense(): Unit = {
    // TODO Auto-generated method stub

    mCandyMachine.releaseCandy() //数量减去
    if (mCandyMachine.getCount() > 0) { //如果还有糖，则进入readystate
      mCandyMachine.setState(mCandyMachine.mOnReadyState);
    } else { // 没有糖，则进入soleoutstate
      println("Oo,out of candies");
      mCandyMachine.setState(mCandyMachine.mSoldOutState);
    }
  }
}
```

- 6.创建OnReadyState 
``` scala
package com.geekparkhub.core.scala.designpatterns.d07

/**
  * 准备状态
  */
class OnReadyState extends State {
  //说明:@transient注解将字段标记为瞬态的,即表示一个域不是该对象串行化的一部分
  @transient private var mCandyMachine: CandyMachine = _

  def this(mCandyMachine: CandyMachine) {
    this
    this.mCandyMachine = mCandyMachine
  }

  override def getstatename(): String = {
    "OnReadyState"
  }

  override def insertCoin(): Unit = {
    println("you have inserted a coin,next,please turn crank!")
    //同时给糖果机设置，有硬币的状态
    this.mCandyMachine.setState(mCandyMachine.mHasCoin)
  }

  override def printstate(): Unit = {
    println("***OnReadyState***")
  }

  override def returnCoin(): Unit = {
    println("you haven't inserted a coin yet!")
  }

  override def turnCrank(): Unit = {
    println("you turned,but you haven't inserted a coin!")
  }

  //在此状态下dispense没有业务逻辑
  override def dispense(): Unit = {}
}
```

- 7.创建SoldOutState
``` scala
package com.geekparkhub.core.scala.designpatterns.d07

/**
  * 销售完成状态
  */
class SoldOutState extends State {
  //说明:@transient注解将字段标记为瞬态的,即表示一个域不是该对象串行化的一部分
  @transient private var mCandyMachine: CandyMachine = _

  def this(mCandyMachine: CandyMachine) {
    this
    this.mCandyMachine = mCandyMachine
  }

  override def getstatename(): String = {
    "SoldOutState"
  }

  override def insertCoin(): Unit = {
    println("you can't insert coin,the machine sold out!")
  }

  override def printstate(): Unit = {
    println("***SoldOutState***")
  }

  override def returnCoin(): Unit = {
    println("you can't return,you haven't inserted a coin yet!")
  }

  override def turnCrank(): Unit = {
    println("you turned,but there are no candies!")
  }

  //没有业务逻辑
  override def dispense(): Unit = {}
}
```

- 8.创建Monitor
``` scala
package com.geekparkhub.core.scala.designpatterns.d07

import scala.collection.mutable.ListBuffer

/**
  * 监控机器
  */
class Monitor {

  // 监控多台机器
  private val candyMachinelst: ListBuffer[CandyMachine] = ListBuffer()

  // 给监控器增加一台机器
  def addMachine(mCandyMachine: CandyMachine) = {
    candyMachinelst.append(mCandyMachine)
  }

  // 输出该监控器管理的各个机器信息
  def report() = {
    //var mCandyMachine:CandyMachine = null
    for (mCandyMachine <- this.candyMachinelst) {
      println("----------------------------------------")
      println("Machine Loc:" + mCandyMachine.getLocation())
      println("Machine Candy count:" + mCandyMachine.getCount())
      println("Machine State:" + mCandyMachine.getstate().getstatename())
    }
  }
}
```

- 9.创建CanyMachineRunFlow
``` scala
package com.geekparkhub.core.scala.designpatterns.d07

object CanyMachineRunFlow {
  def main(args: Array[String]): Unit = {
    //创建一个监控器
    val mMonitor = new Monitor()

    //XXX-AAA地区 糖果机有6颗糖
    var mCandyMachine = new CandyMachine("XXX-AAA", 6)
    //将糖果机加入监控器
    mMonitor.addMachine(mCandyMachine)

    mCandyMachine = new CandyMachine("XXX-BBB", 4)
    mCandyMachine.insertCoin()
    mMonitor.addMachine(mCandyMachine)

    mCandyMachine = new CandyMachine("XXX-CCC", 14);
    //修改XXX-CCC状态
    mCandyMachine.insertCoin()
    mCandyMachine.turnCrank() //转动曲柄出糖
    mMonitor.addMachine(mCandyMachine)
    //输出监控器管理的所有糖果机情况
    mMonitor.report()
  }
}
```
-10.运行查看结果
```
you have inserted a coin,next,please turn crank!
you have inserted a coin,next,please turn crank!
crank turn...!
a candy rolling out!
----------------------------------------
Machine Loc:XXX-AAA
Machine Candy count:6
Machine State:OnReadyState
----------------------------------------
Machine Loc:XXX-BBB
Machine Candy count:4
Machine State:HasCoin State
----------------------------------------
Machine Loc:XXX-CCC
Machine Candy count:13
Machine State:OnReadyState
```

#### 1.9.2 远程代理模式监控方案
> 远程代理 : 远程对象的本地代表,通过它可以把远程对象当本地对象来调用,远程代理通过网络和真正的远程对象沟通信息.

#### 1.9.3 Java RMI实现远程代理
> RMI是指远程方法调用(Remote Method Invocation),它是一种机制能够让在某个Java虚拟机上的对象调用另一个 Java虚拟机中的对象上的方法,可以用此方法调用的任何对象必须实现该远程接口,RMI可以将底层Socket编程封装,简化操作.

#### 1.9.4 Java RMI介绍
> RMI远程方法调用是计算机之间通过网络实现对象调用的一种通讯机制.
> 使用RMI机制,一台计算机上的对象可以调用另外 一台计算机上的对象来获取远程数据.
> RMI被设计成一种面向对象开发方式,允许开发者使用远程对象来实现通信.

#### 1.9.5 Java RMI实例
> 编写JavaRMI实例,代理端(客户端)可以通过RMI远程调用,远程端注册的服务方法,并且返回结果.
> 
> 实例-开发步骤
> 编写远程接口：接口文件
> 远程接口的实现：Service文件
> RMI服务端注册,开启服务
> RMI代理端通过RMI查询到服务端建立连接,通过接口调用远程方法.
- 1.创建RemoteFlow
``` scala
package com.geekparkhub.core.scala.designpatterns.d07.t02

import java.rmi.{Remote, RemoteException}

/**
  * 定义 文件接口
  * 提供远程端与本地端调用
  */
trait RemoteFlow extends Remote {

  // 定义初始化抽象方法,需要抛出RemoteException异常
  @throws(classOf[RemoteException])
  def init(): String
}
```

- 2.创建RemoteFlowImpl
``` scala
package com.geekparkhub.core.scala.designpatterns.d07.t02

import java.rmi.registry.LocateRegistry
import java.rmi.{Naming, RemoteException}
import java.rmi.server.UnicastRemoteObject

/**
  * 定义 文件实现类
  */
class RemoteFlowImpl extends UnicastRemoteObject with RemoteFlow {

  // 复写初始化抽象方法,需要抛出RemoteException异常
  @throws(classOf[RemoteException])
  override def init(): String = {
    "Start initialization!"
  }
}

/**
  * 定义 文件类 半生对象
  * 完成对初始化方法注册任务
  */
object RemoteFlowImpl {
  def main(args: Array[String]): Unit = {

    // 创建对象
    val service: RemoteFlow = new RemoteFlowImpl
    Naming.rebind("rmi://127.0.0.1:9106/initialization", service)
    println("Remote Service Open | info : <Host : 127.0.0.1 | Port : 9106 | Service Name : initialization>")
  }
}
```

- 3.创建RemoteClientFlow
``` scala
package com.geekparkhub.core.scala.designpatterns.d07.t02

import java.rmi.Naming

/**
  * 定义远程调用客户端
  */
class RemoteClientFlow {
  // 定义方法
  def start(): Unit ={
    val remoteFlow: RemoteFlow = Naming.lookup("rmi://127.0.0.1:9106/initialization").asInstanceOf[RemoteFlow]
    val info: String = remoteFlow.init()
    println("info = " + info)
  }
}

object RemoteClientFlow{
  def main(args: Array[String]): Unit = {
    new RemoteClientFlow().start()
  }
}
```

#### 1.9.6 动态代理
> 动态代理 : 运行时动态的创建代理类(对象),并将方法调用转发到指定类(对象).

##### 1.9.6.1 保护代理
> 动态代理其实就体现出保护代理,即代理时对被代理的对象(类)哪些方法可以调用,哪些方法不能调用在InvocationHandler可以控制,因此动态代理就体现(实现)了保护代理的效果.

##### 1.9.6.2 动态代理实例
> 社区项目 : 已知用户个人首页可以展示:个人信息/兴趣爱好/总体评分
> 要求 : 请使用动态代理实现保护代理效果.
> 用户不能给自己评分 / 其它用户可以评分,但是不能设置对方信息/兴趣爱好.
- 1.创建PersonBean
``` scala
package com.geekparkhub.core.scala.designpatterns.d07.t03

/**
  * 定义 用户接口
  */

trait PersonBean {
  def getName(): String

  def getGender(): String

  def getInterests(): String

  def getScore(): Int

  def setName(name: String)

  def setGender(gender: String)

  def setInterests(interests: String)

  def setScore(score: Int)
}
```

- 2.创建PersonBeanImpl
``` scala
package com.geekparkhub.core.scala.designpatterns.d07.t03

/**
  * 用户实现类
  */
class PersonBeanImpl extends PersonBean {

  var name = ""
  var gender = ""
  var interests = ""

  var score: Int = _ // 评分值

  override def getName(): String = {
    return name
  }

  override def getGender(): String = {
    gender
  }

  override def getInterests(): String = {
    interests
  }

  override def setName(name: String): Unit = {
    this.name = name
  }

  override def setGender(gender: String): Unit = {
    this.gender = gender
  }

  // 用户自身可以调用此方法
  // 其它用户不能调用此方法
  override def setInterests(interests: String): Unit = {
    this.interests = interests
  }


  override def getScore(): Int = {
    score
  }

  // 用户自身不能调用此方法
  // 其它用户可以调此方法
  override def setScore(score: Int): Unit = {
    this.score = score
  }

}
```

- 3.创建OwnerInvocationHandler
``` scala
package com.geekparkhub.core.scala.designpatterns.d07.t03

import java.lang.reflect.{InvocationHandler, Method}

// 用户自身调用的代理类
class OwnerInvocationHandler extends InvocationHandler {

  //被调用的对象PersonBeanImpl
  var person: PersonBean = _

  //构造器
  def this(person: PersonBean) {
    this
    this.person = person
  }

  //说明
  //1.这里的proxy就是和OwnerInvocationHandler合作的代理
  @throws(classOf[Throwable])
  override def invoke(proxy: scala.Any, method: Method, args: Array[AnyRef]): AnyRef = {
    //如果是get方法就直接调用
    if (method.getName().startsWith("get")) {
      return method.invoke(person)
      //自己不能调用setHotOrNotRating,给自己评分
    } else if (method.getName().equals("setScore")) {
      //返回一个异常，同时invoke throws掉了
      return new IllegalAccessException()
      //如果是set方法就直接调用
    } else if (method.getName().startsWith("set")) {
      return method.invoke(person, args(0).toString)
    }
    null
  }
}
```

- 4.创建NonOwnerInvocationHandler
``` scala
package com.geekparkhub.core.scala.designpatterns.d07.t03

import java.lang.reflect.{InvocationHandler, Method}

// 其它用户调用的代理类
class NonOwnerInvocationHandler extends InvocationHandler {

  var person: PersonBean = _

  //构造器
  def this(person: PersonBean) {
    this
    this.person = person
  }

  //说明
  //1.这里的proxy就是和NonOwnerInvocationHandler合作的代理
  @throws(classOf[Throwable])
  override def invoke(proxy: scala.Any, method: Method, args: Array[AnyRef]): AnyRef = {
    //如果是get方法就直接调用
    if (method.getName().startsWith("get")) {
      return method.invoke(person)
      //其它用户可以调用setHotOrNotRating,进行评分
    } else if (method.getName().equals("setScore")) {
      return method.invoke(person, Integer.valueOf(args(0).toString))
      //其它用户不能调用set方法
    } else if (method.getName().startsWith("set")) {
      return new IllegalAccessException()
    }
    null
  }
}
```

-5.创建MatchService
``` scala
package com.geekparkhub.core.scala.designpatterns.d07.t03

import java.lang.reflect.Proxy

class MatchService {
  //创建Person
  val tom = getPersonInfo("tom", "男", "爱好编程")

  //得到一个给自己调用的代理对象,它替代被调用的对象
  val OwnerProxy = getOwnerProxy(tom)

  println("Name is " + OwnerProxy.getName()) // tom
  println("Interests is " + OwnerProxy.getInterests()) // 爱好编程

  OwnerProxy.setInterests("爱好淘宝~")
  println("Interests is " + OwnerProxy.getInterests()) // 爱好淘宝~
  //自己给自己设置评分，通过代理控制，不能成功
  OwnerProxy.setScore(100) //刷分不成功!
  println("Score is " + OwnerProxy.getScore()) //分值仍然为 0


  println("********** 测试NonOwnerInvocationHandler **********")

  val mary = getPersonInfo("mary", "女", "爱好购物...")

  //返回一个其用户调用的代理对象
  val nonOwnerProxy = getNonOwnerProxy(mary)
  println("Name is " + nonOwnerProxy.getName()) // mary
  println("Interests is " + nonOwnerProxy.getInterests()) // 爱好购物...
  //其它人不能修改兴趣，通过代理进行控制不能调用setInterests
  nonOwnerProxy.setInterests("爱好小猫咪~~") //失败，在动态代理控制
  println("Interests is " + nonOwnerProxy.getInterests()) //爱好购物...
  nonOwnerProxy.setScore(68) //其它人可以评分ok
  println("score is " + nonOwnerProxy.getScore()) // 68

  /**
    * 定义获取用户信息方法
    *
    * @param name
    * @param gender
    * @param interests
    * @return
    */
  def getPersonInfo(name: String, gender: String, interests: String): PersonBean = {
    val person = new PersonBeanImpl()
    person.setName(name)
    person.setGender(gender)
    person.setInterests(interests)
    person
  }

  /**
    * 定义 获取自身信息方法
    *
    * @param person
    * @return
    */
  def getOwnerProxy(person: PersonBean): PersonBean = {
    Proxy.newProxyInstance(person.getClass().getClassLoader(), person.getClass().getInterfaces(), new OwnerInvocationHandler(person)).asInstanceOf[PersonBean]
  }

  /**
    * 定义 其他用户获取信息方法
    *
    * @param person
    * @return
    */
  def getNonOwnerProxy(person: PersonBean): PersonBean = {
    Proxy.newProxyInstance(person.getClass()
      .getClassLoader(), person.getClass().getInterfaces(),
      new NonOwnerInvocationHandler(person)).asInstanceOf[PersonBean]
  }
}

/**
  * 程序运行入口
  */
object MatchServiceRun {
  def main(args: Array[String]): Unit = {
    val matchService = new MatchService()
  }
}
```

-6.创建 运行程序查看结果
```
Name is tom
Interests is 爱好编程
Interests is 爱好淘宝~
Score is 0
********** 测试NonOwnerInvocationHandler **********
Name is mary
Interests is 爱好购物...
Interests is 爱好购物...
score is 68
```

##### 1.9.6.3 常见代理模式
> 1.防火墙代理
> 内网通过代理穿透防火墙,实现对公网访问.
> 
> 2.缓存代理
> 当请求文件等资源时,先到缓存代理获取,如果获取到资源则OK,如果获取不到资源,再到公网或者数据库获取然后缓存.
> 
> 3.静态代理
> 静态代理通常用于对原有业务逻辑的扩充.
> 如持有第二方包的某个类,并调用了其中的某些方法,比如记录日志、打印工作等,可以创建一个代理类实现和第二方方法相同的方法,通过让代理类持有真实对象,调用代理类方法,来达到增加业务逻辑的目的.
> 
> 4.Cglib代理
> 使用`cglib[Code Generation Library]`实现动态代理,并不要求委托类必须实现接口,底层采用asm字节码生成框架生成代理类的字节码.
> 说明 : ASM是一个java字节码操纵框架,它能被用来动态生成类或者增强既有类的功能.
> 
> 5.同步代理
> 主要使用在多线程编程中完成多线程间同步工作.



## 2. 📖 算法 📖
### 2.1 🔖  数据结构 介绍 🔖 
> 1.数据结构是一门研究算法的学科,自从有了编程语言也就有了数据结构,学习好数据结构可以编写出更加漂亮,更加优雅有效率的代码.
> 
> 2.想要学习好数据结构就要多考虑如何将生活中遇到的问题,用程序思维去实现解决问题.
> 
> 3.程序 = 数据结构 + 算法


### 2.2 🔖 数据结构和算法的关系 🔖 
> 1.算法是程序的灵魂,为什么有些网站能够在高并发和海量吞吐情况下依然坚如磐石,大家可能会说 : 网站使用了服务器群集技术、数据库读写分离和缓存技术(比如Redis等等).那我们可以反思一下,这些优化技术又是怎样被那些天才的技术高手设计出来的呢?
> 
> 2.思考一个问题 : 是什么原因让不同开发者编写出的同样的代码,从功能看是一样的,但从效率上却有天壤之别?
> 
> 3.在《漫谈 Scala 数据结构 & 算法》Blog中,将着重讲解算法的基石-数据结构.


### 2.3 🔖 实际编程中遇到的问题 🔖 
> 试写出用单链表表示的字符串类及字符串结点类的定义,并依次实现它的构造函数,以及计算串长度,串赋值,判断两串相等,求子串,两串连接,求子串在串中位置等7个成员函数.
#### 2.3.1 五子棋程序
![enter image description here](https://s2.ax1x.com/2019/04/12/Ab0IA0.png)
> 如何判断游戏输赢,并可以完成存盘退出和继续上局功能.

#### 2.3.2 约瑟夫问题 (丢手帕问题)
> Josephu问题为 : 设编号为1,2…, n的n个人围坐一圈,约定编号为k(1<=k<=n)的人从1开始报数,数到m的那个人出列,它的下一位又从1开始报数,数到m的那个人又出列,依次类推,直到所有人出列为止,由此产生一个出队编号的序列.
> 
> 提示 : 用一个不带头结点的循环链表来处理 Josephu
> 
> 问题 : 先构成一个有n个结点的单循环链表,然后由k结点起从1开始计数,计到m时,对应结点从链表中删除,然后再从被删除结点的下一个结点又从1开始计数,直到最后一个结点从链表中删除算法结束.

#### 2.3.3 其它常见算法问题
> 邮差问题 / 最短路径问题 / 汉诺塔 / 八皇后问题


### 2.4 🔖 稀疏数组 sparsearray 🔖
![enter image description here](https://s2.ax1x.com/2019/04/12/Ab0ThT.png)
#### 2.4.1 基本介绍
> 当一个数组中大部分元素为0,或者为同一个值的数组时,可以使用稀疏数组来保存该数组.
> 
> 稀疏数组 处理方法 : 
> 1.记录数组一共有几行几列,有多少个不同的值.
> 2.把具有不同值的元素的行列及值记录在一个小规模的数组中从而缩小程序的规模.
> 
> 稀疏数组举例说明 : 
![enter image description here](https://s2.ax1x.com/2019/04/12/Ab0H9U.png)

#### 2.4.2 应用实例
> 1.使用稀疏数组来保留类似前面的二维数组(棋盘、地图等等).
> 2.将稀疏数组存盘,并且可以重新恢复原来二维数组数.
![enter image description here](https://s2.ax1x.com/2019/04/12/Ab047q.png)
``` scala
package com.geekparkhub.core.scala.algorithm

import scala.collection.mutable.ArrayBuffer

object AlgorithmFlow {
  def main(args: Array[String]): Unit = {
    // 定义二维稀疏数组
    val rowSize = 11
    val colSize = 11
    val chessMap = Array.ofDim[Int](rowSize, colSize)

    // 初始化数组 1即表示黑棋,2即表示白棋
    chessMap(1)(2) = 1
    chessMap(2)(3) = 2

    // 循环遍历 原始数组
    for (i <- chessMap) {
      for (j <- i) {
        printf("%d\t", j)
      }
      println()
    }

    println()

    /**
      * 将 chessMap 转成 稀疏数组
      * 效果是达到对数据的压缩
      */
    val nodesToNodes = ArrayBuffer[Node]()
    val node = new Node(rowSize, colSize, 0)
    nodesToNodes.append(node)
    for (x <- 0 until chessMap.length) {
      for (y <- 0 until chessMap(x).length) {
        // 判断该值是否为0,如果不为0则保存
        if (chessMap(x)(y) != 0) {
          // 创建节点
          val node = new Node(x, y, chessMap(x)(y))
          // 添加到稀疏数组
          nodesToNodes.append(node)
        }
      }
    }

    // 循环输出压缩后稀疏数组
    for (node <- nodesToNodes) {
      printf("%d\t%d\t%d\n", node.row, node.col, node.value)
    }

    println()

    // 将稀疏数组恢复至原始数组
    val newNode: Node = nodesToNodes(0)
    val newRow: Int = newNode.row
    val newCol: Int = newNode.col
    val newChessMap = Array.ofDim[Int](newRow, newCol)
    // 遍历稀疏数组
    for (values <- 1 until nodesToNodes.length) {
      val array = nodesToNodes(values)
      newChessMap(array.row)(array.col) = array.value
    }

    // 稀疏数组恢复棋盘地图
    for (v1 <- newChessMap) {
      for (v2 <- v1) {
        printf("%d\t", v2)
      }
      println()
    }
  }
}

/**
  * 定义节点类
  *
  * @param row
  * @param col
  * @param value
  */
class Node(val row: Int, val col: Int, val value: Int)
```



### 2.5 🔖 队列 queue 🔖 
#### 2.5.1 队列 使用场景
> 比如与排队相关的场景即表示为队列.

#### 2.5.2 队列 介绍
> 1.队列是一个有序列表,可以用数组或是链表来实现.
> 
> 2.遵循先入先出的原则,即先存入队列的数据要先取出,后存入的要后取出.

#### 2.5.3 数组模拟 单向队列
> 1.队列本身是有序列表,若使用数组的结构来存储队列的数据,则队列数组的声明如下 : 其中maxSize是该队列的最大容量.
> 
> 2.因为队列的输出、输入是分别从前后端来处理,因此需要两个变量front(或head)及 rear(或tail)分别记录队列前后端下标,front会随着数据输出而改变,而rear则是随着数据输入而改变.
> 
> ![enter image description here](https://s2.ax1x.com/2019/04/12/Ab0qc4.png)
> 
> 视图说明 : 
> 将数据存入队列时称为addqueue,addqueue处理需要有两个步骤 : 
> 
> 1.将尾指针往后移 : rear + 1,如果front == rear [表示队列为空]
> 
> 2.若尾指引rear小于等于队列的最大下标maxSize - 1,则将数据存入rear所指的数组元素中,否则无法存入数据, rear == maxSize - 1 [表示队列已满]
> 
> 3.虽然实现了队列,但是数据空间不能复用,因此需要对其进行优化,使用取模方式实现环形队列.
``` scala
package com.geekparkhub.core.scala.algorithm

import scala.io.StdIn

object AlgorithmFlow01 {
  def main(args: Array[String]): Unit = {

    // 初始化队列
    val algorithm = new Algorithm(3)
    var inputKey = ""

    // 接收输入参数并触发对应方法
    while (true) {
      println("-add <添加队列数据>")
      println("-show <显示队列数据>")
      println("-get <取出队列数据>")
      println("-head <查看队列头数据>")
      println("-exit <退出队列程序>")
      println()
      inputKey = StdIn.readLine()
      inputKey match {
        case "-add" => {
          println("请输入数据")
          var num1 = StdIn.readInt()
          algorithm.addQueue(num1)
        }
        case "-show" => algorithm.showQueue()
        case "-get" => {
          var res = algorithm.getQueue()
          if (res.isInstanceOf[Exception]) {
            println(res.asInstanceOf[Exception].getMessage)
          } else {
            println(s"取值数据 = $res")
          }
        }
        case "-head" => {
          val res = algorithm.headQueue()
          if (res.isInstanceOf[Exception]) {
            println(res.asInstanceOf[Exception].getMessage)
          } else {
            println(s"头部数据 = $res")
          }
        }
        case "-exit" => System.exit(0)
        case _ => println("输入指令无效,请重试")
      }
    }
  }
}

/**
  * 定义 数组模拟队列
  *
  * @param maxSize
  */
class Algorithm(maxSize: Int) {
  // 定义当前数组最大值
  val max = maxSize
  // 定义数组并存放数据,用于模拟队列
  val arr = new Array[Int](max)
  // 记录队列前端
  var front = -1 // front 是队列最前元素的索引[不含]
  // 记录队列后端
  var rear = -1 // rear 是队列最后元素的索引[含]

  /**
    * 定义 队列是否满足函数
    *
    * @return
    */
  def isFull(): Boolean = {
    rear == max - 1
  }

  /**
    * 定义队列是否为空函数
    *
    * @return
    */
  def isNull(): Boolean = {
    front == rear
  }

  /**
    * 定义 队列取值函数
    *
    * @return
    */
  def getQueue(): Any = {
    if (isNull()) {
      return new Exception("队列数据为空!")
    }
    front += 1
    return arr(front)
  }

  /**
    * 定义 添加数据函数
    *
    * @param n1
    */
  def addQueue(n1: Int): Unit = {
    if (isFull()) {
      println("队列已满,无法添加数据")
      return
    }
    rear += 1
    arr(rear) = n1
    println("数据" + n1 + "添加成功")
    println()
  }

  /**
    * 定义显示队列所有数据 函数
    */
  def showQueue(): Unit = {
    // 显示队列数据之前,先判断队列是否为空
    if (isNull()) {
      println("队列为空,无数据")
      println()
      return
    }
    // 遍历队列数据
    for (i <- front + 1 to rear) {
      printf("res = arr[%d]=%d\n", i, arr(i))
      println()
    }
  }

  /**
    * 定义 查看队列头部元素
    */
  def headQueue(): Unit = {
    if (isNull()) {
      return new Exception("队列数据为空!")
    }
    return arr(front + 1)
  }
}
```

#### 2.5.4 数组模拟 环形队列
> 说明：
> 对上面的数组模拟队列的优化,充分利用数组,因此将数组看做是一个环形,(通过取模方式来实现即可).
> 
> 分析说明 : 
> 1.尾索引的下一个为头索引时表示队列满,即将队列容量空出一个作为约定,在做判断队列满的时需要注意`(rear + 1) % maxSize == front` [表示队列已满].
> 
> 2.rear == front [表示队列为空]
``` scala
package com.geekparkhub.core.scala.algorithm

import scala.io.StdIn

object AlgorithmFlow02 {
  def main(args: Array[String]): Unit = {
    // 初始化队列
    val algorithm = new Algorithms(4)
    var inputKey = ""

    // 接收输入参数并触发对应方法
    while (true) {
      println("-add <添加队列数据>")
      println("-show <显示队列数据>")
      println("-get <取出队列数据>")
      println("-head <查看队列头数据>")
      println("-exit <退出队列程序>")
      println()
      inputKey = StdIn.readLine()
      inputKey match {
        case "-add" => {
          println("请输入数据")
          var num1 = StdIn.readInt()
          algorithm.addQueue(num1)
        }
        case "-show" => algorithm.showQueue()
        case "-get" => {
          var res = algorithm.getQueue()
          if (res.isInstanceOf[Exception]) {
            println(res.asInstanceOf[Exception].getMessage)
          } else {
            println(s"取值数据 = $res")
          }
        }
        case "-head" => {
          val res = algorithm.headQueue()
          if (res.isInstanceOf[Exception]) {
            println(res.asInstanceOf[Exception].getMessage)
          } else {
            println(s"头部数据 = $res")
          }
        }
        case "-exit" => System.exit(0)
        case _ => println("输入指令无效,请重试")
      }
    }
  }
}

/**
  * 定义 数组模拟队列
  *
  * @param maxSizes
  */
class Algorithms(maxSizes: Int) {
  // 定义当前数组最大值
  val max = maxSizes
  // 定义数组并存放数据,用于模拟队列
  val arr = new Array[Int](max)
  // 记录队列前端
  var front = 0 // front 是队列最前元素的索引[含]
  // 记录队列后端
  var rear = 0 // rear 是队列最后元素的索引[含]

  /**
    * 定义 判断队列是否已满 方法
    *
    * @return
    */
  def isFull(): Boolean = {
    // 尾索引的下一个为头索引时表示队列满,即将队列容量空出一个作为约定,在做判断队列满的时候需要注意
    (rear + 1) % maxSizes == front
  }

  /**
    * 定义 判断队列是否为空 方法
    *
    * @return
    */
  def isNull(): Boolean = {
    rear == front
  }

  /**
    * 定义 添加数据函数
    *
    * @param n2
    */
  def addQueue(n2: Int): Unit = {
    if (isFull()) {
      println("队列已满,无法添加数据")
      return
    }
    arr(rear) = n2
    // 将 rear 通过取模的方式后移m注意与 rear = rear + 1 的区别
    rear = (rear + 1) % maxSizes
    println("数据" + n2 + "添加成功")
    println()
  }

  /**
    * 定义 获取对列数据 方法
    *
    * @return
    */
  def getQueue(): Any = {
    // 获取队列数据之前,先判断队列是否为空
    if (isNull()) {
      return new Exception("对列为空,无法获取对列数据")
    }
    val value = arr(front)
    // 将 front 通过取模的方式后移，注意与 front = front + 1 的区别
    front = (front + 1) % maxSizes
    return value
  }

  // 显示环形队列的所有数据
  def showQueue(): Unit = {
    // 显示队列数据之前，先判断队列是否为空
    if (isNull()) {
      println("队列为空，没有数据可显示...")
      return
    }

    // 思路：从 front 取，取出几个元素
    for (i <- front until front + size()) {
      printf("arr[%d]=%d\n", i % maxSizes, arr(i % maxSizes))
    }
  }

  // 求出当前环形队列有几个元素
  def size(): Int = {
    // 算法
    (rear + maxSizes - front) % maxSizes
  }

  // 查看队列的头元素，但是不是改变队列
  def headQueue(): Any = {
    if (isNull()) {
      return new Exception("队列为空，没有头元素可查看")
    }
    // 这里注意，不要去改变 fornt 值
    return arr(front)
  }

}
```



### 2.6 🔖 链表 linked list 🔖 
#### 2.6.1 链表 介绍
> 链表是有序列表.
> 
> 链表数据,在内存空间不一定是连续分布.
> 
> 链表在内存中是存储如下 : 
> ![enter image description here](https://s2.ax1x.com/2019/04/12/Ab0LjJ.png)

#### 2.6.2 单向链表 介绍
> 单向链表(带头结点)逻辑结构示意图如下 : 
> 
> 所谓带头节点就是链表的头有一个head点,该节点不存放具体数据,只是为了操作方便而设计的这个节点.
> 
> ![enter image description here](https://s2.ax1x.com/2019/04/12/Ab0jBR.png)


#### 2.6.3 单向链表 应用实例
> 使用带head头的单向链表实现 : 排行榜管理功能
> 完成对单向链表的增删改查功能.
- 1.无序单向链表实例
``` scala
package com.geekparkhub.core.scala.algorithm

import util.control.Breaks._

object AlgorithmFlow03 extends App {

  // 创建PersonaNode对象
  val node01 = new PersonaNode(1, "RoBot001", "RB01")
  val node02 = new PersonaNode(2, "RoBot002", "RB02")
  val node04 = new PersonaNode(4, "RoBot004", "RB04")
  val node03 = new PersonaNode(3, "RoBot003", "RB03")

  // 创建单向链表对象
  val singleLinkedList = new SingleLinkedList()
  // 调用添加链表方法
  singleLinkedList.add001(node01)
  singleLinkedList.add001(node02)
  singleLinkedList.add001(node04)
  singleLinkedList.add001(node03)
  // 调用查询链表方法
  singleLinkedList.list()
}

/**
  * 定义单向链表
  */
class SingleLinkedList {

  // 初始化 PersonaNode 头节点
  val headNode = new PersonaNode(0, "", "")

  /**
    * 第一种方式 : 定义 添加节点方法
    * 在添加人物信息时,直接将数据添加到链表尾部
    *
    * @param personaNode
    */
  def add001(personaNode: PersonaNode): Unit = {
    // 定义临时节点作为辅助
    var tempNode = headNode
    // 寻找链表最后
    breakable {
      while (true) {
        if (tempNode.next == null) {
          break()
        }
        // 如果没有到链表最后,继续寻找链表
        tempNode = tempNode.next
      }
    }
    // 在链表最后将对象地址赋值给tempNode
    tempNode.next = personaNode
  }

  /**
    * 定义 查询节点方法
    */
  def list(): Unit = {
    // 先判断当前列表是否为空
    if (headNode.next == null) {
      println("链表为空!")
      return
    }
    // temp指向head下一个数据地址
    var temp = headNode.next
    breakable {
      while (true) {
        if (temp == null) {
          break()
        }
        printf("Node Info : no = %d name = %s nickname = %s\n", temp.no, temp.name, temp.nickname)
        temp = temp.next
      }
    }
  }
}

/**
  * 定义 人物角色节点
  * Persona Node
  * @param personaNo 角色ID
  * @param personaName 角色名称
  * @param personaNickname 角色简称
  */
class PersonaNode(personaNo: Int, personaName: String, personaNickname: String) {
  var no: Int = personaNo
  var name: String = personaName
  var nickname: String = personaNickname
  // next 默认为 null
  var next: PersonaNode = null
}
```

- 2.有序单向链表实例
``` scala
package com.geekparkhub.core.scala.algorithm

import util.control.Breaks._

object AlgorithmFlow03 extends App {

  // 创建PersonaNode对象
  val node01 = new PersonaNode(1, "RoBot001", "RB01")
  val node02 = new PersonaNode(2, "RoBot002", "RB02")
  val node04 = new PersonaNode(4, "RoBot004", "RB04")
  val node03 = new PersonaNode(3, "RoBot003", "RB03")
  val node05 = new PersonaNode(3, "RoBot005", "RB05")
  val node06 = new PersonaNode(3, "RoBot006", "RB06")

  // 创建单向链表对象
  val singleLinkedList = new SingleLinkedList()

  // 调用无序添加链表方法
  singleLinkedList.add001(node01)
  singleLinkedList.add001(node02)
  singleLinkedList.add001(node04)
  singleLinkedList.add001(node03)

  // 调用有序添加链表方法
  //  singleLinkedList.add002(node01)
  //  singleLinkedList.add002(node02)
  //  singleLinkedList.add002(node04)
  //  singleLinkedList.add002(node03)

  // 调用无序修改链表方法
  singleLinkedList.update(node05)

  // 调用无序修改链表方法
  singleLinkedList.update2(node06)

  // 调用无序删除链表方法
  singleLinkedList.del(3)

  // 调用查询链表方法
  singleLinkedList.list()
}

/**
  * 定义单向链表
  */
class SingleLinkedList {
  // 初始化 PersonaNode 头节点
  val headNode = new PersonaNode(0, "", "")

  /**
    * 第一种方式 : 定义 添加节点方法
    * 在添加人物信息时,直接将数据添加到链表尾部
    *
    * @param personaNode
    */
  def add001(personaNode: PersonaNode): Unit = {
    // 定义临时节点作为辅助
    var tempNode = headNode
    // 寻找链表最后
    breakable {
      while (true) {
        if (tempNode.next == null) {
          break()
        }
        // 如果没有到链表最后,继续寻找链表
        tempNode = tempNode.next
      }
    }
    // 在链表最后将对象地址赋值给tempNode
    tempNode.next = personaNode
  }

  /**
    * 第二种方式 : 定义 添加节点方法
    * 在添加人物信息时,根据排名将人物信息插入到指定位置
    *
    * @param personaNode
    */
  def add002(personaNode: PersonaNode): Unit = {
    // 定义临时节点作为辅助
    var tempNode = headNode
    // flag 用于判断该人物编号是否已存在
    var flag = false
    breakable {
      while (true) {
        // 节点tempNode已经是链表最后
        if (tempNode.next == null) {
          break()
        }
        // 位置定位,节点personaNode应加入到节点tempNode.next前面与节点tempNode后面
        if (personaNode.no < tempNode.next.no) {
          break()
        } else if (personaNode.no == tempNode.next.no) {
          flag = true
          break()
        }
        tempNode = tempNode.next
      }
    }
    if (flag) {
      printf("待添加人物ID %d 已经存在,无法加入\\n\",personaNode.no")
    } else {
      personaNode.next = tempNode.next
      tempNode.next = personaNode
    }
  }

  /**
    * 方式一 : 定义 修改节点数据 方法
    * 根据人物ID修改节点数据
    *
    * @param newPersonaNode
    */
  def update(newPersonaNode: PersonaNode): Unit = {
    // 判断链表是否为空
    if (headNode.next == null) {
      println("链表为空,无法修改!")
      break()
    }
    var temp = headNode.next
    var flag = false
    breakable {
      while (true) {
        if (temp == null) {
          break()
        }
        if (temp.no == newPersonaNode.no) {
          flag = true
          break()
        }
        temp = temp.next
      }
    }
    // 跳出循环,找到对应链表节点,并修改数据
    if (flag) {
      temp.name = newPersonaNode.name
      temp.nickname = newPersonaNode.nickname
    } else {
      printf("没有找到编号为 %d 的节点,无法修改！\n", newPersonaNode.no)
    }
  }

  /**
    * 方式二 : 定义 修改节点数据 方法
    * 将整个节点替换,即重新指向新节点数据
    *
    * @param newPersonaNod1
    */
  def update2(newPersonaNod1: PersonaNode): Unit = {
    if (headNode.next == null) {
      println("链表为空,不能修改!")
      return
    }
    var temp = headNode.next
    var flag = false
    breakable {
      while (true) {
        // 判断是否找到该节点
        if (temp == null) {
          break()
        }
        // 判断已找到该节点
        if (temp.no == newPersonaNod1.no) {
          flag = true
          break()
        }
        temp = temp.next
      }
    }
    if (flag) {
      // 删除节点ID
      del(temp.no)
      // 添加新节点
      add001(newPersonaNod1)
    } else {
      printf("没有找到人物ID为 %d 节点,无法修改！\n", newPersonaNod1.no)
    }
  }

  /**
    * 定义 删除节点方法
    * 根据人物ID删除节点数据
    *
    * @param no
    */
  def del(no: Int): Unit = {
    var temp = headNode
    var flag = false
    breakable {
      while (true) {
        if (temp.next == null) {
          break()
        }
        // 判断是否找到该节点
        if (temp.next.no == no) {
          flag = true
          break()
        }
        temp = temp.next
      }
    }
    if (flag) {
      // 删除节点操作
      temp.next = temp.next.next
    } else {
      printf("no=%d 节点删除失败,因节点不存在\n", no)
    }
  }

  /**
    * 定义 查询节点方法
    */
  def list(): Unit = {
    // 先判断当前列表是否为空
    if (headNode.next == null) {
      println("链表为空!")
      return
    }
    // temp指向head下一个数据地址
    var temp = headNode.next
    breakable {
      while (true) {
        if (temp == null) {
          break()
        }
        printf("Node Info : no = %d name = %s nickname = %s\n", temp.no, temp.name, temp.nickname)
        temp = temp.next
      }
    }
  }
}

/**
  * 定义 人物角色节点
  * Persona Node
  *
  * @param personaNo 角色ID
  * @param personaName 角色名称
  * @param personaNickname 角色简称
  */
class PersonaNode(personaNo: Int, personaName: String, personaNickname: String) {
  var no: Int = personaNo
  var name: String = personaName
  var nickname: String = personaNickname
  // next 默认为 null
  var next: PersonaNode = null
}
```





#### 2.6.4 双向链表 应用实例
> 使用带head头的双向链表实现 : 人物排行榜管理.
> 
> 单向链表的缺点分析 : 
> 1.单向链表查找的方向只能是一个方向,而双向链表可以向前或者向后查找.
> 2.单向链表不能自我删除,需要靠辅助节点,而双向链表则可以自我删除,所以单链表删除时节点,总是找到temp的下一个节点来删除.
- 1.双向链表实例
``` scala
package com.geekparkhub.core.scala.algorithm

import util.control.Breaks._

object AlgorithmFlow04 extends App {

  // 创建PersonaNodes对象
  val node01 = new PersonaNodes(1, "RoBot001", "RB01")
  val node02 = new PersonaNodes(2, "RoBot002", "RB02")
  val node04 = new PersonaNodes(4, "RoBot004", "RB04")
  val node03 = new PersonaNodes(3, "RoBot003", "RB03")
  val node05 = new PersonaNodes(3, "RoBot005", "RB05")

  // 创建双向链表对象
  val doubleLinkedList = new DoubleLinkedList()

  // 调用 双向链表 添加无序数据 方法
  doubleLinkedList.addDoubleLinked(node01)
  doubleLinkedList.addDoubleLinked(node02)
  doubleLinkedList.addDoubleLinked(node04)
  doubleLinkedList.addDoubleLinked(node03)

  // 调用无序修改链表方法
  doubleLinkedList.update(node05)

  // 调用 双向链表 删除节点方法
  doubleLinkedList.del(2)
  doubleLinkedList.del(3)

  // 调用 双向链表 查询数据方法
  doubleLinkedList.showDoubleLinked()
}

/**
  * 定义 双向链表
  */
class DoubleLinkedList {
  // 初始化 PersonaNodes 头节点
  val headNodes = new PersonaNodes(0, "", "")

  /**
    * 方式一 : 定义 双向链表 添加无序数据 方法
    * 在添加人物信息时,直接将数据添加到链表尾部
    *
    * @param personaNodes
    */
  def addDoubleLinked(personaNodes: PersonaNodes): Unit = {
    // 定义临时节点作为辅助
    var temp = headNodes
    breakable {
      // 寻找链表最后
      while (true) {
        if (temp.next == null) {
          break()
        }
        temp = temp.next
      }
    }
    // 当退出while循环后,temp指向的就是链表的最后
    // 在链表的最后将 角色对象地址赋值给temp
    temp.next = personaNodes
    personaNodes.pre = temp
  }

  /**
    * 方式二 : 定义 双向链表 添加有序数据 方法
    * 在添加人物信息时,根据排名将人物信息插入到指定位置
    *
    * @param personaNodes
    */
  def addDoubleLinkeds(personaNodes: PersonaNodes): Unit = {

  }

  /**
    * 定义 查询 双向链表数据 方法
    */
  def showDoubleLinked(): Unit = {
    // 先判断当前列表是否为空
    if (headNodes.next == null) {
      println("链表为空!")
      return
    }
    // temp指向head下一个数据地址
    var temp = headNodes.next
    breakable {
      while (true) {
        if (temp == null) {
          break()
        }
        printf("Node Info : no = %d name = %s nickname = %s\n", temp.no, temp.name, temp.nickname)
        temp = temp.next
      }
    }
  }

  /**
    * 定义 双向链表 节点更新 方法
    * @param personaNodes
    */
  def update(personaNodes: PersonaNodes): Unit = {
    // 判断链表是否为空
    if (headNodes.next == null) {
      println("链表为空,无法修改!")
      break()
    }
    var temp = headNodes.next
    var flag = false
    breakable {
      while (true) {
        if (temp == null) {
          break()
        }
        if (temp.no == personaNodes.no) {
          flag = true
          break()
        }
        temp = temp.next
      }
    }
    // 跳出循环,找到对应链表节点,并修改数据
    if (flag) {
      temp.name = personaNodes.name
      temp.nickname = personaNodes.nickname
    } else {
      printf("没有找到编号为 %d 的节点,无法修改！\n", personaNodes.no)
    }
  }

  /**
    * 定义 删除节点
    * 根据编号删除节点,利用双向链表可以实现自我删除的特点
    * @param no
    */
  def del(no: Int): Unit = {
    // 先判断当前列表是否为空
    if (headNodes.next == null) {
      println("链表为空,无法删除!")
      return
    }
    // 辅助节点
    var temp = headNodes.next
    var flag = false
    breakable {
      while (true) {
        if (temp == null) {
          break()
        }
        if (temp.no == no) { // 找到该节点
          flag = true
          break()
        }
        temp = temp.next
      }
    }
    if (flag) {
      // 删除节点
      temp.pre.next = temp.next
      if (temp.next != null) {
        temp.next.pre = temp.pre
        temp.pre = null
        temp.next = null
      } else {
        temp.pre = null
      }
    } else {
      printf("删除失败,该no=%d节点不存在\n", no)
    }
  }
}

/**
  * 定义 人物角色节点
  * Persona Node
  * @param personaNo  角色ID
  * @param personaName 角色名称
  * @param personaNickname 角色简称
  */
class PersonaNodes(personaNo: Int, personaName: String, personaNickname: String) {
  var no: Int = personaNo
  var name: String = personaName
  var nickname: String = personaNickname
  var pre: PersonaNodes = null
  // next 默认为 null
  var next: PersonaNodes = null
}
```


#### 2.6.5 单向环形链表 应用场景
##### 2.6.5 约瑟夫问题
> 说明 : 
> 
> 设编号为1,2，…，n的n个人围坐一圈,约定编号为k（1<=k<=n）的人从1开始报数,数到 m的那个人出列,它的下一位又从1开始报数,数到m的那个人又出列,依次类推,直到所有人出列为止,由此产生一个出队编号的序列.
> 
> 问题具体化 : 
> 先构成一个有n个结点的单循环链表,然后由k结点起从1开始计数,计到m时,对应结点从链表中删除,然后再从被删除结点的下一个结点又从1开始计数,直到最后一个结点从链表中删除算法结束.
- **单向环形链表 实例**
``` scala
package com.geekparkhub.core.scala.algorithm

import util.control.Breaks._

object JosephuFlow extends App {
  // 创建 单向环形链表对象
  val boyGame = new BoyGame()
  // 调用 添加玩家方法
  boyGame.addBoy(7)
  // 调用 显示玩家方法
  boyGame.showBoy()
  boyGame.countBoy(4, 3, 7)
}

/**
  * 定义单向链表,用来管理Boy
  */
class BoyGame {

  // 初始化头结点,禁止改动头结点
  var first: Boy = null

  /**
    * 定义添加Boy 方法
    * 形成单向环形链表
    *
    * @param nums 表示共有多少玩家
    */
  def addBoy(nums: Int): Unit = {
    if (nums < 1) {
      println("Boy人数不正确,请重新输入!")
      return
    }
    // 因为头结点不能动,因此需要有一个临时节点作为辅助,只是该辅助节点的指向是null,即是一个没有指向任何地址的指针
    var temp: Boy = null
    for (no <- 1 to nums) {
      // 根据编号创建Boy对象
      val boy = new Boy(no)
      // 如果是第一个Boy则自己指向自己,并将temp也指向第一个 Boy
      if (no == 1) {
        first = boy
        boy.next = first
        temp = first // 辅助指针指向到第一个Boy,即 irst
      } else {
        temp.next = boy // 辅助指针指向当前的Boy
        boy.next = first // 当前的Boy指向第一个Boy
        temp = boy // 辅助指针指向下一个Boy
      }
    }
  }

  /**
    * 定义 遍历单向环形链表 方法
    */
  def showBoy(): Unit = {
    if (first.next == null) {
      println("没有Boy")
      return
    }
    // 因为头结点不能动,因此需要有临时节点作为辅助
    // 又因为first节点的数据有关,因此这里使得temp指向first地址
    var temp = first
    breakable {
      while (true) {
        printf("玩家 Boy ID = %d\n", temp.no)
        println("===================")
        if (temp.next == first) {
          break()
        }
        temp = temp.next // 移动指针到下一个Boy
      }
    }
  }

  /**
    * 编写 countBoy
    *
    * @param startNo  从第几个玩家开始数
    * @param countNum 次数
    * @param nums     总人数
    */
  def countBoy(startNo: Int, countNum: Int, nums: Int): Unit = {
    // 对参数进行判断
    if (first.next == null || startNo < 1 || startNo > nums) {
      println("参数有误,请重新输入!")
      return
    }
    /**
      * 思路
      * 1.在first前面设计辅助指针temp,即将temp指针定位到first前面
      */
    var temp = first // 辅助指针
    breakable {
      // 遍历一圈单向环形链表后,找到指针first的前一个位置,此时是新temp
      while (true) {
        if (temp.next == first) {
          break()
        }
        // 移动指针
        temp = temp.next
      }
    }
    // 2.将first指针移动到startNo位置,将temp指针移动到startNo - 1位置
    for (i <- 1 until startNo) {
      first = first.next
      temp = temp.next
    }
    breakable {
      while (true) {
        if (temp == first) {
          break()
        }
        // 3.开始数countNum个位置, first和temp指针对应移动
        for (i <- 1 until countNum) {
          first = first.next
          temp = temp.next
        }
        printf("玩家 Boy ID = %d  已出局\n", first.no)
        // 4.删除first指向的节点,并移动first指针到下一节点,temp指针对应移动
        temp.next = first.next
        first = first.next
      }
    }
    // while循环结束后,只有一个玩家
    printf("最后玩家 Boy ID = %d", first.no)
  }
}

// 定义 Boy 类
class Boy(bNo: Int) {
  var no: Int = bNo
  var next: Boy = null
}
```

### 2.7 🔖 栈 stack 🔖 
#### 2.7.1 实际需求
> 请输入一个表达式并输出计算结果.
> 计算式：[722-5+1-5+3-3]  = ?
#### 2.7.2 栈 介绍
> 1.栈 英文为(stack)
> 
> 2.栈是一个先入后出(FILO:First In Last Out)有序列表
> 
> 3.栈(stack)是限制线性表中元素的插入和删除只能在线性表的同一端进行的一种特殊线性表,允许插入和删除的一端,为变化的一端,称为栈顶(Top),另一端为固定的一端,称为栈底(Bottom).
> 
> 4.根据堆栈的定义可知,最先放入栈中元素在栈底,最后放入的元素在栈顶,而删除元素刚好相反,最后放入的元素最先删除,最先放入的元素最后删除.
> 
> 出栈 & 入栈 概念
> 
> 入栈 : 
> ![enter image description here](https://s2.ax1x.com/2019/04/12/AbBEDA.png)
> 
> 出栈 : 
> ![enter image description here](https://s2.ax1x.com/2019/04/12/AbBFjH.png)



#### 2.7.3 栈 经典应用场景
> 1.子程序的调用 : 在跳往子程序前,会先将下个指令的地址存到堆栈中,直到子程序执行完后再将地址取出,以回到原来的程序中.
> 
> 2.处理递归调用 : 和子程序的调用类似,只是除了储存下一个指令的地址外,也将参数、区域变量等数据存入堆栈中.
> 
> 3.表达式的转换与求值.
> 
> 4.二叉树遍历
> 
> 5.图形深度优先(depth-first)搜索法.



#### 2.7.4 栈 快速入门
> 使用数组模拟 栈
> 由于栈是一种有序列表,可以使用数组结构来储存栈的数据内容.
> 下面用数组模拟栈的出栈、入栈等操作,实现思路分析并画出示意图,如下 : 
> ![enter image description here](https://s2.ax1x.com/2019/04/12/AbBAud.png)
- 栈 实例
``` scala
package com.geekparkhub.core.scala.algorithm

import scala.io.StdIn

object StackFlow extends App {
  // 创建arrayStack建对象
  val arrayStack = new ArrayStack(4)
  var key = ""
  while (true) {
    println("-show 显示栈")
    println("-push 压栈")
    println("-pop 弹栈")
    println("-quit 退出栈")
    key = StdIn.readLine()
    key match {
      case "-show" => arrayStack.showStack()
      case "-push" => {
        println("请输入整数")
        val temps = StdIn.readInt()
        arrayStack.push(temps)
      }
      case "-pop" => {
        val res: Any = arrayStack.pop()
        if (res.isInstanceOf[Exception]) {
          println(res.asInstanceOf[Exception].getMessage)
        } else {
          printf("Res is %d\n", res)
        }
      }
      case "-quit" => System.exit(0)
      case _ => println("输入参数有误,请重试!")
    }
  }
}

/**
  * 定义 栈
  *
  * @param maxSize
  */
class ArrayStack(maxSize: Int) {
  // 定义参数最大值
  var max = maxSize

  // 定义 Top栈顶指针
  var top = -1

  // 定义 数组
  var stack = new Array[Int](max)

  /**
    * 定义 栈是否为满 方法
    * @return
    */
  def isFull(): Boolean = {
    top == max - 1
  }

  /**
    * 定义 判断栈是否为空 方法
    * @return
    */
  def isNull(): Boolean = {
    top == -1
  }

  /**
    * 定义 入栈方法
    * @param value
    */
  def push(value: Int): Unit = {
    if (isFull()) {
      println("栈满")
      return
    }
    // 栈顶指针+1上移
    top += 1
    //即表示 arr(1) = value
    stack(top) = value
  }

  /**
    * 出栈
    * @return
    */
  def pop(): Any = {
    if (isNull()) {
      return new Exception("栈空")
    }
    // 将栈缓存到tempStack变量中
    val tempStack = stack(top)
    // 栈顶指针-1下移
    top -= 1
    // 最后返回tempStack
    return tempStack
  }

  /**
    * 遍历 栈
    */
  def showStack(): Unit = {
    if (isNull()) {
      println("栈空")
      return
    }
    for (i <- 0 to top reverse) {
      printf("stack[%d]=%d\n", i, stack(i))
    }
  }
}
```



#### 2.7.5 栈 实现综合计算器



## 🔒 尚未解锁 正在探索中... 尽情期待 Blog更新! 🔒
### 2.8 🔖 递归 recursive 🔖 
#### 2.8.1 实际应用场景
#### 2.8.2 递归 概念
#### 2.8.3 递归 快速入门
#### 2.8.4 递归用于解决哪些问题
#### 2.8.5 递归遵守重要原则
#### 2.8.6 应用实例 迷宫问题

### 2.9 🔖 排序 sort 🔖 
#### 2.9.1 排序 介绍
#### 2.9.2 冒泡排序
#### 2.9.3 选择排序
#### 2.9.4 插入排序
#### 2.9.5 快速排序
#### 2.9.6 归并排序

### 2.10 🔖 查找 🔖 
#### 2.10.1 介绍
#### 2.10.2 线性查找
#### 2.10.3 二分查找

### 2.11 🔖 哈希表(散列表) 🔖 
#### 2.11.1 实际需求
#### 2.11.2 哈希表 基本介绍
#### 2.11.3 应用实例

### 2.12 🔖 二叉树 🔖 
#### 2.12.1 为什么需要树数据结构
#### 2.12.2 二叉树 示意图
#### 2.12.3 二叉树 概念
#### 2.12.4 二叉树 遍历说明
#### 2.12.5 二叉树遍历 应用实例(前序/中序/后序)
#### 2.12.6 二叉树-查找指定节点
#### 2.12.7 二叉树-删除节点

### 2.13 🔖 顺序存储二叉树 🔖 
#### 2.13.1 顺序存储二叉树 概念
#### 2.13.2 顺序存储二叉树 遍历

### 2.14 🔖 二叉排序树 🔖 
#### 2.14.1 实例需求
#### 2.14.2 二叉排序树 介绍
#### 2.14.3 二叉排序树 创建 & 遍历
#### 2.14.4 二叉排序树 删除

### 2.15 🔖 其它二叉树 🔖 



## 3. 修仙之道 技术架构迭代 登峰造极之势
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