package com.geekparkhub.core.flink.workflow

import org.apache.flink.api.java.io.TextInputFormat
import org.apache.flink.core.fs.Path
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
  * FlinkSourceFlow
  * <p>
  */

object FlinkSourceFlow extends App {

  // 调用readTextFileFlow方法
  readTextFileFlow()
  println()

  // 调用readFileFlow方法
  readFileFlow()

  // 调用socketTextFlow方法
  socketTextFlow()

  // 调用fromCollectionFlow方法
  fromCollectionFlow()

  // 调用fromCollectionIteratorFlow方法
  fromCollectionIteratorFlow()

  // 调用fromElementsFlow方法
  fromElementsFlow()

  // 调用generateSequenceFlow方法
  generateSequenceFlow()

  /**
    * 定义 readTextFile方法
    * 读取文本文件
    */
  def readTextFileFlow(): Unit = {
    // 创建执行环境
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    // 加载初始数据 -> (Source)
    val filePaths = "../flink_server/flink-coreflow/src/main/resources/input_01/test01.txt"
    val stream = env.readTextFile(filePaths)
    // 打印数据 -> (Sink)
    stream.print()
    // 触发程序执行
    env.execute("readTextFileFlow")
  }

  /**
    * 定义 readFileFlow方法
    * 指定文件格式读取文件
    */
  def readFileFlow(): Unit = {
    // 创建执行环境
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    // 创建文件路径
    val paths = "../flink_server/flink-coreflow/src/main/resources/input_01/test02.txt"
    val path = new Path(paths)
    // 加载初始数据 -> (Source)
    val filePath = "../flink_server/flink-coreflow/src/main/resources/input_01/test02.txt"
    val stream = env.readFile(new TextInputFormat(path), filePath)
    // 打印数据 -> (Sink)
    stream.print()
    // 触发程序执行
    env.execute("readFileFlow")
  }

  /**
    * 定义 socketTextFlow方法
    * 从Socket中读取信息,元素可以用分隔符分开
    */
  def socketTextFlow(): Unit = {
    // 创建执行环境
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    // 加载初始数据 -> (Source)
    val stream = env.socketTextStream("systemhub", 9999)
    // 打印数据 -> (Sink)
    stream.print()
    // 触发程序执行
    env.execute("socketTextFlow")
  }

  /**
    * 定义 fromCollectionFlow 方法
    * 从集合中创建一个数据流
    */
  def fromCollectionFlow(): Unit = {
    // 创建执行环境
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    // 创建集合,集合中所有元素类型需一致
    val list = List(1, 2, 3, 4)
    // 加载初始数据 -> (Source)
    val stream = env.fromCollection(list)
    // 打印数据 -> (Sink)
    stream.print()
    // 触发程序执行
    env.execute("fromCollectionFlow")
  }

  /**
    * 定义 fromCollectionIteratorFlow 方法
    * 从集合中创建一个数据流
    */
  def fromCollectionIteratorFlow(): Unit = {
    // 创建执行环境
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    // 创建集合,集合中所有元素类型需一致
    val iterator = Iterator(1, 2, 3, 4)
    // 加载初始数据 -> (Source)
    val stream = env.fromCollection(iterator)
    // 打印数据 -> (Sink)
    stream.print()
    // 触发程序执行
    env.execute("fromCollectionIteratorFlow")
  }

  /**
    * 定义 fromElementsFlow 方法
    * 从一个给定的对象序列中创建一个数据流,所有的对象必须是相同类型
    */
  def fromElementsFlow(): Unit = {
    // 创建执行环境
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    // 创建集合,集合中所有元素类型需一致
    val list = List(1, 2, 3, 4)
    // 加载初始数据 -> (Source)
    val stream = env.fromElements(list)
    // 打印数据 -> (Sink)
    stream.print()
    // 触发程序执行
    env.execute("fromElementsFlow")
  }

  /**
    * 定义 generateSequenceFlow 方法
    */
  def generateSequenceFlow(): Unit = {
    // 创建执行环境
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    // 创建初始数据 -> (Source)
    val stream = env.generateSequence(1, 20)
    // 打印数据 -> (Sink)
    stream.print()
    // 触发程序执行
    env.execute("generateSequenceFlow")
  }
}