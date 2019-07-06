package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.api.windowing.time.Time

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
  * WindowsFlow
  * <p>
  */

object WindowsFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用countWindowFlow方法
  countWindowFlow()

  // 调用countWindowsFlow方法
  countWindowsFlow()

  // 调用TimeWindowFlow方法
  TimeWindowFlow()

  // 调用SlidingEventTimeWindowsFlow方法
  SlidingEventTimeWindowsFlow()

  // 调用WindowReduceFlow方法
  WindowReduceFlow()

  // 调用WindowFoldFlow方法
  WindowFoldFlow()

  // 调用aggregationOnWindowFlow方法
  aggregationOnWindowFlow()

  /**
    * 定义countWindowFlow方法
    */
  def countWindowFlow(): Unit = {
    // 监听端口并加载初始数据 -> (Source)
    val stream = env.socketTextStream("systemhub", 9999)
    // 对stream进行处理并按key聚合
    val streamKeyBy = stream.map(x => (x, 1L)).keyBy(0)

    /**
      * 引入滚动窗口
      * 参数5即表示5个相同key的元素计算一次
      * 注意 : CountWindow的window_size指的是相同Key的元素的个数,不是输入的所有元素的总数.
      */
    val streamWindow = streamKeyBy.countWindow(5)
    // 将聚合数据写入文件
    val streamReduce = streamWindow.reduce((x, y) => (x._1, x._2 + y._2))
    // 打印数据 -> (Sink)
    streamReduce.print()
    // 触发程序执行
    env.execute("countWindowFlow")
  }

  /**
    * 定义countWindowsFlow方法
    */
  def countWindowsFlow(): Unit = {
    // 监听端口并加载初始数据 -> (Source)
    val stream = env.socketTextStream("systemhub", 9999)
    // 对stream进行处理并按key聚合
    val streamKeyBy = stream.map(x => (x, 1L)).keyBy(0)
    /**
      * 引入滑动窗口
      * 每收到两个相同key的数据就计算一次,每一次计算的window范围是5个元素.
      */
    val streamWindow = streamKeyBy.countWindow(5, 2)
    // 将聚合数据写入文件
    val streamReduce = streamWindow.reduce((x, y) => (x._1, x._2 + y._2))
    // 打印数据 -> (Sink)
    streamReduce.print()
    // 触发程序执行
    env.execute("countWindowsFlow")
  }

  /**
    * 定义TimeWindowFlow方法
    */
  def TimeWindowFlow(): Unit = {
    // 监听端口并加载初始数据 -> (Source)
    val stream = env.socketTextStream("systemhub", 9999)
    // 对stream进行处理并按key聚合
    val streamKeyBy = stream.map(x => (x, 1L)).keyBy(0)
    /**
      * 引入滚动时间窗口
      * 时间间隔,可以通过`Time.milliseconds(x)`,`Time.seconds(x)`,`Time.minutes(x)`等其中一个来指定.
      */
    val streamTimeWindow = streamKeyBy.timeWindow(Time.seconds(5))
    // 将聚合数据写入文件
    val streamReduce = streamTimeWindow.reduce((x, y) => (x._1, x._2 + y._2))
    // 打印数据 -> (Sink)
    streamReduce.print()
    // 触发程序执行
    env.execute("TimeWindowFlow")
  }

  /**
    * 定义SlidingEventTimeWindowsFlow方法
    */
  def SlidingEventTimeWindowsFlow(): Unit = {
    // 监听端口并加载初始数据 -> (Source)
    val stream = env.socketTextStream("systemhub", 9999)
    // 对stream进行处理并按key聚合
    val streamKeyBy = stream.map(x => (x, 1L)).keyBy(0)
    /**
      * 引入滑动时间窗口
      * 窗口每2s就计算一次,每一次计算的window范围是10s内的所有元素.
      * 时间间隔,可以通过`Time.milliseconds(x)`,`Time.seconds(x)`,`Time.minutes(x)`等其中一个来指定.
      */
    val streamWindows = streamKeyBy.timeWindow(Time.seconds(10), Time.seconds(2))
    // 将聚合数据写入文件
    val streamReduce = streamWindows.reduce((x, y) => (x._1, x._2 + y._2))
    // 打印数据 -> (Sink)
    streamReduce.print()
    // 触发程序执行
    env.execute("SlidingEventTimeWindowsFlow")
  }

  /**
    * 定义WindowReduceFlow方法
    */
  def WindowReduceFlow(): Unit = {
    // 监听端口并加载初始数据 -> (Source)
    val stream = env.socketTextStream("systemhub", 9999)
    // 对stream进行处理并按key聚合
    val streamKeyBy = stream.map(x => (x, 1L)).keyBy(0)
    /**
      * 引入滑动时间窗口
      * 窗口每2s就计算一次,每一次计算的window范围是10s内的所有元素.
      * 时间间隔,可以通过`Time.milliseconds(x)`,`Time.seconds(x)`,`Time.minutes(x)`等其中一个来指定.
      */
    val streamWindows = streamKeyBy.timeWindow(Time.seconds(10), Time.seconds(2))
    // 将聚合数据写入文件
    val streamReduce = streamWindows.reduce((x, y) => (x._1, x._2 + y._2))
    // 打印数据 -> (Sink)
    streamReduce.print()
    // 触发程序执行
    env.execute("WindowReduceFlow")
  }

  /**
    * 定义WindowFoldFlow方法
    */
  def WindowFoldFlow(): Unit = {
    // 监听端口并加载初始数据 -> (Source)
    val stream = env.socketTextStream("systemhub", 9999, '\n', 3)
    // 对stream进行处理并按key聚合
    val streamKeyBy = stream.map(x => (x, 1)).keyBy(0)
    /**
      * 引入滚动时间窗口
      * 时间间隔,可以通过`Time.milliseconds(x)`,`Time.seconds(x)`,`Time.minutes(x)`等其中一个来指定.
      */
    val streamTimeWindow = streamKeyBy.timeWindow(Time.seconds(5))
    // 调用fold函数操作
    val streamFold = streamTimeWindow.fold(100) {
      (x, y) => x + y._2
    }
    // 打印数据 -> (Sink)
    streamFold.print()
    // 触发程序执行
    env.execute("WindowFoldFlow")
  }

  /**
    * 定义aggregationOnWindowFlow方法
    */
  def aggregationOnWindowFlow(): Unit = {
    // 监听端口并加载初始数据 -> (Source)
    val stream = env.socketTextStream("systemhub", 9999)
    // 对stream进行处理并按key聚合
    val streamKeyBy = stream.map(item => (item.split(" ")(0), item.split(" ")(1))).keyBy(0)
    // 引入滚动窗口
    val streamWindow = streamKeyBy.timeWindow(Time.seconds(5))
    // 执行聚合操作
    val streamMax = streamWindow.max(1)
    // 打印数据 -> (Sink)
    streamMax.print()
    // 触发程序执行
    env.execute("aggregationOnWindowFlow")
  }
}