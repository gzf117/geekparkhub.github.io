package com.geekparkhub.core.flink.workflow

import org.apache.flink.streaming.api.TimeCharacteristic
import org.apache.flink.streaming.api.functions.timestamps.BoundedOutOfOrdernessTimestampExtractor
import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.api.windowing.assigners.{EventTimeSessionWindows, SlidingEventTimeWindows, TumblingEventTimeWindows}
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
  * EvnetTimeWindowFlow
  * <p>
  */
object EvnetTimeWindowFlow extends App {

  // 创建执行环境
  val env = StreamExecutionEnvironment.getExecutionEnvironment

  // 调用watermarkFlow方法
  watermarkFlow()

  // 调用TumblingEventTimeWindowsFlow方法
  TumblingEventTimeWindowsFlow()

  // 调用SlidingEventTimeWindowsFlow方法
  SlidingEventTimeWindowsFlow()

  // 调用EventTimeSessionWindowsFlow方法
  EventTimeSessionWindowsFlow()

  /**
    * 定义watermarkFlow方法
    * 分配时间戳与Watermarks
    */
  def watermarkFlow(): Unit = {
    // 设置时间特征为EventTime,即表示从调用时开始赋予env创建的每个stream追加时间特征
    env.setStreamTimeCharacteristic(TimeCharacteristic.EventTime)
    // 设置时间戳
    val stream = env.socketTextStream("systemhub", 9999)
      .assignTimestampsAndWatermarks(new BoundedOutOfOrdernessTimestampExtractor[String](Time.milliseconds(0)) {
        override def extractTimestamp(time: String): Long = {
          // / EventTime是日志生成时间,从日志中解析EventTime
          val eventTime = time.split(" ")(0).toLong
          println("eventTime = " + eventTime)
          eventTime
        }
      })
  }

  /**
    * 定义TumblingEventTimeWindowsFlow方法
    * 定义 滚动窗口 方法
    */
  def TumblingEventTimeWindowsFlow(): Unit = {
    // 设置时间特征为EventTime,即表示从调用时开始赋予env创建的每个stream追加时间特征
    env.setStreamTimeCharacteristic(TimeCharacteristic.EventTime)
    // 设置时间戳,对stream进行处理并按key聚合
    val stream = env.socketTextStream("systemhub", 9999)
      .assignTimestampsAndWatermarks(new BoundedOutOfOrdernessTimestampExtractor[String](Time.milliseconds(3000)) {
        override def extractTimestamp(time: String): Long = {
          // / EventTime是日志生成时间,从日志中解析EventTime
          val eventTime = time.split(" ")(0).toLong
          println("eventTime = " + eventTime)
          eventTime
        }
      }).map(x => (x.split(" ")(1), (1L))).keyBy(0)
    // 引入滚动窗口,设置每5秒开启一个窗口
    val streamWindow = stream.window(TumblingEventTimeWindows.of(Time.seconds(5)))
    // 执行聚合操作
    val streamReduce = streamWindow.reduce((x, y) => (x._1, x._2 + y._2))
    // 打印数据 -> (Sink)
    streamReduce.print()
    // 触发程序执行
    env.execute("TumblingEventTimeWindowsFlow")
  }

  /**
    * 定义SlidingEventTimeWindowsFlow方法
    * 定义 滑动窗口 方法
    */
  def SlidingEventTimeWindowsFlow(): Unit = {
    // 设置时间特征为EventTime,即表示从调用时开始赋予env创建的每个stream追加时间特征
    env.setStreamTimeCharacteristic(TimeCharacteristic.EventTime)
    // 设置时间戳,对stream进行处理并按key聚合
    val stream = env.socketTextStream("systemhub", 9999)
      .assignTimestampsAndWatermarks(new BoundedOutOfOrdernessTimestampExtractor[String](Time.milliseconds(3000)) {
        override def extractTimestamp(time: String): Long = {
          // / EventTime是日志生成时间,从日志中解析EventTime
          val eventTime = time.split(" ")(0).toLong
          println("eventTime = " + eventTime)
          eventTime
        }
      }).map(x => (x.split(" ")(1), (1L))).keyBy(0)
    /**
      * 引入滑动窗口,设置窗口大小为10秒,并设置窗口滑动过程为5秒
      * 即表示5秒触发一次窗口执行,计算范围为10秒
      */
    val streamWindow = stream.window(SlidingEventTimeWindows.of(Time.seconds(10), Time.seconds(5)))
    // 执行聚合操作
    val streamReduce = streamWindow.reduce((x, y) => (x._1, x._2 + y._2))
    // 打印数据 -> (Sink)
    streamReduce.print()
    // 触发程序执行
    env.execute("SlidingEventTimeWindowsFlow")
  }

  /**
    * 定义EventTimeSessionWindowsFlow方法
    * 定义 会话窗口 方法
    */
  def EventTimeSessionWindowsFlow(): Unit = {
    // 设置时间特征为EventTime,即表示从调用时开始赋予env创建的每个stream追加时间特征
    env.setStreamTimeCharacteristic(TimeCharacteristic.EventTime)
    // 设置时间戳,对stream进行处理并按key聚合
    val stream = env.socketTextStream("systemhub", 9999)
      .assignTimestampsAndWatermarks(new BoundedOutOfOrdernessTimestampExtractor[String](Time.milliseconds(3000)) {
        override def extractTimestamp(time: String): Long = {
          // / EventTime是日志生成时间,从日志中解析EventTime
          val eventTime = time.split(" ")(0).toLong
          println("eventTime = " + eventTime)
          eventTime
        }
      }).map(x => (x.split(" ")(1), (1L))).keyBy(0)
    /**
      * 引入会话窗口
      * 设置5秒触发一次窗口执行,准确的说当前5秒加上3秒等于8秒,既每8秒才触发对应的窗口执行
      */
    val streamWindow = stream.window(EventTimeSessionWindows.withGap(Time.seconds(5)))
    // 执行聚合操作
    val streamReduce = streamWindow.reduce((x, y) => (x._1, x._2 + y._2))
    // 打印数据 -> (Sink)
    streamReduce.print()
    // 触发程序执行
    env.execute("EventTimeSessionWindowsFlow")
  }
}