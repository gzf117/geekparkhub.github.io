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


### 1.5 简单工厂
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


### 1.6 单例模式
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

### 1.7 装饰者模式
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

### 1.8 观察者模式
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


### 1.9 代理模式



## 🔒 尚未解锁 正在探索中... 尽情期待 Blog更新! 🔒
## 2. 📖 算法 📖
### 2.1 🔖  数据结构介绍 🔖 
### 2.2 🔖 数据结构和算法的关系 🔖 

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