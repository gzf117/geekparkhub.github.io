package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._

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
  * TransformationFlow
  * <p>
  */

object TransformationFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用mapFlow方法
  mapFlow()

  // 调用FlatMapFlow方法
  FlatMapFlow()

  // 调用FilterFlow方法
  FilterFlow()

  // 调用ConnectFlow方法
  ConnectFlow()

  // 调用CoMapFlow方法
  CoMapFlow()

  // 调用CoFlatMapFlow方法
  CoFlatMapFlow()

  // 调用SplitFlow方法
  SplitFlow()

  // 调用SplitAndSelectFlow方法
  SplitAndSelectFlow()

  // 调用UnionFlow方法
  UnionFlow()

  // 调用KeyByFlow方法
  KeyByFlow()

  // 调用ReduceFlow方法
  ReduceFlow()

  // 调用FoldFlow方法
  FoldFlow()

  // 调用AggregationsFlow方法
  AggregationsFlow()

  /**
    * 定义map方法
    * DataStream →DataStream：输入一个参数产生一个参数
    */
  def mapFlow(): Unit = {
    // 创建初始数据 -> (Source)
    val stream = env.generateSequence(1, 20)
    // 调用map函数
    val streamMap = stream.map(x => x * 2)
    // 打印数据 -> (Sink)
    streamMap.print()
    // 触发程序执行
    env.execute("mapFlow")
  }

  /**
    * 定义FlatMapFlow方法
    * DataStream → DataStream：输入一个参数,产生0个、1个或者多个输出.
    */
  def FlatMapFlow(): Unit = {
    // 加载初始数据 -> (Source)
    val filePaths = "../flink_server/flink-coreflow/src/main/resources/input_01/test03.txt"
    val stream = env.readTextFile(filePaths)
    // 调用flatMap函数对数据以空格进行数据切分
    val streamFlatMap = stream.flatMap(x => x.split(" "))
    // 打印数据 -> (Sink)
    streamFlatMap.print()
    // 触发程序执行
    env.execute("FlatMapFlow")
  }

  /**
    * 定义FilterFlow方法
    * DataStream → DataStream : 计算每个元素的布尔值,并返回布尔值为true的元素.
    */
  def FilterFlow(): Unit = {
    // 创建初始数据 -> (Source)
    val stream = env.generateSequence(1, 20)
    // 调用filter函数,去除不等于1的元素的值
    val streamFilter = stream.filter(x => x == 1)
    // 打印数据 -> (Sink)
    streamFilter.print()
    // 触发程序执行
    env.execute("FilterFlow")
  }

  /**
    * 定义ConnectFlow方法
    * DataStream , DataStream → ConnectedStreams
    */
  def ConnectFlow(): Unit = {
    // 加载与创建初始数据 -> (Source)
    val filePaths = "../flink_server/flink-coreflow/src/main/resources/input_01/test03.txt"
    val stream01 = env.generateSequence(1, 20)
    val stream02 = env.readTextFile(filePaths).flatMap(x => x.split(" "))
    // stream01将与stream02连接并形成ConnectedStreams连接流
    var streamConnect = stream01.connect(stream02)
    /**
      * 当ConnectedStreams在调用map函数的过程就称之为CoMap操作
      * x 即代表stream01在调用flatMap函数的过程就称之为CoFlatMap操作
      * y 即代表stream02在调用flatMap函数时的过程就称之为CoFlatMap操作
      *
      * 说明 : 对ConnectedStreams流进行CoMap操作
      * 说明 : `x` 即代表对stream01进行CoFlatMap操作
      * 说明 : `y` 即代表对stream02进行CoFlatMap操作
      *
      */
    val streamRes = streamConnect.map(x => x * 2, y => (y, 1L))
    // 打印数据 -> (Sink)
    streamRes.print()
    // 触发程序执行
    env.execute("ConnectFlow")
  }

  /**
    * 定义CoMapFlow方法
    * ConnectedStreams → DataStream
    */
  def CoMapFlow(): Unit = {
    // 加载与创建初始数据 -> (Source)
    val filePaths = "../flink_server/flink-coreflow/src/main/resources/input_01/test03.txt"
    val stream01 = env.generateSequence(1, 20)
    val stream02 = env.readTextFile(filePaths).flatMap(x => x.split(" "))
    // stream01将与stream02连接并形成ConnectedStreams连接流
    var streamConnect = stream01.connect(stream02)
    // 当streamConnect调用map函数的过程就称之为CoMap操作
    val streamCoMap = streamConnect.map((x) => x + 100, (y) => y + " connect")
    // 打印数据 -> (Sink)
    streamCoMap.print()
    // 触发程序执行
    env.execute("CoMapFlow")
  }

  /**
    * 定义CoFlatMapFlow方法
    * ConnectedStreams → DataStream
    */
  def CoFlatMapFlow(): Unit = {
    // 加载初始数据 -> (Source)
    val filePaths = "../flink_server/flink-coreflow/src/main/resources/input_01/test03.txt"
    val stream01 = env.readTextFile(filePaths)
    val stream02 = env.readTextFile(filePaths)
    // stream01将与stream02连接并形成ConnectedStreams连接流
    var streamConnect = stream01.connect(stream02)
    // 当streamConnect调用flatMap函数的过程就称之为CoFlatMap操作
    val streamCoFlatMap = streamConnect.flatMap((x) => x.split(" "), (y) => y.split(" "))
    // 打印数据 -> (Sink)
    streamCoFlatMap.print()
    // 触发程序执行
    env.execute("CoFlatMapFlow")
  }

  /**
    * 定义SplitFlow方法
    * DataStream → SplitStream
    * 通常split()函数会与select()函数配合使用
    */
  def SplitFlow(): Unit = {
    // 加载初始数据 -> (Source)
    val filePaths = "../flink_server/flink-coreflow/src/main/resources/input_01/test03.txt"
    val stream = env.readTextFile(filePaths).flatMap(x => x.split(" "))
    // 调用split函数
    var streamSplit = stream.split(
      // 遍历每行数据,并校验values值与hadoop值相等,则表示条件成立
      values => ("hadoop".equals(values))
        // 将values值进行match模式匹配
      match {
        // 如果values条件为true,则将hadoop追加List集合中
        case true => List("hadoop")
        // 如果values条件为false,则将other追加List集合中
        case false => List("other")
      }
    )
    // 打印数据 -> (Sink)
    streamSplit.print()
    // 触发程序执行
    env.execute("SplitFlow")
  }

  /**
    * 定义SplitAndSelectFlow方法
    * SplitStream → DataStream
    * 通常select()函数会与split()函数配合使用
    */
  def SplitAndSelectFlow(): Unit = {
    // 加载初始数据 -> (Source)
    val filePaths = "../flink_server/flink-coreflow/src/main/resources/input_01/test03.txt"
    val stream = env.readTextFile(filePaths).flatMap(x => x.split(" "))
    // 调用split函数
    var streamSplit = stream.split(
      // 遍历每行数据,并校验values值与hadoop值相等,则表示条件成立
      values => ("hadoop".equals(values))
        // 将values值进行match模式匹配
      match {
        // 如果values条件为true,则将hadoop追加List集合中
        case true => List("hadoop")
        // 如果values条件为false,则将other追加List集合中
        case false => List("other")
      }
    )
    // 调用select函数
    val streamSelectHadoop = streamSplit.select("hadoop")
    val streamSelectOther = streamSplit.select("other")
    // 打印数据 -> (Sink)
    streamSelectHadoop.print()
    //    streamSelectOther.print()
    // 触发程序执行
    env.execute("SplitAndSelectFlow")
  }

  /**
    * 定义UnionFlow方法
    * DataStream → DataStream
    */
  def UnionFlow(): Unit = {
    // 加载初始数据 -> (Source)
    val filePath01 = "../flink_server/flink-coreflow/src/main/resources/input_01/test01.txt"
    val filePath02 = "../flink_server/flink-coreflow/src/main/resources/input_01/test03.txt"
    val stream01 = env.readTextFile(filePath01).flatMap(x => x.split(" "))
    val stream02 = env.readTextFile(filePath02).flatMap(x => x.split(" "))
    // 调用union函数
    val streamUnion = stream01.union(stream02)
    // 打印数据 -> (Sink)
    streamUnion.print()
    // 触发程序执行
    env.execute("UnionFlow")
  }

  /**
    * 定义KeyByFlow方法
    * DataStream → KeyedStream
    */
  def KeyByFlow(): Unit = {
    // 加载初始数据 -> (Source)
    val filePath = "../flink_server/flink-coreflow/src/main/resources/input_01/test03.txt"
    val stream = env.readTextFile(filePath).flatMap(x => x.split(" ")).map(x => (x, 1L))
    // 调用keyBy函数
    val streamkeyBy = stream.keyBy(0)
    // 打印数据 -> (Sink)
    streamkeyBy.print()
    // 触发程序执行
    env.execute("KeyByFlow")
  }

  /**
    * 定义ReduceFlow方法
    * KeyedStream → DataStream
    */
  def ReduceFlow(): Unit = {
    // 加载初始数据 -> (Source)
    val filePath = "../flink_server/flink-coreflow/src/main/resources/input_01/test03.txt"
    val stream = env.readTextFile(filePath).flatMap(x => x.split(" ")).map(x => (x, 1L))
    // 调用keyBy函数
    val streamkeyBy = stream.keyBy(0)
    // 调用reduce函数
    val streamReduce = streamkeyBy.reduce((item1, item2) => (item1._1, item1._2 + item2._2))
    // 打印数据 -> (Sink)
    streamReduce.print()
    // 触发程序执行
    env.execute("ReduceFlow")
  }

  /**
    * 定义FoldFlow方法
    * KeyedStream → DataStream
    */
  def FoldFlow(): Unit = {
    // 加载初始数据 -> (Source)
    val filePath = "../flink_server/flink-coreflow/src/main/resources/input_01/test03.txt"
    // 依次调用flatMap函数 -> map函数 -> keyBy函数
    val streamkeyBy = env.readTextFile(filePath).flatMap(x => x.split(" ")).map(x => (x, 1)).keyBy(0)
    // 调用fold函数
    val streamReduceFold = streamkeyBy.fold(100)((x, y) => (x + y._2))
    // 打印数据 -> (Sink)
    streamReduceFold.print()
    // 触发程序执行
    env.execute("FoldFlow")
  }

  /**
    * 定义AggregationsFlow方法
    * KeyedStream → DataStream
    */
  def AggregationsFlow(): Unit = {
    // 加载初始数据 -> (Source)
    val filePath = "../flink_server/flink-coreflow/src/main/resources/input_01/test02.txt"
    // 依次调用map函数 ->  keyBy函数
    val streamkeyBy = env.readTextFile(filePath).map(item => (item.split(" ")(0), item.split(" ")(1).toLong)).keyBy(0)
    // 调用sum函数
    val streamReduceAggregations = streamkeyBy.sum(1)
    // 打印数据 -> (Sink)
    streamReduceAggregations.print()
    // 触发程序执行
    env.execute("AggregationsFlow")
  }

}